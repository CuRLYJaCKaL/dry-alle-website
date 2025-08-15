// Elite Neighborhoods Component
class EliteNeighborhoodsComponent {
    constructor(containerId, config = {}) {
        this.containerId = containerId;
        this.config = {
            title: config.title || 'Elite Semtlerde Özel Hizmet',
            subtitle: config.subtitle || 'İstanbul\'un en prestijli mahallelerinde 25 yıldır güvenilir hizmet sunuyoruz',
            cardsToShow: config.cardsToShow || 9,
            rotationInterval: config.rotationInterval || 25000,
            enableRotation: config.enableRotation !== false,
            showOnlyNearby: config.showOnlyNearby || false,
            currentLocation: config.currentLocation || null,
            ...config
        };
        
        this.allCards = [
            // ANADOLU YAKASI - Premium Kuru Temizleme Services
            { 
                href: 'bolgeler/acibadem-kuru-temizleme.html', 
                icon: '🎩', 
                title: 'Acıbadem Kuru Temizleme', 
                desc: 'Premium takım elbise bakımı',
                active: true,
                category: 'kuru-temizleme',
                location: 'acıbadem'
            },
            { 
                href: 'bolgeler/fenerbahce-kuru-temizleme.html', 
                icon: '🏆', 
                title: 'Fenerbahçe Kuru Temizleme', 
                desc: 'Elite kıyafet bakımı',
                active: true,
                category: 'kuru-temizleme',
                location: 'fenerbahçe'
            },
            { 
                href: 'bolgeler/camlica-kuru-temizleme.html', 
                icon: '👔', 
                title: 'Çamlıca VIP Kuru Temizleme', 
                desc: 'Elite kıyafet bakımı',
                active: true,
                category: 'kuru-temizleme',
                location: 'çamlıca'
            },
            { 
                href: 'bolgeler/kozyatagi-kuru-temizleme.html', 
                icon: '💼', 
                title: 'Kozyatağı İş Kıyafetleri', 
                desc: 'Profesyoneller için hızlı servis',
                active: true,
                category: 'kuru-temizleme',
                location: 'kozyatağı'
            },
            { 
                href: 'bolgeler/kadikoy-kuru-temizleme.html', 
                icon: '🎯', 
                title: 'Kadıköy Premium Kuru Temizleme', 
                desc: 'Merkezi lokasyon VIP hizmet',
                active: true,
                category: 'kuru-temizleme',
                location: 'kadıköy'
            },
            
            // ANADOLU YAKASI - Premium Halı Yıkama Services
            { 
                href: 'bolgeler/suadiye-hali-yikama.html', 
                icon: '🏛️', 
                title: 'Suadiye Halı Yıkama', 
                desc: 'Antik ve değerli halı bakımı',
                active: true,
                category: 'hali-yikama',
                location: 'suadiye'
            },
            { 
                href: 'bolgeler/caddebostan-hali-yikama.html', 
                icon: '💎', 
                title: 'Caddebostan Halı Yıkama', 
                desc: 'Lüks halı koleksiyonları',
                active: true,
                category: 'hali-yikama',
                location: 'caddebostan'
            },
            { 
                href: 'bolgeler/erenkoy-hali-yikama.html', 
                icon: '🎨', 
                title: 'Erenköy Antik Halı Yıkama', 
                desc: 'Değerli halı koleksiyonları',
                active: true,
                category: 'hali-yikama',
                location: 'erenköy'
            },
            { 
                href: 'bolgeler/goztepe-hali-yikama.html', 
                icon: '🔍', 
                title: 'Göztepe Lüks Halı Bakımı', 
                desc: 'Premium halı temizleme',
                active: true,
                category: 'hali-yikama',
                location: 'göztepe'
            },
            { 
                href: 'bolgeler/uskudar-hali-yikama.html', 
                icon: '🕌', 
                title: 'Üsküdar Tarihi Halı Yıkama', 
                desc: 'Antik halı koleksiyonları',
                active: true,
                category: 'hali-yikama',
                location: 'üsküdar'
            },
            { 
                href: 'bolgeler/maltepe-hali-yikama.html', 
                icon: '🌊', 
                title: 'Maltepe Marina Halı Yıkama', 
                desc: 'Sahil halı temizleme',
                active: true,
                category: 'hali-yikama',
                location: 'maltepe'
            },
            { 
                href: 'bolgeler/atasehir-hali-yikama.html', 
                icon: '🏢', 
                title: 'Ataşehir Business Halı Yıkama', 
                desc: 'Kurumsal halı temizleme',
                active: true,
                category: 'hali-yikama',
                location: 'ataşehir'
            },
            { 
                href: 'bolgeler/umraniye-hali-yikama.html', 
                icon: '👑', 
                title: 'Ümraniye VIP Halı Yıkama', 
                desc: 'Kraliyet halı bakımı',
                active: true,
                category: 'hali-yikama',
                location: 'ümraniye'
            },
            { 
                href: 'bolgeler/altunizade-hali-yikama.html', 
                icon: '✨', 
                title: 'Altunizade Lüks Halı Yıkama', 
                desc: 'Elite halı koleksiyonları',
                active: true,
                category: 'hali-yikama',
                location: 'altunizade'
            },
            
            // ANADOLU YAKASI - Premium Koltuk Yıkama Services  
            { 
                href: 'bolgeler/kalamis-koltuk-yikama.html', 
                icon: '🪑', 
                title: 'Kalamış Koltuk Yıkama', 
                desc: 'Designer mobilya temizliği',
                active: true,
                category: 'koltuk-yikama',
                location: 'kalamış'
            },
            { 
                href: 'bolgeler/bostanci-koltuk-yikama.html', 
                icon: '🏠', 
                title: 'Bostancı Koltuk Yıkama', 
                desc: 'Premium mobilya bakımı',
                active: true,
                category: 'koltuk-yikama',
                location: 'bostancı'
            },
            { 
                href: 'bolgeler/barbaros-koltuk-yikama.html', 
                icon: '🛡️', 
                title: 'Barbaros Luxury Koltuk Yıkama', 
                desc: 'VIP mobilya bakımı',
                active: true,
                category: 'koltuk-yikama',
                location: 'barbaros'
            },
            { 
                href: 'bolgeler/fikirtepe-koltuk-yikama.html', 
                icon: '🛋️', 
                title: 'Fikirtepe Modern Koltuk Temizliği', 
                desc: 'Çağdaş mobilya bakımı',
                active: true,
                category: 'koltuk-yikama',
                location: 'fikirtepe'
            },
            { 
                href: 'bolgeler/uskudar-koltuk-yikama.html', 
                icon: '🎨', 
                title: 'Üsküdar Antik Mobilya Temizleme', 
                desc: 'Tarihi koltuk bakımı',
                active: true,
                category: 'koltuk-yikama',
                location: 'üsküdar'
            },
            { 
                href: 'bolgeler/kadikoy-koltuk-yikama.html', 
                icon: '🎭', 
                title: 'Kadıköy Sanat Mobilya Yıkama', 
                desc: 'Sanatsal mobilya temizliği',
                active: true,
                category: 'koltuk-yikama',
                location: 'kadıköy'
            },
            { 
                href: 'bolgeler/moda-koltuk-yikama.html', 
                icon: '🌟', 
                title: 'Moda Chic Koltuk Yıkama', 
                desc: 'Trendy mobilya bakımı',
                active: true,
                category: 'koltuk-yikama',
                location: 'moda'
            },
            { 
                href: 'bolgeler/bagdat-caddesi-koltuk-yikama.html', 
                icon: '🛍️', 
                title: 'Bağdat Caddesi VIP Koltuk Yıkama', 
                desc: 'Prestij mobilya temizliği',
                active: true,
                category: 'koltuk-yikama',
                location: 'bağdat-caddesi'
            },
            { 
                href: 'bolgeler/kartal-koltuk-yikama.html', 
                icon: '🦅', 
                title: 'Kartal Premium Koltuk Yıkama', 
                desc: 'Yüksek kalite mobilya bakımı',
                active: true,
                category: 'koltuk-yikama',
                location: 'kartal'
            },
            { 
                href: 'bolgeler/pendik-koltuk-yikama.html', 
                icon: '⚓', 
                title: 'Pendik Marina Koltuk Yıkama', 
                desc: 'Sahil mobilya temizliği',
                active: true,
                category: 'koltuk-yikama',
                location: 'pendik'
            },
            
            // ANADOLU YAKASI - Luxury Gelinlik & Özel Kıyafet Services
            { 
                href: 'bolgeler/uskudar-gelinlik-temizleme.html', 
                icon: '💍', 
                title: 'Üsküdar Gelinlik Temizleme', 
                desc: 'Özel günler için hassas bakım',
                active: true,
                category: 'gelinlik-temizleme',
                location: 'üsküdar'
            },
            { 
                href: 'bolgeler/kadikoy-luxury-kiyafet.html', 
                icon: '👗', 
                title: 'Kadıköy Luxury Kıyafet Bakımı', 
                desc: 'Designer kıyafet temizleme',
                active: true,
                category: 'luxury-kiyafet',
                location: 'kadıköy'
            },
            { 
                href: 'bolgeler/atasehir-premium-temizlik.html', 
                icon: '🏢', 
                title: 'Ataşehir Premium İş Kıyafetleri', 
                desc: 'İş merkezleri için VIP hizmet',
                active: true,
                category: 'premium-temizlik',
                location: 'ataşehir'
            },
            { 
                href: 'bolgeler/bagdat-caddesi-haute-couture.html', 
                icon: '✨', 
                title: 'Bağdat Caddesi Haute Couture Bakımı', 
                desc: 'En lüks kıyafetler için özel hizmet',
                active: true,
                category: 'haute-couture',
                location: 'bağdat-caddesi'
            },
            
            // EKSİK SAYFALARI EKLENDİ - SEO CROSS-LİNKİNG İÇİN KRİTİK
            { 
                href: 'bolgeler/altunizade-premium-temizlik.html', 
                icon: '🏢', 
                title: 'Altunizade Premium Temizlik', 
                desc: 'Profesyonel iş merkezi hizmeti',
                active: true,
                category: 'premium-temizlik',
                location: 'altunizade'
            },
            { 
                href: 'bolgeler/icerenkoy-hali-yikama.html', 
                icon: '🎨', 
                title: 'İçerenköy Halı Yıkama', 
                desc: 'Antik ve değerli halı bakımı',
                active: true,
                category: 'hali-yikama',
                location: 'içerenköy'
            },
            { 
                href: 'bolgeler/kucukbakkalkoy-hali-yikama.html', 
                icon: '🏡', 
                title: 'Küçükbakkalçıköy Halı Yıkama', 
                desc: 'Komşu dost halı temizliği',
                active: true,
                category: 'hali-yikama',
                location: 'küçükbakkalköy'
            },
            { 
                href: 'bolgeler/kucukbakkalkoy-koltuk-yikama.html', 
                icon: '🛋️', 
                title: 'Küçükbakkalçıköy Koltuk Yıkama', 
                desc: 'Mahalle mobilya temizliği',
                active: true,
                category: 'koltuk-yikama',
                location: 'küçükbakkalköy'
            },
            { 
                href: 'bolgeler/maltepe-luxury-hizmet.html', 
                icon: '💎', 
                title: 'Maltepe Luxury Hizmet', 
                desc: 'Lüks koltuk ve halı bakımı',
                active: true,
                category: 'luxury-hizmet',
                location: 'maltepe'
            },
            { 
                href: 'bolgeler/sahrayicedit-premium-bakim.html', 
                icon: '🎆', 
                title: 'Sahrayıcedit Premium Bakım', 
                desc: 'Merkez lokasyon premium hizmet',
                active: true,
                category: 'premium-bakim',
                location: 'sahrayıcedit'
            },
            { 
                href: 'bolgeler/umraniye-vip-temizlik.html', 
                icon: '⭐', 
                title: 'Ümraniye VIP Temizlik', 
                desc: 'VIP kıyafet ve tekstil bakımı',
                active: true,
                category: 'vip-temizlik',
                location: 'ümraniye'
            },
            { 
                href: 'bolgeler/uskudar-luxury-kiyafet.html', 
                icon: '👗', 
                title: 'Üküdar Luxury Kıyafet', 
                desc: 'Tarihi semtte lüks kıyafet bakımı',
                active: true,
                category: 'luxury-kiyafet',
                location: 'üsküdar'
            }
        ];
        
        this.currentStartIndex = 0;
        this.init();
    }
    
