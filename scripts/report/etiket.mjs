// Sayfa yollarini insan okuyabilecegi adlara cevirir.
// "/" satirini raporda goren kisi bunun ana sayfa oldugunu anlamiyordu;
// adlar config'den (ve blog dosyalarinin frontmatter'indan) TURETILIR,
// elle liste tutulmaz — yeni hizmet/bolge eklenince kendiliginden calisir.
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const kok = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
const config = JSON.parse(readFileSync(join(kok, 'config', 'site.config.json'), 'utf8'));

const hizmet = new Map(config.services.map((s) => [s.slug, s.name]));
const ilce = new Map(config.serviceAreas.map((a) => [a.districtSlug, a.district]));
const mahalle = new Map(
  config.serviceAreas.flatMap((a) => a.neighborhoods.map((n) => [`${a.districtSlug}/${n.slug}`, n.name])),
);

// Blog basliklari — frontmatter'daki title. Dosya yoksa slug'dan okunakli ad uretilir.
const blog = new Map();
const blogDizin = join(kok, 'src', 'content', 'blog');
if (existsSync(blogDizin)) {
  for (const dosya of readdirSync(blogDizin).filter((f) => f.endsWith('.md'))) {
    const m = readFileSync(join(blogDizin, dosya), 'utf8').match(/^---[\s\S]*?\ntitle:\s*(.+?)\s*$/m);
    if (m) blog.set(dosya.replace(/\.md$/, ''), m[1].replace(/^["']|["']$/g, ''));
  }
}

// Tekil sayfalar — bunlarin config'de karsiligi yok.
const sabit = {
  '/': 'Ana sayfa',
  '/fiyatlar/': 'Fiyat listesi',
  '/siparis/': 'Online sipariş',
  '/hakkimizda/': 'Hakkımızda',
  '/blog/': 'Blog',
  '/hizmetler/': 'Hizmetler',
  '/bolge/': 'Hizmet bölgeleri',
  '/iletisim/': 'İletişim',
};

const okunakli = (s) =>
  s.replace(/-/g, ' ').replace(/\S+/g, (w) => w.charAt(0).toLocaleUpperCase('tr-TR') + w.slice(1));

const kisalt = (s, n = 42) => (s.length > n ? `${s.slice(0, n - 1).trimEnd()}…` : s);

/** Yol -> okunabilir ad. Eslesme bulunamazsa slug'dan makul bir ad uretir. */
export function sayfaAdi(yol) {
  const y = (yol || '/').split('?')[0].split('#')[0];
  const temiz = y === '/' ? '/' : `/${y.replace(/^\/|\/$/g, '')}/`;
  if (sabit[temiz]) return sabit[temiz];

  const p = temiz.replace(/^\/|\/$/g, '').split('/').filter(Boolean);

  if (p[0] === 'hizmetler' && p[1]) return hizmet.get(p[1]) ?? okunakli(p[1]);
  if (p[0] === 'blog' && p[1]) return kisalt(blog.get(p[1]) ?? okunakli(p[1]));
  if (p[0] === 'bolge' && p[1]) {
    const ilceAd = ilce.get(p[1]) ?? okunakli(p[1]);
    if (!p[2]) return `${ilceAd} bölgesi`;
    // 3 segment: ya ilce+hizmet ya ilce+mahalle
    const mahalleAd = mahalle.get(`${p[1]}/${p[2]}`);
    if (!p[3]) {
      if (mahalleAd) return `${mahalleAd} (${ilceAd})`;
      const h = hizmet.get(p[2]);
      return h ? `${ilceAd} · ${h}` : `${ilceAd} · ${okunakli(p[2])}`;
    }
    const h = hizmet.get(p[3]) ?? okunakli(p[3]);
    return kisalt(`${mahalleAd ?? okunakli(p[2])} · ${h}`);
  }
  return kisalt(okunakli(p[p.length - 1] ?? 'Ana sayfa'));
}
