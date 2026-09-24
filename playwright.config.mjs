import { defineConfig } from '@playwright/test';
export default defineConfig({
  testDir: './tests/browser', timeout: 30000, fullyParallel: false, workers: 1,
  forbidOnly: !!process.env.CI, retries: 0,
  reporter: [['list'], ['html', { open: 'never' }], ['json', { outputFile: 'audit-results/playwright.json' }]],
  use: { baseURL: 'http://127.0.0.1:4173', viewport: { width: 1440, height: 1000 }, colorScheme: 'light',
    headless: true, trace: 'retain-on-failure', screenshot: 'only-on-failure',
    launchOptions: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH } : {} },
  webServer: { command: 'python3 tests/server.py', url: 'http://127.0.0.1:4173', reuseExistingServer: !process.env.CI, timeout: 15000 },
});
