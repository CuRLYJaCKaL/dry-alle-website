// Component Loader
function loadComponent(componentName, targetSelector) {
    // Current page path'ini tespit et
    const currentPath = window.location.pathname;
    const isServicePage = currentPath.includes('/hizmetler/');
    const componentPath = isServicePage ? `../components/${componentName}.html` : `./components/${componentName}.html`;
    
    return fetch(componentPath)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(html => {
            const targetElement = document.querySelector(targetSelector);
            if (targetElement) {
                targetElement.innerHTML = html;
            }
        })
        .catch(error => {
            console.error(`Component ${componentName} yüklenemedi:`, error);
        });
}

// Hızlı İletişim component'ini yükle
function loadQuickContact() {
    loadComponent('quick-contact', '.quick-contact-container');
}

// Hizmet Bölgeleri component'ini yükle
function loadServiceAreas() {
    loadComponent('service-areas', '.service-areas-container');
}

// Mobile Sticky Bar component'ini yükle
function loadMobileStickyBar() {
    loadComponent('mobile-sticky-bar', '.mobile-sticky-bar-container');
}

// Lead Capture Form component'ini yükle
function loadLeadCaptureForm() {
    loadComponent('lead-capture-form', '.lead-capture-container');
}

// Customer Testimonials component'ini yükle
function loadCustomerTestimonials() {
    loadComponent('customer-testimonials', '.customer-testimonials-container');
}

// Sayfa yüklendiğinde çalışacak
document.addEventListener('DOMContentLoaded', function() {
    // Eğer quick-contact-container varsa component'i yükle
    if (document.querySelector('.quick-contact-container')) {
        loadQuickContact();
    }
    
    // Eğer service-areas-container varsa component'i yükle
    if (document.querySelector('.service-areas-container')) {
        loadServiceAreas();
    }
    
    // Eğer mobile-sticky-bar-container varsa component'i yükle
    if (document.querySelector('.mobile-sticky-bar-container')) {
        loadMobileStickyBar();
    }
    
    // Eğer lead-capture-container varsa component'i yükle
    if (document.querySelector('.lead-capture-container')) {
        loadLeadCaptureForm();
    }
    
    // Eğer customer-testimonials-container varsa component'i yükle
    if (document.querySelector('.customer-testimonials-container')) {
        loadCustomerTestimonials();
    }
});