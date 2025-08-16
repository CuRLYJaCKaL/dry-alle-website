#!/usr/bin/env python3
"""
DryAlle Site Inventory Extractor
Extracts SEO data from all HTML files for Phase 0.1 of SEO strategy
"""

import os
import re
import csv
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

def extract_html_content(file_path):
    """Extract SEO-relevant content from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "NO TITLE"
        
        # Extract meta description
        desc_match = re.search(r'<meta\s+name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
        meta_desc = desc_match.group(1).strip() if desc_match else "NO META DESCRIPTION"
        
        # Extract canonical URL
        canonical_match = re.search(r'<link\s+rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', content, re.IGNORECASE)
        canonical = canonical_match.group(1).strip() if canonical_match else "NO CANONICAL"
        
        # Extract H1
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        h1 = h1_match.group(1).strip() if h1_match else "NO H1"
        h1 = re.sub(r'<[^>]+>', '', h1)  # Remove HTML tags
        
        # Extract all headings for hierarchy
        headings = []
        for i in range(1, 7):
            heading_matches = re.findall(f'<h{i}[^>]*>(.*?)</h{i}>', content, re.IGNORECASE | re.DOTALL)
            for match in heading_matches:
                clean_heading = re.sub(r'<[^>]+>', '', match).strip()
                if clean_heading:
                    headings.append(f"H{i}: {clean_heading}")
        
        heading_hierarchy = " | ".join(headings[:10])  # Limit to first 10 headings
        
        # Extract image alt attributes
        img_alts = re.findall(r'<img[^>]*alt=["\']([^"\']*)["\']', content, re.IGNORECASE)
        alt_status = f"{len(img_alts)} images with alt" if img_alts else "NO ALT ATTRIBUTES"
        
        # Check robots meta
        robots_match = re.search(r'<meta\s+name=["\']robots["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
        robots_meta = robots_match.group(1).strip() if robots_match else "NO ROBOTS META"
        
        return {
            'title': title,
            'h1': h1,
            'meta_desc': meta_desc,
            'canonical': canonical,
            'heading_hierarchy': heading_hierarchy,
            'img_alts': alt_status,
            'robots_meta': robots_meta
        }
        
    except Exception as e:
        return {
            'title': f"ERROR: {str(e)}",
            'h1': "ERROR",
            'meta_desc': "ERROR", 
            'canonical': "ERROR",
            'heading_hierarchy': "ERROR",
            'img_alts': "ERROR",
            'robots_meta': "ERROR"
        }

def get_sitemap_status(sitemap_file, url):
    """Check if URL is in sitemap.xml"""
    try:
        tree = ET.parse(sitemap_file)
        root = tree.getroot()
        
        # Handle namespace
        namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        for url_elem in root.findall('.//sitemap:url', namespace):
            loc = url_elem.find('sitemap:loc', namespace)
            if loc is not None and url in loc.text:
                priority_elem = url_elem.find('sitemap:priority', namespace)
                priority = priority_elem.text if priority_elem is not None else "N/A"
                return f"YES (Priority: {priority})"
        
        return "NOT IN SITEMAP"
        
    except Exception as e:
        return f"SITEMAP ERROR: {str(e)}"

def main():
    # Base directory
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    sitemap_file = base_dir / "sitemap.xml"
    output_file = base_dir / "seo/outputs/00_inventory.csv"
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Find all HTML files
    html_files = list(base_dir.glob("**/*.html"))
    
    # Filter out component files
    html_files = [f for f in html_files if "components/" not in str(f)]
    
    # Base URL for canonical generation
    base_url = "https://dryallekurutemizleme.com"
    
    inventory_data = []
    
    print(f"Processing {len(html_files)} HTML files...")
    
    for html_file in sorted(html_files):
        relative_path = html_file.relative_to(base_dir)
        
        # Generate expected URL
        if str(relative_path) == "index.html":
            expected_url = f"{base_url}/"
        else:
            url_path = str(relative_path).replace("\\", "/")
            if url_path.endswith("index.html"):
                url_path = url_path[:-10]  # Remove "index.html"
            expected_url = f"{base_url}/{url_path}"
        
        print(f"Processing: {relative_path}")
        
        # Extract HTML content
        html_data = extract_html_content(html_file)
        
        # Check sitemap status
        sitemap_status = get_sitemap_status(sitemap_file, expected_url)
        
        # Determine page type
        if "blog/" in str(relative_path):
            if "/index.html" in str(relative_path):
                page_type = "Blog Category"
            else:
                page_type = "Blog Article"
        elif "hizmetler/" in str(relative_path):
            page_type = "Service Page"
        elif "bolgeler/" in str(relative_path):
            page_type = "Local Landing"
        elif str(relative_path) == "index.html":
            page_type = "Homepage"
        else:
            page_type = "Other"
        
        # Add to inventory
        inventory_data.append({
            'File Path': str(relative_path),
            'Expected URL': expected_url,
            'Page Type': page_type,
            'Title': html_data['title'][:100] + "..." if len(html_data['title']) > 100 else html_data['title'],
            'H1': html_data['h1'][:100] + "..." if len(html_data['h1']) > 100 else html_data['h1'],
            'Meta Description': html_data['meta_desc'][:150] + "..." if len(html_data['meta_desc']) > 150 else html_data['meta_desc'],
            'Canonical URL': html_data['canonical'],
            'Heading Hierarchy': html_data['heading_hierarchy'][:200] + "..." if len(html_data['heading_hierarchy']) > 200 else html_data['heading_hierarchy'],
            'Image Alt Status': html_data['img_alts'],
            'Robots Meta': html_data['robots_meta'],
            'Sitemap Status': sitemap_status
        })
    
    # Write CSV
    fieldnames = [
        'File Path', 'Expected URL', 'Page Type', 'Title', 'H1', 
        'Meta Description', 'Canonical URL', 'Heading Hierarchy', 
        'Image Alt Status', 'Robots Meta', 'Sitemap Status'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory_data)
    
    print(f"\nSite inventory completed!")
    print(f"Total pages analyzed: {len(inventory_data)}")
    print(f"Output saved to: {output_file}")
    
    # Summary statistics
    page_types = {}
    sitemap_issues = 0
    title_issues = 0
    h1_issues = 0
    meta_desc_issues = 0
    canonical_issues = 0
    
    for item in inventory_data:
        page_types[item['Page Type']] = page_types.get(item['Page Type'], 0) + 1
        
        if "NOT IN SITEMAP" in item['Sitemap Status']:
            sitemap_issues += 1
        if "NO TITLE" in item['Title']:
            title_issues += 1
        if "NO H1" in item['H1']:
            h1_issues += 1
        if "NO META DESCRIPTION" in item['Meta Description']:
            meta_desc_issues += 1
        if "NO CANONICAL" in item['Canonical URL']:
            canonical_issues += 1
    
    print("\n=== SUMMARY STATISTICS ===")
    print(f"Page Types:")
    for ptype, count in page_types.items():
        print(f"  {ptype}: {count}")
    
    print(f"\nSEO Issues Found:")
    print(f"  Missing from sitemap: {sitemap_issues}")
    print(f"  Missing titles: {title_issues}")
    print(f"  Missing H1: {h1_issues}")
    print(f"  Missing meta descriptions: {meta_desc_issues}")
    print(f"  Missing canonical URLs: {canonical_issues}")

if __name__ == "__main__":
    main()