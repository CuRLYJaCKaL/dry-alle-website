// Image Optimization & Compression System
class ImageOptimizer {
    constructor() {
        this.compressionQuality = 0.7; // 70% quality for balance
        this.maxWidth = 1200; // Maximum width for images
        this.maxHeight = 800; // Maximum height for images
        this.init();
    }

    init() {
        this.compressExistingImages();
        this.implementLazyLoading();
        this.addResponsiveImages();
        this.preloadCriticalImages();
    }

    // Compress images on the client side if needed
    compressExistingImages() {
        // Only apply to non-critical images to avoid breaking hero images
        const images = document.querySelectorAll('img:not(.critical-image):not(.hero-image)');
        
        images.forEach((img) => {
            // Only add lazy loading if not already set
            if (!img.hasAttribute('loading')) {
                img.setAttribute('loading', 'lazy');
            }
            if (!img.hasAttribute('decoding')) {
                img.setAttribute('decoding', 'async');
            }
        });
    }

    optimizeImageSize(img) {
        // Minimal optimization - just ensure responsive behavior
        if (!img.style.maxWidth) {
            img.style.maxWidth = '100%';
        }
        if (!img.style.height) {
            img.style.height = 'auto';
        }
    }

    makeImageResponsive(img) {
        // Add responsive classes and behavior
        if (!img.classList.contains('responsive-image')) {
            img.classList.add('responsive-image');
            
            // Wrap in responsive container if not already wrapped
            if (!img.parentElement.classList.contains('image-container')) {
                const wrapper = document.createElement('div');
                wrapper.className = 'image-container';
                img.parentNode.insertBefore(wrapper, img);
                wrapper.appendChild(img);
            }
        }
    }

    implementLazyLoading() {
        // Very minimal lazy loading - only add fade effect to already lazy images
        if ('loading' in HTMLImageElement.prototype) {
            const lazyImages = document.querySelectorAll('img[loading="lazy"]');
            lazyImages.forEach(img => {
                if (!img.complete && !img.style.transition) {
                    img.onload = function() {
                        this.style.transition = 'opacity 0.3s ease';
                    };
                }
            });
        }
    }

    addResponsiveImages() {
        // Add CSS for responsive behavior
        const style = document.createElement('style');
        style.textContent = `
            .responsive-image {
                max-width: 100%;
                height: auto;
                display: block;
                transition: opacity 0.3s ease;
            }
            
            .image-container {
                position: relative;
                overflow: hidden;
                background-color: #f5f5f5;
            }
            
            .image-loading {
                opacity: 0;
            }
            
            .image-loaded {
                opacity: 1;
            }
            
            /* Critical images optimization */
            .hero-image {
                width: 100%;
                max-width: 1200px;
                height: auto;
                object-fit: cover;
                background-color: #f0f0f0;
            }
            
            /* Service images optimization */
            .service-image {
                width: 100%;
                max-width: 400px;
                height: auto;
                object-fit: cover;
                border-radius: 8px;
            }
            
            /* Mobile optimizations */
            @media (max-width: 768px) {
                .hero-image {
                    max-width: 100%;
                    height: 250px;
                    object-fit: cover;
                }
                
                .service-image {
                    max-width: 100%;
                    height: 200px;
                    object-fit: cover;
                }
            }
            
            /* Lazy loading placeholder */
            img[loading="lazy"] {
                background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
                background-size: 200% 100%;
                animation: loading 1.5s infinite;
            }
            
            @keyframes loading {
                0% { background-position: 200% 0; }
                100% { background-position: -200% 0; }
            }
            
            /* WebP support detection */
            .webp .hero-image {
                background-image: url('asset/hero-image.webp');
            }
            
            .no-webp .hero-image {
                background-image: url('asset/hero-image.jpg');
            }
        `;
        document.head.appendChild(style);
    }

    preloadCriticalImages() {
        // Preload only the most critical images
        const criticalImages = [
            'asset/hero-image.png',
            'asset/hero-background.png'
        ];

        criticalImages.forEach(src => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.as = 'image';
            link.href = src;
            document.head.appendChild(link);
        });
    }

    // WebP support detection
    detectWebPSupport() {
        const webP = new Image();
        webP.onload = webP.onerror = function () {
            if (webP.height == 2) {
                document.documentElement.classList.add('webp');
            } else {
                document.documentElement.classList.add('no-webp');
            }
        };
        webP.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
    }

    // Compress image function (for future use)
    compressImage(file, quality = 0.7, maxWidth = 1200, maxHeight = 800) {
        return new Promise((resolve) => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            const img = new Image();

            img.onload = function() {
                // Calculate new dimensions
                let { width, height } = img;
                
                if (width > maxWidth) {
                    height = (height * maxWidth) / width;
                    width = maxWidth;
                }
                
                if (height > maxHeight) {
                    width = (width * maxHeight) / height;
                    height = maxHeight;
                }

                canvas.width = width;
                canvas.height = height;

                // Draw and compress
                ctx.drawImage(img, 0, 0, width, height);
                
                canvas.toBlob(resolve, 'image/jpeg', quality);
            };

            img.src = URL.createObjectURL(file);
        });
    }

    // Performance monitoring
    monitorImagePerformance() {
        if ('PerformanceObserver' in window) {
            const observer = new PerformanceObserver((list) => {
                for (const entry of list.getEntries()) {
                    if (entry.initiatorType === 'img') {
                        console.log(`Image ${entry.name} loaded in ${entry.duration}ms`);
                        
                        // Track slow loading images
                        if (entry.duration > 1000) {
                            console.warn(`Slow image detected: ${entry.name}`);
                            
                            // Analytics tracking
                            if (typeof gtag !== 'undefined') {
                                gtag('event', 'slow_image', {
                                    'event_category': 'Performance',
                                    'event_label': entry.name,
                                    'value': Math.round(entry.duration)
                                });
                            }
                        }
                    }
                }
            });
            observer.observe({ entryTypes: ['resource'] });
        }
    }

    // Get image optimization recommendations
    getOptimizationRecommendations() {
        const images = document.querySelectorAll('img');
        const recommendations = [];

        images.forEach((img, index) => {
            const naturalWidth = img.naturalWidth;
            const naturalHeight = img.naturalHeight;
            const displayWidth = img.offsetWidth;
            const displayHeight = img.offsetHeight;

            // Check if image is oversized
            if (naturalWidth > displayWidth * 2 || naturalHeight > displayHeight * 2) {
                recommendations.push({
                    element: img,
                    issue: 'oversized',
                    natural: `${naturalWidth}x${naturalHeight}`,
                    display: `${displayWidth}x${displayHeight}`,
                    savings: `${Math.round(((naturalWidth * naturalHeight) - (displayWidth * displayHeight * 4)) / (naturalWidth * naturalHeight) * 100)}%`
                });
            }
        });

        return recommendations;
    }
}

// Initialize image optimization when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const optimizer = new ImageOptimizer();
    
    // Detect WebP support
    optimizer.detectWebPSupport();
    
    // Monitor performance
    optimizer.monitorImagePerformance();
    
    // Log optimization recommendations in development
    if (window.location.hostname === 'localhost') {
        setTimeout(() => {
            const recommendations = optimizer.getOptimizationRecommendations();
            if (recommendations.length > 0) {
                console.group('Image Optimization Recommendations:');
                recommendations.forEach(rec => {
                    console.log(`${rec.element.src} - ${rec.issue} (${rec.natural} → ${rec.display}) - Potential savings: ${rec.savings}`);
                });
                console.groupEnd();
            }
        }, 2000);
    }
});

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ImageOptimizer;
}