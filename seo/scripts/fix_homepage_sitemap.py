#!/usr/bin/env python3
"""
Fix homepage detection and add critical missing pages to sitemap
"""

import xml.etree.ElementTree as ET
from datetime import datetime

def fix_sitemap_critical_issues():
    """Add critical missing pages to sitemap"""
    
    # Parse existing sitemap
    tree = ET.parse('/Users/macos/Documents/Projeler/DryAlle/sitemap.xml')
    root = tree.getroot()
    
    # Define critical pages that must be in sitemap
    critical_pages = [
        {
            'url': 'https://dryallekurutemizleme.com/',
            'priority': '1.0',
            'changefreq': 'daily',
            'description': 'Homepage - Highest Priority'
        },
        {
            'url': 'https://dryallekurutemizleme.com/sss.html',
            'priority': '0.9',
            'changefreq': 'weekly',
            'description': 'SSS/FAQ Page'
        }
    ]
    
    # Check if critical pages exist in sitemap
    existing_urls = []
    for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc_elem is not None:
            existing_urls.append(loc_elem.text)
    
    # Add missing critical pages at the beginning
    for page in critical_pages:
        if page['url'] not in existing_urls:
            print(f"🚨 CRITICAL: Adding missing {page['description']}: {page['url']}")
            
            # Create new URL element
            url_element = ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            
            # Location
            loc = ET.SubElement(url_element, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            loc.text = page['url']
            
            # Last modification
            lastmod = ET.SubElement(url_element, '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
            lastmod.text = datetime.now().strftime('%Y-%m-%d')
            
            # Change frequency
            changefreq = ET.SubElement(url_element, '{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq')
            changefreq.text = page['changefreq']
            
            # Priority
            priority = ET.SubElement(url_element, '{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
            priority.text = page['priority']
            
            # Mobile optimization
            mobile = ET.SubElement(url_element, '{http://www.google.com/schemas/sitemap-mobile/1.0}mobile')
            
            # Insert at the beginning (highest priority pages first)
            root.insert(0, url_element)
        else:
            print(f"✅ {page['description']} already exists: {page['url']}")
    
    # Format and save
    ET.indent(tree, space="  ", level=0)
    tree.write('/Users/macos/Documents/Projeler/DryAlle/sitemap.xml', 
               encoding='utf-8', xml_declaration=True)
    
    # Validate final sitemap
    final_tree = ET.parse('/Users/macos/Documents/Projeler/DryAlle/sitemap.xml')
    final_root = final_tree.getroot()
    final_urls = final_root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url')
    
    print(f"✅ Sitemap fixed! Total URLs: {len(final_urls)}")
    
    # Verify homepage is first
    first_url = final_root.find('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if first_url is not None and first_url.text == 'https://dryallekurutemizleme.com/':
        print("✅ Homepage correctly positioned as first URL")
    else:
        print("⚠️ Homepage positioning needs verification")
    
    return len(final_urls)

if __name__ == "__main__":
    total_urls = fix_sitemap_critical_issues()
    print(f"🎯 Sitemap ready for Google Search Console: {total_urls} URLs")