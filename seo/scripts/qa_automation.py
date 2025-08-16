#!/usr/bin/env python3
"""
DryAlle Quality Assurance Automation
Comprehensive QA testing for all deployed content
"""

import os
import re
import csv
import json
import requests
from pathlib import Path
from datetime import datetime
import time

def qa_test_page(file_path, expected_data=None):
    """Run comprehensive QA tests on a single page"""
    
    if not os.path.exists(file_path):
        return {
            "overall_status": "FAIL",
            "error": "File not found",
            "tests": {}
        }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            "overall_status": "FAIL", 
            "error": f"Cannot read file: {str(e)}",
            "tests": {}
        }
    
    qa_results = {
        "overall_status": "PASS",
        "tests": {},
        "warnings": [],
        "errors": []
    }
    
    # Test 1: Title Tag Validation
    title_test = test_title_tag(content, expected_data)
    qa_results["tests"]["title"] = title_test
    if title_test["status"] == "FAIL":
        qa_results["overall_status"] = "FAIL"
        qa_results["errors"].append(title_test["message"])
    elif title_test["status"] == "WARN":
        qa_results["warnings"].append(title_test["message"])
    
    # Test 2: Meta Description Validation
    meta_test = test_meta_description(content, expected_data)
    qa_results["tests"]["meta_description"] = meta_test
    if meta_test["status"] == "FAIL":
        qa_results["overall_status"] = "FAIL"
        qa_results["errors"].append(meta_test["message"])
    elif meta_test["status"] == "WARN":
        qa_results["warnings"].append(meta_test["message"])
    
    # Test 3: H1 Tag Validation
    h1_test = test_h1_tag(content, expected_data)
    qa_results["tests"]["h1"] = h1_test
    if h1_test["status"] == "FAIL":
        qa_results["overall_status"] = "FAIL"
        qa_results["errors"].append(h1_test["message"])
    
    # Test 4: Internal Links Validation
    links_test = test_internal_links(content)
    qa_results["tests"]["internal_links"] = links_test
    if links_test["status"] == "FAIL":
        qa_results["overall_status"] = "FAIL"
        qa_results["errors"].append(links_test["message"])
    elif links_test["status"] == "WARN":
        qa_results["warnings"].append(links_test["message"])
    
    # Test 5: CTA Validation
    cta_test = test_cta_functionality(content)
    qa_results["tests"]["cta"] = cta_test
    if cta_test["status"] == "FAIL":
        qa_results["overall_status"] = "FAIL"
        qa_results["errors"].append(cta_test["message"])
    elif cta_test["status"] == "WARN":
        qa_results["warnings"].append(cta_test["message"])
    
    # Test 6: Schema Markup Validation
    schema_test = test_schema_markup(content)
    qa_results["tests"]["schema"] = schema_test
    if schema_test["status"] == "FAIL":
        qa_results["overall_status"] = "FAIL"
        qa_results["errors"].append(schema_test["message"])
    
    # Test 7: Mobile Optimization
    mobile_test = test_mobile_optimization(content)
    qa_results["tests"]["mobile"] = mobile_test
    if mobile_test["status"] == "FAIL":
        qa_results["overall_status"] = "FAIL"
        qa_results["errors"].append(mobile_test["message"])
    
    # Test 8: Image Optimization
    image_test = test_image_optimization(content)
    qa_results["tests"]["images"] = image_test
    if image_test["status"] == "WARN":
        qa_results["warnings"].append(image_test["message"])
    
    return qa_results

def test_title_tag(content, expected_data):
    """Test title tag optimization"""
    title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    
    if not title_match:
        return {"status": "FAIL", "message": "No title tag found"}
    
    title = title_match.group(1).strip()
    title_length = len(title)
    
    if title_length == 0:
        return {"status": "FAIL", "message": "Empty title tag"}
    elif title_length < 30:
        return {"status": "WARN", "message": f"Title too short ({title_length} chars)"}
    elif title_length > 60:
        return {"status": "WARN", "message": f"Title too long ({title_length} chars)"}
    
    # Check for brand name
    if "dry alle" not in title.lower():
        return {"status": "WARN", "message": "Brand name missing from title"}
    
    return {
        "status": "PASS", 
        "message": f"Title tag valid ({title_length} chars)",
        "title": title
    }

