// Rewrites a finished build in dist/ so it can live in a subfolder, e.g.
//   node scripts/subpath.mjs /smarts.studio https://pranka.id.lv
import { readdirSync, readFileSync, writeFileSync, statSync, rmSync, existsSync } from 'node:fs';
import { join } from 'node:path';
const [base, origin] = process.argv.slice(2);
if (!base || !origin) { console.error('usage: subpath.mjs /folder https://host'); process.exit(1); }
const walk = d => readdirSync(d).flatMap(f => { const p = join(d, f); return statSync(p).isDirectory() ? walk(p) : [p]; });
let n = 0;
for (const f of walk('dist')) {
  if (!f.endsWith('.html')) continue;
  let s = readFileSync(f, 'utf8');
  s = s.replace(/\bsrcset="([^"]*)"/g, (m, v) => `srcset="${v.replace(/(^|,\s*)\/(?!\/)/g, `$1${base}/`)}"`);
  s = s.replace(/\b(href|src|action)="\/(?!\/)/g, `$1="${base}/`).replaceAll('https://smarts.studio/', `${origin}${base}/`);
  writeFileSync(f, s); n++;
}
if (existsSync('dist/_redirects')) rmSync('dist/_redirects'); // only Cloudflare understands this file
console.log(`rewrote ${n} pages for ${origin}${base}/`);
