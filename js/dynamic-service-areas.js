/**
 * DryAlle Dynamic Service Areas System
 * MIT-Level JavaScript Architecture
 * Smart Dynamic Content Loading & Display
 */

class DynamicServiceAreas {
    constructor() {
        this.database = null;
        this.currentPageCategory = this.detectPageCategory();
        this.loadDatabase();
    }

    /**
     * Detect current page category from URL
     */
    detectPageCategory() {
        const url = window.location.pathname;
        
        // Category detection patterns
        const patterns = {
            'kuru-temizleme': /kuru-temizleme|haute-couture|luxury-kiyafet|premium-temizlik/i,
            'hali-yikama': /hali-yikama/i,
            'koltuk-yikama': /koltuk-yikama/i,
            'premium': /premium|luxury|haute-couture/i
        };

        // Check each pattern
        for (const [category, pattern] of Object.entries(patterns)) {
            if (pattern.test(url)) {
                return category;
            }
        }

        // Default fallback
        return 'kuru-temizleme';
    }

    /**
     * Load service areas database
     */
    async loadDatabase() {
        try {
            const response = await fetch('/data/service-areas-database.json');
            this.database = await response.json();
            this.initializeServiceAreas();
        } catch (error) {
            console.error('Service areas database loading failed:', error);
            this.fallbackInitialization();
        }
    }

    /**
     * Initialize service areas display
     */
    initializeServiceAreas() {
        const containers = document.querySelectorAll('.service-areas-container');
        
        if (containers.length === 0) {
            return;
        }

        containers.forEach(container => {
            if (container.children.length === 0) {
                this.renderServiceAreas(container);
            }
        });
    }

    /**
     * Generate dynamic related areas based on current page
     */
    generateRelatedAreas() {
        if (!this.database) return [];

        const currentCategory = this.currentPageCategory;
        const currentUrl = window.location.pathname;
        const allAreas = this.database.serviceAreas;
        const rules = this.database.dynamicMapping.rules;
        const relations = this.database.dynamicMapping.categoryRelations;

        let relatedAreas = [];

        // Get same category areas (excluding current page)
        const sameCategory = allAreas[currentCategory] || [];
        const sameCategoryFiltered = sameCategory.filter(area => 
            !currentUrl.includes(area.id)
        );

        // Add same category areas (70%)
        const sameCategoryCount = Math.min(
            rules.sameCategory.maxItems, 
            sameCategoryFiltered.length
        );
        
        relatedAreas.push(...this.shuffleArray(sameCategoryFiltered)
            .slice(0, sameCategoryCount));

        // Add related category areas (30%)
        const relatedCategories = relations[currentCategory] || [];
        const remainingSlots = 8 - relatedAreas.length;

        if (remainingSlots > 0 && relatedCategories.length > 0) {
            let relatedCategoryAreas = [];
            
            relatedCategories.forEach(category => {
                const categoryAreas = allAreas[category] || [];
                relatedCategoryAreas.push(...categoryAreas);
            });

            const relatedCount = Math.min(
                rules.relatedCategory.maxItems,
                remainingSlots,
                relatedCategoryAreas.length
            );

            relatedAreas.push(...this.shuffleArray(relatedCategoryAreas)
                .slice(0, relatedCount));
        }

        return relatedAreas.slice(0, 8); // Max 8 areas for 2x4 grid
    }

    /**
     * Shuffle array for randomization
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
     * Render service areas HTML
     */
    renderServiceAreas(container) {
        const relatedAreas = this.generateRelatedAreas();
        
        if (relatedAreas.length === 0) {
            return;
        }

        const categoryNames = {
            'kuru-temizleme': 'Kuru Temizleme',
            'hali-yikama': 'Halı Yıkama',
            'koltuk-yikama': 'Koltuk Yıkama',
            'premium': 'Premium Hizmetler'
        };

        const currentCategoryName = categoryNames[this.currentPageCategory] || 'Premium Hizmetler';

        const html = `
            <section class="service-areas-section">
                <div class="service-areas-header">
                    <h2 class="service-areas-title">İlgili ${currentCategoryName} Bölgeleri</h2>
                    <p class="service-areas-subtitle">Çevre bölgelerdeki profesyonel hizmet noktalarımız</p>
                </div>
                
                <div class="related-areas-grid">
                    ${relatedAreas.map(area => this.renderAreaCard(area)).join('')}
                </div>
            </section>
        `;

        container.innerHTML = html;

        // Add loading animation
        this.addLoadingAnimation(container);
    }

