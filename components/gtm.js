// Google Tag Manager Global Component
// Bu dosya tüm sayfalarda çağrılabilir

// GTM Container ID - Gerçek GTM ID
const GTM_ID = 'GTM-PXKN4266';

// GTM Script Injection - Head kısmına GTM kodunu enjekte eder
function injectGTMHead() {
    // Zaten yüklenmiş mi kontrol et
    if (document.querySelector('#gtm-script') || window.google_tag_manager) {
        return;
    }
    
    // DataLayer oluştur
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
    
    // GTM Script oluştur ve head'e ekle
    const gtmScript = document.createElement('script');
    gtmScript.id = 'gtm-script';
    gtmScript.async = true;
    gtmScript.src = `https://www.googletagmanager.com/gtm.js?id=${GTM_ID}`;
    
    const firstScript = document.getElementsByTagName('script')[0];
    firstScript.parentNode.insertBefore(gtmScript, firstScript);
    
    console.log('GTM Head Script injected:', GTM_ID);
}

// GTM NoScript Injection - Body kısmına noscript iframe enjekte eder
function injectGTMNoScript() {
    // Zaten var mı kontrol et
    if (document.querySelector('#gtm-noscript')) {
        return;
    }
    
    // NoScript iframe oluştur
    const noscript = document.createElement('noscript');
    noscript.id = 'gtm-noscript';
    noscript.innerHTML = `<iframe src="https://www.googletagmanager.com/ns.html?id=${GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe>`;
    
    // Body'nin en başına ekle
    document.body.insertBefore(noscript, document.body.firstChild);
    
    console.log('GTM NoScript injected:', GTM_ID);
}

// Sayfa bilgilerini GTM'e gönder
function sendPageData() {
    if (!window.dataLayer) {
        window.dataLayer = [];
    }
    
    // Sayfa spesifik veriler
    window.dataLayer.push({
        'event': 'page_view_custom',
        'page_title': document.title,
        'page_location': window.location.href,
        'page_path': window.location.pathname,
        'content_group1': getContentGroup(),
        'site_section': getSiteSection()
    });
    
    console.log('Page data sent to GTM:', getContentGroup());
}

// İçerik grubunu belirle (sayfa tipine göre)
function getContentGroup() {
    const path = window.location.pathname;
    
    if (path.includes('/blog/')) {
        return 'Blog';
    } else if (path.includes('/hizmetler/')) {
        return 'Services';
    } else if (path.includes('/bolgeler/')) {
        return 'Regions';
    } else if (path.includes('fiyatlar.html')) {
        return 'Pricing';
    } else if (path === '/' || path.includes('index.html')) {
        return 'Homepage';
    }
    return 'Other';
}

// Site bölümünü belirle
function getSiteSection() {
    const path = window.location.pathname;
    
    if (path.includes('/blog/')) {
        return 'Content Marketing';
    } else if (path.includes('/hizmetler/')) {
        return 'Service Pages';
    } else if (path.includes('/bolgeler/')) {
        return 'Location Pages';
    } else if (path.includes('fiyatlar.html')) {
        return 'Pricing';
    } else if (path === '/' || path.includes('index.html')) {
        return 'Homepage';
    }
    return 'Other Pages';
}

