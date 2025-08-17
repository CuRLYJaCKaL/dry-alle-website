#!/usr/bin/env python3
"""
GitHub Actions için Sitemap Otomasyonu
Bu script GitHub Actions workflow'unda çalışır
"""

import sys
import os

# Proje kök dizinini bul
project_root = os.getcwd()
sys.path.append(os.path.join(project_root, 'seo/scripts'))

try:
    from automated_sitemap_integration import AutomatedSitemapManager
    
    def main():
        manager = AutomatedSitemapManager(project_root)
        
        # Blog durumunu kontrol et
        published_blogs = manager.detect_published_blogs()
        print(f"📊 {len(published_blogs)} yayınlanmış blog tespit edildi")
        
        # Site sayfalarını tespit et
        site_pages = manager.detect_all_site_pages()
        print(f"📊 {len(site_pages)} site sayfası tespit edildi")
        
        # Sitemap oluştur
        sitemap_tree = manager.create_comprehensive_sitemap(site_pages, published_blogs)
        
        # Doğrula
        is_valid = manager.validate_sitemap_xml(sitemap_tree)
        if not is_valid:
            print("❌ Sitemap doğrulama başarısız")
            return False
        
        # Kaydet
        sitemap_path = manager.save_sitemap(sitemap_tree)
        print(f"✅ Sitemap güncellendi: {sitemap_path}")
        
        return True
    
    if __name__ == "__main__":
        success = main()
        exit(0 if success else 1)

except ImportError as e:
    print(f"❌ Import hatası: {e}")
    exit(1)
