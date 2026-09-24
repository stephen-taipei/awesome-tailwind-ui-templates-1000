import { test, expect } from '@playwright/test';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
const manifest = JSON.parse(await readFile('templates.json', 'utf8'));
const settle = page => page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
test('every catalog template boots without JavaScript exceptions or local asset failures', async ({ browser }) => {
  test.setTimeout(600000);
  const results = [];
  let cursor = 0;
  await Promise.all(Array.from({ length: 6 }, async () => {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
    await context.route('**/*', route => {
      const url = new URL(route.request().url());
      return url.hostname === '127.0.0.1' ? route.continue() : route.abort();
    });
    const page = await context.newPage();
    while (cursor < manifest.templates.length) {
      const item = manifest.templates[cursor++];
      const result = { id: item.id, path: item.path, errors: [], missingAssets: [] };
      const error = value => result.errors.push(value.message);
      const response = value => { if (value.url().startsWith('http://127.0.0.1:4173/') && value.status() >= 400) result.missingAssets.push(`${value.status()} ${value.url()}`); };
      page.on('pageerror', error); page.on('response', response);
      try {
        await page.setViewportSize({ width: 1440, height: 900 });
        await page.goto(`http://127.0.0.1:4173/${item.path}`, { waitUntil: 'load', timeout: 15000 });
        await page.waitForTimeout(50); await settle(page);
        result.title = await page.title();
        result.desktopOverflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
        await page.setViewportSize({ width: 390, height: 844 }); await settle(page);
        result.mobileOverflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
        if (result.mobileOverflow) result.overflowDetails = await page.evaluate(() => ({ width: document.documentElement.scrollWidth, nodes: [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 1).slice(0, 5).map(e => ({ tag: e.tagName, className: e.getAttribute('class'), text: e.textContent.trim().slice(0, 100), width: e.getBoundingClientRect().width })) }));
      } catch (value) { result.errors.push(value.message); }
      finally { page.off('pageerror', error); page.off('response', response); }
      results.push(result);
    }
    await context.close();
  }));
  results.sort((a, b) => a.id.localeCompare(b.id));
  await mkdir('audit-results', { recursive: true });
  await writeFile('audit-results/browser-smoke.json', JSON.stringify({ templates: results.length, viewportWidths: [1440, 390], externalMedia: 'blocked', results }, null, 2));
  expect(results.filter(result => result.errors.length || result.missingAssets.length), 'See audit-results/browser-smoke.json for per-template evidence').toEqual([]);
  expect(results.filter(result => result.desktopOverflow || result.mobileOverflow), 'All templates must keep horizontal overflow inside an intentional scroll region').toEqual([]);
  expect(results.length).toBe(manifest.total);
});
