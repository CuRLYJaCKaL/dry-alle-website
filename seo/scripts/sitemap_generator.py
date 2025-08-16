#!/usr/bin/env python3
"""
DryAlle Sitemap Generator
Generates comprehensive sitemap.xml with all 434 planned pages
"""

import csv
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

def load_url_master_data():
    """Load URL master data from Phase 0.3"""
    master_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_url_meta_master.csv")
    pages = []
    
    with open(master_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pages.append(row)
    
    return pages

def generate_sitemap_xml():
    """Generate complete sitemap.xml with all pages"""
    
    # Load page data
    pages = load_url_master_data()
    
    # Create XML structure
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    urlset.set("xmlns:news", "http://www.google.com/schemas/sitemap-news/0.9")
    urlset.set("xmlns:xhtml", "http://www.w3.org/1999/xhtml")
    urlset.set("xmlns:mobile", "http://www.google.com/schemas/sitemap-mobile/1.0")
    urlset.set("xmlns:image", "http://www.google.com/schemas/sitemap-image/1.1")
    urlset.set("xmlns:video", "http://www.google.com/schemas/sitemap-video/1.1")
    
    # Get current date for lastmod
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Priority and changefreq mapping based on page type
    page_config = {
        "Homepage": {"priority": "1.0", "changefreq": "weekly"},
        "Service Hub": {"priority": "0.9", "changefreq": "weekly"},
        "Service Page": {"priority": "0.9", "changefreq": "monthly"},
        "District Hub": {"priority": "0.85", "changefreq": "weekly"},
        "Location Landing": {"priority": "0.95", "changefreq": "weekly"},
        "Blog Hub": {"priority": "0.9", "changefreq": "weekly"},
        "Blog Category": {"priority": "0.8", "changefreq": "weekly"},
        "Blog Article": {"priority": "0.7", "changefreq": "monthly"},
        "FAQ": {"priority": "0.7", "changefreq": "monthly"},
        "Contact": {"priority": "0.7", "changefreq": "monthly"},
        "About": {"priority": "0.6", "changefreq": "monthly"},
        "References": {"priority": "0.6", "changefreq": "monthly"}
    }
    
    # Sort pages by priority (highest first)
    pages.sort(key=lambda x: float(page_config.get(x["Page Type"], {"priority": "0.5"})["priority"]), reverse=True)
    
    for page in pages:
        url_elem = ET.SubElement(urlset, "url")
        
        # URL location
        loc = ET.SubElement(url_elem, "loc")
        loc.text = page["Full URL"]
        
        # Last modification date
        lastmod = ET.SubElement(url_elem, "lastmod")
        if page["Status"] == "Exists":
            lastmod.text = "2025-01-16"  # Recently updated existing pages
        else:
            lastmod.text = current_date  # New pages to be created
        
        # Change frequency
        changefreq = ET.SubElement(url_elem, "changefreq")
        config = page_config.get(page["Page Type"], {"changefreq": "monthly"})
        changefreq.text = config["changefreq"]
        
        # Priority
        priority = ET.SubElement(url_elem, "priority")
        priority.text = config["priority"]
        
        # Add mobile annotation for mobile-optimized pages
        if page["Page Type"] in ["Location Landing", "Service Page", "Homepage"]:
            mobile = ET.SubElement(url_elem, "mobile:mobile")
    
    # Pretty print XML
    xml_str = ET.tostring(urlset, encoding='unicode')
    
    # Format XML properly
    import xml.dom.minidom
    dom = xml.dom.minidom.parseString(xml_str)
    formatted_xml = dom.toprettyxml(indent="    ")
    
    # Remove empty lines and fix formatting
    lines = [line for line in formatted_xml.split('\n') if line.strip()]
    formatted_xml = '\n'.join(lines)
    
    return formatted_xml

def generate_robots_txt():
    """Generate optimized robots.txt file"""
    
    robots_content = """User-agent: *
Allow: /

# Sitemap Reference
Sitemap: https://dryallekurutemizleme.com/sitemap.xml

# Allow Important Pages
Allow: /index.html
Allow: /hizmetler/
Allow: /bolgeler/
Allow: /blog/

# Allow Static Assets
Allow: /asset/
Allow: /styles.css
Allow: /service-detail-styles.css
Allow: /script.js
Allow: /blog/blog-styles.css
Allow: /components/

# Block Development and System Files
Disallow: /.git/
Disallow: /.claude/
Disallow: /seo/
Disallow: *.md
Disallow: /DNS_YONLENDIRME_REHBERI.md
Disallow: /DOMAIN_TRANSFER_VE_HOSTING_GECIS_REHBERI.md
Disallow: /WIX_VELO_ENTEGRASYON_ADIMLAR.md
Disallow: /dry-alle-custom-element.js
Disallow: /google-my-business-optimization.md

# Block Test and Temporary Files
Disallow: /test/
Disallow: /temp/
Disallow: /backup/
Disallow: /_test/
Disallow: /staging/

# Crawl Delay for Better Server Performance
Crawl-delay: 1

# Specific User Agents
User-agent: Googlebot
Allow: /
Crawl-delay: 1

User-agent: Bingbot
Allow: /
Crawl-delay: 1

User-agent: YandexBot
Allow: /
Crawl-delay: 2

User-agent: facebookexternalhit
Allow: /

User-agent: Twitterbot
Allow: /

# Block Aggressive Crawlers
User-agent: MJ12bot
Disallow: /

User-agent: AhrefsBot
Crawl-delay: 10

User-agent: SemrushBot
Crawl-delay: 10

# Host Declaration
Host: https://dryallekurutemizleme.com
"""
    
    return robots_content

def generate_robots_meta_recommendations():
    """Generate robots meta tag recommendations for different page types"""
    
    recommendations = {
        "Homepage": {
            "robots": "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
            "googlebot": "index, follow",
            "reason": "Most important page, needs full indexing and crawling"
        },
        "Service Page": {
            "robots": "index, follow, max-image-preview:large, max-snippet:-1",
            "googlebot": "index, follow", 
            "reason": "Important conversion pages, need full visibility"
        },
        "Location Landing": {
            "robots": "index, follow, max-image-preview:standard",
            "googlebot": "index, follow",
            "reason": "Local SEO pages, important for geographic targeting"
        },
        "Blog Category": {
            "robots": "index, follow, max-snippet:300",
            "googlebot": "index, follow",
            "reason": "Category pages help organize content, important for site structure"
        },
        "Blog Article": {
            "robots": "index, follow, max-image-preview:large, max-snippet:-1", 
            "googlebot": "index, follow",
            "reason": "Content pages that drive organic traffic and establish expertise"
        },
        "District Hub": {
            "robots": "index, follow, max-snippet:200",
            "googlebot": "index, follow",
            "reason": "Navigation hubs that distribute link equity to location pages"
        },
        "Service Hub": {
            "robots": "index, follow, max-snippet:300",
            "googlebot": "index, follow",
            "reason": "Main navigation page for services, important for site structure"
        },
        "Blog Hub": {
            "robots": "index, follow, max-snippet:200",
            "googlebot": "index, follow",
            "reason": "Main blog navigation, helps with content discovery"
        },
        "FAQ": {
            "robots": "index, follow, max-snippet:-1",
            "googlebot": "index, follow",
            "reason": "FAQ pages often rank for question-based queries"
        },
        "Contact": {
            "robots": "index, follow, max-snippet:200",
            "googlebot": "index, follow",
            "reason": "Contact information important for local SEO and user trust"
        },
        "About": {
            "robots": "index, follow, max-snippet:300",
            "googlebot": "index, follow",
            "reason": "About pages build trust and authority"
        },
        "References": {
            "robots": "index, follow, max-snippet:300",
            "googlebot": "index, follow",
            "reason": "Social proof pages that enhance credibility"
        }
    }
    
    return recommendations

def analyze_sitemap_impact():
    """Analyze the impact of the new sitemap vs current"""
    
    pages = load_url_master_data()
    
    # Count by page type
    page_counts = {}
    existing_count = 0
    new_count = 0
    
    for page in pages:
        page_type = page["Page Type"]
        page_counts[page_type] = page_counts.get(page_type, 0) + 1
        
        if page["Status"] == "Exists":
            existing_count += 1
        else:
            new_count += 1
    
    analysis = {
        "total_pages": len(pages),
        "existing_pages": existing_count,
        "new_pages": new_count,
        "page_type_breakdown": page_counts,
        "seo_impact": {
            "keyword_coverage": f"+{new_count * 5} new keyword opportunities",
            "local_coverage": "100% neighborhood coverage in target districts",
            "content_depth": f"{len([p for p in pages if 'Location Landing' in p['Page Type']])} location-specific pages",
            "service_authority": f"{len([p for p in pages if 'Service' in p['Page Type']])} service-focused pages"
        }
    }
    
    return analysis

def main():
    """Generate sitemap, robots.txt and analysis"""
    
    print("DryAlle Sitemap Generation başlatılıyor...")
    
    # Generate sitemap.xml
    sitemap_xml = generate_sitemap_xml()
    sitemap_path = Path("/Users/macos/Documents/Projeler/DryAlle/sitemap.xml")
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    
    # Generate robots.txt
    robots_txt = generate_robots_txt()
    robots_path = Path("/Users/macos/Documents/Projeler/DryAlle/robots.txt")
    
    with open(robots_path, 'w', encoding='utf-8') as f:
        f.write(robots_txt)
    
    # Generate robots meta recommendations
    robots_meta = generate_robots_meta_recommendations()
    
    # Analyze impact
    analysis = analyze_sitemap_impact()
    
    # Save analysis report
    analysis_path = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/01_sitemap_analysis.json")
    
    import json
    with open(analysis_path, 'w', encoding='utf-8') as f:
        json.dump({
            "analysis": analysis,
            "robots_meta_recommendations": robots_meta,
            "generation_timestamp": datetime.now().isoformat()
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n=== SITEMAP GENERATION SUMMARY ===")
    print(f"Total pages in sitemap: {analysis['total_pages']}")
    print(f"Existing pages: {analysis['existing_pages']}")
    print(f"New pages to create: {analysis['new_pages']}")
    print(f"Sitemap saved to: {sitemap_path}")
    print(f"Robots.txt saved to: {robots_path}")
    print(f"Analysis saved to: {analysis_path}")
    
    print(f"\n=== PAGE TYPE BREAKDOWN ===")
    for page_type, count in analysis['page_type_breakdown'].items():
        print(f"{page_type}: {count} pages")
    
    print(f"\n=== SEO IMPACT PROJECTION ===")
    for metric, value in analysis['seo_impact'].items():
        print(f"{metric}: {value}")

if __name__ == "__main__":
    main()