// GTM Events - tüm sayfalarda kullanılabilir
const GTMEvents = {
    // Telefon tıklama eventi
    trackPhoneClick: function(phoneNumber) {
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'phone_click',
                'event_category': 'engagement',
                'event_label': phoneNumber,
                'phone_number': phoneNumber,
                'value': 1
            });
        }
    },
    
    // Hizmet sorgusu eventi
    trackServiceInquiry: function(service, location = '') {
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'service_inquiry',
                'event_category': 'lead_generation',
                'event_label': service,
                'service_type': service,
                'location_area': location,
                'value': 1
            });
        }
    },
    
    // Blog etkileşimi
    trackBlogInteraction: function(action, category, article = '') {
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'blog_interaction',
                'event_category': 'blog_engagement',
                'event_label': article || category,
                'blog_action': action,
                'blog_category': category,
                'blog_article': article
            });
        }
    },
    
    // Form gönderimi
    trackFormSubmission: function(formType, formLocation = '') {
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'form_submit',
                'event_category': 'lead_generation',
                'event_label': formType,
                'form_type': formType,
                'form_location': formLocation,
                'value': 5
            });
        }
    },
    
    // Fiyat listesi görüntüleme
    trackPricingView: function(serviceCategory) {
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'pricing_view',
                'event_category': 'engagement',
                'event_label': serviceCategory,
                'pricing_category': serviceCategory
            });
        }
    },
    
    // Scroll depth tracking
    trackScrollDepth: function(depth) {
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'scroll_depth',
                'event_category': 'engagement',
                'event_label': depth + '%',
                'scroll_depth': depth
            });
        }
    }
};

// Otomatik event listener'lar
function initializeAutoTracking() {
    // Telefon linklerine tıklama
    document.addEventListener('click', function(e) {
        if (e.target.href && e.target.href.startsWith('tel:')) {
            const phoneNumber = e.target.href.replace('tel:', '');
            GTMEvents.trackPhoneClick(phoneNumber);
        }
        
        // Email linklerine tıklama
        if (e.target.href && e.target.href.startsWith('mailto:')) {
            const email = e.target.href.replace('mailto:', '');
            if (window.dataLayer) {
                window.dataLayer.push({
                    'event': 'email_click',
                    'event_category': 'engagement',
                    'event_label': email
                });
            }
        }
        
        // Blog makale tıklamaları (blog sayfasında)
        if (e.target.closest('.blog-card-cta') || e.target.closest('.blog-card-title')) {
            const blogCard = e.target.closest('.modern-blog-card');
            if (blogCard) {
                const title = blogCard.querySelector('.blog-card-title')?.textContent || 'Unknown Article';
                GTMEvents.trackBlogInteraction('article_click', 'article_engagement', title);
            }
        }
        
        // Hizmet linklerine tıklama
        if (e.target.href && (e.target.href.includes('/hizmetler/') || e.target.closest('.service-card'))) {
            const serviceCard = e.target.closest('.service-card');
            if (serviceCard) {
                const serviceName = serviceCard.querySelector('h3')?.textContent || 'Unknown Service';
                GTMEvents.trackServiceInquiry(serviceName);
            }
        }
    });
    
    // Scroll depth tracking
    let scrollDepthTracked = {};
    window.addEventListener('scroll', function() {
        const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
        
        // 25%, 50%, 75%, 100% için tracking
        [25, 50, 75, 100].forEach(depth => {
            if (scrollPercent >= depth && !scrollDepthTracked[depth]) {
                scrollDepthTracked[depth] = true;
                GTMEvents.trackScrollDepth(depth);
            }
        });
    });
}

// GTM Initialization - Ana başlatma fonksiyonu
function initGTM() {
    // 1. GTM scripts'lerini enjekte et
    injectGTMHead();
    
    // 2. DOM yüklendiğinde noscript'i ekle
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            injectGTMNoScript();
            sendPageData();
            initializeAutoTracking();
        });
    } else {
        injectGTMNoScript();
        sendPageData();
        initializeAutoTracking();
    }
    
    // 3. Sayfa spesifik tracking
    setTimeout(function() {
        if (window.location.pathname.includes('fiyatlar.html')) {
            GTMEvents.trackPricingView('all_services');
        }
    }, 1000);
    
    console.log('GTM Initialization completed for:', window.location.pathname);
}

// Sayfa yüklendiğinde otomatik başlat
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGTM);
} else {
    initGTM();
}

// Global olarak erişilebilir yap
window.GTMEvents = GTMEvents;
window.initGTM = initGTM;