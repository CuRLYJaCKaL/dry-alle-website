/**
 * Script.js - Global Site Functionality
 * MIT Architecture - Corporate Standard
 * Handles general site interactions, mobile optimization, and performance
 */

// Global site initialization
document.addEventListener('DOMContentLoaded', function() {
    initMobileNavigation();
    initContactButton();
    initPerformanceOptimization();
    initAccessibilityEnhancements();
    initSEOEnhancements();
});

// Mobile Navigation Enhancement
function initMobileNavigation() {
    const contactButton = document.querySelector('.contact-button');
    if (contactButton) {
        contactButton.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Show contact options on mobile
            if (window.innerWidth <= 768) {
                showMobileContactMenu();
            } else {
                // Desktop behavior - scroll to contact
                const contactSection = document.querySelector('#contact');
                if (contactSection) {
                    contactSection.scrollIntoView({ behavior: 'smooth' });
                }
            }
            
            // GTM tracking
            if (typeof gtag !== 'undefined') {
                gtag('event', 'contact_button_click', {
                    'event_category': 'Contact',
                    'event_label': 'Header Contact Button'
                });
            }
        });
    }
}

// Mobile Contact Menu
function showMobileContactMenu() {
    const existingMenu = document.querySelector('.mobile-contact-menu');
    if (existingMenu) {
        existingMenu.remove();
        return;
    }

    const menu = document.createElement('div');
    menu.className = 'mobile-contact-menu';
    menu.innerHTML = `
        <div class="mobile-contact-overlay">
            <div class="mobile-contact-content">
                <div class="contact-header">
                    <h3>İletişim Seçenekleri</h3>
                    <button class="close-btn" onclick="closeMobileContactMenu()">×</button>
                </div>
                <div class="contact-options">
                    <a href="tel:+905433527474" class="contact-option">
                        <span class="option-icon">📞</span>
                        <div class="option-text">
                            <span class="option-title">Hemen Arayın</span>
                            <span class="option-subtitle">0 (543) 352 74 74</span>
                        </div>
                    </a>
                    <a href="#" class="contact-option" onclick="openWhatsApp()">
                        <span class="option-icon">💬</span>
                        <div class="option-text">
                            <span class="option-title">WhatsApp</span>
                            <span class="option-subtitle">Hızlı mesaj gönderin</span>
                        </div>
                    </a>
                    <a href="#contact" class="contact-option">
                        <span class="option-icon">📍</span>
                        <div class="option-text">
                            <span class="option-title">Adres & İletişim</span>
                            <span class="option-subtitle">Detaylı bilgiler</span>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(menu);
    
    // Close on overlay click
    menu.querySelector('.mobile-contact-overlay').addEventListener('click', function(e) {
        if (e.target === this) {
            closeMobileContactMenu();
        }
    });
}

// Close mobile contact menu
function closeMobileContactMenu() {
    const menu = document.querySelector('.mobile-contact-menu');
    if (menu) {
        menu.remove();
    }
}

// Contact button initialization
function initContactButton() {
    // Add click tracking to all phone links
    document.querySelectorAll('a[href^="tel:"]').forEach(link => {
        link.addEventListener('click', function() {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'phone_call_click', {
                    'event_category': 'Contact',
                    'event_label': this.href.replace('tel:', ''),
                    'value': 1
                });
            }
        });
    });
}

// Performance Optimization
function initPerformanceOptimization() {
    // Lazy load images if intersection observer is supported
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        observer.unobserve(img);
                    }
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Preload critical resources
    const criticalResources = [
        '../styles.css',
        '../asset/logo.webp'
    ];

    criticalResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = resource;
        document.head.appendChild(link);
    });
}

// Accessibility Enhancements
function initAccessibilityEnhancements() {
    // Improve keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeMobileContactMenu();
        }
    });

    // Add focus visible for better keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            document.body.classList.add('keyboard-navigation');
        }
    });

    document.addEventListener('mousedown', function() {
        document.body.classList.remove('keyboard-navigation');
    });
}

// SEO & Analytics Enhancements
function initSEOEnhancements() {
    // Track scroll depth for engagement metrics
    let scrollDepthTracked = false;
    
    window.addEventListener('scroll', function() {
        const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
        
        if (scrollPercent > 50 && !scrollDepthTracked && typeof gtag !== 'undefined') {
            gtag('event', 'scroll_depth_50', {
                'event_category': 'Engagement',
                'event_label': document.title
            });
            scrollDepthTracked = true;
        }
    });

    // Track time on page
    const startTime = Date.now();
    window.addEventListener('beforeunload', function() {
        const timeOnPage = Math.round((Date.now() - startTime) / 1000);
        if (timeOnPage > 30 && typeof gtag !== 'undefined') {
            gtag('event', 'time_on_page', {
                'event_category': 'Engagement',
                'event_label': document.title,
                'value': timeOnPage
            });
        }
    });
}

// Utility function for smooth scrolling
function smoothScrollTo(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// WhatsApp integration (global utility)
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

// Error handling for missing resources
window.addEventListener('error', function(e) {
    // Log JavaScript errors but don't break functionality
    if (typeof gtag !== 'undefined') {
        gtag('event', 'javascript_error', {
            'event_category': 'Technical',
            'event_label': e.message || 'Unknown error',
            'value': 0
        });
    }
});

// Export functions for global access
window.Dry All = {
    openWhatsApp,
    smoothScrollTo,
    closeMobileContactMenu
};