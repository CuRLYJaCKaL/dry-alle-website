// Service Elite Neighborhoods Component - Cross-linking for Service Pages
class ServiceEliteNeighborhoodsComponent {
    constructor(containerId, config = {}) {
        this.containerId = containerId;
        this.config = {
            title: config.title || 'Hizmet Verdiğimiz Bölgeler',
            subtitle: config.subtitle || 'İstanbul\'un elit semtlerinde özel hizmet alanlarımız',
            cardsToShow: config.cardsToShow || 8,
            currentService: config.currentService || 'kuru-temizleme',
            ...config
        };
        
        // Service-specific mappings
        this.serviceMapping = {
            'kuru-temizleme': {
                pages: [
                    { href: '../bolgeler/acibadem-kuru-temizleme.html', icon: '🎩', title: 'Acıbadem Kuru Temizleme', desc: 'Premium takım elbise bakımı' },
                    { href: '../bolgeler/fenerbahce-kuru-temizleme.html', icon: '🏆', title: 'Fenerbahçe Kuru Temizleme', desc: 'Elite kıyafet bakımı' },
                    { href: '../bolgeler/camlica-kuru-temizleme.html', icon: '👔', title: 'Çamlıca VIP Kuru Temizleme', desc: 'Elite kıyafet bakımı' },
                    { href: '../bolgeler/kozyatagi-kuru-temizleme.html', icon: '💼', title: 'Kozyatağı İş Kıyafetleri', desc: 'Profesyoneller için hızlı servis' },
                    { href: '../bolgeler/kadikoy-kuru-temizleme.html', icon: '🌟', title: 'Kadıköy Merkez Kuru Temizleme', desc: 'Premium bakım merkezi' },
                    { href: '../bolgeler/atasehir-premium-temizlik.html', icon: '💎', title: 'Ataşehir Premium Temizlik', desc: 'VIP kıyafet bakımı' },
                    { href: '../bolgeler/sahrayicedit-premium-bakim.html', icon: '🏛️', title: 'Sahrayıcedit Premium Bakım', desc: 'Elite mahalle özel hizmet' },
                    { href: '../bolgeler/altunizade-premium-temizlik.html', icon: '✨', title: 'Altunizade Premium Temizlik', desc: 'Lüks kıyafet bakımı' }
                ]
            },
            'koltuk-yikama': {
                pages: [
                    { href: '../bolgeler/kadikoy-koltuk-yikama.html', icon: '🛋️', title: 'Kadıköy Koltuk Yıkama', desc: 'Profesyonel koltuk temizliği' },
                    { href: '../bolgeler/atasehir-hali-yikama.html', icon: '🏠', title: 'Ataşehir Halı Yıkama', desc: 'Premium ev tekstili bakımı' },
                    { href: '../bolgeler/fenerbahce-kuru-temizleme.html', icon: '🏆', title: 'Fenerbahçe Elite Temizlik', desc: 'Lüks ev bakım hizmetleri' },
                    { href: '../bolgeler/kozyatagi-kuru-temizleme.html', icon: '💺', title: 'Kozyatağı Mobilya Bakımı', desc: 'Özel koltuk temizlik hizmeti' },
                    { href: '../bolgeler/barbaros-koltuk-yikama.html', icon: '🌟', title: 'Barbaros Koltuk Yıkama', desc: 'Elite mahalle özel hizmet' },
                    { href: '../bolgeler/bostanci-koltuk-yikama.html', icon: '🏖️', title: 'Bostancı Koltuk Yıkama', desc: 'Sahil bölgesi premium hizmet' },
                    { href: '../bolgeler/moda-koltuk-yikama.html', icon: '👑', title: 'Moda Koltuk Yıkama', desc: 'Prestijli bölge özel bakım' },
                    { href: '../bolgeler/kalamis-koltuk-yikama.html', icon: '⭐', title: 'Kalamış Koltuk Yıkama', desc: 'Marina bölgesi lüks hizmet' }
                ]
            },
            'hali-yikama': {
                pages: [
                    { href: '../bolgeler/atasehir-hali-yikama.html', icon: '🏠', title: 'Ataşehir Halı Yıkama', desc: 'Premium halı temizlik merkezi' },
                    { href: '../bolgeler/suadiye-hali-yikama.html', icon: '🌊', title: 'Suadiye Halı Yıkama', desc: 'Sahil bölgesi özel hizmet' },
                    { href: '../bolgeler/caddebostan-hali-yikama.html', icon: '🏖️', title: 'Caddebostan Halı Yıkama', desc: 'Marina çevresi lüks bakım' },
                    { href: '../bolgeler/erenkoy-hali-yikama.html', icon: '🌸', title: 'Erenköy Halı Yıkama', desc: 'Prestijli mahalle hizmeti' },
                    { href: '../bolgeler/goztepe-hali-yikama.html', icon: '👁️', title: 'Göztepe Halı Yıkama', desc: 'Elite bölge özel temizlik' },
                    { href: '../bolgeler/maltepe-hali-yikama.html', icon: '🏛️', title: 'Maltepe Halı Yıkama', desc: 'Premium halı bakım merkezi' },
                    { href: '../bolgeler/uskudar-hali-yikama.html', icon: '🕌', title: 'Üsküdar Halı Yıkama', desc: 'Tarihi bölge özel hizmet' },
                    { href: '../bolgeler/umraniye-hali-yikama.html', icon: '🌿', title: 'Ümraniye Halı Yıkama', desc: 'Modern yaşam alanı bakımı' }
                ]
            },
            'canta-temizleme': {
                pages: [
                    { href: '../bolgeler/bagdat-caddesi-haute-couture.html', icon: '👜', title: 'Bağdat Caddesi Haute Couture', desc: 'Lüks çanta bakım atölyesi' },
                    { href: '../bolgeler/kadikoy-luxury-kiyafet.html', icon: '💎', title: 'Kadıköy Luxury Kıyafet', desc: 'Designer çanta uzmanı' },
                    { href: '../bolgeler/atasehir-premium-temizlik.html', icon: '✨', title: 'Ataşehir Premium Çanta Bakımı', desc: 'VIP çanta restaurasyon' },
                    { href: '../bolgeler/fenerbahce-kuru-temizleme.html', icon: '🏆', title: 'Fenerbahçe Elite Çanta Servisi', desc: 'Lüks çanta temizlik hizmeti' },
                    { href: '../bolgeler/uskudar-luxury-kiyafet.html', icon: '🌟', title: 'Üsküdar Luxury Çanta', desc: 'Premium deri bakım merkezi' },
                    { href: '../bolgeler/kozyatagi-kuru-temizleme.html', icon: '💼', title: 'Kozyatağı Çanta Atölyesi', desc: 'İş çantası uzman bakımı' },
                    { href: '../bolgeler/sahrayicedit-premium-bakim.html', icon: '🏛️', title: 'Sahrayıcedit Çanta Bakımı', desc: 'Elite çanta restaurasyon' },
                    { href: '../bolgeler/altunizade-premium-temizlik.html', icon: '👑', title: 'Altunizade Lüks Çanta', desc: 'Designer çanta servisi' }
                ]
            },
            'ev-tekstili-temizligi': {
                pages: [
                    { href: '../bolgeler/atasehir-hali-yikama.html', icon: '🏠', title: 'Ataşehir Ev Tekstili', desc: 'Premium ev tekstili merkezi' },
                    { href: '../bolgeler/kadikoy-luxury-kiyafet.html', icon: '🌟', title: 'Kadıköy Elite Tekstil', desc: 'Lüks ev kumaşları bakımı' },
                    { href: '../bolgeler/fenerbahce-kuru-temizleme.html', icon: '🏆', title: 'Fenerbahçe Ev Tekstili', desc: 'Premium ev kumaşı hizmeti' },
                    { href: '../bolgeler/suadiye-hali-yikama.html', icon: '🌊', title: 'Suadiye Tekstil Bakımı', desc: 'Sahil bölgesi özel hizmet' },
                    { href: '../bolgeler/uskudar-luxury-kiyafet.html', icon: '🕌', title: 'Üsküdar Ev Tekstili', desc: 'Tarihi bölge premium bakım' },
                    { href: '../bolgeler/kozyatagi-kuru-temizleme.html', icon: '🏢', title: 'Kozyatağı Tekstil Merkezi', desc: 'Modern ev tekstili bakımı' },
                    { href: '../bolgeler/caddebostan-hali-yikama.html', icon: '🏖️', title: 'Caddebostan Ev Tekstili', desc: 'Marina çevresi lüks hizmet' },
                    { href: '../bolgeler/erenkoy-hali-yikama.html', icon: '🌸', title: 'Erenköy Tekstil Atölyesi', desc: 'Prestijli mahalle hizmeti' }
                ]
            },
            'kumas-deri-boyama': {
                pages: [
                    { href: '../bolgeler/kadikoy-luxury-kiyafet.html', icon: '🎨', title: 'Kadıköy Kumaş Boyama', desc: 'Master boyama atölyesi' },
                    { href: '../bolgeler/bagdat-caddesi-haute-couture.html', icon: '👗', title: 'Bağdat Caddesi Boyama', desc: 'Haute couture renk uzmanı' },
                    { href: '../bolgeler/atasehir-premium-temizlik.html', icon: '✨', title: 'Ataşehir Deri Boyama', desc: 'Premium deri renklendirme' },
                    { href: '../bolgeler/fenerbahce-kuru-temizleme.html', icon: '🏆', title: 'Fenerbahçe Kumaş Atölyesi', desc: 'Elite kumaş boyama merkezi' },
                    { href: '../bolgeler/uskudar-luxury-kiyafet.html', icon: '🌈', title: 'Üsküdar Renk Atölyesi', desc: 'Geleneksel boyama teknikleri' },
                    { href: '../bolgeler/kozyatagi-kuru-temizleme.html', icon: '🖌️', title: 'Kozyatağı Boyama Merkezi', desc: 'Modern kumaş boyama hizmeti' },
                    { href: '../bolgeler/sahrayicedit-premium-bakim.html', icon: '🎭', title: 'Sahrayıcedit Deri Atölyesi', desc: 'Elite deri boyama hizmeti' },
                    { href: '../bolgeler/altunizade-premium-temizlik.html', icon: '🌟', title: 'Altunizade Kumaş Boyama', desc: 'Lüks kumaş renklendirme' }
                ]
            },
            'lostra-hizmeti': {
                pages: [
                    { href: '../bolgeler/kadikoy-luxury-kiyafet.html', icon: '👞', title: 'Kadıköy Ayakkabı Bakımı', desc: 'Master ayakkabı ustası' },
                    { href: '../bolgeler/bagdat-caddesi-haute-couture.html', icon: '👠', title: 'Bağdat Caddesi Lostra', desc: 'Lüks ayakkabı bakım merkezi' },
                    { href: '../bolgeler/atasehir-premium-temizlik.html', icon: '✨', title: 'Ataşehir Ayakkabı Servisi', desc: 'Premium lostra hizmeti' },
                    { href: '../bolgeler/fenerbahce-kuru-temizleme.html', icon: '🏆', title: 'Fenerbahçe Lostra', desc: 'Elite ayakkabı bakım atölyesi' },
                    { href: '../bolgeler/uskudar-luxury-kiyafet.html', icon: '🕌', title: 'Üsküdar Ayakkabı Ustası', desc: 'Geleneksel lostra sanatı' },
                    { href: '../bolgeler/kozyatagi-kuru-temizleme.html', icon: '💼', title: 'Kozyatağı İş Ayakkabısı', desc: 'Profesyonel ayakkabı bakımı' },
                    { href: '../bolgeler/sahrayicedit-premium-bakim.html', icon: '🏛️', title: 'Sahrayıcedit Lostra', desc: 'Elite ayakkabı hizmeti' },
                    { href: '../bolgeler/altunizade-premium-temizlik.html', icon: '👑', title: 'Altunizade Ayakkabı', desc: 'Lüks ayakkabı bakım merkezi' }
                ]
            },
            'perde-temizleme': {
                pages: [
                    { href: '../bolgeler/atasehir-hali-yikama.html', icon: '🏠', title: 'Ataşehir Perde Temizliği', desc: 'Premium perde bakım merkezi' },
                    { href: '../bolgeler/kadikoy-luxury-kiyafet.html', icon: '🌟', title: 'Kadıköy Elite Perde', desc: 'Lüks perde temizlik hizmeti' },
                    { href: '../bolgeler/fenerbahce-kuru-temizleme.html', icon: '🏆', title: 'Fenerbahçe Perde Servisi', desc: 'Elite perde bakım atölyesi' },
                    { href: '../bolgeler/suadiye-hali-yikama.html', icon: '🌊', title: 'Suadiye Perde Bakımı', desc: 'Sahil bölgesi özel hizmet' },
                    { href: '../bolgeler/uskudar-luxury-kiyafet.html', icon: '🕌', title: 'Üsküdar Perde Atölyesi', desc: 'Geleneksel perde bakımı' },
                    { href: '../bolgeler/kozyatagi-kuru-temizleme.html', icon: '🏢', title: 'Kozyatağı Perde Merkezi', desc: 'Modern perde temizlik hizmeti' },
                    { href: '../bolgeler/caddebostan-hali-yikama.html', icon: '🏖️', title: 'Caddebostan Perde', desc: 'Marina çevresi premium hizmet' },
                    { href: '../bolgeler/erenkoy-hali-yikama.html', icon: '🌸', title: 'Erenköy Perde Bakımı', desc: 'Prestijli mahalle hizmeti' }
                ]
            },
            'utu-hizmetleri': {
                pages: [
                    { href: '../bolgeler/kadikoy-luxury-kiyafet.html', icon: '👔', title: 'Kadıköy Ütü Hizmeti', desc: 'Master ütü ustası hizmeti' },
                    { href: '../bolgeler/atasehir-premium-temizlik.html', icon: '✨', title: 'Ataşehir Ütü Servisi', desc: 'Premium ütü merkezi' },
                    { href: '../bolgeler/fenerbahce-kuru-temizleme.html', icon: '🏆', title: 'Fenerbahçe Ütü Atölyesi', desc: 'Elite ütü hizmet merkezi' },
                    { href: '../bolgeler/kozyatagi-kuru-temizleme.html', icon: '💼', title: 'Kozyatağı İş Ütüsü', desc: 'Profesyonel ütü hizmeti' },
                    { href: '../bolgeler/uskudar-luxury-kiyafet.html', icon: '🌟', title: 'Üsküdar Ütü Ustası', desc: 'Geleneksel ütü sanatı' },
                    { href: '../bolgeler/bagdat-caddesi-haute-couture.html', icon: '👗', title: 'Bağdat Caddesi Ütü', desc: 'Haute couture ütü hizmeti' },
                    { href: '../bolgeler/sahrayicedit-premium-bakim.html', icon: '🏛️', title: 'Sahrayıcedit Ütü', desc: 'Elite mahalle ütü servisi' },
                    { href: '../bolgeler/altunizade-premium-temizlik.html', icon: '👑', title: 'Altunizade Ütü Merkezi', desc: 'Lüks ütü hizmet atölyesi' }
                ]
            }
        };
        
        this.init();
    }

