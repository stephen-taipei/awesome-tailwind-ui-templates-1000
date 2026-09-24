"""One-time, idempotent migration of known legacy dependencies. No network or Git writes."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
try:
    from scripts.accessibility import repair
except ModuleNotFoundError:
    from accessibility import repair

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOTS = ('templates', 'cards', 'forms', 'lists')


def template_paths(root: Path = ROOT) -> list[Path]:
    return sorted(p for directory in TEMPLATE_ROOTS for p in (root / directory).rglob('*.html'))


def asset_path(path: Path, asset: str, root: Path = ROOT) -> str:
    return Path(os.path.relpath(root / asset, path.parent)).as_posix()


def config_to_css(match: re.Match) -> str:
    script = match.group(1)
    wrapper = re.fullmatch(
        r"\s*tailwind\.config\s*=\s*\{\s*theme\s*:\s*\{\s*extend\s*:\s*\{\s*colors\s*:\s*\{(.*?)\}\s*,?\s*\}\s*,?\s*\}\s*,?\s*\}\s*;?\s*",
        script, re.S,
    )
    if not wrapper:
        raise ValueError('Unknown legacy Tailwind config; review manually instead of evaluating JavaScript')
    block = wrapper.group(1)
    entry = re.compile(r"\s*['\"]?([\w-]+)['\"]?\s*:\s*(['\"])([^'\";{}<>]+)\2\s*,?\s*")
    variables = []
    pos = 0
    while pos < len(block):
        if not block[pos:].strip():
            break
        item = entry.match(block, pos)
        if not item:
            raise ValueError('Unsupported color definition in legacy config')
        variables.append(f'  --color-{item[1]}: {item[3]};')
        pos = item.end()
    return '<style>\n:root {\n' + '\n'.join(variables) + '\n}\n</style>'


def migrate_html(text: str, path: Path, root: Path = ROOT) -> str:
    css = asset_path(path, 'assets/css/tailwind.css', root)
    alpine = asset_path(path, 'assets/vendor/alpine.min.js', root)
    runtime = asset_path(path, 'assets/js/template-runtime.js', root)
    text = re.sub(r'<script\s+src=["\']https://stephen\.taipei/tailwindcss-browser\.js["\']\s*>\s*</script>',
                  f'<link rel="stylesheet" href="{css}">', text, flags=re.I)
    text = re.sub(r'<link\b[^>]*href=["\']/vendor/tailwind/tailwind\.min\.css["\'][^>]*>',
                  f'<link rel="stylesheet" href="{css}">', text, flags=re.I)
    text = text.replace('/vendor/misc/alpine.min.js', alpine)
    text = re.sub(r'<script>\s*(tailwind\.config\s*=.*?)</script>', config_to_css, text, flags=re.S)
    def theme_style(match: re.Match) -> str:
        body = match[1]
        if re.search(r'@(apply|utility|variant|source|import)\b', body):
            raise ValueError(f'{path}: this style requires explicit build-time processing')
        return '<style>' + re.sub(r'@theme\s*\{', ':root {', body) + '</style>'
    text = re.sub(r'<style\s+type=["\']text/tailwindcss["\']\s*>(.*?)</style>', theme_style, text, flags=re.S)
    text = text.replace('<!-- Tailwind CSS v4 via stephen.taipei CDN -->', '<!-- Precompiled Tailwind CSS v4; run npm run build after editing classes. -->')
    text = text.replace('https://source.unsplash.com/random/400x400?sig=${item}',
                        'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=400&q=80&sig=${item}')
    if 'assets/js/template-runtime.js' not in text:
        text = text.replace('</body>', f'  <script src="{runtime}" defer></script>\n</body>')
    if 'data-i18n' in text and 'src/js/i18n.js' not in text:
        translator = asset_path(path, 'src/js/i18n.js', root)
        text = text.replace('</body>', f'  <script type="module" src="{translator}"></script>\n</body>')
    if path.name == 'landing-040.html':
        text = text.replace('.innerHTML =', '.textContent =')
    if path.name == 'price-003.html':
        text = text.replace('@click="annual = !annual">', '@click="annual = !annual" role="switch" :aria-checked="annual">')
        text = text.replace('<span class="sr-only">Use setting</span>', '<span class="sr-only">Yearly billing</span>')
    return repair(text)


def migrate_generators(root: Path) -> list[str]:
    changed = []
    for path in sorted(root.glob('generate*.py')):
        text = path.read_text(encoding='utf-8')
        match = re.search(r'^def (generate_and_push\w*)\(\):', text, flags=re.M)
        if not match or 'scripts.legacy' in text:
            continue
        variable = 'TEMPLATES_BATCH_10' if path.name == 'generate_final_part2.py' else ('ALL_TEMPLATES' if path.name == 'generate_final_part1.py' else 'TEMPLATES')
        text = text[:match.start()] + f'''def {match[1]}():
    """Generate into an explicit output directory; never stage, commit, or push."""
    from scripts.legacy import generate_templates
    generate_templates({variable}, BASE_HTML)


if __name__ == "__main__":
    {match[1]}()
'''
        path.write_text(text, encoding='utf-8')
        changed.append(path.name)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Write migration; otherwise report pending changes')
    args = parser.parse_args()
    pending = []
    for path in template_paths():
        before = path.read_text(encoding='utf-8')
        after = migrate_html(before, path)
        if before != after:
            pending.append(path.relative_to(ROOT).as_posix())
            if args.apply:
                path.write_text(after, encoding='utf-8')
    generators = migrate_generators(ROOT) if args.apply else []
    if args.apply:
        (ROOT / 'debug.log').unlink(missing_ok=True)
        (ROOT / 'news-sitemap.xml').unlink(missing_ok=True)
    print(json.dumps({'templates_changed': len(pending), 'generators_changed': generators, 'applied': args.apply}))


if __name__ == '__main__':
    main()
