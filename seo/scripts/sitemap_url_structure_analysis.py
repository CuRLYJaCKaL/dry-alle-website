#!/usr/bin/env python3
"""
Sitemap URL Yapısı Analizi ve Düzeltme
SEO dostu URL yapısı analizi ve optimizasyon önerileri
"""

import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import re
from urllib.parse import urlparse

class SitemapURLAnalyzer:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.base_url = "https://dryallekurutemizleme.com"
        
        # SEO dostu URL kriterleri
        self.url_criteria = {
            'length': {'max': 100, 'recommended': 60},
            'structure': {
                'use_hyphens': True,
                'avoid_underscores': True,
                'lowercase_only': True,
                'no_special_chars': True
            },
            'readability': {
                'descriptive': True,
                'hierarchical': True,
                'logical_structure': True
            }
        }

    def find_sitemap_files(self):
        """Sitemap dosyalarını bul"""
        sitemap_files = []
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if 'sitemap' in file.lower() and file.endswith('.xml'):
                    sitemap_files.append(os.path.join(root, file))
        
        return sitemap_files

    def analyze_sitemap_urls(self, sitemap_path):
        """Sitemap URL'lerini analiz et"""
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            
            # XML namespace handling
            namespaces = {'': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            urls = []
            
            for url_elem in root.findall('.//loc', namespaces):
                if url_elem.text:
                    urls.append(url_elem.text)
            
            # Namespace yoksa standart parsing
            if not urls:
                for url_elem in root.findall('.//loc'):
                    if url_elem.text:
                        urls.append(url_elem.text)
            
            return urls
            
        except Exception as e:
            print(f"Sitemap parsing error: {e}")
            return []

    def analyze_url_quality(self, url):
        """URL kalitesini analiz et"""
        parsed = urlparse(url)
        path = parsed.path
        
        analysis = {
            'url': url,
            'path': path,
            'issues': [],
            'score': 100,
            'recommendations': []
        }
        
        # URL uzunluğu kontrolü
        if len(url) > self.url_criteria['length']['max']:
            analysis['issues'].append('URL too long')
            analysis['score'] -= 20
            analysis['recommendations'].append(f'Shorten URL to under {self.url_criteria["length"]["max"]} characters')
        
        # Path structure analizi
        path_segments = [seg for seg in path.split('/') if seg]
        
        # Generated pages problemi
        if 'generated_pages' in path:
            analysis['issues'].append('Contains "generated_pages" in path - not SEO friendly')
            analysis['score'] -= 30
            analysis['recommendations'].append('Move to logical directory structure like /bolgeler/kadikoy/')
        
        # URL structure problems
        if any(seg for seg in path_segments if len(seg) > 50):
            analysis['issues'].append('URL segment too long')
            analysis['score'] -= 15
            analysis['recommendations'].append('Break long segments into shorter, descriptive parts')
        
        # Underscore vs hyphen
        if '_' in path:
            analysis['issues'].append('Contains underscores instead of hyphens')
            analysis['score'] -= 10
            analysis['recommendations'].append('Replace underscores with hyphens for better SEO')
        
        # Turkish characters
        if re.search(r'[çğıöşüÇĞIİÖŞÜ]', path):
            analysis['issues'].append('Contains Turkish characters')
            analysis['score'] -= 10
            analysis['recommendations'].append('Use URL-safe ASCII characters')
        
        # Concatenated words without hyphens
        concatenated_pattern = r'/[a-z]+[A-Z][a-z]+|/[a-z]{10,}/'
        if re.search(concatenated_pattern, path):
            analysis['issues'].append('Concatenated words without proper separation')
            analysis['score'] -= 15
            analysis['recommendations'].append('Separate words with hyphens for readability')
        
        return analysis

    def generate_improved_url_structure(self, problematic_urls):
        """İyileştirilmiş URL yapısı öner"""
        improved_urls = {}
        
        for url_analysis in problematic_urls:
            original_url = url_analysis['url']
            path = url_analysis['path']
            
            # Parse the original path
            if 'generated_pages' in path:
                # Extract meaningful parts
                filename = os.path.basename(path)
                name_part = filename.replace('.html', '')
                
                # Fix specific cases
                if 'bolgeler' in name_part:
                    improved_path = self.fix_bolgeler_url(name_part)
                else:
                    improved_path = self.fix_generic_url(name_part)
                
                improved_url = f"{self.base_url}{improved_path}"
                
                improved_urls[original_url] = {
                    'original': original_url,
                    'improved': improved_url,
                    'improvement_type': 'Structure and readability',
                    'seo_score_improvement': '+40 points'
                }
        
        return improved_urls

    def fix_bolgeler_url(self, name_part):
        """Bölgeler URL'lerini düzelt"""
        # Example: bolgelerkadikoysuadiye-utu-hizmetleri
        # Should become: /bolgeler/kadikoy/suadiye-utu-hizmetleri.html
        
        # Extract parts
        if 'bolgeler' in name_part:
            parts = name_part.replace('bolgeler', '').strip()
            
            # Common district patterns
            district_map = {
                'kadikoy': 'kadikoy',
                'atasehir': 'atasehir',
                'uskudar': 'uskudar',
                'besiktas': 'besiktas',
                'sisli': 'sisli',
                'beyoglu': 'beyoglu'
            }
            
            service_part = None
            district = None
            neighborhood = None
            
            # Find district
            for key, value in district_map.items():
                if key in parts.lower():
                    district = value
                    # Extract remaining parts
                    remaining = parts.lower().replace(key, '')
                    break
            
            if district:
                # Extract service and neighborhood
                if '-' in remaining:
                    parts_list = remaining.split('-')
                    if len(parts_list) > 1:
                        neighborhood = parts_list[0].strip()
                        service_part = '-'.join(parts_list[1:]).strip()
                
                if neighborhood and service_part:
                    return f"/bolgeler/{district}/{neighborhood}-{service_part}.html"
                elif service_part:
                    return f"/bolgeler/{district}/{service_part}.html"
        
        # Fallback
        return f"/hizmetler/{self.clean_url_segment(name_part)}.html"

    def fix_generic_url(self, name_part):
        """Genel URL'leri düzelt"""
        # Clean and structure the URL
        cleaned = self.clean_url_segment(name_part)
        
        # Categorize by content type
        if any(keyword in cleaned for keyword in ['utu', 'utuleme']):
            return f"/hizmetler/utu/{cleaned}.html"
        elif any(keyword in cleaned for keyword in ['kuru-temizleme', 'dry-cleaning']):
            return f"/hizmetler/kuru-temizleme/{cleaned}.html"
        elif any(keyword in cleaned for keyword in ['hali', 'carpet']):
            return f"/hizmetler/hali-yikama/{cleaned}.html"
        elif any(keyword in cleaned for keyword in ['perde', 'curtain']):
            return f"/hizmetler/perde-temizleme/{cleaned}.html"
        else:
            return f"/hizmetler/{cleaned}.html"

    def clean_url_segment(self, segment):
        """URL segmentini temizle"""
        # Remove special characters and normalize
        cleaned = re.sub(r'[^a-zA-Z0-9\-]', '', segment)
        
        # Add hyphens between concatenated words
        cleaned = re.sub(r'([a-z])([A-Z])', r'\1-\2', cleaned)
        
        # Convert to lowercase
        cleaned = cleaned.lower()
        
        # Remove multiple hyphens
        cleaned = re.sub(r'-+', '-', cleaned)
        
        # Remove leading/trailing hyphens
        cleaned = cleaned.strip('-')
        
        return cleaned

    def create_url_improvement_report(self):
        """URL iyileştirme raporu oluştur"""
        
        # Sitemap dosyalarını bul
        sitemap_files = self.find_sitemap_files()
        
        all_urls = []
        for sitemap_file in sitemap_files:
            urls = self.analyze_sitemap_urls(sitemap_file)
            all_urls.extend(urls)
        
        # URL'leri analiz et
        url_analyses = []
        problematic_urls = []
        
        for url in all_urls:
            analysis = self.analyze_url_quality(url)
            url_analyses.append(analysis)
            
            if analysis['score'] < 80:
                problematic_urls.append(analysis)
        
        # İyileştirme önerileri
        improved_urls = self.generate_improved_url_structure(problematic_urls)
        
        # Comprehensive report
        report = {
            'analysis_date': datetime.now().isoformat(),
            'project': 'DryAlle Sitemap URL Structure Analysis',
            'summary': {
                'total_urls_analyzed': len(all_urls),
                'problematic_urls_count': len(problematic_urls),
                'avg_url_score': sum(a['score'] for a in url_analyses) / len(url_analyses) if url_analyses else 0,
                'improvement_potential': len(improved_urls)
            },
            'problematic_urls': problematic_urls,
            'improved_url_suggestions': improved_urls,
            'seo_recommendations': {
                'immediate_actions': [
                    'Move files from /seo/outputs/generated_pages/ to proper directory structure',
                    'Implement 301 redirects from old URLs to new URLs',
                    'Update internal links to use new URL structure',
                    'Update sitemap.xml with new URLs'
                ],
                'url_structure_guidelines': [
                    'Use descriptive, hierarchical URLs',
                    'Keep URLs under 60 characters when possible',
                    'Use hyphens to separate words',
                    'Avoid special characters and numbers',
                    'Make URLs readable and logical'
                ],
                'best_practices': [
                    'Group related content in logical directories',
                    'Use consistent naming conventions',
                    'Implement breadcrumb navigation matching URL structure',
                    'Ensure URL structure reflects site architecture'
                ]
            },
            'implementation_priority': {
                'high_priority': [
                    {
                        'issue': 'generated_pages directory structure',
                        'impact': 'Very poor SEO and user experience',
                        'urls_affected': len([u for u in problematic_urls if 'generated_pages' in u['path']]),
                        'action': 'Immediate restructuring required'
                    }
                ],
                'medium_priority': [
                    {
                        'issue': 'Long URL segments',
                        'impact': 'Poor readability and SEO',
                        'urls_affected': len([u for u in problematic_urls if any('too long' in issue for issue in u['issues'])]),
                        'action': 'Shorten and optimize URLs'
                    }
                ]
            }
        }
        
        return report

    def save_analysis_report(self):
        """Analiz raporunu kaydet"""
        report = self.create_url_improvement_report()
        
        # JSON raporu kaydet
        reports_dir = os.path.join(self.project_root, 'seo/reports')
        os.makedirs(reports_dir, exist_ok=True)
        
        report_path = os.path.join(reports_dir, 'sitemap_url_structure_analysis.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report_path, report

def main():
    """Sitemap URL Yapısı Analizi"""
    print("🔗 SITEMAP URL YAPISI ANALİZİ")
    print("=" * 60)
    print("🎯 SEO URL Quality | Structure Analysis | Optimization")
    print("=" * 60)
    
    analyzer = SitemapURLAnalyzer()
    
    try:
        # Analiz raporunu oluştur
        report_path, report = analyzer.save_analysis_report()
        
        # Özet
        print("\n" + "=" * 60)
        print("🔗 SITEMAP URL ANALİZİ TAMAMLANDI")
        print("=" * 60)
        
        summary = report['summary']
        print(f"✅ Toplam URL analiz edildi: {summary['total_urls_analyzed']}")
        print(f"❌ Problemli URL sayısı: {summary['problematic_urls_count']}")
        print(f"📊 Ortalama URL skoru: {summary['avg_url_score']:.1f}/100")
        print(f"🔧 İyileştirme potansiyeli: {summary['improvement_potential']} URL")
        
        # Yüksek öncelikli problemler
        priority = report['implementation_priority']['high_priority']
        if priority:
            print(f"\n🔴 YÜKSEK ÖNCELİKLİ PROBLEMLER:")
            for issue in priority:
                print(f"   • {issue['issue']}: {issue['urls_affected']} URL etkilendi")
                print(f"     Impact: {issue['impact']}")
        
        # İyileştirme örnekleri
        improved = report['improved_url_suggestions']
        if improved:
            print(f"\n🔧 URL İYİLEŞTİRME ÖRNEKLERİ:")
            for i, (original, data) in enumerate(list(improved.items())[:3], 1):
                print(f"   {i}. Öncesi: {original}")
                print(f"      Sonrası: {data['improved']}")
                print(f"      İyileştirme: {data['seo_score_improvement']}")
        
        # Öneriler
        recommendations = report['seo_recommendations']
        print(f"\n💡 HEMEN YAPILMASI GEREKENLER:")
        for action in recommendations['immediate_actions'][:3]:
            print(f"   • {action}")
        
        print(f"\n📋 URL YAPISI KURALLARI:")
        for guideline in recommendations['url_structure_guidelines'][:3]:
            print(f"   • {guideline}")
        
        print(f"\n📁 RAPOR DOSYASI:")
        print(f"   📊 Detaylı Analiz: {report_path}")
        
        print(f"\n🎯 KRİTİK SORUN:")
        print(f"   ❌ /seo/outputs/generated_pages/ yapısı SEO için çok kötü")
        print(f"   ✅ /bolgeler/kadikoy/suadiye-utu-hizmetleri.html şeklinde olmalı")
        print(f"   🔄 301 redirect'ler ile geçiş planlanmalı")
        
        print(f"\n🎉 URL YAPISI ANALİZİ HAZIR!")
        print(f"   • Mevcut URL problemleri tespit edildi")
        print(f"   • SEO dostu alternatifler önerildi")
        print(f"   • Uygulama öncelikleri belirlendi")
        
        return True
        
    except Exception as e:
        print(f"❌ URL analiz hatası: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)