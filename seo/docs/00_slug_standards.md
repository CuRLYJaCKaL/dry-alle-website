# DryAlle URL & Naming Standards (Phase 0.3)
**Generated:** January 16, 2025  
**Based on:** Phase 0.2 Information Architecture Blueprint  
**Purpose:** Standardized URL/Meta framework for 341 planned pages

## Executive Summary

This document establishes consistent URL slug patterns, meta tag templates, and naming conventions for DryAlle's complete site structure. All standards are designed for Turkish language optimization, local SEO dominance, and programmatic content generation.

---

## 1. URL Slug Standards

### 1.1 Character Transformation Rules
**Turkish Character Mapping:**
```
ç → c    (Çamlıca → camlica)
ğ → g    (Bağdat → bagdat)  
ö → o    (Göztepe → goztepe)
ş → s    (Ataşehir → atasehir)
ü → u    (Küçük → kucuk)
ı → i    (Kızıltoprak → kiziltoprak)
İ → i    (İçerenköy → icerenkoy)
```

### 1.2 Slug Formation Rules
**Word Separation:** `-` (hyphen)  
**Case:** lowercase only  
**Special Characters:** Remove apostrophes, periods, spaces  
**Multiple Words:** Separate with hyphens  

**Examples:**
- `Sahrayı Cedit` → `sahrayicedit`
- `Küçükbakkalköy` → `kucukbakkalkoy` 
- `Mustafa Kemal` → `mustafakemal`
- `Ataşehir OSB` → `atasehir-osb`

### 1.3 URL Structure Patterns

#### Homepage
```
Pattern: /
URL: https://dryallekurutemizleme.com/
```

#### Service Pages
```
Pattern: /hizmetler/{service-slug}.html
Examples:
  /hizmetler/kuru-temizleme.html
  /hizmetler/gelinlik-temizleme.html
  /hizmetler/hali-yikama.html
```

#### District Hub Pages
```
Pattern: /bolgeler/{district-slug}/
Examples:
  /bolgeler/kadikoy/
  /bolgeler/atasehir/
```

#### Location Landing Pages
```
Pattern: /bolgeler/{district-slug}/{neighborhood-slug}-{service-slug}.html
Examples:
  /bolgeler/kadikoy/sahrayicedit-kuru-temizleme.html
  /bolgeler/atasehir/kucukbakkalkoy-hali-yikama.html
  /bolgeler/kadikoy/fenerbahce-gelinlik-temizleme.html
```

#### Blog Structure
```
Pattern: /blog/{category-slug}/{article-slug}.html
Examples:
  /blog/kuru-temizleme/hassas-kumaslar-rehberi.html
  /blog/yerel/kadikoy-temizlik-rehberi.html
```

---

## 2. Service Slug Definitions

### 2.1 Primary Services
| Service Name | Slug | Priority |
|--------------|------|----------|
| Kuru Temizleme | `kuru-temizleme` | High |
| Gelinlik Temizleme | `gelinlik-temizleme` | High |
| Abiye Temizleme | `abiye-temizleme` | High |
| Valiz Temizleme | `valiz-temizleme` | Medium |
| Bavul Temizleme | `bavul-temizleme` | Medium |
| Halı Yıkama | `hali-yikama` | High |
| Koltuk Yıkama | `koltuk-yikama` | High |
| Perde Temizleme | `perde-temizleme` | Medium |
| Ev Tekstili Temizliği | `ev-tekstili-temizligi` | Medium |
| Çanta Temizleme | `canta-temizleme` | Medium |
| Kumaş Deri Boyama | `kumas-deri-boyama` | Medium |
| Lostra Hizmeti | `lostra-hizmeti` | Medium |
| Ütü Hizmetleri | `utu-hizmetleri` | Low |

### 2.2 Service Variations (for specialized landing pages)
| Variation | Slug | Use Case |
|-----------|------|----------|
| Premium Temizlik | `premium-temizlik` | Luxury neighborhoods |
| VIP Temizlik | `vip-temizlik` | High-end positioning |
| Luxury Hizmet | `luxury-hizmet` | Premium services |
| Haute Couture Temizlik | `haute-couture-temizlik` | Designer garments |

---

## 3. District & Neighborhood Slug Definitions