    init() {
        this.createComponent();
        if (this.config.enableRotation) {
            this.startRotation();
        }
    }
    
    createComponent() {
        const container = document.getElementById(this.containerId);
        if (!container) return;
        
        const cardsToDisplay = this.getCardsToDisplay();
        
        container.innerHTML = `
            <section class="elite-neighborhoods">
                <div class="container">
                    <h2>${this.config.title}</h2>
                    <p>${this.config.subtitle}</p>
                    <div class="neighborhoods-scroll-container">
                        <div class="neighborhoods-grid" id="${this.containerId}-grid">
                            ${this.renderCards(cardsToDisplay)}
                        </div>
                    </div>
                    <div class="neighborhoods-info" itemscope itemtype="https://schema.org/ServiceArea">
                        <p>Hizmet verdiğimiz diğer elite bölgeler: <span itemprop="areaServed">${this.getOtherLocations()}</span></p>
                    </div>
                </div>
            </section>
        `;
        
        this.attachEventListeners();
    }
    
    getCardsToDisplay() {
        if (this.config.showOnlyNearby && this.config.currentLocation) {
            return this.getNearbyCards();
        }
        
        const startIndex = this.currentStartIndex;
        const cardsToShow = this.config.cardsToShow;
        const cards = [];
        
        for (let i = 0; i < cardsToShow; i++) {
            const cardIndex = (startIndex + i) % this.allCards.length;
            cards.push(this.allCards[cardIndex]);
        }
        
        return cards;
    }
    
