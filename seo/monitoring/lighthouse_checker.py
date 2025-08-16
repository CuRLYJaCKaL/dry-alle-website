#!/usr/bin/env python3
"""
Manual Lighthouse Score Checker
Quick performance monitoring for key pages
"""

import subprocess
import json
import os
from datetime import datetime

def run_lighthouse_check():
    """Run Lighthouse checks on key pages"""
    
    # Key pages to monitor
    pages = [
        {
            'name': 'Homepage',
            'url': 'https://dryallekurutemizleme.com/',
            'target_performance': 95,
            'target_seo': 98
        },
        {
            'name': 'Blog Index',
            'url': 'https://dryallekurutemizleme.com/blog/',
            'target_performance': 90,
            'target_seo': 95
        },
        {
            'name': 'Featured Blog Post',
            'url': 'https://dryallekurutemizleme.com/blog/2025-01/2025-yilinda-istanbul-kuru-temizleme-trendleri.html',
            'target_performance': 85,
            'target_seo': 95
        },
        {
            'name': 'Service Page',
            'url': 'https://dryallekurutemizleme.com/hizmetler/kuru-temizleme.html',
            'target_performance': 90,
            'target_seo': 98
        }
    ]
    
    results = []
    
    print("🚀 Starting Lighthouse performance monitoring...")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    for page in pages:
        print(f"\n📊 Testing: {page['name']}")
        print(f"🔗 URL: {page['url']}")
        
        try:
            # Run Lighthouse command
            cmd = [
                'lighthouse',
                page['url'],
                '--only-categories=performance,seo,accessibility',
                '--output=json',
                '--quiet',
                '--chrome-flags=--headless --no-sandbox'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                # Parse Lighthouse results
                lighthouse_data = json.loads(result.stdout)
                categories = lighthouse_data['categories']
                
                performance = int(categories['performance']['score'] * 100)
                seo = int(categories['seo']['score'] * 100)
                accessibility = int(categories['accessibility']['score'] * 100)
                
                # Status indicators
                perf_status = "✅" if performance >= page['target_performance'] else "⚠️" if performance >= (page['target_performance'] - 10) else "❌"
                seo_status = "✅" if seo >= page['target_seo'] else "⚠️" if seo >= (page['target_seo'] - 5) else "❌"
                acc_status = "✅" if accessibility >= 90 else "⚠️" if accessibility >= 80 else "❌"
                
                print(f"   {perf_status} Performance: {performance}/100 (target: {page['target_performance']}+)")
                print(f"   {seo_status} SEO: {seo}/100 (target: {page['target_seo']}+)")
                print(f"   {acc_status} Accessibility: {accessibility}/100 (target: 90+)")
                
                # Store results
                results.append({
                    'page': page['name'],
                    'url': page['url'],
                    'performance': performance,
                    'seo': seo,
                    'accessibility': accessibility,
                    'timestamp': datetime.now().isoformat()
                })
                
                # Core Web Vitals (if available)
                audits = lighthouse_data.get('audits', {})
                if 'largest-contentful-paint' in audits:
                    lcp = audits['largest-contentful-paint']['numericValue']
                    print(f"   📈 LCP: {lcp/1000:.1f}s (target: <2.5s)")
                
            else:
                print(f"   ❌ Lighthouse test failed: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            print(f"   ⏰ Lighthouse test timeout for {page['name']}")
        except Exception as e:
            print(f"   ❌ Error testing {page['name']}: {str(e)}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📈 MONITORING SUMMARY")
    print("=" * 60)
    
    if results:
        avg_performance = sum(r['performance'] for r in results) / len(results)
        avg_seo = sum(r['seo'] for r in results) / len(results)
        avg_accessibility = sum(r['accessibility'] for r in results) / len(results)
        
        print(f"🎯 Average Scores:")
        print(f"   Performance: {avg_performance:.1f}/100")
        print(f"   SEO: {avg_seo:.1f}/100")
        print(f"   Accessibility: {avg_accessibility:.1f}/100")
        
        # Issues to address
        issues = []
        for r in results:
            if r['performance'] < 85:
                issues.append(f"Performance issue on {r['page']}: {r['performance']}/100")
            if r['seo'] < 95:
                issues.append(f"SEO issue on {r['page']}: {r['seo']}/100")
        
        if issues:
            print(f"\n⚠️ Issues to Address:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print(f"\n✅ All pages meet performance standards!")
        
        # Save results
        os.makedirs('/tmp', exist_ok=True)
        with open(f'/tmp/lighthouse_results_{datetime.now().strftime("%Y%m%d_%H%M")}.json', 'w') as f:
            json.dump(results, f, indent=2)
            
        print(f"\n💾 Results saved to: /tmp/lighthouse_results_{datetime.now().strftime('%Y%m%d_%H%M')}.json")
    
    print("\n🏁 Monitoring complete!")

if __name__ == "__main__":
    run_lighthouse_check()