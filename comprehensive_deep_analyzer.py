#!/usr/bin/env python3
"""
DryAlle Comprehensive Deep Analyzer
Her sayfayı detaylı analiz eder, hiçbirini atlamaz
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

class DeepPageAnalyzer:
    def __init__(self):
        self.all_pages = []
        self.analysis_results = {}
        
    def extract_all_meta_tags(self, content):
        """Tüm meta tagleri çıkar"""
        meta_pattern = r'<meta\s+([^>]+)>'
        metas = re.findall(meta_pattern, content, re.IGNORECASE)
        
        meta_dict = {}
        for meta in metas:
            # name="..." content="..." pattern
            name_match = re.search(r'name=["\']([^"\']+)["\']', meta)
            content_match = re.search(r'content=["\']([^"\']*)["\']', meta)
            
            if name_match and content_match:
                meta_dict[name_match.group(1)] = content_match.group(1)
        
        return meta_dict
    
    def extract_title_and_description(self, content):
        """Title ve description çıkar"""
        title_match = re.search(r'<title>([^<]*)</title>', content, re.IGNORECASE)
        title = title_match.group(1) if title_match else ""
        
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', content, re.IGNORECASE)
        description = desc_match.group(1) if desc_match else ""
        
        return title, description
    
    def check_critical_css_inline(self, content):
        """Critical CSS inline kontrolü"""
        has_style_tag = '<style>' in content and 'Critical above-the-fold styles' in content
        has_css_vars = ':root{--color-primary:#006a44' in content
        has_mobile_styles = '@media (max-width:767px)' in content
        
        return {
            'has_inline_styles': has_style_tag,
            'has_css_variables': has_css_vars,
            'has_mobile_styles': has_mobile_styles,
            'score': sum([has_style_tag, has_css_vars, has_mobile_styles])
        }
    
    def check_geo_location_signals(self, content):
        """Geo location sinyalleri kontrolü"""
        checks = {
            'geo_region': 'geo.region' in content and 'TR-34' in content,
            'geo_placename': 'geo.placename' in content,
            'geo_position': 'geo.position' in content,
            'icbm': 'ICBM' in content,
            'location_tracking': 'data-location-verified' in content
        }
        
        return {
            'checks': checks,
            'score': sum(checks.values()),
            'total': len(checks)
        }
    
    def check_performance_optimizations(self, content):
        """Performance optimizasyonları kontrolü"""
        checks = {
            'font_preload': 'Font Loading Optimization for Mobile Performance' in content,
            'critical_css': 'Critical CSS for LCP Optimization' in content,
            'service_worker': 'serviceWorker' in content and 'navigator.serviceWorker.register' in content,
            'web_vitals': 'Web Vitals ready for 2025 Google ranking factors' in content,
            'lcp_attributes': 'data-lcp-candidate="true"' in content and 'data-above-fold="true"' in content,
            'mobile_optimized': 'data-mobile-optimized="true"' in content
        }
        
        return {
            'checks': checks,
            'score': sum(checks.values()),
            'total': len(checks)
        }
    
    def check_pwa_signals(self, content):
        """PWA sinyalleri kontrolü"""
        checks = {
            'mobile_web_app_title': 'mobile-web-app-title' in content,
            'apple_touch_fullscreen': 'apple-touch-fullscreen' in content,
            'format_detection': 'format-detection' in content,
            'theme_color': 'theme-color' in content,
            'apple_mobile_capable': 'apple-mobile-web-app-capable' in content,
            'msapplication_tile': 'msapplication-TileColor' in content
        }
        
        return {
            'checks': checks,
            'score': sum(checks.values()),
            'total': len(checks)
        }
    
    def extract_location_info(self, filename, content):
        """Lokasyon bilgilerini çıkar"""
        # Filename'den lokasyon
        location_from_filename = None
        service_from_filename = None
        
        base = filename.replace('.html', '')
        
        # Service tespiti
        if 'kuru-temizleme' in base:
            service_from_filename = 'kuru-temizleme'
        elif 'koltuk-yikama' in base:
            service_from_filename = 'koltuk-yikama'
        elif 'hali-yikama' in base:
            service_from_filename = 'hali-yikama'
        elif 'premium' in base or 'luxury' in base:
            service_from_filename = 'premium-service'
        elif 'gelinlik' in base:
            service_from_filename = 'gelinlik-temizleme'
        elif 'haute-couture' in base:
            service_from_filename = 'haute-couture'
        else:
            service_from_filename = 'specialized-service'
        
        # Lokasyon tespiti
        locations = ['acibadem', 'altunizade', 'atasehir', 'bagdat-caddesi', 'barbaros', 'bostanci', 
                    'caddebostan', 'camlica', 'erenkoy', 'fenerbahce', 'fikirtepe', 'goztepe', 
                    'icerenkoy', 'kadikoy', 'kalamis', 'kartal', 'kozyatagi', 'kucukbakkalkoy', 
                    'maltepe', 'moda', 'pendik', 'sahrayicedit', 'suadiye', 'umraniye', 'uskudar']
        
        for loc in locations:
            if base.startswith(loc):
                location_from_filename = loc
                break
        
        # Content'ten koordinatlar
        geo_pos_match = re.search(r'geo\.position["\']?\s*content=["\']([^"\']*)["\']', content)
        coordinates = geo_pos_match.group(1) if geo_pos_match else ""
        
        # Content'ten placename
        placename_match = re.search(r'geo\.placename["\']?\s*content=["\']([^"\']*)["\']', content)
        placename = placename_match.group(1) if placename_match else ""
        
        return {
            'location_from_filename': location_from_filename,
            'service_from_filename': service_from_filename,
            'coordinates': coordinates,
            'placename': placename
        }
    
    def check_schema_markup(self, content):
        """Schema markup kontrolü"""
        has_local_business = 'LocalBusiness' in content
        has_webpage = 'WebPage' in content
        has_breadcrumb = 'BreadcrumbList' in content
        
        # JSON-LD sayısı
        json_ld_count = content.count('application/ld+json')
        
        return {
            'has_local_business': has_local_business,
            'has_webpage': has_webpage,
            'has_breadcrumb': has_breadcrumb,
            'json_ld_count': json_ld_count,
            'score': sum([has_local_business, has_webpage, has_breadcrumb])
        }
    
    def analyze_single_page(self, file_path):
        """Tek sayfayı derinlemesine analiz et"""
        filename = os.path.basename(file_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Temel bilgiler
            title, description = self.extract_title_and_description(content)
            meta_tags = self.extract_all_meta_tags(content)
            
            # Detaylı analizler
            critical_css = self.check_critical_css_inline(content)
            geo_signals = self.check_geo_location_signals(content)
            performance = self.check_performance_optimizations(content)
            pwa_signals = self.check_pwa_signals(content)
            location_info = self.extract_location_info(filename, content)
            schema_markup = self.check_schema_markup(content)
            
            # Genel skor hesaplama
            total_possible = (
                critical_css['score'] + 
                geo_signals['total'] + 
                performance['total'] + 
                pwa_signals['total'] + 
                schema_markup['score']
            )
            
            total_achieved = (
                critical_css['score'] + 
                geo_signals['score'] + 
                performance['score'] + 
                pwa_signals['score'] + 
                schema_markup['score']
            )
            
            overall_score = (total_achieved / total_possible * 100) if total_possible > 0 else 0
            
            return {
                'filename': filename,
                'title': title,
                'description': description,
                'meta_tags_count': len(meta_tags),
                'critical_css': critical_css,
                'geo_signals': geo_signals,
                'performance': performance,
                'pwa_signals': pwa_signals,
                'location_info': location_info,
                'schema_markup': schema_markup,
                'overall_score': round(overall_score, 1),
                'total_achieved': total_achieved,
                'total_possible': total_possible,
                'status': 'PERFECT' if overall_score >= 95 else 'NEEDS_ATTENTION'
            }
            
        except Exception as e:
            return {
                'filename': filename,
                'error': str(e),
                'status': 'ERROR'
            }
    
    def analyze_all_pages(self):
        """Tüm sayfaları analiz et"""
        bolgeler_dir = Path('/Users/macos/Documents/Projeler/DryAlle/bolgeler')
        html_files = sorted([f for f in bolgeler_dir.glob('*.html')])
        
        print(f"🔍 STARTING COMPREHENSIVE DEEP ANALYSIS OF {len(html_files)} PAGES...")
        print("=" * 80)
        
        results = []
        perfect_count = 0
        
        for i, file_path in enumerate(html_files, 1):
            print(f"\\n📄 ANALYZING {i:2d}/41: {file_path.name}")
            print("-" * 50)
            
            result = self.analyze_single_page(file_path)
            results.append(result)
            
            if result.get('status') == 'PERFECT':
                perfect_count += 1
                print(f"✅ PERFECT SCORE: {result.get('overall_score', 0)}%")
            elif result.get('status') == 'ERROR':
                print(f"❌ ERROR: {result.get('error', 'Unknown error')}")
            else:
                print(f"⚠️  NEEDS ATTENTION: {result.get('overall_score', 0)}%")
                
                # Eksik olanları göster
                if 'geo_signals' in result:
                    failed_geo = [k for k, v in result['geo_signals']['checks'].items() if not v]
                    if failed_geo:
                        print(f"   📍 Missing geo signals: {', '.join(failed_geo)}")
                
                if 'performance' in result:
                    failed_perf = [k for k, v in result['performance']['checks'].items() if not v]
                    if failed_perf:
                        print(f"   ⚡ Missing performance: {', '.join(failed_perf)}")
                
                if 'pwa_signals' in result:
                    failed_pwa = [k for k, v in result['pwa_signals']['checks'].items() if not v]
                    if failed_pwa:
                        print(f"   📱 Missing PWA signals: {', '.join(failed_pwa)}")
        
        # Final rapor
        print("\\n" + "=" * 80)
        print(f"📊 COMPREHENSIVE ANALYSIS COMPLETE")
        print(f"✅ Perfect pages: {perfect_count}/41")
        print(f"📈 Success rate: {perfect_count/41*100:.1f}%")
        
        if perfect_count < 41:
            needs_attention = [r for r in results if r.get('status') == 'NEEDS_ATTENTION']
            print(f"\\n⚠️  PAGES NEEDING ATTENTION ({len(needs_attention)}):")
            for result in needs_attention:
                print(f"   - {result['filename']}: {result.get('overall_score', 0)}%")
        
        return results

def main():
    analyzer = DeepPageAnalyzer()
    results = analyzer.analyze_all_pages()
    
    # Sonuçları JSON olarak kaydet
    with open('/Users/macos/Documents/Projeler/DryAlle/deep_analysis_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\\n💾 Detailed results saved to: deep_analysis_results.json")

if __name__ == "__main__":
    main()