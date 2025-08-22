#!/usr/bin/env python3
"""
DryAlle Bulk Mobile SEO Optimizer
MIT Architecture Preserved - 2025 Google/AI/LLM Ready
"""

import os
import re
import json
from pathlib import Path

# Location data for each region
LOCATIONS = {
    'atasehir': {'coords': '41.0188;29.1264', 'district': 'Ataşehir, İstanbul'},
    'bagdat-caddesi': {'coords': '40.9667;29.0667', 'district': 'Bağdat Caddesi, Kadıköy, İstanbul'},
    'barbaros': {'coords': '41.0392;29.0067', 'district': 'Barbaros, Beşiktaş, İstanbul'},
    'bostanci': {'coords': '40.9588;29.0944', 'district': 'Bostancı, Kadıköy, İstanbul'},
    'caddebostan': {'coords': '40.9656;29.0933', 'district': 'Caddebostan, Kadıköy, İstanbul'},
    'camlica': {'coords': '41.0194;29.0664', 'district': 'Çamlıca, Üsküdar, İstanbul'},
    'erenkoy': {'coords': '40.9772;29.0725', 'district': 'Erenköy, Kadıköy, İstanbul'},
    'fenerbahce': {'coords': '40.9633;29.0467', 'district': 'Fenerbahçe, Kadıköy, İstanbul'},
    'fikirtepe': {'coords': '40.9689;29.0533', 'district': 'Fikirtepe, Kadıköy, İstanbul'},
    'goztepe': {'coords': '40.9839;29.0564', 'district': 'Göztepe, Kadıköy, İstanbul'},
    'icerenkoy': {'coords': '40.9711;29.0778', 'district': 'İçerenköy, Ataşehir, İstanbul'},
    'kadikoy': {'coords': '40.9903;29.0275', 'district': 'Kadıköy, İstanbul'},
    'kalamis': {'coords': '40.9628;29.0394', 'district': 'Kalamış, Kadıköy, İstanbul'},
    'kartal': {'coords': '40.9092;29.1822', 'district': 'Kartal, İstanbul'},
    'kozyatagi': {'coords': '40.9711;29.0778', 'district': 'Kozyatağı, Kadıköy, İstanbul'},
    'kucukbakkalkoy': {'coords': '40.9756;29.0853', 'district': 'Küçükbakkalköy, Ataşehir, İstanbul'},
    'maltepe': {'coords': '40.9333;29.1333', 'district': 'Maltepe, İstanbul'},
    'moda': {'coords': '40.9800;29.0333', 'district': 'Moda, Kadıköy, İstanbul'},
    'pendik': {'coords': '40.8783;29.2322', 'district': 'Pendik, İstanbul'},
    'sahrayicedit': {'coords': '40.9667;29.0667', 'district': 'Sahrayıcedit, Kadıköy, İstanbul'},
    'suadiye': {'coords': '40.9583;29.0567', 'district': 'Suadiye, Kadıköy, İstanbul'},
    'umraniye': {'coords': '41.0167;29.1167', 'district': 'Ümraniye, İstanbul'},
    'uskudar': {'coords': '41.0214;29.0144', 'district': 'Üsküdar, İstanbul'},
    'altunizade': {'coords': '41.0156;29.0661', 'district': 'Altunizade, Üsküdar, İstanbul'}
}

def extract_location_from_filename(filename):
    """Extract location key from filename"""
    base = filename.replace('.html', '')
    for location in LOCATIONS:
        if base.startswith(location):
            return location
    return None

def get_service_type(filename):
    """Extract service type from filename"""
    if 'kuru-temizleme' in filename:
        return 'kuru-temizleme'
    elif 'koltuk-yikama' in filename:
        return 'koltuk-yikama'
    elif 'hali-yikama' in filename:
        return 'hali-yikama'
    elif 'premium' in filename or 'luxury' in filename:
        return 'premium-service'
    elif 'gelinlik' in filename:
        return 'gelinlik-temizleme'
    elif 'haute-couture' in filename:
        return 'haute-couture'
    else:
        return 'specialized-service'

