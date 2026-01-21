# 📸 DryAlle Görsel Güncelleme Kılavuzu

Bu kılavuz, DryAlle projesindeki tüm ürün görsellerini toplu olarak güncellemenizi sağlar.

## 📋 İçindekiler

1. [Hızlı Başlangıç](#hızlı-başlangıç)
2. [Dosya İsimlendirme Kuralları](#dosya-isimlendirme-kuralları)
3. [Adım Adım Kullanım](#adım-adım-kullanım)
4. [Gelişmiş Kullanım](#gelişmiş-kullanım)
5. [Sorun Giderme](#sorun-giderme)

---

## 🚀 Hızlı Başlangıç

### 3 Basit Adım:

```bash
# 1. Ürün ID'lerini listele
python3 extract_images.py

# 2. Görselleri images/products/ klasörüne koy
#    Dosya adı = Ürün ID + uzantı
#    Örnek: gomlek-erkek.jpg, takim-elbise.png

# 3. Görselleri güncelle
python3 update_images.py
```

---

## 📝 Dosya İsimlendirme Kuralları

### Temel Kural:
**Dosya Adı = Ürün ID + Uzantı**

### Örnekler:

| Ürün ID | Ürün Adı | Dosya Adı |
|---------|----------|-----------|
| `gomlek-erkek` | GÖMLEK ERKEK | `gomlek-erkek.jpg` |
| `takim-elbise` | TAKIM ELBİSE (2 PARÇA) | `takim-elbise.png` |
| `gelinlik` | GELİNLİK | `gelinlik.webp` |
| `hali-yikama` | HALI (m² Başına) | `hali-yikama.jpg` |
| `koltuk-temizleme` | KOLTUK TEMİZLİĞİ | `koltuk-temizleme.png` |

### Desteklenen Formatlar:
- ✅ `.jpg` / `.jpeg` (önerilen)
- ✅ `.png` (şeffaf arka plan için)
- ✅ `.webp` (modern tarayıcılar için)
- ✅ `.svg` (vektör görseller)
- ✅ `.gif` (animasyonlar)

### Önerilen Görsel Boyutları:
- **Genişlik**: 400-800px
- **Yükseklik**: 400-800px
- **Oran**: 1:1 veya 4:3 (kare veya yatay)
- **Dosya boyutu**: < 200 KB (optimize edilmiş)

---

## 📖 Adım Adım Kullanım

### Adım 1: Ürün ID Listesini Çıkarma

```bash
python3 extract_images.py
```

**Çıktı:**
```
🔍 Ürün görselleri listeleniyor...
📦 374 ürün bulundu
✅ Excel dosyası oluşturuldu: DryAlle_Gorseller.csv
```

Bu komut **DryAlle_Gorseller.csv** dosyası oluşturur.

### Adım 2: Excel'de İnceleyin

**DryAlle_Gorseller.csv** dosyasını Excel'de açın:

| ID | Ürün Adı | Kategori | Mevcut Görsel URL | Yeni Görsel Dosya Adı |
|----|----------|----------|-------------------|----------------------|
| gomlek-erkek | GÖMLEK ERKEK | erkek-giyim | https://images.unsplash.com/... | gomlek-erkek.jpg |
| takim-elbise | TAKIM ELBİSE | erkek-giyim | https://images.unsplash.com/... | takim-elbise.jpg |

### Adım 3: Görselleri Hazırlayın

**Görsellerinizi hazırlayın:**

1. **Görsel boyutlarını ayarlayın** (400x400px veya 800x800px)
2. **Dosya boyutunu optimize edin** (< 200 KB)
3. **Dosya adlarını düzenleyin** (ID ile aynı olmalı)

**Örnek:**
```
Orijinal dosya: "erkek_gomlek_foto.jpg"
Yeni ad:        "gomlek-erkek.jpg"
```

### Adım 4: Görselleri Klasöre Koyun

```bash
# Görselleri images/products/ klasörüne kopyalayın
cp ~/Downloads/gomlek-erkek.jpg images/products/
cp ~/Downloads/takim-elbise.png images/products/
cp ~/Downloads/gelinlik.jpg images/products/
```

**Veya Finder'da:**
1. `images/products/` klasörünü açın
2. Görselleri sürükleyip bırakın

### Adım 5: Güncellemeyi Çalıştırın

```bash
python3 update_images.py
```

**Çıktı:**
```
🔄 DryAlle Görsel Güncelleme Sistemi
==================================================

📁 Görsel klasörü taranıyor: images/products
📦 Bulunan Görsel: 3

📸 Bulunan Görseller:
   • gomlek-erkek: gomlek-erkek.jpg (145.2 KB)
   • takim-elbise: takim-elbise.png (189.7 KB)
   • gelinlik: gelinlik.jpg (201.3 KB)

==================================================
⚠️  3 ürünün görseli güncellenecek!
==================================================

❓ Devam etmek istiyor musunuz? (evet/hayir): evet

💾 Backup oluşturuldu: pricing-data_20250130_152045.backup.js

🔄 Görseller güncelleniyor...

   ✅ gomlek-erkek: photo-1594938298603 → gomlek-erkek.jpg
   ✅ takim-elbise: photo-1507003211169 → takim-elbise.png
   ✅ gelinlik: photo-1606800052052 → gelinlik.jpg

==================================================
✨ Güncelleme tamamlandı!
==================================================
✅ 3 görsel güncellendi
```

### Adım 6: Test Edin

1. **Tarayıcıda açın**: `fiyatlar.html`
2. **Görselleri kontrol edin**: Doğru göründüğünden emin olun
3. **Sorun varsa**: Backup'tan geri yükleyin

---

## 🎯 Gelişmiş Kullanım

### Yöntem 1: Toplu Dosya İsimlendirme (Batch Rename)

**macOS/Linux:**
```bash
# Örnek: Tüm JPG dosyalarını küçük harfe çevir
cd images/products/
for file in *.JPG; do
    mv "$file" "${file%.JPG}.jpg"
done
```

**Windows PowerShell:**
```powershell
# Örnek: Boşlukları tire ile değiştir
Get-ChildItem *.jpg | Rename-Item -NewName {$_.Name -replace ' ','-'}
```

### Yöntem 2: Excel ile Manuel Eşleştirme

**DryAlle_Gorseller.csv** dosyasına yeni bir sütun ekleyin:

| ID | Ürün Adı | Yeni Görsel Yolu |
|----|----------|-----------------|
| gomlek-erkek | GÖMLEK ERKEK | images/products/erkek-gomlek.jpg |
| takim-elbise | TAKIM ELBİSE | images/products/suit.png |

Script hem klasör taramasını hem de Excel eşleştirmesini destekler.

### Yöntem 3: Görsel Optimizasyonu

**ImageMagick ile toplu optimize:**
```bash
# Tüm görselleri 800x800'e resize et ve optimize et
cd images/products/
for img in *.jpg; do
    convert "$img" -resize 800x800 -quality 85 "optimized_$img"
done
```

**Online araçlar:**
- https://tinypng.com/ (PNG/JPG sıkıştırma)
- https://squoosh.app/ (WebP dönüştürme)
- https://imagecompressor.com/ (toplu sıkıştırma)

---

## 🛠️ Sorun Giderme

### Sorun 1: "Hiç görsel bulunamadı" hatası

**Çözüm:**
```bash
# 1. Klasörün var olduğunu kontrol edin
ls -la images/products/

# 2. Yoksa oluşturun
mkdir -p images/products/

# 3. Görselleri kopyalayın
cp ~/path/to/images/*.jpg images/products/
```

### Sorun 2: Görsel güncellendi ama görünmüyor

**Olası Nedenler:**
1. ✅ Dosya adı yanlış (ID ile eşleşmiyor)
2. ✅ Dosya yolu yanlış (images/products/ klasöründe değil)
3. ✅ Tarayıcı cache'i (Ctrl+Shift+R ile yenileyin)

**Kontrol:**
```bash
# Dosya adını kontrol et
ls -la images/products/gomlek-erkek.jpg

# ID'yi kontrol et (Excel'de)
grep "gomlek-erkek" DryAlle_Gorseller.csv
```

### Sorun 3: Görsel çok büyük (yavaş yükleniyor)

**Çözüm: Görseli optimize edin**
```bash
# ImageMagick ile optimize et
convert gomlek-erkek.jpg -resize 800x800 -quality 80 gomlek-erkek-opt.jpg

# Dosya boyutunu kontrol et
ls -lh images/products/gomlek-erkek.jpg
```

### Sorun 4: Bazı görseller eşleşmedi

**Kontrol listesi:**
1. Dosya adı tam olarak ID ile aynı mı?
   - ✅ `gomlek-erkek.jpg` (doğru)
   - ❌ `gömlek-erkek.jpg` (Türkçe karakter)
   - ❌ `Gomlek-Erkek.jpg` (büyük harf)
   - ❌ `gomlek_erkek.jpg` (alt çizgi)

2. Uzantı doğru mu?
   - ✅ `.jpg`, `.png`, `.webp`
   - ❌ `.jpeg` (desteklenir ama `.jpg` tercih edilir)

**Debug:**
```bash
# Script'in bulduğu dosyaları listele
python3 update_images.py --dry-run  # (test modu - henüz eklenmedi)
```

### Sorun 5: Güncelleme sonrası sorun çıktı

**Çözüm: Backup'tan geri yükle**
```bash
# En son backup'ı bul
ls -lt js/pricing-data_*.backup.js | head -1

# Geri yükle
cp js/pricing-data_20250130_152045.backup.js js/pricing-data.js

# Sayfayı yenile
# Tarayıcıda fiyatlar.html'i aç ve Ctrl+Shift+R ile yenile
```

---

## 💡 İpuçları ve En İyi Uygulamalar

### 💡 İpucu 1: Görsel İsimlendirme Standartları

**Tutarlı bir isimlendirme kullanın:**
```
✅ gomlek-erkek.jpg
✅ takim-elbise.jpg
✅ hali-yikama.jpg

❌ Gomlek_Erkek.JPG
❌ takim elbise.jpg
❌ HALI-YIKAMA.PNG
```

### 💡 İpucu 2: Toplu Görsel Hazırlama

**Photoshop/GIMP Action:**
1. Bir görsel için işlemleri kaydedin:
   - Resize: 800x800px
   - Optimize: Quality 85%
   - Save: JPG format

2. Batch process ile tüm görsellere uygulayın

### 💡 İpucu 3: WebP Formatı (Modern)

WebP formatı daha küçük dosya boyutu sağlar:

```bash
# JPG'yi WebP'ye dönüştür
cwebp -q 80 gomlek-erkek.jpg -o gomlek-erkek.webp

# Toplu dönüştürme
for img in *.jpg; do
    cwebp -q 80 "$img" -o "${img%.jpg}.webp"
done
```

### 💡 İpucu 4: Aşamalı Güncelleme

Tüm görselleri bir anda değiştirmek yerine:

1. **İlk 10 ürünü** güncelleyin
2. **Test edin**
3. **Sorun yoksa** kalan görselleri ekleyin

```bash
# Sadece belirli görselleri kopyala
cp ~/Downloads/{gomlek-erkek,takim-elbise,ceket-erkek}.jpg images/products/
python3 update_images.py
```

### 💡 İpucu 5: Kategoriye Göre Güncelleme

Excel'de filtreleme yaparak kategorilere göre güncelleyin:

1. **Excel'de filtre açın**: Kategori = "erkek-giyim"
2. **Sadece erkek giyim görsellerini** hazırlayın
3. **Güncelleyin ve test edin**
4. **Diğer kategorilere** geçin

---

## 📊 Ürün ID Örnekleri

### Erkek Giyim:
```
gomlek-erkek.jpg          → GÖMLEK ERKEK
takim-elbise.jpg          → TAKIM ELBİSE (2 PARÇA)
ceket-erkek.jpg           → CEKET ERKEK
esofman-takim.jpg         → EŞOFMAN TAKIM
pantolon.jpg              → PANTOLON
```

### Kadın Giyim:
```
elbise-kadin.jpg          → ELBİSE KADIN (NORMAL)
bluz-kadin.jpg            → BLUZ KADIN
gelinlik.jpg              → GELİNLİK
etek.jpg                  → ETEK
```

### Ev Tekstili:
```
hali-yikama.jpg           → HALI (m² Başına)
koltuk-temizleme.jpg      → KOLTUK TEMİZLİĞİ (Yerinde)
perde.jpg                 → PERDE (m² Başına)
kilim.jpg                 → KİLİM (m² Başına)
yatak-ortüsü.jpg          → YATAK ÖRTÜSÜ
```

### Özel Temizleme:
```
deri-ceket.jpg            → DERİ CEKET
canta.jpg                 → ÇANTA
canta-deri.jpg            → ÇANTA DERİ
ayakkabi.jpg              → AYAKKABI
```

**Tüm ürün ID'leri için:**
```bash
python3 extract_images.py
# DryAlle_Gorseller.csv dosyasını açın
```

---

## 📋 Checklist: Görsel Güncelleme

- [ ] `python3 extract_images.py` ile ID listesini çıkardım
- [ ] Excel'de ürün ID'lerini inceledim
- [ ] Görselleri hazırladım (boyut, kalite, format)
- [ ] Dosya adlarını ID'lerle eşleştirdim (küçük harf, tire ile)
- [ ] Görselleri `images/products/` klasörüne kopyaladım
- [ ] `python3 update_images.py` ile güncelleme yaptım
- [ ] Script'in backup oluşturduğunu gördüm
- [ ] `fiyatlar.html` sayfasını tarayıcıda test ettim
- [ ] Görsellerin doğru göründüğünü onayladım
- [ ] Tarayıcı cache'ini temizleyip yeniden kontrol ettim

---

## 🎯 Özet

```
1️⃣ python3 extract_images.py          → ID listesini çıkar
2️⃣ Görselleri hazırla                 → Boyut, format, isim
3️⃣ images/products/ klasörüne koy     → ID ile aynı isimle
4️⃣ python3 update_images.py           → Güncelle
5️⃣ Tarayıcıda test et                 → Doğrula
```

**Başarılar! 🎉**

---

## 📞 Ek Kaynaklar

### Görsel Optimizasyon Araçları:
- **TinyPNG**: https://tinypng.com/
- **Squoosh**: https://squoosh.app/
- **ImageOptim** (macOS): https://imageoptim.com/

### Toplu İsimlendirme Araçları:
- **Bulk Rename Utility** (Windows)
- **Rename** (macOS/Linux): `brew install rename`
- **PowerRename** (Windows PowerToys)

### Görsel Düzenleme:
- **GIMP**: https://www.gimp.org/ (ücretsiz)
- **Photopea**: https://www.photopea.com/ (online)
- **ImageMagick**: https://imagemagick.org/ (CLI)
