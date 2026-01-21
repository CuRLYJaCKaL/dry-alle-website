# 💰 DryAlle Fiyat Güncelleme Kılavuzu

Bu kılavuz, DryAlle projesindeki tüm fiyatları toplu olarak güncellemenizi sağlar.

## 📋 İçindekiler

1. [Hızlı Başlangıç](#hızlı-başlangıç)
2. [Adım Adım Kullanım](#adım-adım-kullanım)
3. [Excel Dosyası Yapısı](#excel-dosyası-yapısı)
4. [Sorun Giderme](#sorun-giderme)

---

## 🚀 Hızlı Başlangıç

### 1. Mevcut Fiyatları Excel'e Çıkar

```bash
python3 extract_prices.py
```

Bu komut `DryAlle_Fiyatlar.csv` dosyasını oluşturur (Excel'de açılabilir).

### 2. Excel'de Fiyatları Düzenle

- `DryAlle_Fiyatlar.csv` dosyasını Excel'de açın
- Fiyatları istediğiniz gibi güncelleyin
- Dosyayı **CSV formatında** kaydedin

### 3. Fiyatları Güncelle

```bash
python3 update_prices.py
```

Bu komut güncellenmiş fiyatları `js/pricing-data.js` dosyasına yazar.

---

## 📝 Adım Adım Kullanım

### Adım 1: Mevcut Fiyatları Çıkarma

Terminal'de proje klasöründe:

```bash
python3 extract_prices.py
```

**Çıktı:**
```
🔍 Fiyat verileri çıkarılıyor...
📦 374 ürün bulundu
✅ Excel dosyası oluşturuldu: DryAlle_Fiyatlar.csv
📊 Toplam 1014 fiyat kaydı çıkarıldı
```

### Adım 2: Excel'de Düzenleme

1. **DryAlle_Fiyatlar.csv** dosyasına çift tıklayın (Excel'de açılır)

2. **Sütunlar:**
   - `ID`: Ürün kimliği (DEĞİŞTİRMEYİN!)
   - `Ürün Adı`: Ürün ismi (DEĞİŞTİRMEYİN!)
   - `Kategori`: Ana kategori (DEĞİŞTİRMEYİN!)
   - `Alt Kategori`: Alt kategori (DEĞİŞTİRMEYİN!)
   - `Hizmet Türü`: Hizmet tipi (DEĞİŞTİRMEYİN!)
   - **`Fiyat (TL)`**: Fiyatı buradan güncelleyin ✏️
   - **`Popüler`**: EVET veya HAYIR ✏️

3. **Örnek Güncelleme:**

   **Önce:**
   ```
   ID              | Ürün Adı      | Hizmet Türü      | Fiyat (TL) | Popüler
   gomlek-erkek    | GÖMLEK ERKEK  | kuru-temizleme   | 95         | EVET
   ```

   **Sonra:**
   ```
   ID              | Ürün Adı      | Hizmet Türü      | Fiyat (TL) | Popüler
   gomlek-erkek    | GÖMLEK ERKEK  | kuru-temizleme   | 120        | EVET
   ```

4. **Kaydet**: Dosyayı **CSV (virgülle ayrılmış değerler)** formatında kaydedin

### Adım 3: Fiyatları Güncelleme

```bash
python3 update_prices.py
```

**Çıktı:**
```
🔄 DryAlle Fiyat Güncelleme Sistemi
==================================================
📂 Excel dosyası: DryAlle_Fiyatlar.csv
📂 JS dosyası: js/pricing-data.js

✅ Fiyatlar doğrulanıyor...
✅ Doğrulama başarılı!

📖 Excel'den fiyatlar okunuyor...
✅ 374 ürün okundu

💾 Backup oluşturuldu: pricing-data_20250130_143022.backup.js

🔄 Fiyatlar güncelleniyor...

==================================================
✨ Güncelleme tamamlandı!
✅ 1014 fiyat güncellendi
```

### Adım 4: Test Etme

1. **Tarayıcıda açın**: `fiyatlar.html`
2. **Kontrol edin**: Fiyatların doğru güncellendiğini doğrulayın
3. **Sorun varsa**: Backup dosyasından geri yükleyin

---

## 📊 Excel Dosyası Yapısı

### Sütun Açıklamaları

| Sütun | Açıklama | Düzenlenebilir? |
|-------|----------|-----------------|
| **ID** | Ürün kimliği (benzersiz) | ❌ HAYIR |
| **Ürün Adı** | Ürünün tam adı | ❌ HAYIR |
| **Kategori** | Ana kategori (erkek-giyim, kadin-giyim, vb.) | ❌ HAYIR |
| **Alt Kategori** | Alt kategori (erkek-ust-giyim, vb.) | ❌ HAYIR |
| **Hizmet Türü** | Hizmet tipi (kuru-temizleme, yikama, vb.) | ❌ HAYIR |
| **Fiyat (TL)** | Fiyat tutarı (sadece rakam) | ✅ EVET |
| **Popüler** | Popüler hizmet mi? (EVET/HAYIR) | ✅ EVET |

### Hizmet Türleri

Sistemde tanımlı hizmet türleri:

- `kuru-temizleme`: Kuru temizleme
- `yikama`: Yaş yıkama
- `utuleme`: Ütüleme
- `boyama`: Boyama (kumaş/deri)
- `leke-cikarma`: Leke çıkarma
- `hali-yikama`: Halı yıkama
- `hali-tamiri`: Halı tamiri
- `sacak-tamiri`: Saçak tamiri
- `hali-boyama`: Halı boyama
- `yerinde-temizleme`: Yerinde temizleme (koltuk, vb.)
- `antibakteriyel`: Antibakteriyel uygulama
- `deri-boyama`: Deri boyama

### Kategoriler

- `erkek-giyim`: Erkek giyim
- `kadin-giyim`: Kadın giyim
- `cocuk-giyim`: Çocuk giyim
- `ev-tekstili`: Ev tekstili (halı, koltuk, perde, vb.)
- `ozel-temizleme`: Özel temizleme (çanta, ayakkabı, vb.)

---

## 🛠️ Sorun Giderme

### Sorun 1: "CSV dosyası bulunamadı" hatası

**Çözüm:**
```bash
python3 extract_prices.py
```

### Sorun 2: "Doğrulama hataları bulundu"

**Olası Nedenler:**
- Fiyat alanına harf yazılmış (sadece rakam olmalı)
- Popüler alanına yanlış değer girilmiş (EVET veya HAYIR olmalı)
- Zorunlu alanlar boş bırakılmış

**Çözüm:** Excel'i açıp hatalı satırları düzeltin.

### Sorun 3: Fiyatlar güncellenmedi

**Kontrol Listesi:**
1. ✅ CSV dosyasını CSV formatında kaydettiniz mi?
2. ✅ ID sütununu değiştirmediniz mi?
3. ✅ Hizmet Türü sütununu değiştirmediniz mi?

### Sorun 4: Güncellemeden sonra sorun çıktı

**Çözüm:** Backup dosyasından geri yükleyin

```bash
# Backup dosyalarını listele
ls -lt js/pricing-data_*.backup.js | head -1

# En son backup'ı geri yükle
cp js/pricing-data_20250130_143022.backup.js js/pricing-data.js
```

---

## 📞 İpuçları

### 💡 İpucu 1: Toplu Fiyat Artırımı

Excel'de formül kullanabilirsiniz:

1. Yeni bir sütun ekleyin: `Yeni Fiyat`
2. Formül: `=G2*1.10` (%10 artış için)
3. Formülü tüm satırlara kopyalayın
4. Yeni fiyatları kopyalayıp `Fiyat (TL)` sütununa yapıştırın (değerler olarak)

### 💡 İpucu 2: Filtreleme

Excel'de filtreleme yaparak belirli kategorilerdeki fiyatları güncelleyebilirsiniz:

1. Header satırını seçin
2. **Veri** > **Filtre**
3. Kategori veya Hizmet Türü'ne göre filtreleyin
4. Sadece görünen satırları güncelleyin

### 💡 İpucu 3: Güvenli Güncelleme

Büyük değişiklikler yapmadan önce:

1. CSV dosyasının bir kopyasını alın
2. Küçük bir test güncellemesi yapın
3. Sonuçları kontrol edin
4. Her şey yolundaysa tüm değişiklikleri yapın

---

## 📋 Checklist: Güvenli Güncelleme

- [ ] `extract_prices.py` ile mevcut fiyatları çıkardım
- [ ] CSV dosyasının yedeğini aldım
- [ ] Excel'de sadece "Fiyat (TL)" ve "Popüler" sütunlarını düzenledim
- [ ] Dosyayı CSV formatında kaydettim
- [ ] `update_prices.py` ile güncelleme yaptım
- [ ] Script'in backup oluşturduğunu gördüm
- [ ] `fiyatlar.html` sayfasını tarayıcıda test ettim
- [ ] Fiyatların doğru göründüğünü onayladım

---

## 🎯 Özet

```
1️⃣ python3 extract_prices.py    → Excel'e çıkar
2️⃣ Excel'de düzenle             → Fiyatları güncelle
3️⃣ python3 update_prices.py     → JS dosyasına yaz
4️⃣ Tarayıcıda test et           → Doğrula
```

**Başarılar! 🎉**
