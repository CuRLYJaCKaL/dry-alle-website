#!/usr/bin/env python3
"""
DryAlle Internal Linking Audit & Optimization
Analyzes internal link structure and provides optimization recommendations
"""

import os
import re
from pathlib import Path
import json
from urllib.parse import urlparse, urljoin, unquote
# import networkx as nx  # Simplified version without network analysis

def scan_html_files():
    """Scan all HTML files and extract internal links"""
    
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    html_files = list(base_dir.glob("**/*.html"))
    
    # Exclude component files and test files
    html_files = [f for f in html_files if "components/" not in str(f) and "test/" not in str(f)]
    
    pages_data = []
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract page info
            page_url = str(html_file.relative_to(base_dir))
            if page_url == "index.html":
                page_url = "/"
            else:
                page_url = "/" + page_url
            
            # Extract title
            title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            title = title_match.group(1).strip() if title_match else "No title"
            
            # Extract H1
            h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            h1 = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else "No H1"
            
            # Extract meta description
            meta_desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
            meta_desc = meta_desc_match.group(1) if meta_desc_match else "No meta description"
            
            # Extract all internal links
            internal_links = extract_internal_links(content, page_url)
            
            # Categorize page type
            page_type = categorize_page_type(page_url, title, h1)
            
            pages_data.append({
                "url": page_url,
                "file_path": str(html_file.relative_to(base_dir)),
                "title": title,
                "h1": h1,
                "meta_description": meta_desc,
                "page_type": page_type,
                "internal_links": internal_links,
                "link_count": len(internal_links),
                "issues": identify_linking_issues(internal_links, page_type)
            })
            
        except Exception as e:
            print(f"Error scanning {html_file}: {e}")
    
    return pages_data

def extract_internal_links(content, current_page_url):
    """Extract all internal links from HTML content"""
    
    links = []
    
    # Find all <a> tags with href
    link_pattern = r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>'
    link_matches = re.findall(link_pattern, content, re.IGNORECASE | re.DOTALL)
    
    for href, anchor_text in link_matches:
        # Clean anchor text
        clean_anchor = re.sub(r'<[^>]+>', '', anchor_text).strip()
        
        # Skip external links, mailto, tel, javascript
        if (href.startswith('http') or 
            href.startswith('mailto:') or 
            href.startswith('tel:') or 
            href.startswith('javascript:') or
            href.startswith('#')):
            continue
        
        # Normalize internal URLs
        if href.startswith('/'):
            normalized_url = href
        elif href.startswith('./'):
            normalized_url = href[1:]  # Remove the dot
        elif href == "index.html":
            normalized_url = "/"
        elif href.endswith('.html'):
            normalized_url = "/" + href
        else:
            normalized_url = "/" + href if not href.startswith('/') else href
        
        # Skip self-links
        if normalized_url == current_page_url:
            continue
        
        links.append({
            "target_url": normalized_url,
            "anchor_text": clean_anchor,
            "raw_href": href,
            "is_contextual": is_contextual_link(clean_anchor),
            "anchor_optimization": analyze_anchor_text(clean_anchor, normalized_url)
        })
    
    return links

def categorize_page_type(url, title, h1):
    """Categorize page type based on URL and content"""
    
    if url == "/" or "index.html" in url:
        return "Homepage"
    elif "/hizmetler/" in url and url.count('/') == 2:
        return "Service Hub"
    elif "/hizmetler/" in url and url.count('/') > 2:
        return "Service Page"
    elif "/bolgeler/" in url and url.count('/') == 2:
        return "District Hub"
    elif "/bolgeler/" in url and url.count('/') > 2:
        return "Location Landing"
    elif "/blog/" in url and url.count('/') == 2:
        return "Blog Hub"
    elif "/blog/kategori/" in url:
        return "Blog Category"
    elif "/blog/" in url and url.count('/') > 2:
        return "Blog Article"
    elif "hakkimizda" in url or "about" in url:
        return "About"
    elif "iletisim" in url or "contact" in url:
        return "Contact"
    elif "referanslar" in url or "references" in url:
        return "References"
    elif "sss" in url or "faq" in url:
        return "FAQ"
    else:
        return "Other"

def is_contextual_link(anchor_text):
    """Check if link is contextual (descriptive) vs navigational"""
    
    # Navigational phrases
    nav_phrases = [
        "devamını oku", "detay", "daha fazla", "tümünü gör", "more", "read more",
        "burada", "buraya tıklayın", "click here", "link", "bağlantı"
    ]
    
    anchor_lower = anchor_text.lower()
    return not any(phrase in anchor_lower for phrase in nav_phrases)

