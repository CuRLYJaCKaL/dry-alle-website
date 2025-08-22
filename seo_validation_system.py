#!/usr/bin/env python3
"""
DryAlle SEO Validation System
Post-optimization verification for all pages
"""

import os
import re
from pathlib import Path

def validate_page(file_path):
    """Validate a single optimized page"""
    try:
        filename = os.path.basename(file_path)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = {
            'critical_css': 'Critical CSS for LCP Optimization' in content,
            'font_preload': 'Font Loading Optimization for Mobile Performance' in content,
            'geo_signals': 'geo.placename' in content and 'geo.position' in content,
            'mobile_performance': 'Mobile Performance Monitoring - 2025 AI/LLM Ready' in content,
            'body_attributes': 'data-mobile-optimized="true"' in content and 'data-lcp-element="service-hero"' in content,
            'hero_attributes': 'data-lcp-candidate="true"' in content and 'data-above-fold="true"' in content,
            'pwa_signals': 'mobile-web-app-title' in content and 'apple-touch-fullscreen' in content,
            'format_detection': 'format-detection' in content,
            'service_worker': 'serviceWorker' in content,
            'location_tracking': 'data-location-verified' in content
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        status = "✅ PERFECT" if passed == total else f"⚠️  {passed}/{total}"
        
        print(f"{status} {filename}")
        
        # Show failed checks
        if passed < total:
            for check, result in checks.items():
                if not result:
                    print(f"  ❌ Missing: {check}")
        
        return passed == total
        
    except Exception as e:
        print(f"❌ ERROR validating {filename}: {e}")
        return False

def main():
    """Main validation function"""
    bolgeler_dir = Path('/Users/macos/Documents/Projeler/DryAlle/bolgeler')
    html_files = list(bolgeler_dir.glob('*.html'))
    
    print(f"🔍 VALIDATING {len(html_files)} pages for mobile SEO optimization...\\n")
    
    perfect_count = 0
    for file_path in html_files:
        if validate_page(file_path):
            perfect_count += 1
    
    print(f"\\n📊 VALIDATION RESULTS:")
    print(f"✅ Perfect pages: {perfect_count}/{len(html_files)}")
    print(f"📈 Success rate: {(perfect_count/len(html_files)*100):.1f}%")
    
    if perfect_count == len(html_files):
        print("\\n🎉 ALL PAGES PERFECTLY OPTIMIZED FOR 2025 GOOGLE/AI/LLM!")
    else:
        print(f"\\n⚠️  {len(html_files) - perfect_count} pages need attention")

if __name__ == "__main__":
    main()