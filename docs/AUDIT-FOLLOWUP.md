# Follow-up audit: preserve category home and repair child templates

Date: 2026-09-24. Base: `3739618724a83b89b7d1843c2e8a5b13a7d08b65`.
Original homepage design reference: `43585b2ee68ff3f4590826e3244b26645f2ae5d6:index.html`.

## Scope and design boundary

The category homepage is restored to its original header, hero, progress block, eight category cards, featured navigation previews and footer. Classes, icon paths, card order and featured-section styling are recorded in immutable review fixtures and compared in the browser suite. Only real inventory counts, functional destinations, relative resource paths and local precompiled CSS replace the original stale values/dependencies. The original eight-card composition is not expanded into a new layout. All 21 categories are reachable through the existing full-directory text area.

The already implemented Tailwind Atlas search/favorites tool is retained at `explore.html`. It does not replace the category homepage. The compiled assets, pinned dependencies, i18n repairs, safe generators and earlier responsive fixes remain in place. Existing child URLs are unchanged.

## Verified defects and repairs

| Finding | Repair |
|---|---|
| Original home counted only 4/1000 and inactive cards did not reach their categories | Generate counts from all 1,043 real files. Keep card classes/order and link to actual catalog anchors. |
| 100 unnamed controls reported by the earlier audit | Reviewed names added to 48 child templates. Exact names are recorded in `reviewed-control-labels.json`. |
| Unassociated labels put `None` in the label-target set, accidentally accepting unrelated ID-less fields | Fixed the predicate. It exposed another 140 unnamed controls in 44 files. Most now have real visible-label `for`/`id` associations. Evidence is recorded in `reviewed-label-associations.json`. |
| 37 broken references in 36 files | Connect 34 modal names to real headings or explicit contextual names, fix two OTP group names and an attachment label target. |
| Five OTP layouts lacked complete usable input handling | Numeric input, full-width digit normalization, whole-code paste/autofill, focus movement, Backspace/arrows/Tab, format feedback. Codes are not stored, logged, submitted or authenticated. |
| Video modal depended on absent legacy aspect-ratio utilities | Replace with the built-in `aspect-video` utility. |
| Hover-only file selection checkboxes hid keyboard focus | Reveal them on focus without changing their idle design. |
| Reduced-motion preference did not disable smooth scrolling | Explicitly disable smooth scrolling under the existing preference. |

This follow-up edits 124 child HTML files. It does not redesign every template or implement every business operation.

## Regression gates and evidence

`npm test` covers catalog/i18n/generator/responsive logic, home generation, the missing-ID label regression, reference validation and pure OTP formatting. `npm run audit` scans **1,047 published HTML files**, including the restored homepage, directory, inspector and optional search tool. It also syntax-checks first-party JavaScript files and detects stale generated home/catalog outputs.

The browser suite covers the original homepage class/icon/order signatures at 390px and 1440px, JavaScript-disabled category browsing, Pages subpaths, visible label activation, the video ratio and five OTP layouts at 320px. The previous full 1,043-template boot/1440px/390px smoke test is retained, as are the gallery and preview-shell axe checks.

Local source checks: **44 unit tests passed** and the full static scan has **0 blocking errors**. The container Chromium cannot navigate localhost (`ERR_BLOCKED_BY_ADMINISTRATOR`), so local browser attempts are not counted as a pass. Browser results must come from the GitHub Actions run for the final commit. CI artifacts include JSON results, captured commit identity and screenshots. The exact final run and results are recorded in the PR, not inferred from previous runs.

## Remaining limitations

The static report retains **6,389 placeholder links** and **173 missing authored image alternatives** for contextual review. They are not hidden or filled with invented descriptions. Implicit labels, the quality of names, contrast and every interactive modal flow still require broader browser/manual evaluation. Existing authentication/checkout/upload/counter copy is demonstrative. No backend is implemented.

Full-template smoke blocks external media. It proves first-party boot/resource availability and the measured page boundaries, not third-party asset availability, all responsive widths, Safari/Firefox compatibility, complete WCAG conformity or production readiness. The five OTP examples only check formatting and deliberately never claim authentication success.

The one-time branch migration workflow is removed before final review. Permanent verification uses read-only repository permissions, pinned Actions and no automatic commit/push/deploy.
