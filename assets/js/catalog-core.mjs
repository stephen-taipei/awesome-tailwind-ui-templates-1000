/** Pure catalog logic shared by the gallery, inspector and regression tests. */
export const PAGE_SIZE = 24;
const ID = /^[a-z]+-\d{3,4}$/;
const PATH = /^(?:templates|cards|forms|lists)\/[a-zA-Z0-9_/-]+\.html$/;
export function validateManifest(data) {
  if (!data || data.schemaVersion !== 1 || !Array.isArray(data.templates) || !Array.isArray(data.categories)) throw new Error('Unsupported catalog format');
  const categories = new Set();
  for (const category of data.categories) {
    if (!category || !/^[a-z-]+$/.test(category.id) || typeof category.name !== 'string' || !Number.isInteger(category.count) || category.count < 1 || categories.has(category.id)) throw new Error('Invalid category');
    categories.add(category.id);
  }
  const ids = new Set();
  for (const item of data.templates) {
    if (!item || typeof item.id !== 'string' || !ID.test(item.id) || ids.has(item.id) || typeof item.title !== 'string' || typeof item.description !== 'string' || typeof item.path !== 'string' || !PATH.test(item.path) || item.path.includes('//') || !categories.has(item.category)) throw new Error('Invalid template entry');
    ids.add(item.id);
  }
  if (data.total !== ids.size || data.categories.some(category => category.count !== data.templates.filter(item => item.category === category.id).length)) throw new Error('Catalog counts do not match');
  return data;
}
export async function loadCatalog() {
  const response = await fetch(new URL('../../templates.json', import.meta.url), { signal: AbortSignal.timeout(20000) });
  if (!response.ok) throw new Error(`Catalog request failed (${response.status})`);
  return validateManifest(await response.json());
}
export function readState(params) {
  const page = Number(params.get('page'));
  return { q: (params.get('q') || '').slice(0, 160), category: params.get('category') || 'all',
    sort: ['name', 'id'].includes(params.get('sort')) ? params.get('sort') : 'featured', saved: params.get('saved') === '1',
    page: Number.isSafeInteger(page) && page > 0 ? Math.min(page, 100000) : 1 };
}
export function stateParams(state) {
  const params = new URLSearchParams();
  if (state.q) params.set('q', state.q);
  if (state.category !== 'all') params.set('category', state.category);
  if (state.sort !== 'featured') params.set('sort', state.sort);
  if (state.saved) params.set('saved', '1');
  if (state.page > 1) params.set('page', String(state.page));
  return params;
}
export function filterTemplates(data, state, saved = new Set()) {
  const tokens = state.q.toLocaleLowerCase('en').trim().split(/\s+/).filter(Boolean);
  const result = data.templates.filter(item => (state.category === 'all' || item.category === state.category)
    && (!state.saved || saved.has(item.id))
    && tokens.every(token => `${item.id} ${item.title} ${item.description} ${item.category}`.toLocaleLowerCase('en').includes(token)))
    .sort((a, b) => state.sort === 'name' ? a.title.localeCompare(b.title, 'en') || a.id.localeCompare(b.id, 'en', { numeric: true }) : a.id.localeCompare(b.id, 'en', { numeric: true }));
  if (state.sort !== 'featured') return result;
  const groups = data.categories.map(category => result.filter(item => item.category === category.id));
  const mixed = [];
  for (let row = 0; mixed.length < result.length; row++) for (const group of groups) if (group[row]) mixed.push(group[row]);
  return mixed;
}
export function readSaved(storage) {
  try {
    const value = JSON.parse((storage || globalThis.localStorage).getItem('atlas-saved') || '[]');
    return new Set(Array.isArray(value) ? value.filter(item => typeof item === 'string' && ID.test(item)).slice(0, 5000) : []);
  } catch { return new Set(); }
}
export function writeSaved(saved, storage) {
  try { (storage || globalThis.localStorage).setItem('atlas-saved', JSON.stringify([...saved])); return true; }
  catch { return false; }
}
export function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}
