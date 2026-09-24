"""Evidence-driven, source-preserving fixes for narrow template viewports."""
from pathlib import Path
import argparse
import json
import re
try:
    from scripts.accessibility import Tags
    from scripts.migrate_legacy import ROOT, template_paths
except ModuleNotFoundError:
    from accessibility import Tags
    from migrate_legacy import ROOT, template_paths

NAVIGATION = {63,64,65,66,69,70,71,76,77,82,84,85,86,87,88,90,91,92,93,94,96,97,98,99,100,101,102,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,137,138,139,141,142,144,145,147,148,149,150,151,152,153,154,155,156,157,158,160,161}
NAV_CSS = '''
@media (max-width: 767px) {
  body { padding-inline: 1rem; }
  [data-mobile-wrap] { flex-wrap: wrap; row-gap: .75rem; max-width: 100%; min-width: 0; }
  [data-mobile-wrap] > * { min-width: 0; max-width: 100%; }
  [data-mobile-height] { height: auto; min-height: 4rem; padding-block: .75rem; }
  h1, h2, h3 { overflow-wrap: anywhere; }
}
'''
# Each rule is tied to an observed component; content is reflowed, not hidden globally.
CUSTOM = {
'card-049': '@media(max-width:639px){input{min-width:0}.flex.gap-2:has(>input){flex-direction:column}}',
'form-005': '@media(max-width:639px){.flex:has(>input){flex-direction:column}input{min-width:0}}',
'form-018': '@media(max-width:639px){.flex.justify-between{flex-wrap:wrap;gap:.75rem}.flex.justify-between>*{min-width:0;overflow-wrap:anywhere}}',
'form-029': '@media(max-width:639px){.flex:has(>label){flex-wrap:wrap}}',
'form-034': '.sr-only{position:absolute}label:has(>.sr-only){position:relative}',
'landing-033': '@media(max-width:767px){.flex.justify-center.gap-8{flex-wrap:wrap}}',
'landing-035': '@media(max-width:639px){.flex.justify-center.gap-4{flex-direction:column;align-items:stretch}}',
'landing-040': '@media(max-width:639px){form .flex{flex-direction:column;border-radius:1.25rem}form input{min-width:0;width:100%}form button{justify-content:center}}',
'landing-042': '@media(max-width:639px){.absolute.-right-6{right:0}}',
'landing-045': '@media(max-width:639px){.absolute.-right-6{right:0}}',
'nav-026': '@media(max-width:767px){body>.flex{flex-direction:column}aside{width:100%!important}main.flex-1{min-width:0;padding:1rem}main .flex{flex-wrap:wrap}.sidebar-tooltip{display:none}}',
'nav-045': '@media(max-width:767px){.flex:has(>button){flex-wrap:wrap;gap:.5rem}.flex.gap-6{flex-direction:column}.flex-1{min-width:0}}',
'nav-071': '@media(max-width:767px){li:has(.clip-arrow),li:has(.clip-arrow-middle),li:has(.clip-arrow-end){flex:1 1 100%}}',
'nav-007': '#top-header{margin-left:0}@media(min-width:1024px){#top-header.main-content-expanded{left:16rem}#top-header.main-content-collapsed{left:5rem}}',
'team-009': '@media(max-width:639px){.inline-flex:has(>button){flex-wrap:wrap;justify-content:center} .inline-flex>button{padding-inline:1rem}}',
'test-030': '@media(max-width:639px){.inline-flex:has(>button){flex-wrap:wrap;justify-content:center} .inline-flex>button{padding-inline:1rem}}',
'test-044': '@media(max-width:639px){.translate-x-8{transform:none;translate:none}}',
'test-023': '@media(max-width:639px){.group{position:static}.group>div.absolute{left:50%;width:min(16rem,calc(100vw - 2rem))}}',
}

def repair(text: str, path: Path) -> str:
    template_id = path.parent.name if path.stem == 'index' else path.stem
    if 'id="responsive-repair"' in text: return text
    if template_id == 'nav-096':
        text = text.replace('absolute left-6 top-1/2', 'absolute right-6 top-1/2')
    styles = CUSTOM.get(template_id, '')
    if template_id.startswith('nav-') and int(template_id.split('-')[1]) in NAVIGATION:
        parser = Tags(text); parser.feed(text)
        edits = []
        for tag, attrs, source, start, _ in parser.tags:
            classes = (attrs.get('class') or '').split()
            if tag not in ('div','nav','header','ul','ol','form'): continue
            if not {'flex','inline-flex'}.intersection(classes) or 'flex-col' in classes or 'overflow-x-auto' in classes: continue
            if any(re.fullmatch(r'w-\d+', c) for c in classes) and any(re.fullmatch(r'h-\d+', c) for c in classes): continue
            attributes = ' data-mobile-wrap'
            if 'justify-between' in classes and any(re.fullmatch(r'h-\d+', c) for c in classes): attributes += ' data-mobile-height'
            edits.append((start, start+len(source), source[:-1]+attributes+'>'))
        for start, end, value in reversed(edits): text=text[:start]+value+text[end:]
        styles += NAV_CSS
    if template_id == 'nav-042':
        # A seven-column calendar requires a bounded, keyboard-scrollable preview on phones.
        text = text.replace('<section>', '<section class="calendar-example" tabindex="0" role="region" aria-label="Calendar layout example; scroll horizontally on narrow screens">')
        styles += '.calendar-example{max-width:100%;overflow-x:auto}.calendar-example>div{min-width:56rem}.calendar-example h2{position:sticky;left:0}'
    if styles: text = text.replace('</head>', '<style id="responsive-repair">\n'+styles+'\n</style>\n</head>')
    return text

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--apply',action='store_true');args=parser.parse_args();changed=[]
    for path in template_paths():
        before=path.read_text(encoding='utf-8');after=repair(before,path)
        if before!=after:
            changed.append(path.relative_to(ROOT).as_posix())
            if args.apply:path.write_text(after,encoding='utf-8')
    print(json.dumps({'responsiveFiles':len(changed),'applied':args.apply}))
if __name__=='__main__':main()
