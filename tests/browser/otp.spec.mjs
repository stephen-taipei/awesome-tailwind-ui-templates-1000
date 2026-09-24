import { test, expect } from '@playwright/test';
import { mkdir } from 'node:fs/promises';
const examples = [
  ['templates/10-forms/form-017.html', 4], ['templates/11-authentication/auth-013.html', 6],
  ['templates/11-authentication/auth-020.html', 6], ['templates/13-modals/modal-014.html', 6],
  ['templates/11-authentication/auth-030.html', 1],
];
async function paste(locator, text) {
  await locator.evaluate((input, text) => {
    const data = new DataTransfer(); data.setData('text', text);
    input.dispatchEvent(new ClipboardEvent('paste', { clipboardData: data, bubbles: true, cancelable: true }));
  }, text);
}
for (const [path, count] of examples) {
  test(`${path}: named numeric input, paste, incomplete feedback and demo-only submission`, async ({ page }) => {
    await page.route('https://**/*', route => route.abort());
    await page.setViewportSize({ width: 320, height: 800 });
    const requests = []; page.on('request', r => { if (r.method() !== 'GET') requests.push(r.url()); });
    await page.goto('/' + path);
    await expect(page.locator('[data-otp-group]')).toHaveAttribute('data-otp-ready', 'true');
    const inputs = page.locator('[data-otp-group] input');
    await expect(inputs).toHaveCount(count);
    const verify = page.getByRole('button', { name: /^Verify( Code)?$/ });
    await verify.click();
    await expect(page.locator('[data-otp-status]')).toContainText('Enter all');
    await expect(inputs.first()).toBeFocused();
    await expect(inputs.first()).toHaveAttribute('aria-invalid', 'true');
    await paste(inputs.nth(count === 1 ? 0 : 2), count === 4 ? '１２３４' : '１２３４５６');
    expect((await inputs.evaluateAll(nodes => nodes.map(n => n.value))).join('')).toBe(count === 4 ? '1234' : '123456');
    await expect(inputs.first()).not.toHaveAttribute('aria-invalid', 'true');
    await verify.click();
    await expect(page.locator('[data-otp-status]')).toContainText('no authentication was performed');
    expect(requests).toEqual([]);
    expect(new URL(page.url()).search).toBe('');
    expect(await page.evaluate(() => ({ local: localStorage.length, session: sessionStorage.length }))).toEqual({ local: 0, session: 0 });
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    await mkdir('audit-results/screenshots', { recursive: true });
    await page.screenshot({ path: `audit-results/screenshots/${path.split('/').pop().replace('.html', '')}-320.png`, fullPage: true });
  });
}
test('OTP typing, backspace, arrows, autofill and normal Tab preserve keyboard control', async ({ page }) => {
  await page.route('https://**/*', route => route.abort());
  await page.goto('/templates/11-authentication/auth-013.html');
  const inputs = page.locator('[data-otp-group] input');
  await expect(page.locator('[data-otp-group]')).toHaveAttribute('data-otp-ready', 'true');
  await inputs.first().focus(); await page.keyboard.type('12');
  await expect(inputs.nth(2)).toBeFocused();
  await page.keyboard.press('Backspace'); await expect(inputs.nth(1)).toBeFocused();
  await expect(inputs.nth(1)).toHaveValue('');
  await page.keyboard.press('ArrowLeft'); await expect(inputs.first()).toBeFocused();
  await page.keyboard.press('ArrowRight'); await expect(inputs.nth(1)).toBeFocused();
  await page.keyboard.press('Tab'); await expect(inputs.nth(2)).toBeFocused();
  await inputs.nth(2).evaluate(input => input.dispatchEvent(new InputEvent('beforeinput', {
    bubbles: true, cancelable: true, inputType: 'insertReplacementText', data: '987654',
  })));
  expect(await inputs.evaluateAll(nodes => nodes.map(n => n.value))).toEqual(['9','8','7','6','5','4']);
  await expect(inputs.last()).toBeFocused();
  await page.keyboard.press('Tab'); await expect(page.getByRole('button', { name: 'Verify', exact: true })).toBeFocused();
});
