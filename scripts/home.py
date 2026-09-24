"""Render inventory values into the preserved category-home design."""
from pathlib import Path
import re


def render_home(data: dict, source: str) -> str:
    total = data['total']
    counts = {item['id']: item['count'] for item in data['categories']}
    declared = set(re.findall(r'{{count:([a-z-]+)}}', source))
    if not declared.issubset(counts):
        raise ValueError(f'Home categories differ from catalog: {declared ^ set(counts)}')
    result = source.replace('{{total}}', f'{total:,}').replace('{{category_count}}', str(len(counts)))
    result = result.replace('{{progress_width}}', str(min(100, total / 10)))
    result = result.replace('{{progress_percent}}', f'{total / 10:g}')
    result = re.sub(r'{{count:([a-z-]+)}}', lambda match: str(counts[match[1]]), result)
    if '{{' in result:
        raise ValueError('Unresolved category-home token')
    return result


def write_home(root: Path, data: dict) -> None:
    source = (root / 'src/home.html').read_text(encoding='utf-8')
    (root / 'index.html').write_text(render_home(data, source), encoding='utf-8')
