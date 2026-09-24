"""Generate the catalog and sitemap from HTML, never from assumed ID ranges."""
from __future__ import annotations
from collections import Counter
from html import escape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from urllib.parse import urlsplit
from xml.etree.ElementTree import Element, SubElement, tostring
try:
    from scripts.migrate_legacy import ROOT, template_paths
except ModuleNotFoundError:
    from migrate_legacy import ROOT, template_paths

CATEGORIES = {
    'nav': ('navigation', 'Navigation'), 'hero': ('hero', 'Hero sections'),
    'feat': ('features', 'Features'), 'content': ('content', 'Content'),
    'cta': ('cta', 'Calls to action'), 'price': ('pricing', 'Pricing'),
    'test': ('testimonials', 'Testimonials'), 'team': ('team', 'Team'),
    'gallery': ('gallery', 'Gallery'), 'form': ('forms', 'Forms'),
    'card': ('cards', 'Cards'), 'list': ('lists', 'Lists & tables'),
    'modal': ('modals', 'Modals & dialogs'), 'notification': ('notifications', 'Notifications'),
    'footer': ('footers', 'Footers'), 'auth': ('authentication', 'Authentication'),
    'dashboard': ('dashboard', 'Dashboards'), 'ecommerce': ('ecommerce', 'E-commerce'),
    'blog': ('blog', 'Blog'), 'landing': ('landing', 'Landing pages'),
    'community': ('community', 'Community'),
}
DEFAULT_SITE = 'https://stephen-taipei.github.io/awesome-tailwind-ui-templates-1000/'


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ''
        self.description = ''
        self.in_title = False
        self.interactive = False
        self.locales = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title': self.in_title = True
        if tag == 'meta' and attrs.get('name', '').lower() == 'description':
            self.description = attrs.get('content', '')
        if tag == 'script' and not attrs.get('src', '').endswith('template-runtime.js'):
            if attrs.get('type') != 'application/ld+json': self.interactive = True
        if 'x-data' in attrs or any(key.startswith('@') or key.startswith('on') for key in attrs):
            self.interactive = True
        if any(key.startswith('data-i18n') for key in attrs): self.locales = True

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_title: self.title += data


def collect(root: Path = ROOT) -> dict:
    templates = []
    seen = set()
    labels = {}
    for path in template_paths(root):
        template_id = path.parent.name if path.stem == 'index' else path.stem
        if template_id in seen: raise ValueError(f'Duplicate template ID: {template_id}')
        seen.add(template_id)
        prefix = template_id.rsplit('-', 1)[0]
        if prefix not in CATEGORIES: raise ValueError(f'Unmapped category prefix: {prefix} ({path})')
        category, label = CATEGORIES[prefix]
        labels[category] = label
        parser = Metadata()
        parser.feed(path.read_text(encoding='utf-8'))
        title = re.sub(r'\s*(?:\|| - )\s*(?:Awesome )?Tailwind UI Templates.*$', '', parser.title.strip(), flags=re.I)
        title = re.sub(r'^' + re.escape(template_id) + r'\s*[:\-]\s*', '', title, flags=re.I)
        templates.append({'id': template_id, 'title': title or template_id,
                          'description': parser.description.strip(), 'category': category,
                          'path': path.relative_to(root).as_posix(),
                          'interactive': parser.interactive, 'i18n': parser.locales})
    counts = Counter(t['category'] for t in templates)
    categories = [{'id': key, 'name': labels[key], 'count': counts[key]} for key in labels]
    categories.sort(key=lambda item: list(dict(CATEGORIES.values())).index(item['id']))
    templates.sort(key=lambda item: (item['category'], int(item['id'].rsplit('-', 1)[1])))
    return {'schemaVersion': 1, 'total': len(templates), 'categories': categories, 'templates': templates}


def site_url() -> str:
    url = os.environ.get('SITE_URL', DEFAULT_SITE).rstrip('/') + '/'
    parsed = urlsplit(url)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError('SITE_URL must be an absolute http(s) site root without query or fragment')
    return url


def render_catalog(data: dict) -> str:
    sections = []
    for category in data['categories']:
        links = ''.join(f'<li><a href="{escape(t["path"], quote=True)}">{escape(t["id"])} — {escape(t["title"])}</a></li>'
                        for t in data['templates'] if t['category'] == category['id'])
        sections.append(f'<section id="{category["id"]}"><h2>{escape(category["name"])} <span>({category["count"]})</span></h2><ul class="directory-list">{links}</ul></section>')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>All {data['total']:,} templates — Tailwind Atlas</title><meta name="description" content="Complete static directory of every template. No JavaScript required.">
<link rel="stylesheet" href="assets/css/gallery.css"><link rel="canonical" href="{escape(site_url(), quote=True)}catalog.html"></head>
<body><a class="skip-link" href="#catalog-content">Skip to templates</a><header class="site-header"><div class="header-inner"><a class="brand" href="index.html">Tailwind Atlas <span>by Stephen</span></a><a href="index.html">Search the collection ↗</a></div></header>
<main id="catalog-content" class="directory wrap"><p class="eyebrow">THE COMPLETE INDEX</p><h1>Every template. One place.</h1><p>{data['total']:,} HTML examples across {len(data['categories'])} categories. These are UI demos, not finished applications.</p>
{''.join(sections)}</main><footer class="site-footer wrap"><a href="index.html">Back to gallery</a></footer></body></html>\n'''


def main() -> None:
    data = collect()
    (ROOT / 'templates.json').write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    (ROOT / 'catalog.html').write_text(render_catalog(data), encoding='utf-8')
    namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    xml = Element('urlset', xmlns=namespace)
    for path in ['', 'catalog.html'] + [item['path'] for item in data['templates']]:
        SubElement(SubElement(xml, 'url'), 'loc').text = site_url() + path
    (ROOT / 'sitemap.xml').write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + tostring(xml, encoding='utf-8') + b'\n')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {site_url()}sitemap.xml\n', encoding='utf-8')
    print(f'Catalog: {data["total"]} templates, {len(data["categories"])} categories')


if __name__ == '__main__': main()
