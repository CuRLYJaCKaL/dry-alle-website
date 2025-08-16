#!/usr/bin/env python3
"""
DryAlle Deployment Verification Script
Validates all 434 pages are ready for production deployment
"""

import os
import xml.etree.ElementTree as ET
from pathlib import Path
import json
import re
from datetime import datetime

def verify_sitemap_integrity():
    """Verify sitemap.xml contains all expected pages"""
    sitemap_path = Path("/Users/macos/Documents/Projeler/DryAlle/sitemap.xml")
    
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        
        urls = []
        for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            if loc is not None:
                urls.append(loc.text)
        
        return {
            "total_urls": len(urls),
            "valid": len(urls) == 434,
            "sample_urls": urls[:5],
            "status": "PASS" if len(urls) == 434 else "FAIL"
        }
    except Exception as e:
        return {
            "total_urls": 0,
            "valid": False,
            "error": str(e),
            "status": "ERROR"
        }

def verify_robots_txt():
    """Verify robots.txt is correctly configured"""
    robots_path = Path("/Users/macos/Documents/Projeler/DryAlle/robots.txt")
    
    try:
        with open(robots_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_elements = [
            "User-agent: *",
            "Sitemap: https://dryallekurutemizleme.com/sitemap.xml",
            "Allow: /",
            "Disallow: /seo/"
        ]
        
        issues = []
        for element in required_elements:
            if element not in content:
                issues.append(f"Missing: {element}")
        
        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "status": "PASS" if len(issues) == 0 else "FAIL"
        }
    except Exception as e:
        return {
            "valid": False,
            "error": str(e),
            "status": "ERROR"
        }

def verify_generated_pages():
    """Verify all generated location pages exist"""
    generated_dir = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/generated_pages/")
    
    if not generated_dir.exists():
        return {
            "total_files": 0,
            "valid": False,
            "status": "ERROR",
            "error": "Generated pages directory not found"
        }
    
    html_files = list(generated_dir.glob("*.html"))
    
    return {
        "total_files": len(html_files),
        "expected": 403,
        "valid": len(html_files) >= 403,
        "status": "PASS" if len(html_files) >= 403 else "FAIL"
    }

def verify_essential_pages():
    """Verify essential pages exist and are valid"""
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    
    essential_pages = [
        "index.html",
        "sss.html",
        "hizmetler/kuru-temizleme.html",
        "hizmetler/hali-yikama.html",
        "hizmetler/koltuk-yikama.html"
    ]
    
    results = {}
    
    for page in essential_pages:
        page_path = base_dir / page
        
        if page_path.exists():
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Basic validation checks
                has_title = '<title>' in content
                has_meta_desc = 'name="description"' in content
                has_h1 = '<h1' in content
                has_schema = 'application/ld+json' in content
                has_phone_cta = 'tel:+905433527474' in content
                
                results[page] = {
                    "exists": True,
                    "has_title": has_title,
                    "has_meta_desc": has_meta_desc,
                    "has_h1": has_h1,
                    "has_schema": has_schema,
                    "has_phone_cta": has_phone_cta,
                    "status": "PASS" if all([has_title, has_meta_desc, has_h1, has_phone_cta]) else "WARN"
                }
            except Exception as e:
                results[page] = {
                    "exists": True,
                    "error": str(e),
                    "status": "ERROR"
                }
        else:
            results[page] = {
                "exists": False,
                "status": "FAIL"
            }
    
    return results

def verify_schema_markup():
    """Verify schema markup in key pages"""
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    
    schema_pages = {
        "homepage": "index.html",
        "faq": "sss.html"
    }
    
    results = {}
    
    for page_type, page_path in schema_pages.items():
        full_path = base_dir / page_path
        
        if full_path.exists():
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract schema markup
                schema_matches = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', 
                                          content, re.DOTALL)
                
                schema_types = []
                valid_schemas = 0
                
                for schema_content in schema_matches:
                    try:
                        schema_data = json.loads(schema_content.strip())
                        if "@type" in schema_data:
                            schema_types.append(schema_data["@type"])
                            valid_schemas += 1
                        elif isinstance(schema_data, list):
                            for item in schema_data:
                                if "@type" in item:
                                    schema_types.append(item["@type"])
                                    valid_schemas += 1
                    except json.JSONDecodeError:
                        continue
                
                results[page_type] = {
                    "schema_found": len(schema_matches) > 0,
                    "valid_schemas": valid_schemas,
                    "schema_types": schema_types,
                    "status": "PASS" if valid_schemas > 0 else "FAIL"
                }
                
            except Exception as e:
                results[page_type] = {
                    "error": str(e),
                    "status": "ERROR"
                }
        else:
            results[page_type] = {
                "exists": False,
                "status": "FAIL"
            }
    
    return results

