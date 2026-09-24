"""Audit every published HTML file and enforce release-blocking invariants."""
from __future__ import annotations
import ast
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
try:
    from scripts.catalog import collect
    from scripts.home import render_home
    from scripts.migrate_legacy import ROOT, template_paths
except ModuleNotFoundError:
    from catalog import collect
    from home import render_home
    from migrate_legacy import ROOT, template_paths

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.scripts = []
        self.script = None
        self.stack = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('input', 'select', 'textarea') and 'label' in self.stack: attrs['_implicit_label'] = True
        if tag not in VOID: self.stack.append(tag)
        self.tags.append((tag, attrs, self.getpos()[0]))
        if tag == 'script': self.script = [attrs, '', self.getpos()[0]]
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_data(self, data):
        if self.script is not None: self.script[1] += data
    def handle_endtag(self, tag):
        if tag in self.stack:
            index = len(self.stack) - 1 - self.stack[::-1].index(tag)
            del self.stack[index:]
        if tag == 'script' and self.script is not None:
            self.scripts.append(self.script)
            self.script = None

def semantic_issues(page: Page) -> list[dict]:
    """Static, authored names/references. Dynamic content still needs browser testing."""
    issues = []
    targets = {attrs['id']: (tag, attrs) for tag, attrs, _ in page.tags if attrs.get('id')}
    label_for = {attrs.get('for') for tag, attrs, _ in page.tags if tag == 'label'}
    def add(line, code, detail):
        issues.append({'line': line, 'code': code, 'detail': detail})
    for tag, attrs, line in page.tags:
        for attribute in ('aria-labelledby', 'aria-describedby', 'aria-controls'):
            for target in attrs.get(attribute, '').split():
                if target not in targets: add(line, 'broken-id-reference', f'{attribute}={target}')
        if tag == 'label' and attrs.get('for'):
            target = targets.get(attrs['for'])
            if target is None:
                add(line, 'broken-label-reference', attrs['for'])
            elif target[0] not in ('button', 'input', 'meter', 'output', 'progress', 'select', 'textarea') or target[1].get('type') == 'hidden':
                add(line, 'invalid-label-target', attrs['for'])
        if tag in ('input', 'select', 'textarea') and attrs.get('type') not in ('hidden', 'submit', 'button', 'reset'):
            if not (attrs.get('aria-label', '').strip() or attrs.get('aria-labelledby', '').strip() or (attrs.get('id') and attrs['id'] in label_for) or attrs.get('_implicit_label')):
                add(line, 'control-label', 'An authored accessible name is required')
    return issues


