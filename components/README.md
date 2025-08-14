# Dry Alle Components

Bu klasör, website'de tekrar kullanılabilir component'leri içerir.

## Kullanım

### Hızlı İletişim Component'i

Herhangi bir hizmet sayfasında kullanmak için:

```html
<!-- Hızlı İletişim Component -->
<div class="quick-contact">
    <h3>Hızlı İletişim</h3>
    <div class="contact-item">
        <span class="contact-icon">📞</span>
        <div>
            <strong>Telefon</strong>
            <a href="tel:+902163527474">0 (216) 352 74 74</a>
        </div>
    </div>
    <div class="contact-item">
        <span class="contact-icon">📱</span>
        <div>
            <strong>WhatsApp</strong>
            <a href="tel:+905433527474">0 (543) 352 74 74</a>
        </div>
    </div>
    <div class="contact-item">
        <span class="contact-icon">📧</span>
        <div>
            <strong>E-posta</strong>
            <a href="mailto:dryallekurutemizleme@gmail.com">dryallekurutemizleme@gmail.com</a>
        </div>
    </div>
    <div class="contact-item">
        <span class="contact-icon">📍</span>
        <div>
            <strong>Adres</strong>
            <a href="https://maps.app.goo.gl/2uDnQz3UYnRA8MYK6" target="_blank" style="color: #333; text-decoration: none;">Sahrayı Cedit, Kadıköy, İstanbul</a>
        </div>
    </div>
</div>
```

## Güncelleme

Adres, telefon veya e-posta bilgileri değiştiğinde:
1. `components/quick-contact.html` dosyasını güncelleyin
2. Bu README'deki kodu da güncelleyin
3. Tüm hizmet sayfalarında aynı kodu kullandığınızdan emin olun

## Stil

Component'in stilini `service-detail-styles.css` dosyasında `.quick-contact` class'ı altında bulabilirsiniz.