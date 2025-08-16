#!/usr/bin/env python3
"""
Update sitemap.xml with blog posts for optimal SEO
"""

import xml.etree.ElementTree as ET
from datetime import datetime
import os

def update_sitemap_with_blog():
    """Add blog posts to existing sitemap.xml"""
    
    # Read existing sitemap
    tree = ET.parse('/Users/macos/Documents/Projeler/DryAlle/sitemap.xml')
    root = tree.getroot()
    
    # Blog URLs to add
    blog_urls = [
        # Main blog index
        {
            'url': 'https://dryallekurutemizleme.com/blog/',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        # Featured articles (high priority)
        {
            'url': 'https://dryallekurutemizleme.com/blog/2025-01/2025-yilinda-istanbul-kuru-temizleme-trendleri.html',
            'priority': '0.8',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://dryallekurutemizleme.com/blog/2025-01/gelinlik-temizleme-ultimate-rehber-2025.html',
            'priority': '0.8',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://dryallekurutemizleme.com/blog/2025-01/kis-aylarinda-kuru-temizleme-ipuclari.html',
            'priority': '0.8',
            'changefreq': 'monthly'
        },
        # Pillar content (highest priority for blog content)
        {
            'url': 'https://dryallekurutemizleme.com/blog/pillar-content/ultimate-turkish-dry-cleaning-guide.html',
            'priority': '0.9',
            'changefreq': 'quarterly'
        },
        {
            'url': 'https://dryallekurutemizleme.com/blog/pillar-content/istanbul-seasonal-clothing-care-calendar.html',
            'priority': '0.9',
            'changefreq': 'quarterly'
        },
        {
            'url': 'https://dryallekurutemizleme.com/blog/pillar-content/complete-home-textile-maintenance-manual.html',
            'priority': '0.9',
            'changefreq': 'quarterly'
        }
    ]
    
    # Add blog URLs to sitemap
    for blog_entry in blog_urls:
        url_element = ET.SubElement(root, 'url')
        
        loc = ET.SubElement(url_element, 'loc')
        loc.text = blog_entry['url']
        
        lastmod = ET.SubElement(url_element, 'lastmod')
        lastmod.text = datetime.now().strftime('%Y-%m-%d')
        
        changefreq = ET.SubElement(url_element, 'changefreq')
        changefreq.text = blog_entry['changefreq']
        
        priority = ET.SubElement(url_element, 'priority')
        priority.text = blog_entry['priority']
        
        # Add mobile optimization
        mobile = ET.SubElement(url_element, '{http://www.google.com/schemas/sitemap-mobile/1.0}mobile')
    
    # Format and save updated sitemap
    ET.indent(tree, space="    ", level=0)
    tree.write('/Users/macos/Documents/Projeler/DryAlle/sitemap.xml', 
               encoding='utf-8', xml_declaration=True)
    
    print("✅ Sitemap updated with blog URLs")
    print(f"📊 Added {len(blog_urls)} blog entries to sitemap")
    
    # Validate sitemap
    try:
        test_tree = ET.parse('/Users/macos/Documents/Projeler/DryAlle/sitemap.xml')
        urls = test_tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        print(f"🗺️ Total URLs in sitemap: {len(urls)}")
        print("✅ Sitemap XML validation successful")
    except ET.ParseError as e:
        print(f"❌ Sitemap validation failed: {e}")

if __name__ == "__main__":
    update_sitemap_with_blog()