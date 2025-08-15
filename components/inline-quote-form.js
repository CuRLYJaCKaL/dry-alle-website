// Inline Quote Form Component with WhatsApp Integration
class InlineQuoteFormComponent {
    constructor() {
        this.phoneNumber = "905433527474";
        this.init();
    }

    init() {
        this.attachEventListeners();
    }

    attachEventListeners() {
        document.addEventListener('submit', (e) => {
            if (e.target.id === 'inline-price-quote-form') {
                e.preventDefault();
                this.handleFormSubmit(e.target);
            }
        });
    }

    handleFormSubmit(form) {
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        // Form validation
        if (!data.customerName || !data.customerPhone || !data.serviceType || !data.customerLocation) {
            alert('Lütfen zorunlu alanları doldurun!');
            return;
        }

        // WhatsApp mesajını oluştur
        const message = this.createWhatsAppMessage(data);
        
        // WhatsApp'a gönder
        const whatsappUrl = `https://wa.me/${this.phoneNumber}?text=${encodeURIComponent(message)}`;
        
        // Analytics tracking
        if (typeof gtag !== 'undefined') {
            gtag('event', 'inline_quote_submit', {
                'event_category': 'Lead Generation',
                'event_label': `${data.serviceType}_${data.customerLocation}`,
                'value': 1
            });
        }

        // Success feedback
        this.showSuccessMessage(form);
        
        // Open WhatsApp
        setTimeout(() => {
            window.open(whatsappUrl, '_blank');
        }, 1500);
    }

    createWhatsAppMessage(data) {
        const serviceNames = {
            'kuru-temizleme': 'Kuru Temizleme',
            'koltuk-yikama': 'Koltuk Yıkama',
            'hali-yikama': 'Halı Yıkama',
            'perde-temizleme': 'Perde Temizleme',
            'canta-ayakkabi': 'Çanta & Ayakkabı Bakımı',
            'gelinlik-temizleme': 'Gelinlik Temizleme',
            'diger': 'Diğer Hizmet'
        };

        const locationNames = {
            'kadikoy': 'Kadıköy',
            'atasehir': 'Ataşehir',
            'uskudar': 'Üsküdar',
            'acibadem': 'Acıbadem',
            'suadiye': 'Suadiye',
            'erenkoy': 'Erenköy',
            'goztepe': 'Göztepe',
            'bostanci': 'Bostancı',
            'kozyatagi': 'Kozyatağı',
            'altunizade': 'Altunizade',
            'camlica': 'Çamlıca',
            'maltepe': 'Maltepe',
            'kartal': 'Kartal',
            'pendik': 'Pendik',
            'umraniye': 'Ümraniye',
            'diger': 'Diğer Bölge'
        };

        let message = `🧽 *DRY ALLE - FİYAT TEKLİFİ TALEBİ*\\n\\n`;
        message += `👤 *Müşteri Bilgileri:*\\n`;
        message += `• Ad Soyad: ${data.customerName}\\n`;
        message += `• Telefon: ${data.customerPhone}\\n\\n`;
        
        message += `🏠 *Hizmet Detayları:*\\n`;
        message += `• Hizmet Türü: ${serviceNames[data.serviceType] || data.serviceType}\\n`;
        message += `• Bölge: ${locationNames[data.customerLocation] || data.customerLocation}\\n`;
        
        if (data.serviceDetails && data.serviceDetails.trim()) {
            message += `\\n📝 *Ek Detaylar:*\\n${data.serviceDetails.trim()}\\n`;
        }
        
        message += `\\n⏰ *Talep Zamanı:* ${new Date().toLocaleDateString('tr-TR')} ${new Date().toLocaleTimeString('tr-TR')}\\n`;
        message += `\\n💬 Lütfen detaylı fiyat teklifi gönderir misiniz?`;

        return message;
    }