### 3.1 Kadıköy District
| Neighborhood | Turkish Name | Slug | Status |
|--------------|--------------|------|--------|
| Moda | Moda | `moda` | ✅ Exists |
| Fenerbahçe | Fenerbahçe | `fenerbahce` | ✅ Exists |
| Camlıca | Çamlıca | `camlica` | ✅ Exists |
| Sahrayıcedit | Sahrayı Cedit | `sahrayicedit` | ✅ Exists |
| Kızıltoprak | Kızıltoprak | `kiziltoprak` | 🔄 Create |
| Hasanpaşa | Hasanpaşa | `hasanpasa` | 🔄 Create |
| Rasimpaşa | Rasimpaşa | `rasimpasa` | 🔄 Create |
| Zühtüpaşa | Zühtüpaşa | `zuhtupasa` | 🔄 Create |
| Osmanağa | Osmanağa | `osmanaga` | 🔄 Create |
| Göztepe | Göztepe | `goztepe` | ✅ Exists |
| Erenköy | Erenköy | `erenkoy` | ✅ Exists |
| Suadiye | Suadiye | `suadiye` | ✅ Exists |
| Caddebostan | Caddebostan | `caddebostan` | ✅ Exists |
| Bostancı | Bostancı | `bostanci` | ✅ Exists |
| Kalamış | Kalamış | `kalamis` | ✅ Exists |
| Feneryolu | Feneryolu | `feneryolu` | 🔄 Create |
| Koşuyolu | Koşuyolu | `kosuyolu` | 🔄 Create |
| Altıntepe | Altıntepe | `altintepe` | 🔄 Create |
| Fikirtepe | Fikirtepe | `fikirtepe` | ✅ Exists |

### 3.2 Ataşehir District
| Neighborhood | Turkish Name | Slug | Status |
|--------------|--------------|------|--------|
| Ataşehir Merkez | Ataşehir | `merkez` | ✅ Exists |
| Küçükbakkalköy | Küçükbakkalköy | `kucukbakkalkoy` | ✅ Exists |
| Ferhatpaşa | Ferhatpaşa | `ferhatpasa` | 🔄 Create |
| Barbaros | Barbaros | `barbaros` | ✅ Exists |
| Kayışdağı | Kayışdağı | `kayisdagi` | 🔄 Create |
| Esatpaşa | Esatpaşa | `esatpasa` | 🔄 Create |
| Mustafa Kemal | Mustafa Kemal | `mustafakemal` | 🔄 Create |
| Yenisahra | Yenisahra | `yenisahra` | 🔄 Create |
| İnönü | İnönü | `inonu` | 🔄 Create |
| Örnek | Örnek | `ornek` | 🔄 Create |
| Ataşehir OSB | Ataşehir OSB | `osb` | 🔄 Create |
| Batı Ataşehir | Batı Ataşehir | `bati` | 🔄 Create |

---

## 4. Meta Tag Templates

### 4.1 Title Tag Templates

#### Homepage
```
Template: Kuru Temizleme Halı Yıkama Koltuk Yıkama İstanbul Kadıköy Ataşehir | Dry Alle
Length: 78 characters
```

#### Service Pages
```
Template: {Service} İstanbul Kadıköy Ataşehir | Dry Alle
Example: Gelinlik Temizleme İstanbul Kadıköy Ataşehir | Dry Alle
Length: 45-65 characters (varies by service)
```

#### District Hub Pages
```
Template: {District} Kuru Temizleme Halı Yıkama Hizmetleri | Dry Alle İstanbul
Example: Kadıköy Kuru Temizleme Halı Yıkama Hizmetleri | Dry Alle İstanbul
Length: 55-75 characters
```

#### Location Landing Pages
```
Template: {Neighborhood} {Service} | {District} | Dry Alle
Example: Sahrayicedit Kuru Temizleme | Kadıköy | Dry Alle
Length: 35-55 characters (optimal for local SEO)
```

#### Blog Articles
```
Template: {Article Title} | Dry Alle İstanbul
Example: Hassas Kumaşlar Kuru Temizleme Rehberi | Dry Alle İstanbul
Length: 45-65 characters
```

### 4.2 H1 Tag Templates

#### Homepage
```
Template: İstanbul Anadolu Yakası Kuru Temizleme, Halı Yıkama ve Koltuk Yıkama Uzmanı
```

