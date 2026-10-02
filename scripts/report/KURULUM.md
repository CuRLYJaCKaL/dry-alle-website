# Haftalık rapor e-postası — kurulum

Rapor her pazartesi 08:00'de (İstanbul) GitHub Actions üzerinden gönderilir.

## Durum (2 Ekim 2026)

Google tarafı **tamamlandı ve canlı veriyle doğrulandı**. Geriye tek adım kaldı: Resend.

### Kullanılan servis hesabı

- Dosya: `~/Downloads/dark-runway-462917-n2-dabd325d6ce3.json`
- Hesap: `sporcutakvimi-gsc-reader@dark-runway-462917-n2.iam.gserviceaccount.com`
- GCP projesi: `dark-runway-462917-n2`

Hesabın adı eski bir projeden geliyor; **veri karışmaz**. Rapor yalnızca iki kaynağı
sorgular, ikisi de DryAlle'ye aittir ve kodda sabittir:
GA4 mülkü `548056288` ve GSC mülkü `https://dryallekurutemizleme.com/`.
Başka hiçbir mülk okunmaz.

| Kontrol | Durum |
|---|---|
| Anahtar geçerli, token alınıyor | ✅ |
| Analytics Data API etkin | ✅ |
| GA4 — DryAlle mülkü (Görüntüleyici) | ✅ |
| Search Console API etkin | ✅ |
| GSC — DryAlle mülkü (Tam) | ✅ |
| Canlı veriyle rapor üretimi | ✅ |

### Repo değişkenleri (yazıldı)

| Ad | Değer |
|---|---|
| `GA4_PROPERTY_ID` | `548056288` |
| `GSC_SITE_URL` | `https://dryallekurutemizleme.com/` |
| `REPORT_FROM` | `DryAlle Rapor <onboarding@resend.dev>` |

## Kalan adımlar

### 1. GOOGLE_SERVICE_ACCOUNT_JSON secret'ı

Terminalde:

```bash
cd ~/Documents/Projeler/DryAlleAstro
gh secret set GOOGLE_SERVICE_ACCOUNT_JSON < ~/Downloads/dark-runway-462917-n2-dabd325d6ce3.json
```

### 2. Resend

Alan adı doğrulanmadığında gönderici `onboarding@resend.dev` olur ve
**yalnızca Resend hesabının sahibi olan adrese** gönderim yapılabilir.
Hesap `asdcjb` olduğundan rapor `asdcjb@gmail.com` adresine gider.

https://resend.com/api-keys → **Create API Key** (izin: *Sending access* yeterli), sonra:

```bash
gh secret set RESEND_API_KEY --body "re_..."
gh secret set REPORT_TO --body "asdcjb@gmail.com"
```

Başka adreslere de göndermek için alan adını doğrulamak gerekir
(Resend → Domains → `dryallekurutemizleme.com` → DNS kayıtları).

## Test

GitHub → Actions → **Haftalik performans raporu** → Run workflow.

Yerelde tasarımı görmek için (hiçbir şey göndermez):

```bash
export GOOGLE_SERVICE_ACCOUNT_JSON="$(cat ~/Downloads/dark-runway-462917-n2-*.json)"
npm run rapor -- --dry      # dist-report/rapor.html
```
