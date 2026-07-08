# Yeni Ürün Dönüşüm Rehberi

> Bu doküman, aynı codebase ile farklı sektörlere web sitesi üretmek için adım adım rehberdir.
> İnsan veya AI (Claude Code, GPT vb.) bu dokümanı izleyerek sıfır hatayla yeni site üretebilir.
> **Kod dosyalarına DOKUNULMAZ.** Sadece config, görseller ve içerik değişir.

---

## 0. Hızlı Başlangıç

```
1. Repo'yu clone et veya fork et
2. config/site.config.json → Tüm alanları yeni sektöre göre doldur
3. astro.config.mjs:8 → site URL'ini değiştir
4. public/ → Logo, favicon, OG image koy
5. npm install && npm run build → 0 hata → Deploy
```

### Değişecek Dosyalar (SADECE bunlar)

| # | Dosya | Ne Değişir |
|---|-------|-----------|
| 1 | `config/site.config.json` | Tüm iş mantığı, metinler, SEO, iletişim |
| 2 | `astro.config.mjs` | Satır 8: site URL |
| 3 | `public/robots.txt` | Satır 29: Sitemap URL |
| 4 | `public/manifest.json` | name, short_name, description, theme_color |
| 5 | `package.json` | Satır 2: proje adı |
| 6 | `public/images/` | logo.png, logo.webp, og-default.png |
| 7 | `public/` | favicon.svg, favicon-16.png, favicon-32.png, apple-touch-icon.png |
| 8 | `src/content/blog/` | Eski blog yazılarını sil, yeni sektöre uygun yaz |

### Değişmeyecek Dosyalar (DOKUNMA)

```
src/components/     ← Tüm component'lar
src/pages/          ← Tüm sayfa şablonları
src/layouts/        ← BaseLayout
src/utils/engine.ts ← Utility fonksiyonları
src/styles/         ← Global stiller
tailwind.config.mjs ← Renk token'ları config'den otomatik gelir
CLAUDE.md           ← AI kuralları
tsconfig.json       ← TypeScript config
```

---

## 1. Mimari Anlayış

Bu proje bir **web sitesi üretim motorudur**. `config/site.config.json` değiştirilerek farklı sektör sitesi üretilir. Kod dosyaları sabittir, config profili değişkendir.