#### Service Pages
```
Template: İstanbul {Service} Hizmeti
Example: İstanbul Gelinlik Temizleme Hizmeti
```

#### District Hub Pages
```
Template: {District} Kuru Temizleme ve Tekstil Hizmetleri
Example: Kadıköy Kuru Temizleme ve Tekstil Hizmetleri
```

#### Location Landing Pages
```
Template: {Neighborhood}'de {Service}
Example: Sahrayicedit'te Kuru Temizleme
```

### 4.3 Meta Description Templates

#### Homepage
```
Template: İstanbul Anadolu Yakası'nda 25 yıllık deneyimle kuru temizleme, halı yıkama, koltuk yıkama hizmeti. Kadıköy ve Ataşehir'e ücretsiz teslimat. Hemen arayın!
Length: 154 characters
```

#### Service Pages
```
Template: İstanbul Kadıköy ve Ataşehir'de profesyonel {service} hizmeti. 25 yıllık deneyim, ücretsiz teslimat. Anadolu Yakası'nın tüm semtlerine hizmet.
Example: İstanbul Kadıköy ve Ataşehir'de profesyonel gelinlik temizleme hizmeti. 25 yıllık deneyim, ücretsiz teslimat. Anadolu Yakası'nın tüm semtlerine hizmet.
Length: 140-155 characters
```

#### District Hub Pages
```
Template: {District}'de kuru temizleme, halı yıkama, koltuk yıkama hizmetleri. 25 yıllık deneyim, ücretsiz alma-getirme. Tüm semtlere hizmet.
Example: Kadıköy'de kuru temizleme, halı yıkama, koltuk yıkama hizmetleri. 25 yıllık deneyim, ücretsiz alma-getirme. Tüm semtlere hizmet.
Length: 130-145 characters
```

#### Location Landing Pages
```
Template: {Neighborhood} {service} için kapıdan alım, hızlı teslim, lüks kumaş uzmanlığı. 25 yıllık deneyim ile güvenilir hizmet. Hemen arayın!
Example: Sahrayicedit kuru temizleme için kapıdan alım, hızlı teslim, lüks kumaş uzmanlığı. 25 yıllık deneyim ile güvenilir hizmet. Hemen arayın!
Length: 145-155 characters
```

#### Blog Articles
```
Template: {Brief Article Description}. İstanbul Anadolu Yakası {related service} uzmanından ipuçları ve profesyonel tavsiyeleri.
Example: Gelinlik temizleme ve bakım rehberi. İstanbul Anadolu Yakası kuru temizleme uzmanından ipuçları ve profesyonel tavsiyeleri.
Length: 140-155 characters
```

---

## 5. URL Validation Rules

### 5.1 Technical Constraints
- **Max Length:** 100 characters total
- **Special Characters:** Only hyphens allowed
- **Case:** Lowercase only
- **File Extension:** .html for static pages, / for hubs
- **Encoding:** UTF-8 with Turkish character conversion

### 5.2 SEO Optimization Rules
- **Keyword Placement:** Primary keyword within first 50 characters
- **Readability:** Human-readable, descriptive slugs
- **Hyphens:** Separate words, never underscores
- **Redundancy:** No duplicate words in slug

### 5.3 Consistency Checks
**District Names:** Always use official district names (Kadıköy, Ataşehir)  
**Service Names:** Consistent with service slug definitions  
**Neighborhood Names:** Match official municipality names  

---

## 6. Content Standards

### 6.1 Keyword Density Guidelines
- **Primary Keyword:** 1-2% density (neighborhood + service combination)
- **Secondary Keywords:** 0.5-1% density (district, related services)
- **Location Keywords:** Include district, neighborhood, "İstanbul", "Anadolu Yakası"
- **Service Keywords:** Include exact service name + variations

### 6.2 Content Length Standards
- **Homepage:** 800-1200 words
- **Service Pages:** 600-900 words  
- **District Hubs:** 400-600 words
- **Location Landing Pages:** 300-500 words
- **Blog Articles:** 1000-2000 words

### 6.3 Internal Linking Requirements
- **Location Pages:** Minimum 5 internal links (service, district, related neighborhoods)
- **Service Pages:** Minimum 8 internal links (locations, related services, blog)
- **Blog Articles:** Minimum 3 internal links (relevant services/locations)

