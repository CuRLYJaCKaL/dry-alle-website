/**
 * Components.js - Regional Pages Component System
 * MIT Architecture - Corporate Standard
 * Handles quick contact, lead capture, and mobile sticky bar components
 */

// Quick Contact Component
function initQuickContact() {
    const container = document.querySelector('.quick-contact-container');
    if (!container) return;

    container.innerHTML = `
        <div class="quick-contact-card">
            <h3>Hızlı İletişim</h3>
            <div class="contact-methods">
                <a href="tel:+905433527474" class="contact-method phone">
                    <span class="contact-icon">📞</span>
                    <div class="contact-info">
                        <span class="contact-label">Hemen Arayın</span>
                        <span class="contact-value">0 (543) 352 74 74</span>
                    </div>
                </a>
                <a href="#" class="contact-method whatsapp" onclick="openWhatsApp()">
                    <span class="contact-icon">💬</span>
                    <div class="contact-info">
                        <span class="contact-label">WhatsApp</span>
                        <span class="contact-value">Hızlı Mesaj</span>
                    </div>
                </a>
            </div>
        </div>
    `;
}

// Lead Capture Component  
function initLeadCapture() {
    const container = document.querySelector('.lead-capture-container');
    if (!container) return;

    container.innerHTML = `
        <div class="lead-capture-card">
            <h3>Ücretsiz Fiyat Teklifi</h3>
            <form class="quick-quote-form" onsubmit="handleQuickQuote(event)">
                <div class="form-group">
                    <input type="text" id="customer-name" name="name" placeholder="Adınız" required>
                </div>
                <div class="form-group">
                    <input type="tel" id="customer-phone" name="phone" placeholder="Telefon Numaranız" required>
                </div>
                <div class="form-group">
                    <select name="service" required>
                        <option value="">Hizmet Seçin</option>
                        <option value="hali-yikama">Halı Yıkama</option>
                        <option value="koltuk-yikama">Koltuk Yıkama</option>
                        <option value="kuru-temizleme">Kuru Temizleme</option>
                        <option value="perde-temizleme">Perde Temizleme</option>
                    </select>
                </div>
                <button type="submit" class="quote-button">
                    💰 Fiyat Teklifi Al
                </button>
            </form>
        </div>
    `;
}

// Mobile Sticky Bar Component
function initMobileStickyBar() {
    const container = document.querySelector('.mobile-sticky-bar-container');
    if (!container) return;

    container.innerHTML = `
        <div class="mobile-sticky-bar">
            <div class="sticky-bar-content">
                <a href="tel:+905433527474" class="sticky-action call">
                    <span class="action-icon">📞</span>
                    <span class="action-text">Ara</span>
                </a>
                <a href="#" class="sticky-action whatsapp" onclick="openWhatsApp()">
                    <span class="action-icon">💬</span>
                    <span class="action-text">WhatsApp</span>
                </a>
                <a href="../index.html#contact" class="sticky-action location">
                    <span class="action-icon">📍</span>
                    <span class="action-text">Adres</span>
                </a>
            </div>
        </div>
    `;
}

// Utility Functions
function openWhatsApp() {
    const phone = "905433527474";
    const message = encodeURIComponent("Merhaba, hizmetleriniz hakkında bilgi almak istiyorum.");
    window.open(`https://wa.me/${phone}?text=${message}`, '_blank');
}

function handleQuickQuote(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {
        name: formData.get('name'),
        phone: formData.get('phone'),
        service: formData.get('service')
    };
    
    // GTM tracking
    if (typeof gtag !== 'undefined') {
        gtag('event', 'form_submit', {
            'event_category': 'Lead Capture',
            'event_label': data.service,
            'value': 1
        });
    }
    
    alert('Teşekkürler! En kısa sürede sizinle iletişime geçeceğiz.');
    event.target.reset();
}

// Initialize all components when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initQuickContact();
    initLeadCapture();
    initMobileStickyBar();
});

// Initialize components when the script loads (for dynamic loading)
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        initQuickContact();
        initLeadCapture();
        initMobileStickyBar();
    });
} else {
    // DOM already loaded
    initQuickContact();
    initLeadCapture();
    initMobileStickyBar();
}