def analyze_anchor_text(anchor_text, target_url):
    """Analyze anchor text quality and provide optimization suggestions"""
    
    issues = []
    suggestions = []
    
    # Check for generic anchor text
    generic_terms = ["buraya tıklayın", "tıklayın", "devamını oku", "detay", "daha fazla", 
                    "click here", "read more", "more", "link"]
    
    if anchor_text.lower() in generic_terms:
        issues.append("Generic anchor text")
        suggestions.append("Use descriptive, keyword-rich anchor text")
    
    # Check anchor text length
    if len(anchor_text) < 3:
        issues.append("Anchor text too short")
        suggestions.append("Use more descriptive anchor text (3+ words)")
    
    if len(anchor_text) > 100:
        issues.append("Anchor text too long")
        suggestions.append("Shorten anchor text to <100 characters")
    
    # Suggest keyword-optimized anchor text based on target URL
    if "/hizmetler/" in target_url:
        if "kuru-temizleme" in target_url:
            suggestions.append("Suggested: 'İstanbul Kuru Temizleme Hizmeti'")
        elif "hali-yikama" in target_url:
            suggestions.append("Suggested: 'Kadıköy Halı Yıkama Hizmeti'")
        elif "koltuk-yikama" in target_url:
            suggestions.append("Suggested: 'Ataşehir Koltuk Yıkama Hizmeti'")
    
    return {
        "issues": issues,
        "suggestions": suggestions,
        "quality_score": calculate_anchor_quality(anchor_text, issues)
    }

def calculate_anchor_quality(anchor_text, issues):
    """Calculate anchor text quality score (0-100)"""
    
    score = 100
    
    # Deduct points for issues
    if "Generic anchor text" in issues:
        score -= 40
    if "Anchor text too short" in issues:
        score -= 20
    if "Anchor text too long" in issues:
        score -= 10
    
    # Bonus for keyword inclusion
    keywords = ["temizleme", "yıkama", "İstanbul", "Kadıköy", "Ataşehir", "hizmet"]
    anchor_lower = anchor_text.lower()
    
    for keyword in keywords:
        if keyword.lower() in anchor_lower:
            score += 5
    
    return max(0, min(100, score))

def identify_linking_issues(internal_links, page_type):
    """Identify internal linking issues for the page"""
    
    issues = []
    
    # Check for orphan pages (no internal links)
    if len(internal_links) == 0:
        issues.append("Orphan page - no internal links")
    
    # Check for pages with too few internal links
    if page_type in ["Homepage", "Service Hub", "District Hub"] and len(internal_links) < 10:
        issues.append(f"Hub page with too few internal links ({len(internal_links)})")
    
    # Check for pages with too many internal links
    if len(internal_links) > 100:
        issues.append(f"Too many internal links ({len(internal_links)}) - may dilute link equity")
    
    # Check for generic anchor text usage
    generic_count = sum(1 for link in internal_links if not link["is_contextual"])
    if generic_count > len(internal_links) * 0.3:  # More than 30% generic
        issues.append(f"High generic anchor text usage ({generic_count}/{len(internal_links)})")
    
    return issues

def analyze_link_distribution():
    """Analyze how link equity is distributed across the site"""
    
    pages = scan_html_files()
    
    # Create simple link analysis without networkx
    in_degree = {}
    out_degree = {}
    all_urls = [p["url"] for p in pages]
    
    # Initialize counters
    for page in pages:
        in_degree[page["url"]] = 0
        out_degree[page["url"]] = page["link_count"]
    
    # Count incoming links for each page
    for page in pages:
        for link in page["internal_links"]:
            if link["target_url"] in all_urls:
                in_degree[link["target_url"]] += 1
    
    # Find pages with linking issues
    orphan_pages = [url for url, degree in in_degree.items() if degree == 0]
    over_linked_pages = [url for url, degree in out_degree.items() if degree > 100]
    
    # Calculate total internal links
    total_links = sum(len(page["internal_links"]) for page in pages)
    
    return {
        "in_degree": in_degree,
        "out_degree": out_degree,
        "orphan_pages": orphan_pages,
        "over_linked_pages": over_linked_pages,
        "total_internal_links": total_links
    }

def generate_linking_recommendations():
    """Generate specific internal linking recommendations"""
    
    pages = scan_html_files()
    
    recommendations = {
        "priority_links_to_add": [],
        "anchor_text_improvements": [],
        "link_equity_optimization": [],
        "site_structure_improvements": []
    }
    
    # Identify important pages that need more internal links
    important_pages = [p for p in pages if p["page_type"] in ["Service Page", "Location Landing"]]
    hub_pages = [p for p in pages if p["page_type"] in ["Homepage", "Service Hub", "District Hub"]]
    
    # Recommend links from hub pages to important pages
    for hub in hub_pages:
        for important in important_pages:
            # Check if link already exists
            existing_link = any(link["target_url"] == important["url"] for link in hub["internal_links"])
            
            if not existing_link:
                recommendations["priority_links_to_add"].append({
                    "from_page": hub["url"],
                    "to_page": important["url"],
                    "suggested_anchor": generate_optimized_anchor(important["page_type"], important["url"]),
                    "reason": f"Link from {hub['page_type']} to {important['page_type']} for better navigation",
                    "priority": "High"
                })
    
    # Recommend anchor text improvements
    for page in pages:
        for link in page["internal_links"]:
            if link["anchor_optimization"]["issues"]:
                recommendations["anchor_text_improvements"].append({
                    "page": page["url"],
                    "current_anchor": link["anchor_text"],
                    "target_url": link["target_url"],
                    "issues": link["anchor_optimization"]["issues"],
                    "suggestions": link["anchor_optimization"]["suggestions"]
                })
    
    return recommendations

