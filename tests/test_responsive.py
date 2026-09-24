import unittest
from scripts.migrate_legacy import template_paths, ROOT
from scripts.responsive import repair

class ResponsiveTests(unittest.TestCase):
    def test_repairs_are_idempotent_for_every_template(self):
        for path in template_paths():
            text = path.read_text(encoding='utf-8')
            self.assertEqual(text, repair(text, path), str(path))

    def test_calendar_content_remains_keyboard_scrollable(self):
        path = ROOT / 'templates/01-navigation/nav-042.html'
        text = path.read_text(encoding='utf-8')
        self.assertIn('tabindex="0"', text)
        self.assertIn('overflow-x:auto', text)
        self.assertNotIn('body{overflow-x:hidden', text)

if __name__ == '__main__': unittest.main()
