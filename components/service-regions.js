/**
 * Service Regions Component
 * MIT Architecture - Dynamic Region Display for Service Pages
 * Shows 8 relevant regions based on service type
 */

// All available regions data
const allRegions = [
    {
        id: 'kadikoy-kuru-temizleme',
        title: 'Kadıköy Kuru Temizleme',
        description: 'Sanat mahallesi premium hizmet',
        url: '../bolgeler/kadikoy-kuru-temizleme.html',
        serviceTypes: ['kuru-temizleme', 'ev-tekstili-temizligi', 'canta-temizleme']
    },
    {
        id: 'uskudar-luxury-kiyafet',
        title: 'Üsküdar Luxury Kıyafet',
        description: 'Historic premium luxury care',
        url: '../bolgeler/uskudar-luxury-kiyafet.html',
        serviceTypes: ['kuru-temizleme', 'kumas-deri-boyama', 'canta-temizleme']
    },
    {
        id: 'acibadem-kuru-temizleme',
        title: 'Acıbadem Kuru Temizleme',
        description: 'Sağlık merkezi çevresinde kaliteli hizmet',
        url: '../bolgeler/acibadem-kuru-temizleme.html',
        serviceTypes: ['kuru-temizleme', 'ev-tekstili-temizligi']
    },
    {
        id: 'atasehir-premium-temizlik',
        title: 'Ataşehir Premium Temizlik',
        description: 'Modern iş bölgesinde premium hizmet',
        url: '../bolgeler/atasehir-premium-temizlik.html',
        serviceTypes: ['kuru-temizleme', 'utu-hizmetleri']
    },
    {
        id: 'kozyatagi-kuru-temizleme',
        title: 'Kozyatağı Kuru Temizleme',
        description: 'Modern iş bölgesinde premium hizmet',
        url: '../bolgeler/kozyatagi-kuru-temizleme.html',
        serviceTypes: ['kuru-temizleme', 'utu-hizmetleri']
    },
    {
        id: 'suadiye-hali-yikama',
        title: 'Suadiye Halı Yıkama',
        description: 'Lüks semtte profesyonel halı temizleme',
        url: '../bolgeler/suadiye-hali-yikama.html',
        serviceTypes: ['hali-yikama', 'perde-temizleme']
    },
    {
        id: 'suadiye-koltuk-yikama',
        title: 'Suadiye Koltuk Yıkama',
        description: 'Lüks semtte mobilya temizleme',
        url: '../bolgeler/suadiye-koltuk-yikama.html',
        serviceTypes: ['koltuk-yikama', 'ev-tekstili-temizligi']
    },
    {
        id: 'bagdat-caddesi-haute-couture',
        title: 'Bağdat Caddesi Haute Couture',
        description: 'Haute couture ve lüks giyim temizleme hizmeti',
        url: '../bolgeler/bagdat-caddesi-haute-couture.html',
        serviceTypes: ['kuru-temizleme', 'kumas-deri-boyama']
    },
    {
        id: 'fenerbahce-kuru-temizleme',
        title: 'Fenerbahçe Kuru Temizleme',
        description: 'Sahil kesiminde profesyonel hizmet',
        url: '../bolgeler/fenerbahce-kuru-temizleme.html',
        serviceTypes: ['kuru-temizleme', 'utu-hizmetleri']
    },
    {
        id: 'moda-koltuk-yikama',
        title: 'Moda Koltuk Yıkama',
        description: 'Sanat mahallesi mobilya temizliği',
        url: '../bolgeler/moda-koltuk-yikama.html',
        serviceTypes: ['koltuk-yikama', 'ev-tekstili-temizligi']
    },
    {
        id: 'caddebostan-hali-yikama',
        title: 'Caddebostan Halı Yıkama',
        description: 'Sahil kesiminde halı temizlik hizmeti',
        url: '../bolgeler/caddebostan-hali-yikama.html',
        serviceTypes: ['hali-yikama', 'perde-temizleme']
    },
    {
        id: 'bostanci-koltuk-yikama',
        title: 'Bostancı Koltuk Yıkama',
        description: 'Merkezi konumda mobilya temizliği',
        url: '../bolgeler/bostanci-koltuk-yikama.html',
        serviceTypes: ['koltuk-yikama', 'ev-tekstili-temizligi']
    },
    {
        id: 'camlica-kuru-temizleme',
        title: 'Çamlıca Kuru Temizleme',
        description: 'Prestij bölgesinde kaliteli hizmet',
        url: '../bolgeler/camlica-kuru-temizleme.html',
        serviceTypes: ['kuru-temizleme', 'canta-temizleme']
    },
    {
        id: 'icerenkoy-hali-yikama',
        title: 'İçerenköy Halı Yıkama',
        description: 'İş merkezinde halı temizlik hizmeti',
        url: '../bolgeler/icerenkoy-hali-yikama.html',
        serviceTypes: ['hali-yikama', 'perde-temizleme']
    },
    {
        id: 'sahrayicedit-premium-bakim',
        title: 'Sahrayıcedit Premium Bakım',
        description: 'Merkez lokasyonda özel hizmet',
        url: '../bolgeler/sahrayicedit-premium-bakim.html',
        serviceTypes: ['kuru-temizleme', 'lostra-hizmeti', 'kumas-deri-boyama']
    }
];

