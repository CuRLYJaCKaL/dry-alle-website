// Ücretsiz Fiyat Teklifi Pop-up Component with WhatsApp Integration
class QuoteFormComponent {
    constructor() {
        this.phoneNumber = "905433527474";
        this.popupCount = 0;
        this.maxPopups = 2;
        this.init();
    }

    init() {
        this.attachEventListeners();
        this.startTimers();
    }

    startTimers() {
        // 1. pop-up: 1 dakika sonra
        setTimeout(() => {
            if (this.popupCount < this.maxPopups) {
                this.showPopup();
                this.popupCount++;
            }
        }, 60000); // 1 dakika

        // 2. pop-up: 3 dakika sonra  
        setTimeout(() => {
            if (this.popupCount < this.maxPopups) {
                this.showPopup();
                this.popupCount++;
            }
        }, 180000); // 3 dakika
    }

    showPopup() {
        const popupHTML = `
            <div class="quote-popup-overlay" id="quote-popup-overlay">
                <div class="quote-popup" id="quote-popup">
                    <button class="quote-popup-close" id="quote-popup-close">&times;</button>
                    <div class="quote-popup-content">
                        <div class="quote-header">
                            <div class="quote-icon">💬</div>
                            <h2>Ücretsiz Fiyat Teklifi</h2>
                            <p>Hızla bilgi alın, WhatsApp'tan anında dönelim!</p>
                        </div>
                        
                        <div class="quote-form-container">
                            <form class="quote-form" id="price-quote-form">
                                <div class="form-row">
                                    <div class="form-group">
                                        <label for="customerName">Ad Soyad *</label>
                                        <input type="text" id="customerName" name="customerName" required>
                                    </div>
                                    <div class="form-group">
                                        <label for="customerPhone">Telefon *</label>
                                        <input type="tel" id="customerPhone" name="customerPhone" required>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-group">
                                        <label for="serviceType">Hizmet Türü *</label>
                                        <select id="serviceType" name="serviceType" required>
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
                                    <div class="form-group">
                                        <label for="customerLocation">Bölgeniz *</label>
                                        <select id="customerLocation" name="customerLocation" required>
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
                                
                                <div class="form-group">
                                    <label for="serviceDetails">Ek Detaylar</label>
                                    <textarea id="serviceDetails" name="serviceDetails" rows="3" placeholder="Kısaca belirtiniz..."></textarea>
                                </div>
                                
                                <div class="form-actions">
                                    <button type="submit" class="quote-submit-btn">
                                        <svg width="20" height="20" fill="#fff" viewBox="0 0 24 24">
                                            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.885 3.488"/>
                                        </svg>
                                        WhatsApp'a Gönder
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        `;

        // Pop-up'ı body'e ekle
        document.body.insertAdjacentHTML('beforeend', popupHTML);
        
        // Pop-up açılma animasyonu
        setTimeout(() => {
            document.getElementById('quote-popup-overlay').classList.add('show');
        }, 100);

        // Close event listeners
        this.attachPopupCloseListeners();
    }

    attachPopupCloseListeners() {
        const closeBtn = document.getElementById('quote-popup-close');
        const overlay = document.getElementById('quote-popup-overlay');
        
        if (closeBtn) {
            closeBtn.addEventListener('click', () => this.closePopup());
        }
        
        if (overlay) {
            overlay.addEventListener('click', (e) => {
                if (e.target === overlay) {
                    this.closePopup();
                }
            });
        }
        
        // ESC tuşu ile kapatma
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                const popup = document.getElementById('quote-popup-overlay');
                if (popup) {
                    this.closePopup();
                }
            }
        });
    }

    closePopup() {
        const overlay = document.getElementById('quote-popup-overlay');
        if (overlay) {
            overlay.classList.add('hide');
            setTimeout(() => {
                overlay.remove();
            }, 300);
        }
    }

    attachEventListeners() {
        document.addEventListener('submit', (e) => {
            if (e.target.id === 'price-quote-form') {
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
            gtag('event', 'quote_popup_submit', {
                'event_category': 'Lead Generation',
                'event_label': `${data.serviceType}_${data.customerLocation}`,
                'value': 1
            });
        }

        // Success feedback
        this.showSuccessMessage();
        
        // Open WhatsApp
        setTimeout(() => {
            window.open(whatsappUrl, '_blank');
            this.closePopup();
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

    showSuccessMessage() {
        const successMessage = document.createElement('div');
        successMessage.className = 'quote-success-message';
        successMessage.innerHTML = `
            <div class="success-content">
                <span class="success-icon">✅</span>
                <h4>Talebiniz alındı!</h4>
                <p>WhatsApp'a yönlendiriliyorsunuz...</p>
            </div>
        `;

        const popup = document.getElementById('quote-popup');
        if (popup) {
            popup.appendChild(successMessage);

            setTimeout(() => {
                successMessage.remove();
            }, 2000);
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const quoteForm = new QuoteFormComponent();
});

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = QuoteFormComponent;
}