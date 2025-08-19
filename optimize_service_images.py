#!/usr/bin/env python3
"""
DryAlle Service Images Optimization Script
Converts service images to WebP format for better performance
"""

import os
import requests
from PIL import Image
import shutil

def optimize_service_images():
    """
    Service images on homepage that need optimization:
    1. dry-cleaning.png
    2. carpet-cleaning.png  
    3. furniture-cleaning.png
    4. home-textile-cleaning.png
    5. fabric-leather-dyeing.png
    6. shoe-polish-service.png
    7. ironing-service.png
    8. curtain-blind-cleaning.png
    9. luggage-bag-cleaning.png
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
    optimized_dir = "/Users/macos/Documents/Projeler/DryAlle/asset/optimized"
    
    # Create optimized directory
    if not os.path.exists(optimized_dir):
        os.makedirs(optimized_dir)
        print(f"✅ Created directory: {optimized_dir}")
    
    results = []
    
    for image_name in service_images:
        original_path = os.path.join(asset_dir, image_name)
        
        if not os.path.exists(original_path):
            print(f"❌ Image not found: {original_path}")
            continue
            
        try:
            # Get original file size
            original_size = os.path.getsize(original_path)
            
            # Open and optimize image
            with Image.open(original_path) as img:
                # Convert to RGB if necessary (for WebP compatibility)
                if img.mode in ('RGBA', 'LA', 'P'):
                    # Create white background for transparency
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize to optimal dimensions (300x200 as specified in HTML)
                target_size = (300, 200)
                img = img.resize(target_size, Image.Resampling.LANCZOS)
                
                # Save as WebP with high quality
                webp_name = image_name.replace('.png', '.webp')
                webp_path = os.path.join(asset_dir, webp_name)
                
                img.save(webp_path, 'WebP', quality=85, optimize=True)
                
                # Get new file size
                new_size = os.path.getsize(webp_path)
                reduction = ((original_size - new_size) / original_size) * 100
                
                # Backup original to optimized folder
                backup_path = os.path.join(optimized_dir, image_name)
                shutil.copy2(original_path, backup_path)
                
                results.append({
                    'original': image_name,
                    'webp': webp_name,
                    'original_size': original_size,
                    'new_size': new_size,
                    'reduction': reduction
                })
                
                print(f"✅ {image_name} -> {webp_name}")
                print(f"   📊 Size reduction: {original_size:,} bytes -> {new_size:,} bytes ({reduction:.1f}% smaller)")
                
        except Exception as e:
            print(f"❌ Error processing {image_name}: {str(e)}")
    
    # Print summary
    print("\n" + "="*60)
    print("🎯 OPTIMIZATION SUMMARY")
    print("="*60)
    
    total_original = sum(r['original_size'] for r in results)
    total_new = sum(r['new_size'] for r in results)
    total_reduction = ((total_original - total_new) / total_original) * 100 if total_original > 0 else 0
    
    print(f"📈 Total images processed: {len(results)}")
    print(f"📊 Total size before: {total_original:,} bytes ({total_original/1024/1024:.2f} MB)")
    print(f"📊 Total size after: {total_new:,} bytes ({total_new/1024/1024:.2f} MB)")
    print(f"🚀 Total reduction: {total_reduction:.1f}%")
    print(f"💾 Space saved: {(total_original-total_new):,} bytes ({(total_original-total_new)/1024/1024:.2f} MB)")
    
    return results

def update_html_references():
    """Update HTML file to use WebP images"""
    
    html_file = "/Users/macos/Documents/Projeler/DryAlle/index.html"
    
    replacements = [
        ('src="asset/dry-cleaning.png"', 'src="asset/dry-cleaning.webp"'),
        ('src="asset/carpet-cleaning.png"', 'src="asset/carpet-cleaning.webp"'),
        ('src="asset/furniture-cleaning.png"', 'src="asset/furniture-cleaning.webp"'),
        ('src="asset/home-textile-cleaning.png"', 'src="asset/home-textile-cleaning.webp"'),
        ('src="asset/fabric-leather-dyeing.png"', 'src="asset/fabric-leather-dyeing.webp"'),
        ('src="asset/shoe-polish-service.png"', 'src="asset/shoe-polish-service.webp"'),
        ('src="asset/ironing-service.png"', 'src="asset/ironing-service.webp"'),
        ('src="asset/curtain-blind-cleaning.png"', 'src="asset/curtain-blind-cleaning.webp"'),
        ('src="asset/luggage-bag-cleaning.png"', 'src="asset/luggage-bag-cleaning.webp"')
    ]
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for old_ref, new_ref in replacements:
            content = content.replace(old_ref, new_ref)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated HTML references in {html_file}")
            print(f"📝 Updated {len(replacements)} image references to WebP format")
        else:
            print("ℹ️ No changes needed in HTML file")
            
    except Exception as e:
        print(f"❌ Error updating HTML file: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting DryAlle Service Images Optimization")
    print("="*60)
    
    # Check if PIL (Pillow) is available
    try:
        from PIL import Image
        print("✅ PIL (Pillow) is available")
    except ImportError:
        print("❌ PIL (Pillow) not found. Installing...")
        os.system("pip3 install Pillow")
        from PIL import Image
        print("✅ PIL (Pillow) installed successfully")
    
    # Optimize images
    results = optimize_service_images()
    
    if results:
        print(f"\n📝 Updating HTML references...")
        update_html_references()
        
        print(f"\n🎉 Optimization completed successfully!")
        print(f"💡 Next steps:")
        print(f"   1. Test the website locally to ensure images load correctly")
        print(f"   2. Commit changes to git")
        print(f"   3. Deploy to production")
        print(f"   4. Check page speed improvements")
    else:
        print("❌ No images were processed successfully")