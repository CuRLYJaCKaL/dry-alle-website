# DryAlle Landing Page Content Template
## Semt × Hizmet Sayfaları İçin Programatik Şablon

### 📋 Template Variables
```
{NEIGHBORHOOD} = Semt adı (örn: Moda, Kozyatağı, Anadolu Hisarı)
{DISTRICT} = İlçe adı (Kadıköy, Ataşehir, Maltepe)  
{SERVICE} = Hizmet adı (Kuru Temizleme, Halı Yıkama, Koltuk Yıkama)
{SERVICE_LOWER} = Hizmet adı küçük harf (kuru temizleme, halı yıkama)
{PHONE} = +90-543-352-7474
{WHATSAPP} = +90-543-352-7474
{BRAND} = Dry Alle
```

---

## 1. Page Meta Information

### Title Tag Pattern:
```
{NEIGHBORHOOD} {SERVICE} | {DISTRICT} | {BRAND}
```

**Examples:**
- Moda Kuru Temizleme | Kadıköy | Dry Alle
- Kozyatağı Halı Yıkama | Ataşehir | Dry Alle
- Anadolu Hisarı Koltuk Yıkama | Ataşehir | Dry Alle

### H1 Pattern:
```
{NEIGHBORHOOD}'da {SERVICE} - Kapıdan Alım Hızlı Teslim
```

**Examples:**
- Moda'da Kuru Temizleme - Kapıdan Alım Hızlı Teslim
- Kozyatağı'nda Halı Yıkama - Kapıdan Alım Hızlı Teslim
- Anadolu Hisarı'nda Koltuk Yıkama - Kapıdan Alım Hızlı Teslim

### Meta Description Pattern:
```
{NEIGHBORHOOD} {SERVICE_lower} için kapıdan alım, hızlı teslim, lüks kumaş uzmanlığı. 25 yıllık deneyim ile güvenilir hizmet. Hemen arayın!
```

---

## 2. Content Template Structure

### Hero Section (100-120 kelime)
```markdown
## {NEIGHBORHOOD}'da En Güvenilir {SERVICE} Hizmeti

{NEIGHBORHOOD}'da yaşıyorsanız ve kaliteli {service_lower} hizmeti arıyorsanız, Dry Alle 25 yıllık deneyimi ile yanınızda. {DISTRICT}'in en köklü tekstil hizmet sağlayıcısı olarak, {NEIGHBORHOOD} sakinlerine özel kapıdan alım ve hızlı teslim hizmeti sunuyoruz.

**Neden {NEIGHBORHOOD} sakinleri bizi tercih ediyor?**
- Kapıdan ücretsiz alım ve teslim
- Aynı gün veya 24 saat içinde teslimat
- Lüks kumaş ve markalı tekstil uzmanlığı
- 25 yıllık sektör deneyimi
- {DISTRICT} genelinde güvenilir referanslar

📞 **Hemen arayın:** [{PHONE}](tel:{PHONE})  
💬 **WhatsApp:** [Randevu Al](https://wa.me/905433527474)
```

### Service Benefits Section (120-150 kelime)
```markdown
## {NEIGHBORHOOD} {SERVICE} Hizmetinin Avantajları

### 🏠 Kapıdan Alım-Teslim Hizmeti
{NEIGHBORHOOD}'da ikamet eden müşterilerimize özel olarak, evinizin kapısından alım ve teslim hizmeti sunuyoruz. İş yoğunluğunuz nedeniyle vakit ayıramıyor musunuz? Hiç sorun değil! Randevu aldığınız saatte kapınızdayız.

### ⚡ Hızlı Teslimat Garantisi
{SERVICE_lower} işlemleriniz için:
- **Acil servis**: Aynı gün teslim (öğle 12:00'a kadar verilen siparişler)
- **Standart servis**: 24-48 saat içinde teslimat
- **Özel kumaşlar**: 3-5 iş günü (kumaş tipine göre)

### 🧵 Lüks Kumaş Uzmanlığı
- İpek, kaşmir, yün gibi hassas kumaşlar
- Markalı giyim ve aksesuar temizliği
- Gelinlik, abiye gibi özel günlük kıyafetler
- Deri ve süet ürünler için özel işlemler

**{NEIGHBORHOOD}'da güvenilir {service_lower} için:** [{PHONE}](tel:{PHONE})
```

