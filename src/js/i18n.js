/**
 * i18n (Internationalization) Module
 * Lightweight translation system using data-i18n attributes
 *
 * @module i18n
 * @version 1.0.0
 */

const i18n = (function () {
  'use strict';

  // Private state
  let currentLocale = 'en';
  let translations = {};
  let fallbackLocale = 'en';

  /**
   * Get nested value from object using dot notation
   * @param {Object} obj - Source object
   * @param {string} path - Dot notation path (e.g., 'nav.home')
   * @returns {string|undefined} - Value at path or undefined
   */
  function getNestedValue(obj, path) {
    return path.split('.').reduce((current, key) => {
      return current && current[key] !== undefined ? current[key] : undefined;
    }, obj);
  }

  /**
   * Load translations from JSON file
   * @param {string} locale - Locale code (e.g., 'en', 'zh-TW')
   * @returns {Promise<Object>} - Translations object
   */
  async function loadLocale(locale) {
    try {
      const response = await fetch(`/locales/${locale}.json`);
      if (!response.ok) {
        throw new Error(`Failed to load locale: ${locale}`);
      }
      return await response.json();
    } catch (error) {
      console.warn(`i18n: Could not load locale "${locale}"`, error);
      return null;
    }
  }

  /**
   * Translate a single key
   * @param {string} key - Translation key (e.g., 'nav.home')
   * @param {Object} params - Interpolation parameters
   * @returns {string} - Translated string or key if not found
   */
  function translate(key, params = {}) {
    let value = getNestedValue(translations[currentLocale], key);

    // Fallback to default locale if not found
    if (value === undefined && currentLocale !== fallbackLocale) {
      value = getNestedValue(translations[fallbackLocale], key);
    }

    // Return key if translation not found
    if (value === undefined) {
      console.warn(`i18n: Missing translation for "${key}" in "${currentLocale}"`);
      return key;
    }

    // Interpolate parameters (e.g., "Hello, {{name}}")
    if (typeof value === 'string' && Object.keys(params).length > 0) {
      Object.entries(params).forEach(([paramKey, paramValue]) => {
        value = value.replace(new RegExp(`{{\\s*${paramKey}\\s*}}`, 'g'), paramValue);
      });
    }

    return value;
  }

  /**
   * Update all elements with data-i18n attribute
   */
  function updateDOM() {
    // Update text content
    document.querySelectorAll('[data-i18n]').forEach((element) => {
      const key = element.getAttribute('data-i18n');
      const translation = translate(key);
      element.textContent = translation;
    });

    // Update aria-label attributes
    document.querySelectorAll('[data-i18n-aria]').forEach((element) => {
      const key = element.getAttribute('data-i18n-aria');
      const translation = translate(key);
      element.setAttribute('aria-label', translation);
    });

    // Update placeholder attributes
    document.querySelectorAll('[data-i18n-placeholder]').forEach((element) => {
      const key = element.getAttribute('data-i18n-placeholder');
      const translation = translate(key);
      element.setAttribute('placeholder', translation);
    });

    // Update title attributes
    document.querySelectorAll('[data-i18n-title]').forEach((element) => {
      const key = element.getAttribute('data-i18n-title');
      const translation = translate(key);
      element.setAttribute('title', translation);
    });

    // Update document lang attribute
    document.documentElement.lang = currentLocale;

    // Dispatch custom event
    document.dispatchEvent(
      new CustomEvent('i18n:localeChanged', {
        detail: { locale: currentLocale },
      })
    );
  }

  /**
   * Set the current locale and update DOM
   * @param {string} locale - Locale code
   * @returns {Promise<boolean>} - Success status
   */
  async function setLocale(locale) {
    // Load locale if not already loaded
    if (!translations[locale]) {
      const loaded = await loadLocale(locale);
      if (!loaded) {
        console.error(`i18n: Failed to set locale "${locale}"`);
        return false;
      }
      translations[locale] = loaded;
    }

    currentLocale = locale;

    // Store preference
    try {
      localStorage.setItem('i18n-locale', locale);
    } catch (e) {
      // localStorage not available
    }

    updateDOM();
    return true;
  }

  /**
   * Get current locale
   * @returns {string} - Current locale code
   */
  function getLocale() {
    return currentLocale;
  }

  /**
   * Get available locales
   * @returns {string[]} - Array of loaded locale codes
   */
  function getAvailableLocales() {
    return Object.keys(translations);
  }

  /**
   * Add translations programmatically
   * @param {string} locale - Locale code
   * @param {Object} data - Translations object
   */
  function addTranslations(locale, data) {
    if (!translations[locale]) {
      translations[locale] = {};
    }
    Object.assign(translations[locale], data);
  }

  /**
   * Initialize i18n system
   * @param {Object} options - Configuration options
   * @param {string} options.defaultLocale - Default locale (default: 'en')
   * @param {string[]} options.supportedLocales - Locales to preload
   * @returns {Promise<void>}
   */
  async function init(options = {}) {
    const {
      defaultLocale = 'en',
      supportedLocales = ['en'],
    } = options;

    fallbackLocale = defaultLocale;

    // Preload supported locales
    await Promise.all(
      supportedLocales.map(async (locale) => {
        const data = await loadLocale(locale);
        if (data) {
          translations[locale] = data;
        }
      })
    );

    // Detect user's preferred locale
    let preferredLocale = defaultLocale;

    // Check localStorage first
    try {
      const stored = localStorage.getItem('i18n-locale');
      if (stored && supportedLocales.includes(stored)) {
        preferredLocale = stored;
      }
    } catch (e) {
      // localStorage not available
    }

    // Fallback to browser language
    if (preferredLocale === defaultLocale) {
      const browserLang = navigator.language || navigator.userLanguage;
      if (supportedLocales.includes(browserLang)) {
        preferredLocale = browserLang;
      } else {
        // Try base language (e.g., 'en' from 'en-US')
        const baseLang = browserLang.split('-')[0];
        if (supportedLocales.includes(baseLang)) {
          preferredLocale = baseLang;
        }
      }
    }

    await setLocale(preferredLocale);
  }

  // Public API
  return {
    init,
    setLocale,
    getLocale,
    getAvailableLocales,
    translate,
    t: translate, // Shorthand alias
    addTranslations,
    updateDOM,
  };
})();

// Export for ES modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = i18n;
}

// Auto-initialize when DOM is ready
if (typeof document !== 'undefined') {
  document.addEventListener('DOMContentLoaded', () => {
    // Only auto-init if not explicitly initialized
    if (i18n.getAvailableLocales().length === 0) {
      i18n.init({
        defaultLocale: 'en',
        supportedLocales: ['en', 'zh-TW', 'zh-CN', 'ja', 'ko'],
      });
    }
  });
}
