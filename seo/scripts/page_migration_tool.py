#!/usr/bin/env python3
"""
DryAlle Existing Pages Migration Tool
Migrates existing 65 pages to new SEO standards and CTA optimizations
"""

import csv
import os
import re
from pathlib import Path
import json
from datetime import datetime

def load_existing_pages():
    """Load list of existing pages that need migration"""
    master_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_url_meta_master.csv")
    existing_pages = []
    
    with open(master_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Status"] == "Exists":
                existing_pages.append(row)
    
    return existing_pages

def analyze_current_page(file_path):
    """Analyze current page content and identify improvement areas"""
    
    if not os.path.exists(file_path):
        return {"error": "File not found", "improvements": []}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"error": f"Cannot read file: {str(e)}", "improvements": []}
    
    improvements = []
    current_state = {}
    
    # Extract current meta information
    title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    current_state["title"] = title_match.group(1).strip() if title_match else "No title found"
    
    meta_desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    current_state["meta_description"] = meta_desc_match.group(1) if meta_desc_match else "No meta description"
    
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    current_state["h1"] = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else "No H1 found"
    
    # Check for CTAs
    phone_cta_count = len(re.findall(r'href=["\']tel:', content, re.IGNORECASE))
    whatsapp_cta_count = len(re.findall(r'wa\.me|whatsapp', content, re.IGNORECASE))
    current_state["phone_ctas"] = phone_cta_count
    current_state["whatsapp_ctas"] = whatsapp_cta_count
    
    # Check for schema markup
    has_schema = 'application/ld+json' in content
    current_state["has_schema"] = has_schema
    
    # Check for mobile optimization
    has_viewport = 'viewport' in content
    current_state["has_viewport"] = has_viewport
    
    # Identify improvements needed
    if len(current_state["title"]) > 60:
        improvements.append("Title too long (>60 characters)")
    
    if len(current_state["meta_description"]) > 160:
        improvements.append("Meta description too long (>160 characters)")
    
    if len(current_state["meta_description"]) < 120:
        improvements.append("Meta description too short (<120 characters)")
    
    if phone_cta_count == 0:
        improvements.append("No phone CTAs found")
    
    if whatsapp_cta_count == 0:
        improvements.append("No WhatsApp CTAs found")
    
    if not has_schema:
        improvements.append("No schema markup found")
    
    if not has_viewport:
        improvements.append("No mobile viewport meta tag")
    
    # Check for image optimization
    img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
    images_without_loading = len([img for img in img_tags if 'loading=' not in img])
    if images_without_loading > 0:
        improvements.append(f"{images_without_loading} images missing loading attribute")
    
    images_without_alt = len([img for img in img_tags if 'alt=' not in img])
    if images_without_alt > 0:
        improvements.append(f"{images_without_alt} images missing alt text")
    
    return {
        "current_state": current_state,
        "improvements": improvements,
        "img_tags_count": len(img_tags)
    }

