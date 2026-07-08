// GitHub Pages uyumluluk katmani: sunucu 301'i olmayan ortamlar icin
// migration.config.json'daki her kural icin eski yolda meta-refresh + canonical
// stub HTML uretir. Cloudflare'e gecildiginde _redirects gercek 301 doner;
// stublar zararsiz sekilde golgede kalir.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const dist = join(root, 'dist');
if (!existsSync(dist)) {
  console.error('[redirect-stubs] dist/ yok — once astro build calistir.');
  process.exit(1);
}

const config = JSON.parse(readFileSync(join(root, 'config', 'migration.config.json'), 'utf8'));
const host = `https://${config.canonicalHost}`;

let written = 0;
let skipped = 0;

for (const { from, to } of config.redirects) {
  if (from === '/' || from === '/index.html') { skipped++; continue; }

  const target = `${host}${to}`;
  const stubPath = from.endsWith('.html')
    ? join(dist, from)
    : join(dist, from, 'index.html');

  if (!from.endsWith('.html') && existsSync(stubPath)) {
    // Gercek sayfa uretilmisse stub ile EZME
    skipped++;
    continue;
  }

  mkdirSync(dirname(stubPath), { recursive: true });
  writeFileSync(stubPath, `<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<title>Yönlendiriliyor…</title>
<meta http-equiv="refresh" content="0; url=${target}">
<link rel="canonical" href="${target}">
<meta name="robots" content="noindex">
<script>location.replace(${JSON.stringify(target)});</script>
</head>
<body>
<p>Bu sayfa taşındı: <a href="${target}">${target}</a></p>
</body>
</html>
`);
  written++;
}

// GitHub Pages gereksinimleri
writeFileSync(join(dist, 'CNAME'), config.canonicalHost + '\n');
writeFileSync(join(dist, '.nojekyll'), '');

// Eski GSC kayitlarinda /sitemap.xml gonderilmis olabilir — index'in kopyasini sun
const sitemapIndex = join(dist, 'sitemap-index.xml');
if (existsSync(sitemapIndex)) {
  writeFileSync(join(dist, 'sitemap.xml'), readFileSync(sitemapIndex));
}

console.log(`[redirect-stubs] ${written} stub yazildi, ${skipped} atlandi. CNAME + .nojekyll eklendi.`);
