#!/usr/bin/env python3
"""
DryAlle Responsive Images Optimization Script
Creates multiple sizes with high quality for responsive design
"""

import os
from PIL import Image
import shutil

def create_responsive_images():
    """
    Create responsive images with multiple sizes and high quality
    """
    
    service_images = [
        "dry-cleaning.png",
        "carpet-cleaning.png",
        "furniture-cleaning.png", 
        "home-textile-cleaning.png",
        "fabric-leather-dyeing.png",
        "shoe-polish-service.png",
        "ironing-service.png",
        "curtain-blind-cleaning.png",
        "luggage-bag-cleaning.png"
    ]
    
    asset_dir = "/Users/macos/Documents/Projeler/DryAlle/asset"
    
    # Define responsive sizes
    sizes = {
        'small': (400, 300),    # Mobile
        'medium': (600, 450),   # Tablet 
        'large': (800, 600),    # Desktop
        'original': (1200, 900) # High-res displays
    }
    
    results = []
    
    for image_name in service_images:
        original_path = os.path.join(asset_dir, f"optimized/{image_name}")
        
        if not os.path.exists(original_path):
            print(f"❌ Original backup not found: {original_path}")
            continue
            
        try:
            # Get original file size
            original_size = os.path.getsize(original_path)
            image_base = image_name.replace('.png', '')
            
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
                
                print(f"\n🖼️ Processing: {image_name}")
                print(f"📐 Original size: {img.size}")
                
                size_results = {}
                
                for size_name, (width, height) in sizes.items():
                    # Resize maintaining aspect ratio
                    resized_img = img.copy()
                    resized_img.thumbnail((width, height), Image.Resampling.LANCZOS)
                    
                    # Save WebP with high quality (92 for better quality)
                    webp_filename = f"{image_base}-{size_name}.webp"
                    webp_path = os.path.join(asset_dir, webp_filename)
                    
                    # Higher quality for larger images
                    quality = 95 if size_name in ['large', 'original'] else 92
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
                fallback_img.thumbnail(sizes['medium'], Image.Resampling.LANCZOS)
                jpg_path = os.path.join(asset_dir, f"{image_base}.jpg")
                fallback_img.save(jpg_path, 'JPEG', quality=85, optimize=True)
                
                results.append({
                    'original': image_name,
                    'original_size': original_size,
                    'sizes': size_results,
                    'fallback': f"{image_base}.jpg"
                })
                
        except Exception as e:
            print(f"❌ Error processing {image_name}: {str(e)}")
    
    return results

def generate_html_picture_elements(results):
    """Generate HTML picture elements for responsive images"""
    
    html_snippets = []
    
    for result in results:
        image_base = result['original'].replace('.png', '')
        sizes = result['sizes']
        
        # Generate picture element
        picture_html = f"""
<picture>
    <source 
        media="(max-width: 480px)" 
        srcset="asset/{sizes['small']['filename']}" 
        type="image/webp">
    <source 
        media="(max-width: 768px)" 
        srcset="asset/{sizes['medium']['filename']}" 
        type="image/webp">
    <source 
        media="(max-width: 1200px)" 
        srcset="asset/{sizes['large']['filename']}" 
        type="image/webp">
    <source 
        srcset="asset/{sizes['original']['filename']}" 
        type="image/webp">
    <img 
        src="asset/{result['fallback']}" 
        alt="İstanbul Kuru Temizleme Hizmeti - Dry Alle" 
        width="300" 
        height="200" 
        loading="lazy" 
        decoding="async">
</picture>"""
        
        html_snippets.append({
            'original': result['original'],
            'html': picture_html
        })
    
    return html_snippets

def update_html_with_responsive_images(html_snippets):
    """Update HTML file with responsive picture elements"""
    
    html_file = "/Users/macos/Documents/Projeler/DryAlle/index.html"
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Map of current WebP files to new picture elements
        replacements = {
            'dry-cleaning.webp': html_snippets[0]['html'],
            'carpet-cleaning.webp': html_snippets[1]['html'],
            'furniture-cleaning.webp': html_snippets[2]['html'],
            'home-textile-cleaning.webp': html_snippets[3]['html'],
            'fabric-leather-dyeing.webp': html_snippets[4]['html'],
            'shoe-polish-service.webp': html_snippets[5]['html'],
            'ironing-service.webp': html_snippets[6]['html'],
            'curtain-blind-cleaning.webp': html_snippets[7]['html'],
            'luggage-bag-cleaning.webp': html_snippets[8]['html'],
        }
        
        # Replace simple img tags with picture elements
        for webp_file, picture_element in replacements.items():
            # Find the current img tag pattern
            import re
            pattern = f'<img[^>]*src="asset/{webp_file}"[^>]*>'
            if re.search(pattern, content):
                content = re.sub(pattern, picture_element.strip(), content)
                print(f"✅ Updated {webp_file} with responsive picture element")
        
        # Write updated content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ Updated HTML file with responsive images")
        
    except Exception as e:
        print(f"❌ Error updating HTML: {str(e)}")

def print_summary(results):
    """Print optimization summary"""
    
    print("\n" + "="*60)
    print("🎯 RESPONSIVE IMAGES OPTIMIZATION SUMMARY")
    print("="*60)
    
    total_original = sum(r['original_size'] for r in results)
    total_new = sum(sum(s['size'] for s in r['sizes'].values()) for r in results)
    
    print(f"📈 Images processed: {len(results)}")
    print(f"📊 Original total size: {total_original:,} bytes ({total_original/1024/1024:.2f} MB)")
    print(f"📊 New total size (all variants): {total_new:,} bytes ({total_new/1024/1024:.2f} MB)")
    
    for result in results:
        sizes = result['sizes']
        print(f"\n📷 {result['original']}:")
        for size_name, size_data in sizes.items():
            print(f"   • {size_name}: {size_data['dimensions']} - {size_data['size']:,} bytes")

if __name__ == "__main__":
    print("🚀 Starting DryAlle Responsive Images Optimization")
    print("="*60)
    
    # Create responsive images
    results = create_responsive_images()
    
    if results:
        # Generate HTML snippets
        html_snippets = generate_html_picture_elements(results)
        
        # Update HTML file
        update_html_with_responsive_images(html_snippets)
        
        # Print summary
        print_summary(results)
        
        print(f"\n🎉 Responsive images optimization completed!")
        print(f"💡 Benefits:")
        print(f"   • High quality images for all devices")
        print(f"   • Faster loading on mobile devices")
        print(f"   • WebP support with JPG fallback")
        print(f"   • SEO-optimized responsive images")
        print(f"   • Better Core Web Vitals scores")
    else:
        print("❌ No images were processed successfully")