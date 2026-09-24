import { loadCatalog, readSaved, writeSaved } from './catalog-core.mjs';
const $ = id => document.getElementById(id);
let item;
let source = '';
let saved = readSaved();
function saveState() {
  if (!item) return;
  const active = saved.has(item.id);
  $('preview-save').textContent = active ? '♥ Saved template' : '♡ Save template';
  $('preview-save').setAttribute('aria-pressed', String(active));
}
function view(code) {
  $('source-panel').hidden = !code;
  $('preview-canvas').hidden = code || !item;
  $('width-controls').hidden = code;
  $('view-preview').setAttribute('aria-pressed', String(!code));
  $('view-code').setAttribute('aria-pressed', String(code));
}
async function init() {
  try {
    const id = new URLSearchParams(location.search).get('template');
    const data = await loadCatalog();
    item = data.templates.find(template => template.id === id);
    if (!item) throw new Error('Choose a valid template from the collection. Arbitrary URLs are not accepted.');
    document.title = `${item.id}: ${item.title} — Tailwind Atlas`;
    $('template-id').textContent = item.id.toUpperCase(); $('template-title').textContent = item.title; $('template-description').textContent = item.description;
    $('open-original').href = item.path; $('open-original').hidden = false;
    $('template-frame').title = `${item.id}: ${item.title}`;
    $('template-frame').addEventListener('load', () => { $('preview-status').textContent = 'Preview loaded in an isolated frame. Some demo actions and translations require opening the original.'; }, { once: true });
    $('template-frame').src = item.path; $('preview-canvas').hidden = false;
    $('preview-save').disabled = false; saveState();
    $('preview-status').textContent = 'Loading template preview…';
    try {
      const response = await fetch(item.path, { signal: AbortSignal.timeout(20000) });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      source = await response.text(); $('source').value = source;
      $('copy').disabled = false; $('download').disabled = false;
    } catch { $('source').value = 'Source could not be loaded. Open the original or reload this page to try again.'; }
  } catch (error) {
    item = undefined; $('template-title').textContent = 'Template unavailable'; $('preview-error').hidden = false;
    $('preview-error-message').textContent = error instanceof Error ? error.message : 'The catalog could not be loaded.';
    $('preview-status').textContent = ''; $('preview-canvas').hidden = true;
  }
}
$('view-preview').addEventListener('click', () => view(false)); $('view-code').addEventListener('click', () => view(true));
for (const button of document.querySelectorAll('[data-width]')) button.addEventListener('click', () => {
  $('template-frame').style.width = button.dataset.width;
  for (const other of document.querySelectorAll('[data-width]')) other.setAttribute('aria-pressed', String(other === button));
});
$('preview-save').addEventListener('click', () => {
  if (!item) return;
  saved.has(item.id) ? saved.delete(item.id) : saved.add(item.id);
  const persisted = writeSaved(saved); saveState();
  $('preview-status').textContent = persisted ? 'Saved collection updated.' : 'Saved for this session; browser storage is unavailable.';
});
$('copy').addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(source); $('preview-status').textContent = 'HTML copied. Keep the referenced project assets when reusing it.'; }
  catch { view(true); $('source').focus(); $('source').select(); $('preview-status').textContent = 'Clipboard unavailable. HTML selected; press Ctrl+C or Command+C to copy.'; }
});
$('download').addEventListener('click', () => {
  if (!item || !source) return;
  const url = URL.createObjectURL(new Blob([source], { type: 'text/html;charset=utf-8' }));
  const link = document.createElement('a'); link.href = url; link.download = `${item.id}.html`;
  document.body.append(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  $('preview-status').textContent = 'Download started. This HTML requires the project assets at their original relative paths.';
});
addEventListener('storage', event => { if (event.key === 'atlas-saved') { saved = readSaved(); saveState(); } });
init();