def generate_mobile_seo_block(location_key, service_type, title):
    """Generate mobile SEO optimization block"""
    location_data = LOCATIONS.get(location_key, {'coords': '41.0000;29.0000', 'district': 'İstanbul'})
    
    # Custom tracking parameter
    tracking_param = f"{location_key}_{service_type}".replace('-', '_')
    
    return f'''
    <!-- Font Loading Optimization for Mobile Performance -->
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&family=Dancing+Script:wght@700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&family=Dancing+Script:wght@700&display=swap"></noscript>
    
    <!-- Google Mobile SEO Enhancement -->
    <meta name="format-detection" content="telephone=yes">
    <meta name="mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-touch-fullscreen" content="yes">
    
    <!-- PWA & Mobile Performance Signals - {location_data['district']} Specific -->
    <meta name="mobile-web-app-title" content="Dry Alle - {title}">
    <meta name="application-name" content="Dry Alle {location_data['district'].split(',')[0]} Services">
    <meta name="msapplication-TileColor" content="#006a44">
    <meta name="msapplication-config" content="../browserconfig.xml">
    
    <!-- 2025 AI/LLM Location-Specific Signals -->
    <meta name="geo.region" content="TR-34">
    <meta name="geo.placename" content="{location_data['district']}">
    <meta name="geo.position" content="{location_data['coords']}">
    <meta name="ICBM" content="{location_data['coords'].replace(';', ', ')}">
    
    <!-- Critical CSS for LCP Optimization -->
    <style>
    /* Critical above-the-fold styles - MIT architecture preserved */
    :root{{--color-primary:#006a44;--color-primary-darker:#00623b;--color-secondary:#f6ec3d;--color-white:#ffffff;--spacing-2:0.5rem;--spacing-4:1rem;--spacing-5:1.25rem;--spacing-6:1.5rem;--spacing-8:2rem;--spacing-10:2.5rem;--spacing-12:3rem;--spacing-16:4rem;--font-size-base:1rem;--font-size-lg:1.125rem;--font-size-xl:1.25rem;--font-size-2xl:1.5rem;--font-weight-medium:500;--font-weight-semibold:600;--font-weight-bold:700;--transition-base:0.3s ease}}
    *,*::before,*::after{{box-sizing:border-box}}*{{margin:0;padding:0}}
    body{{font-family:'Roboto',-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif;line-height:1.6;color:#333}}
    .top-bar{{background:var(--color-secondary);color:#333;font-weight:var(--font-weight-semibold);text-align:center;padding:var(--spacing-2) 0;font-size:var(--font-size-base)}}
    .service-hero{{background:linear-gradient(135deg,var(--color-primary-darker) 0%,#1a5d42 100%);color:var(--color-white);padding:var(--spacing-16) 0 var(--spacing-12) 0;position:relative;overflow:hidden}}
    .service-hero-content{{display:grid;grid-template-columns:2fr 1fr;gap:var(--spacing-10);align-items:center;max-width:1140px;margin:0 auto;padding:0 var(--spacing-5)}}
    /* Mobile critical styles */
    @media (max-width:767px){{.service-hero-content{{grid-template-columns:1fr;text-align:center;gap:var(--spacing-6);padding:0 var(--spacing-4)}}}}
    </style>
    
    <!-- Styles - Preload Critical CSS -->'''

def generate_performance_script(location_key, service_type):
    """Generate performance monitoring script"""
    location_data = LOCATIONS.get(location_key, {'coords': '41.0000;29.0000'})
    coords = location_data['coords'].split(';')
    lat, lon = coords[0], coords[1]
    tracking_param = f"{location_key}_{service_type}".replace('-', '_')
    
    script = '''
    <!-- Mobile Performance Monitoring - 2025 AI/LLM Ready -->
    <script>
    /* Critical performance metrics for Google & AI crawlers */
    if('serviceWorker' in navigator){navigator.serviceWorker.register('../sw.js').catch(()=>{})}
    /* Web Vitals ready for 2025 Google ranking factors */
    window.addEventListener('load',()=>{if(typeof gtag!=='undefined'){gtag('event','page_view',{page_title:document.title,page_location:location.href,custom_parameter_1:'TRACKING_PARAM'})}})
    /* Location-specific performance tracking */
    if(navigator.geolocation){navigator.geolocation.getCurrentPosition((pos)=>{if(Math.abs(pos.coords.latitude-LAT_VALUE)<0.01&&Math.abs(pos.coords.longitude-LON_VALUE)<0.01){document.body.setAttribute('data-location-verified','LOCATION_KEY-local')}})}
    </script>'''
    
    return script.replace('TRACKING_PARAM', tracking_param).replace('LAT_VALUE', lat).replace('LON_VALUE', lon).replace('LOCATION_KEY', location_key)