def generate_migration_plan(page_data, analysis):
    """Generate specific migration plan for a page"""
    
    migration_tasks = []
    priority = "Low"
    
    page_type = page_data.get("Page Type", "")
    
    # Title optimization
    if "Title too long" in analysis["improvements"]:
        migration_tasks.append({
            "task": "Optimize title tag",
            "current": analysis["current_state"]["title"],
            "target": page_data.get("Title", ""),
            "priority": "High"
        })
        priority = "High"
    
    # Meta description optimization
    if any("Meta description" in imp for imp in analysis["improvements"]):
        migration_tasks.append({
            "task": "Optimize meta description",
            "current": analysis["current_state"]["meta_description"],
            "target": page_data.get("Meta Description", ""),
            "priority": "High"
        })
        priority = "High"
    
    # CTA additions
    if "No phone CTAs found" in analysis["improvements"]:
        migration_tasks.append({
            "task": "Add phone CTAs",
            "current": f"{analysis['current_state']['phone_ctas']} phone CTAs",
            "target": "3-5 strategic phone CTAs",
            "priority": "High"
        })
        priority = "High"
    
    if "No WhatsApp CTAs found" in analysis["improvements"]:
        migration_tasks.append({
            "task": "Add WhatsApp CTAs",
            "current": f"{analysis['current_state']['whatsapp_ctas']} WhatsApp CTAs",
            "target": "2-3 WhatsApp CTAs with pre-filled text",
            "priority": "High"
        })
        priority = "High"
    
    # Schema markup
    if analysis.get("current_state", {}).get("has_schema", False) == False:
        migration_tasks.append({
            "task": "Add schema markup",
            "current": "No schema markup",
            "target": get_schema_type_for_page(page_type),
            "priority": "Medium"
        })
        if priority == "Low":
            priority = "Medium"
    
    # Image optimization
    if "images missing loading attribute" in str(analysis["improvements"]):
        migration_tasks.append({
            "task": "Add loading attributes to images",
            "current": "Images without lazy loading",
            "target": "All images with appropriate loading attributes",
            "priority": "Medium"
        })
        if priority == "Low":
            priority = "Medium"
    
    # Mobile optimization
    if not analysis.get("current_state", {}).get("has_viewport", True):
        migration_tasks.append({
            "task": "Add mobile viewport meta tag",
            "current": "No viewport meta",
            "target": "Responsive viewport meta tag",
            "priority": "High"
        })
        priority = "High"
    
    return {
        "overall_priority": priority,
        "tasks": migration_tasks,
        "estimated_effort": estimate_effort(migration_tasks),
        "impact_score": calculate_impact_score(migration_tasks, page_type)
    }

def get_schema_type_for_page(page_type):
    """Get appropriate schema type for page"""
    schema_types = {
        "Homepage": "LocalBusiness + Organization",
        "Service Hub": "LocalBusiness + ServiceOffer",
        "Service Page": "LocalBusiness + Service",
        "District Hub": "LocalBusiness + Place",
        "Blog Hub": "Blog + WebSite",
        "Blog Category": "Blog + CollectionPage",
        "Blog Article": "Article + LocalBusiness",
        "FAQ": "FAQPage + LocalBusiness",
        "Contact": "ContactPage + LocalBusiness",
        "About": "AboutPage + LocalBusiness"
    }
    return schema_types.get(page_type, "LocalBusiness")

def estimate_effort(tasks):
    """Estimate development effort for migration tasks"""
    effort_hours = 0
    
    for task in tasks:
        task_name = task["task"]
        if "title" in task_name.lower() or "meta" in task_name.lower():
            effort_hours += 0.5
        elif "cta" in task_name.lower():
            effort_hours += 1.5
        elif "schema" in task_name.lower():
            effort_hours += 1.0
        elif "image" in task_name.lower():
            effort_hours += 1.0
        elif "viewport" in task_name.lower():
            effort_hours += 0.25
        else:
            effort_hours += 0.5
    
    return round(effort_hours, 2)

def calculate_impact_score(tasks, page_type):
    """Calculate expected SEO impact score"""
    impact_score = 0
    
    # Page type multipliers
    page_multipliers = {
        "Homepage": 3.0,
        "Service Page": 2.5,
        "Service Hub": 2.0,
        "District Hub": 2.0,
        "Blog Article": 1.5,
        "FAQ": 1.5,
        "Contact": 1.0,
        "About": 1.0
    }
    
    multiplier = page_multipliers.get(page_type, 1.0)
    
    for task in tasks:
        task_name = task["task"]
        priority = task["priority"]
        
        base_score = 0
        if "title" in task_name.lower():
            base_score = 15
        elif "meta" in task_name.lower():
            base_score = 10
        elif "cta" in task_name.lower():
            base_score = 20
        elif "schema" in task_name.lower():
            base_score = 25
        elif "image" in task_name.lower():
            base_score = 8
        elif "viewport" in task_name.lower():
            base_score = 12
        
        # Priority multiplier
        priority_multiplier = {"High": 1.5, "Medium": 1.0, "Low": 0.7}.get(priority, 1.0)
        
        impact_score += base_score * priority_multiplier
    
    return round(impact_score * multiplier, 1)

