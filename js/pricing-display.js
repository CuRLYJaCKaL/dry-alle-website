/* 
 * DryAlle Design System - Pricing Display Module
 * Card Rendering & Display Logic
 * MIT-Level Architecture Implementation
 */

class PricingDisplay {
    constructor() {
        this.priceGrid = document.getElementById('priceGrid');
        this.noResults = document.getElementById('noResults');
        this.loadingElement = document.querySelector('.pricing-loading');
        
        // Infinite scroll settings
        this.itemsPerPage = 10;
        this.currentPage = 1;
        this.totalItems = 0;
        this.currentData = [];
        this.allData = [];
        this.isLoading = false;
        
        // Initialize display on load
        this.initialize();
        
        // Initialize infinite scroll
        this.initializeInfiniteScroll();
    }

    // Initialize the display system
    initialize() {
        if (!window.PricingData) {
            console.error('PricingData module not loaded');
            return;
        }
        
        // Update category counts first
        this.updateCategoryCounts();
        
        // Show initial data
        this.updateDisplay(window.PricingData.multiServicePricingData);
        
        // Remove loading state
        if (this.loadingElement) {
            this.loadingElement.style.display = 'none';
        }
    }

    // Main display update method with pagination
    updateDisplay(filteredData) {
        if (!this.priceGrid || !this.noResults) {
            console.error('Required DOM elements not found');
            return;
        }

        if (filteredData.length === 0) {
            this.showNoResults();
            return;
        }
        
        // Store data for pagination
        this.allData = filteredData;
        this.totalItems = filteredData.length;
        this.currentPage = 1;
        
        this.showResults();
        this.renderPaginatedCards();
    }

    // Show no results state
    showNoResults() {
        this.priceGrid.style.display = 'none';
        this.noResults.style.display = 'block';
    }

    // Show results state
    showResults() {
        this.priceGrid.style.display = 'grid';
        this.noResults.style.display = 'none';
    }

    // Render paginated pricing cards
    renderPaginatedCards() {
        // Sort by category, then by name
        const sortedData = [...this.allData].sort((a, b) => {
            if (a.category !== b.category) return a.category.localeCompare(b.category);
            return a.name.localeCompare(b.name);
        });
        
        // Calculate current page data
        const startIndex = (this.currentPage - 1) * this.itemsPerPage;
        const endIndex = startIndex + this.itemsPerPage;
        const currentPageData = sortedData.slice(0, endIndex); // Show from beginning to current page
        
        const cardsHTML = currentPageData.map(item => this.createPricingCard(item)).join('');
        
        // Create scroll status display
        const statusHTML = this.createScrollStatus(sortedData.length);
        
        this.priceGrid.innerHTML = cardsHTML + statusHTML;
    }

    // Create infinite scroll status display
    createScrollStatus(totalItems) {
        const currentlyShowing = this.currentPage * this.itemsPerPage;
        const hasMore = currentlyShowing < totalItems;
        
        if (!hasMore) {
            return '<div class="pricing-scroll-status completed">' +
                '<div class="pricing-total-info">' +
                    '<span class="status-icon">✅</span>' +
                    '<p>Tüm hizmetler yüklendi • Toplam ' + totalItems + ' hizmet</p>' +
                '</div>' +
            '</div>';
        }
        
        return '<div class="pricing-scroll-status loading" id="scrollStatus">' +
            '<div class="pricing-scroll-info">' +
                '<div class="scroll-progress-bar">' +
                    '<div class="scroll-progress-fill" style="width: ' + Math.round((currentlyShowing / totalItems) * 100) + '%"></div>' +
                '</div>' +
                '<p class="scroll-status-text">Gösterilen: ' + currentlyShowing + ' / ' + totalItems + ' hizmet</p>' +
                '<p class="scroll-hint">Daha fazla görmek için aşağı kaydırın</p>' +
            '</div>' +
        '</div>';
    }