def generate_body_attributes(location_key, service_type):
    """Generate body attributes"""
    return f'class="region-page {location_key}-page" data-mobile-optimized="true" data-lcp-element="service-hero" data-location="{location_key}" data-service="{service_type}"'

def generate_hero_attributes(location_key, service_type):
    """Generate service hero attributes"""
    return f'class="service-hero" data-lcp-candidate="true" data-above-fold="true" data-location-context="{location_key}-{service_type}"'

def optimize_file(file_path):
    """Optimize a single HTML file"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract info from filename
        filename = os.path.basename(file_path)
        location_key = extract_location_from_filename(filename)
        service_type = get_service_type(filename)
        
        if not location_key:
            print(f"⚠️  Could not extract location from {filename}")
            return False
        
        # Extract title from existing content
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else f"{location_key.title()} Service"
        
        # Check if already optimized
        if 'Mobile Performance Monitoring - 2025 AI/LLM Ready' in content:
            print(f"✅ {filename} already optimized")
            return True
        
        # 1. Insert mobile SEO block after dns-prefetch
        mobile_seo_pattern = r'(<link rel="dns-prefetch" href="//dryallekurutemizleme\.com">\s*\n\s*<!-- Styles - Preload Critical CSS -->)'
        mobile_seo_replacement = f'<link rel="dns-prefetch" href="//dryallekurutemizleme.com">{generate_mobile_seo_block(location_key, service_type, title)}'
        
        content = re.sub(mobile_seo_pattern, mobile_seo_replacement, content, flags=re.MULTILINE)
        
        # 2. Insert performance script before </head>
        head_pattern = r'(\s*</script>\s*</head>)'
        head_replacement = f'\\1{generate_performance_script(location_key, service_type)}\n</head>'
        
        content = re.sub(head_pattern, head_replacement, content)
        
        # 3. Update body attributes
        body_pattern = r'<body class="region-page">'
        body_replacement = f'<body {generate_body_attributes(location_key, service_type)}>'
        
        content = re.sub(body_pattern, body_replacement, content)
        
        # 4. Update service-hero attributes
        hero_pattern = r'<section class="service-hero">'
        hero_replacement = f'<section {generate_hero_attributes(location_key, service_type)}>'
        
        content = re.sub(hero_pattern, hero_replacement, content)
        
        # Write optimized content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Optimized {filename} for {location_key} - {service_type}")
        return True
        
    except Exception as e:
        print(f"❌ Error optimizing {file_path}: {e}")
        return False

def main():
    """Main optimization function"""
    bolgeler_dir = Path('/Users/macos/Documents/Projeler/DryAlle/bolgeler')
    
    # Get all HTML files except already optimized ones
    html_files = [f for f in bolgeler_dir.glob('*.html') 
                  if f.name not in ['kadikoy-koltuk-yikama.html', 'acibadem-kuru-temizleme.html', 'altunizade-hali-yikama.html']]
    
    print(f"🚀 Starting bulk optimization of {len(html_files)} pages...")
    
    success_count = 0
    for file_path in html_files:
        if optimize_file(file_path):
            success_count += 1
    
    print(f"\\n🎉 COMPLETED: {success_count}/{len(html_files)} pages successfully optimized!")
    print(f"📊 Success rate: {(success_count/len(html_files)*100):.1f}%")

if __name__ == "__main__":
    main()