# AI Web Production Engine — Claude Code Rules

> Bu dosya Claude Code tarafindan otomatik okunur.
> Tum gelistirme bu kurallara tabidir. Ihlal edilemez.

## Projenin Amaci

Bu proje tek bir web sitesi degil, **sektor-agnostik bir web sitesi uretim motorudur**.
Ayni core mimari ile farkli sektorlere (kuru temizleme, pilates, okul, diyetisyen vb.)
sadece `config/site.config.json` degistirilerek site uretilir.

**Kod = uretim hatti. site.config.json = urun tarifi.**

---

## Tech Stack (Sabit — Degistirilemez)

| Teknoloji | Versiyon | Amac |
|-----------|----------|------|
| Astro | ^5.x (LTS) | Static site generation, SEO-first |
| TypeScript | strict mode | Tip guvenligi |
| Tailwind CSS | ^3.x | Utility-first styling, design tokens |
| JSON-LD | schema.org | Google Rich Results |
| Deploy | DigitalOcean App Platform | Production hosting |

### Yasaklar
- Next.js, Nuxt, SvelteKit gibi alternatif framework KULLANILAMAZ.
- React, Vue, Svelte gibi UI framework'leri EKLENMEZ (Astro native component yeterli).
- Harici CSS framework'u (Bootstrap, Bulma vb.) EKLENMEZ.
- Runtime JavaScript minimize edilir. Client-side JS sadece zorunlu interaksiyon icin.

---

## Mimari Kurallar

### 1. Core vs Profile Ayrimi

**CORE (sabit, degismez):**
- Sayfa turleri: homepage, service, area (bolge), blog
- URL yapisi
- SEO meta uretim mantigi
- H1 politikasi (sayfa basina 1 adet)
- Internal linking grafi
- CTA sayisi ve konumu
- Component yapisi ve sirasi
- Responsive davranis
- JSON-LD schema yapisi