**Akış:** `site.config.json` → `tailwind.config.mjs` (renk token'ları) → Component'lar (veri okuma) → `astro build` (statik HTML üretimi)

**Üç temel fonksiyon** (`src/utils/engine.ts`):
- `interpolate(template, tokens)` — `{businessName}` gibi token'ları değerle değiştirir
- `deterministicIndex(slug, length)` — Bölge sayfalarında aynı slug'a her zaman aynı varyantı atar
- `validateConfig(config)` — Build öncesi zorunlu alanları kontrol eder, eksikse build'ı durdurur

**Conditional rendering kuralı:** Boolean flag YOKTUR. Veri varsa component render edilir, yoksa atlanır.
- `pricing.categories` dizisi doluysa → PriceTable görünür
- `corporate.sectors` dizisi doluysa → CorporateSection görünür
- Dizi boş veya yoksa → component otomatik gizlenir

---

## 2. Ön Koşullar

Başlamadan önce bunların hazır olduğundan emin ol:

- [ ] **Node.js** >= 18.x (`node -v`)
- [ ] **npm** >= 9.x (`npm -v`)
- [ ] **Git** (`git --version`)
- [ ] **Domain** — DNS erişimi olan bir alan adı
- [ ] **Hosting** — DigitalOcean App Platform veya herhangi bir static host (Netlify, Vercel, Cloudflare Pages)
- [ ] **Logo** — PNG 1024x1024px + WebP versiyonu
- [ ] **Favicon seti** — SVG kaynak + 16px PNG + 32px PNG + 180px Apple Touch Icon
- [ ] **OG Image** — PNG 1200x630px (sosyal medya paylaşım görseli)
- [ ] **İletişim bilgileri** — Telefon, e-posta, WhatsApp, adres, Google Maps linki
- [ ] **Koordinatlar** — Enlem/boylam (Google Maps'ten alınır)
- [ ] **Schema.org @type** — İşletme tipine uygun alt tip (Bölüm 6'daki tablodan seç)
- [ ] **Google Business verileri** — Gerçek rating ve yorum sayısı (yoksa socialProof bölümünü boş bırak)

---

## 3. Adım Adım Dönüşüm

> **KURAL:** Her adımı sırayla izle. Adım atlamak build hatasına neden olabilir.
> Her adımda "Kuru Temizleme → Pilates Stüdyosu" karşılaştırmalı örnek verilmiştir.

---

### Adım 1: identity

**Dosya:** `config/site.config.json` → `"identity"` bölümü

| Alan | Tip | Zorunlu | Açıklama |
|------|-----|---------|----------|
| `businessName` | string | EVET | Tam işletme adı. Tüm SEO meta, JSON-LD ve sayfa başlıklarında kullanılır. |
| `brandName` | string | hayır | Kısa marka adı (Header, Footer). Yoksa businessName kullanılır. |
| `sectorLabel` | string | EVET | Sektör etiketi. Title, H1, description'larda `{sectorLabel}` token'ı olarak kullanılır. |
| `schemaType` | string | EVET | Schema.org @type. Bölüm 6'daki tablodan seç. |
| `sectorType` | string | hayır | Dahili kategori kodu (camelCase). |
| `tagline` | string | hayır | Ana sayfa Hero bölümünde slogan. |
| `description` | string | hayır | JSON-LD ve Footer'da kullanılan uzun açıklama. |
| `heroDescription` | string | hayır | Ana sayfa Hero paragrafı. |
| `establishedYear` | number | hayır | Kuruluş yılı. SEO template'lerde `{establishedYear}` token'ı. |
| `locale` | string | hayır | Dil kodu. Varsayılan: `"tr-TR"`. |

**Kuru Temizleme:**
```json
"identity": {
  "businessName": "Dry Prestij Kuru Temizleme",
  "brandName": "Dry Prestij",
  "sectorLabel": "Kuru Temizleme",
  "schemaType": "DryCleaningOrLaundry",
  "tagline": "Boğaz'ın En Titiz Kuru Temizlemecisi",
  "establishedYear": 2020
}
```

**Pilates Stüdyosu:**
```json
"identity": {
  "businessName": "Flow Pilates Studio",
  "brandName": "Flow Pilates",
  "sectorLabel": "Pilates",
  "schemaType": "SportsActivityLocation",
  "tagline": "Beşiktaş'ın En Profesyonel Pilates Stüdyosu",
  "establishedYear": 2018
}
```

**DİKKAT:**
- `businessName` boş bırakılırsa build DURUR.
- `sectorLabel` tüm sayfalarda `{sectorLabel}` token'ı olarak kullanılır — doğru yazıldığından emin ol.
- `schemaType` geçerli bir Schema.org tipi olmalı (Bölüm 6'daki tablodan seç).

---

### Adım 2: brand

**Dosya:** `config/site.config.json` → `"brand"` bölümü

Tüm renkler `tailwind.config.mjs` tarafından otomatik okunur ve Tailwind token'larına dönüştürülür. Component'larda hardcoded renk YOKTUR.

| Alan | Format | Açıklama |
|------|--------|----------|
| `primaryColor` | `#RRGGBB` | Ana marka rengi (butonlar, başlıklar, hero arka plan) |
| `secondaryColor` | `#RRGGBB` | İkincil renk |
| `accentColor` | `#RRGGBB` | Vurgu rengi (ikonlar, badge'ler) |
| `accentLight` | `#RRGGBB` | Açık vurgu |
| `backgroundColor` | `#RRGGBB` | Sayfa arka planı (genelde `#FFFFFF`) |
| `surfaceColor` | `#RRGGBB` | Kart/section arka planı |
| `surfaceAlt` | `#RRGGBB` | Alternatif yüzey rengi |
| `textPrimary` | `#RRGGBB` | Ana metin rengi |
| `textSecondary` | `#RRGGBB` | İkincil metin rengi |
| `primaryDark` | `#RRGGBB` | Primary'nin koyu tonu (gradient, footer) |
| `borderColor` | `#RRGGBB` | Kenarlık rengi |
| `fontFamily` | string | Font adı (Google Fonts'tan). Varsayılan: `"Inter"` |
| `brandVoice` | string | Marka tonu: `"professional"`, `"friendly"`, `"luxury"` vb. (içerik rehberliği) |

**Kuru Temizleme (koyu mavi tema):**
```json
"brand": {
  "primaryColor": "#0B2341",
  "accentColor": "#29B6F6",
  "surfaceColor": "#E3F2FD",
  "fontFamily": "Inter"
}
```

**Pilates Stüdyosu (sıcak ton tema):**
```json
"brand": {
  "primaryColor": "#2D1B4E",
  "accentColor": "#E040FB",
  "surfaceColor": "#F3E5F5",
  "fontFamily": "Poppins"
}
```

**DİKKAT:**
- Tüm değerler `#RRGGBB` hex formatında olmalı. `rgb()` veya renk adı KABUL EDİLMEZ.
- `fontFamily` değiştirildiyse, `src/layouts/BaseLayout.astro` içindeki Google Fonts `<link>` tag'ini kontrol et.

---

### Adım 3: contact

**Dosya:** `config/site.config.json` → `"contact"` bölümü

| Alan | Format | Zorunlu | Açıklama |
|------|--------|---------|----------|
| `phone` | `"+90 5XX XXX XX XX"` | EVET | Uluslararası format. `tel:` linkleri için. |
| `phoneDisplay` | `"0 (5XX) XXX XX XX"` | hayır | Görüntüleme formatı. |
| `email` | `"info@domain.com"` | hayır | E-posta adresi. |
| `whatsapp` | `"+905XXXXXXXXX"` | hayır | WhatsApp numarası. Boşluk ve + işareti kodda temizlenir. |
| `domain` | `"domain.com"` | EVET | `https://` OLMADAN sadece domain. Canonical, OG, JSON-LD'de kullanılır. |
| `address.street` | string | hayır | Sokak adresi. |
| `address.postalCode` | string | hayır | Posta kodu. |
| `address.city` | string | hayır | İl (örn: İstanbul). |
| `address.province` | string | hayır | İlçe (örn: Sarıyer). SEO template'lerde `{province}` token'ı. |
| `geo.latitude` | string | hayır | Enlem (Google Maps'ten kopyala). |
| `geo.longitude` | string | hayır | Boylam. |
| `socialLinks.googleMaps` | URL | hayır | Google Maps paylaşım linki. JSON-LD `sameAs` alanı. |

**DİKKAT:**
- `domain` alanı `https://` İÇERMEMELİ — sadece `"domain.com"` formatında.
- `domain` değeri `astro.config.mjs:8` ile UYUMLU olmalı. Uyumsuzluk → kırık canonical/sitemap.
- `whatsapp` alanı `wa.me/` URL'ine dönüştürülür. Format: sadece rakam veya `+` ile başlayan rakam.

---

### Adım 4: openingHours

**Dosya:** `config/site.config.json` → `"openingHours"` bölümü

```json
"openingHours": {
  "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
  "opens": "08:00",
  "closes": "20:00",
  "displayText": "Pazartesi – Cumartesi: 08:00 - 20:00"
}
```

| Alan | Format | Açıklama |
|------|--------|----------|
| `days` | İngilizce gün adları dizisi | JSON-LD OpeningHoursSpecification için. |
| `opens` | `"HH:MM"` (24 saat) | Açılış saati. |
| `closes` | `"HH:MM"` (24 saat) | Kapanış saati. |
| `displayText` | string | Kullanıcıya gösterilecek metin (Türkçe). |

**DİKKAT:** `days` dizisi İngilizce olmalı (Monday, Tuesday...). `displayText` Türkçe olabilir.

---

### Adım 5: services[]

**Dosya:** `config/site.config.json` → `"services"` dizisi

Bu dizi her hizmet için bir sayfa üretir: `/hizmetler/{slug}/`

**Minimum 1 hizmet ZORUNLU.** Dizi boşsa build DURUR.

| Alan | Tip | Zorunlu | Açıklama |
|------|-----|---------|----------|
| `name` | string | EVET | Hizmet adı. Title ve H1'de kullanılır. **Her name UNIQUE olmalı.** |
| `slug` | string | EVET | URL slug'ı. Küçük harf, tire ile ayrılmış, Türkçe karakter YOK. |
| `description` | string | hayır | Kısa açıklama (hizmet kartı ve meta description). |
| `icon` | string | hayır | İkon adı: `"shirt"`, `"iron"`, `"carpet"`, `"suit"`, `"dress"`, `"leather"`, `"sofa"`, `"textile"`, `"organic"` |
| `image` | string | hayır | Hizmet görseli yolu: `"/images/services/dosya.jpg"` |
| `features` | string[] | hayır | Hizmet özellikleri (madde işaretli liste olarak gösterilir). |
| `detailParagraphs` | string[] | hayır | Detaylı paragraflar. `{businessName}`, `{province}`, `{sectorLabel}` token'ları kullanılabilir. |
| `relatedBlogSlugs` | string[] | hayır | İlişkili blog yazısı slug'ları. Blog aktifse internal link oluşturur. |

**Örnek (Pilates):**
```json
{
  "name": "Mat Pilates",
  "slug": "mat-pilates",
  "description": "Grup ve özel mat pilates dersleri ile esnekliğinizi artırın.",
  "icon": "carpet",
  "features": [
    "Küçük gruplar (max 8 kişi)",
    "Sertifikalı eğitmenler",
    "Ücretsiz deneme dersi",
    "Esnek seans saatleri"
  ],
  "detailParagraphs": [
    "{businessName} olarak {province} bölgesinde profesyonel mat pilates dersleri sunuyoruz.",
    "Grup derslerimiz maksimum 8 kişilik olup, her seviyeye uygun programlarla çalışıyoruz."
  ],
  "relatedBlogSlugs": []
}
```

**DİKKAT:**
- `name` alanları unique olmalı. Duplicate → build DURUR.
- `slug` formatı: küçük harf + tire. Örnek: `"mat-pilates"`, `"reformer-pilates"`. Türkçe karakter (ş, ç, ö, ü, ı, ğ) KULLANMA.
- `icon` değerleri sabit bir listeden gelir. Yeni ikon eklemek kod değişikliği gerektirir.

---

### Adım 6: serviceAreas[]

**Dosya:** `config/site.config.json` → `"serviceAreas"` dizisi

Bu dizi bölge sayfaları üretir:
- İlçe: `/bolge/{districtSlug}/`
- Mahalle: `/bolge/{districtSlug}/{neighborhoodSlug}/`

**Minimum 1 bölge ZORUNLU.** Dizi boşsa build DURUR.

```json
{
  "city": "İstanbul",
  "district": "Beşiktaş",
  "districtSlug": "besiktas",
  "neighborhoods": [
    { "name": "Etiler", "slug": "etiler" },
    { "name": "Levent", "slug": "levent" }
  ]
}
```

| Alan | Tip | Zorunlu | Açıklama |
|------|-----|---------|----------|
| `city` | string | EVET | İl adı. |
| `district` | string | EVET | İlçe adı. |
| `districtSlug` | string | EVET | URL slug'ı. Küçük harf, tire, Türkçe karakter YOK. |
| `neighborhoods` | array | hayır | Mahalle listesi. Her birinde `name` ve `slug` zorunlu. |

**DİKKAT:**
- `packageConfig.activeRegionLimit` toplam bölge sayısını sınırlar. Limit aşılırsa fazla bölgeler üretilmez.
- Aynı district+neighborhood kombinasyonu TEKRARLANAMAZ.
- `districtSlug` ve `neighborhoods[].slug`: Türkçe karakter YOK (`ş→s`, `ç→c`, `ö→o`, `ü→u`, `ı→i`, `ğ→g`).

---

### Adım 7: seoTemplates

**Dosya:** `config/site.config.json` → `"seoTemplates"` bölümü

Token interpolation sistemi. `{token}` → değer olarak işlenir.

| Alan | Zorunlu | Nerede Kullanılır |
|------|---------|-------------------|
| `homeTitle` | EVET | Ana sayfa `<title>` |
| `homeDescription` | hayır | Ana sayfa `<meta description>` |
| `serviceTitle` | EVET | Hizmet sayfası `<title>` |
| `serviceDescription` | hayır | Hizmet sayfası `<meta description>` |
| `regionTitle` | EVET | Bölge sayfası `<title>` |
| `regionDescription` | hayır | Bölge sayfası `<meta description>` |
| `regionH1` | hayır | Bölge sayfası `<h1>` |
| `aboutTitle` | EVET | Hakkımızda sayfası `<title>` |
| `aboutDescription` | hayır | Hakkımızda sayfası `<meta description>` |
| `corporateTitle` | hayır | Kurumsal sayfası `<title>` |
| `corporateDescription` | hayır | Kurumsal sayfası `<meta description>` |
| `orderServiceType` | hayır | Sipariş sayfası JSON-LD serviceType |
| `corporateServiceType` | hayır | Kurumsal sayfası JSON-LD serviceType |
| `catalogName` | EVET | JSON-LD OfferCatalog adı |

**Kullanılabilir Token'lar:**

| Token | Kaynak | Örnek Değer |
|-------|--------|-------------|
| `{businessName}` | identity.businessName | "Flow Pilates Studio" |
| `{sectorLabel}` | identity.sectorLabel | "Pilates" |
| `{sectorLabelLower}` | sectorLabel.toLowerCase() | "pilates" |
| `{province}` | contact.address.province | "Beşiktaş" |
| `{location}` | Sayfa bazlı (ilçe/mahalle adı) | "Etiler" |
| `{serviceName}` | services[].name | "Mat Pilates" |
| `{serviceNameLower}` | serviceName.toLowerCase() | "mat pilates" |
| `{primaryKeyword}` | seoTokens.primaryKeywords[0] | "pilates dersi" |
| `{primaryKeywordCap}` | İlk harf büyük | "Pilates dersi" |
| `{establishedYear}` | identity.establishedYear | "2018" |

**Örnek (Pilates):**
```json
"seoTemplates": {
  "homeTitle": "{businessName} | {province} {sectorLabel}",
  "homeDescription": "{province} ve çevresinde profesyonel {sectorLabelLower} dersleri. {businessName} güvencesiyle ücretsiz deneme dersi.",
  "serviceTitle": "{serviceName} | {businessName}",
  "serviceDescription": "{province} bölgesinde profesyonel {serviceNameLower} dersleri. {businessName} farkıyla sağlıklı yaşam.",
  "regionTitle": "{location} {primaryKeywordCap} | {businessName}",
  "regionDescription": "{location} bölgesinde profesyonel {primaryKeyword} dersleri. {businessName} — {establishedYear}'den bu yana hizmetinizde.",
  "regionH1": "{location} {sectorLabel} Dersleri",
  "aboutTitle": "Hakkımızda | {businessName}",
  "aboutDescription": "{businessName} hakkında. {establishedYear}'den bu yana {province}'de profesyonel {sectorLabelLower} eğitimi veriyoruz.",
  "corporateTitle": "Kurumsal {sectorLabel} | {businessName}",
  "corporateDescription": "İşletmeniz için kurumsal {sectorLabelLower} programları.",
  "orderServiceType": "Online {sectorLabel} Randevu",
  "corporateServiceType": "Corporate Pilates",
  "catalogName": "{sectorLabel} Dersleri"
}
```

**DİKKAT:**
- 5 zorunlu alan eksikse build DURUR: `homeTitle`, `serviceTitle`, `regionTitle`, `aboutTitle`, `catalogName`.
- Token adları büyük-küçük harf duyarlı. `{BusinessName}` ÇALIŞMAZ, `{businessName}` doğru.
- Eksik token boş string ile değiştirilir — görsel olarak fark edilir ama build durmaz.

---

### Adım 8: contentTokens

**Dosya:** `config/site.config.json` → `"contentTokens"` bölümü

Bu bölüm component'lara beslenen içerik parçalarını tanımlar.

| Alan | Tip | Nerede Kullanılır |
|------|-----|-------------------|
| `valuePropositions` | string[3] | About bölümü başlıkları |
| `valuePropositionDetails` | string[3] | About bölümü detay paragrafları |
| `serviceHighlights` | string[3] | Hero bölümü rozet listesi |
| `servicesSubtitle` | string | Services bölümü alt başlığı |
| `aboutTitle` | string | About bölümü ana başlığı (örn: "Neden Flow Pilates?") |
| `aboutStoryParagraphs` | string[3] | Hakkımızda sayfası hikaye paragrafları. Token'lar: `{businessName}`, `{establishedYear}`, `{province}`, `{sectorLabel}`, `{serviceCount}`, `{areaCount}`, `{googleRating}`, `{reviewCount}` |
| `aboutValues` | object[3] | Hakkımızda sayfası değerler kartları. Her biri: `{ title, description, icon }`. icon: `"shield"`, `"leaf"`, `"star"` |
| `regionVariants` | string[3+] | Bölge sayfası giriş paragrafı varyantları. `deterministicIndex()` ile seçilir. Token'lar: `{location}`, `{sectorLabel}`, `{businessName}`, `{primaryKeyword}` |
| `regionSubtitleVariants` | string[3+] | Bölge sayfası alt başlık varyantları. |
| `actionVerbs` | string[] | CTA metinleri için (isteğe bağlı). |
| `audienceTerms` | string[] | Hedef kitle terimleri (isteğe bağlı). |

**DİKKAT:**
- `valuePropositions` ve `valuePropositionDetails` dizileri aynı uzunlukta olmalı (eşleşme index bazlı).
- `regionVariants` en az 3 öğe içermeli — bölge sayfalarında tekrarı önler.
- `aboutValues[].icon` sabit değerlerden biri olmalı: `"shield"`, `"leaf"`, `"star"`.

---

### Adım 9: conversionTokens

**Dosya:** `config/site.config.json` → `"conversionTokens"` bölümü

```json
"conversionTokens": {
  "primaryCTA": "Ücretsiz Deneme Dersi",
  "secondaryCTA": "WhatsApp ile Yazın",
  "ctaPhone": "Hemen Arayın"
}
```

Bu metinler Hero, Header ve CTA bölümlerindeki butonlarda görünür.

---

### Adım 10: socialProof

**Dosya:** `config/site.config.json` → `"socialProof"` bölümü

```json
"socialProof": {
  "googleRating": 4.9,
  "reviewCount": 85,
  "testimonials": [
    {
      "name": "Ayşe H.",
      "comment": "Reformer dersleri harika, eğitmenler çok ilgili.",
      "rating": 5
    }
  ]
}
```

**MUTLAK KURAL — FAKE VERİ YASAKTIR:**
- `googleRating` → Google Business'tan GERÇEK puan. Uydurma YASAK.
- `reviewCount` → Google Business'tan GERÇEK yorum sayısı. Uydurma YASAK.
- `testimonials` → GERÇEK müşteri yorumları. Uydurma YASAK.
- Gerçek veri yoksa → `"socialProof": {}` yap veya bölümü tamamen kaldır.
- Gerçek olmayan aggregateRating, Google tarafından ceza sebebidir.

---

### Adım 11: faq[]

**Dosya:** `config/site.config.json` → `"faq"` dizisi

```json
"faq": [
  {
    "question": "Pilates için önceden deneyim gerekli mi?",
    "answer": "Hayır, derslerimiz başlangıçtan ileri seviyeye kadar her düzeye uygundur."
  }
]
```

Her soru-cevap çifti FAQ bölümünde ve JSON-LD FAQPage schema'sında kullanılır.

---

### Adım 12: pricing (OPSİYONEL)

**Dosya:** `config/site.config.json` → `"pricing"` bölümü

Bu bölüm **opsiyoneldir**. Yoksa veya `categories` dizisi boşsa PriceTable component'ı ana sayfada GÖRÜNMEZ.

```json
"pricing": {
  "categories": [
    {
      "name": "Grup Dersleri",
      "icon": "M12 2L6 7H2v4l4 2v9h12v-9l4-2V7h-4L12 2z",
      "items": [
        { "name": "Mat Pilates (Aylık 8 Seans)", "price": 2500 },
        { "name": "Mat Pilates (Aylık 12 Seans)", "price": 3200 },
        { "name": "Halı Yıkama", "price": 80, "unit": "m²" }
      ]
    }
  ]
}
```

| Alan | Açıklama |
|------|----------|
| `categories[].name` | Kategori başlığı (akordeon header) |
| `categories[].icon` | SVG path string (ikon) |
| `categories[].items[].name` | Ürün/hizmet adı |
| `categories[].items[].price` | Fiyat (sayı, TRY) |
| `categories[].items[].unit` | **Opsiyonel.** Birim varsa fiyat `₺/birim` olarak gösterilir (ör. `"m²"` → `80 ₺/m²`). Yoksa sadece `₺` gösterilir. JSON-LD'de `UnitPriceSpecification` + `unitText` olarak yansır. |

> **Örnek birimler:** `"m²"` (perde, halı), `"kg"` (çamaşır), `"kişi"` (catering), `"saat"` (danışmanlık)

**Fiyat tablosu istemiyorsan:** `"pricing": {}` veya tamamen kaldır.

---

### Adım 13: corporate (OPSİYONEL)

**Dosya:** `config/site.config.json` → `"corporate"` bölümü

Bu bölüm **opsiyoneldir**. Yoksa veya `sectors` dizisi boşsa CorporateSection GÖRÜNMEZ ve `/kurumsal/` sayfası oluşmaz.

```json
"corporate": {
  "title": "İşletmenize Özel Pilates Programları",
  "description": "Ofisler, oteller ve spor merkezleri için kurumsal pilates.",
  "sectors": [
    { "name": "Ofis & İş Yeri", "description": "Çalışanlar için düzenli seans programı", "icon": "briefcase" }
  ],
  "advantages": [
    { "title": "Grup İndirimi", "description": "10+ kişide %20 indirim.", "icon": "tag" }
  ]
}
```

**sectors[].icon değerleri:** `"building"`, `"utensils"`, `"briefcase"`, `"store"`, `"dumbbell"`, `"bank"`
**advantages[].icon değerleri:** `"tag"`, `"calendar"`, `"document"`, `"user"`

**Kurumsal bölüm istemiyorsan:** `"corporate": {}` veya tamamen kaldır.

---

### Adım 14: packageConfig

**Dosya:** `config/site.config.json` → `"packageConfig"` bölümü

```json
"packageConfig": {
  "activeRegionLimit": 16,
  "monthlyRegionIncrement": 4,
  "blogEnabled": false,
  "blogPostLimit": 0
}
```

| Alan | Açıklama |
|------|----------|
| `activeRegionLimit` | Üretilecek maksimum bölge sayısı. Limit aşılırsa fazlası atlanır. |
| `blogEnabled` | `true` = blog aktif, `false` = blog devre dışı. |
| `blogPostLimit` | Maksimum blog yazısı. `0` = sınırsız. |

---

### Adım 15: seoTokens

**Dosya:** `config/site.config.json` → `"seoTokens"` bölümü

```json
"seoTokens": {
  "primaryKeywords": ["pilates dersi", "reformer pilates", "mat pilates"],
  "secondaryKeywords": ["yoga", "esneklik", "postür düzeltme"],
  "locationModifiers": ["yakınımda", "en yakın", "profesyonel"],
  "brandModifiers": ["Flow Pilates", "flow pilates"]
}
```

`primaryKeywords[0]` bölge sayfalarında `{primaryKeyword}` token'ı olarak kullanılır.

---

### Adım 16: astro.config.mjs

**Dosya:** `astro.config.mjs` — Satır 8

```javascript
site: 'https://YENIDOMAIN.com',
```

**KURAL:** Bu URL `config/site.config.json` → `contact.domain` ile AYNI domain olmalı.
- Config: `"domain": "flowpilates.com"`
- Astro: `site: 'https://flowpilates.com'`

Uyumsuzluk → sitemap URL'leri ve canonical tag'ler KIRILIR.

---

### Adım 17: robots.txt

**Dosya:** `public/robots.txt` — Satır 29

Eski:
```
Sitemap: https://dryprestijkurutemizleme.com/sitemap-index.xml
```

Yeni:
```
Sitemap: https://flowpilates.com/sitemap-index.xml
```

Ayrıca 1. satırdaki yorumu da güncelle.

---

### Adım 18: manifest.json

**Dosya:** `public/manifest.json`

```json
{
  "name": "Flow Pilates Studio",
  "short_name": "Flow Pilates",
  "description": "Beşiktaş'ın Profesyonel Pilates Stüdyosu",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FFFFFF",
  "theme_color": "#2D1B4E"
}
```

**KURAL:** `theme_color` değeri `config.brand.primaryColor` ile AYNI olmalı.

---

### Adım 19: package.json

**Dosya:** `package.json` — Satır 2

```json
"name": "flow-pilates-studio",
```

Format: küçük harf, tire ile ayrılmış (npm convention).

---

### Adım 20: Görseller

**Klasör:** `public/images/` ve `public/`

| Dosya | Boyut | Format | Açıklama |
|-------|-------|--------|----------|
| `public/images/logo.png` | 1024x1024 | PNG | Ana logo (JSON-LD, SEO) |
| `public/images/logo.webp` | 1024x1024 | WebP | Header/Footer logosu |
| `public/images/og-default.png` | 1200x630 | PNG | Sosyal medya paylaşım görseli |
| `public/favicon.svg` | — | SVG | Vektör favicon |
| `public/favicon-16.png` | 16x16 | PNG | Küçük favicon |
| `public/favicon-32.png` | 32x32 | PNG | Standart favicon |
| `public/apple-touch-icon.png` | 180x180 | PNG | iOS kısayol ikonu |

**DİKKAT:** Dosya adları AYNI kalmalı. Component'lar bu adlara hardcoded referans verir.

---

### Adım 21: Blog İçeriği

**Klasör:** `src/content/blog/`

**Seçenek A — Blog aktif:** Eski `.md` dosyalarını SİL, yeni sektöre uygun yazılar oluştur.

Her dosya şu formatta olmalı:
```markdown
---
title: "Pilates'e Yeni Başlayanlar İçin Rehber"
description: "Pilates'e başlamadan önce bilmeniz gereken temel bilgiler ve ipuçları."
date: "2024-06-15"
tags: ["pilates", "başlangıç", "rehber"]
---

## İçerik başlığı

Paragraf metni...
```

- `title`: Yazı başlığı (H1 olarak render edilir)
- `description`: SEO meta description (140-160 karakter)
- `date`: Yayın tarihi (YYYY-MM-DD formatı)
- `tags`: Etiket dizisi

**Seçenek B — Blog devre dışı:** `packageConfig.blogEnabled: false` yap. Blog sayfaları üretilmez.

---

## 4. Opsiyonel Özellikler Karar Tablosu

| Özellik | Aktifleştirme | Devre Dışı Bırakma |
|---------|---------------|---------------------|
| Fiyat Tablosu | `pricing.categories` dizisini doldur | `"pricing": {}` veya kaldır |
| Kurumsal Bölüm | `corporate.sectors` dizisini doldur | `"corporate": {}` veya kaldır |
| Blog | `packageConfig.blogEnabled: true` + `.md` dosyaları ekle | `packageConfig.blogEnabled: false` |
| Google Rating | `socialProof.googleRating` + `reviewCount` doldur (GERÇEK) | `"socialProof": {}` veya kaldır |

---

## 5. Schema.org @type Seçim Rehberi

`config/site.config.json` → `identity.schemaType` alanına yazılacak değer:

| Sektör | schemaType Değeri |
|--------|-------------------|
| Kuru Temizleme | `"DryCleaningOrLaundry"` |
| Pilates / Spor | `"SportsActivityLocation"` |
| Restoran | `"Restaurant"` |
| Kuaför / Güzellik Salonu | `"BeautySalon"` |
| Diş Hekimi | `"Dentist"` |
| Avukat / Hukuk Bürosu | `"LegalService"` |
| Oto Yıkama | `"AutoWash"` |
| Eğitim Kurumu | `"EducationalOrganization"` |
| Sağlık / Klinik | `"MedicalBusiness"` |
| Veteriner | `"VeterinaryCare"` |
| Eczane | `"Pharmacy"` |
| Emlak | `"RealEstateAgent"` |
| Genel İşletme | `"LocalBusiness"` |

Tam liste: https://schema.org/LocalBusiness (alt tipler bölümü)

**Emin değilsen** `"LocalBusiness"` yaz — her sektör için çalışır.

---

## 6. Build & Doğrulama

Config tamamlandıktan sonra sırayla çalıştır:

### 6.1 Build

```bash
npm install
npm run build
```

Beklenen çıktı: `XX page(s) built`, `Complete!`, 0 hata.

Build "Config validation failed" hatası verirse → hata mesajındaki alanları kontrol et.

### 6.2 Eski Sektör Metni Kontrolü

```bash
# ESKİ_MARKA ve ESKİ_SEKTOR değerlerini eski projeye göre ayarla
grep -ri "Dry Prestij\|Kuru Temizleme" src/components/ src/pages/ --include="*.astro"
```

Beklenen çıktı: **0 sonuç.** Eğer sonuç varsa → o alan hala hardcoded, config'e taşınmalı.

**NOT:** Bu kontrol `src/content/blog/` ve `config/site.config.json` dosyalarını kapsamaz — onlar zaten profil katmanı.

### 6.3 Title Uniqueness

```bash
grep -roh '<title>[^<]*</title>' dist/ | sort | uniq -d
```

Beklenen çıktı: **0 satır** (duplicate title yok).

### 6.4 Description Uniqueness

```bash
grep -roh 'name="description" content="[^"]*"' dist/ | sort | uniq -d
```

Beklenen çıktı: **0 satır**.

### 6.5 H1 Sayısı Kontrolü

```bash
for f in dist/**/*.html; do
  count=$(grep -c '<h1' "$f" 2>/dev/null)
  [ "$count" -ne 1 ] 2>/dev/null && echo "H1 ERROR ($count): $f"
done
```

Beklenen çıktı: **0 hata** (her sayfada tam 1 adet H1).

### 6.6 JSON-LD Syntax Doğrulama

```bash
python3 -c "
import re, json, os
errors = 0
for r, d, files in os.walk('dist'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(r, f)
            with open(p) as fh:
                c = fh.read()
            for b in re.findall(r'<script type=\"application/ld\+json\">\s*(.*?)\s*</script>', c, re.DOTALL):
                try:
                    json.loads(b)
                except:
                    print(f'JSON-LD ERROR: {p}')
                    errors += 1
print(f'Toplam {errors} hata')
"
```

Beklenen çıktı: `Toplam 0 hata`.

### 6.7 Canonical Uniqueness

```bash
grep -roh 'rel="canonical" href="[^"]*"' dist/ | sort | uniq -d
```

Beklenen çıktı: **0 satır**.

---

## 7. Deploy (DigitalOcean App Platform)

1. **GitHub repo oluştur** — kodu push et
2. **DigitalOcean** → Apps → Create App → GitHub repo seç
3. **Build settings:**
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Environment: Static Site
4. **Domain ekle:** Settings → Domains → Add Domain
5. **DNS ayarı:** Domain sağlayıcında A record → DigitalOcean IP
6. **SSL:** Otomatik (Let's Encrypt). Domain doğrulandıktan sonra aktif olur.
7. **Auto-deploy:** `main` branch'e push → otomatik build ve deploy

Alternatif host'lar da aynı şekilde çalışır:
- **Netlify:** Build: `npm run build`, Publish: `dist/`
- **Vercel:** Framework: Astro (otomatik algılar)
- **Cloudflare Pages:** Build: `npm run build`, Output: `dist/`

---

## 8. Sık Yapılan Hatalar

| # | Hata | Neden | Çözüm |
|---|------|-------|-------|
| 1 | Build "Config validation failed" | Zorunlu config alanı eksik | Hata mesajındaki alan adını kontrol et, config'e ekle |
| 2 | Sitemap URL yanlış domain gösteriyor | `robots.txt` güncellenmedi | `public/robots.txt` satır 29'u yeni domain ile değiştir |
| 3 | Canonical URL eski domaine gidiyor | `astro.config.mjs` site URL eski | `astro.config.mjs:8` → `site: 'https://yenidomain.com'` |
| 4 | OG image sosyal medyada görünmüyor | `og-default.png` yok veya yanlış boyut | 1200x630 PNG dosyası `public/images/og-default.png` olarak koy |
| 5 | PWA adı eski isim gösteriyor | `manifest.json` güncellenmedi | `public/manifest.json` → name, short_name, theme_color güncelle |
| 6 | Sayfada eski sektör metni görünüyor | Config'de eski değer kalmış | `grep -ri "eski terim" config/` ile tara, düzelt |
| 7 | Build "Duplicate service names" hatası | İki hizmetin `name` alanı aynı | Her `services[].name` unique olmalı |
| 8 | Bölge sayfası üretilmiyor | `activeRegionLimit` aşıldı | `packageConfig.activeRegionLimit` değerini artır |
| 9 | Blog 404 veriyor | Blog devre dışı | `packageConfig.blogEnabled: true` yap |
| 10 | JSON-LD @type hatalı | `schemaType` geçersiz değer | Bölüm 5'teki tablodan doğru tipi seç |
| 11 | Renkler uygulanmıyor | Hex format hatalı | `#RRGGBB` formatı kullan (6 karakter) |
| 12 | WhatsApp linki çalışmıyor | Numara formatı hatalı | `"whatsapp": "+905XXXXXXXXX"` — ülke kodu dahil |
| 13 | Fake rating eklendi | socialProof'a uydurma veri konulmuş | YASAK — gerçek Google Business verisi koy veya bölümü boşalt |
| 14 | Domain uyuşmazlığı | `astro.config.mjs` ≠ `contact.domain` | İkisi de aynı domain'i göstermeli |
| 15 | Font değişmedi | Google Fonts link tag'i eski | BaseLayout.astro'daki `<link>` tag'ini kontrol et |

---

## 9. AI Agent Talimatları

> Bu bölüm, bir AI agent'ın (Claude Code, GPT vb.) bu dokümanı okuyup otonom çalışması için kurallardır.

**Genel kurallar:**
1. Bu dokümanın Adım 1-21'ini sırayla izle. Adım ATLAMA.
2. Her adımda belirtilen format kısıtlarına harfiyen uy.
3. `src/components/`, `src/pages/`, `src/layouts/`, `src/utils/` dosyalarına DOKUNMA.
4. Config tamamlandıktan sonra Bölüm 6'daki Build & Doğrulama Pipeline'ını çalıştır.
5. Build'de 0 hata, grep'te 0 eski sektör metni olmalı.

**Müşteri bilgisi eksikse:**
- Zorunlu alanlar (businessName, sectorLabel, schemaType, phone, domain, services, serviceAreas) → DUR ve SOR.
- Opsiyonel alanlar (pricing, corporate, blog) → Atla, boş bırak.
- socialProof → Gerçek veri yoksa boş bırak. ASLA uydurma.

**Doğrulama sırası:**
1. `npm run build` → 0 hata
2. Eski marka/sektör grep → 0 sonuç
3. Title uniqueness → 0 duplicate
4. H1 kontrolü → sayfa başına 1
5. JSON-LD syntax → 0 hata
6. `npx astro preview` → görsel kontrol

**Başarı kriterleri:**
- 46 (veya bölge sayısına göre değişken) sayfa, 0 hata ile build edildi
- Eski sektör metni hiçbir yerde görünmüyor
- Tüm SEO meta verileri yeni sektöre uygun
- JSON-LD schema'lar geçerli ve doğru @type kullanıyor
