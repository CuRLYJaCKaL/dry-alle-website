#!/usr/bin/env node
// SEO BUTUNLUK KAPISI — build sonrasi dist/ taranir.
//
// Neden var: interpolate() tanimsiz token'i sessizce bos string yapiyor.
// Ana sayfa aciklamasi aylarca "Yakasi'nda 'den bu yana..." diye yayinda
// kaldi ve kimse fark etmedi (Eyl 2026'da GSC'den yakalandi).
// Bu kapi o hata sinifini build'de durdurur.
//
// HATA (build durur): cozulmemis {token}, bos token artigi, eksik canonical /
//   H1 / title / JSON-LD, ayni basligi paylasan indekslenebilir sayfalar.
// UYARI (build devam eder, raporlanir): baslik 50-60, aciklama 140-160 disi.

import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const DIST = 'dist';
const TITLE_MIN = 50, TITLE_MAX = 60;
const DESC_MIN = 140, DESC_MAX = 160;

function walk(dir) {
  const out = [];
  for (const e of readdirSync(dir)) {
    const p = join(dir, e);
    if (statSync(p).isDirectory()) out.push(...walk(p));
    else if (e.endsWith('.html')) out.push(p);
  }
  return out;
}

const pick = (html, re) => {
  const m = html.match(re);
  return m ? m[1].replace(/\s+/g, ' ').trim() : '';
};

