import { test, expect } from '@playwright/test';
import { mkdir } from 'node:fs/promises';
test('repaired mobile layouts reflow and wide calendars stay keyboard-scrollable', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.route('**/*', route => new URL(route.request().url()).hostname === '127.0.0.1' ? route.continue() : route.abort());
  const paths = ['templates/01-navigation/nav-150.html', 'templates/01-navigation/nav-063.html', 'templates/01-navigation/nav-042.html', 'templates/01-navigation/nav-096.html', 'templates/10-forms/form-005.html', 'templates/20-landing-pages/landing-040.html'];
  for (const path of paths) {
    await page.goto('/' + path);
    await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), path).toBe(true);
    if (path.includes('nav-042')) {
      const region = page.locator('.calendar-example').first(); await region.focus();
      await expect(region).toBeFocused();
      expect(await region.evaluate(element => element.scrollWidth > element.clientWidth)).toBe(true);
      await page.keyboard.press('ArrowRight');
      await expect.poll(() => region.evaluate(element => element.scrollLeft)).toBeGreaterThan(0);
    }
  }
  await mkdir('audit-results/screenshots', { recursive: true });
  await page.screenshot({ path: 'audit-results/screenshots/repaired-landing-mobile.png' });
  await page.goto('/templates/01-navigation/nav-150.html');
  await page.screenshot({ path: 'audit-results/screenshots/repaired-navigation-mobile.png' });
});
