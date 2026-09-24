import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { validateManifest, readState, stateParams, filterTemplates, readSaved, writeSaved, PAGE_SIZE } from '../assets/js/catalog-core.mjs';
const data = validateManifest(JSON.parse(await readFile(new URL('../templates.json', import.meta.url), 'utf8')));
const state = () => readState(new URLSearchParams());
test('catalog covers unique real entries and balanced recommended categories', () => {
  assert.ok(data.total >= 1000); assert.equal(new Set(data.templates.map(t => t.id)).size, data.total);
  assert.equal(new Set(filterTemplates(data, state()).slice(0, data.categories.length).map(t => t.category)).size, data.categories.length);
  assert.equal(PAGE_SIZE, 24);
});
test('search matches every token, category and saved filter together', () => {
  const input = { ...state(), q: 'nav-001 centered', category: 'navigation', saved: true };
  assert.deepEqual(filterTemplates(data, input, new Set(['nav-001'])).map(t => t.id), ['nav-001']);
  assert.equal(filterTemplates(data, input, new Set()).length, 0);
});
test('sort by name and ID is stable', () => {
  const entries = filterTemplates(data, { ...state(), category: 'navigation', sort: 'id' });
  assert.equal(entries[0].id, 'nav-001'); assert.equal(entries[entries.length - 1].id, 'nav-166');
  const names = filterTemplates(data, { ...state(), sort: 'name' });
  assert.ok(names.every((item, i) => !i || names[i - 1].title.localeCompare(item.title, 'en') <= 0));
});
test('query state round-trips without injecting markup', () => {
  const input = { ...state(), q: '<script>& test', category: 'cards', sort: 'name', saved: true, page: 3 };
  assert.deepEqual(readState(stateParams(input)), input);
  assert.equal(readState(new URLSearchParams('page=-100&sort=evil')).page, 1);
  assert.equal(readState(new URLSearchParams('page=Infinity')).page, 1);
  assert.equal(readState(new URLSearchParams('q=' + 'x'.repeat(1000))).q.length, 160);
});
test('manifest rejects external, traversing, encoded and duplicate paths/IDs', () => {
  for (const path of ['https://evil.test/a.html', '../index.html', 'templates/%2e%2e/a.html', 'javascript:alert(1)', '/templates/a.html']) {
    const invalid = structuredClone(data); invalid.templates[0].path = path;
    assert.throws(() => validateManifest(invalid));
  }
  const duplicate = structuredClone(data); duplicate.templates[1].id = duplicate.templates[0].id;
  assert.throws(() => validateManifest(duplicate));
});
test('manifest rejects inconsistent counts', () => {
  const invalid = structuredClone(data); invalid.total--;
  assert.throws(() => validateManifest(invalid));
});
test('corrupted or unavailable storage does not break browsing', () => {
  for (const value of ['{bad', '{}', 'null', '"hello"']) assert.equal(readSaved({ getItem: () => value }).size, 0);
  assert.deepEqual([...readSaved({ getItem: () => '["nav-001",null,"evil","nav-001"]' })], ['nav-001']);
  const denied = { getItem() { throw new Error('denied'); }, setItem() { throw new Error('denied'); } };
  assert.equal(readSaved(denied).size, 0); assert.equal(writeSaved(new Set(), denied), false);
});
