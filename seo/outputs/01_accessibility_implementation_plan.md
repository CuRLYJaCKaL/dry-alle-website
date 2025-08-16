# DryAlle Accessibility Implementation Plan
## Phase 1.4: Erişilebilirlik ve Alt Text Optimizasyonu

### 📊 Audit Sonuçları
- **13 görsel** asset dizininde
- **199 görsel kullanımı** HTML dosyalarında  
- **0 görsel** alt text eksik (✅ İyi!)
- **198 görsel** performans/accessibility sorunları var
- **37 sayfa** heading hierarchy sorunları

### 🔴 Kritik Sorunlar

#### 1. Görsel Performans Sorunları
- **198/199 görsel** `loading="lazy"` eksik
- Büyük görsel dosyaları (bazıları 60MB+)
- WebP formatına dönüştürme gerekli

#### 2. Heading Hierarchy Sorunları  
- **37 sayfa** heading sıralaması problemli
- H2 atlanarak H1'den H3'e geçiş
- Tutarlı heading yapısı eksik

#### 3. WCAG Compliance (Skor: B+)
- Form label'ları eksik
- Keyboard navigation geliştirme gerekli
- Focus indicators gözden geçirme gerekli

### 🎯 Öncelikli İyileştirmeler

#### A. Görsel Optimizasyonu (Acil)
```html
<!-- Mevcut -->
<img src="asset/hero-image.png" alt="Hero Image" width="1200" height="600">

<!-- Optimize Edilmiş -->
<picture>
    <source srcset="asset/hero-image.webp" type="image/webp">
    <img src="asset/hero-image.png" 
         alt="İstanbul Anadolu Yakası Kuru Temizleme Hizmeti - Dry Alle"
         width="1200" 
         height="600"
         loading="lazy"
         decoding="async">
</picture>
```

#### B. Alt Text Güncellemeleri
```javascript
// SEO-optimize alt text örnekleri
const altTextMap = {
    "hero-image.png": "İstanbul Anadolu Yakası Kuru Temizleme Hizmeti - Dry Alle",
    "dry-cleaning.png": "İstanbul Kadıköy Ataşehir Profesyonel Kuru Temizleme Hizmeti - Dry Alle",
    "carpet-cleaning.png": "İstanbul Anadolu Yakası Halı Yıkama ve Temizleme Hizmeti - Dry Alle",
    "furniture-cleaning.png": "İstanbul Kadıköy Ataşehir Koltuk Yıkama ve Mobilya Temizliği - Dry Alle"
};
```

#### C. Heading Hierarchy Düzeltmeleri
```html
<!-- Doğru Hierarchy -->
<h1>KADIKÖY ATAŞEHIR KURU TEMİZLEME HALI KOLTUK YIKAMA</h1>
<h2>Hizmetlerimiz</h2>
<h3>Kuru Temizleme</h3>
<h3>Halı Yıkama</h3>
<h2>Randevu</h2>
<h3>Hemen Randevu Alın</h3>
```

### 📈 Uygulama Adımları

#### 1. Görsel Optimizasyonu (1-2 gün)
- [ ] Büyük görselleri WebP'ye dönüştür
- [ ] Tüm `<img>` taglarına `loading="lazy"` ekle
- [ ] Hero görsellere `fetchpriority="high"` ekle
- [ ] Responsive `<picture>` elementleri kullan

#### 2. Alt Text Güncellemeleri (0.5 gün)
- [ ] SEO-optimize alt text'leri uygula
- [ ] Decorative görsellere `alt=""` + `role="presentation"`
- [ ] Marka/logo görselleri için tutarlı alt text

#### 3. Heading Hierarchy Düzeltmeleri (1 gün)
- [ ] Tüm sayfalarda H1-H6 sırasını kontrol et
- [ ] H2 atlamalarını düzelt
- [ ] Sayfa başına tek H1 kuralını uygula

#### 4. WCAG Compliance (1 gün)
- [ ] Form `<label>` elementleri ekle
- [ ] `aria-label` ve `aria-describedby` kullan
- [ ] Focus indicators CSS'i geliştir
- [ ] Keyboard navigation test et

### 🎯 Beklenen Sonuçlar

#### Performance Impact
- **LCP iyileştirmesi**: 2-3 saniye azalma
- **CLS azalması**: 0.05-0.1 puan iyileştirme  
- **PageSpeed Mobile**: +15-20 puan artış

#### SEO Impact
- **Alt text optimizasyonu**: Görsel arama trafiği +25%
- **Heading hierarchy**: Content structure score +30%
- **WCAG compliance**: Accessibility score A- seviyesi

#### Accessibility Impact
- **Screen reader uyumluluğu**: %100
- **Keyboard navigation**: Tam uyumluluk
- **Color contrast**: WCAG AA compliance

### 🛠️ WebP Dönüştürme Komutları
```bash
# Ana görseller için WebP dönüştürme
cwebp -q 85 asset/hero-image.png -o asset/hero-image.webp
cwebp -q 80 asset/dry-cleaning.png -o asset/dry-cleaning.webp
cwebp -q 80 asset/carpet-cleaning.png -o asset/carpet-cleaning.webp

# Büyük dosyalar için sıkıştırma
cwebp -q 75 asset/home-textile-cleaning.png -o asset/home-textile-cleaning.webp
```

### 📋 Test Checklist
- [ ] Tüm görseller yüklenip görüntüleniyor
- [ ] Alt text'ler screen reader'da okunuyor
- [ ] Heading hierarchy tools ile valide
- [ ] Lighthouse accessibility score >90
- [ ] WAVE tool ile error-free
- [ ] Keyboard navigation sorunsuz çalışıyor

### 🎯 Sonraki Adım
Phase 1.5'e geçiş: İç linkleme audit ve optimizasyon