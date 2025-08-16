#!/usr/bin/env python3
"""
DryAlle On-Page Content Audit
Analyzes all 434 pages for title, H1, meta description optimization
"""

import csv
import re
from pathlib import Path
import json

def load_url_master_data():
    """Load URL master data from Phase 0.3"""
    master_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_url_meta_master.csv")
    pages = []
    
    with open(master_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pages.append(row)
    
    return pages

def analyze_title_tag(title, page_type, district, neighborhood, service):
    """Analyze title tag for SEO optimization"""
    
    issues = []
    score = 100
    recommendations = []
    
    # Title length check
    if len(title) < 30:
        issues.append("Title too short (<30 chars)")
        score -= 20
    elif len(title) > 60:
        issues.append("Title too long (>60 chars)")
        score -= 15
    
    # Required keywords check
    required_keywords = {
        "Homepage": ["kuru temizleme", "halı yıkama", "istanbul"],
        "Service Page": ["istanbul", service.lower() if service else ""],
        "Location Landing": ["istanbul", district.lower() if district else "", service.lower() if service else ""],
        "District Hub": ["istanbul", district.lower() if district else ""],
        "Service Hub": ["istanbul", "hizmetler"],
        "Blog Hub": ["blog", "istanbul"],
        "Blog Category": ["blog", "istanbul"],
        "Blog Article": ["istanbul"]
    }
    
    keywords_for_type = required_keywords.get(page_type, [])
    missing_keywords = []
    
    title_lower = title.lower()
    for keyword in keywords_for_type:
        if keyword and keyword not in title_lower:
            missing_keywords.append(keyword)
    
    if missing_keywords:
        issues.append(f"Missing keywords: {', '.join(missing_keywords)}")
        score -= len(missing_keywords) * 10
    
    # Brand presence check
    if "dry alle" not in title_lower:
        issues.append("Brand name missing")
        score -= 15
    
    # Generate optimized title suggestion
    optimized_title = generate_optimized_title(page_type, district, neighborhood, service)
    
    return {
        "current_title": title,
        "length": len(title),
        "issues": issues,
        "score": max(0, score),
        "recommendations": recommendations,
        "optimized_suggestion": optimized_title
    }

def analyze_h1_tag(h1, page_type, district, neighborhood, service):
    """Analyze H1 tag for SEO optimization"""
    
    issues = []
    score = 100
    
    # H1 length check
    if len(h1) < 20:
        issues.append("H1 too short (<20 chars)")
        score -= 20
    elif len(h1) > 70:
        issues.append("H1 too long (>70 chars)")
        score -= 10
    
    # Location specificity for location pages
    if page_type == "Location Landing":
        if not neighborhood or neighborhood.lower() not in h1.lower():
            issues.append("Neighborhood not mentioned in H1")
            score -= 25
    
    # Service specificity
    if service and service.lower() not in h1.lower():
        issues.append("Service not clearly mentioned in H1")
        score -= 20
    
    # Generate optimized H1 suggestion
    optimized_h1 = generate_optimized_h1(page_type, district, neighborhood, service)
    
    return {
        "current_h1": h1,
        "length": len(h1),
        "issues": issues,
        "score": max(0, score),
        "optimized_suggestion": optimized_h1
    }

def analyze_meta_description(meta_desc, page_type, district, neighborhood, service):
    """Analyze meta description for SEO optimization"""
    
    issues = []
    score = 100
    
    # Meta description length check
    if len(meta_desc) < 120:
        issues.append("Meta description too short (<120 chars)")
        score -= 20
    elif len(meta_desc) > 160:
        issues.append("Meta description too long (>160 chars)")
        score -= 15
    
    # CTA presence check
    cta_words = ["arayın", "iletişim", "randevu", "hemen", "whatsapp", "telefon"]
    has_cta = any(cta in meta_desc.lower() for cta in cta_words)
    
    if not has_cta:
        issues.append("No clear call-to-action")
        score -= 15
    
    # Local specificity
    if page_type in ["Location Landing", "District Hub"]:
        if district and district.lower() not in meta_desc.lower():
            issues.append("District not mentioned")
            score -= 20
        
        if page_type == "Location Landing" and neighborhood:
            if neighborhood.lower() not in meta_desc.lower():
                issues.append("Neighborhood not mentioned")
                score -= 15
    
    # Generate optimized meta description suggestion
    optimized_meta = generate_optimized_meta_description(page_type, district, neighborhood, service)
    
    return {
        "current_meta": meta_desc,
        "length": len(meta_desc),
        "issues": issues,
        "score": max(0, score),
        "optimized_suggestion": optimized_meta
    }

def generate_optimized_title(page_type, district, neighborhood, service):
    """Generate SEO-optimized title suggestions"""
    
    if page_type == "Homepage":
        return "İstanbul Kuru Temizleme Halı Yıkama Koltuk Yıkama | Dry Alle"
    
    elif page_type == "Service Page":
        service_titles = {
            "Kuru Temizleme": "İstanbul Kuru Temizleme Hizmeti | Kadıköy Ataşehir | Dry Alle",
            "Gelinlik Temizleme": "Gelinlik Temizleme İstanbul | Kadıköy Ataşehir | Dry Alle",
            "Halı Yıkama": "Halı Yıkama İstanbul | Kadıköy Ataşehir | Dry Alle",
            "Koltuk Yıkama": "Koltuk Yıkama İstanbul | Kadıköy Ataşehir | Dry Alle",
            "Perde Temizleme": "Perde Temizleme İstanbul | Kadıköy Ataşehir | Dry Alle"
        }
        return service_titles.get(service, f"{service} İstanbul | Kadıköy Ataşehir | Dry Alle")
    
    elif page_type == "Location Landing":
        return f"{neighborhood} {service} | {district} | Dry Alle"
    
    elif page_type == "District Hub":
        return f"{district} Kuru Temizleme Halı Yıkama | Dry Alle İstanbul"
    
    elif page_type == "Service Hub":
        return "Kuru Temizleme Hizmetleri İstanbul | Kadıköy Ataşehir | Dry Alle"
    
    return "Optimized title needed"

def generate_optimized_h1(page_type, district, neighborhood, service):
    """Generate SEO-optimized H1 suggestions"""
    
    if page_type == "Homepage":
        return "İstanbul Anadolu Yakası Kuru Temizleme, Halı ve Koltuk Yıkama"
    
    elif page_type == "Service Page":
        return f"İstanbul {service} Hizmeti - Kadıköy ve Ataşehir"
    
    elif page_type == "Location Landing":
        return f"{neighborhood}'da {service} - Kapıdan Alım Hızlı Teslim"
    
    elif page_type == "District Hub":
        return f"{district} Kuru Temizleme ve Tekstil Hizmetleri"
    
    return "Optimized H1 needed"

def generate_optimized_meta_description(page_type, district, neighborhood, service):
    """Generate SEO-optimized meta description suggestions"""
    
    if page_type == "Homepage":
        return "İstanbul Anadolu Yakası'nda 25 yıllık deneyimle kuru temizleme, halı yıkama, koltuk yıkama. Kadıköy ve Ataşehir'e ücretsiz teslimat. Hemen arayın!"
    
    elif page_type == "Service Page":
        return f"İstanbul'da profesyonel {service.lower()} hizmeti. Kadıköy ve Ataşehir'e ücretsiz teslimat, 25 yıllık deneyim. Hemen randevu alın!"
    
    elif page_type == "Location Landing":
        return f"{neighborhood} {service.lower()} için kapıdan alım, hızlı teslim, lüks kumaş uzmanlığı. 25 yıllık deneyim ile güvenilir hizmet. Hemen arayın!"
    
    elif page_type == "District Hub":
        return f"{district}'de kuru temizleme, halı yıkama, koltuk yıkama hizmetleri. 25 yıllık deneyim, ücretsiz alma-getirme. Tüm semtlere hizmet."
    
    return "Optimized meta description needed"

def check_duplicate_content(pages):
    """Check for duplicate titles, H1s, and meta descriptions"""
    
    duplicates = {
        "titles": {},
        "h1s": {},
        "meta_descriptions": {}
    }
    
    for page in pages:
        title = page["Title"]
        h1 = page["H1"]
        meta = page["Meta Description"]
        
        # Track duplicates
        if title in duplicates["titles"]:
            duplicates["titles"][title].append(page["Full URL"])
        else:
            duplicates["titles"][title] = [page["Full URL"]]
        
        if h1 in duplicates["h1s"]:
            duplicates["h1s"][h1].append(page["Full URL"])
        else:
            duplicates["h1s"][h1] = [page["Full URL"]]
        
        if meta in duplicates["meta_descriptions"]:
            duplicates["meta_descriptions"][meta].append(page["Full URL"])
        else:
            duplicates["meta_descriptions"][meta] = [page["Full URL"]]
    
    # Filter to only actual duplicates
    duplicate_titles = {k: v for k, v in duplicates["titles"].items() if len(v) > 1}
    duplicate_h1s = {k: v for k, v in duplicates["h1s"].items() if len(v) > 1}
    duplicate_metas = {k: v for k, v in duplicates["meta_descriptions"].items() if len(v) > 1}
    
    return {
        "duplicate_titles": duplicate_titles,
        "duplicate_h1s": duplicate_h1s,
        "duplicate_meta_descriptions": duplicate_metas
    }

def identify_weak_content(pages):
    """Identify pages with weak or template-like content"""
    
    weak_content_pages = []
    
    for page in pages:
        weak_signals = []
        
        # Check for repetitive patterns
        title = page["Title"]
        h1 = page["H1"]
        meta = page["Meta Description"]
        
        # Very similar title/H1
        if title.lower().replace("| dry alle", "").strip() == h1.lower().strip():
            weak_signals.append("Title and H1 are nearly identical")
        
        # Template-like meta descriptions
        template_phrases = [
            "25 yıllık deneyim, ücretsiz teslimat",
            "Anadolu Yakası'nın tüm semtlerine hizmet",
            "profesyonel.*hizmeti.*25 yıllık deneyim"
        ]
        
        meta_lower = meta.lower()
        for phrase in template_phrases:
            if re.search(phrase, meta_lower):
                weak_signals.append(f"Template phrase detected: {phrase}")
        
        # Generic content indicators
        if len(meta) < 100:
            weak_signals.append("Very short meta description")
        
        if weak_signals:
            weak_content_pages.append({
                "url": page["Full URL"],
                "page_type": page["Page Type"],
                "issues": weak_signals
            })
    
    return weak_content_pages

def main():
    """Run comprehensive on-page content audit"""
    
    print("DryAlle On-Page Content Audit başlatılıyor...")
    
    # Load pages data
    pages = load_url_master_data()
    
    # Audit results storage
    audit_results = []
    
    # Analyze each page
    for page in pages:
        page_type = page["Page Type"]
        district = page.get("District", "")
        neighborhood = page.get("Neighborhood", "")
        service = page.get("Service", "")
        
        # Analyze title, H1, meta description
        title_analysis = analyze_title_tag(page["Title"], page_type, district, neighborhood, service)
        h1_analysis = analyze_h1_tag(page["H1"], page_type, district, neighborhood, service)
        meta_analysis = analyze_meta_description(page["Meta Description"], page_type, district, neighborhood, service)
        
        # Calculate overall page score
        overall_score = (title_analysis["score"] + h1_analysis["score"] + meta_analysis["score"]) / 3
        
        audit_results.append({
            "URL": page["Full URL"],
            "Page Type": page_type,
            "District": district,
            "Neighborhood": neighborhood,
            "Service": service,
            "Status": page["Status"],
            "Title Score": title_analysis["score"],
            "Title Issues": "; ".join(title_analysis["issues"]),
            "Title Suggestion": title_analysis["optimized_suggestion"],
            "H1 Score": h1_analysis["score"],
            "H1 Issues": "; ".join(h1_analysis["issues"]),
            "H1 Suggestion": h1_analysis["optimized_suggestion"],
            "Meta Score": meta_analysis["score"],
            "Meta Issues": "; ".join(meta_analysis["issues"]),
            "Meta Suggestion": meta_analysis["optimized_suggestion"],
            "Overall Score": round(overall_score, 1),
            "Priority": "High" if overall_score < 70 else "Medium" if overall_score < 85 else "Low"
        })
    
    # Check for duplicates and weak content
    duplicates = check_duplicate_content(pages)
    weak_content = identify_weak_content(pages)
    
    # Save audit results to CSV
    output_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/02_onpage_audit.csv")
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = audit_results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(audit_results)
    
    # Generate summary statistics
    total_pages = len(audit_results)
    high_priority = len([p for p in audit_results if p["Priority"] == "High"])
    medium_priority = len([p for p in audit_results if p["Priority"] == "Medium"])
    low_priority = len([p for p in audit_results if p["Priority"] == "Low"])
    
    avg_title_score = sum(p["Title Score"] for p in audit_results) / total_pages
    avg_h1_score = sum(p["H1 Score"] for p in audit_results) / total_pages
    avg_meta_score = sum(p["Meta Score"] for p in audit_results) / total_pages
    avg_overall_score = sum(p["Overall Score"] for p in audit_results) / total_pages
    
    # Print summary
    print(f"\n=== ON-PAGE CONTENT AUDIT SUMMARY ===")
    print(f"Total pages analyzed: {total_pages}")
    print(f"High priority issues: {high_priority}")
    print(f"Medium priority issues: {medium_priority}")
    print(f"Low priority issues: {low_priority}")
    
    print(f"\n=== AVERAGE SCORES ===")
    print(f"Title Score: {avg_title_score:.1f}/100")
    print(f"H1 Score: {avg_h1_score:.1f}/100")
    print(f"Meta Description Score: {avg_meta_score:.1f}/100")
    print(f"Overall Score: {avg_overall_score:.1f}/100")
    
    print(f"\n=== DUPLICATE CONTENT ===")
    print(f"Duplicate titles: {len(duplicates['duplicate_titles'])}")
    print(f"Duplicate H1s: {len(duplicates['duplicate_h1s'])}")
    print(f"Duplicate meta descriptions: {len(duplicates['duplicate_meta_descriptions'])}")
    
    print(f"\n=== WEAK CONTENT ===")
    print(f"Pages with weak content: {len(weak_content)}")
    
    print(f"\nResults saved to: {output_file}")
    
    # Save additional analysis data
    analysis_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/02_content_analysis.json")
    
    with open(analysis_file, 'w', encoding='utf-8') as f:
        json.dump({
            "summary": {
                "total_pages": total_pages,
                "priority_breakdown": {
                    "high": high_priority,
                    "medium": medium_priority,
                    "low": low_priority
                },
                "average_scores": {
                    "title": round(avg_title_score, 1),
                    "h1": round(avg_h1_score, 1),
                    "meta": round(avg_meta_score, 1),
                    "overall": round(avg_overall_score, 1)
                }
            },
            "duplicates": duplicates,
            "weak_content": weak_content,
            "timestamp": "2025-01-16"
        }, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()