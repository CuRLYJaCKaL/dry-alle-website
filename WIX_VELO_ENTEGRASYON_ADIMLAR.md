# Wix Velo Custom Element Entegrasyon Adımları

## 1. Wix Studio'ya Giriş
- Wix hesabınızla giriş yapın
- Mevcut sitenizi Wix Studio'da açın
- "Dev Mode" veya "Velo" seçeneğini aktif edin

## 2. Custom Element Dosyasını Yükleme

### A. Wix IDE ile:
1. Wix Studio'da **"Code"** panelini açın
2. **"Public"** klasörüne sağ tıklayın
3. **"New File"** > **"JavaScript File"** seçin
4. Dosya adını `dry-alle-custom-element.js` yapın
5. Oluşturulan dosyayı açın ve `dry-alle-custom-element.js` içeriğini kopyalayın

### B. GitHub Integration ile:
1. Projeyi GitHub'a push edin
2. Wix Studio'da **"Settings"** > **"Developer Tools"** > **"Git Integration"**
3. GitHub repository'nizi bağlayın
4. Dosyalar otomatik senkronize olacak

## 3. Görselleri Wix Media Library'ye Yükleme

### Gerekli Görseller:
- `hero-image.png` → Wix Media Library'ye yükleyin
- `dry-cleaning.png` → Service görselleri
- `carpet-cleaning.png` 
- `furniture-cleaning.png`
- `home-textile-cleaning.png`
- `fabric-leather-dyeing.png`
- `shoe-polish-service.png`
- `ironing-service.png`
- `curtain-blind-cleaning.png`
- `luggage-bag-cleaning.png`
- `about-us.png`

### Görsel URL'lerini Güncelleme:
1. Wix Media Library'den her görselin URL'sini kopyalayın
2. Custom Element dosyasında placeholder URL'leri değiştirin:
```javascript
// Örnek:
<img src="https://static.wixstatic.com/media/your-hero-image.jpg" alt="Dry Alle Kuru Temizleme" class="hero-image">
```
↓
```javascript
<img src="https://static.wixstatic.com/media/abc123_hero-image.jpg" alt="Dry Alle Kuru Temizleme" class="hero-image">
```

## 4. Sayfaya Custom Element Ekleme

### A. Yeni Sayfa Oluşturma:
1. **"Site Structure"** > **"Pages"** > **"Add Page"**
2. **"Blank Page"** seçin
3. Sayfa adını "Ana Sayfa" yapın

### B. Custom Element Ekleme:
1. Sayfayı açın
2. **"Add"** > **"Embed"** > **"Custom Element"** seçin
3. Custom Element ayarlarında:
   - **Tag Name**: `dry-alle-website`
   - **Source**: Custom Element dosyanızın yolu
4. Element'i sayfaya yerleştirin ve boyutunu ayarlayın

## 5. Velo Code ile Entegrasyon

### Page Code Örneği:
```javascript
import { DryAlleCustomElement } from 'public/dry-alle-custom-element.js';

$w.onReady(function () {
    // Custom element yüklendiğinde
    $w('#customElement1').onCustomEvent('dry-alle-loaded', (event) => {
        console.log('Dry Alle website loaded:', event.detail.message);
    });

    // Belirli bir servise odaklanma
    $w('#serviceButton').onClick(() => {
        const customElement = $w('#customElement1').getElement();
        customElement.highlightService(0); // İlk servisi vurgula
    });

    // Belirli bölüme scroll
    $w('#aboutButton').onClick(() => {
        const customElement = $w('#customElement1').getElement();
        customElement.scrollToSection('about');
    });

    // İletişim bilgilerini güncelleme
    $w('#updateContactButton').onClick(() => {
        const customElement = $w('#customElement1').getElement();
        customElement.updateContactInfo(
            '0 (216) 352 74 74',
            '0 (543) 352 74 74', 
            'dryallekurutemizleme@gmail.com'
        );
    });
});
```

## 6. CSS Optimizasyonu

