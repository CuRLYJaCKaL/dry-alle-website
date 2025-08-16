#!/usr/bin/env python3
"""
Batch fix QA warnings across all service pages
- Add WhatsApp CTAs
- Fix image loading attributes
- Optimize CSS/font loading
"""

import os
import re
from pathlib import Path

def fix_service_page(file_path):
    """Fix QA warnings for a single service page"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Fix WhatsApp CTA in hero buttons (if not already fixed)
    if 'WhatsApp İletişim' not in content:
        # Find service-specific WhatsApp text
        service_name = Path(file_path).stem.replace('-', ' ').title()
        service_texts = {
            'canta-temizleme': 'Çanta%20temizleme%20hizmetiniz%20hakkında%20bilgi%20almak%20istiyorum',
            'ev-tekstili-temizligi': 'Ev%20tekstili%20temizliği%20hizmetiniz%20hakkında%20bilgi%20almak%20istiyorum',
            'koltuk-yikama': 'Koltuk%20yıkama%20hizmetiniz%20hakkında%20bilgi%20almak%20istiyorum',
            'kumas-deri-boyama': 'Kumaş%20ve%20deri%20boyama%20hizmetiniz%20hakkında%20bilgi%20almak%20istiyorum',
            'lostra-hizmeti': 'Lostra%20hizmetiniz%20hakkında%20bilgi%20almak%20istiyorum',
            'perde-temizleme': 'Perde%20temizleme%20hizmetiniz%20hakkında%20bilgi%20almak%20istiyorum',
            'utu-hizmetleri': 'Ütü%20hizmetleriniz%20hakkında%20bilgi%20almak%20istiyorum'
        }
        
        service_key = Path(file_path).stem
        whatsapp_text = service_texts.get(service_key, 'Hizmetleriniz%20hakkında%20bilgi%20almak%20istiyorum')
        
        # Pattern for hero buttons
        hero_buttons_pattern = r'(<div class="service-hero-buttons">\s*<a href="tel:\+905433527474" class="cta-button primary">Hemen Ara</a>\s*<a href="[^"]*" class="cta-button secondary">İletişime Geç</a>\s*</div>)'
        
        replacement = f'''<div class="service-hero-buttons">
                            <a href="tel:+905433527474" class="cta-button primary">Hemen Ara</a>
                            <a href="https://wa.me/905433527474?text={whatsapp_text}" class="cta-button secondary">WhatsApp İletişim</a>
                            <a href="../index.html#contact" class="cta-button tertiary">İletişime Geç</a>
                        </div>'''
        
        content = re.sub(hero_buttons_pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)
    
    # 2. Fix font loading (async)
    font_pattern = r'<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet">'
    
    def replace_font(match):
        original = match.group(0)
        href = re.search(r'href="([^"]*)"', original).group(1)
        return f'<link href="{href}" rel="stylesheet" media="print" onload="this.media=\'all\'">\n    <noscript><link href="{href}" rel="stylesheet"></noscript>'
    
    content = re.sub(font_pattern, replace_font, content)
    
    # 3. Fix CSS loading (async)
    css_pattern = r'<link rel="stylesheet" href="([^"]*\.css)">'
    
    def replace_css(match):
        href = match.group(1)
        return f'<link rel="stylesheet" href="{href}" media="print" onload="this.media=\'all\'">\n    <noscript><link rel="stylesheet" href="{href}"></noscript>'
    
    content = re.sub(css_pattern, replace_css, content)
    
    # 4. Fix images - add lazy loading and dimensions (except hero images)
    img_pattern = r'<img src="([^"]*)" alt="([^"]*)"(?!\s+width=)([^>]*)>'
    
    def replace_img(match):
        src = match.group(1)
        alt = match.group(2)
        rest = match.group(3)
        
        # Check if it's a hero image (usually large service images)
        if any(service in src.lower() for service in ['dry-cleaning', 'carpet-cleaning', 'furniture-cleaning']):
            if '../asset' in src and not any(x in src.lower() for x in ['icon', 'logo']):
                # Main service image - eager loading
                return f'<img src="{src}" alt="{alt}" width="400" height="300" loading="eager"{rest}>'
        
        # Related service icons/images - lazy loading
        if '../asset' in src:
            return f'<img src="{src}" alt="{alt}" width="80" height="80" loading="lazy" decoding="async"{rest}>'
        
        # Other images
        return f'<img src="{src}" alt="{alt}" loading="lazy" decoding="async"{rest}>'
    
    content = re.sub(img_pattern, replace_img, content)
    
    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed: {file_path}")
        return True
    else:
        print(f"ℹ️  No changes needed: {file_path}")
        return False

def main():
    """Process all service pages"""
    
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    hizmetler_dir = base_dir / "hizmetler"
    
    files_to_process = [
        "canta-temizleme.html",
        "ev-tekstili-temizligi.html", 
        "koltuk-yikama.html",
        "kumas-deri-boyama.html",
        "lostra-hizmeti.html",
        "perde-temizleme.html",
        "utu-hizmetleri.html"
    ]
    
    print("🔧 Starting batch QA warnings fix...")
    
    fixed_count = 0
    for filename in files_to_process:
        file_path = hizmetler_dir / filename
        if file_path.exists():
            if fix_service_page(file_path):
                fixed_count += 1
        else:
            print(f"❌ File not found: {file_path}")
    
    print(f"\n✅ Batch fix complete! Fixed {fixed_count} files.")

if __name__ == "__main__":
    main()