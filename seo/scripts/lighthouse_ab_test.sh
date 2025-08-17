#!/bin/bash
# Lighthouse Performance Testing Script
# Blog görsel optimizasyonu A/B test analizi

echo "🔍 LIGHTHOUSE PERFORMANCE TESTING BAŞLIYOR..."
echo "============================================="

# Test URL'leri
OPTIMIZED_URLS=(
    "https://dryallekurutemizleme.com/blog/vintage-clothing-ozel-care/"
    "https://dryallekurutemizleme.com/blog/wedding-season-wedding-dress-carei/"
    "https://dryallekurutemizleme.com/blog/professional-vs-evde-carpet-cleaning-comparison/"
    "https://dryallekurutemizleme.com/blog/outdoor-textile-urunleri-carei/"
    "https://dryallekurutemizleme.com/blog/is-kiyafetleri-professional-care/"
)

CONTROL_URLS=(
    "https://dryallekurutemizleme.com/blog/autumn-kiyafet-gecisi-guide/"
    "https://dryallekurutemizleme.com/blog/winter-preparation-tekstil-koruma/"
    "https://dryallekurutemizleme.com/blog/kalorifer-sezonu-tekstil-carei/"
    "https://dryallekurutemizleme.com/blog/air-conditioned-tekstil-carei/"
    "https://dryallekurutemizleme.com/blog/back-to-school-uniform-carei/"
)

# Optimized blogları test et
echo "📊 Optimized Blogs Test Ediliyor..."
for url in "${OPTIMIZED_URLs[@]}"; do
    echo "Testing: $url"
    npx lighthouse "$url" --only-categories=performance,seo --output=json --output-path="./lighthouse-optimized-$(basename "$url").json" --chrome-flags="--headless"
done

# Control blogları test et  
echo "📊 Control Blogs Test Ediliyor..."
for url in "${CONTROL_URLS[@]}"; do
    echo "Testing: $url"
    npx lighthouse "$url" --only-categories=performance,seo --output=json --output-path="./lighthouse-control-$(basename "$url").json" --chrome-flags="--headless"
done

echo "✅ Lighthouse testleri tamamlandı!"