def test_meta_description(content, expected_data):
    """Test meta description optimization"""
    meta_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    
    if not meta_match:
        return {"status": "FAIL", "message": "No meta description found"}
    
    meta_desc = meta_match.group(1)
    meta_length = len(meta_desc)
    
    if meta_length == 0:
        return {"status": "FAIL", "message": "Empty meta description"}
    elif meta_length < 120:
        return {"status": "WARN", "message": f"Meta description too short ({meta_length} chars)"}
    elif meta_length > 160:
        return {"status": "WARN", "message": f"Meta description too long ({meta_length} chars)"}
    
    # Check for CTA words
    cta_words = ["arayın", "iletişim", "randevu", "hemen", "whatsapp"]
    has_cta = any(word in meta_desc.lower() for word in cta_words)
    
    if not has_cta:
        return {"status": "WARN", "message": "No CTA in meta description"}
    
    return {
        "status": "PASS",
        "message": f"Meta description valid ({meta_length} chars)",
        "meta_description": meta_desc
    }

def test_h1_tag(content, expected_data):
    """Test H1 tag optimization"""
    h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    
    if not h1_matches:
        return {"status": "FAIL", "message": "No H1 tag found"}
    
    if len(h1_matches) > 1:
        return {"status": "WARN", "message": f"Multiple H1 tags found ({len(h1_matches)})"}
    
    h1_text = re.sub(r'<[^>]+>', '', h1_matches[0]).strip()
    h1_length = len(h1_text)
    
    if h1_length == 0:
        return {"status": "FAIL", "message": "Empty H1 tag"}
    elif h1_length > 70:
        return {"status": "WARN", "message": f"H1 too long ({h1_length} chars)"}
    
    return {
        "status": "PASS",
        "message": f"H1 tag valid ({h1_length} chars)",
        "h1": h1_text
    }

def test_internal_links(content):
    """Test internal linking structure"""
    # Find all internal links
    link_pattern = r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>'
    links = re.findall(link_pattern, content, re.IGNORECASE)
    
    # Filter internal links (exclude external, mailto, tel, javascript)
    internal_links = []
    for link in links:
        if (not link.startswith('http') and 
            not link.startswith('mailto:') and 
            not link.startswith('tel:') and 
            not link.startswith('javascript:') and
            not link.startswith('#')):
            internal_links.append(link)
    
    internal_count = len(internal_links)
    
    if internal_count == 0:
        return {"status": "WARN", "message": "No internal links found"}
    elif internal_count < 3:
        return {"status": "WARN", "message": f"Few internal links ({internal_count})"}
    elif internal_count > 100:
        return {"status": "WARN", "message": f"Too many internal links ({internal_count})"}
    
    return {
        "status": "PASS",
        "message": f"Internal links valid ({internal_count} links)",
        "link_count": internal_count
    }

def test_cta_functionality(content):
    """Test CTA implementation"""
    # Check for phone CTAs
    phone_ctas = len(re.findall(r'href=["\']tel:', content, re.IGNORECASE))
    
    # Check for WhatsApp CTAs
    whatsapp_ctas = len(re.findall(r'wa\.me|whatsapp', content, re.IGNORECASE))
    
    total_ctas = phone_ctas + whatsapp_ctas
    
    if total_ctas == 0:
        return {"status": "FAIL", "message": "No CTAs found"}
    elif total_ctas < 2:
        return {"status": "WARN", "message": f"Few CTAs ({total_ctas})"}
    
    # Check for proper phone number format
    phone_number_pattern = r'\+90[- ]?5\d{2}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}'
    if phone_ctas > 0 and not re.search(phone_number_pattern, content):
        return {"status": "WARN", "message": "Phone number format may be incorrect"}
    
    return {
        "status": "PASS",
        "message": f"CTAs valid (Phone: {phone_ctas}, WhatsApp: {whatsapp_ctas})",
        "phone_ctas": phone_ctas,
        "whatsapp_ctas": whatsapp_ctas
    }

def test_schema_markup(content):
    """Test schema markup implementation"""
    # Check for JSON-LD schema
    schema_matches = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', content, re.IGNORECASE | re.DOTALL)
    
    if not schema_matches:
        return {"status": "FAIL", "message": "No schema markup found"}
    
    schema_types = []
    for schema_content in schema_matches:
        try:
            schema_data = json.loads(schema_content.strip())
            if "@type" in schema_data:
                schema_types.append(schema_data["@type"])
            elif isinstance(schema_data, list):
                for item in schema_data:
                    if "@type" in item:
                        schema_types.append(item["@type"])
        except json.JSONDecodeError:
            return {"status": "FAIL", "message": "Invalid JSON in schema markup"}
    
    if not schema_types:
        return {"status": "FAIL", "message": "No valid schema types found"}
    
    return {
        "status": "PASS",
        "message": f"Schema markup valid ({', '.join(schema_types)})",
        "schema_types": schema_types
    }

