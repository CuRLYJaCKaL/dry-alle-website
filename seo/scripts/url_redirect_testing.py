#!/usr/bin/env python3
"""
URL Redirect Testing Script
Test 301 redirects from old Turkish URLs to new English slugs
"""

import os
import json
import requests
from datetime import datetime

class URLRedirectTester:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.base_url = "https://dryallekurutemizleme.com"
        
        # Test scenarios - 5 sample redirect cases
        self.test_scenarios = [
            {
                'name': 'Vintage Giyim Özel Bakım',
                'old_url': f"{self.base_url}/blog/vintage-giyim-özel-bakım/",
                'new_url': f"{self.base_url}/blog/vintage-clothing-ozel-care/",
                'expected_status': 301
            },
            {
                'name': 'Düğün Sezonu Gelinlik Bakımı',
                'old_url': f"{self.base_url}/blog/düğün-sezonu-gelinlik-bakımı/", 
                'new_url': f"{self.base_url}/blog/wedding-season-wedding-dress-care/",
                'expected_status': 301
            },
            {
                'name': 'Profesyonel vs Evde Halı Temizliği',
                'old_url': f"{self.base_url}/blog/profesyonel-vs-evde-halı-temizliği/",
                'new_url': f"{self.base_url}/blog/professional-vs-evde-carpet-cleaning-comparison/",
                'expected_status': 301
            },
            {
                'name': 'İpek Kumaş Leke Çıkarma',
                'old_url': f"{self.base_url}/blog/ipek-kumaş-leke-çıkarma/",
                'new_url': f"{self.base_url}/blog/silk-fabric-stain-removal/",
                'expected_status': 301
            },
            {
                'name': 'Kış Montları Özel Temizlik',
                'old_url': f"{self.base_url}/blog/kış-montları-özel-temizlik/",
                'new_url': f"{self.base_url}/blog/winter-coats-special-cleaning/",
                'expected_status': 301
            }
        ]

    def test_url_redirect(self, scenario):
        """Tek URL redirect'ini test et"""
        try:
            # Allow redirects=False to manually check redirect status
            response = requests.get(scenario['old_url'], allow_redirects=False, timeout=10)
            
            test_result = {
                'scenario': scenario['name'],
                'old_url': scenario['old_url'],
                'expected_new_url': scenario['new_url'],
                'expected_status': scenario['expected_status'],
                'actual_status': response.status_code,
                'redirect_url': response.headers.get('Location', ''),
                'test_passed': False,
                'issues': []
            }
            
            # Status code kontrolü
            if response.status_code != scenario['expected_status']:
                test_result['issues'].append(f"Expected status {scenario['expected_status']}, got {response.status_code}")
            
            # Redirect URL kontrolü
            if response.status_code in [301, 302]:
                redirect_url = response.headers.get('Location', '')
                if redirect_url != scenario['new_url']:
                    test_result['issues'].append(f"Redirect URL mismatch: expected {scenario['new_url']}, got {redirect_url}")
                else:
                    # Final URL'e ikinci request gönder
                    final_response = requests.get(redirect_url, timeout=10)
                    test_result['final_status'] = final_response.status_code
                    
                    if final_response.status_code != 200:
                        test_result['issues'].append(f"Final URL returned status {final_response.status_code}")
            
            # Test başarı durumu
            test_result['test_passed'] = len(test_result['issues']) == 0
            
            return test_result
            
        except requests.exceptions.RequestException as e:
            return {
                'scenario': scenario['name'],
                'old_url': scenario['old_url'],
                'test_passed': False,
                'error': str(e),
                'issues': [f"Request failed: {str(e)}"]
            }

    def test_404_handling(self):
        """404 sayfası handling'ini test et"""
        print("🔍 Testing 404 handling...")
        
        # Non-existent URLs
        test_404_urls = [
            f"{self.base_url}/blog/non-existent-page/",
            f"{self.base_url}/blog/invalid-slug-123/",
            f"{self.base_url}/blog/test-404-page/"
        ]
        
        results = []
        
        for url in test_404_urls:
            try:
                response = requests.get(url, timeout=10)
                
                result = {
                    'url': url,
                    'status_code': response.status_code,
                    'expected_status': 404,
                    'test_passed': response.status_code == 404,
                    'has_404_page': '404' in response.text.lower() or 'not found' in response.text.lower()
                }
                
                results.append(result)
                
            except requests.exceptions.RequestException as e:
                results.append({
                    'url': url,
                    'test_passed': False,
                    'error': str(e)
                })
        
        return results

    def test_canonical_urls(self):
        """Canonical URL'leri test et"""
        print("🔗 Testing canonical URLs...")
        
        # Birkaç blog post'un canonical URL'ini test et
        test_urls = [
            f"{self.base_url}/blog/vintage-clothing-ozel-care/",
            f"{self.base_url}/blog/wedding-season-wedding-dress-care/",
            f"{self.base_url}/blog/"
        ]
        
        results = []
        
        for url in test_urls:
            try:
                response = requests.get(url, timeout=10)
                
                # HTML içeriğini parse et
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                canonical_link = soup.find('link', {'rel': 'canonical'})
                
                result = {
                    'url': url,
                    'status_code': response.status_code,
                    'has_canonical': canonical_link is not None,
                    'canonical_url': canonical_link.get('href') if canonical_link else None,
                    'canonical_matches_url': False
                }
                
                if canonical_link:
                    canonical_href = canonical_link.get('href', '')
                    result['canonical_matches_url'] = canonical_href == url
                
                results.append(result)
                
            except Exception as e:
                results.append({
                    'url': url,
                    'error': str(e),
                    'test_passed': False
                })
        
        return results

    def validate_sitemap_urls(self):
        """Sitemap'teki URL'leri doğrula"""
        print("🗺️ Validating sitemap URLs...")
        
        sitemap_path = os.path.join(self.project_root, 'sitemap.xml')
        
        if not os.path.exists(sitemap_path):
            return {'error': 'Sitemap file not found'}
        
        # Sitemap'i parse et
        from xml.etree import ElementTree as ET
        
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            
            # URL'leri çıkar
            urls = []
            for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
                urls.append(url_elem.text)
            
            # İlk 10 URL'i test et (performance için)
            test_urls = urls[:10]
            results = []
            
            for url in test_urls:
                try:
                    response = requests.head(url, timeout=10)  # HEAD request for faster testing
                    
                    results.append({
                        'url': url,
                        'status_code': response.status_code,
                        'accessible': response.status_code == 200,
                        'redirect': response.status_code in [301, 302]
                    })
                    
                except requests.exceptions.RequestException as e:
                    results.append({
                        'url': url,
                        'accessible': False,
                        'error': str(e)
                    })
            
            return {
                'total_urls_in_sitemap': len(urls),
                'tested_urls': len(test_urls),
                'test_results': results,
                'accessibility_rate': len([r for r in results if r.get('accessible', False)]) / len(results) * 100
            }
            
        except Exception as e:
            return {'error': f'Failed to parse sitemap: {str(e)}'}

    def generate_redirect_test_report(self):
        """Kapsamlı redirect test raporu oluştur"""
        print("📊 Generating redirect test report...")
        
        # Ana redirect testleri
        redirect_results = []
        for scenario in self.test_scenarios:
            print(f"Testing: {scenario['name']}")
            result = self.test_url_redirect(scenario)
            redirect_results.append(result)
        
        # 404 handling testleri
        error_handling_results = self.test_404_handling()
        
        # Canonical URL testleri
        canonical_results = self.test_canonical_urls()
        
        # Sitemap URL validation
        sitemap_validation = self.validate_sitemap_urls()
        
        # Rapor oluştur
        report = {
            'test_date': datetime.now().isoformat(),
            'project': 'DryAlle URL Redirect Testing',
            'redirect_tests': {
                'total_scenarios': len(self.test_scenarios),
                'passed_tests': len([r for r in redirect_results if r.get('test_passed', False)]),
                'results': redirect_results
            },
            'error_handling_tests': {
                'total_tests': len(error_handling_results),
                'passed_tests': len([r for r in error_handling_results if r.get('test_passed', False)]),
                'results': error_handling_results
            },
            'canonical_url_tests': {
                'total_tests': len(canonical_results),
                'canonical_coverage': len([r for r in canonical_results if r.get('has_canonical', False)]),
                'results': canonical_results
            },
            'sitemap_validation': sitemap_validation,
            'overall_summary': {
                'redirect_success_rate': 0,
                'error_handling_success_rate': 0,
                'canonical_success_rate': 0,
                'recommendations': []
            }
        }
        
        # Success rate hesaplama
        redirect_success_rate = (report['redirect_tests']['passed_tests'] / 
                               report['redirect_tests']['total_scenarios']) * 100
        report['overall_summary']['redirect_success_rate'] = redirect_success_rate
        
        error_success_rate = (report['error_handling_tests']['passed_tests'] / 
                             report['error_handling_tests']['total_tests']) * 100
        report['overall_summary']['error_handling_success_rate'] = error_success_rate
        
        canonical_success_rate = (report['canonical_url_tests']['canonical_coverage'] / 
                                 report['canonical_url_tests']['total_tests']) * 100
        report['overall_summary']['canonical_success_rate'] = canonical_success_rate
        
        # Öneriler
        if redirect_success_rate < 100:
            report['overall_summary']['recommendations'].append('Fix failing redirect rules')
        
        if error_success_rate < 100:
            report['overall_summary']['recommendations'].append('Improve 404 error handling')
        
        if canonical_success_rate < 90:
            report['overall_summary']['recommendations'].append('Add canonical URLs to more pages')
        
        # Raporu kaydet
        report_path = os.path.join(self.project_root, 'seo/reports/url_redirect_testing.json')
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report_path, report