    init() {
        this.render();
    }

    getCurrentServiceCards() {
        const service = this.config.currentService;
        return this.serviceMapping[service]?.pages || this.serviceMapping['kuru-temizleme'].pages;
    }

    render() {
        const container = document.getElementById(this.containerId);
        if (!container) {
            console.warn(`Service Elite Neighborhoods container ${this.containerId} not found`);
            return;
        }

        const cards = this.getCurrentServiceCards().slice(0, this.config.cardsToShow);
        
        const html = `
            <section class="elite-neighborhoods">
                <div class="container">
                    <h2>${this.config.title}</h2>
                    <p>${this.config.subtitle}</p>
                    <div class="neighborhoods-scroll-container">
                        <div class="neighborhoods-grid">
                            ${cards.map(card => this.renderCard(card)).join('')}
                        </div>
                    </div>
                </div>
            </section>
        `;
        
        container.innerHTML = html;
        console.log(`Service Elite Neighborhoods loaded for ${this.config.currentService}`);
    }

    renderCard(card) {
        return `
            <a href="${card.href}" class="neighborhood-card">
                <div class="card-icon">${card.icon}</div>
                <h3>${card.title}</h3>
                <p>${card.desc}</p>
                <span class="service-arrow">→</span>
            </a>
        `;
    }
}