def test_mobile_optimization(content):
    """Test mobile optimization"""
    # Check for viewport meta tag
    if 'name="viewport"' not in content:
        return {"status": "FAIL", "message": "No viewport meta tag"}
    
    # Check for responsive design indicators
    responsive_indicators = [
        'width=device-width',
        'max-width',
        'media=',
        '@media',
        'mobile'
    ]
    
    responsive_score = sum(1 for indicator in responsive_indicators if indicator in content)
    
    if responsive_score < 2:
        return {"status": "WARN", "message": "Limited mobile optimization indicators"}
    
    return {
        "status": "PASS",
        "message": "Mobile optimization present",
        "responsive_score": responsive_score
    }

def test_image_optimization(content):
    """Test image optimization"""
    img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
    
    if not img_tags:
        return {"status": "PASS", "message": "No images to test"}
    
    issues = []
    
    # Check for alt attributes
    images_without_alt = len([img for img in img_tags if 'alt=' not in img])
    if images_without_alt > 0:
        issues.append(f"{images_without_alt} images without alt text")
    
    # Check for loading attributes
    images_without_loading = len([img for img in img_tags if 'loading=' not in img])
    if images_without_loading > 0:
        issues.append(f"{images_without_loading} images without loading attribute")
    
    # Check for width/height attributes
    images_without_dimensions = len([img for img in img_tags if 'width=' not in img or 'height=' not in img])
    if images_without_dimensions > 0:
        issues.append(f"{images_without_dimensions} images without dimensions")
    
    if issues:
        return {
            "status": "WARN",
            "message": f"Image optimization issues: {'; '.join(issues)}",
            "total_images": len(img_tags)
        }
    
    return {
        "status": "PASS",
        "message": f"Images well optimized ({len(img_tags)} images)",
        "total_images": len(img_tags)
    }

def run_comprehensive_qa():
    """Run QA tests on all content"""
    
    print("DryAlle Comprehensive QA Testing başlatılıyor...")
    
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    generated_dir = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/generated_pages")
    
    qa_results = []
    
    # Test existing pages
    existing_files = [
        "index.html",
        "sss.html",
        "hizmetler/kuru-temizleme.html",
        "hizmetler/hali-yikama.html",
        "hizmetler/koltuk-yikama.html",
        "hizmetler/perde-temizleme.html",
        "hizmetler/ev-tekstili-temizligi.html",
        "hizmetler/canta-temizleme.html",
        "hizmetler/kumas-deri-boyama.html",
        "hizmetler/lostra-hizmeti.html",
        "hizmetler/utu-hizmetleri.html"
    ]
    
    print("Testing existing pages...")
    for file_path in existing_files:
        full_path = base_dir / file_path
        if full_path.exists():
            print(f"Testing: {file_path}")
            result = qa_test_page(full_path)
            qa_results.append({
                "file_path": file_path,
                "page_type": "Existing",
                "qa_status": result["overall_status"],
                "errors": len(result.get("errors", [])),
                "warnings": len(result.get("warnings", [])),
                "test_results": result["tests"],
                "timestamp": datetime.now().isoformat()
            })
    
    # Test sample of generated pages
    print("Testing generated pages (sample)...")
    if generated_dir.exists():
        generated_files = list(generated_dir.glob("*.html"))[:20]  # Test first 20
        
        for file_path in generated_files:
            print(f"Testing: {file_path.name}")
            result = qa_test_page(file_path)
            qa_results.append({
                "file_path": str(file_path.relative_to(base_dir)),
                "page_type": "Generated",
                "qa_status": result["overall_status"],
                "errors": len(result.get("errors", [])),
                "warnings": len(result.get("warnings", [])),
                "test_results": result["tests"],
                "timestamp": datetime.now().isoformat()
            })
    
    # Generate QA summary
    total_tested = len(qa_results)
    passed = len([r for r in qa_results if r["qa_status"] == "PASS"])
    failed = len([r for r in qa_results if r["qa_status"] == "FAIL"])
    
    total_errors = sum(r["errors"] for r in qa_results)
    total_warnings = sum(r["warnings"] for r in qa_results)
    
    print(f"\n=== QA TESTING SUMMARY ===")
    print(f"Total pages tested: {total_tested}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")
    print(f"Success rate: {(passed/total_tested)*100:.1f}%")
    
    # Save detailed results
    output_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_qa_results.json")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            "summary": {
                "total_tested": total_tested,
                "passed": passed,
                "failed": failed,
                "total_errors": total_errors,
                "total_warnings": total_warnings,
                "success_rate": round((passed/total_tested)*100, 1)
            },
            "results": qa_results,
            "timestamp": datetime.now().isoformat()
        }, f, indent=2, ensure_ascii=False)
    
    print(f"Detailed results saved to: {output_file}")
    
    return qa_results

if __name__ == "__main__":
    qa_results = run_comprehensive_qa()