### Local Context Section (80-100 kelime)
```markdown
## {NEIGHBORHOOD}'da En Çok Tercih Edilen {SERVICE} Hizmeti

{NEIGHBORHOOD}, {DISTRICT}'in en prestijli semtlerinden biri olarak kaliteli yaşam standardına sahip sakinleri barındırıyor. Bu nedenle tekstil bakım hizmetlerinde de kaliteden ödün vermek istemiyor. 

**{NEIGHBORHOOD} müşteri memnuniyeti:**
- %98 müşteri memnuniyet oranı
- 500+ {NEIGHBORHOOD} hanehalkı müşterimiz
- {DISTRICT} genelinde 15+ yıllık hizmet geçmişi
- Prestijli markaların yetkili temizlik partneri

> *"{NEIGHBORHOOD}'da 8 yıldır Dry Alle hizmetini kullanıyorum. Kalite ve güvenilirlik açısından hiç hayal kırıklığı yaşamadım."*  
> **- {NEIGHBORHOOD} müşterisi**

📱 **WhatsApp Randevu:** [Hemen Mesaj At](https://wa.me/905433527474?text={NEIGHBORHOOD}%20{SERVICE}%20için%20randevu%20almak%20istiyorum)
```

### Call-to-Action Section (60-80 kelime)
```markdown
## {NEIGHBORHOOD} {SERVICE} İçin Hemen İletişime Geçin

Tekstil bakım ihtiyaçlarınız için {NEIGHBORHOOD}'da en güvenilir adres Dry Alle. 25 yıllık deneyimimiz ve müşteri memnuniyet odaklı hizmet anlayışımızla yanınızdayız.

### 📞 Hemen Ara: [{PHONE}](tel:{PHONE})
- **Hafta içi:** 09:00 - 18:00
- **Cumartesi:** 09:00 - 17:00  
- **Pazar:** Kapalı

### 💬 WhatsApp Randevu
[{NEIGHBORHOOD} {SERVICE} Randevu Al](https://wa.me/905433527474?text={NEIGHBORHOOD}%20{SERVICE}%20için%20randevu%20almak%20istiyorum)

### 🚗 Ücretsiz Alım-Teslim
{NEIGHBORHOOD} adresinizden ücretsiz alım, temizlik sonrası kapınıza teslim.
```

---

## 3. Service-Specific Content Variations

### Kuru Temizleme Variations:
```markdown
**Özel vurgular:**
- Hassas kumaş uzmanlığı (ipek, yün, kaşmir)
- Leke çıkarma garantisi
- Kuru temizleme için çevreci çözümler
- Markalı giyim özel bakımı

**Yerel bağlam örneği:**
"{NEIGHBORHOOD}'da yaşayan profesyoneller için iş kıyafetleri, özel günlük giysiler ve hassas kumaşların temizliğinde uzmanız."
```

### Halı Yıkama Variations:
```markdown
**Özel vurgular:**
- El dokuması halı uzmanlığı
- Antika halı restorasyonu
- Leke ve koku giderme
- Halı koruma ve empregne

**Yerel bağlam örneği:**
"{NEIGHBORHOOD}'daki köklü ailelerin değerli halıları için özel bakım ve restorasyon hizmetleri."
```

### Koltuk Yıkama Variations:
```markdown
**Özel vurgular:**
- Deri koltuk özel bakımı
- Kumaş koltuk derin temizlik
- Çekyat ve berjer temizliği
- Koltuk koruma empregne

**Yerel bağlam örneği:**
"{NEIGHBORHOOD}'da modern yaşam alanlarının vazgeçilmezi olan kaliteli mobilyalar için özel temizlik çözümleri."
```

### Gelinlik Temizleme Variations:
```markdown
**Özel vurgular:**
- Gelinlik özel paketleme
- İpek ve tül kumaş uzmanlığı
- Boncuk ve işlemeli detay temizliği
- Uzun süreli muhafaza çözümleri

**Yerel bağlam örneği:**
"{NEIGHBORHOOD}'da düzenlenen düğünler için gelinlik ve abiye temizliğinde güvenilir partner."
```

---

## 4. Technical SEO Elements

### Internal Linking Patterns:
```markdown
**Related Services (Her sayfada):**
- [İpekli Kumaş Temizleme]({DISTRICT}/ipek-temizleme.html)
- [Leke Çıkarma Hizmetleri]({DISTRICT}/leke-cikarma.html)  
- [Express Temizlik]({DISTRICT}/express-temizlik.html)

**Neighborhood Links:**
- [{NEIGHBORHOOD} Diğer Hizmetler](../{NEIGHBORHOOD}/)
- [{DISTRICT} Tüm Semtler](../{DISTRICT}/)
- [Yakın Semtler](nearby-neighborhoods.html)

**Service Category Links:**
- [Tüm {SERVICE} Hizmetleri](../../hizmetler/{service-slug}/)
- [İstanbul {SERVICE}](../../istanbul-{service-slug}/)
```