    getNearbyCards() {
        const currentLocation = this.config.currentLocation;
        const nearbyMap = {
            // ANADOLU YAKASI CROSS-LINKING - 8 nearby locations per area
            'acıbadem': ['fenerbahçe', 'kozyatağı', 'çamlıca', 'altunizade', 'ataşehir', 'üsküdar', 'maltepe', 'ümraniye'],
            'suadiye': ['caddebostan', 'bağdat-caddesi', 'kalamış', 'fenerbahçe', 'erenköy', 'bostancı', 'göztepe', 'moda'],
            'caddebostan': ['suadiye', 'bağdat-caddesi', 'kalamış', 'erenköy', 'fenerbahçe', 'bostancı', 'göztepe', 'moda'],
            'erenköy': ['göztepe', 'caddebostan', 'suadiye', 'fikirtepe', 'kadıköy', 'bağdat-caddesi', 'moda', 'kalamış'],
            'göztepe': ['erenköy', 'fikirtepe', 'kadıköy', 'bağdat-caddesi', 'moda', 'caddebostan', 'suadiye', 'üsküdar'],
            'fenerbahçe': ['acıbadem', 'suadiye', 'kalamış', 'bostancı', 'caddebostan', 'kozyatağı', 'çamlıca', 'barbaros'],
            'çamlıca': ['acıbadem', 'altunizade', 'üsküdar', 'kozyatağı', 'fenerbahçe', 'ataşehir', 'maltepe', 'ümraniye'],
            'kozyatağı': ['acıbadem', 'ataşehir', 'çamlıca', 'altunizade', 'fenerbahçe', 'barbaros', 'ümraniye', 'maltepe'],
            'kalamış': ['suadiye', 'caddebostan', 'bostancı', 'fenerbahçe', 'erenköy', 'barbaros', 'moda', 'bağdat-caddesi'],
            'bostancı': ['kalamış', 'barbaros', 'suadiye', 'fenerbahçe', 'caddebostan', 'ataşehir', 'kozyatağı', 'altunizade'],
            'barbaros': ['bostancı', 'ataşehir', 'kozyatağı', 'altunizade', 'kalamış', 'suadiye', 'fenerbahçe', 'caddebostan'],
            'fikirtepe': ['göztepe', 'erenköy', 'kadıköy', 'üsküdar', 'moda', 'bağdat-caddesi', 'çamlıca', 'altunizade'],
            'üsküdar': ['çamlıca', 'fikirtepe', 'altunizade', 'maltepe', 'acıbadem', 'göztepe', 'kadıköy', 'ümraniye'],
            'kadıköy': ['göztepe', 'fikirtepe', 'moda', 'bağdat-caddesi', 'erenköy', 'üsküdar', 'caddebostan', 'suadiye'],
            'ataşehir': ['kozyatağı', 'barbaros', 'ümraniye', 'altunizade', 'acıbadem', 'çamlıca', 'maltepe', 'bostancı'],
            'maltepe': ['üsküdar', 'altunizade', 'kartal', 'ataşehir', 'çamlıca', 'ümraniye', 'acıbadem', 'pendik'],
            'ümraniye': ['ataşehir', 'çamlıca', 'altunizade', 'üsküdar', 'maltepe', 'kozyatağı', 'acıbadem', 'kartal'],
            'altunizade': ['ataşehir', 'ümraniye', 'maltepe', 'üsküdar', 'çamlıca', 'kozyatağı', 'acıbadem', 'barbaros'],
            'moda': ['kadıköy', 'bağdat-caddesi', 'fikirtepe', 'kalamış', 'göztepe', 'erenköy', 'suadiye', 'caddebostan'],
            'bağdat-caddesi': ['kadıköy', 'moda', 'suadiye', 'caddebostan', 'göztepe', 'erenköy', 'kalamış', 'fikirtepe'],
            'kartal': ['maltepe', 'pendik', 'ataşehir', 'altunizade', 'üsküdar', 'ümraniye', 'çamlıca', 'kozyatağı'],
            'pendik': ['kartal', 'maltepe', 'altunizade', 'ataşehir', 'ümraniye', 'üsküdar', 'çamlıca', 'kozyatağı'],
            
            // EKSİK LOKASYONLARİN CROSS-LİNKİNG HARİTALARI
            'içerenköy': ['göztepe', 'erenköy', 'kadıköy', 'ataşehir', 'kozyatağı', 'caddebostan', 'suadiye', 'ümraniye'],
            'küçükbakkalköy': ['ataşehir', 'kozyatağı', 'altunizade', 'ümraniye', 'maltepe', 'üsküdar', 'barbaros', 'acıbadem'],
            'sahrayıcedit': ['kadıköy', 'üsküdar', 'acıbadem', 'kozyatağı', 'ataşehir', 'çamlıca', 'altunizade', 'göztepe']
        };
        
        const nearbyLocations = nearbyMap[currentLocation] || [];
        // Filter out the current location and return 8 nearby cards
        return this.allCards.filter(card => 
            nearbyLocations.includes(card.location) && 
            card.location !== currentLocation
        ).slice(0, 8);
    }
    
