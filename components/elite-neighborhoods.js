/**
 * Elite Neighborhoods Component
 * MIT Architecture - Premium Regional Display
 * Shows premium neighboring areas for cross-selling
 */

// Elite neighborhoods data
const eliteNeighborhoods = [
    {
        id: 'suadiye-hali-yikama',
        title: 'Suadiye Halı Yıkama',
        description: 'Lüks semtte profesyonel halı temizleme',
        url: 'suadiye-hali-yikama.html',
        serviceType: 'hali-yikama',
        district: 'Kadıköy',
        premium: true
    },
    {
        id: 'caddebostan-hali-yikama', 
        title: 'Caddebostan Halı Yıkama',
        description: 'Sahil kesiminde halı temizlik hizmeti',
        url: 'caddebostan-hali-yikama.html',
        serviceType: 'hali-yikama',
        district: 'Kadıköy',
        premium: true
    },
    {
        id: 'uskudar-luxury-kiyafet',
        title: 'Üsküdar Luxury Kıyafet',
        description: 'Tarihi semtte premium kıyafet bakımı',
        url: 'uskudar-luxury-kiyafet.html', 
        serviceType: 'kuru-temizleme',
        district: 'Üsküdar',
        premium: true
    },
    {
        id: 'kadikoy-luxury-kiyafet',
        title: 'Kadıköy Luxury Kıyafet',
        description: 'Sanat mahallesinde premium kıyafet hizmeti',
        url: 'kadikoy-luxury-kiyafet.html',
        serviceType: 'kuru-temizleme', 
        district: 'Kadıköy',
        premium: true
    },
    {
        id: 'bagdat-caddesi-haute-couture',
        title: 'Bağdat Caddesi Haute Couture',
        description: 'Premium alışveriş caddesinde haute couture bakımı',
        url: 'bagdat-caddesi-haute-couture.html',
        serviceType: 'kuru-temizleme',
        district: 'Kadıköy', 
        premium: true
    },
    {
        id: 'atasehir-premium-temizlik',
        title: 'Ataşehir Premium Temizlik',
        description: 'Modern iş bölgesinde premium hizmet',
        url: 'atasehir-premium-temizlik.html',
        serviceType: 'kuru-temizleme',
        district: 'Ataşehir',
        premium: true
    }
];

// Get current page to exclude from recommendations
function getCurrentPageId() {
    const path = window.location.pathname;
    const filename = path.split('/').pop().replace('.html', '');
    return filename;
}

// Shuffle array using Fisher-Yates algorithm
function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

// Get related elite neighborhoods (exclude current page)
function getRelatedEliteNeighborhoods(currentPageId, limit = 4) {
    const filtered = eliteNeighborhoods.filter(neighborhood => 
        neighborhood.id !== currentPageId
    );
    const shuffled = shuffleArray(filtered);
    return shuffled.slice(0, limit);
}

// Render elite neighborhoods section
function renderEliteNeighborhoods() {
    const container = document.querySelector('#elite-neighborhoods-related');
    if (!container) return;

    const currentPageId = getCurrentPageId();
    const neighborhoods = getRelatedEliteNeighborhoods(currentPageId, 4);

    if (neighborhoods.length === 0) return;

    const html = `
        <section class="elite-neighborhoods-section">
            <div class="container">
                <h2 class="section-title">Premium Bölgelerdeki Hizmetlerimiz</h2>
                <p class="section-subtitle">Yakın çevredeki prestijli semtlerde de kaliteli hizmet sunuyoruz</p>
                
                <div class="elite-neighborhoods-grid">
                    ${neighborhoods.map(neighborhood => `
                        <div class="elite-neighborhood-card">
                            <div class="card-content">
                                <h3>${neighborhood.title}</h3>
                                <p>${neighborhood.description}</p>
                                <div class="card-meta">
                                    <span class="district-badge">${neighborhood.district}</span>
                                    ${neighborhood.premium ? '<span class="premium-badge">Premium</span>' : ''}
                                </div>
                                <a href="${neighborhood.url}" class="neighborhood-link">
                                    Hizmet Al ›
                                </a>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        </section>
    `;

    container.innerHTML = html;

    // GTM tracking for elite neighborhood clicks
    container.addEventListener('click', function(e) {
        if (e.target.matches('.neighborhood-link')) {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'elite_neighborhood_click', {
                    'event_category': 'Regional Navigation',
                    'event_label': e.target.closest('.elite-neighborhood-card').querySelector('h3').textContent,
                    'value': 1
                });
            }
        }
    });
}

// WhatsApp integration
function openWhatsApp() {
    const phone = "905433527474";
    const pageTitle = document.title || "Dry Alle Hizmet";
    const message = encodeURIComponent(`Merhaba, ${pageTitle} hakkında bilgi almak istiyorum.`);
    window.open(`https://wa.me/${phone}?text=${message}`, '_blank');
    
    // GTM tracking
    if (typeof gtag !== 'undefined') {
        gtag('event', 'whatsapp_click', {
            'event_category': 'Contact',
            'event_label': pageTitle,
            'value': 1
        });
    }
}

// Initialize all elite neighborhood functionality
function initEliteNeighborhoods() {
    renderEliteNeighborhoods();
    
    // Add intersection observer for performance tracking
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && typeof gtag !== 'undefined') {
                    gtag('event', 'elite_neighborhoods_viewed', {
                        'event_category': 'Content Engagement',
                        'event_label': 'Elite Neighborhoods Section'
                    });
                    observer.unobserve(entry.target);
                }
            });
        });
        
        const section = document.querySelector('.elite-neighborhoods-section');
        if (section) {
            observer.observe(section);
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', initEliteNeighborhoods);

// Initialize if DOM already loaded
if (document.readyState !== 'loading') {
    initEliteNeighborhoods();
}