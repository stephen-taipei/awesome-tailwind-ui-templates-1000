import json
from pathlib import Path
import unittest
from scripts.catalog import collect
from scripts.home import render_home
from scripts.audit import Page

ROOT = Path(__file__).resolve().parents[1]


class HomeTests(unittest.TestCase):
    def test_inventory_values_are_rendered_without_js(self):
        data = {'total': 1043, 'categories': [{'id': 'navigation', 'count': 166}]}
        self.assertEqual(render_home(data, '{{total}} {{count:navigation}} {{progress_width}} {{progress_percent}}'), '1,043 166 100 104.3')

    def test_unknown_categories_fail(self):
        with self.assertRaises(ValueError):
            render_home({'total': 0, 'categories': []}, '{{count:unknown}}')

    def test_unresolved_tokens_fail(self):
        with self.assertRaises(ValueError):
            render_home({'total': 0, 'categories': []}, '{{future-token}}')

    def test_committed_home_matches_inventory(self):
        self.assertEqual((ROOT / 'index.html').read_text(), render_home(collect(), (ROOT / 'src/home.html').read_text()))

    def test_reviewed_names_have_explicit_per_template_evidence(self):
        reviewed = json.loads((ROOT / 'docs/reviewed-control-labels.json').read_text())
        self.assertEqual(sum(len(names) for names in reviewed.values()), 100)
        for path, names in reviewed.items():
            parser = Page()
            parser.feed((ROOT / path).read_text())
            labels = [attrs.get('aria-label') for _, attrs, _ in parser.tags]
            for name in names:
                self.assertIn(name, labels, path)

    def test_reviewed_associations_point_to_the_actual_fields(self):
        reviewed = json.loads((ROOT / 'docs/reviewed-label-associations.json').read_text())
        self.assertEqual(sum(len(names) for names in reviewed.values()), 140)
        for path, items in reviewed.items():
            parser = Page()
            parser.feed((ROOT / path).read_text())
            for item in items:
                if item['method'] == 'label-for':
                    self.assertTrue(any(a.get('id') == item['id'] for _, a, _ in parser.tags), path)
                    self.assertTrue(any(tag == 'label' and a.get('for') == item['id'] for tag, a, _ in parser.tags), path)
                else:
                    self.assertTrue(any(a.get('aria-label') == item['name'] for _, a, _ in parser.tags), path)
