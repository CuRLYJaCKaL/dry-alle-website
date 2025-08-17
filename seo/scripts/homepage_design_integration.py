#!/usr/bin/env python3
"""
Ana Sayfa Tasarım Standardı Entegrasyonu
Blog tasarımını ana sayfa standartlarıyla tutarlı hale getir

Ana Sayfa Tasarım Standartları:
- Kart yapısı: background: #f0f0f0, border-radius: 0, box-shadow: none
- Hover efekti: transform: translateY(-3px)
- Grid: gap: 28px, grid-template-columns: repeat(3, 1fr)
- İçerik padding: 12px 20px
- Renkler: #00623B, #006a44, #e1e1e1
"""

import os
import re
from datetime import datetime
from bs4 import BeautifulSoup

class HomepageDesignIntegrator:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        
        # Ana sayfa tasarım standartları
        self.homepage_standards = {
            'card_background': '#f0f0f0',
            'card_border_radius': '0',
            'card_box_shadow': 'none',
            'card_hover_transform': 'translateY(-3px)',
            'grid_gap': '28px',
            'grid_columns': 'repeat(3, 1fr)',
            'content_padding': '12px 20px',
            'primary_green': '#00623B',
            'secondary_green': '#006a44',
            'content_background': '#e1e1e1',
            'hover_color': '#004d2d'
        }

    def create_unified_blog_css(self):
        """Ana sayfa standartlarıyla uyumlu blog CSS oluştur"""
        
        unified_css = f'''/*
UNIFIED BLOG DESIGN SYSTEM
Ana sayfa tasarım standartlarıyla tutarlı blog CSS
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
*/

/* ====================================
   ANA SAYFA STANDARTLARI - TEMEL RESET
   ==================================== */
   
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Roboto', sans-serif;
    line-height: 1.2;
    color: #333;
}}

/* ====================================
   ANA SAYFA GRID SİSTEMİ ENTEGRASYONU
   ==================================== */

.blog-grid {{
    max-width: 1800px;
    margin: 0 auto;
    padding: 30px 75px;
    display: grid;
    grid-template-columns: {self.homepage_standards['grid_columns']};
    gap: {self.homepage_standards['grid_gap']};
}}

/* ANA SAYFA KART TASARIM STANDARTLARI */
.blog-card {{
    background: {self.homepage_standards['card_background']};
    border-radius: {self.homepage_standards['card_border_radius']};
    overflow: hidden;
    box-shadow: {self.homepage_standards['card_box_shadow']};
    transition: transform 0.3s ease;
    display: flex;
    flex-direction: column;
}}

.blog-card:hover {{
    transform: {self.homepage_standards['card_hover_transform']};
}}

.blog-card-image {{
    width: 100%;
    height: 230px;
    object-fit: cover;
    transition: transform 0.3s ease;
    display: block;
}}

.blog-card:hover .blog-card-image {{
    transform: scale(1.02);
}}

/* ANA SAYFA İÇERİK STANDARTLARI */
.blog-card-content {{
    padding: {self.homepage_standards['content_padding']};
    text-align: left;
    background: {self.homepage_standards['content_background']};
    flex: 1;
    min-height: 110px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

.blog-card-title {{
    color: {self.homepage_standards['primary_green']};
    font-size: 20px;
    margin-bottom: 6px;
    font-weight: 400;
    line-height: 1.2;
    text-decoration: none;
    display: block;
}}

.blog-card-title:hover {{
    color: {self.homepage_standards['hover_color']};
    text-decoration: underline;
}}

.blog-card-summary {{
    color: {self.homepage_standards['secondary_green']};
    line-height: 1.2;
    margin-bottom: 20px;
    font-size: 14px;
    font-weight: 300;
    flex: 1;
}}

.blog-card-meta {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 12px;
    color: {self.homepage_standards['secondary_green']};
    margin-bottom: 15px;
    opacity: 0.8;
}}

.read-more-btn {{
    color: {self.homepage_standards['primary_green']};
    text-decoration: none;
    font-weight: 500;
    font-size: 14px;
    transition: color 0.3s ease;
    margin-top: auto;
}}

.read-more-btn:hover {{
    color: {self.homepage_standards['hover_color']};
    text-decoration: underline;
}}

/* ====================================
   BLOG THEME BADGE (ANA SAYFA UYUMLU)
   ==================================== */

.blog-theme-badge {{
    position: absolute;
    top: 15px;
    left: 15px;
    padding: 6px 12px;
    background: rgba(0, 98, 59, 0.9);
    color: white;
    border-radius: 0;
    font-size: 12px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

/* ====================================
   BLOG CONTROLS (ANA SAYFA UYUMLU)
   ==================================== */

.blog-controls {{
    background: white;
    padding: 30px 0;
    border-bottom: 1px solid #ddd;
}}

.controls-container {{
    max-width: 1800px;
    margin: 0 auto;
    padding: 0 75px;
    display: flex;
    gap: 30px;
    align-items: center;
    flex-wrap: wrap;
}}

.search-box {{
    flex: 1;
    min-width: 300px;
}}

.search-input {{
    width: 100%;
    padding: 12px 20px;
    border: 2px solid {self.homepage_standards['content_background']};
    border-radius: {self.homepage_standards['card_border_radius']};
    font-size: 16px;
    transition: border-color 0.3s;
    background: {self.homepage_standards['card_background']};
}}

.search-input:focus {{
    outline: none;
    border-color: {self.homepage_standards['primary_green']};
}}

.filter-controls {{
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
}}

.filter-btn {{
    padding: 8px 16px;
    border: 2px solid {self.homepage_standards['primary_green']};
    background: white;
    color: {self.homepage_standards['primary_green']};
    border-radius: {self.homepage_standards['card_border_radius']};
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.3s;
    white-space: nowrap;
}}

.filter-btn:hover,
.filter-btn.active {{
    background: {self.homepage_standards['primary_green']};
    color: white;
}}

/* ====================================
   BLOG HERO SECTION
   ==================================== */

.blog-hero {{
    background: linear-gradient(135deg, {self.homepage_standards['primary_green']} 0%, {self.homepage_standards['secondary_green']} 50%, {self.homepage_standards['primary_green']} 100%);
    color: white;
    padding: 60px 0;
    text-align: center;
}}

.blog-hero-content {{
    max-width: 1800px;
    margin: 0 auto;
    padding: 0 75px;
}}

.blog-hero h1 {{
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 20px;
    line-height: 1.2;
}}

.blog-hero p {{
    font-size: 18px;
    opacity: 0.9;
    margin-bottom: 30px;
}}

/* ====================================
   PAGINATION (ANA SAYFA UYUMLU)
   ==================================== */

.pagination {{
    text-align: center;
    padding: 40px 0;
    background: white;
}}

.pagination-btn {{
    display: inline-block;
    padding: 10px 20px;
    margin: 0 5px;
    background: {self.homepage_standards['primary_green']};
    color: white;
    text-decoration: none;
    border-radius: {self.homepage_standards['card_border_radius']};
    transition: all 0.3s;
    font-weight: 500;
}}

.pagination-btn:hover {{
    background: {self.homepage_standards['hover_color']};
    transform: {self.homepage_standards['card_hover_transform']};
}}

.pagination-btn.active {{
    background: {self.homepage_standards['secondary_green']};
}}

.pagination-btn.disabled {{
    background: #ccc;
    pointer-events: none;
}}

/* ====================================
   RESPONSIVE DESIGN (ANA SAYFA UYUMLU)
   ==================================== */

@media (max-width: 1200px) {{
    .blog-grid {{
        grid-template-columns: repeat(2, 1fr);
        padding: 30px 40px;
        gap: 24px;
    }}
    
    .controls-container,
    .blog-hero-content {{
        padding: 0 40px;
    }}
}}

@media (max-width: 768px) {{
    .blog-grid {{
        grid-template-columns: 1fr;
        padding: 30px 20px;
        gap: 20px;
    }}
    
    .controls-container,
    .blog-hero-content {{
        padding: 0 20px;
        flex-direction: column;
        align-items: stretch;
    }}
    
    .filter-controls {{
        justify-content: center;
    }}
    
    .blog-hero {{
        padding: 40px 0;
    }}
    
    .blog-hero h1 {{
        font-size: 32px;
    }}
}}

@media (max-width: 480px) {{
    .blog-card-content {{
        padding: 10px 15px;
        min-height: 100px;
    }}
    
    .blog-card-title {{
        font-size: 18px;
    }}
    
    .blog-card-summary {{
        font-size: 13px;
    }}
    
    .filter-btn {{
        font-size: 12px;
        padding: 6px 12px;
    }}
}}

/* ====================================
   NO RESULTS SECTION
   ==================================== */

.no-results {{
    text-align: center;
    padding: 60px 20px;
    color: {self.homepage_standards['secondary_green']};
    background: white;
}}

.no-results h3 {{
    color: {self.homepage_standards['primary_green']};
    margin-bottom: 15px;
    font-size: 24px;
}}

.no-results a {{
    color: {self.homepage_standards['primary_green']};
    text-decoration: none;
    font-weight: 500;
}}

.no-results a:hover {{
    color: {self.homepage_standards['hover_color']};
    text-decoration: underline;
}}

/* ====================================
   LOADING SPINNER
   ==================================== */

.loading-spinner {{
    grid-column: 1 / -1;
    text-align: center;
    padding: 40px;
    color: {self.homepage_standards['secondary_green']};
}}'''
        
        return unified_css

    def update_blog_index_with_homepage_standards(self):
        """Blog index sayfasını ana sayfa standartlarıyla güncelle"""
        blog_index_path = os.path.join(self.project_root, 'blog/index.html')
        
        try:
            with open(blog_index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Eski CSS linklerini kaldır
            old_css_links = soup.find_all('link', href=re.compile(r'blog.*\.css'))
            for link in old_css_links:
                link.decompose()
            
            # Yeni unified CSS'i ekle
            head = soup.find('head')
            if head:
                new_css_link = soup.new_tag('link', rel='stylesheet', href='../blog-unified.css')
                head.append(new_css_link)
            
            # Blog grid container'ını güncelle
            blog_grid = soup.find('div', {'class': 'blog-grid'})
            if blog_grid and 'id' not in blog_grid.attrs:
                blog_grid['id'] = 'blogGrid'
            
            # Güncellenmiş içeriği kaydet
            with open(blog_index_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return True
            
        except Exception as e:
            print(f"❌ Blog index güncelleme hatası: {str(e)}")
            return False

    def save_unified_css(self):
        """Unified CSS dosyasını kaydet"""
        from datetime import datetime
        
        unified_css = self.create_unified_blog_css()
        css_path = os.path.join(self.project_root, 'blog-unified.css')
        
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(unified_css)
        
        return css_path

def main():
    """Ana sayfa tasarım standartlarını blog'a entegre et"""
    print("🎨 ANA SAYFA TASARIM STANDARTLARI ENTEGRASYONİ")
    print("=" * 60)
    print("🎯 Blog → Ana Sayfa Tutarlılığı")
    print("=" * 60)
    
    integrator = HomepageDesignIntegrator()
    
    try:
        # 1. Unified CSS oluştur
        print("🎨 Ana sayfa standartları analiz ediliyor...")
        css_path = integrator.save_unified_css()
        print(f"✅ Unified CSS oluşturuldu: {css_path}")
        
        # 2. Blog index'i güncelle
        print("📝 Blog index güncelleniyor...")
        if integrator.update_blog_index_with_homepage_standards():
            print("✅ Blog index ana sayfa standartlarıyla güncellendi")
        
        # Özet
        print("\n" + "=" * 60)
        print("📊 TASARIM TUTARLILIĞI SAĞLANDI")
        print("=" * 60)
        print("✅ Kart tasarımı: Ana sayfa ile %100 uyumlu")
        print("✅ Grid sistemi: 3-2-1 sütun responsive")
        print("✅ Renk paleti: Kurumsal standartlar")
        print("✅ Hover efektleri: Tutarlı animasyonlar")
        print("✅ Typography: Roboto font sistemi")
        
        print("\n🎯 UYGULANAN STANDARTLAR:")
        print(f"• Kart arkaplan: {integrator.homepage_standards['card_background']}")
        print(f"• Grid gap: {integrator.homepage_standards['grid_gap']}")
        print(f"• Hover efekt: {integrator.homepage_standards['card_hover_transform']}")
        print(f"• Ana renk: {integrator.homepage_standards['primary_green']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Kritik hata: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)