    showSuccessMessage(form) {
        // Mevcut success mesajını kaldır
        const existingMessage = form.parentNode.querySelector('.inline-success-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        const successMessage = document.createElement('div');
        successMessage.className = 'inline-success-message';
        successMessage.innerHTML = `
            <div class="inline-success-content">
                <span class="inline-success-icon">✅</span>
                <h4>Talebiniz alındı!</h4>
                <p>WhatsApp'a yönlendiriliyorsunuz... En kısa sürede size dönüş yapacağız.</p>
            </div>
        `;

        // Form'un altına ekle
        form.parentNode.appendChild(successMessage);

        // Form'u temizle
        form.reset();

        // 5 saniye sonra success mesajını kaldır
        setTimeout(() => {
            if (successMessage.parentNode) {
                successMessage.remove();
            }
        }, 5000);
    }
}

// Inline Quote Form Component'i yükle
function loadInlineQuoteForm() {
    const containers = document.querySelectorAll('.inline-quote-form-container');
    
    if (containers.length === 0) return;
    
    // CSS'i yükle
    loadInlineQuoteCSS();
    
    containers.forEach(container => {
        // HTML'i direkt ekle (daha güvenilir)
        container.innerHTML = getInlineQuoteFormHTML();
        console.log('Inline quote form yüklendi');
    });

    // Component'i initialize et
    const inlineQuoteForm = new InlineQuoteFormComponent();
}

// CSS yükleme fonksiyonu
function loadInlineQuoteCSS() {
    if (!document.querySelector('link[href*="inline-quote-form.css"]')) {
        const cssLink = document.createElement('link');
        cssLink.rel = 'stylesheet';
        // Path'i dinamik olarak ayarla
        const basePath = window.location.pathname.includes('/hizmetler/') ? '../' : '';
        cssLink.href = basePath + 'components/inline-quote-form.css';
        document.head.appendChild(cssLink);
        console.log('Inline quote form CSS yüklendi');
    }
}

// Fallback HTML fonksiyonu
function getInlineQuoteFormHTML() {
    return `
        <!-- Inline Quote Form Component - DryAlle Site Standardı -->
        <section class="inline-quote-section">
            <div class="container">
                <div class="inline-quote-container">
                    <div class="quote-header-inline">
                        <div class="quote-icon-inline">🎯</div>
                        <h2>Ücretsiz Fiyat Teklifi Alın</h2>
                        <p>Hizmetimiz hakkında detaylı bilgi ve özel fiyat teklifimizi hemen öğrenin!</p>
                    </div>
                    
                    <div class="quote-form-wrapper">
                        <form class="inline-quote-form" id="inline-price-quote-form">
                            <div class="inline-form-row">
                                <div class="inline-form-group">
                                    <label for="inlineCustomerName">Adınız Soyadınız *</label>
                                    <input type="text" id="inlineCustomerName" name="customerName" placeholder="Adınız Soyadınız" required>
                                </div>
                                <div class="inline-form-group">
                                    <label for="inlineCustomerPhone">Telefon Numaranız *</label>
                                    <input type="tel" id="inlineCustomerPhone" name="customerPhone" placeholder="Telefon Numaranız" required>
                                </div>
                            </div>
                            
                            <div class="inline-form-row">
                                <div class="inline-form-group">
                                    <label for="inlineServiceType">Hangi hizmeti istiyorsunuz? *</label>
                                    <select id="inlineServiceType" name="serviceType" required>
                                        <option value="">Hizmet seçiniz</option>
                                        <option value="kuru-temizleme">Kuru Temizleme</option>
                                        <option value="koltuk-yikama">Koltuk Yıkama</option>
                                        <option value="hali-yikama">Halı Yıkama</option>
                                        <option value="perde-temizleme">Perde Temizleme</option>
                                        <option value="canta-ayakkabi">Çanta & Ayakkabı Bakımı</option>
                                        <option value="gelinlik-temizleme">Gelinlik Temizleme</option>
                                        <option value="diger">Diğer</option>
                                    </select>
                                </div>
                                <div class="inline-form-group">
                                    <label for="inlineCustomerLocation">Hangi bölgedesiniz? *</label>
                                    <select id="inlineCustomerLocation" name="customerLocation" required>
                                        <option value="">Bölge seçiniz</option>
                                        <option value="kadikoy">Kadıköy</option>
                                        <option value="atasehir">Ataşehir</option>
                                        <option value="uskudar">Üsküdar</option>
                                        <option value="acibadem">Acıbadem</option>
                                        <option value="suadiye">Suadiye</option>
                                        <option value="erenkoy">Erenköy</option>
                                        <option value="goztepe">Göztepe</option>
                                        <option value="bostanci">Bostancı</option>
                                        <option value="kozyatagi">Kozyatağı</option>
                                        <option value="altunizade">Altunizade</option>
                                        <option value="camlica">Çamlıca</option>
                                        <option value="maltepe">Maltepe</option>
                                        <option value="kartal">Kartal</option>
                                        <option value="pendik">Pendik</option>
                                        <option value="umraniye">Ümraniye</option>
                                        <option value="diger">Diğer</option>
                                    </select>
                                </div>
                            </div>
                            
                            <div class="inline-form-group full-width">
                                <label for="inlineServiceDetails">Ek bilgi veya özel ihtiyaçlarınız varsa yazabilirsiniz...</label>
                                <textarea id="inlineServiceDetails" name="serviceDetails" rows="3" placeholder="Ek bilgi veya özel ihtiyaçlarınız varsa yazabilirsiniz..."></textarea>
                            </div>
                            
                            <div class="inline-form-actions">
                                <button type="submit" class="inline-quote-submit-btn">
                                    🚀 Ücretsiz Teklif Al
                                </button>
                                <p class="form-disclaimer">📞 Hemen arayacağız! Bilgileriniz güvenli ve gizlidir.</p>
                            </div>
                        </form>
                    </div>
                    </div>
                </div>
            </div>
        </section>
    `;
}

// DOM ready olduğunda yükle
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadInlineQuoteForm);
} else {
    loadInlineQuoteForm();
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = InlineQuoteFormComponent;
}