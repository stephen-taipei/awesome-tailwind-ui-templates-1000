"""Conservative, source-preserving fixes; ambiguous controls/images stay in the audit."""
from html import escape
from html.parser import HTMLParser
import re

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
class Tags(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.offsets = [0]
        for line in text.splitlines(keepends=True): self.offsets.append(self.offsets[-1] + len(line))
        self.tags = []
        self.stack = []
        self.labels = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'label' and attrs.get('for'): self.labels.add(attrs['for'])
        line, column = self.getpos()
        self.tags.append((tag, attrs, self.get_starttag_text(), self.offsets[line - 1] + column, 'label' in self.stack))
        if tag not in VOID: self.stack.append(tag)
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_endtag(self, tag):
        if tag in self.stack:
            index = len(self.stack) - 1 - self.stack[::-1].index(tag)
            del self.stack[index:]

def repair(text: str) -> str:
    parser = Tags(text); parser.feed(text)
    edits = []
    for tag, attrs, source, offset, implicit_label in parser.tags:
        additions = ''
        placeholder = attrs.get('placeholder', '')
        if tag in ('input', 'textarea', 'select') and placeholder and sum(ch.isalpha() for ch in placeholder) >= 3:
            if not implicit_label and not (attrs.get('aria-label') or attrs.get('aria-labelledby') or attrs.get('id') in parser.labels):
                additions += f' aria-label="{escape(placeholder, quote=True)}"'
        if tag == 'a' and attrs.get('target') == '_blank' and not attrs.get('rel'):
            additions += ' rel="noopener noreferrer"'
        if additions:
            updated = re.sub(r'(\s*/?>)$', lambda match: additions + match[1], source)
            edits.append((offset, offset + len(source), updated))
    for start, end, replacement in reversed(edits): text = text[:start] + replacement + text[end:]
    return text