### Global CSS Eklemeleri:
1. **"Site"** > **"Global CSS"** bölümüne gidin
2. Aşağıdaki CSS'i ekleyin:
```css
/* Font import'ları */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;500;600;700&display=swap');

/* Custom element container */
dry-alle-website {
    width: 100%;
    display: block;
    min-height: 100vh;
}

/* Wix ile uyumluluk */
.wix-custom-element-wrapper {
    width: 100% !important;
    height: auto !important;
}
```

## 7. Responsive Ayarları

### Desktop/Mobile Optimizasyonu:
1. Custom Element'i seçin
2. **"Layout"** ayarlarında:
   - **Dock**: Full Width
   - **Scaling**: Fit to Width
   - **Mobile behavior**: Same as Desktop

## 8. SEO ve Meta Ayarları

### Page Settings:
1. **"Page Settings"** > **"SEO"**
2. Aşağıdaki bilgileri girin:
   - **Title**: "Dry Alle Kuru Temizleme - Temiz Mevsim Temiz Giysiler"
   - **Description**: "Kadıköy'de profesyonel kuru temizleme, halı yıkama ve koltuk temizliği hizmeti. Ücretsiz kapıdan teslimat."
   - **Keywords**: "kuru temizleme, halı yıkama, koltuk temizliği, kadıköy"

## 9. Test ve Yayınlama

### Test Aşaması:
1. **"Preview"** butonuna tıklayın
2. Desktop ve mobile görünümü test edin
3. Tüm linklerin çalıştığını kontrol edin
4. Form gönderimlerini test edin

### Yayınlama:
1. **"Publish"** butonuna tıklayın
2. Domain ayarlarını kontrol edin
3. SSL sertifikasının aktif olduğunu onaylayın

## 10. Gelişmiş Özellikler

### A. Velo Database Entegrasyonu:
```javascript
import wixData from 'wix-data';

// Hizmet bilgilerini database'den çekme
$w.onReady(async function () {
    try {
        const services = await wixData.query('Services')
            .limit(9)
            .find();
        
        // Custom element'e hizmetleri gönder
        const customElement = $w('#customElement1').getElement();
        customElement.updateServices(services.items);
    } catch (error) {
        console.error('Services loading error:', error);
    }
});
```

### B. Contact Form Integration:
```javascript
import wixCrm from 'wix-crm';

// Form gönderimi yakalama
$w('#customElement1').onCustomEvent('form-submit', async (event) => {
    try {
        const formData = event.detail;
        
        // CRM'e contact ekleme
        await wixCrm.createContact({
            firstName: formData.name,
            phone: formData.phone,
            email: formData.email
        });
        
        console.log('Contact created successfully');
    } catch (error) {
        console.error('Contact creation error:', error);
    }
});
```

### C. Analytics Integration:
```javascript
import wixAnalytics from 'wix-analytics';

// Custom events tracking
$w('#customElement1').onCustomEvent('service-clicked', (event) => {
    wixAnalytics.trackEvent('Service View', {
        serviceName: event.detail.serviceName,
        serviceCategory: event.detail.category
    });
});
```

## 11. Bakım ve Güncelleme

### Güncellemeler:
1. Custom Element dosyasını güncelleyin
2. Wix Studio'da **"Refresh"** yapın
3. **"Preview"** ile test edin
4. **"Publish"** ile yayınlayın

### Monitoring:
1. **"Analytics"** bölümünden traffic'i takip edin
2. **"Site Events"** ile kullanıcı etkileşimlerini izleyin
3. **"Console"** ile hataları kontrol edin

## Notlar:
- Custom Element premium plan gerektirir
- Tüm görseller Wix Media Library üzerinden serve edilmelidir
- External font'lar Google Fonts'tan çekilmelidir
- Cross-domain issues için CORS ayarları gerekebilir

## Destek:
- Wix Velo Docs: https://dev.wix.com/docs/velo
- Custom Elements: https://dev.wix.com/docs/velo/velo-only-apis/$w/custom-element
- Community Forum: https://www.wix.com/velo/forum