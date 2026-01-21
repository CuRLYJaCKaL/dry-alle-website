# 🛠️ DryAlle Toplu Güncelleme Sistemleri

Bu proje için **Fiyat** ve **Görsel** güncelleme sistemleri hazırlanmıştır. Her iki sistem de Excel tabanlı, kullanımı kolay ve hatasız çalışmaktadır.

---

## 📦 Mevcut Sistemler

### 1️⃣ Fiyat Güncelleme Sistemi

**Dosyalar:**
- `extract_prices.py` - Mevcut fiyatları Excel'e çıkarır
- `update_prices.py` - Excel'den fiyatları günceller
- `DryAlle_Fiyatlar.csv` - Fiyat listesi (1014 kayıt)
- `FIYAT_GUNCELLEME_KILAVUZU.md` - Detaylı kullanım kılavuzu

**Kullanım:**
```bash
# 1. Mevcut fiyatları çıkar
python3 extract_prices.py

# 2. Excel'de DryAlle_Fiyatlar.csv'yi düzenle
# 3. Güncelle
python3 update_prices.py
```

**Özellikler:**
- ✅ 374 ürün, 1014 fiyat kaydı
- ✅ Otomatik backup
- ✅ Fiyat doğrulama
- ✅ Hata önleme
- ✅ Tek komutla güncelleme

---

### 2️⃣ Görsel Güncelleme Sistemi

**Dosyalar:**
- `extract_images.py` - Ürün ID'lerini ve görselleri listeler
- `update_images.py` - Görselleri otomatik günceller
- `DryAlle_Gorseller.csv` - Görsel listesi (374 ürün)
- `images/products/` - Görsellerin konulacağı klasör
- `GORSEL_GUNCELLEME_KILAVUZU.md` - Detaylı kullanım kılavuzu

**Kullanım:**
```bash
# 1. Ürün ID listesini çıkar
python3 extract_images.py

# 2. Görselleri images/products/ klasörüne koy
#    Dosya adı = Ürün ID (örn: gomlek-erkek.jpg)

# 3. Güncelle
python3 update_images.py
```

**Özellikler:**
- ✅ 374 ürün
- ✅ Otomatik dosya eşleştirme
- ✅ Otomatik backup
- ✅ Çoklu format desteği (JPG, PNG, WebP, SVG)
- ✅ Onay mekanizması

---

## 🚀 Hızlı Başlangıç

### Fiyat Güncellemesi (3 Adım):

```bash
python3 extract_prices.py              # Excel'e çıkar
# Excel'de düzenle
python3 update_prices.py               # Güncelle
```

### Görsel Güncellemesi (3 Adım):

```bash
python3 extract_images.py              # ID listesi çıkar
# Görselleri images/products/ klasörüne koy
python3 update_images.py               # Güncelle
```

---

## 📊 Dosya Yapısı

```
DryAlle/
├── extract_prices.py                  # Fiyat çıkarma
├── update_prices.py                   # Fiyat güncelleme
├── extract_images.py                  # Görsel listesi
├── update_images.py                   # Görsel güncelleme
│
├── DryAlle_Fiyatlar.csv              # Fiyat Excel dosyası
├── DryAlle_Gorseller.csv             # Görsel Excel dosyası
│
├── FIYAT_GUNCELLEME_KILAVUZU.md      # Fiyat kılavuzu
├── GORSEL_GUNCELLEME_KILAVUZU.md     # Görsel kılavuzu
├── README_GUNCELLEME_SISTEMLERI.md   # Bu dosya
│
├── js/
│   └── pricing-data.js                # Ana veri dosyası
│
└── images/
    └── products/                      # Ürün görselleri
        ├── gomlek-erkek.jpg
        ├── takim-elbise.jpg
        └── ...
```

---

## 💡 Excel Dosya Formatları

### Fiyat Excel (DryAlle_Fiyatlar.csv):

| ID | Ürün Adı | Kategori | Alt Kategori | Hizmet Türü | **Fiyat (TL)** | **Popüler** |
|----|----------|----------|--------------|-------------|----------------|-------------|
| gomlek-erkek | GÖMLEK ERKEK | erkek-giyim | erkek-ust-giyim | kuru-temizleme | 95 | EVET |

**Düzenlenebilir sütunlar:** Sadece "Fiyat (TL)" ve "Popüler"

### Görsel Excel (DryAlle_Gorseller.csv):

| ID | Ürün Adı | Kategori | Mevcut Görsel URL | **Yeni Görsel Dosya Adı** |
|----|----------|----------|-------------------|---------------------------|
| gomlek-erkek | GÖMLEK ERKEK | erkek-giyim | https://unsplash.com/... | gomlek-erkek.jpg |

**Not:** Dosya adları ürün ID'leriyle aynı olmalı

---

## 🔒 Güvenlik Özellikleri

### Otomatik Backup:
Her güncelleme öncesi otomatik backup oluşturulur:
```
js/pricing-data_20250130_143022.backup.js
```

### Geri Yükleme:
```bash
# En son backup'ı listele
ls -lt js/pricing-data_*.backup.js | head -1

# Geri yükle
cp js/pricing-data_20250130_143022.backup.js js/pricing-data.js
```

### Doğrulama:
- ✅ Fiyat doğrulama (negatif, boş, geçersiz değerler)
- ✅ Dosya adı kontrolü (ID eşleştirmesi)
- ✅ Onay mekanizması (güncelleme öncesi onay)

