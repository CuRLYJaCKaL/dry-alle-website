#!/usr/bin/env python3
"""
Google Görünürlük Simülatörü
DryAlle sayfalarının Google'daki performansını simüle eder
"""

import json
import os
import random
from datetime import datetime, timedelta

class GoogleVisibilitySimulator:
    def __init__(self, analysis_file):
        with open(analysis_file, 'r', encoding='utf-8') as f:
            self.analysis_data = json.load(f)
        
        # İstanbul bölgeleri ve nüfus yoğunlukları
        self.region_population = {
            'kadikoy': 450000,
            'uskudar': 550000,
            'maltepe': 500000,
            'atasehir': 450000,
            'umraniye': 700000,
            'kartal': 450000,
            'pendik': 650000,
            'bostanci': 150000,
            'fenerbahce': 120000,
            'caddebostan': 80000,
            'suadiye': 90000,
            'moda': 40000,
            'kalamis': 35000,
            'barbaros': 45000,
            'fikirtepe': 180000,
            'goztepe': 120000,
            'erenkoy': 85000,
            'altunizade': 95000,
            'icerenkoy': 110000,
            'kucukbakkalkoy': 75000,
            'kozyatagi': 140000,
            'acibadem': 95000,
            'camlica': 60000,
            'sahrayicedit': 85000
        }
        
        # Hizmet türü arama hacmi (aylık)
        self.service_search_volume = {
            'koltuk-yikama': 8900,
            'hali-yikama': 12100,
            'kuru-temizleme': 6600,
            'premium-temizlik': 2400,
            'luxury-hizmet': 1800
        }
        
        # Rekabet yoğunluğu (1-10 arası)
        self.competition_level = {
            'koltuk-yikama': 8,
            'hali-yikama': 7,
            'kuru-temizleme': 6,
            'premium-temizlik': 4,
            'luxury-hizmet': 3
        }
    
    def simulate_serp_position(self, page_data):
        """SERP pozisyonu simülasyonu"""
        seo_score = page_data['seo_score']
        
        # Temel pozisyon hesaplaması
        if seo_score >= 95:
            base_position = random.randint(1, 3)
        elif seo_score >= 85:
            base_position = random.randint(2, 8)
        elif seo_score >= 75:
            base_position = random.randint(5, 15)
        elif seo_score >= 65:
            base_position = random.randint(10, 25)
        else:
            base_position = random.randint(20, 50)
        
        # Hizmet türüne göre rekabet düzeltmesi
        service_type = self.extract_service_type(page_data['filename'])
        competition = self.competition_level.get(service_type, 5)
        
        # Yüksek rekabet durumunda pozisyon kayması
        competition_penalty = (competition - 5) * 2
        final_position = min(100, base_position + competition_penalty)
        
        return max(1, final_position)
    
    def extract_service_type(self, filename):
        """Dosya adından hizmet türünü çıkar"""
        if 'koltuk-yikama' in filename:
            return 'koltuk-yikama'
        elif 'hali-yikama' in filename:
            return 'hali-yikama'
        elif 'kuru-temizleme' in filename:
            return 'kuru-temizleme'
        elif any(x in filename for x in ['premium', 'luxury', 'vip', 'haute-couture']):
            return 'premium-temizlik'
        else:
            return 'hali-yikama'  # default
    
    def extract_region(self, filename):
        """Dosya adından bölgeyi çıkar"""
        return filename.split('-')[0]
    
    def calculate_traffic_estimate(self, page_data, serp_position):
        """Trafik tahmini hesapla"""
        service_type = self.extract_service_type(page_data['filename'])
        region = self.extract_region(page_data['filename'])
        
        # Bölgesel arama hacmi
        region_population = self.region_population.get(region, 100000)
        base_searches = self.service_search_volume.get(service_type, 5000)
        
        # Bölgesel oran hesaplama (nüfusa göre)
        region_ratio = region_population / 450000  # Kadıköy referans
        local_monthly_searches = int(base_searches * region_ratio * 0.1)  # %10'u yerel
        
        # CTR (Click Through Rate) SERP pozisyonuna göre
        ctr_rates = {
            1: 0.284, 2: 0.147, 3: 0.103, 4: 0.073, 5: 0.053,
            6: 0.041, 7: 0.032, 8: 0.026, 9: 0.022, 10: 0.019
        }
        
        if serp_position <= 10:
            ctr = ctr_rates.get(serp_position, 0.019)
        elif serp_position <= 20:
            ctr = 0.010
        elif serp_position <= 30:
            ctr = 0.005
        else:
            ctr = 0.002
        
        estimated_clicks = int(local_monthly_searches * ctr)
        
        return {
            'monthly_searches': local_monthly_searches,
            'estimated_clicks': estimated_clicks,
            'ctr': round(ctr * 100, 2),
            'serp_position': serp_position,
            'region_factor': round(region_ratio, 2)
        }
    
    def analyze_keyword_cannibalization(self):
        """Kelime kannibalizasyonu analizi"""
        service_pages = {}
        
        for filename, data in self.analysis_data['detailed_analysis'].items():
            service_type = self.extract_service_type(filename)
            region = self.extract_region(filename)
            
            key = f"{service_type}_{region}"
            if key not in service_pages:
                service_pages[key] = []
            service_pages[key].append((filename, data['seo_score']))
        
        # Aynı hizmet + bölge kombinasyonu olan sayfaları bul
        cannibalization_issues = {}
        for key, pages in service_pages.items():
            if len(pages) > 1:
                cannibalization_issues[key] = sorted(pages, key=lambda x: x[1], reverse=True)
        
        return cannibalization_issues
    
    def simulate_competitor_analysis(self):
        """Rakip analizi simülasyonu"""
        competitors = {
            'Halı Yıkama İstanbul': {'domain_authority': 45, 'pages': 25, 'avg_content': 250},
            'Premium Koltuk Temizleme': {'domain_authority': 38, 'pages': 18, 'avg_content': 320},
            'İstanbul Kuru Temizleme': {'domain_authority': 42, 'pages': 30, 'avg_content': 180},
            'Luxury Furniture Care': {'domain_authority': 35, 'pages': 12, 'avg_content': 400},
            'Express Temizlik': {'domain_authority': 40, 'pages': 22, 'avg_content': 200}
        }
        
        # DryAlle metrikleri
        our_metrics = {
            'estimated_da': 52,  # Güçlü teknik SEO'ya dayanarak
            'pages': len(self.analysis_data['detailed_analysis']),
            'avg_content': self.analysis_data['summary']['average_word_count'],
            'avg_seo_score': self.analysis_data['summary']['average_seo_score']
        }
        
        competitive_advantage = []
        improvement_areas = []
        
        for competitor, metrics in competitors.items():
            if our_metrics['pages'] > metrics['pages']:
                competitive_advantage.append(f"Sayfa sayısı avantajı vs {competitor}")
            
            if our_metrics['avg_content'] > metrics['avg_content']:
                competitive_advantage.append(f"İçerik kalitesi avantajı vs {competitor}")
            else:
                improvement_areas.append(f"İçerik uzunluğu geliştirme vs {competitor}")
        
        return {
            'our_metrics': our_metrics,
            'competitors': competitors,
            'advantages': competitive_advantage,
            'improvement_areas': improvement_areas
        }
    
    def generate_traffic_forecast(self, months=6):
        """6 aylık trafik tahmini"""
        forecast = {}
        
        for filename, data in self.analysis_data['detailed_analysis'].items():
            current_position = self.simulate_serp_position(data)
            traffic_data = self.calculate_traffic_estimate(data, current_position)
            
            # 6 aylık gelişim simülasyonu
            monthly_forecast = []
            for month in range(1, months + 1):
                # SEO iyileştirmeleri ile pozisyon gelişimi
                improvement_factor = 1 - (month * 0.05)  # Her ay %5 iyileşme
                projected_position = max(1, int(current_position * improvement_factor))
                
                projected_traffic = self.calculate_traffic_estimate(data, projected_position)
                monthly_forecast.append({
                    'month': month,
                    'position': projected_position,
                    'clicks': projected_traffic['estimated_clicks']
                })
            
            forecast[filename] = {
                'current': traffic_data,
                'forecast': monthly_forecast
            }
        
        return forecast
    
    def generate_local_search_insights(self):
        """Yerel arama insights"""
        local_insights = {}
        
        # Bölge performansı
        region_performance = {}
        for filename, data in self.analysis_data['detailed_analysis'].items():
            region = self.extract_region(filename)
            
            if region not in region_performance:
                region_performance[region] = {
                    'page_count': 0,
                    'avg_score': 0,
                    'total_score': 0,
                    'population': self.region_population.get(region, 100000),
                    'pages': []
                }
            
            region_performance[region]['page_count'] += 1
            region_performance[region]['total_score'] += data['seo_score']
            region_performance[region]['pages'].append(filename)
        
        # Ortalama skorları hesapla
        for region, data in region_performance.items():
            data['avg_score'] = round(data['total_score'] / data['page_count'], 1)
            data['efficiency'] = round(data['avg_score'] / (data['population'] / 100000), 2)
        
        # En performanslı bölgeleri bul
        top_regions = sorted(region_performance.items(), 
                           key=lambda x: x[1]['avg_score'], reverse=True)[:5]
        
        return {
            'region_performance': region_performance,
            'top_performing_regions': top_regions,
            'total_coverage': len(region_performance)
        }
    
    def generate_comprehensive_report(self):
        """Kapsamlı Google görünürlük raporu"""
        
        print("Google Görünürlük Analizi Başlıyor...")
        
        # Ana analizler
        traffic_forecast = self.generate_traffic_forecast()
        competitor_analysis = self.simulate_competitor_analysis()
        local_insights = self.generate_local_search_insights()
        cannibalization = self.analyze_keyword_cannibalization()
        
        # Toplam trafik hesaplaması
        total_current_traffic = sum(page['current']['estimated_clicks'] 
                                  for page in traffic_forecast.values())
        total_projected_traffic = sum(page['forecast'][5]['clicks'] 
                                    for page in traffic_forecast.values())
        
        # Rapor verilerini birleştir
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_pages_analyzed': len(self.analysis_data['detailed_analysis']),
                'current_monthly_traffic': total_current_traffic,
                'projected_6m_traffic': total_projected_traffic,
                'growth_potential': round((total_projected_traffic - total_current_traffic) / total_current_traffic * 100, 1),
                'avg_serp_position': round(sum(self.simulate_serp_position(data) 
                                             for data in self.analysis_data['detailed_analysis'].values()) / 
                                         len(self.analysis_data['detailed_analysis']), 1)
            },
            'traffic_forecast': traffic_forecast,
            'competitor_analysis': competitor_analysis,
            'local_insights': local_insights,
            'cannibalization_issues': cannibalization,
            'recommendations': self.generate_actionable_recommendations()
        }
        
        return report_data
    
    def generate_actionable_recommendations(self):
        """Eyleme geçirilebilir öneriler"""
        return {
            'immediate_actions': [
                "Fenerbahçe halı yıkama ve koltuk yıkama sayfalarının meta description'larını ekleyin",
                "Title uzunluklarını 50-60 karakter arasında optimize edin",
                "Google My Business profilleri oluşturun ve optimize edin",
                "Müşteri yorumları toplamaya başlayın",
                "Yerel backlink stratejisi geliştirin"
            ],
            'weekly_tasks': [
                "Her sayfa için blog içeriği oluşturun",
                "İç bağlantı yapısını güçlendirin",
                "Social media paylaşımları yapın",
                "Müşteri fotoğrafları ekleyin",
                "FAQ bölümleri genişletin"
            ],
            'monthly_goals': [
                "Google Search Console verilerini analiz edin",
                "Rakip siteleri inceleyin",
                "Yeni long-tail keyword'ler bulun",
                "Sayfa hızlarını optimize edin",
                "Mobile experience iyileştirin"
            ]
        }