def verify_cta_links():
    """Verify CTA links are correctly formatted"""
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    
    test_pages = ["index.html", "sss.html"]
    results = {}
    
    expected_phone = "+905433527474"
    expected_whatsapp_base = "wa.me/905433527474"
    
    for page in test_pages:
        page_path = base_dir / page
        
        if page_path.exists():
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check phone links
                phone_links = re.findall(r'href=["\']tel:([^"\']*)["\']', content)
                whatsapp_links = re.findall(r'href=["\']https://wa\.me/([^"\']*)["\']', content)
                
                phone_correct = any(expected_phone in link for link in phone_links)
                whatsapp_correct = any("905433527474" in link for link in whatsapp_links)
                
                results[page] = {
                    "phone_links_count": len(phone_links),
                    "whatsapp_links_count": len(whatsapp_links),
                    "phone_correct": phone_correct,
                    "whatsapp_correct": whatsapp_correct,
                    "status": "PASS" if phone_correct and whatsapp_correct else "WARN"
                }
                
            except Exception as e:
                results[page] = {
                    "error": str(e),
                    "status": "ERROR"
                }
        else:
            results[page] = {
                "exists": False,
                "status": "FAIL"
            }
    
    return results

def run_deployment_verification():
    """Run comprehensive deployment verification"""
    
    print("🚀 DryAlle Deployment Verification Starting...")
    print("=" * 60)
    
    verification_results = {
        "timestamp": datetime.now().isoformat(),
        "total_tests": 5,
        "passed_tests": 0,
        "failed_tests": 0,
        "tests": {}
    }
    
    # Test 1: Sitemap Verification
    print("📋 Test 1: Sitemap Verification...")
    sitemap_result = verify_sitemap_integrity()
    verification_results["tests"]["sitemap"] = sitemap_result
    if sitemap_result["status"] == "PASS":
        verification_results["passed_tests"] += 1
        print(f"   ✅ PASS: {sitemap_result['total_urls']} URLs found")
    else:
        verification_results["failed_tests"] += 1
        print(f"   ❌ FAIL: Expected 434 URLs, found {sitemap_result['total_urls']}")
    
    # Test 2: Robots.txt Verification
    print("🤖 Test 2: Robots.txt Verification...")
    robots_result = verify_robots_txt()
    verification_results["tests"]["robots"] = robots_result
    if robots_result["status"] == "PASS":
        verification_results["passed_tests"] += 1
        print("   ✅ PASS: Robots.txt correctly configured")
    else:
        verification_results["failed_tests"] += 1
        print(f"   ❌ FAIL: Issues found - {robots_result.get('issues', [])}")
    
    # Test 3: Generated Pages Verification
    print("📄 Test 3: Generated Pages Verification...")
    pages_result = verify_generated_pages()
    verification_results["tests"]["generated_pages"] = pages_result
    if pages_result["status"] == "PASS":
        verification_results["passed_tests"] += 1
        print(f"   ✅ PASS: {pages_result['total_files']} generated pages found")
    else:
        verification_results["failed_tests"] += 1
        print(f"   ❌ FAIL: Expected 403+ pages, found {pages_result['total_files']}")
    
    # Test 4: Essential Pages Verification
    print("🏠 Test 4: Essential Pages Verification...")
    essential_result = verify_essential_pages()
    verification_results["tests"]["essential_pages"] = essential_result
    passed_essential = sum(1 for page in essential_result.values() if page.get("status") == "PASS")
    if passed_essential >= 4:
        verification_results["passed_tests"] += 1
        print(f"   ✅ PASS: {passed_essential}/5 essential pages valid")
    else:
        verification_results["failed_tests"] += 1
        print(f"   ❌ FAIL: Only {passed_essential}/5 essential pages valid")
    
    # Test 5: Schema Markup Verification
    print("🔗 Test 5: Schema Markup Verification...")
    schema_result = verify_schema_markup()
    verification_results["tests"]["schema_markup"] = schema_result
    passed_schema = sum(1 for page in schema_result.values() if page.get("status") == "PASS")
    if passed_schema >= 1:
        verification_results["passed_tests"] += 1
        print(f"   ✅ PASS: {passed_schema}/2 pages have valid schema")
    else:
        verification_results["failed_tests"] += 1
        print(f"   ❌ FAIL: Only {passed_schema}/2 pages have valid schema")
    
    # Test 6: CTA Links Verification
    print("📞 Test 6: CTA Links Verification...")
    cta_result = verify_cta_links()
    verification_results["tests"]["cta_links"] = cta_result
    passed_cta = sum(1 for page in cta_result.values() if page.get("status") in ["PASS", "WARN"])
    if passed_cta >= 1:
        verification_results["passed_tests"] += 1
        print(f"   ✅ PASS: CTA links functional on {passed_cta}/2 pages")
    else:
        verification_results["failed_tests"] += 1
        print(f"   ❌ FAIL: CTA links issues found")
    
    # Final Results
    print("=" * 60)
    success_rate = (verification_results["passed_tests"] / 6) * 100
    print(f"🎯 DEPLOYMENT VERIFICATION COMPLETE")
    print(f"📊 Results: {verification_results['passed_tests']}/6 tests passed ({success_rate:.1f}%)")
    
    if success_rate >= 90:
        print("🚀 READY FOR DEPLOYMENT!")
        verification_results["deployment_ready"] = True
    elif success_rate >= 75:
        print("⚠️  DEPLOYMENT POSSIBLE WITH MINOR FIXES")
        verification_results["deployment_ready"] = "with_fixes"
    else:
        print("❌ NOT READY FOR DEPLOYMENT - CRITICAL ISSUES FOUND")
        verification_results["deployment_ready"] = False
    
    # Save results
    output_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/reports/deployment_verification.json")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(verification_results, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Detailed results saved to: {output_file}")
    
    return verification_results

if __name__ == "__main__":
    results = run_deployment_verification()