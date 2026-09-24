# Awesome Tailwind UI Templates 1000

This collection contains **1,043 HTML UI demos across 21 categories**. The original category homepage is preserved. **Tailwind Atlas** remains available as a separate optional [search tool](explore.html). The repository name is unchanged. Counts below are an audit snapshot; [`templates.json`](templates.json) is generated from the actual files.

[Category homepage](https://stephen-taipei.github.io/awesome-tailwind-ui-templates-1000/) · [Complete static index](catalog.html) · [Search templates](explore.html) · [Follow-up audit](docs/AUDIT-FOLLOWUP.md) · [Initial audit](docs/AUDIT.md) · [Contributing](docs/CONTRIBUTING.md)

## What is included

The homepage keeps the original category cards, styling, order and featured examples. Counts and category links are generated from the real inventory, with a static directory covering all 21 categories. Edit `src/home.html` for nonvisual content fixes. Do not redesign this entry page without explicit owner approval.

At `explore.html`, search by name, description, category, or template ID. Recommended ordering shows different categories instead of hundreds of similar entries. Save favorites locally, share filtered URLs, and inspect real templates in an isolated desktop/tablet/mobile preview. HTML source can be viewed, copied, or downloaded. The complete static index works without JavaScript.

**These are interface examples, not finished applications.** Authentication, checkout, search results, uploads, and other business operations need your own implementation. Placeholder links, accessibility review items, and external stock images remain in the legacy collection. Do not interpret a successful build or automated boot check as certification of every template's interactions or WCAG compliance.

Template pages use locally compiled **Tailwind CSS 4.3.3** and, where needed, locally bundled **Alpine.js 3.15.12**. The gallery has no runtime framework dependency. There is no backend or database. Some original templates still request external images or fonts; this is **not** an entirely offline asset library.

## Quick start

To browse the checked-in static files, use Python 3.11+:

```sh
git clone https://github.com/stephen-taipei/awesome-tailwind-ui-templates-1000.git
cd awesome-tailwind-ui-templates-1000
python3 -m http.server 4173 --bind 127.0.0.1
# Open http://127.0.0.1:4173
```

Use an HTTP server rather than double-clicking `index.html`: browser module and fetch security rules apply to file URLs.

For development, use Node.js 22+ and Python 3.11+:

```sh
npm ci
npm run build
npm test
npm run audit
npx playwright install chromium
npm run test:browser
```

`npm run dev` rebuilds once and starts a local server. It is not a watch process: rerun `npm run build` after changing utility classes, theme variables, template metadata, or adding/removing templates. `npm run check` runs the build, unit tests, static audit, and browser suite; install Chromium first. Linux CI also installs the browser's OS dependencies.

## Real inventory

| Category | Files | Category | Files |
|---|---:|---|---:|
| Navigation | 166 | Hero sections | 50 |
| Features | 50 | Content | 50 |
| Calls to action | 50 | Pricing | 50 |
| Testimonials | 50 | Team | 50 |
| Gallery | 50 | Forms | 50 |
| Cards | 50 | Lists & tables | 50 |
| Modals & dialogs | 50 | Notifications | 50 |
| Footers | 50 | Authentication | 50 |
| Dashboards | 22 | E-commerce | 25 |
| Blog | 25 | Landing pages | 30 |
| Community | 25 | **Total** | **1,043** |

Historical IDs contain intentional gaps, and some navigation files contain several visual variants. A file is counted once; this is not a claim that every file is a unique production-ready component. Existing paths are preserved so previously shared links keep working.

## Reuse a template

Open a template in the inspector, then choose **Open original**, **HTML source**, or **Download**. A downloaded HTML file is **not a self-contained bundle**: preserve its relative position and the referenced `assets/` files. Templates with translation support additionally reference `src/js/i18n.js` and `locales/`.

For an existing Tailwind application, copy the relevant markup and per-template `:root` variables into your own build. Include any custom theme tokens in your Tailwind `@theme` registration. Replace demo links and operations, provide appropriate content and alt text, test keyboard navigation and contrast, and review third-party assets before shipping. The demo runtime deliberately prevents forms with no real action from submitting data.

## Structure and maintenance

```text
index.html / preview.html       Gallery and isolated template inspector
catalog.html / templates.json   Generated no-JS directory and canonical inventory
templates/                      Original category directories
cards/ forms/ lists/            Preserved historical paths
assets/css/gallery.css          Gallery design system, light/dark and responsive
assets/css/tailwind.css         Generated shared template stylesheet
assets/js/                      Gallery, inspector, and demo safeguards
assets/vendor/                  Pinned Alpine bundle and third-party licenses
src/css/main.css                Tailwind source and shared theme tokens
src/js/i18n.js                  ES-module translator
locales/                       en, zh-TW, zh-CN (partial content coverage)
scripts/                       Build, inventory, audit, and safe legacy migration
tests/                         Unit and browser regression coverage
docs/                          Audit findings and contribution contract
```

`npm run build` generates the catalog, full sitemap, robots file, shared CSS and Alpine bundle. It scans actual HTML paths rather than assuming 20 categories with 50 entries each. Template-local colors and fonts remain local `:root` values; the build registers their utility tokens without forcing every template into one theme.

The historical `generate_*.py` scripts are compatibility utilities, not the source of truth. They now require an explicit output directory and never stage, commit, or push Git changes:

```sh
python3 generate_batch_5.py --output-dir .generated/batch-5
# --overwrite is required to replace files already in that output directory.
```

Generate into a staging directory, review the output, then deliberately copy selected files into the collection. Copy project assets as well to preview a standalone staging tree. `npm run migrate` is an idempotent migration for known old dependency formats; it rejects unknown Tailwind JavaScript configurations instead of evaluating them.

## Internationalization and browser support

The translator supports the **three dictionaries that actually exist**: English, Traditional Chinese and Simplified Chinese. Their key coverage is partial; 29 annotated templates load it. Missing translations preserve authored content, and the fallback language is English. It resolves dictionaries relative to the module URL, including GitHub Pages project subpaths. Explicit saved language choices win over browser preferences.

```js
import i18n from './src/js/i18n.js';
await i18n.init();
await i18n.setLocale('zh-TW');
```

The preview sandbox intentionally does not grant same-origin privileges. Open the original page to use module-based translations. The gallery supports a persisted light/dark appearance; this does not imply that every original template implements dark mode.

Tailwind v4 targets modern browsers. See the [official compatibility guidance](https://tailwindcss.com/docs/compatibility); the previous Chrome 90 / Safari 14 support claim has been removed. Automated browser tests currently use Chromium, not a complete cross-browser certification matrix.

## Verification and known limits

The static audit inspects every published HTML file, local references, duplicate IDs, required metadata, inline JavaScript syntax, generated inventory, and sitemap counts. It records unresolved content/accessibility review items instead of masking them with empty attributes. Browser tests cover the gallery, inspector, local Alpine behavior, translation paths, and boot all catalog entries. External media is blocked during the all-template smoke test to keep first-party regressions reproducible.

CI uploads `audit-results/`, including per-template boot results, overflow observations, full static review items, browser traces and screenshots. The [audit report](docs/AUDIT.md) separates resolved defects from remaining editorial and interaction work.

## License

Repository code is MIT-licensed; see [LICENSE](LICENSE). The included Alpine and Tailwind license notices are under [`assets/vendor/`](assets/vendor/). Stock photography, remote fonts, trademarks and other third-party content are **not automatically covered** by the repository's MIT license. Review the relevant providers' terms and replace examples with assets you are authorized to use.

## 繁體中文摘要

這是一套 **1,043 份、21 類的前端 UI 示範模板**，不是已完成後端串接、全面無障礙認證或全部互動驗證的應用程式。新版目錄提供搜尋、分類、收藏、響應式預覽與 HTML 原始碼；既有模板網址保持不變。

直接以本機 HTTP 伺服器即可瀏覽。修改模板後執行 `npm run build`，以 `npm run check` 驗證；詳細修復範圍、證據與剩餘工作請見 [Codebase Audit](docs/AUDIT.md)。
