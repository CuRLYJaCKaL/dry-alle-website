#!/usr/bin/env node
/**
 * verify-contact.mjs
 *
 * Iletisim tutarlilik kapisi: dist'te uretilmis TUM tiklanabilir iletisim
 * linkleri (tel: ve wa.me) config/site.config.json'daki resmi numarayla
 * birebir ayni olmali. Amac: numara config'de degistiginde blog/icerik
 * gibi elle yazilmis yerlerde ESKI numarali link kalmasini onlemek —
 * musteri olu/yanlis numarayi aramasin.
 *
 * Kapsam: yalnizca href="tel:..." ve href="...wa.me/<rakam>..." (prose degil).
 *   - Numarasiz paylasim linkleri (wa.me/?text=...) atlanir.
 * Cikis kodu: herhangi bir link config numarasindan farkliysa 1, aksi halde 0.
 */

import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '..');
const distDir = join(rootDir, 'dist');
const configPath = join(rootDir, 'config', 'site.config.json');

if (!existsSync(distDir)) {
  console.error('[verify-contact] HATA: dist/ dizini bulunamadi. Once build calistirin.');
  process.exit(1);
}
if (!existsSync(configPath)) {
  console.error(`[verify-contact] HATA: config yok: ${configPath}`);
  process.exit(1);
}

const config = JSON.parse(readFileSync(configPath, 'utf8'));
const onlyDigits = (s) => (s || '').replace(/\D/g, '');
const canonicalWa = onlyDigits(config?.contact?.whatsapp);
const canonicalPhone = onlyDigits(config?.contact?.phone);

if (!canonicalWa || !canonicalPhone) {
  console.error('[verify-contact] HATA: config.contact.whatsapp / phone okunamadi.');
  process.exit(1);
}

// Gecerli kabul edilen numaralar (whatsapp ve phone ayni olsa da ikisini de kabul et)
const validNumbers = new Set([canonicalWa, canonicalPhone]);

/** dist altindaki tum .html dosyalarini topla. */
function collectHtml(dir) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) out.push(...collectHtml(full));
    else if (entry.endsWith('.html')) out.push(full);
  }
  return out;
}

const htmlFiles = collectHtml(distDir);

const telRe = /href="tel:([^"]+)"/g;
const waRe = /href="[^"]*wa\.me\/([0-9]+)[^"]*"/g;

const errors = [];
let telChecked = 0;
let waChecked = 0;

for (const file of htmlFiles) {
  const html = readFileSync(file, 'utf8');
  const rel = file.slice(distDir.length);
  let m;

  telRe.lastIndex = 0;
  while ((m = telRe.exec(html)) !== null) {
    const num = onlyDigits(m[1]);
    if (!num) continue; // bos tel: (olmamali) — atla
    telChecked++;
    if (!validNumbers.has(num)) {
      errors.push(`TEL UYUSMAZLIGI: ${rel} → tel:${m[1]} (rakam ${num}, beklenen ${canonicalPhone})`);
    }
  }

  waRe.lastIndex = 0;
  while ((m = waRe.exec(html)) !== null) {
    const num = onlyDigits(m[1]);
    if (!num) continue; // numarasiz paylasim linki — atla
    waChecked++;
    if (!validNumbers.has(num)) {
      errors.push(`WA UYUSMAZLIGI: ${rel} → wa.me/${m[1]} (rakam ${num}, beklenen ${canonicalWa})`);
    }
  }
}

console.log('================ ILETISIM TUTARLILIK RAPORU ================');
console.log(`Resmi numara (whatsapp/phone) : ${canonicalWa} / ${canonicalPhone}`);
console.log(`Taranan HTML dosyasi          : ${htmlFiles.length}`);
console.log(`Kontrol edilen tel: link      : ${telChecked}`);
console.log(`Kontrol edilen wa.me link     : ${waChecked}`);
console.log(`Uyusmazlik                    : ${errors.length}`);
console.log('===========================================================');

if (errors.length > 0) {
  console.error('\nHATALAR (config numarasi degistiyse bu icerikleri de guncelleyin):');
  for (const e of errors) console.error(`  - ${e}`);
  console.error(`\n[verify-contact] BASARISIZ: ${errors.length} link config numarasiyla uyusmuyor.`);
  process.exit(1);
}

console.log('\n[verify-contact] BASARILI: tum iletisim linkleri config numarasiyla tutarli.');
