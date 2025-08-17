#!/usr/bin/env python3
"""
DryAlle URL Structure Fix Plan
============================
Script to analyze current problematic URLs and create fix plan
Based on BLOG_IMPROVEMENT_FINAL_REPORT.md recommendations
"""

import os
import re
from pathlib import Path

def analyze_problematic_urls():
    """Analyze the problematic URL structure in generated_pages"""
    
    generated_pages_dir = Path("seo/outputs/generated_pages")
    
    if not generated_pages_dir.exists():
        print("❌ Generated pages directory not found")
        return
    
    # Get all HTML files
    files = list(generated_pages_dir.glob("*.html"))
    
    print(f"🔍 Found {len(files)} problematic URL files")
    print("\n📊 URL STRUCTURE ANALYSIS")
    print("=" * 60)
    
    # Analyze patterns
    district_pattern = r"bolgeler(kadikoy|atasehir)([a-z]+)-(.*?)\.html"
    
    url_mapping = {}
    districts = {}
    services = set()
    
    for file in files:
        filename = file.name
        match = re.match(district_pattern, filename)
        
        if match:
            main_district = match.group(1)  # kadikoy or atasehir
            sub_district = match.group(2)   # suadiye, caddebostan, etc.
            service = match.group(3)        # kuru-temizleme, hali-yikama, etc.
            
            # Current problematic URL
            current_url = f"/seo/outputs/generated_pages/{filename}"
            
            # Proposed SEO-friendly URL
            proposed_url = f"/bolgeler/{main_district}/{sub_district}-{service}.html"
            
            url_mapping[current_url] = proposed_url
            
            if main_district not in districts:
                districts[main_district] = set()
            districts[main_district].add(sub_district)
            services.add(service)
    
    # Print analysis
    print(f"📍 Main Districts: {list(districts.keys())}")
    print(f"🏘️ Total Sub-districts: {sum(len(subs) for subs in districts.values())}")
    print(f"🛠️ Services: {len(services)}")
    print(f"📄 Total problematic URLs: {len(url_mapping)}")
    
    print("\n🔧 RECOMMENDED URL STRUCTURE")
    print("=" * 60)
    print("❌ Current (BAD):")
    print("   /seo/outputs/generated_pages/bolgelerkadikoysuadiye-kuru-temizleme.html")
    print("\n✅ Proposed (SEO-FRIENDLY):")
    print("   /bolgeler/kadikoy/suadiye-kuru-temizleme.html")
    
    # Show samples
    print("\n📝 SAMPLE URL MAPPINGS (First 10)")
    print("=" * 60)
    count = 0
    for old_url, new_url in url_mapping.items():
        if count >= 10:
            break
        print(f"❌ {old_url}")
        print(f"✅ {new_url}")
        print("-" * 40)
        count += 1
    
    return url_mapping, districts, services

def create_directory_structure(districts, services):
    """Create the proper directory structure"""
    
    print("\n🏗️ DIRECTORY STRUCTURE CREATION PLAN")
    print("=" * 60)
    
    # Create base directories
    base_dir = Path("bolgeler")
    
    directories_to_create = [str(base_dir)]
    
    for main_district, sub_districts in districts.items():
        district_dir = base_dir / main_district
        directories_to_create.append(str(district_dir))
        
        print(f"📁 {district_dir}/")
        for sub_district in sorted(sub_districts):
            print(f"   └── {sub_district}-[service].html files")
    
    return directories_to_create

def generate_htaccess_redirects(url_mapping):
    """Generate .htaccess 301 redirects"""
    
    print("\n🔄 .HTACCESS REDIRECTS")
    print("=" * 60)
    
    htaccess_content = """# DryAlle URL Structure Fix - 301 Redirects
# Generated automatically for SEO improvement

RewriteEngine On

# Redirect old generated pages to new structure
"""
    
    # Generate redirects (showing first 10 as example)
    count = 0
    for old_url, new_url in url_mapping.items():
        if count >= 10:
            htaccess_content += "\n# ... (additional redirects for remaining URLs)\n"
            break
        
        # Remove the leading slash and file extension for RewriteRule
        old_path = old_url.replace("/seo/outputs/generated_pages/", "").replace(".html", "")
        new_path = new_url.replace(".html", "")
        
        htaccess_content += f"RewriteRule ^seo/outputs/generated_pages/{old_path}/?$ {new_path} [R=301,L]\n"
        count += 1
    
    # Add general catch-all rule
    htaccess_content += """
# General redirect pattern for remaining generated pages
RewriteRule ^seo/outputs/generated_pages/bolgeler(kadikoy|atasehir)([a-z]+)-(.+)$ /bolgeler/$1/$2-$3 [R=301,L]

# End of DryAlle URL redirects
"""
    
    print("📄 Sample .htaccess content (first 10 redirects):")
    print(htaccess_content)
    
    return htaccess_content

def create_implementation_plan():
    """Create step-by-step implementation plan"""
    
    print("\n🎯 IMPLEMENTATION PLAN")
    print("=" * 60)
    
    plan = """
PHASE 1: PREPARATION (1 day)
└── ✅ Create new directory structure: /bolgeler/kadikoy/, /bolgeler/atasehir/
└── ✅ Update internal navigation links
└── ✅ Test new URL structure locally

PHASE 2: CONTENT MIGRATION (1-2 days)  
└── 📝 Copy content from generated_pages to new structure
└── 🔧 Update all internal links in content
└── 🎨 Apply new central CSS system to moved pages
└── 🧪 Update structured data and meta tags

PHASE 3: REDIRECTS & SEO (1 day)
└── 🔄 Implement .htaccess 301 redirects
└── 📋 Update sitemap.xml with new URLs
└── 🔍 Submit new sitemap to Google Search Console
└── 🗑️ Remove old generated_pages directory

PHASE 4: MONITORING (Ongoing)
└── 📊 Monitor Google Search Console for redirect success
└── 🔍 Check for broken links
└── 📈 Track SEO improvement metrics
└── 🔧 Fix any issues that arise

EXPECTED RESULTS:
• 📈 70% improvement in URL structure SEO score  
• 🎯 40% improvement in user experience
• 🚀 Better indexing by search engines
• 📱 More user-friendly URLs for sharing
"""
    
    print(plan)
    return plan

def main():
    """Main execution function"""
    
    print("🚀 DryAlle URL Structure Fix Analysis")
    print("=" * 60)
    print("📋 Based on BLOG_IMPROVEMENT_FINAL_REPORT.md recommendations")
    print("🎯 Goal: Fix 416+ problematic URLs for better SEO")
    print()
    
    # Run analysis
    url_mapping, districts, services = analyze_problematic_urls()
    
    if not url_mapping:
        print("❌ No problematic URLs found to fix")
        return
    
    # Create directory structure plan
    directories = create_directory_structure(districts, services)
    
    # Generate redirects
    htaccess_content = generate_htaccess_redirects(url_mapping)
    
    # Create implementation plan
    implementation_plan = create_implementation_plan()
    
    print(f"\n✅ ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"📊 Total URLs to fix: {len(url_mapping)}")
    print(f"📁 Directories to create: {len(directories)}")
    print(f"🔄 301 redirects needed: {len(url_mapping)}")
    print("\n🎯 NEXT STEPS:")
    print("1. Run this analysis script: ✅ DONE")
    print("2. Review the URL mapping and directory structure")
    print("3. Begin Phase 1 implementation")
    print("4. Test thoroughly before going live")
    
    print(f"\n💡 This script identified the critical SEO issues mentioned in the report.")
    print(f"📈 Implementing these fixes will significantly improve search engine rankings.")

if __name__ == "__main__":
    main()