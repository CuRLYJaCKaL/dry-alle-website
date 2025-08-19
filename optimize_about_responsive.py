#!/usr/bin/env python3
"""
DryAlle About Us Image Responsive Optimization Script
Creates multiple responsive sizes for about-us image
"""

import os
from PIL import Image

def create_responsive_about_images():
    """
    Create responsive about-us images with multiple sizes for different devices
    """
    
    asset_dir = "/Users/macos/Documents/Projeler/DryAlle/asset"
    original_path = os.path.join(asset_dir, "about-us.png")
    
    if not os.path.exists(original_path):
        print(f"❌ About-us image not found: {original_path}")
        return None
    
    # Create backup first
    optimized_dir = os.path.join(asset_dir, "optimized")
    if not os.path.exists(optimized_dir):
        os.makedirs(optimized_dir)
    
    backup_path = os.path.join(optimized_dir, "about-us.png")
    if not os.path.exists(backup_path):
        import shutil
        shutil.copy2(original_path, backup_path)
        print(f"✅ Created backup: {backup_path}")
    
    # Define responsive sizes for about-us image
    sizes = {
        'small': (300, 225),      # Mobile devices
        'medium': (400, 300),     # Tablets  
        'large': (500, 375),      # Desktop
        'xlarge': (600, 450)      # Large screens
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
            
            print(f"🖼️ Processing About Us Image")
            print(f"📐 Original size: {img.size}")
            print(f"📊 Original file size: {original_size:,} bytes ({original_size/1024/1024:.2f} MB)")
            
            size_results = {}
            
            for size_name, (width, height) in sizes.items():
                # Resize maintaining aspect ratio
                resized_img = img.copy()
                resized_img.thumbnail((width, height), Image.Resampling.LANCZOS)
                
                # Save WebP with high quality
                webp_filename = f"about-us-{size_name}.webp"
                webp_path = os.path.join(asset_dir, webp_filename)
                
                # High quality for about-us image
                quality = 92
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
            fallback_img.thumbnail(sizes['large'], Image.Resampling.LANCZOS)
            jpg_path = os.path.join(asset_dir, "about-us.jpg")
            fallback_img.save(jpg_path, 'JPEG', quality=85, optimize=True)
            
            fallback_size = os.path.getsize(jpg_path)
            print(f"   ✅ fallback JPG: {fallback_img.size} -> {fallback_size:,} bytes")
            
            return {
                'original_size': original_size,
                'sizes': size_results,
                'fallback': 'about-us.jpg',
                'fallback_size': fallback_size
            }
            
    except Exception as e:
        print(f"❌ Error processing about-us image: {str(e)}")
        return None

def update_html_about_responsive():
    """Update HTML file with responsive about-us picture element"""
    
    html_file = "/Users/macos/Documents/Projeler/DryAlle/index.html"
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create responsive picture element for about-us
        about_picture_html = '''<picture>
    <source 
        media="(max-width: 480px)" 
        srcset="asset/about-us-small.webp" 
        type="image/webp">
    <source 
        media="(max-width: 768px)" 
        srcset="asset/about-us-medium.webp" 
        type="image/webp">
    <source 
        media="(max-width: 1200px)" 
        srcset="asset/about-us-large.webp" 
        type="image/webp">
    <source 
        srcset="asset/about-us-xlarge.webp" 
        type="image/webp">
    <img 
        src="asset/about-us.jpg" 
        alt="Dry Alle Kuru Temizleme - 25 Yıllık Deneyim İstanbul Anadolu Yakası" 
        width="400" 
        height="300" 
        loading="lazy" 
        decoding="async">
</picture>'''
        
        # Replace current about-us img tag with picture element
        import re
        about_pattern = r'<img[^>]*src="asset/about-us\.png"[^>]*>'
        if re.search(about_pattern, content):
            content = re.sub(about_pattern, about_picture_html, content)
            print(f"✅ Updated about-us image with responsive picture element")
        else:
            print("⚠️ About-us image pattern not found for replacement")
        
        # Update structured data image reference
        content = content.replace(
            '"https://dryallekurutemizleme.com/asset/about-us.png"',
            '"https://dryallekurutemizleme.com/asset/about-us-large.webp"'
        )
        
        # Write updated content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ Updated HTML file with responsive about-us image")
        
    except Exception as e:
        print(f"❌ Error updating HTML: {str(e)}")

def print_about_summary(result):
    """Print about-us optimization summary"""
    
    if not result:
        return
    
    print("\n" + "="*60)
    print("🎯 ABOUT-US IMAGE RESPONSIVE OPTIMIZATION SUMMARY")
    print("="*60)
    
    total_new = sum(s['size'] for s in result['sizes'].values()) + result['fallback_size']
    reduction = ((result['original_size'] - total_new) / result['original_size']) * 100
    
    print(f"📊 Original size: {result['original_size']:,} bytes ({result['original_size']/1024/1024:.2f} MB)")
    print(f"📊 Total new size (all variants): {total_new:,} bytes ({total_new/1024/1024:.2f} MB)")
    print(f"🚀 Total reduction: {reduction:.1f}%")
    
    print(f"\n📷 About-Us Image Variants:")
    for size_name, size_data in result['sizes'].items():
        print(f"   • {size_name}: {size_data['dimensions']} - {size_data['size']:,} bytes")
    print(f"   • fallback JPG: {result['fallback_size']:,} bytes")

if __name__ == "__main__":
    print("🚀 Starting DryAlle About-Us Image Responsive Optimization")
    print("="*60)
    
    # Create responsive about-us images
    result = create_responsive_about_images()
    
    if result:
        # Update HTML file
        update_html_about_responsive()
        
        # Print summary
        print_about_summary(result)
        
        print(f"\n🎉 About-us image responsive optimization completed!")
        print(f"💡 Benefits:")
        print(f"   • Mobile: 300×225 WebP for fast loading")
        print(f"   • Tablet: 400×300 WebP for balanced quality")
        print(f"   • Desktop: 500×375 WebP for sharp display")
        print(f"   • Large: 600×450 WebP for high-res screens")
        print(f"   • JPG fallback for compatibility")
        print(f"   • Better user experience across all devices")
    else:
        print("❌ About-us image optimization failed")