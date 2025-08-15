// WhatsApp Business Integration Component
class WhatsAppBusinessWidget {
    constructor() {
        this.phoneNumber = "905433527474";
        this.defaultMessage = "Merhaba, hizmetiniz hakkında bilgi almak istiyorum.";
        this.init();
    }

    init() {
        this.createFloatingButton();
        this.createQuickMessageButtons();
        this.attachEventListeners();
        this.addBusinessSchema();
    }

    createFloatingButton() {
        const floatingBtn = document.createElement('div');
        floatingBtn.id = 'whatsapp-floating';
        floatingBtn.className = 'whatsapp-floating';
        floatingBtn.innerHTML = `
            <div class="whatsapp-btn" onclick="WhatsAppBusiness.openChat()">
                <svg viewBox="0 0 24 24" width="28" height="28" fill="#fff">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.885 3.488"/>
                </svg>
                <span class="whatsapp-text">WhatsApp</span>
            </div>
        `;
        document.body.appendChild(floatingBtn);
    }

    createQuickMessageButtons() {
        // Bölge-specific hızlı mesaj butonları oluştur
        const currentPage = window.location.pathname;
        let serviceType = "genel";
        let location = "";

        if (currentPage.includes('koltuk')) serviceType = "koltuk yıkama";
        if (currentPage.includes('hali')) serviceType = "halı yıkama";
        if (currentPage.includes('kuru')) serviceType = "kuru temizleme";

        // Lokasyon tespiti
        const locationMatch = currentPage.match(/\/([^\/]+)\.html$/);
        if (locationMatch) {
            location = locationMatch[1].replace(/-/g, ' ').replace('koltuk yikama', '').replace('hali yikama', '').replace('kuru temizleme', '').trim();
        }

        this.serviceType = serviceType;
        this.location = location;
    }

    openChat(customMessage = null) {
        let message = customMessage || this.defaultMessage;
        
        if (this.serviceType && this.location) {
            message = `Merhaba, ${this.location} bölgesinde ${this.serviceType} hizmeti almak istiyorum. Detaylı bilgi alabilir miyim?`;
        }

        const encodedMessage = encodeURIComponent(message);
        const whatsappUrl = `https://wa.me/${this.phoneNumber}?text=${encodedMessage}`;
        
        // SEO tracking
        if (typeof gtag !== 'undefined') {
            gtag('event', 'whatsapp_click', {
                'event_category': 'Contact',
                'event_label': this.serviceType + '_' + this.location,
                'value': 1
            });
        }

        window.open(whatsappUrl, '_blank');
    }

    addBusinessSchema() {
        // Local Business Schema für SEO
        const businessSchema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "Dry Alle Kuru Temizleme",
            "description": "İstanbul Anadolu Yakası premium kuru temizleme, koltuk ve halı yıkama hizmeti",
            "telephone": "+90-543-352-7474",
            "url": "https://dryallekurutemizleme.com",
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": "+90-543-352-7474",
                "contactType": "customer service",
                "availableLanguage": "Turkish",
                "contactOption": "TollFree"
            },
            "sameAs": [
                `https://wa.me/${this.phoneNumber}`
            ]
        };

        const script = document.createElement('script');
        script.type = 'application/ld+json';
        script.textContent = JSON.stringify(businessSchema);
        document.head.appendChild(script);
    }

    attachEventListeners() {
        // CTA butonları için WhatsApp entegrasyonu
        document.addEventListener('DOMContentLoaded', () => {
            const ctaButtons = document.querySelectorAll('.cta-button.secondary');
            ctaButtons.forEach(button => {
                if (button.textContent.includes('WhatsApp')) {
                    button.addEventListener('click', (e) => {
                        e.preventDefault();
                        this.openChat();
                    });
                }
            });
        });
    }
}

// Global instance
const WhatsAppBusiness = new WhatsAppBusinessWidget();

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = WhatsAppBusinessWidget;
}