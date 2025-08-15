// Performance Optimization & Core Web Vitals Enhancement
class PerformanceOptimizer {
    constructor() {
        this.images = [];
        this.lazyLoadThreshold = 50;
        this.init();
    }

    init() {
        // Image optimization disabled to prevent loading issues
        // this.optimizeImages();
        // Lazy loading also disabled
        // this.implementLazyLoading();
        this.preloadCriticalResources();
        this.optimizeWebFonts();
        this.measureWebVitals();
        this.compressCSS();
        this.deferNonCriticalJS();
    }

    optimizeImages() {
        const images = document.querySelectorAll('img');
        
        images.forEach(img => {
            // WebP format support check
            if (this.supportsWebP()) {
                this.convertToWebP(img);
            }

            // Lazy loading implementation
            img.setAttribute('loading', 'lazy');
            
            // Responsive images
            this.makeResponsive(img);
            
            // Compression hints
            if (!img.hasAttribute('decoding')) {
                img.setAttribute('decoding', 'async');
            }
        });
    }

    supportsWebP() {
        const canvas = document.createElement('canvas');
        return canvas.toDataURL('image/webp').indexOf('data:image/webp') === 0;
    }

    convertToWebP(img) {
        const originalSrc = img.src;
        if (originalSrc.includes('.jpg') || originalSrc.includes('.png')) {
            const webpSrc = originalSrc.replace(/\.(jpg|png)$/, '.webp');
            
            // Create a new image to test WebP availability
            const testImage = new Image();
            testImage.onload = () => {
                img.src = webpSrc;
            };
            testImage.onerror = () => {
                // Keep original format if WebP not available
                console.log('WebP not available for:', originalSrc);
            };
            testImage.src = webpSrc;
        }
    }

    makeResponsive(img) {
        if (!img.hasAttribute('srcset')) {
            const src = img.src;
            const baseName = src.replace(/\.[^/.]+$/, "");
            const extension = src.split('.').pop();
            
            // Generate srcset for different screen sizes
            const srcset = [
                `${baseName}-320w.${extension} 320w`,
                `${baseName}-640w.${extension} 640w`,
                `${baseName}-960w.${extension} 960w`,
                `${baseName}-1280w.${extension} 1280w`
            ].join(', ');
            
            img.setAttribute('srcset', srcset);
            img.setAttribute('sizes', '(max-width: 320px) 280px, (max-width: 640px) 600px, (max-width: 960px) 920px, 1240px');
        }
    }