def generate_optimized_anchor(page_type, url):
    """Generate SEO-optimized anchor text based on page type and URL"""
    
    if page_type == "Service Page":
        if "kuru-temizleme" in url:
            return "İstanbul Kuru Temizleme Hizmeti"
        elif "hali-yikama" in url:
            return "Kadıköy Halı Yıkama Hizmeti"
        elif "koltuk-yikama" in url:
            return "Ataşehir Koltuk Yıkama Hizmeti"
        elif "perde-temizleme" in url:
            return "İstanbul Perde Temizleme Hizmeti"
        elif "canta-temizleme" in url:
            return "Çanta Temizleme Hizmeti"
        elif "lostra-hizmeti" in url:
            return "Ayakkabı Lostra Hizmeti"
        elif "utu-hizmetleri" in url:
            return "Profesyonel Ütü Hizmeti"
        elif "ev-tekstili-temizligi" in url:
            return "Ev Tekstili Temizleme"
        elif "kumas-deri-boyama" in url:
            return "Kumaş Deri Boyama Hizmeti"
    
    elif page_type == "Location Landing":
        # Extract neighborhood name from URL
        if "/kadikoy/" in url:
            return f"Kadıköy Kuru Temizleme"
        elif "/atasehir/" in url:
            return f"Ataşehir Kuru Temizleme"
        elif "/maltepe/" in url:
            return f"Maltepe Kuru Temizleme"
    
    elif page_type == "Blog Article":
        return "Blog Yazısı"  # This should be customized based on article title
    
    return "Detaylı Bilgi"  # Fallback

def main():
    """Run comprehensive internal linking audit"""
    
    print("DryAlle Internal Linking Audit başlatılıyor...")
    
    # Scan all pages and extract linking data
    pages_data = scan_html_files()
    
    # Analyze link distribution and equity
    link_analysis = analyze_link_distribution()
    
    # Generate optimization recommendations
    recommendations = generate_linking_recommendations()
    
    # Compile comprehensive audit results
    audit_results = {
        "timestamp": "2025-01-16",
        "summary": {
            "total_pages_scanned": len(pages_data),
            "total_internal_links": sum(page["link_count"] for page in pages_data),
            "average_links_per_page": round(sum(page["link_count"] for page in pages_data) / len(pages_data), 2),
            "pages_with_issues": len([page for page in pages_data if page["issues"]]),
            "orphan_pages": len(link_analysis["orphan_pages"]),
            "over_linked_pages": len(link_analysis["over_linked_pages"])
        },
        "pages_data": pages_data,
        "link_distribution": link_analysis,
        "recommendations": recommendations,
        "optimization_priorities": {
            "high_priority": len(recommendations["priority_links_to_add"]),
            "anchor_improvements": len(recommendations["anchor_text_improvements"]),
            "structural_improvements": len(recommendations["site_structure_improvements"])
        }
    }
    
    # Save results
    output_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/01_internal_linking_audit.json")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(audit_results, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print(f"\n=== INTERNAL LINKING AUDIT SUMMARY ===")
    print(f"Pages scanned: {audit_results['summary']['total_pages_scanned']}")
    print(f"Total internal links: {audit_results['summary']['total_internal_links']}")
    print(f"Average links per page: {audit_results['summary']['average_links_per_page']}")
    print(f"Pages with issues: {audit_results['summary']['pages_with_issues']}")
    print(f"Orphan pages: {audit_results['summary']['orphan_pages']}")
    print(f"Over-linked pages: {audit_results['summary']['over_linked_pages']}")
    
    print(f"\n=== OPTIMIZATION OPPORTUNITIES ===")
    print(f"High priority links to add: {audit_results['optimization_priorities']['high_priority']}")
    print(f"Anchor text improvements: {audit_results['optimization_priorities']['anchor_improvements']}")
    
    print(f"\nResults saved to: {output_file}")
    
    # Print top issues
    print(f"\n=== TOP ISSUES ===")
    for page in pages_data[:5]:  # Top 5 pages with most issues
        if page["issues"]:
            print(f"📄 {page['url']}: {', '.join(page['issues'])}")

if __name__ == "__main__":
    main()