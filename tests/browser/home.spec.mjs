import { test, expect } from '@playwright/test';
import { readFile, mkdir } from 'node:fs/promises';
const design = JSON.parse(await readFile('tests/fixtures/home-design.json', 'utf8'));
const order = JSON.parse(await readFile('tests/fixtures/home-category-order.json', 'utf8'));
const data = JSON.parse(await readFile('templates.json', 'utf8'));
for (const width of [390, 1440]) {
  test(`category home preserves the pre-audit design at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: width === 390 ? 844 : 1000 });
    await page.goto('/');
    const actual = await page.evaluate(() => {
      const classes = node => [...node.classList];
      const descendants = node => [...node.querySelectorAll('[class]')].map(classes);
      const sections = document.querySelectorAll('main section');
      const cards = [...sections[2].querySelectorAll(':scope > div > a, :scope > div > div')];
      return {
        bodyClass: classes(document.body), headerClasses: descendants(document.querySelector('header')),
        mainClass: classes(document.querySelector('main')), categoryClasses: cards.map(descendants),
        categoryOuterClasses: cards.map(classes), svgPaths: [...document.querySelectorAll('header svg path')].map(n => n.getAttribute('d')),
        featuredClasses: descendants(sections[3]), footerClasses: descendants(document.querySelector('footer')),
      };
    });
    expect(actual).toEqual(design);
    await expect(page.locator('header h1')).toHaveText('Tailwind UI Templates');
    await expect(page.locator('header')).toHaveCSS('background-color', 'rgb(255, 255, 255)');
    await expect(page.locator('[data-category-home]')).toHaveCount(order.length);
    expect(await page.locator('[data-category-home]').evaluateAll(nodes => nodes.map(n => n.dataset.categoryHome))).toEqual(order);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    await mkdir('audit-results/screenshots', { recursive: true });
    await page.screenshot({ path: `audit-results/screenshots/category-home-${width}.png`, fullPage: true });
  });
}
test('original category home and all templates work with JavaScript disabled', async ({ browser }) => {
  // Test native navigation independently of CSS smooth-scroll animation timing.
  const context = await browser.newContext({ javaScriptEnabled: false, reducedMotion: 'reduce' });
  context.setDefaultTimeout(5000);
  await context.route('https://**/*', route => route.abort());
  const page = await context.newPage();
  try {
    await page.goto('http://127.0.0.1:4173/');
    await expect(page.locator('main')).toContainText(data.total.toLocaleString('en'));
    const links = await page.locator('[data-category-home]').evaluateAll(nodes => nodes.map(n => n.getAttribute('href')));
    expect(links).toEqual(order.map(id => `catalog.html#${id}`));
    await page.locator('[data-category-home="hero"]').click();
    await expect(page.locator('section#hero li')).toHaveCount(50);
    await expect(page.locator('main section')).toHaveCount(21);
    await expect(page.locator('.directory-list li')).toHaveCount(data.total);
    await page.locator('#hero a').first().click();
    await expect(page).toHaveURL(/hero-001.html/);
  } finally { await context.close(); }
});
test('preserved home resolves category and exploration links under Pages subpaths', async ({ page }) => {
  const failures = [];
  page.on('response', response => { if (response.status() >= 400) failures.push(response.url()); });
  await page.goto('/awesome-tailwind-ui-templates-1000/');
  await page.locator('a[href="explore.html"]').first().click();
  await expect(page).toHaveURL(/awesome-tailwind-ui-templates-1000\/explore.html/);
  await expect(page.locator('.template-card')).toHaveCount(24);
  expect(failures).toEqual([]);
});
test('associated visible labels focus fields and toggle the intended preferences', async ({ page }) => {
  await page.goto('/templates/99-dashboard/dashboard-905.html');
  const first = page.getByRole('textbox', { name: 'First Name', exact: true });
  await page.locator('label').filter({ hasText: /^First Name$/ }).click();
  await expect(first).toBeFocused();
  const updates = page.getByRole('checkbox', { name: 'Product Updates' });
  await expect(updates).not.toBeChecked();
  await page.locator('label').filter({ hasText: /^Product Updates$/ }).click();
  await expect(updates).toBeChecked();
});
test('video dialog reserves its intended 16:9 frame without a legacy plugin', async ({ page }) => {
  await page.route('https://**/*', route => route.abort());
  await page.goto('/templates/13-modals/modal-005.html');
  const box = await page.locator('.aspect-video').boundingBox();
  expect(box).not.toBeNull();
  expect(box.width / box.height).toBeCloseTo(16 / 9, 1);
  await expect(page.getByRole('dialog', { name: 'Video preview' })).toHaveCount(1);
});