---

## 📋 Kullanım Örnekleri

### Örnek 1: Tüm Fiyatlara %10 Zam

1. `python3 extract_prices.py` - Fiyatları çıkar
2. Excel'de yeni sütun: `=F2*1.10`
3. Formülü tüm satırlara kopyala
4. Yeni fiyatları "Fiyat (TL)" sütununa yapıştır
5. `python3 update_prices.py` - Güncelle

### Örnek 2: Sadece Erkek Giyim Görsellerini Güncelle

1. `python3 extract_images.py` - ID listesini çıkar
2. Excel'de filtrele: Kategori = "erkek-giyim"
3. Sadece erkek giyim görsellerini `images/products/` klasörüne koy
4. `python3 update_images.py` - Güncelle

### Örnek 3: Belirli Hizmetlerin Fiyatını Güncelle

1. `python3 extract_prices.py`
2. Excel'de filtrele: Hizmet Türü = "kuru-temizleme"
3. Sadece kuru temizleme fiyatlarını değiştir
4. `python3 update_prices.py`

---

## 🛠️ Sorun Giderme

### Problem: Script çalışmıyor

**Çözüm:**
```bash
# Python versiyonunu kontrol et
python3 --version  # 3.6 veya üzeri olmalı

# Script'leri çalıştırılabilir yap
chmod +x extract_prices.py update_prices.py extract_images.py update_images.py
```

### Problem: CSV dosyası bulunamadı

**Çözüm:**
```bash
# extract scriptini çalıştır
python3 extract_prices.py   # veya
python3 extract_images.py
```

### Problem: Güncelleme yapılmadı

**Kontrol listesi:**
1. ✅ CSV dosyasını CSV formatında kaydettiniz mi?
2. ✅ Sadece düzenlenebilir sütunları değiştirdiniz mi?
3. ✅ ID sütununu değiştirmediniz mi?

**Debug:**
```bash
# Backup dosyalarını kontrol et
ls -la js/pricing-data_*.backup.js

# Son backup'tan geri yükle
cp js/pricing-data_YYYYMMDD_HHMMSS.backup.js js/pricing-data.js
```

---

## 📖 Detaylı Kılavuzlar

Her sistem için detaylı kullanım kılavuzları mevcuttur:

### Fiyat Güncelleme:
```bash
# Kılavuzu oku
cat FIYAT_GUNCELLEME_KILAVUZU.md
# veya VS Code'da aç
code FIYAT_GUNCELLEME_KILAVUZU.md
```

### Görsel Güncelleme:
```bash
# Kılavuzu oku
cat GORSEL_GUNCELLEME_KILAVUZU.md
# veya VS Code'da aç
code GORSEL_GUNCELLEME_KILAVUZU.md
```

---

## 🎯 En İyi Uygulamalar

### 1. Aşamalı Güncelleme
- İlk 10 ürünü güncelleyin
- Test edin
- Sorun yoksa devam edin

### 2. Backup Kontrolü
Her güncellemeden sonra backup oluşturulduğunu kontrol edin:
```bash
ls -la js/pricing-data_*.backup.js
```

### 3. Test Etme
Her güncellemeden sonra tarayıcıda test edin:
- `fiyatlar.html` sayfasını açın
- Ctrl+Shift+R ile cache'siz yenileyin
- Değişiklikleri doğrulayın

### 4. CSV Formatında Kaydetme
Excel'de kaydetme:
- **Dosya** > **Farklı Kaydet**
- **Format**: CSV (virgülle ayrılmış değerler)
- **Encoding**: UTF-8 (önemli!)

### 5. Dosya İsimlendirme (Görseller için)
```
✅ gomlek-erkek.jpg      (doğru)
❌ Gomlek-Erkek.jpg      (büyük harf)
❌ gomlek_erkek.jpg      (alt çizgi)
❌ gömlek-erkek.jpg      (Türkçe karakter)
```

---

## 📞 İletişim ve Destek

### Sorun Bildirimi:
GitHub Issues üzerinden bildirebilirsiniz.

### Katkıda Bulunma:
1. Fork edin
2. Feature branch oluşturun
3. Değişikliklerinizi commit edin
4. Pull request açın

---

## 📈 İstatistikler

### Mevcut Durum:
- **Toplam Ürün**: 374
- **Toplam Fiyat Kaydı**: 1014
- **Kategoriler**: 5 (erkek-giyim, kadin-giyim, cocuk-giyim, ev-tekstili, ozel-temizleme)
- **Hizmet Türleri**: 12 (kuru-temizleme, yikama, utuleme, boyama, vb.)

### Desteklenen Formatlar:
- **Fiyat**: CSV (Excel uyumlu)
- **Görsel**: JPG, PNG, WebP, SVG, GIF

---

## 🎉 Başarılar!

Her iki sistem de hazır ve kullanıma hazır. Detaylı kılavuzları okuyup rahatlıkla kullanabilirsiniz.

**Sorularınız için:** Detaylı kılavuzlara bakın veya bana sorun!

---

## 📅 Versiyon Geçmişi

### v1.0 (2025-01-30)
- ✅ Fiyat güncelleme sistemi
- ✅ Görsel güncelleme sistemi
- ✅ Otomatik backup
- ✅ Doğrulama mekanizmaları
- ✅ Detaylı kılavuzlar