    /**
     * Render individual area card
     */
    renderAreaCard(area) {
        return `
            <article class="area-card" data-category="${area.category}">
                <div class="area-card-content">
                    <div class="area-service-badge">${area.badge}</div>
                    <h3 class="area-card-title">${area.title}</h3>
                    <p class="area-card-description">${area.description}</p>
                    <a href="${area.url}" class="area-link">
                        <span>Hizmet Al ›</span>
                    </a>
                </div>
            </article>
        `;
    }

    /**
     * Add loading animation to cards
     */
    addLoadingAnimation(container) {
        const cards = container.querySelectorAll('.area-card');
        
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';
            card.style.animation = `fadeInUp 0.6s ease forwards`;
            card.style.animationDelay = `${0.1 + (index * 0.1)}s`;
        });
    }

    /**
     * Fallback initialization if database fails to load
     */
    fallbackInitialization() {
        const containers = document.querySelectorAll('.service-areas-container');
        
        containers.forEach(container => {
            if (container.children.length === 0) {
                const fallbackHTML = `
                    <section class="service-areas-section">
                        <div class="service-areas-header">
                            <h2 class="service-areas-title">İstanbul'da Hizmet Bölgelerimiz</h2>
                            <p class="service-areas-subtitle">Anadolu Yakası'nın tüm semtlerinde profesyonel hizmet</p>
                        </div>
                        <div class="related-areas-grid">
                            ${this.getFallbackAreas().map(area => this.renderAreaCard(area)).join('')}
                        </div>
                    </section>
                `;
                container.innerHTML = fallbackHTML;
            }
        });
    }

    /**
     * Get fallback areas data
     */
    getFallbackAreas() {
        return [
            {
                title: "Bağdat Caddesi Kuru Temizleme",
                description: "Lüks giyim temizleme hizmeti",
                url: "/bolgeler/bagdat-caddesi-haute-couture.html",
                category: "premium",
                badge: "Premium"
            },
            {
                title: "Kadıköy Kuru Temizleme", 
                description: "Merkezi konumda profesyonel hizmet",
                url: "/bolgeler/kadikoy-luxury-kiyafet.html",
                category: "kuru-temizleme",
                badge: "Merkezi"
            },
            {
                title: "Caddebostan Halı Yıkama",
                description: "Premium halı temizleme",
                url: "/bolgeler/caddebostan-hali-yikama.html", 
                category: "hali-yikama",
                badge: "Premium"
            },
            {
                title: "Üsküdar Koltuk Yıkama",
                description: "Mobilya bakım uzmanı",
                url: "/bolgeler/uskudar-koltuk-yikama.html",
                category: "koltuk-yikama", 
                badge: "Uzman"
            }
        ];
    }

    /**
     * Update areas dynamically (for future use)
     */
    updateAreas(newCategory) {
        this.currentPageCategory = newCategory;
        this.initializeServiceAreas();
    }

    /**
     * Get analytics data
     */
    getAnalytics() {
        return {
            currentCategory: this.currentPageCategory,
            loadedAreas: document.querySelectorAll('.area-card').length,
            databaseLoaded: !!this.database,
            timestamp: new Date().toISOString()
        };
    }
}

/**
 * CSS Animation Keyframes (injected if not exists)
 */
function injectAnimationCSS() {
    const existingStyle = document.getElementById('dynamic-areas-animations');
    
    if (!existingStyle) {
        const style = document.createElement('style');
        style.id = 'dynamic-areas-animations';
        style.textContent = `
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .area-card {
                will-change: transform, opacity;
            }
        `;
        document.head.appendChild(style);
    }
}

/**
 * Initialize on DOM load
 */
document.addEventListener('DOMContentLoaded', () => {
    injectAnimationCSS();
    
    // Initialize service areas system
    window.dynamicServiceAreas = new DynamicServiceAreas();
    
    // Optional: Analytics tracking
    if (typeof gtag !== 'undefined') {
        const analytics = window.dynamicServiceAreas.getAnalytics();
        gtag('event', 'dynamic_areas_loaded', {
            category: analytics.currentCategory,
            areas_count: analytics.loadedAreas
        });
    }
});

/**
 * Export for module systems
 */
if (typeof module !== 'undefined' && module.exports) {
    module.exports = DynamicServiceAreas;
}