### Schema Markup Integration:
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Dry Alle {NEIGHBORHOOD} {SERVICE}",
  "serviceType": "{SERVICE}",
  "areaServed": {
    "@type": "Place",
    "name": "{NEIGHBORHOOD}, {DISTRICT}, İstanbul"
  },
  "address": {
    "@type": "PostalAddress", 
    "addressLocality": "{DISTRICT}",
    "addressRegion": "İstanbul",
    "addressCountry": "TR"
  }
}
```

---

## 5. CTA Optimization Matrix

### Primary CTAs:
| Location | CTA Text | Action |
|----------|----------|---------|
| **Hero Section** | "Hemen Ara: {PHONE}" | `tel:{PHONE}` |
| **Service Benefits** | "WhatsApp Randevu Al" | WhatsApp link with pre-filled text |
| **Local Context** | "Ücretsiz Fiyat Teklifi" | Contact form with location pre-filled |
| **Footer** | "{NEIGHBORHOOD} Randevu Al" | WhatsApp with location context |

### Secondary CTAs:
- "Fiyat Listesi İndir" → PDF download
- "Müşteri Yorumları" → Reviews section
- "Diğer Hizmetlerimiz" → Service hub
- "Yakın Semtler" → District hub

---

## 6. Mobile Optimization

### Mobile-First Content Structure:
```html
<!-- Mobile Hero -->
<div class="mobile-hero">
    <h1>{NEIGHBORHOOD} {SERVICE}</h1>
    <p class="mobile-tagline">Kapıdan alım, hızlı teslim</p>
    <div class="mobile-cta-buttons">
        <a href="tel:{PHONE}" class="btn-call">Ara</a>
        <a href="https://wa.me/{WHATSAPP}" class="btn-whatsapp">WhatsApp</a>
    </div>
</div>
```

### Sticky Mobile CTA:
```css
.mobile-sticky-cta {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    z-index: 1000;
}

.btn-mobile-call, .btn-mobile-whatsapp {
    flex: 1;
    padding: 15px;
    text-align: center;
    text-decoration: none;
    font-weight: bold;
}
```

---

## 7. Quality Control Checklist

### Content Quality:
- [ ] 300-400 kelime toplam uzunluk
- [ ] Neighborhood name 5+ kez geçiyor
- [ ] Service name 8+ kez geçiyor  
- [ ] District name 3+ kez geçiyor
- [ ] CTA her 100 kelimede bir
- [ ] Local context authentic

### SEO Optimization:
- [ ] Title 50-60 karakter
- [ ] H1 unique ve descriptive
- [ ] Meta description 150-160 karakter
- [ ] 2+ internal links
- [ ] Schema markup included
- [ ] Mobile-friendly structure

### Conversion Optimization:
- [ ] Primary CTA above fold
- [ ] Phone number clickable
- [ ] WhatsApp pre-filled message
- [ ] Trust signals included
- [ ] Local testimonial/reference
- [ ] Clear value proposition

---

## 8. Implementation Instructions

### Step 1: Variable Replacement
```bash
# Example for Moda Kuru Temizleme
NEIGHBORHOOD="Moda"
DISTRICT="Kadıköy"  
SERVICE="Kuru Temizleme"
SERVICE_LOWER="kuru temizleme"

# Generate content by replacing variables
sed -e "s/{NEIGHBORHOOD}/$NEIGHBORHOOD/g" \
    -e "s/{DISTRICT}/$DISTRICT/g" \
    -e "s/{SERVICE}/$SERVICE/g" \
    -e "s/{SERVICE_LOWER}/$SERVICE_LOWER/g" \
    landing_page_template.md > moda-kuru-temizleme.html
```

### Step 2: Content Customization
- Add neighborhood-specific landmarks
- Include local competition differentiation  
- Add seasonal or event-based content
- Include relevant local images

### Step 3: Quality Assurance
- Readability check (Turkish language)
- Mobile responsiveness test
- CTA functionality test
- Page speed optimization
- Schema markup validation

---

**Template Version:** 2.0  
**Last Updated:** 2025-01-16  
**Target Pages:** 403 Location Landing Pages  
**Content Length:** 300-400 words per page  
**Conversion Goal:** 3-5% phone/WhatsApp contact rate