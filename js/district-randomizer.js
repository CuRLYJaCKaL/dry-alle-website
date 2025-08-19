/**
 * DryAlle District Cards Randomizer
 * MIT-Level JavaScript Architecture
 * Dynamic Content Variation System
 */

class DistrictRandomizer {
    constructor() {
        this.allDistricts = [
            {
                title: "Fenerbahçe Kuru Temizleme",
                description: "Sahil kesiminde özel kıyafet temizleme",
                link: "fenerbahce-kuru-temizleme.html"
            },
            {
                title: "Kozyatağı Kuru Temizleme", 
                description: "Modern iş bölgesinde premium hizmet",
                link: "kozyatagi-kuru-temizleme.html"
            },
            {
                title: "Acıbadem Kuru Temizleme",
                description: "Sağlık merkezi çevresinde kaliteli hizmet",
                link: "acibadem-kuru-temizleme.html"
            },
            {
                title: "Bağdat Caddesi Haute Couture",
                description: "Haute couture ve lüks giyim temizleme hizmeti",
                link: "bagdat-caddesi-haute-couture.html"
            },
            {
                title: "Kadıköy Luxury Kıyafet",
                description: "Merkezi konumda luxury kıyafet bakımı",
                link: "kadikoy-luxury-kiyafet.html"
            },
            {
                title: "Ataşehir Halı Yıkama",
                description: "İş bölgesinde halı temizlik hizmeti",
                link: "atasehir-hali-yikama.html"
            },
            {
                title: "Maltepe Halı Yıkama",
                description: "Sahil kesiminde halı temizlik hizmeti", 
                link: "maltepe-hali-yikama.html"
            },
            {
                title: "Moda Koltuk Yıkama",
                description: "Sanat mahallesinde mobilya temizliği",
                link: "moda-koltuk-yikama.html"
            },
            {
                title: "Suadiye Halı Yıkama",
                description: "Lüks semtte profesyonel halı temizleme",
                link: "suadiye-hali-yikama.html"
            },
            {
                title: "Erenkoy Halı Yıkama", 
                description: "Konut bölgesinde halı temizlik hizmeti",
                link: "erenkoy-hali-yikama.html"
            },
            {
                title: "Göztepe Halı Yıkama",
                description: "Aileviye mahallede halı bakım hizmeti", 
                link: "goztepe-hali-yikama.html"
            },
            {
                title: "Altunizade Halı Yıkama",
                description: "Designer halı yıkama ve bakım hizmeti",
                link: "altunizade-hali-yikama.html"
            },
            {
                title: "Bağdat Caddesi Koltuk Yıkama",
                description: "Prestij caddesinde mobilya temizliği",
                link: "bagdat-caddesi-koltuk-yikama.html"
            },
            {
                title: "Üsküdar Koltuk Yıkama",
                description: "Tarihi yarımadada mobilya bakımı",
                link: "uskudar-koltuk-yikama.html"
            },
            {
                title: "Çamlıca Kuru Temizleme",
                description: "Elite semtte VIP kıyafet bakımı",
                link: "camlica-kuru-temizleme.html"
            },
            {
                title: "Ataşehir Premium Temizlik",
                description: "İş merkezinde hızlı ve güvenilir hizmet",
                link: "atasehir-premium-temizlik.html"
            },
            {
                title: "Kadıköy Koltuk Yıkama",
                description: "Sanat mobilya temizleme hizmeti", 
                link: "kadikoy-koltuk-yikama.html"
            },
            {
                title: "Kartal Koltuk Yıkama",
                description: "Premium kalite mobilya temizleme",
                link: "kartal-koltuk-yikama.html"
            }
        ];
        
        this.currentPage = this.getCurrentPageUrl();
        this.init();
    }
    
    /**
     * Get current page URL to exclude from recommendations
     */
    getCurrentPageUrl() {
        const path = window.location.pathname;
        const filename = path.split('/').pop();
        return filename;
    }
    
    /**
     * Shuffle array using Fisher-Yates algorithm
     */
    shuffleArray(array) {
        const shuffled = [...array];
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        return shuffled;
    }
    
    /**
     * Get random 8 districts excluding current page
     */
    getRandomDistricts() {
        // Exclude current page from recommendations
        const availableDistricts = this.allDistricts.filter(
            district => district.link !== this.currentPage
        );
        
        // Shuffle and take first 8
        const shuffled = this.shuffleArray(availableDistricts);
        return shuffled.slice(0, 8);
    }
    
    /**
     * Create district card HTML
     */
    createDistrictCard(district) {
        return `
            <div class="district-card">
                <div class="district-content">
                    <h3>${district.title}</h3>
                    <p>${district.description}</p>
                    <a href="${district.link}" class="district-link">Hizmet Al ›</a>
                </div>
            </div>
        `;
    }
    
    /**
     * Render districts grid
     */
    renderDistricts() {
        const container = document.querySelector('.districts-grid');
        if (!container) return;
        
        const randomDistricts = this.getRandomDistricts();
        const districtsHTML = randomDistricts
            .map(district => this.createDistrictCard(district))
            .join('');
            
        container.innerHTML = districtsHTML;
        
        // Add animation class for smooth loading
        container.classList.add('districts-loaded');
    }
    
    /**
     * Initialize randomizer
     */
    init() {
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                this.renderDistricts();
            });
        } else {
            this.renderDistricts();
        }
    }
}

// Initialize when script loads
new DistrictRandomizer();