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

const services = config.services.map((s) => `- [${s.name}](${domain}/hizmetler/${s.slug}/): ${s.description}`).join('\n');

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
Güncel fiyat listesi: ${domain}/fiyatlar/ — Halı ve koltuk yıkama metrekare/adet bazlıdır; net fiyat için WhatsApp'tan fotoğraf gönderilir.

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
