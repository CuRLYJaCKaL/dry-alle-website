#!/usr/bin/env python3
"""
DryAlle Kuru Temizleme - Kapsamlı SEO ve Google Görünürlük Analizi
Bu araç 41 bölge sayfası için detaylı SEO analizi yapar.
"""

import os
import json
import re
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import statistics
from collections import Counter
import html

class ComprehensiveSEOAnalyzer:
    def __init__(self, base_dir="/Users/macos/Documents/Projeler/DryAlle/bolgeler"):
        self.base_dir = base_dir
        self.domain = "dryallekurutemizleme.com"
        self.base_url = f"https://{self.domain}"
        
        # Yeni eklenen 5 sayfa
        self.new_pages = [
            'atasehir-koltuk-yikama.html',
            'caddebostan-koltuk-yikama.html', 
            'suadiye-koltuk-yikama.html',
            'fenerbahce-hali-yikama.html',
            'fenerbahce-koltuk-yikama.html'
        ]
        
        # Ana hedef kelimeler
        self.target_keywords = {
            'koltuk-yikama': ['koltuk yıkama', 'koltuk temizleme', 'kanepe yıkama'],
            'hali-yikama': ['halı yıkama', 'halı temizleme'],
            'kuru-temizleme': ['kuru temizleme', 'dry cleaning'],
            'premium-temizlik': ['premium temizlik', 'lüks temizlik'],
            'luxury-hizmet': ['luxury hizmet', 'vip temizlik']
        }
        
        self.results = {}
        
    def analyze_html_file(self, filename):
        """Tek bir HTML dosyasını analiz et"""
        filepath = os.path.join(self.base_dir, filename)
        
        if not os.path.exists(filepath):
            return None
            
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        analysis = {
            'filename': filename,
            'is_new_page': filename in self.new_pages,
            'url': f"{self.base_url}/bolgeler/{filename}",
            'seo_metrics': self.analyze_seo_metrics(soup, content),
            'technical_seo': self.analyze_technical_seo(soup, content),
            'content_analysis': self.analyze_content(soup, content),
            'local_seo': self.analyze_local_seo(soup, content),
            'schema_markup': self.analyze_schema_markup(soup),
            'internal_links': self.analyze_internal_links(soup),
            'recommendations': []
        }
        
        # Sayfa skorunu hesapla
        analysis['seo_score'] = self.calculate_seo_score(analysis)
        
        # Önerileri oluştur
        analysis['recommendations'] = self.generate_recommendations(analysis)
        
        return analysis
    
    def analyze_seo_metrics(self, soup, content):
        """Temel SEO metrikleri analizi"""
        # Title analizi
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else ""
        
        # Meta description analizi
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc.get('content', '') if meta_desc else ""
        
        # Meta keywords
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        keywords = meta_keywords.get('content', '') if meta_keywords else ""
        
        # H1 analizi
        h1_tags = soup.find_all('h1')
        h1_count = len(h1_tags)
        h1_text = [h1.get_text().strip() for h1 in h1_tags]
        
        # Diğer başlık etiketleri
        heading_structure = {}
        for i in range(1, 7):
            headings = soup.find_all(f'h{i}')
            heading_structure[f'h{i}'] = {
                'count': len(headings),
                'texts': [h.get_text().strip() for h in headings]
            }
        
        # Kelime sayısı (sadece görünür metin)
        visible_text = soup.get_text()
        word_count = len(visible_text.split())
        
        return {
            'title': {
                'text': title,
                'length': len(title),
                'optimal': 50 <= len(title) <= 60,
                'contains_brand': 'DryAlle' in title or 'Kuru Temizleme' in title
            },
            'meta_description': {
                'text': description,
                'length': len(description),
                'optimal': 150 <= len(description) <= 160,
                'exists': bool(description)
            },
            'meta_keywords': {
                'text': keywords,
                'exists': bool(keywords)
            },
            'h1': {
                'count': h1_count,
                'texts': h1_text,
                'optimal': h1_count == 1
            },
            'heading_structure': heading_structure,
            'word_count': word_count,
            'content_length_optimal': word_count >= 300
        }
    
    def analyze_technical_seo(self, soup, content):
        """Teknik SEO analizi"""
        # Meta viewport
        viewport = soup.find('meta', attrs={'name': 'viewport'})
        has_viewport = bool(viewport)
        
        # Language
        html_tag = soup.find('html')
        lang = html_tag.get('lang', '') if html_tag else ""
        
        # Canonical URL
        canonical = soup.find('link', attrs={'rel': 'canonical'})
        has_canonical = bool(canonical)
        canonical_url = canonical.get('href', '') if canonical else ""
        
        # Meta robots
        robots = soup.find('meta', attrs={'name': 'robots'})
        robots_content = robots.get('content', '') if robots else ""
        
        # Open Graph tags
        og_tags = {}
        for og in soup.find_all('meta', attrs={'property': re.compile(r'^og:')}):
            og_tags[og.get('property')] = og.get('content')
        
        # Twitter Card tags
        twitter_tags = {}
        for tw in soup.find_all('meta', attrs={'name': re.compile(r'^twitter:')}):
            twitter_tags[tw.get('name')] = tw.get('content')
        
        # Image alt texts
        images = soup.find_all('img')
        image_analysis = {
            'total_images': len(images),
            'images_with_alt': len([img for img in images if img.get('alt')]),
            'images_without_alt': len([img for img in images if not img.get('alt')])
        }
        
        return {
            'mobile_friendly': {
                'has_viewport': has_viewport,
                'viewport_content': viewport.get('content', '') if viewport else ""
            },
            'language': {
                'declared': bool(lang),
                'lang_code': lang
            },
            'canonical': {
                'exists': has_canonical,
                'url': canonical_url
            },
            'robots': {
                'exists': bool(robots),
                'content': robots_content
            },
            'open_graph': og_tags,
            'twitter_cards': twitter_tags,
            'images': image_analysis
        }
    
    def analyze_content(self, soup, content):
        """İçerik analizi"""
        visible_text = soup.get_text().lower()
        
        # Hedef kelime yoğunluğu analizi
        keyword_density = {}
        for category, keywords in self.target_keywords.items():
            for keyword in keywords:
                count = visible_text.count(keyword.lower())
                density = (count * len(keyword.split())) / len(visible_text.split()) * 100
                keyword_density[keyword] = {
                    'count': count,
                    'density': round(density, 2)
                }
        
        # İçerik kalitesi göstergeleri
        paragraphs = soup.find_all('p')
        avg_paragraph_length = statistics.mean([len(p.get_text().split()) for p in paragraphs]) if paragraphs else 0
        
        # Liste kullanımı
        lists = soup.find_all(['ul', 'ol'])
        
        # Güçlü/vurgu etiketleri
        strong_tags = soup.find_all(['strong', 'b'])
        em_tags = soup.find_all(['em', 'i'])
        
        return {
            'keyword_density': keyword_density,
            'readability': {
                'paragraph_count': len(paragraphs),
                'avg_paragraph_length': round(avg_paragraph_length, 1),
                'list_count': len(lists),
                'emphasis_tags': len(strong_tags) + len(em_tags)
            }
        }
    
    def analyze_local_seo(self, soup, content):
        """Yerel SEO sinyalleri analizi"""
        text_content = soup.get_text().lower()
        
        # Bölge adı çıkarımı
        filename_parts = soup.find('title').text.lower() if soup.find('title') else ""
        
        # NAP (Name, Address, Phone) bilgileri
        phone_pattern = r'(\+90|0)?\s*\(?\d{3}\)?\s*\d{3}\s*\d{2}\s*\d{2}'
        phones = re.findall(phone_pattern, content)
        
        # Adres göstergeleri
        address_keywords = ['adres', 'address', 'konum', 'location', 'harita']
        has_address_info = any(keyword in text_content for keyword in address_keywords)
        
        # Çalışma saatleri
        hours_keywords = ['saat', 'açık', 'kapalı', 'çalışma']
        has_hours_info = any(keyword in text_content for keyword in hours_keywords)
        
        return {
            'phone_numbers': phones,
            'has_address_info': has_address_info,
            'has_hours_info': has_hours_info,
            'local_keywords_found': len([k for k in address_keywords if k in text_content])
        }
    
    def analyze_schema_markup(self, soup):
        """Schema.org markup analizi"""
        # JSON-LD Schema
        json_ld_scripts = soup.find_all('script', type='application/ld+json')
        schemas = []
        
        for script in json_ld_scripts:
            try:
                schema_data = json.loads(script.string)
                if isinstance(schema_data, dict):
                    schemas.append(schema_data.get('@type', 'Unknown'))
                elif isinstance(schema_data, list):
                    for item in schema_data:
                        if isinstance(item, dict):
                            schemas.append(item.get('@type', 'Unknown'))
            except json.JSONDecodeError:
                continue
        
        # Microdata
        microdata_items = soup.find_all(attrs={'itemtype': True})
        microdata_types = [item.get('itemtype', '').split('/')[-1] for item in microdata_items]
        
        return {
            'json_ld': {
                'count': len(json_ld_scripts),
                'types': schemas
            },
            'microdata': {
                'count': len(microdata_items),
                'types': microdata_types
            },
            'total_schema_types': len(set(schemas + microdata_types))
        }
    
    def analyze_internal_links(self, soup):
        """İç bağlantı yapısı analizi"""
        links = soup.find_all('a', href=True)
        
        internal_links = []
        external_links = []
        
        for link in links:
            href = link.get('href', '')
            if href.startswith('http'):
                if self.domain in href:
                    internal_links.append(href)
                else:
                    external_links.append(href)
            elif href.startswith('/') or not href.startswith('http'):
                internal_links.append(href)
        
        return {
            'total_links': len(links),
            'internal_links': len(internal_links),
            'external_links': len(external_links),
            'internal_link_ratio': round(len(internal_links) / len(links) * 100, 1) if links else 0
        }
    
    def calculate_seo_score(self, analysis):
        """SEO skorunu hesapla (0-100)"""
        score = 0
        max_score = 0
        
        # Title optimizasyonu (15 puan)
        max_score += 15
        if analysis['seo_metrics']['title']['optimal']:
            score += 15
        elif analysis['seo_metrics']['title']['length'] > 0:
            score += 8
        
        # Meta description (15 puan)
        max_score += 15
        if analysis['seo_metrics']['meta_description']['optimal']:
            score += 15
        elif analysis['seo_metrics']['meta_description']['exists']:
            score += 8
        
        # H1 optimizasyonu (10 puan)
        max_score += 10
        if analysis['seo_metrics']['h1']['optimal']:
            score += 10
        elif analysis['seo_metrics']['h1']['count'] > 0:
            score += 5
        
        # İçerik uzunluğu (10 puan)
        max_score += 10
        if analysis['seo_metrics']['content_length_optimal']:
            score += 10
        elif analysis['seo_metrics']['word_count'] > 150:
            score += 5
        
        # Teknik SEO (20 puan)
        max_score += 20
        if analysis['technical_seo']['mobile_friendly']['has_viewport']:
            score += 5
        if analysis['technical_seo']['canonical']['exists']:
            score += 5
        if analysis['technical_seo']['language']['declared']:
            score += 5
        if analysis['technical_seo']['images']['total_images'] == analysis['technical_seo']['images']['images_with_alt']:
            score += 5
        
        # Schema markup (15 puan)
        max_score += 15
        if analysis['schema_markup']['total_schema_types'] >= 3:
            score += 15
        elif analysis['schema_markup']['total_schema_types'] >= 1:
            score += 8
        
        # İç bağlantılar (15 puan)
        max_score += 15
        if analysis['internal_links']['internal_links'] >= 5:
            score += 15
        elif analysis['internal_links']['internal_links'] >= 2:
            score += 8
        
        return round((score / max_score) * 100, 1) if max_score > 0 else 0
    
    def generate_recommendations(self, analysis):
        """Öneriler oluştur"""
        recommendations = []
        
        # Title önerileri
        if not analysis['seo_metrics']['title']['optimal']:
            if analysis['seo_metrics']['title']['length'] == 0:
                recommendations.append("KRITIK: Title etiketi eksik")
            elif analysis['seo_metrics']['title']['length'] < 50:
                recommendations.append("Title çok kısa, 50-60 karakter arası olmalı")
            elif analysis['seo_metrics']['title']['length'] > 60:
                recommendations.append("Title çok uzun, 50-60 karakter arası olmalı")
        
        # Meta description önerileri
        if not analysis['seo_metrics']['meta_description']['exists']:
            recommendations.append("KRITIK: Meta description eksik")
        elif not analysis['seo_metrics']['meta_description']['optimal']:
            recommendations.append("Meta description 150-160 karakter arası olmalı")
        
        # H1 önerileri
        if analysis['seo_metrics']['h1']['count'] == 0:
            recommendations.append("KRITIK: H1 etiketi eksik")
        elif analysis['seo_metrics']['h1']['count'] > 1:
            recommendations.append("Birden fazla H1 etiketi var, tek olmalı")
        
        # İçerik önerileri
        if not analysis['seo_metrics']['content_length_optimal']:
            recommendations.append(f"İçerik çok kısa ({analysis['seo_metrics']['word_count']} kelime), minimum 300 kelime olmalı")
        
        # Teknik SEO önerileri
        if not analysis['technical_seo']['mobile_friendly']['has_viewport']:
            recommendations.append("Viewport meta etiketi eksik (mobil uyumluluk)")
        
        if not analysis['technical_seo']['canonical']['exists']:
            recommendations.append("Canonical URL eksik")
        
        # Schema önerileri
        if analysis['schema_markup']['total_schema_types'] == 0:
            recommendations.append("Schema markup eksik, LocalBusiness ve Service eklenmeli")
        
        # Görsel önerileri
        if analysis['technical_seo']['images']['images_without_alt'] > 0:
            recommendations.append(f"{analysis['technical_seo']['images']['images_without_alt']} görselin alt metni eksik")
        
        return recommendations
    
    def simulate_google_search_position(self, filename, keywords):
        """Google sıralama simülasyonu (gerçek API olmadığı için tahmini)"""
        # Bu fonksiyon gerçek bir Google API çağrısı yapmaz
        # Sayfa kalitesine göre tahmini sıralama verir
        
        analysis = self.results.get(filename, {})
        seo_score = analysis.get('seo_score', 0)
        
        positions = {}
        for keyword in keywords:
            # SEO skoruna göre tahmini sıralama
            if seo_score >= 80:
                position = f"1-10 (Tahmini: {5 + (100-seo_score)//4})"
            elif seo_score >= 60:
                position = f"11-30 (Tahmini: {15 + (80-seo_score)//2})"
            elif seo_score >= 40:
                position = f"31-50 (Tahmini: {35 + (60-seo_score)})"
            else:
                position = "50+ (Düşük SEO skoru)"
                
            positions[keyword] = position
        
        return positions
    
    def estimate_traffic_potential(self, analysis):
        """Trafik potansiyeli tahmini"""
        seo_score = analysis.get('seo_score', 0)
        location = analysis['filename'].split('-')[0]
        
        # Bölge popülasyonuna göre tahmini (İstanbul ilçeleri)
        population_estimates = {
            'kadikoy': 450000, 'uskudar': 550000, 'maltepe': 500000,
            'atasehir': 450000, 'umraniye': 700000, 'kartal': 450000
        }
        
        base_population = population_estimates.get(location, 300000)
        
        # SEO skoruna göre trafik çarpanı
        traffic_multiplier = seo_score / 100
        
        # Aylık tahmini trafik
        estimated_monthly = int((base_population * 0.001) * traffic_multiplier)
        
        return {
            'estimated_monthly_visits': estimated_monthly,
            'traffic_potential': 'Yüksek' if estimated_monthly > 200 else 'Orta' if estimated_monthly > 100 else 'Düşük'
        }
    
    def analyze_all_pages(self):
        """Tüm sayfaları analiz et"""
        print("DryAlle SEO Analizi Başlıyor...")
        print("=" * 50)
        
        html_files = [f for f in os.listdir(self.base_dir) if f.endswith('.html')]
        total_files = len(html_files)
        
        for i, filename in enumerate(html_files, 1):
            print(f"Analiz ediliyor ({i}/{total_files}): {filename}")
            analysis = self.analyze_html_file(filename)
            if analysis:
                self.results[filename] = analysis
            time.sleep(0.1)  # API rate limiting için
        
        print(f"\nToplam {len(self.results)} sayfa analiz edildi.")
        return self.results
    
    def generate_comprehensive_report(self):
        """Kapsamlı rapor oluştur"""
        if not self.results:
            self.analyze_all_pages()
        
        report = {
            'summary': self.generate_summary(),
            'detailed_analysis': self.results,
            'recommendations': self.generate_global_recommendations(),
            'comparison': self.compare_new_vs_existing(),
            'ranking_tracking': self.generate_ranking_report(),
            'timestamp': datetime.now().isoformat()
        }
        
        return report
    
    def generate_summary(self):
        """Özet tablo oluştur"""
        summary = {
            'total_pages': len(self.results),
            'average_seo_score': round(statistics.mean([r['seo_score'] for r in self.results.values()]), 1),
            'pages_with_optimal_title': len([r for r in self.results.values() if r['seo_metrics']['title']['optimal']]),
            'pages_with_meta_description': len([r for r in self.results.values() if r['seo_metrics']['meta_description']['exists']]),
            'pages_with_schema': len([r for r in self.results.values() if r['schema_markup']['total_schema_types'] > 0]),
            'average_word_count': round(statistics.mean([r['seo_metrics']['word_count'] for r in self.results.values()]), 0)
        }
        
        # Yeni sayfalar özeti
        new_page_results = [r for r in self.results.values() if r['is_new_page']]
        if new_page_results:
            summary['new_pages'] = {
                'count': len(new_page_results),
                'average_seo_score': round(statistics.mean([r['seo_score'] for r in new_page_results]), 1),
                'needs_improvement': len([r for r in new_page_results if r['seo_score'] < 70])
            }
        
        return summary
    
    def compare_new_vs_existing(self):
        """Yeni ve mevcut sayfaları karşılaştır"""
        new_pages = [r for r in self.results.values() if r['is_new_page']]
        existing_pages = [r for r in self.results.values() if not r['is_new_page']]
        
        if not new_pages or not existing_pages:
            return {}
        
        comparison = {
            'new_pages_avg_score': round(statistics.mean([r['seo_score'] for r in new_pages]), 1),
            'existing_pages_avg_score': round(statistics.mean([r['seo_score'] for r in existing_pages]), 1),
            'new_pages_avg_words': round(statistics.mean([r['seo_metrics']['word_count'] for r in new_pages]), 0),
            'existing_pages_avg_words': round(statistics.mean([r['seo_metrics']['word_count'] for r in existing_pages]), 0)
        }
        
        return comparison
    
    def generate_global_recommendations(self):
        """Genel öneriler oluştur"""
        all_recommendations = []
        for result in self.results.values():
            all_recommendations.extend(result['recommendations'])
        
        # En yaygın sorunları bul
        recommendation_counts = Counter(all_recommendations)
        
        global_recommendations = {
            'most_common_issues': dict(recommendation_counts.most_common(10)),
            'priority_actions': [
                "Tüm sayfalar için meta description eklenmeli",
                "Schema markup (LocalBusiness, Service) tüm sayfalara eklenmeli", 
                "İçerik uzunluğu minimum 300 kelime yapılmalı",
                "Tüm görsellere alt metni eklenmeli",
                "İç bağlantı yapısı güçlendirilmeli"
            ]
        }
        
        return global_recommendations
    
    def generate_ranking_report(self):
        """Sıralama takip raporu oluştur"""
        ranking_data = {}
        
        for filename, analysis in self.results.items():
            # Dosya adından hedef kelimeleri çıkar
            service_type = None
            if 'koltuk-yikama' in filename:
                service_type = 'koltuk-yikama'
            elif 'hali-yikama' in filename:
                service_type = 'hali-yikama'
            elif 'kuru-temizleme' in filename:
                service_type = 'kuru-temizleme'
            elif 'premium' in filename or 'luxury' in filename:
                service_type = 'premium-temizlik'
            
            if service_type:
                keywords = self.target_keywords.get(service_type, [])
                positions = self.simulate_google_search_position(filename, keywords)
                
                ranking_data[filename] = {
                    'service_type': service_type,
                    'keywords': keywords,
                    'estimated_positions': positions,
                    'seo_score': analysis['seo_score'],
                    'traffic_potential': self.estimate_traffic_potential(analysis)
                }
        
        return ranking_data