---

## 7. Quality Assurance Standards

### 7.1 Meta Tag Validation
**Title Tags:**
- ✅ Length 30-60 characters (optimal: 50-55)
- ✅ Include primary keyword within first 30 characters
- ✅ Include brand name "Dry Alle"
- ✅ No duplicate titles across site

**Meta Descriptions:**
- ✅ Length 140-155 characters (optimal: 150-155)
- ✅ Include call-to-action ("Hemen arayın", "Ücretsiz teslimat")
- ✅ Include location and service keywords
- ✅ Compelling and click-worthy language

**H1 Tags:**
- ✅ One H1 per page
- ✅ Include primary keyword (neighborhood + service)
- ✅ Length 20-70 characters
- ✅ Match user search intent

### 7.2 URL Structure Validation
**Technical Requirements:**
- ✅ All lowercase
- ✅ Turkish characters converted
- ✅ Hyphens for word separation
- ✅ No trailing slashes on .html pages
- ✅ Consistent with IA hierarchy

**SEO Requirements:**
- ✅ Keywords in URL slug
- ✅ Readable and descriptive
- ✅ Under 100 characters total
- ✅ No keyword stuffing

---

## 8. Implementation Checklist

### Phase 0.3 Deliverables:
- [x] **Slug Standards Document** (/seo/docs/00_slug_standards.md)
- [ ] **URL Meta Master CSV** (/seo/outputs/03_url_meta_master.csv)
- [ ] **Existing Page Audit** (65 current pages vs standards)
- [ ] **Duplicate Detection Report** (title/meta conflicts)

### Phase 3 Preparation:
- [ ] **Template System** for programmatic page generation
- [ ] **Content Variables** for dynamic meta generation
- [ ] **Quality Checks** for automated content validation
- [ ] **Migration Plan** for existing page updates

---

## 9. Example Applications

### 9.1 High-Priority Location Pages
```
Kadıköy Premium Locations:
/bolgeler/kadikoy/sahrayicedit-kuru-temizleme.html
Title: Sahrayicedit Kuru Temizleme | Kadıköy | Dry Alle
H1: Sahrayicedit'te Kuru Temizleme
Meta: Sahrayicedit kuru temizleme için kapıdan alım, hızlı teslim, lüks kumaş uzmanlığı. 25 yıllık deneyim ile güvenilir hizmet. Hemen arayın!

/bolgeler/kadikoy/fenerbahce-gelinlik-temizleme.html
Title: Fenerbahçe Gelinlik Temizleme | Kadıköy | Dry Alle
H1: Fenerbahçe'de Gelinlik Temizleme
Meta: Fenerbahçe gelinlik temizleme için özel bakım, kapıdan alım, güvenli teslim. 25 yıllık deneyim ile düğün hazırlığınızda yanınızdayız!
```

### 9.2 Service Page Examples
```
Premium Service:
/hizmetler/gelinlik-temizleme.html
Title: Gelinlik Temizleme İstanbul Kadıköy Ataşehir | Dry Alle
H1: İstanbul Gelinlik Temizleme Hizmeti
Meta: İstanbul Kadıköy ve Ataşehir'de profesyonel gelinlik temizleme hizmeti. 25 yıllık deneyim, ücretsiz teslimat. Anadolu Yakası'nın tüm semtlerine hizmet.

Travel Service:
/hizmetler/valiz-temizleme.html
Title: Valiz Temizleme İstanbul Kadıköy Ataşehir | Dry Alle
H1: İstanbul Valiz Temizleme Hizmeti  
Meta: İstanbul Kadıköy ve Ataşehir'de profesyonel valiz temizleme hizmeti. 25 yıllık deneyim, ücretsiz teslimat. Anadolu Yakası'nın tüm semtlerine hizmet.
```

---

## Phase 0.3 Status: 📋 Standards Complete

**Next Step:** Generate URL Meta Master CSV with all 341 planned pages  
**Validation:** Cross-check existing 65 pages against new standards  
**Output:** Ready for Phase 3 programmatic implementation

---

*Generated by DryAlle SEO Strategy Phase 0.3 | URL & Naming Standards Framework*