// Auto-initialization for service pages
document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('service-elite-neighborhoods');
    if (container) {
        // Detect current service from page URL or title
        const currentPath = window.location.pathname;
        let currentService = 'kuru-temizleme'; // default
        
        if (currentPath.includes('koltuk-yikama')) currentService = 'koltuk-yikama';
        else if (currentPath.includes('hali-yikama')) currentService = 'hali-yikama';
        else if (currentPath.includes('canta-temizleme')) currentService = 'canta-temizleme';
        else if (currentPath.includes('ev-tekstili')) currentService = 'ev-tekstili-temizligi';
        else if (currentPath.includes('kumas-deri-boyama')) currentService = 'kumas-deri-boyama';
        else if (currentPath.includes('lostra-hizmeti')) currentService = 'lostra-hizmeti';
        else if (currentPath.includes('perde-temizleme')) currentService = 'perde-temizleme';
        else if (currentPath.includes('utu-hizmetleri')) currentService = 'utu-hizmetleri';
        else if (currentPath.includes('kuru-temizleme')) currentService = 'kuru-temizleme';
        
        new ServiceEliteNeighborhoodsComponent('service-elite-neighborhoods', {
            currentService: currentService,
            cardsToShow: 8
        });
    }
});

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ServiceEliteNeighborhoodsComponent;
}