def main():
    analyzer = ComprehensiveSEOAnalyzer()
    
    print("DryAlle Kuru Temizleme - Kapsamlı SEO Analizi")
    print("=" * 60)
    print("Başlangıç zamanı:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print()
    
    # Tüm sayfaları analiz et
    results = analyzer.analyze_all_pages()
    
    # Kapsamlı rapor oluştur
    report = analyzer.generate_comprehensive_report()
    
    # Raporu dosyaya kaydet
    output_file = f"comprehensive_seo_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    output_path = os.path.join(analyzer.base_dir, output_file)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\nKapsamlı SEO analizi tamamlandı!")
    print(f"Rapor dosyası: {output_path}")
    
    # Özet bilgileri ekrana yazdır
    print("\n" + "="*60)
    print("ÖZET BİLGİLER")
    print("="*60)
    
    summary = report['summary']
    print(f"Toplam sayfa sayısı: {summary['total_pages']}")
    print(f"Ortalama SEO skoru: {summary['average_seo_score']}/100")
    print(f"Optimal title'a sahip sayfalar: {summary['pages_with_optimal_title']}/{summary['total_pages']}")
    print(f"Meta description'ı olan sayfalar: {summary['pages_with_meta_description']}/{summary['total_pages']}")
    print(f"Schema markup'ı olan sayfalar: {summary['pages_with_schema']}/{summary['total_pages']}")
    print(f"Ortalama kelime sayısı: {summary['average_word_count']}")
    
    if 'new_pages' in summary:
        print(f"\nYeni sayfalar ({summary['new_pages']['count']} adet):")
        print(f"- Ortalama SEO skoru: {summary['new_pages']['average_seo_score']}/100")
        print(f"- İyileştirme gereken: {summary['new_pages']['needs_improvement']}")
    
    print(f"\nDetaylı analiz için {output_file} dosyasını inceleyiniz.")

if __name__ == "__main__":
    main()