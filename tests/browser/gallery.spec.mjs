import { test, expect } from '@playwright/test';
import { readFile, mkdir } from 'node:fs/promises';
const axe = await readFile('node_modules/axe-core/axe.min.js', 'utf8');
const prefix = '/awesome-tailwind-ui-templates-1000/';
async function ready(page, path = '/explore.html') { await page.goto(path); await expect(page.locator('.template-card')).toHaveCount(24); }
async function noViolations(page, exclude = []) {
  await page.evaluate(axe);
  const violations = await page.evaluate(async exclude => (await axe.run({ exclude }, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa'] } })).violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.map(n => n.target) })), exclude);
  expect(violations).toEqual([]);
}
test('search, category filtering, URL state and pagination work', async ({ page }) => {
  await ready(page);
  await page.locator('[data-category="hero"]').click();
  await expect(page.locator('#results-status')).toContainText('50 templates');
  await page.locator('#next').click(); await expect(page.locator('#page-status')).toHaveText('Page 2 of 3');
  await page.locator('#search').fill('hero-001');
  await expect(page.locator('.template-card')).toHaveCount(1);
  await expect(page).toHaveURL(/q=hero-001/);
  await page.reload(); await expect(page.locator('.template-card')).toHaveCount(1);
  await page.locator('#reset').click(); await expect(page.locator('.template-card')).toHaveCount(24);
  await page.locator('#search').fill('<script>unlikelymissing');
  await expect(page.locator('#empty')).toBeVisible();
  await expect(page.locator('.template-card')).toHaveCount(0);
});
test('favorites persist and corrupted storage is harmless', async ({ page }) => {
  await page.addInitScript(() => localStorage.setItem('atlas-saved', '{invalid'));
  await ready(page);
  await page.locator('[data-save="nav-001"]').click();
  await expect(page.locator('#saved-count')).toHaveText('1');
  await page.locator('#saved-toggle').click(); await expect(page.locator('.template-card')).toHaveCount(1);
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('atlas-saved')))).toEqual(['nav-001']);
});
test('saved state survives a normal reload', async ({ page }) => {
  await ready(page); await page.locator('[data-save="nav-001"]').click(); await page.reload();
  await expect(page.locator('#saved-count')).toHaveText('1');
  await expect(page.locator('[data-save="nav-001"]')).toHaveAttribute('aria-pressed', 'true');
});
test('catalog failures offer a working retry and static fallback', async ({ page }) => {
  await page.route('**/templates.json', route => route.fulfill({ status: 503, body: 'temporarily unavailable' }));
  await page.goto('/explore.html'); await expect(page.locator('#load-error')).toBeVisible();
  await page.unroute('**/templates.json'); await page.locator('#retry').click();
  await expect(page.locator('.template-card')).toHaveCount(24);
});
test('nested hosting, locale preferences and DOM preservation work', async ({ page }) => {
  await ready(page, prefix + 'explore.html');
  const failed = []; page.on('response', response => { if (response.status() >= 400 && response.url().includes('/locales/')) failed.push(response.url()); });
  await page.goto(`${prefix}templates/01-navigation/nav-001.html`);
  await page.waitForFunction(() => globalThis.i18n?.getAvailableLocales().includes('en'));
  await page.evaluate(() => {
    const button = document.createElement('button'); button.id = 'translation-probe'; button.dataset.i18n = 'nav.home'; button.innerHTML = '<svg aria-hidden="true"></svg>Original'; document.body.append(button);
    const span = document.createElement('span'); span.id = 'missing-probe'; span.dataset.i18n = 'missing.never.authored'; span.textContent = 'Keep this text'; document.body.append(span);
    return i18n.setLocale('zh-TW');
  });
  await expect(page.locator('html')).toHaveAttribute('lang', 'zh-TW');
  await expect(page.locator('#translation-probe svg')).toHaveCount(1); await expect(page.locator('#missing-probe')).toHaveText('Keep this text');
  expect(failed).toEqual([]);
});
test('collapsed mobile navigation is inert and Escape restores focus', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 }); await page.goto('/templates/01-navigation/nav-001.html');
  await expect(page.locator('#mobile-menu')).toHaveAttribute('inert', '');
  await page.locator('#mobile-menu-btn').click(); await expect(page.locator('#mobile-menu')).not.toHaveAttribute('inert', '');
  await page.locator('#mobile-menu a').first().focus(); await page.keyboard.press('Escape');
  await expect(page.locator('#mobile-menu-btn')).toBeFocused(); await expect(page.locator('#mobile-menu')).toHaveAttribute('inert', '');
});
test('Alpine pricing switch works with local dependencies', async ({ page }) => {
  await page.goto('/templates/06-pricing/price-003.html');
  await expect(page.getByRole('switch', { name: 'Yearly billing' })).toHaveAttribute('aria-checked', 'false');
  await page.getByRole('switch').click();
  await expect(page.getByRole('switch')).toHaveAttribute('aria-checked', 'true');
  await expect(page.locator('[x-text]').first()).toHaveText('$12');
});
test('preview uses a restrictive sandbox, responsive widths and readable source', async ({ page }) => {
  await page.goto('/preview.html?template=price-003');
  await expect(page.locator('#template-frame')).toHaveAttribute('src', 'templates/06-pricing/price-003.html');
  await expect(page.locator('#template-frame')).toHaveAttribute('sandbox', 'allow-scripts');
  await page.getByRole('button', { name: 'Mobile', exact: true }).click();
  await expect(page.locator('#template-frame')).toHaveCSS('width', '390px');
  await page.getByRole('button', { name: 'HTML source', exact: true }).click();
  await expect(page.locator('#source')).toHaveValue(/<!DOCTYPE html>/);
  await expect(page.locator('#source')).toHaveAttribute('readonly', '');
  await expect(page.locator('#download')).toBeEnabled();
  await page.goto('/preview.html?template=../../evil'); await expect(page.locator('#preview-error')).toBeVisible();
  await expect(page.locator('#template-frame')).not.toHaveAttribute('src');
});
test('demo forms never put entered values into the URL', async ({ page }) => {
  await page.goto('/templates/11-authentication/auth-001.html');
  await page.evaluate(() => { const form = document.querySelector('form'); if (!form) throw new Error('Missing form'); form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true })); });
  await expect(page.locator('[data-demo-status]')).toContainText('no information was submitted');
  expect(new URL(page.url()).search).toBe('');
});
test('gallery and preview shell pass automated WCAG checks at desktop and mobile widths', async ({ page }) => {
  await ready(page); await noViolations(page);
  await page.setViewportSize({ width: 390, height: 844 }); await noViolations(page);
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  await page.getByRole('button', { name: 'Use dark appearance' }).click(); await noViolations(page);
  await page.goto('/preview.html?template=nav-001'); await expect(page.locator('#template-title')).not.toHaveText('Loading template…');
  await noViolations(page, [['#template-frame']]);
});
test('capture gallery and inspector visual evidence', async ({ page }) => {
  await mkdir('audit-results/screenshots', { recursive: true }); await ready(page);
  await page.screenshot({ path: 'audit-results/screenshots/gallery-desktop.png', fullPage: false });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: 'audit-results/screenshots/gallery-mobile.png', fullPage: false });
  await page.getByRole('button', { name: 'Use dark appearance' }).click();
  await page.screenshot({ path: 'audit-results/screenshots/gallery-dark-mobile.png', fullPage: false });
  await page.setViewportSize({ width: 1440, height: 1000 }); await page.goto('/preview.html?template=price-003');
  await expect(page.locator('#template-frame')).toHaveAttribute('src', /price-003/);
  await page.screenshot({ path: 'audit-results/screenshots/inspector.png', fullPage: false });
});
