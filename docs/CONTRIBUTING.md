# Contributing

## Contract

Preserve existing public template URLs unless you also ship redirects. Do not infer IDs from ranges: `scripts/catalog.py` scans real files. Every template needs a unique ID, a descriptive title, `lang`, viewport metadata, and relative local asset URLs. If a new logical category is introduced, add its explicit prefix mapping in the catalog script.

Use compiled Tailwind CSS, not the Play CDN or a mutable third-party browser compiler. Keep template-specific theme values in `:root`; add or edit utility classes and run `npm run build`. Alpine-dependent demos must load `assets/vendor/alpine.min.js` at the correct relative depth. Do not introduce analytics, tracking scripts, secrets, or credential-bearing requests into demo pages.

Use visible labels, meaningful alternative text, semantic controls, keyboard-accessible interactions, focus indicators and reduced-motion behavior. Clearly distinguish demonstrative placeholders from completed interactions. Do not replace missing alt text with `alt=""` merely to silence the audit: empty alt is appropriate only for genuinely decorative or redundant images.

## Development

```sh
npm ci
npm run build
npm test
npm run audit
npx playwright install chromium
npm run test:browser
```

Commit source and generated outputs together. After rebuilding a second time there should be no additional generated diff. Review `audit-results/static.json` and `audit-results/browser-smoke.json`; boot success does not certify every interaction or viewport. Browser artifacts are generated and ignored by Git.

## Historical generators

`generate_*.py` scripts require `--output-dir`, refuse overwrites by default and never invoke Git. Use a disposable directory, compare output, and promote changes deliberately. Never restore `git add .`, auto-commit, automatic pushes to `dev`, or exception swallowing. The manually maintained HTML files are authoritative; generators are not a replacement for reviewing them.

## Pull requests

Describe the affected IDs and why the change improves the collection. Include verification commands and screenshots for visual work. Keep dependency updates separately reviewable, refresh the lockfile with npm, retain third-party license notices, and rerun the complete check. Do not claim WCAG compliance or universal responsiveness from a single automated test.