def main():
    """URL Redirect Testing Execution"""
    print("🔗 URL REDIRECT TESTING & VALIDATION")
    print("=" * 60)
    print("🎯 301 Redirects | 404 Handling | Canonical URLs")
    print("=" * 60)
    
    tester = URLRedirectTester()
    
    try:
        # Comprehensive testing
        report_path, report = tester.generate_redirect_test_report()
        
        # Özet
        print("\n" + "=" * 60)
        print("🔗 URL REDIRECT TESTING TAMAMLANDI")
        print("=" * 60)
        
        redirect_success = report['overall_summary']['redirect_success_rate']
        print(f"✅ Redirect Tests: {redirect_success:.1f}% success rate")
        
        error_success = report['overall_summary']['error_handling_success_rate']
        print(f"✅ 404 Handling: {error_success:.1f}% success rate")
        
        canonical_success = report['overall_summary']['canonical_success_rate']
        print(f"✅ Canonical URLs: {canonical_success:.1f}% coverage")
        
        if 'sitemap_validation' in report and 'accessibility_rate' in report['sitemap_validation']:
            sitemap_success = report['sitemap_validation']['accessibility_rate']
            print(f"✅ Sitemap URLs: {sitemap_success:.1f}% accessible")
        
        print(f"\n📊 TEST SUMMARY:")
        print(f"   🔗 Total redirect scenarios: {report['redirect_tests']['total_scenarios']}")
        print(f"   ✅ Passed redirects: {report['redirect_tests']['passed_tests']}")
        print(f"   🚫 404 tests: {report['error_handling_tests']['total_tests']}")
        print(f"   📋 Canonical tests: {report['canonical_url_tests']['total_tests']}")
        
        if report['overall_summary']['recommendations']:
            print(f"\n🔧 RECOMMENDATIONS:")
            for i, rec in enumerate(report['overall_summary']['recommendations'], 1):
                print(f"   {i}. {rec}")
        
        print(f"\n📋 Detailed Report: {report_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Testing error: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)