def main():
    # En son analiz dosyasını bul
    base_dir = "/Users/macos/Documents/Projeler/DryAlle/bolgeler"
    json_files = [f for f in os.listdir(base_dir) 
                  if f.startswith('comprehensive_seo_analysis_') and f.endswith('.json')]
    
    if not json_files:
        print("Analiz dosyası bulunamadı!")
        return
    
    latest_json = sorted(json_files)[-1]
    json_path = os.path.join(base_dir, latest_json)
    
    # Simülatörü başlat
    simulator = GoogleVisibilitySimulator(json_path)
    
    # Kapsamlı rapor oluştur
    report = simulator.generate_comprehensive_report()
    
    # Raporu kaydet
    output_file = f"google_visibility_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    output_path = os.path.join(base_dir, output_file)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    # Özet raporu yazdır
    print("\n" + "="*60)
    print("GOOGLE GÖRÜNÜRLİK ANALİZİ ÖZETİ")
    print("="*60)
    
    summary = report['summary']
    print(f"📊 Analiz edilen sayfa: {summary['total_pages_analyzed']}")
    print(f"🎯 Mevcut aylık trafik: ~{summary['current_monthly_traffic']:,} ziyaretçi")
    print(f"📈 6 ay sonra tahmini: ~{summary['projected_6m_traffic']:,} ziyaretçi")
    print(f"🚀 Büyüme potansiyeli: %{summary['growth_potential']}")
    print(f"📍 Ortalama SERP pozisyonu: {summary['avg_serp_position']}")
    
    print(f"\n✅ Detaylı rapor: {output_file}")
    
    # Top 5 bölge performansı
    print("\n🏆 En Performanslı Bölgeler:")
    for region, data in report['local_insights']['top_performing_regions']:
        print(f"- {region.title()}: {data['avg_score']}/100 ortalama skor")
    
    # Acil öneriler
    print("\n⚡ Acil Eylemler:")
    for i, action in enumerate(report['recommendations']['immediate_actions'][:3], 1):
        print(f"{i}. {action}")

if __name__ == "__main__":
    main()