    // Initialize infinite scroll functionality  
    initializeInfiniteScroll() {
        let scrollTimeout;
        
        window.addEventListener('scroll', () => {
            // Throttle scroll events
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                this.handleScroll();
            }, 100);
        });
    }

    // Handle scroll event for infinite loading
    handleScroll() {
        if (this.isLoading || !this.allData.length) return;
        
        const currentlyShowing = this.currentPage * this.itemsPerPage;
        const hasMore = currentlyShowing < this.allData.length;
        
        if (!hasMore) return;
        
        // Check if user scrolled near bottom
        const scrollPosition = window.innerHeight + window.scrollY;
        const documentHeight = document.documentElement.offsetHeight;
        const threshold = 800; // Load when 800px from bottom
        
        if (scrollPosition >= documentHeight - threshold) {
            this.loadMoreItems();
        }
    }

    // Load more items automatically
    loadMoreItems() {
        if (this.isLoading) return;
        
        this.isLoading = true;
        this.showLoadingIndicator();
        
        // Simulate loading delay for smooth UX
        setTimeout(() => {
            this.currentPage++;
            this.renderPaginatedCards();
            this.isLoading = false;
            this.hideLoadingIndicator();
        }, 300);
    }

    // Show loading indicator
    showLoadingIndicator() {
        const existingLoader = document.getElementById('infiniteLoader');
        if (existingLoader) return;
        
        const loader = document.createElement('div');
        loader.id = 'infiniteLoader';
        loader.className = 'infinite-scroll-loader';
        loader.innerHTML = 
            '<div class="loader-spinner"></div>' +
            '<p class="loader-text">Yeni hizmetler yükleniyor...</p>';
        
        this.priceGrid.appendChild(loader);
    }

    // Hide loading indicator  
    hideLoadingIndicator() {
        const loader = document.getElementById('infiniteLoader');
        if (loader) {
            loader.remove();
        }
    }

    // Create individual pricing card HTML
    createPricingCard(item) {
        const categoryName = this.getCategoryDisplayName(item.category);
        const subcategoryName = this.getSubcategoryDisplayName(item.subcategory);
        
        // Sort services with popular ones first, then by SEO order
        const sortedServices = this.sortServices(item.services);
        
        // Create service rows HTML
        const serviceRows = this.createServiceRows(sortedServices);
        
        // Create structured data for SEO
        const structuredData = this.createStructuredData(item, sortedServices, categoryName);
        
        // User specified design: 200px image, compact layout
        return '<article class="pricing-card" itemscope itemtype="https://schema.org/Product">' +
            '<script type="application/ld+json">' + JSON.stringify(structuredData) + '</script>' +
            // User specified: 200px görsel area
            '<div class="pricing-card-image">' +
                '<div class="pricing-image-placeholder">👔</div>' +
            '</div>' +
            '<div class="pricing-card-content">' +
                // User specified: Kompakt başlık
                '<div class="pricing-card-header">' +
                    '<h3 class="pricing-card-title" itemprop="name">' + item.name + '</h3>' +
                '</div>' +
                // User specified: Tam genişlik liste
                '<div class="pricing-service-list">' +
                    serviceRows +
                '</div>' +
            '</div>' +
        '</article>';
    }

    // Create service rows HTML
    createServiceRows(services) {
        return services.map(service => 
            '<div class="pricing-service-row">' +
                '<span class="pricing-service-name">' + this.getProcessDisplayName(service.type) + '</span>' +
                '<span class="pricing-service-price">' + 
                    service.price + '₺' + 
                    (service.popular ? '<span class="pricing-popular-indicator"></span>' : '') + 
                '</span>' +
            '</div>'
        ).join('');
    }

    // Sort services by popularity and SEO importance
    sortServices(services) {
        return [...services].sort((a, b) => {
            // Popular services first
            if (a.popular && !b.popular) return -1;
            if (!a.popular && b.popular) return 1;
            
            // Then by SEO ranking (most searched)
            const seoOrder = ['kuru-temizleme', 'yikama', 'utuleme', 'hali-yikama', 'leke-cikarma', 'boyama', 'deri-boyama'];
            const aIndex = seoOrder.indexOf(a.type);
            const bIndex = seoOrder.indexOf(b.type);
            
            if (aIndex !== -1 && bIndex !== -1) return aIndex - bIndex;
            if (aIndex !== -1) return -1;
            if (bIndex !== -1) return 1;
            
            return a.type.localeCompare(b.type);
        });
    }

    // Create structured data for SEO
    createStructuredData(item, services, categoryName) {
        return {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": item.name,
            "category": categoryName,
            "offers": services.map(service => ({
                "@type": "Offer",
                "name": this.getProcessDisplayName(service.type),
                "price": service.price,
                "priceCurrency": "TRY"
            })),
            "brand": {
                "@type": "Organization",
                "name": "Dry Alle Kuru Temizleme"
            }
        };
    }

    // Helper: Get category display name
    getCategoryDisplayName(category) {
        if (!window.PricingData) return category;
        return window.PricingData.categoryDisplayNames[category] || category;
    }

    // Helper: Get subcategory display name
    getSubcategoryDisplayName(subcategory) {
        if (!window.PricingData) return subcategory;
        return window.PricingData.subcategoryDisplayNames[subcategory] || subcategory;
    }

    // Helper: Get process display name
    getProcessDisplayName(process) {
        if (!window.PricingData) return process;
        return window.PricingData.processDisplayNames[process] || process;
    }

    // Show loading state
    showLoading() {
        if (this.loadingElement) {
            this.loadingElement.style.display = 'block';
        }
        if (this.priceGrid) {
            this.priceGrid.style.display = 'none';
        }
        if (this.noResults) {
            this.noResults.style.display = 'none';
        }
    }

    // Hide loading state
    hideLoading() {
        if (this.loadingElement) {
            this.loadingElement.style.display = 'none';
        }
    }

    // Add new pricing data (for future Excel integration)
    addPricingData(newItems) {
        if (!window.PricingData) {
            console.error('PricingData not available');
            return;
        }
        
        // Add to data array
        window.PricingData.multiServicePricingData.push(...newItems);
        
        // Update counts
        this.updateCategoryCounts();
        
        // Refresh display if no filters are active
        if (window.PricingFilters) {
            window.PricingFilters.applyFilters();
        } else {
            this.updateDisplay(window.PricingData.multiServicePricingData);
        }
    }

    // Update category counts in sidebar
    updateCategoryCounts() {
        if (!window.PricingData) return;
        
        const data = window.PricingData.multiServicePricingData;
        
        // Update main category counts
        window.PricingData.categoryCounts = {
            'all': data.length,
            'erkek-giyim': data.filter(item => item.category === 'erkek-giyim').length,
            'kadin-giyim': data.filter(item => item.category === 'kadin-giyim').length,
            'cocuk-giyim': data.filter(item => item.category === 'cocuk-giyim').length,
            'ev-tekstili': data.filter(item => item.category === 'ev-tekstili').length,
            'ozel-temizleme': data.filter(item => item.category === 'ozel-temizleme').length
        };
        
        // Update subcategory counts
        const subcategoryCounts = {};
        data.forEach(item => {
            if (!subcategoryCounts[item.subcategory]) {
                subcategoryCounts[item.subcategory] = 0;
            }
            subcategoryCounts[item.subcategory]++;
        });
        window.PricingData.subcategoryCounts = subcategoryCounts;
        
        // Update UI counts
        this.updateSidebarCounts();
    }

    // Update sidebar count displays
    updateSidebarCounts() {
        if (!window.PricingData) return;
        
        // Update category counts
        Object.entries(window.PricingData.categoryCounts).forEach(([category, count]) => {
            const countElement = document.querySelector(`[data-category="${category}"] .blog-category-count`);
            if (countElement) {
                countElement.textContent = count;
            }
        });
        
        // Update subcategory counts
        Object.entries(window.PricingData.subcategoryCounts).forEach(([subcategory, count]) => {
            const countElement = document.querySelector(`[data-subcategory="${subcategory}"] .subcategory-count`);
            if (countElement) {
                countElement.textContent = count;
            }
        });
    }

    // Error handling
    handleError(error) {
        console.error('Pricing Display Error:', error);
        
        if (this.priceGrid) {
            this.priceGrid.innerHTML = '<div class="pricing-error">' +
                '<h3>Bir hata oluştu</h3>' +
                '<p>Fiyat listesi yüklenirken bir sorun yaşandı. Lütfen sayfayı yenileyin.</p>' +
            '</div>';
        }
    }
}

// Initialize display when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.PricingDisplay = new PricingDisplay();
});

// Export for Node.js environment
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PricingDisplay;
}