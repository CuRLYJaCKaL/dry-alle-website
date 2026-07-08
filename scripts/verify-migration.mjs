#!/usr/bin/env node
/**
 * verify-migration.mjs
 *
 * SEO koruma dogrulamasi: eski sitenin hicbir URL'si 404'e dusmemeli.
 *
 * Kontrol edilen kaynaklar:
 *   1. migration/legacy-sitemap.xml icindeki tum URL'ler
 *   2. config/migration.config.json icindeki tum "from" degerleri
 *
 * Her eski URL icin kural:
 *   - URL yeni sitede birebir karsilaniyor (dist altinda index.html'i var) YA DA
 *   - redirect'i var VE redirect hedefi dist'te gercekten uretilmis.
 *
 * Ek kurallar:
 *   - Blog URL'leri (/blog/{slug}/) birebir korunmali; dist/blog/{slug}/index.html
 *     yoksa HATA (redirect ile gecistirilemez).
 *   - Redirect zinciri (hedefin kendisi baska bir redirect'in "from"u) HATA.
 *
 * Cikis kodu: herhangi bir eski URL karsiliksizsa 1, aksi halde 0.
 */

import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '..');
const sitemapPath = join(rootDir, 'migration', 'legacy-sitemap.xml');
const configPath = join(rootDir, 'config', 'migration.config.json');
const distDir = join(rootDir, 'dist');

if (!existsSync(distDir)) {
  console.error('[verify-migration] HATA: dist/ dizini bulunamadi. Once build calistirin.');
  process.exit(1);
}
if (!existsSync(sitemapPath)) {
  console.error(`[verify-migration] HATA: legacy sitemap yok: ${sitemapPath}`);
  process.exit(1);
}
if (!existsSync(configPath)) {
  console.error(`[verify-migration] HATA: migration config yok: ${configPath}`);
  process.exit(1);
}

/** @type {{ canonicalHost: string, redirects: Array<{from: string, to: string, status: number}> }} */
const config = JSON.parse(readFileSync(configPath, 'utf8'));

/** from -> to eslemesi */
const redirectMap = new Map();
for (const rule of config.redirects) {
  redirectMap.set(rule.from, rule.to);
}

/**
 * Bir path'in dist altinda statik olarak uretilip uretilmedigini kontrol eder.
 * "/x/y/" -> dist/x/y/index.html ; "/" -> dist/index.html
 * ".html" ile biten eski dosya yollari yeni sitede uretilmez, false doner.
 */
function existsInDist(urlPath) {
  if (urlPath.endsWith('.html')) {
    return existsSync(join(distDir, ...urlPath.split('/').filter(Boolean)));
  }
  const parts = urlPath.split('/').filter(Boolean);
  return existsSync(join(distDir, ...parts, 'index.html'));
}

/** Sitemap'ten path listesi cikar. */
function parseSitemapPaths(xml) {
  const paths = [];
  const re = /<loc>\s*([^<\s]+)\s*<\/loc>/g;
  let m;
  while ((m = re.exec(xml)) !== null) {
    const u = new URL(m[1]);
    paths.push(u.pathname);
  }
  return paths;
}

const sitemapPaths = parseSitemapPaths(readFileSync(sitemapPath, 'utf8'));

// Dogrulanacak tum eski URL'ler: sitemap + redirect "from"lari (tekillestirilmis)
const allOldPaths = [...new Set([...sitemapPaths, ...redirectMap.keys()])];

const errors = [];
let servedDirect = 0;
let servedByRedirect = 0;

// 1) Redirect zinciri kontrolu: hicbir "to" baska bir "from" olmamali.
for (const [from, to] of redirectMap) {
  if (redirectMap.has(to)) {
    errors.push(`REDIRECT ZINCIRI: ${from} -> ${to} -> ${redirectMap.get(to)} (hedef baska bir redirect)`);
  }
}

// 2) Redirect hedefleri dist'te gercekten uretilmis mi?
for (const [from, to] of redirectMap) {
  if (!existsInDist(to)) {
    errors.push(`REDIRECT HEDEFI YOK: ${from} -> ${to} (dist'te uretilmemis)`);
  }
}

// 3) Her eski URL karsilaniyor mu?
const blogPageRe = /^\/blog\/[^/]+\/$/;

for (const oldPath of allOldPaths) {
  const isBlogPage = blogPageRe.test(oldPath);

  if (isBlogPage) {
    // Blog URL'leri birebir korunmak zorunda; redirect kabul edilmez.
    if (!existsInDist(oldPath)) {
      errors.push(`BLOG URL KAYIP: ${oldPath} (dist${oldPath}index.html yok — blog URL'leri birebir korunmali)`);
    } else {
      servedDirect++;
    }
    continue;
  }

  if (existsInDist(oldPath)) {
    servedDirect++;
    continue;
  }

  const to = redirectMap.get(oldPath);
  if (to !== undefined) {
    // Hedef ve zincir kontrolleri yukarida yapildi; burada sadece sayiyoruz.
    if (existsInDist(to) && !redirectMap.has(to)) {
      servedByRedirect++;
    } else {
      errors.push(`GECERSIZ REDIRECT: ${oldPath} -> ${to}`);
    }
    continue;
  }

  errors.push(`KARSILIKSIZ URL: ${oldPath} (ne birebir uretim ne de redirect var — 404 olur)`);
}

// Ozet rapor
console.log('================ MIGRATION DOGRULAMA RAPORU ================');
console.log(`Legacy sitemap URL sayisi     : ${sitemapPaths.length}`);
console.log(`Redirect kurali sayisi        : ${redirectMap.size}`);
console.log(`Toplam kontrol edilen eski URL: ${allOldPaths.length}`);
console.log(`  Birebir karsilanan          : ${servedDirect}`);
console.log(`  Redirect ile karsilanan     : ${servedByRedirect}`);
console.log(`  Hata                        : ${errors.length}`);
console.log('=============================================================');

if (errors.length > 0) {
  console.error('\nHATALAR:');
  for (const e of errors) console.error(`  - ${e}`);
  console.error(`\n[verify-migration] BASARISIZ: ${errors.length} sorun bulundu.`);
  process.exit(1);
}

console.log('\n[verify-migration] BASARILI: tum eski URL\'ler karsilaniyor, 404 yok.');
