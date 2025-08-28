/**
 * Dynamic Related Services Component
 * MIT Architecture - Corporate Standard
 * Randomly displays 3 services excluding current page
 */

// All available services data
const allServices = [
    {
        id: 'kuru-temizleme',
        title: 'Kuru Temizleme',
        description: 'Kıyafetleriniz için profesyonel kuru temizleme hizmeti',
        image: 'dry-cleaning.webp',
        alt: 'Kuru Temizleme Hizmeti',
        url: 'kuru-temizleme.html'
    },
    {
        id: 'hali-yikama', 
        title: 'Halı Yıkama',
        description: 'Halılarınız için profesyonel yıkama ve temizlik hizmeti',
        image: 'carpet-cleaning.webp',
        alt: 'Halı Yıkama Hizmeti',
        url: 'hali-yikama.html'
    },
    {
        id: 'koltuk-yikama',
        title: 'Koltuk Yıkama', 
        description: 'Koltuk takımlarınız için özel temizlik çözümleri',
        image: 'furniture-cleaning.webp',
        alt: 'Koltuk Yıkama Hizmeti',
        url: 'koltuk-yikama.html'
    },
    {
        id: 'perde-temizleme',
        title: 'Perde Temizleme',
        description: 'Store, zebra ve tüm perde türleri için özel temizlik',
        image: 'curtain-blind-cleaning.webp', 
        alt: 'Perde Temizleme Hizmeti',
        url: 'perde-temizleme.html'
    },
    {
        id: 'utu-hizmetleri',
        title: 'Ütü Hizmetleri',
        description: 'Profesyonel ütü ve giysi bakım hizmetleri',
        image: 'ironing-service.webp',
        alt: 'Ütü Hizmetleri', 
        url: 'utu-hizmetleri.html'
    },
    {
        id: 'ev-tekstili-temizligi',
        title: 'Ev Tekstili Temizliği',
        description: 'Ev tekstilleri için özel temizlik hizmeti',
        image: 'home-textile-cleaning.webp',
        alt: 'Ev Tekstili Temizliği',
        url: 'ev-tekstili-temizligi.html'
    },
    {
        id: 'canta-temizleme',
        title: 'Çanta Temizleme',
        description: 'Deri ve kumaş çantalar için özel temizlik hizmeti',
        image: 'luggage-bag-cleaning.webp',
        alt: 'Çanta Temizleme',
        url: 'canta-temizleme.html'
    },
    {
        id: 'kumas-deri-boyama',
        title: 'Kumaş ve Deri Boyama',
        description: 'Solmuş kıyafetlere yeni hayat veren boyama hizmeti',
        image: 'fabric-leather-dyeing.webp',
        alt: 'Kumaş ve Deri Boyama',
        url: 'kumas-deri-boyama.html'
    },
    {
        id: 'lostra-hizmeti',
        title: 'Lostra Hizmeti',
        description: 'Ayakkabı ve çantalar için profesyonel parlatma hizmeti',
        image: 'shoe-polish-service.webp',
        alt: 'Lostra Hizmeti',
        url: 'lostra-hizmeti.html'
    }
];

/**
 * Get current service ID from page URL
 */
function getCurrentServiceId() {
    const currentPath = window.location.pathname;
    const fileName = currentPath.split('/').pop().replace('.html', '');
    return fileName;
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
 * Get 3 random services excluding current page
 */
function getRandomServices(currentServiceId) {
    const otherServices = allServices.filter(service => service.id !== currentServiceId);
    const shuffledServices = shuffleArray(otherServices);
    return shuffledServices.slice(0, 3);
}

/**
 * Generate HTML for a single service card
 */
function generateServiceCard(service) {
    return `
        <div class="related-service">
            <img src="../asset/${service.image}" alt="${service.alt}" width="80" height="80" loading="lazy" decoding="async">
            <h3>${service.title}</h3>
            <p>${service.description}</p>
            <a href="${service.url}" class="service-link">Detaylı Bilgi →</a>
        </div>
    `;
}

/**
 * Initialize dynamic related services
 */
function initDynamicRelatedServices() {
    const relatedServicesGrid = document.querySelector('.related-services-grid');
    
    if (!relatedServicesGrid) {
        console.warn('Related services grid not found');
        return;
    }

    const currentServiceId = getCurrentServiceId();
    const randomServices = getRandomServices(currentServiceId);
    
    // Generate HTML for all 3 random services
    const servicesHTML = randomServices.map(service => generateServiceCard(service)).join('');
    
    // Replace existing content
    relatedServicesGrid.innerHTML = servicesHTML;
}

/**
 * Initialize when DOM is ready
 */
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDynamicRelatedServices);
} else {
    initDynamicRelatedServices();
}

// Export for potential use in other components
window.DynamicRelatedServices = {
    init: initDynamicRelatedServices,
    getRandomServices,
    allServices
};