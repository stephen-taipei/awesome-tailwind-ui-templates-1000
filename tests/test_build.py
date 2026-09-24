import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch
from scripts.accessibility import repair
from scripts.catalog import collect
from scripts.migrate_legacy import ROOT, migrate_html, template_paths
from scripts.legacy import generate_templates
from scripts.audit import Page

class BuildTests(unittest.TestCase):
    def test_inventory_is_deterministic_and_complete(self):
        data = collect()
        self.assertEqual(data, collect())
        self.assertEqual(data['total'], len(template_paths()))
        self.assertEqual(data['total'], len({item['id'] for item in data['templates']}))
        self.assertEqual(data, json.loads((ROOT / 'templates.json').read_text()))

    def test_migration_is_idempotent_for_every_template(self):
        for path in template_paths():
            text = path.read_text()
            self.assertEqual(text, migrate_html(text, path), str(path))

    def test_known_legacy_config_becomes_css_without_eval(self):
        source = "<script>tailwind.config = { theme: { extend: { colors: { primary: '#abcdef' } } } };</script>"
        migrated = migrate_html(source, ROOT / 'templates/x/example.html')
        self.assertIn('--color-primary: #abcdef;', migrated)
        self.assertNotIn('tailwind.config', migrated)
        with self.assertRaises(ValueError):
            migrate_html('<script>tailwind.config = evil()</script>', ROOT / 'templates/x/example.html')

    def test_relative_dependency_paths_survive_nested_hosting(self):
        source = '<html><script src="https://stephen.taipei/tailwindcss-browser.js"></script></html>'
        self.assertIn('../../assets/css/tailwind.css', migrate_html(source, ROOT / 'cards/card-001/card-001.html'))

    def test_accessibility_repair_preserves_existing_and_implicit_labels(self):
        text = '<label>Email<input placeholder="Your email"></label><input id="a" placeholder="Your name"><label for="a">Name</label><input placeholder="Search articles">'
        result = repair(text)
        self.assertEqual(result.count('aria-label='), 1)
        self.assertIn('aria-label="Search articles"', result)
        self.assertEqual(result, repair(result))

    def test_dynamic_bound_sources_are_not_static_file_references(self):
        parser = Page(); parser.feed('<img :src="`https://example.test/${id}`" alt="Example"><script>const x = 1;</script>')
        self.assertNotIn('src', parser.tags[0][1])
        self.assertEqual(parser.scripts[0][1], 'const x = 1;')

    def test_legacy_generator_rejects_path_escape(self):
        with tempfile.TemporaryDirectory() as output:
            template = {'dir': '..', 'id': 'escape', 'title': 'Title', 'description': 'Description', 'content': 'content'}
            with patch('sys.argv', ['generator', '--output-dir', output]), self.assertRaises(ValueError):
                generate_templates([template], '{content}')

    def test_legacy_generator_requires_explicit_overwrite(self):
        with tempfile.TemporaryDirectory() as output:
            template = {'dir': 'templates', 'id': 'test', 'title': 'Title', 'description': 'Description', 'content': '<h1>Example</h1>'}
            with patch('sys.argv', ['generator', '--output-dir', output]):
                generate_templates([template], '{content}')
                with self.assertRaises(FileExistsError): generate_templates([template], '{content}')

if __name__ == '__main__': unittest.main()