def create_migration_code(page_data, migration_plan):
    """Generate specific code changes for migration"""
    
    page_type = page_data.get("Page Type", "")
    
    code_changes = {
        "meta_updates": [],
        "cta_additions": [],
        "schema_markup": [],
        "image_optimizations": [],
        "mobile_optimizations": []
    }
    
    # Meta updates
    for task in migration_plan["tasks"]:
        if "title" in task["task"].lower():
            code_changes["meta_updates"].append(f'<title>{task["target"]}</title>')
        
        elif "meta description" in task["task"].lower():
            code_changes["meta_updates"].append(f'<meta name="description" content="{task["target"]}">')
    
    # CTA additions
    if any("phone" in task["task"].lower() for task in migration_plan["tasks"]):
        code_changes["cta_additions"].extend([
            '<a href="tel:+905433527474" class="btn-primary btn-call">📞 Hemen Ara: 0543 352 74 74</a>',
            '<div class="hero-cta"><a href="tel:+905433527474" class="cta-button">Randevu İçin Ara</a></div>',
            '<div class="mobile-sticky-cta"><a href="tel:+905433527474">📞 Ara</a></div>'
        ])
    
    if any("whatsapp" in task["task"].lower() for task in migration_plan["tasks"]):
        whatsapp_text = generate_whatsapp_text(page_data)
        code_changes["cta_additions"].extend([
            f'<a href="https://wa.me/905433527474?text={whatsapp_text}" class="btn-primary btn-whatsapp">💬 WhatsApp Randevu</a>',
            f'<div class="whatsapp-float"><a href="https://wa.me/905433527474?text={whatsapp_text}">💬</a></div>'
        ])
    
    # Schema markup
    if any("schema" in task["task"].lower() for task in migration_plan["tasks"]):
        schema = generate_page_schema(page_data)
        code_changes["schema_markup"].append(f'<script type="application/ld+json">\n{schema}\n</script>')
    
    # Image optimizations
    if any("image" in task["task"].lower() for task in migration_plan["tasks"]):
        code_changes["image_optimizations"].extend([
            'Add loading="lazy" to below-fold images',
            'Add loading="eager" to above-fold images',
            'Add decoding="async" to all images',
            'Ensure all images have width and height attributes'
        ])
    
    # Mobile optimizations
    if any("viewport" in task["task"].lower() for task in migration_plan["tasks"]):
        code_changes["mobile_optimizations"].append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    
    return code_changes

def generate_whatsapp_text(page_data):
    """Generate pre-filled WhatsApp text based on page"""
    district = page_data.get("District", "")
    neighborhood = page_data.get("Neighborhood", "")
    service = page_data.get("Service", "")
    page_type = page_data.get("Page Type", "")
    
    if page_type == "Homepage":
        return "Kuru%20temizleme%20hizmeti%20hakkında%20bilgi%20almak%20istiyorum"
    elif page_type == "Service Page":
        return f"{service}%20hizmeti%20için%20randevu%20almak%20istiyorum"
    elif neighborhood and service:
        return f"{neighborhood}%20{service}%20için%20randevu%20almak%20istiyorum"
    elif district:
        return f"{district}%20bölgesi%20için%20hizmet%20bilgisi%20istiyorum"
    else:
        return "Hizmetleriniz%20hakkında%20bilgi%20almak%20istiyorum"

def generate_page_schema(page_data):
    """Generate appropriate schema markup for page"""
    page_type = page_data.get("Page Type", "")
    
    base_schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Dry Alle Kuru Temizleme",
        "description": page_data.get("Meta Description", ""),
        "url": page_data.get("Full URL", ""),
        "telephone": "+90-543-352-7474",
        "email": "info@dryallekurutemizleme.com",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Sahrayıcedit Mahallesi İnönü Caddesi",
            "addressLocality": "Kadıköy",
            "addressRegion": "İstanbul",
            "postalCode": "34740",
            "addressCountry": "TR"
        },
        "openingHours": "Mo-Sa 09:00-18:00",
        "priceRange": "$$"
    }
    
    if page_type == "Service Page":
        base_schema["serviceType"] = page_data.get("Service", "")
        base_schema["hasOfferCatalog"] = {
            "@type": "OfferCatalog",
            "name": f"{page_data.get('Service', '')} Hizmetleri",
            "itemListElement": [{
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": page_data.get("Service", ""),
                    "description": f"Profesyonel {page_data.get('Service', '').lower()} hizmeti"
                }
            }]
        }
    
    return json.dumps(base_schema, indent=2, ensure_ascii=False)

