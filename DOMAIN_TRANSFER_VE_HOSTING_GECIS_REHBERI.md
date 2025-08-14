# 🌐 Wix'ten Custom Hosting'e Geçiş Rehberi
## dryallekurutemizleme.com Domain Transfer + Hosting Geçişi

---

## 📋 Genel Plan
1. **Yeni hosting hazırla** (Netlify/Vercel)
2. **Test domain ile kontrol et**  
3. **Domain transferi başlat**
4. **DNS ayarlarını güncelle**
5. **SSL sertifikası aktif et**

---

## 🚀 ADIM 1: Netlify ile Hızlı Başlangıç

### A) Netlify Hesap Oluşturma
1. [netlify.com](https://netlify.com) → **Sign Up**
2. GitHub ile bağlan (önerilen)
3. **Free Plan** yeterli (100GB bandwidth/ay)

### B) GitHub Repository Oluşturma
```bash
# Terminal'de:
cd /Users/macos/Documents/Projeler/DryAlle
git init
git add .
git commit -m "Initial commit - DryAlle website"
git branch -M main
git remote add origin https://github.com/[kullaniciadi]/dry-alle-website.git
git push -u origin main
```

### C) Netlify Deployment
1. Netlify Dashboard → **"New site from Git"**
2. **GitHub** seçin → Repository'nizi seçin
3. **Build settings**:
   - Build command: *boş bırakın*
   - Publish directory: `./`
4. **"Deploy site"** tıklayın
5. 2-3 dakikada hazır!

---

## 🌍 ADIM 2: Domain Transfer İşlemleri

### A) Wix'ten Domain Transfer Kodu Alma
1. Wix Dashboard → **"Domains"**
2. `dryallekurutemizleme.com` seçin
3. **"Transfer Domain"** → **"Transfer Away from Wix"**
4. **EPP Code/Auth Code** alın (email'e gelir)
5. **Domain Lock'u kaldırın**

⚠️ **Önemli**: Transfer işlemi 5-7 gün sürer, bu sürede site erişilebilir kalır.

### B) Netlify'a Domain Transfer
1. Netlify Dashboard → **"Domains"**
2. **"Add or register domain"**
3. **"Transfer a domain"** seçin
4. Domain: `dryallekurutemizleme.com`
5. EPP Code'u girin
6. Transfer ücretini ödeyin (~$12/yıl)

---

## 🔧 ADIM 3: DNS Geçiş Stratejisi (Risk Minimizasyonu)

### Seçenek A: Anında Geçiş (Recommended)
```bash
# Netlify'da Custom Domain ekleme:
1. Site Settings → Domain Management
2. "Add custom domain" → dryallekurutemizleme.com
3. DNS ayarları otomatik yapılır
```

### Seçenek B: Aşamalı Geçiş
1. **Alt domain** test: `yeni.dryallekurutemizleme.com`
2. Test tamamlandıktan sonra ana domaine geç
3. Eski siteyi backup olarak tut

---

## ⚡ ADIM 4: Hızlı Alternatif - GitHub Pages (Ücretsiz)

### GitHub Pages Setup:
```bash
# Repository settings:
1. GitHub → Repository → Settings
2. Pages → Source: "Deploy from branch"
3. Branch: main / root
4. Save
```

### Custom Domain Ekleme:
1. **CNAME** dosyası oluştur:
```bash
echo "dryallekurutemizleme.com" > CNAME
git add CNAME
git commit -m "Add CNAME for custom domain"
git push
```

2. GitHub Settings → Pages → Custom domain: `dryallekurutemizleme.com`

---

## 🛡️ ADIM 5: SSL ve Güvenlik

### Netlify SSL (Otomatik):
- Let's Encrypt sertifikası otomatik
- HTTPS redirect otomatik aktif

### GitHub Pages SSL:
1. Repository Settings → Pages
2. **"Enforce HTTPS"** aktif et
3. Sertifika otomatik yüklenir

---

## 📊 ADIM 6: Analytics ve SEO

### Google Analytics Ekleme:
```html
<!-- index.html <head> bölümüne ekle -->
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_TRACKING_ID');
</script>
```

### Google Search Console:
1. [search.google.com/search-console](https://search.google.com/search-console)
2. Domain ekle: `dryallekurutemizleme.com`
3. DNS verification ile doğrula

---

## ⏱️ Timeline ve Süreçler

| Aşama | Süre | Açıklama |
|-------|------|----------|
| **Netlify Setup** | 30 dakika | Repository + deployment |
| **Test** | 1 saat | Tüm fonksiyonları test et |
| **Domain Transfer Başlatma** | 1 gün | EPP code alma + başvuru |
| **DNS Yönlendirme** | 24-48 saat | DNS propagation |
| **SSL Aktifleştirme** | 2-24 saat | Otomatik sertifika |
| **Transfer Tamamlanması** | 5-7 gün | Registrar değişimi |

---

## 💰 Maliyet Karşılaştırması

### Netlify:
- **Hosting**: Ücretsiz (100GB/ay)
- **Domain**: ~$12/yıl
- **SSL**: Ücretsiz
- **Toplam**: $12/yıl

### GitHub Pages:
- **Hosting**: Ücretsiz
- **Domain**: Mevcut (transfer yok)
- **SSL**: Ücretsiz  
- **Toplam**: $0/yıl

### Wix Premium:
- **Hosting + Domain**: $200+/yıl
- **Sınırlamalar**: Çok fazla

---

## 🚨 Risk Yönetimi

### Backup Plan:
1. **Mevcut siteyi screenshot**
2. **Wix export** (varsa)
3. **DNS ayarlarını not al**
4. **Email ayarlarını kontrol et**

### Rollback Stratejisi:
```bash
# Sorun çıkarsa hızla geri dön:
1. DNS ayarlarını eski haline getir
2. Wix'te site yeniden aktifleştir
3. 24 saat içinde eski site erişilebilir
```

---

## 🔥 HIZLI BAŞLANGIC (30 Dakika)

### 1. GitHub Repository Oluştur:
```bash
git init
git add .
git commit -m "DryAlle website"
git push -u origin main
```

### 2. Netlify Deploy:
- [netlify.com](https://netlify.com) → New site from Git
- GitHub repo seçin → Deploy

### 3. Test Linki:
- Netlify size `random-name-123.netlify.app` verir
- Test edin, çalışıyor mu kontrol edin

### 4. Domain Bağla:
- Site Settings → Domain Management
- Add custom domain: `dryallekurutemizleme.com`

### 5. Wix DNS Güncelle:
```
A Record: @ → Netlify IP
CNAME: www → site-name.netlify.app
```

---

## 📞 Acil Durum Kontakları

- **Netlify Support**: [support.netlify.com](https://support.netlify.com)
- **GitHub Support**: [support.github.com](https://support.github.com)
- **Domain Transfer**: Registrar support

---

## ✅ Son Kontrol Listesi

- [ ] GitHub repository hazır
- [ ] Netlify deployment başarılı  
- [ ] Test domain çalışıyor
- [ ] Ana domain bağlandı
- [ ] SSL aktif
- [ ] Form submission çalışıyor
- [ ] Mobile responsive test
- [ ] SEO meta tags kontrol
- [ ] Analytics çalışıyor
- [ ] Email delivery test

---

**💡 Önerilen Yol**: Netlify ile başlayın, 30 dakikada test siteniz hazır olur. Domain transfer paralelinde çalıştırın.

Bu rehberi takip ederek risk minimumuyla geçiş yapabilirsiniz!