const decode = (s) =>
  s.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
   .replace(/&quot;/g, '"').replace(/&#39;/g, "'");

const errors = [];
const warnings = [];
const titles = new Map();
let indexable = 0, stubs = 0;

for (const file of walk(DIST)) {
  const html = readFileSync(file, 'utf8');
  const rel = file.replace(/^dist/, '').replace(/index\.html$/, '') || '/';
  // Arama motoru dogrulama dosyalari (google<hash>.html, BingSiteAuth.xml vb.)
  // icerik sayfasi degildir: basligi, canonical'i, H1'i olmaz.
  if (/^\/(google[0-9a-f]+|BingSiteAuth|yandex_[0-9a-f]+)\.html$/i.test(rel)) continue;

  const isStub = /name="robots"[^>]*noindex|content="[^"]*noindex/i.test(html);
  if (isStub) { stubs++; continue; }
  indexable++;

  const title = decode(pick(html, /<title[^>]*>(.*?)<\/title>/s));
  const desc = decode(pick(html, /<meta name="description" content="(.*?)"/s));
  const canonical = pick(html, /<link rel="canonical" href="([^"]+)"/);
  const h1count = (html.match(/<h1[\s>]/g) || []).length;
  const hasLd = /<script type="application\/ld\+json">/.test(html);

  // ── HATALAR ──
  // Cozulmemis {token} — sayfanin HER yerinde aranir, yalnizca title/meta'da degil.
  // (Zaman token'lari gorsel metinde de kullaniliyor; interpolate'i atlayan bir
  // render yolu olursa ziyaretci "{experienceYears} yillik deneyim" goruyor.)
  const unresolved = [...html.matchAll(/\{(currentYear|experienceYears|businessName|brandName|location|serviceName|establishedYear|sectorLabel|primaryKeyword\w*|province)\}/g)].map((m) => m[1]);
  if (unresolved.length) errors.push(`${rel} — cozulmemis token: {${[...new Set(unresolved)].join('}, {')}}`);

  for (const [alan, deger] of [['baslik', title], ['aciklama', desc]]) {
    if (!deger) { errors.push(`${rel} — ${alan} bos`); continue; }
    if (/\s{2,}/.test(deger)) errors.push(`${rel} — ${alan}'da cift bosluk (bos token artigi?): "${deger.slice(0, 70)}"`);
    if (/(^|\s)['’](den|dan|ten|tan)\s/.test(deger)) errors.push(`${rel} — ${alan}'da sahipsiz ek, token bos kalmis: "${deger.slice(0, 70)}"`);
    if (/\|\s*$|^\s*\||\|\s*\|/.test(deger)) errors.push(`${rel} — ${alan}'da bos ayrac: "${deger.slice(0, 70)}"`);
  }

  if (!canonical) errors.push(`${rel} — canonical yok`);
  if (h1count !== 1) errors.push(`${rel} — H1 sayisi ${h1count} (tam 1 olmali)`);
  if (!hasLd) errors.push(`${rel} — JSON-LD yok`);

  if (title) {
    if (!titles.has(title)) titles.set(title, []);
    titles.get(title).push(rel);
  }

  // ── UYARILAR ──
  if (title && (title.length < TITLE_MIN || title.length > TITLE_MAX))
    warnings.push({ tip: 'baslik', rel, len: title.length, metin: title });
  if (desc && (desc.length < DESC_MIN || desc.length > DESC_MAX))
    warnings.push({ tip: 'aciklama', rel, len: desc.length, metin: desc });
}

// ── CONFIG BAYATLAMA KORUMASI ──
// Zamana bagli deger config'e SABIT yazilamaz: {currentYear} / {experienceYears}
// kullanilmali. Aksi halde site 1 Ocak'ta sessizce bayatlar.
{
  const cfg = JSON.parse(readFileSync('config/site.config.json', 'utf8'));
  const simdikiYil = new Date().getFullYear();
  const bayat = [];
  const gez = (o, yol = '') => {
    if (o && typeof o === 'object') {
      for (const [k, v] of Object.entries(o)) gez(v, yol ? `${yol}.${k}` : k);
    } else if (typeof o === 'string') {
      if (yol.endsWith('identity.establishedYear')) return;
      for (let y = simdikiYil - 1; y <= simdikiYil + 1; y++)
        if (new RegExp(`\\b${y}\\b`).test(o)) bayat.push(`${yol}: sabit yil "${y}" -> {currentYear} kullan`);
      const m = o.match(/(?<![0-9])(\d{1,2})\s*yıl(lık|ı|dır)/);
      if (m) bayat.push(`${yol}: sabit sure "${m[0]}" -> {experienceYears} kullan`);
    }
  };
  gez(cfg);
  for (const b of bayat) errors.push(`config — ${b}`);
}

for (const [title, pages] of titles) {
  if (pages.length > 1) errors.push(`Ayni baslik ${pages.length} sayfada: "${title.slice(0, 60)}" -> ${pages.slice(0, 3).join(', ')}`);
}

const uzunBaslik = warnings.filter((w) => w.tip === 'baslik' && w.len > TITLE_MAX);
const kisaBaslik = warnings.filter((w) => w.tip === 'baslik' && w.len < TITLE_MIN);
const aciklamaUyari = warnings.filter((w) => w.tip === 'aciklama');

console.log('================ SEO BUTUNLUK RAPORU ================');
console.log(`Indekslenebilir sayfa        : ${indexable}`);
console.log(`Yonlendirme stub (atlandi)   : ${stubs}`);
console.log(`Hata                         : ${errors.length}`);
console.log(`Uyari - baslik ${TITLE_MAX}+ karakter : ${uzunBaslik.length}`);
console.log(`Uyari - baslik ${TITLE_MIN}- karakter : ${kisaBaslik.length}`);
console.log(`Uyari - aciklama ${DESC_MIN}-${DESC_MAX} disi: ${aciklamaUyari.length}`);
console.log('=====================================================');

if (uzunBaslik.length) {
  console.log('\nEn uzun 5 baslik (Google kirpar):');
  for (const w of uzunBaslik.sort((a, b) => b.len - a.len).slice(0, 5))
    console.log(`  ${w.len} kr  ${w.rel}`);
}

if (errors.length) {
  console.error('\n[verify-seo] HATA — build durduruldu:');
  for (const e of errors.slice(0, 40)) console.error(`  - ${e}`);
  if (errors.length > 40) console.error(`  ... ve ${errors.length - 40} hata daha`);
  process.exit(1);
}

console.log('\n[verify-seo] BASARILI: token, canonical, H1, JSON-LD ve baslik tekrari temiz.');
