import test from 'node:test';
import assert from 'node:assert/strict';
import { createI18n, nestedValue } from '../src/js/i18n.js';
const ok = data => ({ ok: true, json: async () => data });
const memory = initial => ({ value: initial, getItem() { return this.value; }, setItem(key, value) { this.value = value; } });
const create = options => createI18n({ document: null, storage: null, browserLanguage: 'en', ...options });
test('locale paths resolve relative to the module/site prefix', async () => {
  const urls = [];
  const i18n = create({ baseURL: 'https://example.test/project/locales/', fetcher: async url => { urls.push(String(url)); return ok({ label: 'Hello' }); } });
  await i18n.init(); assert.deepEqual(urls, ['https://example.test/project/locales/en.json']); assert.equal(i18n.t('label'), 'Hello');
});
test('an explicitly saved English preference wins over browser Chinese', async () => {
  const i18n = create({ storage: memory('en'), browserLanguage: 'zh-TW', fetcher: async () => ok({}) });
  await i18n.init(); assert.equal(i18n.getLocale(), 'en');
});
test('browser language matching recognizes Chinese variants', async () => {
  const i18n = create({ browserLanguage: 'zh-Hant-TW', fetcher: async () => ok({}) });
  await i18n.init(); assert.equal(i18n.getLocale(), 'zh-TW');
});
test('only bundled locales load by default; traversal is rejected', async () => {
  const seen = [];
  const i18n = create({ fetcher: async url => { seen.push(String(url)); return ok({}); } });
  await i18n.init();
  for (const locale of ['ja', '../../evil', '__proto__']) assert.equal(await i18n.setLocale(locale), false);
  assert.equal(seen.length, 1); assert.deepEqual(i18n.getSupportedLocales(), ['en', 'zh-TW', 'zh-CN']);
});
test('latest requested locale wins even when requests finish out of order', async () => {
  const pending = new Map();
  const i18n = create({ fetcher: url => new Promise(resolve => pending.set(String(url).split('/').pop(), resolve)) });
  i18n.addTranslations('en', {}); await i18n.init();
  const earlier = i18n.setLocale('zh-TW'); const later = i18n.setLocale('zh-CN');
  pending.get('zh-CN.json')(ok({ label: '简体' })); assert.equal(await later, true);
  pending.get('zh-TW.json')(ok({ label: '繁體' })); assert.equal(await earlier, false);
  assert.equal(i18n.getLocale(), 'zh-CN');
});
test('fallback translation remains available when a selected key is absent', async () => {
  const i18n = create({ fetcher: async () => ok({}) });
  i18n.addTranslations('en', { nav: { home: 'Home' } }); i18n.addTranslations('zh-TW', {});
  await i18n.init(); await i18n.setLocale('zh-TW');
  assert.equal(i18n.t('nav.home'), 'Home'); assert.equal(i18n.t('missing'), 'missing');
});
test('deep additions preserve siblings and reject prototype access', async () => {
  const i18n = create();
  i18n.addTranslations('en', { nav: { home: 'Home' } }); i18n.addTranslations('en', { nav: { about: 'About' } });
  i18n.addTranslations('en', JSON.parse('{"__proto__":{"polluted":"yes"}}'));
  await i18n.init(); assert.equal(i18n.t('nav.home'), 'Home'); assert.equal(i18n.t('nav.about'), 'About');
  assert.equal({}.polluted, undefined); assert.equal(nestedValue({}, 'constructor.name'), undefined);
  assert.equal(i18n.t('nav'), 'nav');
});
test('interpolation handles dollar signs literally and does not compile parameter regex', async () => {
  const i18n = create(); i18n.addTranslations('en', { hello: 'Hi {{ name }} / {{x.y}}' }); await i18n.init();
  assert.equal(i18n.t('hello', { name: '$&', 'x.y': '<svg>' }), 'Hi $& / <svg>');
});
test('network and storage failure preserve authored fallback state', async () => {
  const denied = { getItem() { throw new Error('denied'); }, setItem() { throw new Error('denied'); } };
  const i18n = create({ storage: denied, browserLanguage: 'zh-TW', fetcher: async url => String(url).endsWith('/en.json') ? ok({ title: 'Fallback' }) : { ok: false } });
  await i18n.init(); assert.equal(i18n.getLocale(), 'en'); assert.equal(i18n.t('title'), 'Fallback');
});
test('initialization is idempotent and uses a single fetch', async () => {
  let count = 0; const i18n = create({ fetcher: async () => { count++; return ok({}); } });
  await Promise.all([i18n.init(), i18n.init(), i18n.init()]); assert.equal(count, 1);
});
