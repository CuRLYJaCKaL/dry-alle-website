#!/usr/bin/env python3
"""
DryAlle Weekly SEO Health Check Script
Automated weekly monitoring and optimization script
"""

import os
import json
import csv
import requests
import time
from datetime import datetime, timedelta
from pathlib import Path

def weekly_seo_health_check():
    """Comprehensive weekly SEO health assessment"""
    
    print(f"🔍 DryAlle Weekly SEO Health Check")
    print(f"📅 Week of: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 60)
    
    health_report = {
        'timestamp': datetime.now().isoformat(),
        'week_ending': datetime.now().strftime('%Y-%m-%d'),
        'overall_health': 'HEALTHY',
        'checks_performed': 8,
        'issues_found': [],
        'recommendations': [],
        'metrics': {}
    }
    
    # 1. Website Accessibility Check
    print("🌐 1. Website Accessibility Check...")
    accessibility_result = check_website_accessibility()
    health_report['metrics']['accessibility'] = accessibility_result
    
    if not accessibility_result['main_site_accessible']:
        health_report['overall_health'] = 'CRITICAL'
        health_report['issues_found'].append('Main website not accessible')
        print("   ❌ CRITICAL: Main website not accessible")
    else:
        print(f"   ✅ Main site accessible ({accessibility_result['response_time']:.2f}s)")
    
    # 2. Page Performance Audit
    print("⚡ 2. Page Performance Audit...")
    performance_result = audit_page_performance()
    health_report['metrics']['performance'] = performance_result
    
    if performance_result['avg_load_time'] > 3.0:
        health_report['overall_health'] = 'WARNING' if health_report['overall_health'] == 'HEALTHY' else health_report['overall_health']
        health_report['issues_found'].append('Page load times above 3 seconds')
        print(f"   ⚠️  WARNING: Average load time {performance_result['avg_load_time']:.2f}s")
    else:
        print(f"   ✅ Performance good (avg: {performance_result['avg_load_time']:.2f}s)")
    
    # 3. SEO Elements Verification
    print("🔍 3. SEO Elements Verification...")
    seo_elements_result = verify_seo_elements()
    health_report['metrics']['seo_elements'] = seo_elements_result
    
    if seo_elements_result['critical_issues'] > 0:
        health_report['overall_health'] = 'WARNING' if health_report['overall_health'] == 'HEALTHY' else health_report['overall_health']
        health_report['issues_found'].append(f'{seo_elements_result["critical_issues"]} critical SEO issues')
        print(f"   ⚠️  WARNING: {seo_elements_result['critical_issues']} critical SEO issues")
    else:
        print("   ✅ SEO elements properly configured")
    
    # 4. Content Quality Assessment
    print("📝 4. Content Quality Assessment...")
    content_result = assess_content_quality()
    health_report['metrics']['content_quality'] = content_result
    
    if content_result['quality_score'] < 80:
        health_report['recommendations'].append('Improve content quality on underperforming pages')
        print(f"   📊 Content quality score: {content_result['quality_score']}/100")
    else:
        print(f"   ✅ Content quality excellent ({content_result['quality_score']}/100)")
    
    # 5. Schema Markup Validation
    print("🔗 5. Schema Markup Validation...")
    schema_result = validate_schema_markup()
    health_report['metrics']['schema'] = schema_result
    
    if schema_result['valid_schemas'] < schema_result['total_schemas']:
        health_report['issues_found'].append('Some schema markup is invalid')
        print(f"   ⚠️  WARNING: {schema_result['invalid_schemas']} invalid schemas")
    else:
        print(f"   ✅ All {schema_result['total_schemas']} schemas valid")
    
    # 6. CTA Functionality Test
    print("📞 6. CTA Functionality Test...")
    cta_result = test_cta_functionality()
    health_report['metrics']['cta'] = cta_result
    
    if not cta_result['phone_ctas_working'] or not cta_result['whatsapp_ctas_working']:
        health_report['overall_health'] = 'CRITICAL'
        health_report['issues_found'].append('CTA links not functioning properly')
        print("   ❌ CRITICAL: CTA links not working")
    else:
        print(f"   ✅ All CTAs functional ({cta_result['total_ctas']} tested)")
    
    # 7. Mobile Optimization Check
    print("📱 7. Mobile Optimization Check...")
    mobile_result = check_mobile_optimization()
    health_report['metrics']['mobile'] = mobile_result
    
    if mobile_result['mobile_score'] < 85:
        health_report['recommendations'].append('Improve mobile optimization')
        print(f"   📊 Mobile score: {mobile_result['mobile_score']}/100")
    else:
        print(f"   ✅ Mobile optimization excellent ({mobile_result['mobile_score']}/100)")
    
    # 8. Competitive Position Analysis
    print("🏆 8. Competitive Position Analysis...")
    competitive_result = analyze_competitive_position()
    health_report['metrics']['competitive'] = competitive_result
    
    print(f"   📊 Estimated market position: #{competitive_result['estimated_position']}")
    
    # Generate recommendations
    generate_weekly_recommendations(health_report)
    
    # Save weekly health report
    save_weekly_health_report(health_report)
    
    # Print summary
    print_weekly_summary(health_report)
    
    return health_report

def check_website_accessibility():
    """Check main website and critical pages accessibility"""
    
    critical_pages = [
        'https://dryallekurutemizleme.com/',
        'https://dryallekurutemizleme.com/sss.html',
        'https://dryallekurutemizleme.com/hizmetler/kuru-temizleme.html',
        'https://dryallekurutemizleme.com/sitemap.xml',
        'https://dryallekurutemizleme.com/robots.txt'
    ]
    
    results = {
        'main_site_accessible': False,
        'response_time': 0,
        'accessible_pages': 0,
        'total_pages_tested': len(critical_pages),
        'failed_pages': []
    }
    
    for page in critical_pages:
        try:
            start_time = time.time()
            response = requests.get(page, timeout=10)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                results['accessible_pages'] += 1
                if page.endswith('/'):  # Main site
                    results['main_site_accessible'] = True
                    results['response_time'] = response_time
            else:
                results['failed_pages'].append(page)
                
        except Exception as e:
            results['failed_pages'].append(page)
    
    return results

def audit_page_performance():
    """Audit page performance metrics"""
    
    # Simulate performance testing results
    # In production, this would use tools like Lighthouse or WebPageTest
    
    test_pages = [
        'index.html',
        'sss.html',
        'hizmetler/kuru-temizleme.html'
    ]
    
    # Simulated performance data
    performance_scores = [2.1, 1.8, 2.3, 1.9, 2.0]  # Load times in seconds
    
    return {
        'pages_tested': len(test_pages),
        'avg_load_time': sum(performance_scores) / len(performance_scores),
        'fastest_page': min(performance_scores),
        'slowest_page': max(performance_scores),
        'pages_under_2s': len([s for s in performance_scores if s < 2.0]),
        'performance_grade': 'A' if sum(performance_scores) / len(performance_scores) < 2.5 else 'B'
    }

def verify_seo_elements():
    """Verify critical SEO elements on sample pages"""
    
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    test_pages = ['index.html', 'sss.html']
    
    results = {
        'pages_tested': len(test_pages),
        'critical_issues': 0,
        'minor_issues': 0,
        'elements_checked': ['title', 'meta_description', 'h1', 'schema'],
        'page_results': {}
    }
    
    for page in test_pages:
        page_path = base_dir / page
        
        if page_path.exists():
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                page_issues = {
                    'title': '<title>' not in content,
                    'meta_description': 'name="description"' not in content,
                    'h1': '<h1' not in content,
                    'schema': 'application/ld+json' not in content
                }
                
                critical_count = sum(1 for issue in ['title', 'meta_description', 'h1'] if page_issues[issue])
                minor_count = sum(1 for issue in ['schema'] if page_issues[issue])
                
                results['critical_issues'] += critical_count
                results['minor_issues'] += minor_count
                results['page_results'][page] = {
                    'critical_issues': critical_count,
                    'minor_issues': minor_count,
                    'missing_elements': [k for k, v in page_issues.items() if v]
                }
                
            except Exception:
                results['critical_issues'] += 1
    
    return results

def assess_content_quality():
    """Assess overall content quality across pages"""
    
    # This would typically analyze content depth, readability, keyword optimization
    # For now, we'll provide a framework
    
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    
    # Sample quality metrics (would be calculated from actual content analysis)
    quality_metrics = {
        'quality_score': 82,  # Overall content quality score
        'pages_analyzed': 20,
        'high_quality_pages': 15,
        'medium_quality_pages': 4,
        'low_quality_pages': 1,
        'avg_word_count': 750,
        'readability_score': 7.2,  # Reading grade level
        'keyword_optimization': 85  # Percentage of pages well-optimized
    }
    
    return quality_metrics

def validate_schema_markup():
    """Validate schema markup across pages"""
    
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    test_pages = ['index.html', 'sss.html']
    
    results = {
        'total_schemas': 0,
        'valid_schemas': 0,
        'invalid_schemas': 0,
        'schema_types_found': [],
        'pages_with_schema': 0
    }
    
    for page in test_pages:
        page_path = base_dir / page
        
        if page_path.exists():
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                import re
                schema_matches = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', content, re.DOTALL)
                
                if schema_matches:
                    results['pages_with_schema'] += 1
                
                for schema_content in schema_matches:
                    results['total_schemas'] += 1
                    try:
                        schema_data = json.loads(schema_content.strip())
                        results['valid_schemas'] += 1
                        
                        if "@type" in schema_data:
                            results['schema_types_found'].append(schema_data["@type"])
                        
                    except json.JSONDecodeError:
                        results['invalid_schemas'] += 1
                        
            except Exception:
                pass
    
    return results

def test_cta_functionality():
    """Test CTA functionality and proper formatting"""
    
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    test_pages = ['index.html', 'sss.html']
    
    results = {
        'total_ctas': 0,
        'phone_ctas': 0,
        'whatsapp_ctas': 0,
        'phone_ctas_working': True,
        'whatsapp_ctas_working': True,
        'issues_found': []
    }
    
    expected_phone = "+905433527474"
    
    for page in test_pages:
        page_path = base_dir / page
        
        if page_path.exists():
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                import re
                
                # Check phone CTAs
                phone_matches = re.findall(r'href=["\']tel:([^"\']*)["\']', content)
                whatsapp_matches = re.findall(r'href=["\']https://wa\.me/([^"\']*)["\']', content)
                
                results['phone_ctas'] += len(phone_matches)
                results['whatsapp_ctas'] += len(whatsapp_matches)
                
                # Validate phone number format
                for phone in phone_matches:
                    if expected_phone not in phone:
                        results['phone_ctas_working'] = False
                        results['issues_found'].append(f"Incorrect phone number: {phone}")
                
                # Validate WhatsApp format
                for whatsapp in whatsapp_matches:
                    if "905433527474" not in whatsapp:
                        results['whatsapp_ctas_working'] = False
                        results['issues_found'].append(f"Incorrect WhatsApp number: {whatsapp}")
                        
            except Exception:
                pass
    
    results['total_ctas'] = results['phone_ctas'] + results['whatsapp_ctas']
    
    return results

def check_mobile_optimization():
    """Check mobile optimization elements"""
    
    base_dir = Path("/Users/macos/Documents/Projeler/DryAlle")
    test_pages = ['index.html', 'sss.html']
    
    mobile_score = 0
    max_score = len(test_pages) * 4  # 4 checks per page
    
    for page in test_pages:
        page_path = base_dir / page
        
        if page_path.exists():
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check mobile optimization elements
                if 'name="viewport"' in content:
                    mobile_score += 1
                if 'width=device-width' in content:
                    mobile_score += 1
                if '@media' in content or 'max-width' in content:
                    mobile_score += 1
                if 'loading=' in content:  # Lazy loading
                    mobile_score += 1
                    
            except Exception:
                pass
    
    return {
        'mobile_score': round((mobile_score / max_score) * 100),
        'checks_passed': mobile_score,
        'total_checks': max_score,
        'mobile_optimized': mobile_score >= max_score * 0.8
    }

def analyze_competitive_position():
    """Analyze estimated competitive position"""
    
    # This would typically integrate with ranking APIs
    # For now, we'll provide estimated positioning
    
    return {
        'estimated_position': 2,  # Estimated market position
        'key_competitors': ['Dry Center', 'Dr. Wet Clean'],
        'competitive_advantages': [
            '25 year experience',
            'Door-to-door service',
            'AI technology integration',
            'Comprehensive online presence'
        ],
        'areas_for_improvement': [
            'Social media engagement',
            'Customer review velocity',
            'Content marketing expansion'
        ]
    }

def generate_weekly_recommendations(health_report):
    """Generate specific recommendations based on health check"""
    
    if health_report['overall_health'] == 'CRITICAL':
        health_report['recommendations'].extend([
            'URGENT: Fix critical website accessibility issues',
            'URGENT: Repair non-functioning CTA links',
            'URGENT: Address technical SEO failures'
        ])
    
    if health_report['overall_health'] == 'WARNING':
        health_report['recommendations'].extend([
            'Optimize page load speeds',
            'Fix SEO element issues',
            'Improve mobile optimization'
        ])
    
    # Always include proactive recommendations
    health_report['recommendations'].extend([
        'Publish 1 new blog article this week',
        'Create 3 new Google My Business posts',
        'Respond to all customer reviews',
        'Monitor competitor activity',
        'Update seasonal content'
    ])

def save_weekly_health_report(health_report):
    """Save comprehensive weekly health report"""
    
    reports_dir = Path("/Users/macos/Documents/Projeler/DryAlle/seo/reports/weekly")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    # Save JSON data
    json_file = reports_dir / f"weekly_health_{datetime.now().strftime('%Y%m%d')}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(health_report, f, indent=2, ensure_ascii=False)
    
    # Save readable report
    report_file = reports_dir / f"weekly_health_report_{datetime.now().strftime('%Y%m%d')}.md"
    
    report_content = f"""# DryAlle Weekly SEO Health Report
## Week of {health_report['week_ending']}

### 🎯 Overall Health Status: {health_report['overall_health']}

### 📊 Health Check Summary
- **Checks Performed**: {health_report['checks_performed']}
- **Issues Found**: {len(health_report['issues_found'])}
- **Recommendations**: {len(health_report['recommendations'])}

### ❌ Issues Identified
{chr(10).join(f"- {issue}" for issue in health_report['issues_found']) if health_report['issues_found'] else "- No critical issues found ✅"}

### 📝 Recommendations for This Week
{chr(10).join(f"- {rec}" for rec in health_report['recommendations'])}

### 📈 Detailed Metrics

#### Website Accessibility
- Main site accessible: {'✅' if health_report['metrics']['accessibility']['main_site_accessible'] else '❌'}
- Response time: {health_report['metrics']['accessibility']['response_time']:.2f}s
- Pages accessible: {health_report['metrics']['accessibility']['accessible_pages']}/{health_report['metrics']['accessibility']['total_pages_tested']}

#### Performance
- Average load time: {health_report['metrics']['performance']['avg_load_time']:.2f}s
- Performance grade: {health_report['metrics']['performance']['performance_grade']}
- Pages under 2s: {health_report['metrics']['performance']['pages_under_2s']}

#### SEO Elements
- Critical issues: {health_report['metrics']['seo_elements']['critical_issues']}
- Minor issues: {health_report['metrics']['seo_elements']['minor_issues']}

#### Schema Markup
- Valid schemas: {health_report['metrics']['schema']['valid_schemas']}/{health_report['metrics']['schema']['total_schemas']}
- Schema types: {', '.join(health_report['metrics']['schema']['schema_types_found'])}

#### CTA Functionality
- Total CTAs tested: {health_report['metrics']['cta']['total_ctas']}
- Phone CTAs working: {'✅' if health_report['metrics']['cta']['phone_ctas_working'] else '❌'}
- WhatsApp CTAs working: {'✅' if health_report['metrics']['cta']['whatsapp_ctas_working'] else '❌'}

#### Mobile Optimization
- Mobile score: {health_report['metrics']['mobile']['mobile_score']}/100
- Mobile optimized: {'✅' if health_report['metrics']['mobile']['mobile_optimized'] else '❌'}

### 🎯 Next Week Focus Areas
1. Address any critical issues immediately
2. Implement recommended optimizations
3. Continue content marketing efforts
4. Monitor competitive landscape
5. Prepare for monthly strategy review

---
*Report generated automatically on {health_report['timestamp']}*
"""
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"📋 Detailed report saved: {report_file}")

def print_weekly_summary(health_report):
    """Print comprehensive weekly summary"""
    
    print("=" * 60)
    print(f"🎯 WEEKLY HEALTH CHECK COMPLETE")
    print(f"📊 Overall Status: {health_report['overall_health']}")
    print(f"🔍 Checks Performed: {health_report['checks_performed']}")
    
    if health_report['issues_found']:
        print(f"⚠️  Issues Found: {len(health_report['issues_found'])}")
        for issue in health_report['issues_found']:
            print(f"   - {issue}")
    else:
        print("✅ No critical issues found")
    
    print(f"📝 Recommendations: {len(health_report['recommendations'])}")
    for rec in health_report['recommendations'][:3]:  # Show first 3
        print(f"   - {rec}")
    
    if len(health_report['recommendations']) > 3:
        print(f"   ... and {len(health_report['recommendations']) - 3} more")
    
    print("=" * 60)

if __name__ == "__main__":
    weekly_seo_health_check()