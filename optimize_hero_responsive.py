#!/usr/bin/env python3
"""
DryAlle Hero Image Responsive Optimization Script
Creates multiple responsive sizes for hero image
"""

import os
from PIL import Image

def create_responsive_hero_images():
    """
    Create responsive hero images with multiple sizes for different devices
    """
    
    asset_dir = "/Users/macos/Documents/Projeler/DryAlle/asset"
    original_path = os.path.join(asset_dir, "optimized/hero-image.png")
    
    if not os.path.exists(original_path):
        print(f"❌ Original hero image backup not found: {original_path}")
        return None
    
    # Define responsive sizes for hero image
    sizes = {
        'mobile': (800, 450),     # Mobile devices
        'tablet': (1024, 576),    # Tablets
        'desktop': (1200, 674),   # Desktop
        'large': (1600, 900),     # Large screens
        'xlarge': (1920, 1080)    # Extra large/4K
    }
    
    try:
        original_size = os.path.getsize(original_path)
        
        with Image.open(original_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            print(f"🖼️ Processing Hero Image")
            print(f"📐 Original size: {img.size}")
            print(f"📊 Original file size: {original_size:,} bytes ({original_size/1024/1024:.2f} MB)")
            
            size_results = {}
            
            for size_name, (width, height) in sizes.items():
                # Resize maintaining aspect ratio
                resized_img = img.copy()
                resized_img.thumbnail((width, height), Image.Resampling.LANCZOS)
                
                # Save WebP with high quality (95 for hero image)
                webp_filename = f"hero-image-{size_name}.webp"
                webp_path = os.path.join(asset_dir, webp_filename)
                
                # Very high quality for hero image
                quality = 95
                resized_img.save(webp_path, 'WebP', quality=quality, optimize=True)
                
                new_size = os.path.getsize(webp_path)
                size_results[size_name] = {
                    'filename': webp_filename,
                    'size': new_size,
                    'dimensions': resized_img.size
                }
                
                print(f"   ✅ {size_name}: {resized_img.size} -> {new_size:,} bytes")
            
            # Create fallback JPG for older browsers
            fallback_img = img.copy()
            fallback_img.thumbnail(sizes['desktop'], Image.Resampling.LANCZOS)
            jpg_path = os.path.join(asset_dir, "hero-image.jpg")
            fallback_img.save(jpg_path, 'JPEG', quality=90, optimize=True)
            
            fallback_size = os.path.getsize(jpg_path)
            print(f"   ✅ fallback JPG: {fallback_img.size} -> {fallback_size:,} bytes")
            
            return {
                'original_size': original_size,
                'sizes': size_results,
                'fallback': 'hero-image.jpg',
                'fallback_size': fallback_size
            }
            
    except Exception as e:
        print(f"❌ Error processing hero image: {str(e)}")
        return None

def update_html_hero_responsive():
    """Update HTML file with responsive hero picture element"""
    
    html_file = "/Users/macos/Documents/Projeler/DryAlle/index.html"
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create responsive picture element for hero
        hero_picture_html = '''<picture>
    <source 
        media="(max-width: 480px)" 
        srcset="asset/hero-image-mobile.webp" 
        type="image/webp">
    <source 
        media="(max-width: 768px)" 
        srcset="asset/hero-image-tablet.webp" 
        type="image/webp">
    <source 
        media="(max-width: 1200px)" 
        srcset="asset/hero-image-desktop.webp" 
        type="image/webp">
    <source 
        media="(max-width: 1600px)" 
        srcset="asset/hero-image-large.webp" 
        type="image/webp">
    <source 
        srcset="asset/hero-image-xlarge.webp" 
        type="image/webp">
    <img 
        src="asset/hero-image.jpg" 
        alt="İstanbul Anadolu Yakası Kuru Temizleme Hizmeti - Dry Alle" 
        class="hero-image critical-image" 
        width="800" 
        height="600" 
        style="object-fit: cover; max-width: 1200px; height: 600px;" 
        fetchpriority="high" 
        loading="eager" 
        decoding="async">
</picture>'''
        
        # Replace current hero img tag with picture element
        import re
        hero_pattern = r'<img[^>]*src="asset/hero-image\.webp"[^>]*>'
        if re.search(hero_pattern, content):
            content = re.sub(hero_pattern, hero_picture_html, content)
            print(f"✅ Updated hero image with responsive picture element")
        else:
            print("⚠️ Hero image pattern not found for replacement")
        
        # Update preload reference to use the most appropriate size
        content = content.replace(
            'href="asset/hero-image.webp"',
            'href="asset/hero-image-desktop.webp"'
        )
        
        # Write updated content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ Updated HTML file with responsive hero image")
        
    except Exception as e:
        print(f"❌ Error updating HTML: {str(e)}")

def print_hero_summary(result):
    """Print hero optimization summary"""
    
    if not result:
        return
    
    print("\n" + "="*60)
    print("🎯 HERO IMAGE RESPONSIVE OPTIMIZATION SUMMARY")
    print("="*60)
    
    total_new = sum(s['size'] for s in result['sizes'].values()) + result['fallback_size']
    
    print(f"📊 Original size: {result['original_size']:,} bytes ({result['original_size']/1024/1024:.2f} MB)")
    print(f"📊 Total new size (all variants): {total_new:,} bytes ({total_new/1024/1024:.2f} MB)")
    
    print(f"\n📷 Hero Image Variants:")
    for size_name, size_data in result['sizes'].items():
        print(f"   • {size_name}: {size_data['dimensions']} - {size_data['size']:,} bytes")
    print(f"   • fallback JPG: {result['fallback_size']:,} bytes")

if __name__ == "__main__":
    print("🚀 Starting DryAlle Hero Image Responsive Optimization")
    print("="*60)
    
    # Create responsive hero images
    result = create_responsive_hero_images()
    
    if result:
        # Update HTML file
        update_html_hero_responsive()
        
        # Print summary
        print_hero_summary(result)
        
        print(f"\n🎉 Hero image responsive optimization completed!")
        print(f"💡 Benefits:")
        print(f"   • Optimized loading for all screen sizes")
        print(f"   • Mobile: 800x450 WebP (~100KB)")
        print(f"   • Tablet: 1024x576 WebP (~150KB)")
        print(f"   • Desktop: 1200x674 WebP (~200KB)")
        print(f"   • Large: 1600x900 WebP (~350KB)")
        print(f"   • XLarge: 1920x1080 WebP (~500KB)")
        print(f"   • JPG fallback for compatibility")
    else:
        print("❌ Hero image optimization failed")