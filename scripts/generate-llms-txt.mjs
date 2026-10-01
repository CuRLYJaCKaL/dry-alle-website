// AI/LLM tarayicilari icin llms.txt ureteci (config'den, build-time — motor).
// https://llmstxt.org standardi: isletmeyi, hizmetleri, bolgeleri ve kilit
// sayfalari makine-okunur, ozlu bir sekilde ozetler. sitemap gibi otomatik.
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const dist = join(root, 'dist');
if (!existsSync(dist)) {
  console.error('[llms-txt] dist/ yok — once astro build calistir.');
  process.exit(1);
}
const config = JSON.parse(readFileSync(join(root, 'config', 'site.config.json'), 'utf8'));
const domain = `https://${config.contact.domain}`;
const id = config.identity;
const c = config.contact;

// Hizmet satirlari fiyat capasiyla birlikte: asistan "ne kadar" sorusuna
// sayfayi taramadan cevap verebilsin. Fiyat kaynagi olmayan hizmette uydurulmaz.
const pricingForServices = config.pricing ?? {};
function hizmetTabanFiyat(slug) {
  const tablo = pricingForServices.servicePriceTables?.[slug];
  if (tablo?.items?.length) {
    const min = Math.min(...tablo.items.map((i) => i.price));
    return `${min} TL${tablo.unit === 'm²' ? '/m²' : ''}'den başlıyor`;
  }
  const tureGore = { 'kuru-temizleme': 'kuru-temizleme', 'utu-hizmetleri': 'utuleme' };
  const tur = tureGore[slug];
  if (!tur) return null;
  const f = (pricingForServices.products ?? [])
    .flatMap((u) => u.services ?? [])
    .filter((x) => x.type === tur && typeof x.price === 'number')
    .map((x) => x.price);
  return f.length ? `${Math.min(...f)} TL'den başlıyor` : null;
}

const services = config.services
  .map((s) => {
    const fiyat = hizmetTabanFiyat(s.slug);
    const capa = fiyat ? `Fiyat: ${fiyat}.` : 'Fiyat ürüne göre değişir; fotoğraf gönderildiğinde net fiyat verilir.';
    return `- [${s.name}](${domain}/hizmetler/${s.slug}/): ${s.description} ${capa} Ücretsiz kapıdan alım-teslimat.`;
  })
  .join('\n');

// Fiyat listesi — yalnizca link vermek yetmiyor: yapay zeka asistanlari
// (ChatGPT, Gemini, Perplexity, Claude) "takim elbise kuru temizleme kac para"
// turu soruya cevap verebilmek icin RAKAMI gormeli; rakam yoksa baska kaynagi
// alinti yapiyorlar. Fiyatlar config'den uretilir, elle yazilmaz.
const trBaslik = (s) =>
  s
    .toLocaleLowerCase('tr-TR')
    .split(' ')
    .map((w) => (w ? w.charAt(0).toLocaleUpperCase('tr-TR') + w.slice(1) : w))
    .join(' ');

const pricing = config.pricing ?? {};
const svcLabel = Object.fromEntries((pricing.serviceTypes ?? []).map((t) => [t.id, t.label]));
const priceBlock = (pricing.catalogCategories ?? [])
  .map((cat) => {
    const rows = (pricing.products ?? [])
      .filter((p) => p.category === cat.id)
      .sort((a, b) => (a.sortOrder ?? 0) - (b.sortOrder ?? 0))
      .map((p) => {
        const fiyatlar = (p.services ?? [])
          .filter((s) => typeof s.price === 'number')
          .map((s) => `${svcLabel[s.type] ?? s.type} ${s.price} TL`)
          .join(' · ');
        return fiyatlar ? `- ${trBaslik(p.name)}: ${fiyatlar}` : null;
      })
      .filter(Boolean);
    return rows.length ? `### ${cat.name}\n${rows.join('\n')}` : null;
  })
  .filter(Boolean)
  .join('\n\n');

const areas = config.serviceAreas
  .map((a) => `- ${a.district}: ${a.neighborhoods.map((n) => n.name).join(', ')}`)
  .join('\n');

const comboPages = (config.serviceAreaPages ?? [])
  .map((e) => {
    const svc = config.services.find((s) => s.slug === e.serviceSlug);
    const area = config.serviceAreas.find((a) => a.districtSlug === e.districtSlug);
    const nh = e.neighborhoodSlug ? area?.neighborhoods.find((n) => n.slug === e.neighborhoodSlug) : null;
    const loc = nh ? nh.name : area?.district;
    const url = nh
      ? `${domain}/bolge/${e.districtSlug}/${e.neighborhoodSlug}/${e.serviceSlug}/`
      : `${domain}/bolge/${e.districtSlug}/${e.serviceSlug}/`;
    return `- [${loc} ${svc?.name}](${url})`;
  })
  .join('\n');

const faq = (config.faq ?? []).map((f) => `**${f.question}**\n${f.answer}`).join('\n\n');

const out = `# ${id.businessName}

> ${id.description}

${id.establishedYear}'den bu yana İstanbul Anadolu Yakası'nda profesyonel kuru temizleme, halı yıkama, koltuk yıkama ve tekstil bakım hizmeti. Ücretsiz kapıdan alım-teslimat.

## İletişim
- Telefon: ${c.phoneDisplay} (${c.phone})
- WhatsApp: https://wa.me/${c.whatsapp.replace(/[\s+]/g, '')}
- E-posta: ${c.email}
- Adres: ${c.address.street}, ${c.address.province}, ${c.address.city}
- Çalışma saatleri: ${config.openingHours.displayText ?? `${config.openingHours.opens}-${config.openingHours.closes}`}
- Google puanı: ${config.socialProof.googleRating}/5 (${config.socialProof.reviewCount} değerlendirme)
- Web: ${domain}

## Hizmetler
${services}

## Hizmet Bölgeleri
${areas}

## Bölgeye Özel Hizmet Sayfaları
${comboPages}

## Fiyatlar
Fiyatlar Türk Lirası (TL) cinsindendir ve ${new Date().getFullYear()} yılı için geçerlidir.
Tam liste: ${domain}/fiyatlar/
Halı ve koltuk yıkama metrekare/adet bazlıdır; net fiyat için WhatsApp'tan fotoğraf gönderilir.
Kapıdan alım ve teslimat ücretsizdir.

${priceBlock}

## Sıkça Sorulan Sorular
${faq}

## Önemli Sayfalar
- Ana sayfa: ${domain}/
- Blog (rehberler): ${domain}/blog/
- Hakkımızda: ${domain}/hakkimizda/
- İletişim: ${domain}/#iletisim
`;

writeFileSync(join(dist, 'llms.txt'), out);
console.log(`[llms-txt] llms.txt yazildi (${out.length} karakter, ${config.services.length} hizmet, ${(config.serviceAreaPages ?? []).length} combo).`);