/**
 * Get current service type from page URL
 */
function getCurrentServiceType() {
    const currentPath = window.location.pathname;
    const fileName = currentPath.split('/').pop().replace('.html', '');
    return fileName;
}

/**
 * Get regions relevant to current service
 */
function getRelevantRegions(currentService) {
    // Get regions that offer the current service
    const relevantRegions = allRegions.filter(region => 
        region.serviceTypes.includes(currentService)
    );
    
    // If we have enough relevant regions, use them
    if (relevantRegions.length >= 8) {
        return shuffleArray(relevantRegions).slice(0, 8);
    }
    
    // Otherwise, mix relevant regions with general regions
    const otherRegions = allRegions.filter(region => 
        !region.serviceTypes.includes(currentService)
    );
    
    const mixed = [
        ...relevantRegions,
        ...shuffleArray(otherRegions).slice(0, 8 - relevantRegions.length)
    ];
    
    return shuffleArray(mixed);
}

/**
 * Shuffle array using Fisher-Yates algorithm
 */
function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

/**
 * Generate HTML for a single region card
 */
function generateRegionCard(region) {
    return `
        <div class="district-card">
            <div class="district-content">
                <h3 class="district-title">${region.title}</h3>
                <p class="district-description">${region.description}</p>
                <a href="${region.url}" class="district-link">Hizmet Al ›</a>
            </div>
        </div>
    `;
}

/**
 * Generate service regions section HTML
 */
function generateServiceRegionsSection(currentService) {
    const relevantRegions = getRelevantRegions(currentService);
    const regionsHTML = relevantRegions.map(region => generateRegionCard(region)).join('');
    
    return `
        <section class="premium-districts service-regions">
            <div class="premium-districts-container">
                <h2 class="districts-title">Hizmet Bölgelerimiz</h2>
                <p class="districts-subtitle">Anadolu Yakası'nın premium semtlerinde kaliteli kuru temizleme hizmetleri</p>
                <div class="districts-grid">
                    ${regionsHTML}
                </div>
            </div>
        </section>
    `;
}

/**
 * Initialize service regions display
 */
function initServiceRegions() {
    const currentService = getCurrentServiceType();
    const relatedServicesSection = document.querySelector('.related-services');
    
    if (!relatedServicesSection) {
        console.warn('Related services section not found');
        return;
    }
    
    // Generate and insert service regions section
    const serviceRegionsHTML = generateServiceRegionsSection(currentService);
    relatedServicesSection.insertAdjacentHTML('afterend', serviceRegionsHTML);
    
    // Add loaded class for animation
    setTimeout(() => {
        const regionsGrid = document.querySelector('.service-regions .districts-grid');
        if (regionsGrid) {
            regionsGrid.classList.add('districts-loaded');
        }
    }, 100);
}

/**
 * Initialize when DOM is ready
 */
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initServiceRegions);
} else {
    initServiceRegions();
}

// Export for potential use in other components
window.ServiceRegions = {
    init: initServiceRegions,
    getRelevantRegions,
    allRegions,
    generateServiceRegionsSection
};