import unittest
from scripts.audit import Page, semantic_issues


def issues(source):
    page = Page()
    page.feed(source)
    return semantic_issues(page)


class SemanticsTests(unittest.TestCase):
    def test_named_controls(self):
        self.assertEqual(issues('<label for="code">Code</label><input id="code"><label>Search<input></label><select aria-label="Country"></select>'), [])

    def test_missing_name_is_blocking(self):
        self.assertEqual([issue['code'] for issue in issues('<input placeholder="Email"><select></select>')], ['control-label', 'control-label'])

    def test_nonexistent_label_target(self):
        self.assertEqual(issues('<label for="absent">Code</label>')[0]['code'], 'broken-label-reference')

    def test_label_target_must_be_labelable(self):
        for target in ['<div id="x"></div>', '<input id="x" type="hidden">']:
            self.assertEqual(issues('<label for="x">Name</label>' + target)[0]['code'], 'invalid-label-target')

    def test_each_aria_reference_is_checked(self):
        source = '<h2 id="title">Title</h2><div role="dialog" aria-labelledby="title absent" aria-describedby="description" aria-controls="menu"></div>'
        self.assertEqual([item['detail'] for item in issues(source)], ['aria-labelledby=absent', 'aria-describedby=description', 'aria-controls=menu'])

    def test_forward_references_and_multi_target_names(self):
        self.assertEqual(issues('<input aria-labelledby="a b"><span id="a">Security</span><span id="b">code</span>'), [])

    def test_unassociated_label_does_not_name_unrelated_controls(self):
        result = issues('<label>Visible but unassociated</label><input><select></select>')
        self.assertEqual([item['code'] for item in result], ['control-label', 'control-label'])
