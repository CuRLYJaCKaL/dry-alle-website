# 🚀 DNS Yönlendirme ile Hızlı Geçiş
## Domain Transfer Yapmadan Kodu Yayınlama

---

## 💡 Temel Mantık
- **Domain**: Wix'te kalır (`dryallekurutemizleme.com`)
- **DNS**: Netlify'a yönlendirilir  
- **Hosting**: Netlify'da çalışır
- **Süre**: 30 dakika setup + 24 saat DNS propagation

---

## 🚀 ADIM 1: Netlify'da Site Hazırlama (15 dakika)

### A) GitHub Repository + Netlify Deploy
```bash
# Terminal:
cd /Users/macos/Documents/Projeler/DryAlle
git init
git add .
git commit -m "DryAlle website"

# GitHub'a push et (browser'da repo oluştur)
git remote add origin https://github.com/[username]/dry-alle.git
git push -u origin main
```

### B) Netlify Deployment
1. [netlify.com](https://netlify.com) → **Sign up** (GitHub ile)
2. **"New site from Git"** → GitHub seç
3. Repository: `dry-alle` seç
4. **Deploy settings**:
   - Build command: *boş*
   - Publish directory: `./`
5. **Deploy site** → 3 dakikada hazır!

**Test URL'niz**: `https://magical-unicorn-abc123.netlify.app`

---

## 🌐 ADIM 2: Custom Domain Ekleme (5 dakika)

### Netlify'da Domain Setup:
1. **Site dashboard** → **Domain settings**
2. **"Add custom domain"**
3. Domain: `dryallekurutemizleme.com`
4. **"Yes, add domain"**

**Netlify size DNS bilgileri verecek:**
```
Type: A Record
Host: @
Value: 75.2.60.5

Type: CNAME  
Host: www
Value: magical-unicorn-abc123.netlify.app
```

---

## ⚙️ ADIM 3: Wix DNS Ayarlarını Güncelleme (10 dakika)

### A) Wix'te DNS Ayarlarına Gitme:
1. **Wix Dashboard** → **Domains**
2. `dryallekurutemizleme.com` seç
3. **"Manage DNS"** → **"DNS Records"**

### B) DNS Records Güncelleme:
**Mevcut kayıtları sil ve şunları ekle:**

```dns
Type: A
Host: @
Value: 75.2.60.5
TTL: 3600

Type: CNAME
Host: www  
Value: magical-unicorn-abc123.netlify.app
TTL: 3600
```

### C) Mail Records (Varsa Koru):
```dns
Type: MX
Host: @
Value: [mevcut mail server]
Priority: 10

Type: TXT  
Host: @
Value: [mevcut SPF/DKIM records]
```

---

## 📧 ADIM 4: Email Ayarları (Önemli!)

### Mevcut Email Ayarlarınızı Kontrol:
1. Wix Dashboard → **Domains** → **Email**  
2. Email forwarding varsa not alın:
   - `info@dryallekurutemizleme.com` → `hedef@gmail.com`
   - Contact form email ayarları

### Email Devam Etsin:
```dns
# Bu kayıtları KORUYUN:
MX Record: @ → mail.wix.com
TXT Record: @ → "v=spf1 include:_spf.wix.com ~all"
```

---

## 🔍 ADIM 5: Test ve Doğrulama

### A) DNS Propagation Kontrolü:
```bash
# Terminal'de test:
nslookup dryallekurutemizleme.com
dig dryallekurutemizleme.com
```

**Online tool**: [whatsmydns.net](https://whatsmydns.net) → domain girin

### B) Fonksiyonality Test:
- [ ] Ana sayfa açılıyor
- [ ] Mobil responsive çalışıyor  
- [ ] Telefon linkları çalışıyor
- [ ] Smooth scroll çalışıyor
- [ ] Tüm görseller yükleniyor
- [ ] SSL sertifikası aktif (🔒 ikonu)

---

## ⏱️ Timeline

| Zaman | İşlem | Durum |
|-------|--------|--------|
| **0-15 dk** | Netlify deployment | ✅ Test sitesi hazır |
| **15-25 dk** | Custom domain ekleme | ✅ DNS bilgileri alındı |
| **25-35 dk** | Wix DNS güncelleme | ✅ Ayarlar kaydedildi |
| **1-4 saat** | DNS propagation başlar | 🔄 Kademeli yayılma |
| **4-24 saat** | Tam propagation | ✅ Dünya geneli aktif |
| **24-48 saat** | SSL otomatik aktif | 🔒 HTTPS çalışır |

---

## 🚨 Sorun Giderme

### DNS Henüz Yayılmadı:
```bash
# Manuel test:
curl -H "Host: dryallekurutemizleme.com" https://magical-unicorn-abc123.netlify.app
```

### SSL Sorunu:
1. Netlify → **Domain settings**
2. **"Verify DNS configuration"**
3. **"Provision certificate"** (otomatik)

### Email Gelmiyorsa:
1. Wix'te MX records kontrol et
2. DNS'te MX kayıtlarını koru
3. SPF/DKIM kayıtlarını geri ekle

---

## 💰 Maliyet

### Bu Yöntemle:
- **Netlify hosting**: Ücretsiz
- **Domain**: Wix'te kalır (mevcut ücret)
- **SSL**: Ücretsiz
- **Email**: Mevcut ayarlar devam eder

### Fark:
- **Setup**: 30 dakika
- **Transfer gerekmez**: Risk yok
- **Geri dönüş**: DNS ayarlarını eski haline getir

---

## 🔄 Geri Dönüş Planı

**Sorun çıkarsa 5 dakikada geri dön:**
```dns
# Wix DNS'te eski ayarlara dön:
A Record: @ → [eski wix IP]
CNAME: www → [eski wix CNAME]
```

---

## 🎯 HEMEN BAŞLA - Hızlı Komutlar

### 1. GitHub Repository:
```bash
cd /Users/macos/Documents/Projeler/DryAlle
git init
git add .
git commit -m "DryAlle website"
# GitHub'da repo oluştur, sonra:
git remote add origin [repo-url]
git push -u origin main
```

### 2. Netlify:
- [app.netlify.com](https://app.netlify.com) → New site from Git

### 3. DNS Ayarları:
- Netlify'dan IP al → Wix DNS'e ekle

---

## ✅ Final Checklist

- [ ] GitHub repository hazır
- [ ] Netlify deployment başarılı
- [ ] Custom domain Netlify'a eklendi  
- [ ] Wix DNS records güncellendi
- [ ] Email ayarları korundu
- [ ] DNS propagation başladı
- [ ] Test URL çalışıyor
- [ ] SSL sertifikası pending
- [ ] Monitoring setup edildi

**🎉 Sonuç**: Domain transfer yapmadan, 30 dakikada yeni siteniz yayında!

Bu yöntem %100 güvenli - istediğiniz zaman geri dönebilirsiniz.