**PROFILE (degisken, config'den gelir):**
- Isletme adi, sektoru
- Renkler (primary, secondary)
- Metinler (slogan, aciklama, hizmet isimleri)
- Hizmet listesi
- Bolge listesi (il/ilce/mahalle)
- SEO kelimeleri
- Iletisim bilgileri
- Gorseller

**KURAL:** Core davranisi degistirmek icin ASLA config'e boolean flag eklenmez.
Config sadece "neyle doldurulacagini" soyler, "nasil davranacagini" ASLA.

### 2. Single Source of Truth

`config/site.config.json` sistemin tek otoritesidir.
- Feature aktif mi? → config'de var mi yok mu, ona bak.
- Hangi bolgeler? → config'deki `serviceAreas` dizisi.
- Hangi hizmetler? → config'deki `services` dizisi.
- Renkler? → config'deki `brand` bolumu.

Config'de olmayan hicbir sey kodda hardcode edilemez.

#### Config Schema — Ana Bolumler

| Bolum | Amac | Zorunlu? |
|-------|------|----------|
| `identity` | businessName, brandName, sectorLabel, schemaType, heroDescription, establishedYear | Evet |
| `brand` | Renk token'lari, font, ses tonu | Evet |
| `contact` | Telefon, email, WhatsApp, adres, geo, domain, sosyal linkler | Evet |
| `seoTemplates` | Sayfa tiplerine gore title/description sablonlari ({token} syntax) | Evet |
| `contentTokens` | Yeniden kulllanilan metinler: valuePropositions, serviceHighlights, aboutTitle, valuePropositionDetails, aboutStoryParagraphs, aboutValues, regionVariants, regionSubtitleVariants | Evet |
| `services[]` | name, slug, icon, description + features[], detailParagraphs[], relatedBlogSlugs[] | Evet |
| `serviceAreas[]` | city, district, districtSlug, neighborhoods[] | Evet |
| `pricing` | categories[] (name, icon, items[]) — yoksa PriceTable render edilmez | Opsiyonel |
| `corporate` | title, description, bulletPoints[], sectors[], advantages[] — yoksa CorporateSection render edilmez | Opsiyonel |
| `conversionTokens` | primaryCTA, secondaryCTA, ctaPhone | Evet |
| `socialProof` | googleRating, reviewCount, testimonials[] | Evet |
| `faq[]` | question, answer | Evet |

**seoTemplates token'lari:** `{businessName}`, `{sectorLabel}`, `{province}`, `{location}`, `{serviceName}`, `{primaryKeyword}`, `{establishedYear}`

**Opsiyonel bolum kurali:** `pricing` ve `corporate` bolumleri yoksa veya bossa ilgili component render edilmez. Boolean flag GEREKMEZ.

### Utility Dosyasi: `src/utils/engine.ts`

Izin verilen tek utility dosyasi. 3 fonksiyon icerir:
- `interpolate(template, tokens)` — SEO sablonlarinda `{token}` → deger donusumu
- `deterministicIndex(slug, arrayLength)` — Bolge sayfalari icin varyant secimi (ayni slug = ayni varyant)
- `validateConfig(config)` — Build-time zorunlu alan kontrolu, eksikse build durdurulur

### 3. Component Mimarisi

Izin verilen component'ler (yenisi EKLENEMEZ, onay olmadan):
- `Header.astro` — Ust navigasyon, hamburger menu, CTA butonlari
- `Hero.astro` — Ana banner, tek H1
- `Services.astro` — Hizmet kartlari
- `ServiceAreas.astro` — Bolge listesi
- `About.astro` — Hakkimizda
- `CorporateSection.astro` — Ana sayfada kurumsal bolum
- `FAQ.astro` — Sikca sorulan sorular
- `Testimonials.astro` — Musteri yorumlari
- `Contact.astro` — Iletisim bilgileri + harita
- `WhatsAppCTA.astro` — Sabit WhatsApp butonu
- `Footer.astro` — Alt bilgi
- `SEOHead.astro` — Meta tags + JSON-LD + canonical
- `PriceTable.astro` — Fiyat listesi (akordeon + OfferCatalog JSON-LD)
- `Breadcrumb.astro` — Breadcrumb navigasyon (sayfa sablonlarinda inline uygulanir)

**KURAL:** Yeni component olusturmak icin kullanici onayi gerekir.
"Helper", "wrapper", "utility" component'leri YASAKTIR.

### 4. Sayfa Turleri ve URL Yapisi

| Sayfa Turu | URL Pattern | Kaynak |
|------------|-------------|--------|
| Ana Sayfa | `/` | `src/pages/index.astro` |
| Hizmet | `/hizmetler/{slug}/` | `src/pages/hizmetler/[slug].astro` |
| Bolge (ilce) | `/bolge/{ilce}/` | `src/pages/bolge/[...slug].astro` |
| Bolge (mahalle) | `/bolge/{ilce}/{mahalle}/` | `src/pages/bolge/[...slug].astro` |
| Blog Liste | `/blog/` | `src/pages/blog/index.astro` |
| Blog Yazi | `/blog/{slug}/` | `src/pages/blog/[slug].astro` |
| Hakkimizda | `/hakkimizda/` | `src/pages/hakkimizda/index.astro` |
| Kurumsal | `/kurumsal/` | `src/pages/kurumsal/index.astro` |
| Online Siparis | `/siparis/` | `src/pages/siparis/index.astro` |

**KURAL:** Bu URL pattern'leri DEGISTIRILEMEZ.
Yeni sayfa turu EKLENEMEZ (onay olmadan).

---

## SEO Kurallari (Mutlak — Istisna Yok)

### Zorunlu (Her Sayfada)
1. **Tam 1 adet H1** — Fazlasi YASAK.
2. **Meta title** — 50-60 karakter arasi, lokasyon + hizmet + marka icermeli.
3. **Meta description** — 140-160 karakter.
4. **Canonical tag** — Her sayfada, kendine isaret eden.
5. **JSON-LD** — `LocalBusiness` veya `Service` schema, Google Rich Results %100 uyumlu.
6. **Open Graph tags** — title, description, image, url, type.
7. **Sitemap.xml** — Otomatik uretilmeli.
8. **Robots.txt** — Otomatik uretilmeli.
9. **Alt text** — Her gorsel icin zorunlu.
10. **Internal linking** — Her alt sayfa ana sayfaya, ana sayfa alt sayfalara baglanmali.

### JSON-LD Kurallari
- Her sayfada `LocalBusiness` schema zorunlu.
- Bolge sayfalarinda `areaServed` alani zorunlu.
- Hizmet sayfalarinda `Service` schema zorunlu.
- FAQ sayfalarinda `FAQPage` schema zorunlu.
- Tum schema'lar https://validator.schema.org/ ile dogrulanabilir olmali.
- JSON-LD, `<head>` icinde `<script type="application/ld+json">` olarak inject edilmeli.

### Canonical Kurallari
- Ayni icerige isaret eden 2 canonical OLAMAZ.
- Canonical collision = KRITIK HATA, build durdurulmali.

### Bolge Sayfasi SEO
- Her bolge sayfasi benzersiz H1 icermeli: `{Mahalle/Ilce} {Hizmet Turu}`.
- Near-duplicate icerigi onlemek icin: ilce giri paragrafinda varyasyon olmali.
- District sayfasi, neighborhood sayfalarina otorite linkiyle baglanmali.

---

## Responsive Tasarim Kurallari

- **Mobile-first zorunlu.** Tum CSS mobile-first yazilir.
- Desktop gorunum, mobilin adaptive genislemesidir.
- Breakpoint'ler Tailwind default'lari kullanilir (sm, md, lg, xl).
- Breakpoint sayisi ve davranisi config'den DEGISTIRILEMEZ.
- Tum component'ler 320px ekranda sorunsuz gorunmeli.
- Gorsel boyutlari: responsive `srcset` veya Astro `<Image>` component'i kullanilmali.
- Touch target minimum 44x44px (WCAG).

---

## Design System Kurallari

### Token Bazli Tasarim
- Renkler `config/site.config.json > brand` uzerinden gelir → `tailwind.config.mjs`'de token'lara donusturulur.
- **YASAK:** Hardcoded hex renk degeri (`#000`, `#333` vb.) component icinde kullanilamaz.
- **YASAK:** Hardcoded font-family component icinde tanimlanamaz.
- Tailwind CSS custom theme config uzerinden token'lar tanimlanir (`tailwind.config.mjs`).

### Renk Kullanimi
- `primary` — Ana marka rengi (CTA butonlari, basliklar)
- `secondary` — Ikincil vurgu
- `background` — Sayfa arka plani
- `surface` — Kart/section arka plani
- `text-primary` — Ana metin rengi
- `text-secondary` — Ikincil metin
- `accent` — Vurgu elemanlari

Bunlarin tumu `site.config.json > brand` bolumunden alinir.

---

## Bolge (Service Area) Kurallari

### Hiyerarsi
```
City (Il)
  └── District (Ilce) → /bolge/{ilce}/
        └── Neighborhood (Mahalle) → /bolge/{ilce}/{mahalle}/
```

### Validasyon
- Neighborhood varsa → District ZORUNLU.
- District varsa → City ZORUNLU.
- Ayni city+district+neighborhood kombinasyonu TEKRARLANAMAZ.
- Tekrar varsa → HATA, build durdur.

### Uretim
- Her aktif ServiceArea icin 1 sayfa uretilir.
- Core, sayfa sablonunu tek tip uygular (ilce ve mahalle icin ayni layout).
- Icerik varyasyonu: SEO token'lari ve giriş paragrafı ile saglanir.

### Paket Limiti
- `site.config.json > packageConfig.activeRegionLimit` parametresi kontrol eder.
- Limit asilirsa: fazla bolgeler uretilmez, uyari verilir.
- Bu bir FAIL degil, ticari kisitlamadir.

---

## Kod Yazim Kurallari

### Genel
- TypeScript strict mode zorunlu.
- Tum component prop'lari tiplendirilmis olmali.
- `any` tipi YASAKTIR.
- Console.log uretim kodunda YASAKTIR.
- Yorum: sadece karmasik is mantiginda. Acik koda yorum eklenmez.

### Astro Component'leri
- Her component `site.config.json`'dan veri alir (isletme adi, iletisim, hizmetler, bolgeler).
- Sayfa ozgu icerik metinleri (hero text, section aciklamalari) component icinde yazilabilir.
- Hardcoded renk YASAKTIR — Tailwind token'larindan gelmeli.
- Inline style kullanilamaz (iframe/SVG gibi zorunlu istisnalar haric).
- Props interface'i dosyanin basinda tanimlanmali.

### Client-Side JavaScript Pattern'i (ZORUNLU)
Tum `<script>` bloklari asagidaki pattern'i kullanmalidir:

```javascript
function initMyFeature() {
  var el = document.getElementById('my-element');
  if (!el) return;

  // Cift baslatma korumasi — ZORUNLU
  if (el.dataset.initialized) return;
  el.dataset.initialized = 'true';

  // ... event listener'lar ...
}

document.addEventListener('astro:page-load', initMyFeature);
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMyFeature);
} else {
  initMyFeature();
}
```

**KURALLAR:**
1. `dataset.initialized` guard ZORUNLU — cift calisma onlenir.
2. `astro:page-load` + `DOMContentLoaded` ikili pattern — ViewTransitions uyumlulugu.
3. Form'larda `novalidate` YASAKTIR — tarayici dogrulamasi acik kalmali, JS ek UX saglar.

### Form Guvenligi
- HTML5 `required` attribute'leri her zaman kullanilmali.
- `novalidate` EKLENMEZ — JS yuklenemezse tarayici dogrulamasi devreye girmeli.
- WhatsApp/telefon numarasi `config.contact` uzerinden alinir, ASLA hardcode edilmez.
- Form verisi `data-*` attribute'leriyle template'den JS'e iletilir.

### Dosya Isimlendirme
- Component'ler: PascalCase (`Hero.astro`, `ServiceAreas.astro`)
- Sayfalar: kebab-case veya Astro dynamic routing (`[slug].astro`)
- Config dosyalari: camelCase JSON keys

---

## Erisilebilirlik Kurallari (WCAG 2.1 AA)

### Zorunlu
- **Touch target:** Minimum 44x44px tum tiklanabilir elemanlarda (`min-h-[44px] min-w-[44px]`).
- **Focus visible:** `*:focus-visible` outline tanimli olmali (global.css'de mevcut).
- **Skip link:** `<a href="#main-content" class="sr-only focus:not-sr-only ...">` her sayfada (BaseLayout'ta mevcut).
- **ARIA labels:** Tum ikonlu butonlarda `aria-label` zorunlu.
- **prefers-reduced-motion:** `global.css`'de zorunlu medya sorgusu — animasyonlari ve transition'lari disable eder.

### Animasyon Kurali
- Sonsuz dongu animasyonlari (`infinite`) SADECE dekoratif elemanlarda kullanilabilir.
- Tum animasyonlar `prefers-reduced-motion: reduce`'da devre disi kalmalidir.
- Bu global.css'deki medya sorgusuyla otomatik saglanir — **ASLA bu sorguyu kaldirma.**

---

## Fake Veri Yasagi (MUTLAK)

Asagidaki veriler ASLA uydurulmaz, placeholder olarak eklenmez:
- **aggregateRating** — Google yildiz puani
- **reviewCount** — Yorum sayisi
- **review** — Musteri yorumlari (gercek degilse)
- **priceRange** — Dogrulanamayan fiyat araligi

Bu veriler daha once eklenmis ve kaldirilmistir. **Tekrar eklenmesi YASAKTIR.**
Gercek veri yoksa o alan/bolum tamamen cikarilir.

---

## Deploy Kurallari (GitHub Actions -> GitHub Pages)

**Yayin akisi (tek yol, elle adim yok):**

```
astro-src dalina push
   -> .github/workflows/scheduled-publish.yml tetiklenir
   -> npm run build (tum dogrulama kapilari calisir)
   -> dist/ ciktisi astro-live dalina yazilir
   -> GitHub Pages dryallekurutemizleme.com adresinde yayinlar
```

- Kaynak dal: `astro-src` (yerel `main` bu dali izler).
- Yayin dali: `astro-live` — **elle commit atilmaz**, workflow yazar.
- Ayni workflow her gun 07:00 UTC calisir (tarih-kapili blog yayini icin).
- Build komutu: `npm run build` · Output: `dist/` · Dockerfile GEREKMEZ.
- CNAME ve `.nojekyll`, `scripts/generate-redirect-stubs.mjs` tarafindan
  `dist/` icine uretilir. Bu adim bozulursa **ozel alan adi duser.**

**YASAK:** Bu repo DigitalOcean droplet'ine veya baska bir sunucuya deploy
EDILMEZ. Kardes proje DryPrestij'den kopyalanmis rsync workflow'u
(`/var/www/dryprestij/` hedefli) 4 Eyl 2026'da kaldirildi — geri eklenmez.
Iki projenin deploy hatti birbirinden tamamen ayridir.

---

## Degisiklik Kontrolu

### Core Degisikligi (Onayli)
Asagidakilerden herhangi birini degistirmek icin KULLANICI ONAYI gerekir:
- Yeni sayfa turu ekleme
- URL pattern degisikligi
- Component ekleme/cikarma
- SEO meta uretim mantigi degisikligi
- JSON-LD schema degisikligi
- Responsive breakpoint degisikligi

### Serbest Degisiklik (Onaysiz)
- `site.config.json` icerigi (yeni musteri icin)
- Icerik dosyalari (`src/content/`)
- Gorsel ekleme (`public/images/`)

---

## Hata Davranisi

- Zorunlu config alani eksikse → build BASLATMA, hatayı bildir.
- Duplicate bolge varsa → build BASLATMA, hatayi bildir.
- Canonical cakismasi varsa → build BASLATMA, hatayi bildir.
- JSON-LD gecersizse → UYAR, devam et ama rapor et.
- Paket limiti asilmissa → fazlayi URETME, uyar, devam et.

ASLA tahminle veya varsayimla bosluk doldurma.
Eksik veri = DUR ve SOR.

---

## Proje Klasor Yapisi

```
/
├── CLAUDE.md                          # Bu dosya (kurallar)
├── config/
│   └── site.config.json               # Musteri konfigurasyonu (tek otorite)
├── src/
│   ├── layouts/
│   │   └── BaseLayout.astro           # Ana layout
│   ├── components/
│   │   ├── Header.astro               # Ust navigasyon + hamburger
│   │   ├── Hero.astro                 # Ana banner
│   │   ├── Services.astro             # Hizmet kartlari
│   │   ├── ServiceAreas.astro         # Bolge listesi
│   │   ├── About.astro                # Hakkimizda (ana sayfa)
│   │   ├── CorporateSection.astro     # Kurumsal bolum (ana sayfa)
│   │   ├── FAQ.astro                  # SSS
│   │   ├── Testimonials.astro         # Yorumlar
│   │   ├── Contact.astro              # Iletisim + harita
│   │   ├── WhatsAppCTA.astro          # Sabit WhatsApp butonu
│   │   ├── Footer.astro               # Alt bilgi
│   │   ├── SEOHead.astro              # Meta + JSON-LD
│   │   └── Breadcrumb.astro           # Breadcrumb
│   ├── pages/
│   │   ├── index.astro                # Ana sayfa
│   │   ├── hakkimizda/index.astro     # Hakkimizda sayfasi
│   │   ├── kurumsal/index.astro       # Kurumsal sayfasi
│   │   ├── siparis/index.astro        # Online siparis (WhatsApp form)
│   │   ├── hizmetler/
│   │   │   └── [slug].astro           # Hizmet sayfalari (config'den)
│   │   ├── bolge/
│   │   │   └── [...slug].astro        # Bolge sayfalari (config'den)
│   │   └── blog/
│   │       ├── index.astro            # Blog listesi
│   │       └── [slug].astro           # Blog yazisi
│   ├── utils/
│   │   └── engine.ts                  # interpolate(), deterministicIndex(), validateConfig()
│   ├── content/
│   │   └── blog/                      # Blog icerik dosyalari
│   └── styles/
│       └── global.css                 # Global stiller + prefers-reduced-motion
├── public/
│   ├── images/                        # Statik gorseller
│   └── favicon.svg
├── astro.config.mjs
├── tailwind.config.mjs
├── tsconfig.json
└── package.json
```
