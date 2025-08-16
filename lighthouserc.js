module.exports = {
  ci: {
    collect: {
      url: [
        'http://localhost:8080/',
        'http://localhost:8080/hizmetler/kuru-temizleme.html',
        'http://localhost:8080/hizmetler/hali-yikama.html',
        'http://localhost:8080/hizmetler/koltuk-yikama.html',
        'http://localhost:8080/hizmetler/perde-temizleme.html',
        'http://localhost:8080/bolgeler/kadikoy-kuru-temizleme.html',
        'http://localhost:8080/bolgeler/atasehir-hali-yikama.html',
        'http://localhost:8080/sss.html'
      ],
      startServerCommand: 'python3 -m http.server 8080',
      startServerReadyPattern: 'Serving HTTP',
      settings: {
        chromeFlags: '--no-sandbox --headless',
        preset: 'desktop'
      }
    },
    assert: {
      assertions: {
        'categories:performance': ['warn', {minScore: 0.9}],
        'categories:accessibility': ['error', {minScore: 0.9}],
        'categories:best-practices': ['warn', {minScore: 0.9}],
        'categories:seo': ['error', {minScore: 0.95}],
        'categories:pwa': 'off',
        
        // Performance metrics
        'first-contentful-paint': ['warn', {maxNumericValue: 2000}],
        'largest-contentful-paint': ['warn', {maxNumericValue: 2500}],
        'cumulative-layout-shift': ['error', {maxNumericValue: 0.1}],
        'total-blocking-time': ['warn', {maxNumericValue: 300}],
        
        // SEO specific assertions
        'meta-description': 'error',
        'document-title': 'error',
        'crawlable-anchors': 'error',
        'robots-txt': 'warn',
        'hreflang': 'off',
        'canonical': 'error',
        'structured-data': 'warn',
        
        // Accessibility
        'color-contrast': 'error',
        'image-alt': 'error',
        'label': 'error',
        'link-name': 'error',
        
        // Best practices
        'uses-https': 'error',
        'is-on-https': 'error',
        'uses-text-compression': 'warn',
        'uses-responsive-images': 'warn'
      }
    },
    upload: {
      target: 'temporary-public-storage'
    }
  }
};