/* 
 * DryAlle Design System - Pricing Filters Module
 * Category & Process Filtering Logic
 * MIT-Level Architecture Implementation
 */

class PricingFilters {
    constructor() {
        this.currentCategory = 'all';
        this.currentProcesses = ['all'];
        this.currentSubcategory = null;
        this.searchQuery = '';
        
        this.initializeEventListeners();
    }

    // Initialize all event listeners
    initializeEventListeners() {
        this.initializeCategoryFilters();
        this.initializeProcessFilters();
        this.initializeSearchFilter();
        this.initializeSubcategoryFilters();
    }

    // Category filtering system
    initializeCategoryFilters() {
        // Handle 'Tümü' category links (simple click)
        document.querySelectorAll('.pricing-category-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                this.filterByCategory(link.dataset.category);
                
                // Close all subcategories when selecting 'Tümü'
                this.closeAllSubcategories();
                
                // Remove active from expandable categories and subcategories
                this.clearExpandableActiveStates();
            });
        });

        // Handle expandable category main links
        document.querySelectorAll('.category-main-link').forEach(mainLink => {
            mainLink.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggleSubcategories(mainLink);
                
                // Remove active from simple category links
                document.querySelectorAll('.pricing-category-link').forEach(link => {
                    link.classList.remove('active');
                });
                
                // Add active to this main category
                this.setActiveMainCategory(mainLink);
            });
        });
    }

    // Process filtering system
    initializeProcessFilters() {
        document.querySelectorAll('input[data-process]').forEach(checkbox => {
            checkbox.addEventListener('change', () => this.updateProcessFilters());
        });
    }

    // Search filtering system
    initializeSearchFilter() {
        const searchInput = document.getElementById('serviceSearch');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                this.searchQuery = e.target.value.toLowerCase().trim();
                this.applyFilters();
            });
        }
    }

    // Subcategory filtering system
    initializeSubcategoryFilters() {
        document.querySelectorAll('.subcategory-link').forEach(subLink => {
            subLink.addEventListener('click', (e) => {
                e.preventDefault();
                this.filterBySubcategory(subLink.dataset.subcategory);
            });
        });
    }

    // Filter by main category
    filterByCategory(category) {
        this.currentCategory = category;
        this.currentSubcategory = null; // Clear subcategory when changing main category
        
        // Update UI active states
        this.updateCategoryActiveStates(category);
        
        this.applyFilters();
    }

    // Filter by subcategory
    filterBySubcategory(subcategory) {
        this.currentSubcategory = subcategory;
        
        // Determine parent category from subcategory
        const categoryMap = {
            'erkek-ust-giyim': 'erkek-giyim',
            'erkek-alt-giyim': 'erkek-giyim',
            'erkek-takim-elbise': 'erkek-giyim',
            'kadin-ust-giyim': 'kadin-giyim',
            'kadin-ozel-giyim': 'kadin-giyim',
            'mont-kaban': 'dis-giyim',
            'perde-tul': 'ev-tekstili',
            'yatak-takimi': 'ev-tekstili',
            'deri-kurk': 'ozel-temizleme',
            'aksesuar-genel': 'aksesuar'
        };
        
        // Set parent category
        this.currentCategory = categoryMap[subcategory] || 'all';
        
        // Update UI active states
        this.updateSubcategoryActiveStates(subcategory);
        this.updateCategoryActiveStates(this.currentCategory);
        
        // Ensure parent category subcategories are expanded
        const parentCategoryLink = document.querySelector(`[data-category="${this.currentCategory}"].category-main-link`);
        if (parentCategoryLink) {
            const subcategoriesDiv = parentCategoryLink.nextElementSibling;
            const arrow = parentCategoryLink.querySelector('.category-arrow');
            if (subcategoriesDiv && !subcategoriesDiv.classList.contains('expanded')) {
                subcategoriesDiv.classList.add('expanded');
                if (arrow) arrow.classList.add('expanded');
            }
        }
        
        this.applyFilters('', subcategory);
    }

    // Update process filters
    updateProcessFilters() {
        const checkboxes = document.querySelectorAll('input[data-process]');
        const allCheckbox = document.querySelector('input[data-process="all"]');
        
        if (allCheckbox && allCheckbox.checked) {
            this.currentProcesses = ['all'];
            checkboxes.forEach(cb => {
                if (cb !== allCheckbox) cb.checked = false;
            });
        } else {
            this.currentProcesses = Array.from(checkboxes)
                .filter(cb => cb.checked && cb.dataset.process !== 'all')
                .map(cb => cb.dataset.process);
            
            if (this.currentProcesses.length === 0) {
                allCheckbox.checked = true;
                this.currentProcesses = ['all'];
            }
        }
        
        this.applyFilters();
    }

    // Toggle subcategories display
    toggleSubcategories(categoryElement) {
        const subcategoriesDiv = categoryElement.nextElementSibling;
        const arrow = categoryElement.querySelector('.category-arrow');
        
        if (!subcategoriesDiv || !arrow) return;
        
        // Close all other subcategories
        document.querySelectorAll('.subcategories.expanded').forEach(sub => {
            if (sub !== subcategoriesDiv) {
                sub.classList.remove('expanded');
                const otherArrow = sub.previousElementSibling.querySelector('.category-arrow');
                if (otherArrow) otherArrow.classList.remove('expanded');
            }
        });
        
        // Toggle current subcategory
        subcategoriesDiv.classList.toggle('expanded');
        arrow.classList.toggle('expanded');
        
        // Also filter by this main category
        const category = categoryElement.dataset.category;
        this.filterByCategory(category);
    }

    // Close all subcategories
    closeAllSubcategories() {
        document.querySelectorAll('.subcategories.expanded').forEach(sub => {
            sub.classList.remove('expanded');
            const arrow = sub.previousElementSibling.querySelector('.category-arrow');
            if (arrow) arrow.classList.remove('expanded');
        });
    }

    // Clear active states from expandable categories
    clearExpandableActiveStates() {
        document.querySelectorAll('.category-main-link').forEach(mainLink => {
            mainLink.classList.remove('active');
        });
        document.querySelectorAll('.subcategory-link').forEach(subLink => {
            subLink.classList.remove('active');
        });
    }

    // Update category active states
    updateCategoryActiveStates(category) {
        // Clear all category active states
        document.querySelectorAll('.pricing-category-link').forEach(link => {
            link.classList.remove('active');
        });
        document.querySelectorAll('.category-main-link').forEach(link => {
            link.classList.remove('active');
        });
        
        // Set active state for current category
        const activeLink = document.querySelector(`[data-category="${category}"]`);
        if (activeLink) activeLink.classList.add('active');
    }

    // Update subcategory active states
    updateSubcategoryActiveStates(subcategory) {
        document.querySelectorAll('.subcategory-link').forEach(link => {
            link.classList.remove('active');
        });
        
        const activeSubLink = document.querySelector(`[data-subcategory="${subcategory}"]`);
        if (activeSubLink) activeSubLink.classList.add('active');
    }

    // Set active main category
    setActiveMainCategory(mainLink) {
        document.querySelectorAll('.category-main-link').forEach(link => {
            link.classList.remove('active');
        });
        mainLink.classList.add('active');
    }

    // Apply all filters and trigger display update
    applyFilters(searchQuery = this.searchQuery, subcategory = this.currentSubcategory) {
        if (!window.PricingData) {
            console.error('PricingData not loaded');
            return;
        }

        const filteredData = window.PricingData.multiServicePricingData.filter(item => {
            // Category filter
            const categoryMatch = this.currentCategory === 'all' || item.category === this.currentCategory;
            
            // Subcategory filter (if specified)
            let subcategoryMatch = true;
            if (subcategory) {
                subcategoryMatch = item.subcategory === subcategory;
            }
            
            // Process filter - check if any service in the item matches
            let processMatch = true;
            if (!this.currentProcesses.includes('all')) {
                processMatch = item.services.some(service => 
                    this.currentProcesses.includes(service.type)
                );
            }
            
            // Search filter - search in item name and service types
            const searchMatch = searchQuery === '' || 
                item.name.toLowerCase().includes(searchQuery) ||
                item.services.some(service => service.type.toLowerCase().includes(searchQuery));
            
            return categoryMatch && subcategoryMatch && processMatch && searchMatch;
        });
        
        // Trigger display update
        if (window.PricingDisplay) {
            window.PricingDisplay.updateDisplay(filteredData);
        }
    }

    // Get current filter state
    getCurrentFilters() {
        return {
            category: this.currentCategory,
            subcategory: this.currentSubcategory,
            processes: this.currentProcesses,
            searchQuery: this.searchQuery
        };
    }

    // Reset all filters
    resetFilters() {
        this.currentCategory = 'all';
        this.currentProcesses = ['all'];
        this.currentSubcategory = null;
        this.searchQuery = '';
        
        // Reset UI
        document.querySelectorAll('.pricing-category-link').forEach(link => {
            link.classList.remove('active');
        });
        document.querySelector('[data-category="all"]').classList.add('active');
        
        document.querySelectorAll('input[data-process]').forEach(cb => {
            cb.checked = cb.dataset.process === 'all';
        });
        
        const searchInput = document.getElementById('serviceSearch');
        if (searchInput) searchInput.value = '';
        
        this.closeAllSubcategories();
        this.clearExpandableActiveStates();
        
        this.applyFilters();
    }
}

// Initialize filters when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.PricingFilters = new PricingFilters();
});

// Export for Node.js environment
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PricingFilters;
}