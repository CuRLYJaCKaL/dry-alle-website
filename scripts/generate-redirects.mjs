#!/usr/bin/env node
/**
 * generate-redirects.mjs
 *
 * config/migration.config.json içindeki redirect tablosunu okur ve
 * Cloudflare Pages / Netlify uyumlu dist/_redirects dosyasini uretir.
 *
 * Kullanim: node scripts/generate-redirects.mjs
 * On kosul: `astro build` calismis ve dist/ dizini mevcut olmalidir.
 */

import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '..');
const configPath = join(rootDir, 'config', 'migration.config.json');
const distDir = join(rootDir, 'dist');
const outPath = join(distDir, '_redirects');

if (!existsSync(distDir)) {
  console.error('[generate-redirects] HATA: dist/ dizini bulunamadi.');
  console.error('Once `npm run build` (astro build) calistirilmalidir.');
  process.exit(1);
}

if (!existsSync(configPath)) {
  console.error(`[generate-redirects] HATA: konfigurasyon dosyasi yok: ${configPath}`);
  process.exit(1);
}

/** @type {{ canonicalHost: string, redirects: Array<{from: string, to: string, status: number}> }} */
const config = JSON.parse(readFileSync(configPath, 'utf8'));

if (!Array.isArray(config.redirects) || config.redirects.length === 0) {
  console.error('[generate-redirects] HATA: config.redirects bos veya tanimsiz.');
  process.exit(1);
}

// Ayni "from" iki kez tanimlanirsa ilk kural kazanir; bunu hata sayiyoruz.
const seen = new Set();
const lines = [];

for (const rule of config.redirects) {
  const { from, to, status } = rule;
  if (!from || !to || !status) {
    console.error(`[generate-redirects] HATA: eksik alanli kural: ${JSON.stringify(rule)}`);
    process.exit(1);
  }
  if (seen.has(from)) {
    console.error(`[generate-redirects] HATA: yinelenen "from": ${from}`);
    process.exit(1);
  }
  seen.add(from);
  lines.push(`${from} ${to} ${status}`);
}

writeFileSync(outPath, lines.join('\n') + '\n', 'utf8');
console.log(`[generate-redirects] ${lines.length} redirect yazildi -> ${outPath}`);
