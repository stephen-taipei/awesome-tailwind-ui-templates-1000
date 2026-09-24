"""Safe compatibility runner for historical template definitions."""
from __future__ import annotations
import argparse
from html import escape
from pathlib import Path
from scripts.migrate_legacy import migrate_html


def generate_templates(templates: list[dict], base_html: str) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    root = args.output_dir.resolve()
    planned = []
    seen = set()
    for template in templates:
        target = (root / template['dir'] / f"{template['id']}.html").resolve()
        if not target.is_relative_to(root) or target in seen:
            raise ValueError(f'Unsafe or duplicate output path: {target}')
        if target.exists() and not args.overwrite:
            raise FileExistsError(f'{target}: use --overwrite to replace an existing file')
        seen.add(target)
        content = base_html.format(id=escape(template['id']), title=escape(template['title']),
                                   description=escape(template['description'], quote=True), content=template['content'])
        planned.append((target, migrate_html(content, target, root)))
    for target, content in planned:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
    print(f'Generated {len(planned)} templates in {root}. No Git operations were performed.')
