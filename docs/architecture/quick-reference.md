# DryAlle Blog Sistemi - Hızlı Referans

## 🎯 Tek Cümle Özet
Blog sistemi tamamen merkezi CSS mimarisine geçirildi - herhangi bir güncelleme için sadece 4 ana dosyayı düzenlemen yeterli.

## 📁 Güncelleme Dosyaları

### Blog Kartları → `/styles/components/cards.css`
- Blog ana sayfasındaki kart görünümleri
- Hover efektleri, grid spacing
- Responsive kart davranışı

### Blog Makaleler → `/styles/base/typography.css`  
- Makale başlıkları, içerik tipografisi
- FAQ, CTA, İlgili Makaleler bölümleri
- Mobile responsive font boyutları

### Layout & Sidebar → `/styles/layout/grid.css`
- Blog container, sidebar tasarımı
- Grid sistemleri, responsive layout
- Kategori listesi, arama kutusu

### Renkler & Değişkenler → `/styles/base/variables.css`
- Tüm renkler, spacing, font tanımları
- CSS custom properties
- Site geneli değişkenler

## 🚀 Hızlı Güncelleme Talimatları

### Blog Kartı Değiştirme
```
1. /styles/components/cards.css dosyasını aç
2. .blog-post-card, .modern-blog-card sınıflarını düzenle  
3. Otomatik olarak tüm blog sayfalarına yansır
```

### Makale İçeriği Değiştirme
```
1. /styles/base/typography.css dosyasını aç
2. .article-body, .faq-section, .cta-box sınıflarını düzenle
3. 55+ makale sayfasına otomatik yansır
```

### Renk Değiştirme
```
1. /styles/base/variables.css dosyasını aç
2. --color-primary-darker, --color-secondary değerlerini düzenle
3. Tüm siteye otomatik yansır
```

## ✅ Standartizasyon Durumu
- 55+ blog makale sayfası standartize edildi
- Merkezi CSS mimarisi kuruldu  
- Responsive tasarım optimize edildi
- Corporate tasarım standartları uygulandı
- MIT seviyesinde kod kalitesi sağlandı

## 📋 CSS Sınıf Referansı

### Blog Ana Sayfa
- `.blog-grid`, `.modern-blog-grid` - Ana grid
- `.blog-post-card` - Makale kartları
- `.blog-sidebar` - Yan menü

### Blog Makale Sayfaları  
- `.blog-content` - Ana container
- `.article-header` - Başlık alanı
- `.article-body` - İçerik alanı
- `.faq-section` - FAQ bölümü
- `.blog-cta` - CTA bölümü
- `.related-articles` - İlgili makaleler

## 🔄 AI Asistanı için Talimat
Yeni sessiona bu dokümanı okut ve "Bu blog sisteminde [X] özelliğini güncellemek istiyorum" şeklinde talimat ver. AI doğru dosyayı bulup güncellemeyi yapacak.

---
**Not:** Detaylı bilgi için `blog-system-documentation.md` dosyasını incele.