    implementLazyLoading() {
        // Native lazy loading fallback
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.classList.remove('lazy');
                            imageObserver.unobserve(img);
                        }
                    }
                });
            }, {
                rootMargin: `${this.lazyLoadThreshold}px`
            });

            const lazyImages = document.querySelectorAll('img[data-src]');
            lazyImages.forEach(img => imageObserver.observe(img));
        }
    }

    preloadCriticalResources() {
        // Critical CSS
        const criticalCSS = document.createElement('link');
        criticalCSS.rel = 'preload';
        criticalCSS.href = '/styles.css';
        criticalCSS.as = 'style';
        criticalCSS.onload = function() { this.rel = 'stylesheet'; };
        document.head.appendChild(criticalCSS);

        // Critical fonts
        const criticalFont = document.createElement('link');
        criticalFont.rel = 'preload';
        criticalFont.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap';
        criticalFont.as = 'style';
        criticalFont.crossOrigin = 'anonymous';
        document.head.appendChild(criticalFont);

        // DNS prefetch for external domains
        this.addDNSPrefetch([
            'https://fonts.googleapis.com',
            'https://fonts.gstatic.com',
            'https://www.google-analytics.com',
            'https://wa.me'
        ]);
    }

    addDNSPrefetch(domains) {
        domains.forEach(domain => {
            const prefetch = document.createElement('link');
            prefetch.rel = 'dns-prefetch';
            prefetch.href = domain;
            document.head.appendChild(prefetch);
        });
    }

    optimizeWebFonts() {
        // Font display swap for better CLS
        const fontLinks = document.querySelectorAll('link[href*="fonts.googleapis.com"]');
        fontLinks.forEach(link => {
            if (!link.href.includes('display=swap')) {
                link.href += '&display=swap';
            }
        });
    }

    measureWebVitals() {
        // Core Web Vitals measurement
        if ('PerformanceObserver' in window) {
            // Largest Contentful Paint (LCP)
            new PerformanceObserver((entryList) => {
                for (const entry of entryList.getEntries()) {
                    console.log('LCP:', entry.startTime);
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'web_vitals', {
                            event_category: 'Performance',
                            event_label: 'LCP',
                            value: Math.round(entry.startTime)
                        });
                    }
                }
            }).observe({ type: 'largest-contentful-paint', buffered: true });

            // First Input Delay (FID)
            new PerformanceObserver((entryList) => {
                for (const entry of entryList.getEntries()) {
                    console.log('FID:', entry.processingStart - entry.startTime);
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'web_vitals', {
                            event_category: 'Performance',
                            event_label: 'FID',
                            value: Math.round(entry.processingStart - entry.startTime)
                        });
                    }
                }
            }).observe({ type: 'first-input', buffered: true });

            // Cumulative Layout Shift (CLS)
            let clsValue = 0;
            new PerformanceObserver((entryList) => {
                for (const entry of entryList.getEntries()) {
                    if (!entry.hadRecentInput) {
                        clsValue += entry.value;
                        console.log('CLS:', clsValue);
                        if (typeof gtag !== 'undefined') {
                            gtag('event', 'web_vitals', {
                                event_category: 'Performance',
                                event_label: 'CLS',
                                value: Math.round(clsValue * 1000)
                            });
                        }
                    }
                }
            }).observe({ type: 'layout-shift', buffered: true });
        }
    }

    compressCSS() {
        // Critical CSS inlining
        const criticalCSS = `
            /* Above-the-fold critical styles */
            body { margin: 0; padding: 0; font-family: Inter, system-ui, sans-serif; }
            .header { background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            .service-hero { padding: 80px 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            .whatsapp-floating { position: fixed; bottom: 20px; right: 20px; z-index: 1000; }
        `;
        
        const style = document.createElement('style');
        style.textContent = criticalCSS;
        document.head.appendChild(style);
    }

    deferNonCriticalJS() {
        // Defer non-critical JavaScript
        const scripts = document.querySelectorAll('script[src]');
        scripts.forEach(script => {
            if (!script.src.includes('critical') && !script.hasAttribute('defer')) {
                script.defer = true;
            }
        });
    }

    // Public method to get performance metrics
    getMetrics() {
        return new Promise((resolve) => {
            if ('performance' in window) {
                const navigation = performance.getEntriesByType('navigation')[0];
                const metrics = {
                    dom_load_time: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
                    page_load_time: navigation.loadEventEnd - navigation.loadEventStart,
                    first_byte: navigation.responseStart - navigation.requestStart,
                    dns_time: navigation.domainLookupEnd - navigation.domainLookupStart
                };
                resolve(metrics);
            }
        });
    }
}

// Initialize performance optimizer
document.addEventListener('DOMContentLoaded', () => {
    const performanceOpt = new PerformanceOptimizer();
    
    // Report metrics after page load
    window.addEventListener('load', () => {
        setTimeout(() => {
            performanceOpt.getMetrics().then(metrics => {
                console.log('Performance Metrics:', metrics);
                
                // Send to analytics if available
                if (typeof gtag !== 'undefined') {
                    Object.entries(metrics).forEach(([key, value]) => {
                        gtag('event', 'performance_metric', {
                            event_category: 'Performance',
                            event_label: key,
                            value: Math.round(value)
                        });
                    });
                }
            });
        }, 1000);
    });
});

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PerformanceOptimizer;
}