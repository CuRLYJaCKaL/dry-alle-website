# Haftalık rapor e-postası — kurulum

Rapor her pazartesi 08:00'de (İstanbul) GitHub Actions üzerinden gönderilir.
Kod hazır ve test edildi; aşağıdaki üç adım tamamlanınca çalışır.

## Mevcut durum (2 Ekim 2026'da test edildi)

Elinde zaten bir Google servis hesabı var:

- Dosya: `~/Downloads/dark-runway-462917-n2-dabd325d6ce3.json`
- Hesap: `sporcutakvimi-gsc-reader@dark-runway-462917-n2.iam.gserviceaccount.com`
- GCP projesi: `dark-runway-462917-n2`

Test sonucu:

| Kontrol | Durum |
|---|---|
| Anahtar geçerli, token alınıyor | ✅ |
| Search Console API etkin | ✅ |
| GSC — `sc-domain:sporcutakvimi.com` erişimi | ✅ |
| GSC — DryAlle mülkü erişimi | ❌ paylaşılmamış |
| Analytics Data API etkin | ❌ bu projede hiç açılmamış |

## Yapılacaklar

### 1. Analytics Data API'yi etkinleştir
https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com?project=dark-runway-462917-n2
→ **Etkinleştir**. (Ücretsiz, kota fazlasıyla yeter.)

### 2. Servis hesabını iki mülke ekle

Yukarıdaki `...gserviceaccount.com` adresini şuralara ekle:

- **GA4:** Yönetici → Mülk erişim yönetimi → `+` → rol **Görüntüleyici**
- **Search Console:** (DryAlle mülkü) Ayarlar → Kullanıcılar ve izinler → Kullanıcı ekle → izin **Tam**

### 3. Resend hesabı ve GitHub secret'ları

Resend'de alan adı doğrulanmadığında gönderici `onboarding@resend.dev` olur ve
**yalnızca Resend hesabının sahibi olan e-posta adresine** gönderim yapılabilir.
Bu yüzden Resend'e, raporu almak istediğin adresle kaydol.

GitHub → Settings → Secrets and variables → Actions → **Secrets**:

| Ad | Değer |
|---|---|
| `GOOGLE_SERVICE_ACCOUNT_JSON` | JSON dosyasının tamamı |
| `RESEND_API_KEY` | Resend API anahtarı |
| `REPORT_TO` | raporun gideceği adres (virgülle birden fazla) |

**Variables** (zorunlu değil, varsayılanlar doğru):

| Ad | Varsayılan |
|---|---|
| `REPORT_FROM` | `DryAlle Rapor <rapor@dryallekurutemizleme.com>` — alan adı doğrulanmadıysa `onboarding@resend.dev` yaz |
| `GA4_PROPERTY_ID` | `548056288` |
| `GSC_SITE_URL` | `https://dryallekurutemizleme.com/` |

## Test

Secret'lar girilince beklemeden dene:
GitHub → Actions → **Haftalik performans raporu** → Run workflow.

Yerelde tasarımı görmek için (hiçbir şey göndermez):

```bash
export GOOGLE_SERVICE_ACCOUNT_JSON="$(cat ~/Downloads/dark-runway-462917-n2-*.json)"
npm run rapor -- --dry      # dist-report/rapor.html
```
