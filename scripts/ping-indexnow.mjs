// IndexNow — Bing ve Yandex'e "bu URL'ler degisti" bildirimi.
// Neden: Google sitemap'i sik tarar ama Bing/Yandex degisikligi haftalar sonra
// gorebiliyor. IndexNow tek istekte anlik bildirim yapar; iki motor da destekler.
// Yalnizca KAYNAK degistiginde calistirilir (gunluk bos build'de degil) —
// degismeyen URL'leri tekrar tekrar bildirmek spam sayilir.
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const dist = join(root, 'dist');
if (!existsSync(dist)) { console.error('[indexnow] dist/ yok'); process.exit(1); }

const config = JSON.parse(readFileSync(join(root, 'config', 'site.config.json'), 'utf8'));
const host = config.contact.domain;

// Anahtar dosyasi: public/ icindeki <key>.txt — build sonrasi dist kokunde olur.
const anahtarDosya = readdirSync(dist).find((f) => /^[0-9a-f]{8,128}\.txt$/.test(f));
if (!anahtarDosya) { console.error('[indexnow] anahtar dosyasi bulunamadi, atlandi'); process.exit(0); }
const key = anahtarDosya.replace(/\.txt$/, '');

// URL listesi sitemap'ten — tek dogru kaynak.
const sitemaps = readdirSync(dist).filter((f) => /^sitemap.*\.xml$/.test(f));
const urls = [...new Set(sitemaps.flatMap((f) =>
  [...readFileSync(join(dist, f), 'utf8').matchAll(/<loc>(.*?)<\/loc>/g)].map((m) => m[1])
))].filter((u) => !u.endsWith('.xml'));

if (urls.length === 0) { console.error('[indexnow] URL bulunamadi'); process.exit(0); }

const govde = {
  host,
  key,
  keyLocation: `https://${host}/${anahtarDosya}`,
  urlList: urls.slice(0, 10000),
};

const res = await fetch('https://api.indexnow.org/IndexNow', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: JSON.stringify(govde),
});
console.log(`[indexnow] ${urls.length} URL gonderildi -> HTTP ${res.status} ${res.statusText}`);
// 200/202 basarili. Hata build'i DURDURMAZ: yayin zaten tamamlandi, bildirim ikincil.
if (!res.ok) console.error('[indexnow] UYARI: bildirim basarisiz, yayin etkilenmedi');
