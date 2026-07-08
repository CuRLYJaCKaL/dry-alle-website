# SEO Migrasyon ve Redirect Katmanı

Eski statik sitenin (dryallekurutemizleme.com) 112+ URL'sinin hiçbirinin yeni Astro sitesinde 404'e düşmemesini garanti eden katman.

## Bileşenler

| Dosya | Görev |
|---|---|
| `migration/legacy-sitemap.xml` | Eski sitenin sitemap'inin dondurulmuş kopyası. Doğrulamanın tek referansı. |
| `config/migration.config.json` | Kanonik host + tüm 301 redirect tablosu (69 kural, hepsi açık açık listelenmiş — pattern yok). |
| `scripts/generate-redirects.mjs` | Config'i okur, `dist/_redirects` dosyasını üretir (Cloudflare Pages / Netlify formatı: `from to 301` satırları). `dist/` yoksa exit 1. |
| `scripts/verify-migration.mjs` | Her eski URL için: birebir üretim VEYA geçerli redirect var mı kontrol eder. Herhangi bir açık varsa exit 1. |

## Nasıl çalışır

1. `astro build` → `dist/` üretilir. Blog URL'leri (`/blog/{slug}/`) yeni sitede **birebir aynı** yolda üretilir; bunlar redirect ile taşınmaz.
2. `node scripts/generate-redirects.mjs` → `dist/_redirects` yazılır.
3. `node scripts/verify-migration.mjs` → doğrulama:
   - `legacy-sitemap.xml`'deki her URL + config'teki her `from` için: dist altında `index.html` var mı YA DA redirect'i var mı ve redirect hedefi dist'te gerçekten üretilmiş mi.
   - Blog URL'leri için redirect kabul edilmez; `dist/blog/{slug}/index.html` yoksa HATA.
   - Redirect zinciri (hedefin kendisi başka bir kuralın `from`'u olması) HATA.
4. Doğrulama geçmeden deploy edilmez (CI'da build → generate → verify sırası).

## Redirect kuralları (özet)

- **Hizmetler (9):** `/hizmetler/{slug}.html` → `/hizmetler/{slug}/`
- **Bölgeler (49):** `/bolgeler/{location}-{ek}.html` → en-uzun-önek eşleşmesiyle `/bolge/{ilçe}/` veya `/bolge/{ilçe}/{mahalle}/` (örn. `bagdat-caddesi-koltuk-yikama.html` → `/bolge/kadikoy/bagdat-caddesi/`)
- **Sekonder blog makaleleri (8):** `/blog/{slug}/{makale}.html` → `/blog/{slug}/`
- **Diğer (3):** `/index.html` → `/` ; `/hizmetler/` (listeleme) → `/` ; `/fiyatlar.html` → `/fiyatlar/`

Toplam: **69** kural, hepsi 301 (kalıcı).

## Cloudflare Pages'te `_redirects`

- `_redirects` dosyası deploy çıktısının (`dist/`) kök dizininde bulunmalıdır; `generate-redirects.mjs` tam olarak oraya yazar.
- Format: her satır `kaynak hedef durum-kodu` (örn. `/fiyatlar.html /fiyatlar/ 301`).
- Cloudflare Pages statik kuralları önce değerlendirir; eşleşme yoksa statik dosya servis edilir. Kural sayısı limiti (2100 statik) 69 kural için fazlasıyla yeterlidir.
- Segment-içi placeholder (`/bolgeler/:loc-:svc.html` gibi) **desteklenmez**; bu yüzden tüm kurallar açık açık listelenmiştir. Config'e yeni kural eklerken de pattern kullanmayın.
- Netlify aynı formatı desteklediğinden dosya taşınabilirdir.

## www → apex yönlendirmesi

`www.dryallekurutemizleme.com` → `dryallekurutemizleme.com` yönlendirmesi `_redirects` ile **yapılamaz** (host bazlı kural değildir). Bu, DNS/host katmanında çözülür:

- **Cloudflare:** `www` için CNAME (veya proxy'li kayıt) + **Bulk Redirects** ya da tek bir **Redirect Rule**: `www.dryallekurutemizleme.com/*` → `https://dryallekurutemizleme.com/$1`, 301, "preserve query string".
- Kanonik host `config/migration.config.json` içindeki `canonicalHost` alanında tanımlıdır; sayfa `<link rel="canonical">` etiketleri de apex host'u kullanmalıdır.

## Yeni redirect ekleme

1. `config/migration.config.json` → `redirects` dizisine `{ "from": "...", "to": "...", "status": 301 }` ekle (hedef her zaman `/` ile biten yeni-şema URL olmalı, asla başka bir redirect'in `from`'u olmamalı).
2. `node scripts/generate-redirects.mjs && node scripts/verify-migration.mjs` çalıştır.
