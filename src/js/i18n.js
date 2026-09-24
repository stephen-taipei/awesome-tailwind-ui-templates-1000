/** Small ES-module translator. Missing keys preserve authored DOM, never render HTML. */
const DEFAULT_BASE = new URL('../../locales/', import.meta.url);
const FORBIDDEN = new Set(['__proto__', 'prototype', 'constructor']);
const own = (object, key) => object != null && Object.prototype.hasOwnProperty.call(object, key);
function storageOrNull() { try { return globalThis.localStorage; } catch { return null; } }
export function nestedValue(object, path) {
  if (typeof path !== 'string') return undefined;
  let value = object;
  for (const key of path.split('.')) {
    if (FORBIDDEN.has(key) || !own(value, key)) return undefined;
    value = value[key];
  }
  return typeof value === 'string' ? value : undefined;
}
function merge(target, source, depth = 0) {
  if (!source || typeof source !== 'object' || Array.isArray(source) || depth > 20) return target;
  for (const key of Object.keys(source)) {
    if (FORBIDDEN.has(key)) continue;
    const value = source[key];
    if (typeof value === 'string') target[key] = value;
    else if (value && typeof value === 'object' && !Array.isArray(value)) {
      if (!own(target, key) || typeof target[key] !== 'object') target[key] = Object.create(null);
      merge(target[key], value, depth + 1);
    }
  }
  return target;
}
export function createI18n({ fetcher = globalThis.fetch, document: doc = globalThis.document,
  storage = storageOrNull(), browserLanguage = globalThis.navigator?.language || 'en', baseURL = DEFAULT_BASE } = {}) {
  const translations = Object.create(null);
  const pending = new Map();
  const original = new WeakMap();
  let current = 'en';
  let fallback = 'en';
  let supported = ['en', 'zh-TW', 'zh-CN'];
  let revision = 0;
  let initialization;
  let base = new URL(baseURL, DEFAULT_BASE);
  function valid(locale) { return typeof locale === 'string' && /^[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$/.test(locale) && supported.includes(locale); }
  async function load(locale) {
    if (own(translations, locale)) return translations[locale];
    if (!pending.has(locale)) pending.set(locale, (async () => {
      try {
        const response = await fetcher(new URL(`${locale}.json`, base), { signal: AbortSignal.timeout(12000) });
        if (!response.ok) return null;
        const data = await response.json();
        if (!data || typeof data !== 'object' || Array.isArray(data)) return null;
        translations[locale] = merge(Object.create(null), data);
        return translations[locale];
      } catch { return null; }
      finally { pending.delete(locale); }
    })());
    return pending.get(locale);
  }
  function lookup(key) { return nestedValue(translations[current], key) ?? nestedValue(translations[fallback], key); }
  function translate(key, params = {}) {
    return (lookup(key) ?? key).replace(/{{\s*([\w.-]+)\s*}}/g, (match, name) => own(params, name) && !FORBIDDEN.has(name) ? String(params[name]) : match);
  }
  function binding(element, key, create) {
    if (!original.has(element)) original.set(element, new Map());
    const bindings = original.get(element);
    if (!bindings.has(key)) bindings.set(key, create());
    return bindings.get(key);
  }
  function updateDOM(root = doc) {
    if (!root?.querySelectorAll) return;
    for (const element of root.querySelectorAll('[data-i18n]')) {
      const record = binding(element, 'text', () => ({ nodes: [...element.childNodes].filter(node => node.nodeType === 3).map(node => [node, node.textContent]), added: null }));
      const value = lookup(element.getAttribute('data-i18n'));
      if (value === undefined) {
        for (const [node, text] of record.nodes) node.textContent = text;
        record.added?.remove(); record.added = null;
      } else if (record.nodes.length) {
        record.nodes.forEach(([node], index) => { node.textContent = index === 0 ? value : ''; });
      } else {
        if (!record.added) { record.added = doc.createTextNode(''); element.prepend(record.added); }
        record.added.textContent = value;
      }
    }
    for (const [dataAttr, attr] of [['data-i18n-aria', 'aria-label'], ['data-i18n-placeholder', 'placeholder'], ['data-i18n-title', 'title']]) {
      for (const element of root.querySelectorAll(`[${dataAttr}]`)) {
        const authored = binding(element, attr, () => ({ value: element.getAttribute(attr) }));
        const value = lookup(element.getAttribute(dataAttr)) ?? authored.value;
        value === null ? element.removeAttribute(attr) : element.setAttribute(attr, value);
      }
    }
    if (doc?.documentElement) {
      doc.documentElement.lang = current;
      doc.documentElement.dir = /^(ar|fa|he|ur)(-|$)/.test(current) ? 'rtl' : 'ltr';
    }
    if (doc?.dispatchEvent && globalThis.CustomEvent) doc.dispatchEvent(new CustomEvent('i18n:localeChanged', { detail: { locale: current } }));
  }
  async function setLocale(locale) {
    if (!valid(locale)) return false;
    const request = ++revision;
    const loaded = await load(locale);
    if (request !== revision || !loaded) return false;
    current = locale;
    try { storage?.setItem('i18n-locale', locale); } catch {}
    updateDOM(); return true;
  }
  function choosePreferred(defaultLocale) {
    try { const value = storage?.getItem('i18n-locale'); if (valid(value)) return value; } catch {}
    const exact = supported.find(locale => locale.toLowerCase() === browserLanguage.toLowerCase());
    if (exact) return exact;
    if (/^zh-(hant|tw|hk|mo)/i.test(browserLanguage) && supported.includes('zh-TW')) return 'zh-TW';
    if (/^zh(?:-(hans|cn|sg))?$/i.test(browserLanguage) && supported.includes('zh-CN')) return 'zh-CN';
    return supported.find(locale => locale === browserLanguage.split('-')[0]) || defaultLocale;
  }
  function init(options = {}) {
    if (initialization) return initialization;
    initialization = (async () => {
      fallback = options.defaultLocale || 'en';
      supported = [...new Set(options.supportedLocales || ['en', 'zh-TW', 'zh-CN'])];
      if (!supported.includes(fallback)) supported.unshift(fallback);
      if (!supported.every(locale => valid(locale))) throw new TypeError('Unsupported locale identifier');
      if (options.baseURL) base = new URL(options.baseURL, DEFAULT_BASE);
      const before = revision;
      await load(fallback);
      if (revision !== before) return;
      const preferred = choosePreferred(fallback);
      if (!await setLocale(preferred) && preferred !== fallback && revision === before + 1) await setLocale(fallback);
    })();
    return initialization;
  }
  function addTranslations(locale, data) {
    if (typeof locale !== 'string' || FORBIDDEN.has(locale) || !/^[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$/.test(locale)) throw new TypeError('Invalid locale');
    translations[locale] = merge(translations[locale] || Object.create(null), data);
  }
  return { init, setLocale, translate, t: translate, updateDOM, addTranslations,
    getLocale: () => current, getAvailableLocales: () => Object.keys(translations), getSupportedLocales: () => [...supported] };
}
export const i18n = createI18n();
export default i18n;
if (typeof document !== 'undefined') {
  globalThis.i18n = i18n;
  const start = () => { i18n.init().catch(() => {}); };
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', start, { once: true }) : start();
}
