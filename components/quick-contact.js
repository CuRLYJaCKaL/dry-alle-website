// Quick Contact Component Loader
class QuickContactComponent {
    constructor() {
        this.init();
    }

    init() {
        this.loadComponent();
    }

    loadComponent() {
        const containers = document.querySelectorAll('.quick-contact-container');
        
        if (containers.length === 0) return;
        
        containers.forEach(container => {
            // HTML'i direkt ekle
            container.innerHTML = this.getQuickContactHTML();
            console.log('Quick contact component yüklendi');
        });
    }

    getQuickContactHTML() {
        return `
            <!-- Quick Contact Component - Service Highlights Style -->
            <div class="quick-contact">
                <h3>Hızlı İletişim</h3>
                <div class="contact-info-list">
                    <div class="contact-item">
                        <span class="contact-icon">📞</span>
                        <div class="contact-details">
                            <h4>Telefon</h4>
                            <a href="tel:+905433527474">0 (543) 352 74 74</a>
                        </div>
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">📍</span>
                        <div class="contact-details">
                            <h4>Adres</h4>
                            <a href="https://maps.app.goo.gl/2uDnQz3UYnRA8MYK6" target="_blank">Sahrayı Cedit, Kadıköy</a>
                        </div>
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">🕒</span>
                        <div class="contact-details">
                            <h4>Çalışma Saatleri</h4>
                            <p>Pzt-Cmt: 09:00-18:00</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">💬</span>
                        <div class="contact-details">
                            <h4>WhatsApp</h4>
                            <a href="https://wa.me/905433527474">Hemen Yaz</a>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
}

// Component'i yükle
function loadQuickContact() {
    const quickContact = new QuickContactComponent();
}

// DOM ready olduğunda yükle
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadQuickContact);
} else {
    loadQuickContact();
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = QuickContactComponent;
}