def inspect(root: Path = ROOT) -> dict:
    errors = []
    warnings = []
    scripts = []
    paths = template_paths(root) + [root / name for name in ('index.html', 'catalog.html', 'preview.html', 'explore.html') if (root / name).exists()]
    def issue(bucket, path, line, code, detail):
        bucket.append({'path': path.relative_to(root).as_posix(), 'line': line, 'code': code, 'detail': detail})
    for path in paths:
        text = path.read_text(encoding='utf-8')
        page = Page(); page.feed(text)
        tags = page.tags
        for required, found in [('doctype', bool(re.search(r'<!doctype\s+html', text, re.I))),
            ('document-language', any(tag == 'html' and a.get('lang') for tag, a, _ in tags)),
            ('title', any(tag == 'title' for tag, _, _ in tags)),
            ('viewport', any(tag == 'meta' and a.get('name') == 'viewport' for tag, a, _ in tags))]:
            if not found: issue(errors, path, 1, 'missing-' + required, 'Required document metadata is missing')
        ids = Counter(a['id'] for _, a, _ in tags if a.get('id'))
        for value, count in ids.items():
            if count > 1: issue(errors, path, 1, 'duplicate-id', f'{value}: {count} occurrences')
        for finding in semantic_issues(page):
            issue(errors, path, finding['line'], finding['code'], finding['detail'])
        for tag, attrs, line in tags:
            for attr in ('href', 'src'):
                value = attrs.get(attr)
                if not value: continue
                parsed = urlsplit(value)
                if parsed.scheme or parsed.netloc: continue
                if not parsed.path: continue
                if parsed.path.startswith('/'):
                    issue(errors, path, line, 'root-relative-path', value); continue
                target = (path.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(root.resolve()): issue(errors, path, line, 'path-escape', value)
                elif not target.exists(): issue(errors, path, line, 'missing-local-file', value)
            if tag == 'script' and 'tailwindcss-browser.js' in attrs.get('src', ''):
                issue(errors, path, line, 'browser-compiler', attrs['src'])
            if tag == 'style' and attrs.get('type') == 'text/tailwindcss': issue(errors, path, line, 'uncompiled-style', 'Compile Tailwind directives before publishing')
            if tag == 'img' and 'alt' not in attrs and ':alt' not in attrs and 'x-bind:alt' not in attrs:
                issue(warnings, path, line, 'image-alt-review', 'Image has no authored alt attribute')
            if tag == 'a' and attrs.get('href') == '#': issue(warnings, path, line, 'placeholder-link', 'Demo destination must be connected before production')
            if tag == 'script' and urlsplit(attrs.get('src', '')).scheme in ('http', 'https'):
                issue(warnings, path, line, 'external-script', attrs['src'])
        for attrs, body, line in page.scripts:
            if attrs.get('src') or not body.strip(): continue
            if attrs.get('type') == 'application/ld+json':
                try: json.loads(body)
                except json.JSONDecodeError as error: issue(errors, path, line, 'invalid-jsonld', str(error))
            elif attrs.get('type') != 'module': scripts.append({'path': path.relative_to(root).as_posix(), 'line': line, 'source': body})
    for path in list(root.glob('*.py')) + list((root / 'scripts').glob('*.py')):
        try: ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
        except SyntaxError as error: issue(errors, path, error.lineno or 1, 'python-syntax', error.msg)
        if path.name.startswith('generate') and re.search(r'subprocess\.(run|call|check_call)\s*\(\s*\[\s*[\'"]git', path.read_text()):
            issue(errors, path, 1, 'generator-git-write', 'Generators must not automatically modify Git')
    checker = "const fs=require('node:fs'),vm=require('node:vm');const result=[];for(const s of JSON.parse(fs.readFileSync(0,'utf8'))){try{new vm.Script(s.source,{filename:s.path})}catch(e){result.push({path:s.path,line:s.line,code:'javascript-syntax',detail:e.message})}}console.log(JSON.stringify(result))"
    checked = subprocess.run(['node', '-e', checker], input=json.dumps(scripts), text=True, capture_output=True, check=True)
    errors.extend(json.loads(checked.stdout))
    modules = sorted(list((root / 'assets/js').glob('*.mjs')) + list((root / 'assets/js').glob('*.js')) + list((root / 'src/js').glob('*.js')))
    for module in modules:
        checked_module = subprocess.run(['node', '--check', str(module)], text=True, capture_output=True)
        if checked_module.returncode: issue(errors, module, 1, 'javascript-module-syntax', checked_module.stderr.strip())
    data = collect(root)
    home_source = root / 'src/home.html'
    if home_source.exists() and (root / 'index.html').read_text(encoding='utf-8') != render_home(data, home_source.read_text(encoding='utf-8')):
        issue(errors, root / 'index.html', 1, 'stale-home', 'Run npm run build. Edit src/home.html without redesigning the category homepage.')
    if (root / 'templates.json').exists():
        if json.loads((root / 'templates.json').read_text(encoding='utf-8')) != data:
            issue(errors, root / 'templates.json', 1, 'stale-catalog', 'Run npm run build')
    else: issue(errors, root / 'templates.json', 1, 'missing-catalog', 'Run npm run build')
    sitemap = root / 'sitemap.xml'
    try:
        entries = ElementTree.fromstring(sitemap.read_text()).findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        if len(entries) != data['total'] + 3: issue(errors, sitemap, 1, 'sitemap-count', 'Sitemap does not cover the catalog')
    except (OSError, ElementTree.ParseError) as error: issue(errors, sitemap, 1, 'sitemap-invalid', str(error))
    return {'schemaVersion': 1, 'htmlFiles': len(paths), 'templates': data['total'], 'categories': len(data['categories']),
            'javascriptFilesParsed': len(modules), 'inlineScriptsParsed': len(scripts), 'errors': errors, 'warnings': warnings,
            'warningCounts': dict(Counter(item['code'] for item in warnings))}

def main():
    report = inspect()
    output = ROOT / 'audit-results'; output.mkdir(exist_ok=True)
    (output / 'static.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in ('warnings', 'errors')}, indent=2))
    for item in report['errors'][:100]: print(f"ERROR {item['path']}:{item['line']} [{item['code']}] {item['detail']}")
    print(f"{len(report['errors'])} errors; {len(report['warnings'])} review items. Full details: audit-results/static.json")
    return bool(report['errors'])

if __name__ == '__main__': sys.exit(main())
