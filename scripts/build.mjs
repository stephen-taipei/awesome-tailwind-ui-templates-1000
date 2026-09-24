/** Deterministic, local-only build. Package installation is deliberately separate. */
import { readFile, writeFile, mkdir, copyFile } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
process.chdir(root);
function run(command, args) {
  const result = spawnSync(command, args, { cwd: root, stdio: 'inherit' });
  if (result.error) throw result.error;
  if (result.status !== 0) throw new Error(`${command} exited with ${result.status}`);
}
run(process.env.PYTHON || 'python3', ['scripts/catalog.py']);
await mkdir('.build', { recursive: true });
await mkdir('assets/vendor', { recursive: true });
await mkdir('assets/css', { recursive: true });
const manifest = JSON.parse(await readFile('templates.json', 'utf8'));
const theme = await readFile('node_modules/tailwindcss/theme.css', 'utf8');
const main = await readFile('src/css/main.css', 'utf8');
const declaration = /(--[\w-]+)\s*:\s*([^;{}]+);/g;
const known = new Set([...theme.matchAll(declaration), ...main.matchAll(declaration)].map(match => match[1]));
const custom = new Map();
for (const template of manifest.templates) {
  const html = await readFile(template.path, 'utf8');
  for (const [, css] of html.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)) {
    for (const [, name, value] of css.matchAll(declaration)) {
      if (!known.has(name) && !custom.has(name)) custom.set(name, value.trim());
    }
  }
}
await writeFile('.build/theme.css', `/* Generated token registry. Per-page values live in template :root styles. */\n@theme {\n${[...custom].sort(([a], [b]) => a.localeCompare(b, 'en')).map(([name, value]) => `  ${name}: ${value};`).join('\n')}\n}\n`);
const cliRoot = 'node_modules/@tailwindcss/cli';
const cli = JSON.parse(await readFile(`${cliRoot}/package.json`, 'utf8'));
const executable = typeof cli.bin === 'string' ? cli.bin : cli.bin.tailwindcss;
run(process.execPath, [resolve(cliRoot, executable), '-i', 'src/css/main.css', '-o', 'assets/css/tailwind.css', '--minify']);
await copyFile('node_modules/alpinejs/dist/cdn.min.js', 'assets/vendor/alpine.min.js');
// Alpine's npm archive omits its license. The versioned upstream license is checked in.
for (const packageName of ['tailwindcss']) {
  const license = await readFile(`node_modules/${packageName}/LICENSE`, 'utf8');
  await writeFile(`assets/vendor/${packageName}.LICENSE.txt`, license);
}
const bytes = (await readFile('assets/css/tailwind.css')).length;
console.log(`Built ${manifest.total} templates. Shared CSS: ${bytes.toLocaleString('en')} bytes. No browser compiler.`);