def run_migration_analysis():
    """Run comprehensive migration analysis for all existing pages"""
    
    print("DryAlle Page Migration Analysis başlatılıyor...")
    
    existing_pages = load_existing_pages()
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    
    migration_results = []
    
    for page in existing_pages:
        url_slug = page.get("URL Slug", "")
        
        # Determine file path
        if url_slug == "/":
            file_path = base_dir / "index.html"
        else:
            file_path = base_dir / url_slug.lstrip("/")
        
        print(f"Analyzing: {file_path}")
        
        # Analyze current page
        analysis = analyze_current_page(file_path)
        
        # Generate migration plan
        migration_plan = generate_migration_plan(page, analysis)
        
        # Generate code changes
        code_changes = create_migration_code(page, migration_plan)
        
        migration_results.append({
            "url": page.get("Full URL", ""),
            "page_type": page.get("Page Type", ""),
            "file_path": str(file_path),
            "current_title": analysis.get("current_state", {}).get("title", ""),
            "target_title": page.get("Title", ""),
            "current_meta": analysis.get("current_state", {}).get("meta_description", ""),
            "target_meta": page.get("Meta Description", ""),
            "improvements_needed": len(analysis.get("improvements", [])),
            "priority": migration_plan["overall_priority"],
            "estimated_hours": migration_plan["estimated_effort"],
            "impact_score": migration_plan["impact_score"],
            "tasks": "; ".join([task["task"] for task in migration_plan["tasks"]]),
            "has_schema": analysis.get("current_state", {}).get("has_schema", False),
            "phone_ctas": analysis.get("current_state", {}).get("phone_ctas", 0),
            "whatsapp_ctas": analysis.get("current_state", {}).get("whatsapp_ctas", 0),
            "migration_status": "Pending"
        })
    
    # Save migration analysis
    output_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_page_migration_analysis.csv")
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["url", "page_type", "file_path", "current_title", "target_title", 
                     "current_meta", "target_meta", "improvements_needed", "priority", 
                     "estimated_hours", "impact_score", "tasks", "has_schema", 
                     "phone_ctas", "whatsapp_ctas", "migration_status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(migration_results)
    
    # Generate summary statistics
    total_pages = len(migration_results)
    high_priority = len([r for r in migration_results if r["priority"] == "High"])
    medium_priority = len([r for r in migration_results if r["priority"] == "Medium"])
    low_priority = len([r for r in migration_results if r["priority"] == "Low"])
    
    total_hours = sum(r["estimated_hours"] for r in migration_results)
    avg_impact_score = sum(r["impact_score"] for r in migration_results) / total_pages
    
    pages_without_schema = len([r for r in migration_results if not r["has_schema"]])
    pages_without_phone_cta = len([r for r in migration_results if r["phone_ctas"] == 0])
    pages_without_whatsapp = len([r for r in migration_results if r["whatsapp_ctas"] == 0])
    
    print(f"\n=== MIGRATION ANALYSIS SUMMARY ===")
    print(f"Total pages analyzed: {total_pages}")
    print(f"High priority migrations: {high_priority}")
    print(f"Medium priority migrations: {medium_priority}")
    print(f"Low priority migrations: {low_priority}")
    print(f"Total estimated effort: {total_hours} hours")
    print(f"Average impact score: {avg_impact_score:.1f}")
    
    print(f"\n=== CRITICAL GAPS ===")
    print(f"Pages without schema markup: {pages_without_schema}")
    print(f"Pages without phone CTAs: {pages_without_phone_cta}")
    print(f"Pages without WhatsApp CTAs: {pages_without_whatsapp}")
    
    print(f"\nResults saved to: {output_file}")
    
    return migration_results

if __name__ == "__main__":
    migration_results = run_migration_analysis()