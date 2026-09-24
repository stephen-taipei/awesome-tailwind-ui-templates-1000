import { PAGE_SIZE, loadCatalog, readState, stateParams, filterTemplates, readSaved, writeSaved, element } from './catalog-core.mjs';
const $ = id => document.getElementById(id);
let data;
let state = readState(new URLSearchParams(location.search));
let saved = readSaved();
let debounce;
let requestVersion = 0;
function syncURL() {
  const params = stateParams(state).toString();
  history.replaceState(null, '', `${location.pathname}${params ? `?${params}` : ''}${location.hash}`);
}
function sketch(category) {
  const art = element('div', 'card-art');
  art.setAttribute('aria-hidden', 'true');
  art.dataset.kind = ['forms', 'authentication', 'modals'].includes(category) ? 'form'
    : ['dashboard', 'lists', 'community'].includes(category) ? 'dashboard'
    : ['cards', 'pricing', 'team', 'gallery', 'ecommerce', 'features'].includes(category) ? 'grid'
    : ['navigation', 'footers', 'notifications'].includes(category) ? 'nav' : 'hero';
  const window = element('div', 'mini-window');
  const top = element('div', 'mini-top'); top.append(element('i'), element('b'));
  const body = element('div', 'mini-body');
  const main = element('div', 'mini-main'); main.append(element('b'), element('b'), element('i'));
  body.append(main, element('div', 'mini-side')); window.append(top, body); art.append(window);
  return art;
}
function toggleSaved(id) {
  saved.has(id) ? saved.delete(id) : saved.add(id);
  const persisted = writeSaved(saved);
  render();
  if (!persisted) $('results-status').textContent += ' Saved for this session; browser storage is unavailable.';
}
function card(item) {
  const article = element('article', 'template-card');
  const link = element('a', 'card-link'); link.href = `preview.html?template=${encodeURIComponent(item.id)}`;
  const info = element('div', 'card-info');
  const category = data.categories.find(category => category.id === item.category);
  const kicker = element('div', 'card-kicker', category.name.toUpperCase());
  const heading = element('h3', '', item.title);
  const description = element('p', '', item.description || `An editable ${category.name.toLowerCase()} interface example.`);
  const footer = element('div', 'card-footer'); footer.append(element('span', '', item.id), element('strong', '', 'Explore →'));
  info.append(kicker, heading, description, footer); link.append(sketch(item.category), info);
  const save = element('button', 'save-card', saved.has(item.id) ? '♥' : '♡'); save.type = 'button';
  save.setAttribute('aria-label', `${saved.has(item.id) ? 'Unsave' : 'Save'} ${item.title} (${item.id})`);
  save.setAttribute('aria-pressed', String(saved.has(item.id))); save.dataset.save = item.id;
  save.addEventListener('click', () => {
    toggleSaved(item.id);
    const replacement = [...document.querySelectorAll('[data-save]')].find(button => button.dataset.save === item.id);
    (replacement || $('saved-toggle')).focus({ preventScroll: true });
  });
  article.append(link, save); return article;
}
function renderCategories() {
  const fragment = document.createDocumentFragment();
  for (const category of [{ id: 'all', name: 'All templates', count: data.total }, ...data.categories]) {
    const button = element('button', 'category-button'); button.type = 'button'; button.dataset.category = category.id;
    button.append(element('span', '', category.name), element('span', '', category.count.toLocaleString('en')));
    button.setAttribute('aria-pressed', String(category.id === state.category));
    button.addEventListener('click', () => { state.category = category.id; state.page = 1; render(); });
    fragment.append(button);
  }
  $('categories').replaceChildren(fragment);
}
function render() {
  if (!data) return;
  if (state.category !== 'all' && !data.categories.some(category => category.id === state.category)) state.category = 'all';
  const results = filterTemplates(data, state, saved);
  const pages = Math.max(1, Math.ceil(results.length / PAGE_SIZE));
  state.page = Math.min(state.page, pages);
  const start = (state.page - 1) * PAGE_SIZE;
  $('templates').replaceChildren(...results.slice(start, start + PAGE_SIZE).map(card));
  $('empty').hidden = results.length !== 0;
  $('pagination').hidden = pages < 2;
  $('previous').disabled = state.page === 1; $('next').disabled = state.page === pages;
  $('page-status').textContent = `Page ${state.page} of ${pages}`;
  $('results-status').textContent = results.length ? `${(start + 1).toLocaleString('en')}–${Math.min(start + PAGE_SIZE, results.length).toLocaleString('en')} of ${results.length.toLocaleString('en')} templates` : '0 matching templates';
  $('reset').hidden = !state.q && state.category === 'all' && !state.saved && state.sort === 'featured';
  $('saved-count').textContent = saved.size;
  $('saved-toggle').setAttribute('aria-pressed', String(state.saved));
  $('search').value = state.q; $('sort').value = state.sort;
  for (const button of document.querySelectorAll('[data-category]')) button.setAttribute('aria-pressed', String(button.dataset.category === state.category));
  syncURL();
}
async function load() {
  const version = ++requestVersion;
  $('load-error').hidden = true;
  $('results-status').textContent = 'Loading the collection…';
  try {
    const catalog = await loadCatalog();
    if (version !== requestVersion) return;
    data = catalog;
    saved = new Set([...saved].filter(id => data.templates.some(item => item.id === id)));
    $('total-count').textContent = data.total.toLocaleString('en'); $('category-count').textContent = data.categories.length;
    renderCategories(); render();
  } catch {
    if (version !== requestVersion) return;
    $('load-error').hidden = false; $('results-status').textContent = 'Catalog unavailable. The static index is still accessible.';
  }
}
$('search-form').addEventListener('submit', event => { event.preventDefault(); clearTimeout(debounce); state.q = $('search').value.slice(0, 160); state.page = 1; render(); });
$('search').addEventListener('input', () => { clearTimeout(debounce); debounce = setTimeout(() => { state.q = $('search').value.slice(0, 160); state.page = 1; render(); }, 120); });
$('sort').addEventListener('change', () => { state.sort = $('sort').value; state.page = 1; render(); });
$('saved-toggle').addEventListener('click', () => { state.saved = !state.saved; state.page = 1; render(); });
$('reset').addEventListener('click', () => { clearTimeout(debounce); state = readState(new URLSearchParams()); render(); $('search').focus(); });
$('retry').addEventListener('click', load);
for (const [id, delta] of [['previous', -1], ['next', 1]]) $(id).addEventListener('click', () => { state.page += delta; render(); $('collection-title').scrollIntoView({ block: 'start' }); });
addEventListener('popstate', () => { clearTimeout(debounce); state = readState(new URLSearchParams(location.search)); render(); });
addEventListener('storage', event => { if (event.key === 'atlas-saved') { saved = readSaved(); render(); } });
document.addEventListener('keydown', event => { if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey && !event.target.closest('input,textarea,select,[contenteditable]')) { event.preventDefault(); $('search').focus(); } });
load();