    renderCards(cards) {
        return cards.map(card => `
            <a href="${this.getCardHref(card)}" class="neighborhood-card">
                <div class="card-icon">${card.icon}</div>
                <h3>${card.title}</h3>
                <p>${card.desc}</p>
                <span class="service-arrow">→</span>
            </a>
        `).join('');
    }
    
    getCardHref(card) {
        if (!card.active) return '#';
        
        // Ana sayfadaysa relative path, alt sayfalardaysa '../' ekle
        const isMainPage = window.location.pathname === '/' || window.location.pathname.endsWith('index.html');
        return isMainPage ? card.href : '../' + card.href;
    }
    
    getOtherLocations() {
        const displayedLocations = this.getCardsToDisplay().map(card => card.location);
        const otherLocations = this.allCards
            .filter(card => !displayedLocations.includes(card.location))
            .map(card => this.capitalizeFirst(card.location))
            .slice(0, 6);
        
        return otherLocations.join(' • ');
    }
    
    capitalizeFirst(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
    
    attachEventListeners() {
        const comingSoonCards = document.querySelectorAll(`#${this.containerId} .coming-soon`);
        comingSoonCards.forEach(card => {
            card.addEventListener('click', function(e) {
                e.preventDefault();
                window.open('tel:+905433527474', '_self');
            });
        });
    }
    
    updateCards() {
        const grid = document.getElementById(`${this.containerId}-grid`);
        if (!grid) return;
        
        // Fade out effect
        grid.style.opacity = '0.5';
        
        setTimeout(() => {
            const cardsToDisplay = this.getCardsToDisplay();
            grid.innerHTML = this.renderCards(cardsToDisplay);
            
            // Update other locations info
            const infoElement = document.querySelector(`#${this.containerId} .neighborhoods-info p`);
            if (infoElement) {
                infoElement.textContent = `Hizmet verdiğimiz diğer elite bölgeler: ${this.getOtherLocations()}`;
            }
            
            // Fade in effect
            grid.style.opacity = '1';
            
            // Reattach event listeners
            this.attachEventListeners();
        }, 300);
    }
    
    rotateCards() {
        if (this.config.showOnlyNearby) return; // Don't rotate for nearby cards
        
        this.currentStartIndex = (this.currentStartIndex + 2) % this.allCards.length;
        this.updateCards();
    }
    
    startRotation() {
        if (!this.config.enableRotation || this.config.showOnlyNearby) return;
        
        // SEO-friendly rotation: Longer intervals for better indexing
        setInterval(() => {
            this.rotateCards();
        }, this.config.rotationInterval);
        
        // Pause rotation on user interaction for better UX
        const container = document.getElementById(this.containerId);
        if (container) {
            let rotationPaused = false;
            let resumeTimeout;
            
            container.addEventListener('mouseenter', () => {
                rotationPaused = true;
                clearTimeout(resumeTimeout);
            });
            
            container.addEventListener('mouseleave', () => {
                resumeTimeout = setTimeout(() => {
                    rotationPaused = false;
                }, 3000); // Resume after 3 seconds of no interaction
            });
            
            // Override original rotation to respect pause state
            const originalRotation = setInterval(() => {
                if (!rotationPaused) {
                    this.rotateCards();
                }
            }, this.config.rotationInterval);
        }
    }
    
    // Public method to refresh component
    refresh(newConfig = {}) {
        this.config = { ...this.config, ...newConfig };
        this.createComponent();
    }
}

// Auto-initialize components on page load
document.addEventListener('DOMContentLoaded', function() {
    // Main homepage component
    const mainComponent = document.getElementById('elite-neighborhoods-main');
    if (mainComponent) {
        new EliteNeighborhoodsComponent('elite-neighborhoods-main', {
            title: 'Elite Semtlerde Özel Hizmet',
            subtitle: 'İstanbul\'un en prestijli mahallelerinde 25 yıldır güvenilir hizmet sunuyoruz',
            cardsToShow: 9,
            enableRotation: true,
            rotationInterval: 25000 // SEO-friendly longer interval
        });
    }
    
    // Secondary components (for service pages)
    const secondaryComponent = document.getElementById('elite-neighborhoods-related');
    if (secondaryComponent) {
        // Extract current location from URL
        const currentPath = window.location.pathname;
        const locationMatch = currentPath.match(/bolgeler\/([^-]+)/);
        let currentLocation = locationMatch ? locationMatch[1] : null;
        
        // Convert English characters to Turkish for location mapping
        const locationMap = {
            'kadikoy': 'kadıköy',
            'uskudar': 'üsküdar',
            'umraniye': 'ümraniye', 
            'camlica': 'çamlıca',
            'kozyatagi': 'kozyatağı',
            'atasehir': 'ataşehir',
            'acibadem': 'acıbadem',
            'suadiye': 'suadiye',
            'kalamis': 'kalamış',
            'caddebostan': 'caddebostan',
            'erenkoy': 'erenköy',
            'goztepe': 'göztepe',
            'fenerbahce': 'fenerbahçe',
            'bostanci': 'bostancı',
            'barbaros': 'barbaros',
            'fikirtepe': 'fikirtepe',
            'maltepe': 'maltepe',
            'kartal': 'kartal',
            'pendik': 'pendik',
            'altunizade': 'altunizade',
            'icerenkoy': 'içerenköy',
            'kucukbakkalkoy': 'küçükbakkalköy',
            'sahrayicedit': 'sahrayıcedit',
            'moda': 'moda',
            'bagdat': 'bağdat-caddesi'
        };
        
        // Map English location to Turkish equivalent
        if (currentLocation && locationMap[currentLocation]) {
            currentLocation = locationMap[currentLocation];
        }
        
        new EliteNeighborhoodsComponent('elite-neighborhoods-related', {
            title: 'Yakın Bölgelerdeki Hizmetlerimiz',
            subtitle: 'Çevrenizde bulunan diğer elite semtlerde de hizmet veriyoruz',
            cardsToShow: 8,
            enableRotation: false,
            showOnlyNearby: true,
            currentLocation: currentLocation
        });
    }
});

// Export for manual initialization
window.EliteNeighborhoodsComponent = EliteNeighborhoodsComponent;