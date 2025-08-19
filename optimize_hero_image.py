#!/usr/bin/env python3
"""
DryAlle Hero Image Optimization Script
Optimizes the main hero image for better performance
"""

import os
from PIL import Image
import shutil

def optimize_hero_image():
    """
    Optimize the hero image (hero-image.png) for web performance
    """
    
    asset_dir = "/Users/macos/Documents/Projeler/DryAlle/asset"
    hero_image = "hero-image.png"
    original_path = os.path.join(asset_dir, hero_image)
    
    if not os.path.exists(original_path):
        print(f"❌ Hero image not found: {original_path}")
        return
    
    try:
        # Get original file size
        original_size = os.path.getsize(original_path)
        print(f"📊 Original hero image size: {original_size:,} bytes ({original_size/1024/1024:.2f} MB)")
        
        # Open and optimize image
        with Image.open(original_path) as img:
            print(f"📐 Original dimensions: {img.size}")
            
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background for transparency
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize to optimal dimensions for hero section (max 1200x800)
            # Maintain aspect ratio
            max_width = 1200
            max_height = 800
            
            # Calculate new size maintaining aspect ratio
            ratio = min(max_width/img.width, max_height/img.height)
            if ratio < 1:  # Only resize if image is larger
                new_width = int(img.width * ratio)
                new_height = int(img.height * ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                print(f"📐 Resized to: {img.size}")
            
            # Save as WebP with high quality
            webp_path = os.path.join(asset_dir, "hero-image.webp")
            img.save(webp_path, 'WebP', quality=85, optimize=True)
            
            # Get new file size
            new_size = os.path.getsize(webp_path)
            reduction = ((original_size - new_size) / original_size) * 100
            
            print(f"✅ {hero_image} -> hero-image.webp")
            print(f"📊 Size reduction: {original_size:,} bytes -> {new_size:,} bytes ({reduction:.1f}% smaller)")
            print(f"💾 Space saved: {(original_size-new_size):,} bytes ({(original_size-new_size)/1024/1024:.2f} MB)")
            
            return {
                'original_size': original_size,
                'new_size': new_size,
                'reduction': reduction
            }
            
    except Exception as e:
        print(f"❌ Error processing hero image: {str(e)}")
        return None

def update_html_hero_reference():
    """Update HTML file to use WebP hero image"""
    
    html_file = "/Users/macos/Documents/Projeler/DryAlle/index.html"
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace hero image reference
        old_ref = 'src="asset/hero-image.png"'
        new_ref = 'src="asset/hero-image.webp"'
        content = content.replace(old_ref, new_ref)
        
        # Also update preload reference if exists
        old_preload = 'href="asset/hero-image.png"'
        new_preload = 'href="asset/hero-image.webp"'
        content = content.replace(old_preload, new_preload)
        
        # Update og:image and other meta references
        old_og = 'content="https://dryallekurutemizleme.com/asset/hero-image.png"'
        new_og = 'content="https://dryallekurutemizleme.com/asset/hero-image.webp"'
        content = content.replace(old_og, new_og)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated hero image references in {html_file}")
        else:
            print("ℹ️ No hero image references found to update")
            
    except Exception as e:
        print(f"❌ Error updating HTML file: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting DryAlle Hero Image Optimization")
    print("="*60)
    
    # Optimize hero image
    result = optimize_hero_image()
    
    if result:
        print(f"\n📝 Updating HTML references...")
        update_html_hero_reference()
        
        print(f"\n🎉 Hero image optimization completed successfully!")
        print(f"💡 Next steps:")
        print(f"   1. Test the website locally to ensure hero image loads correctly")
        print(f"   2. Commit changes to git")
        print(f"   3. Deploy to production")
    else:
        print("❌ Hero image optimization failed")