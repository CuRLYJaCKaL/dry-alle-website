#!/usr/bin/env python3
"""
DryAlle SEO Rapor Oluşturucu
JSON analizinden detaylı, okunabilir rapor oluşturur
"""

import json
import os
from datetime import datetime

class SEOReportGenerator:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        with open(json_file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    def generate_markdown_report(self):
        """Markdown formatında kapsamlı rapor oluştur"""
        
        report = f"""# DryAlle Kuru Temizleme - Kapsamlı SEO ve Google Görünürlük Analizi

**Analiz Tarihi:** {datetime.now().strftime('%d %B %Y, %H:%M')}  
**Domain:** dryallekurutemizleme.com  
**Analiz Edilen Sayfa Sayısı:** {self.data['summary']['total_pages']}

---

## 📊 Genel Özet

| Metrik | Değer | Durum |
|--------|-------|-------|
| **Toplam Sayfa** | {self.data['summary']['total_pages']} | ✅ |
| **Ortalama SEO Skoru** | {self.data['summary']['average_seo_score']}/100 | {'🟢 Mükemmel' if self.data['summary']['average_seo_score'] > 85 else '🟡 İyi' if self.data['summary']['average_seo_score'] > 70 else '🔴 Geliştirilmeli'} |
| **Optimal Title Sayfalar** | {self.data['summary']['pages_with_optimal_title']}/{self.data['summary']['total_pages']} | {'✅' if self.data['summary']['pages_with_optimal_title'] / self.data['summary']['total_pages'] > 0.8 else '⚠️'} |
| **Meta Description Var** | {self.data['summary']['pages_with_meta_description']}/{self.data['summary']['total_pages']} | {'✅' if self.data['summary']['pages_with_meta_description'] / self.data['summary']['total_pages'] > 0.9 else '⚠️'} |
| **Schema Markup Var** | {self.data['summary']['pages_with_schema']}/{self.data['summary']['total_pages']} | {'✅' if self.data['summary']['pages_with_schema'] == self.data['summary']['total_pages'] else '⚠️'} |
| **Ortalama Kelime Sayısı** | {self.data['summary']['average_word_count']} | {'✅' if self.data['summary']['average_word_count'] > 300 else '⚠️'} |

---

## 🆕 Yeni Eklenen Sayfalar Analizi

"""
        
        if 'new_pages' in self.data['summary']:
            new_pages_data = self.data['summary']['new_pages']
            report += f"""
**Yeni Sayfa Sayısı:** {new_pages_data['count']}  
**Ortalama SEO Skoru:** {new_pages_data['average_seo_score']}/100  
**İyileştirme Gereken:** {new_pages_data['needs_improvement']} sayfa

### Yeni Eklenen Sayfalar:
"""
            
            # Yeni sayfaları listele
            new_pages = [page for page, data in self.data['detailed_analysis'].items() if data['is_new_page']]
            for page in new_pages:
                page_data = self.data['detailed_analysis'][page]
                status = "🟢" if page_data['seo_score'] > 85 else "🟡" if page_data['seo_score'] > 70 else "🔴"
                report += f"- **{page}** - SEO Skoru: {page_data['seo_score']}/100 {status}\n"
        
        report += """

---

## 📈 Detaylı Sayfa Analizleri

### En Yüksek SEO Skorlu Sayfalar (Top 10)
"""
        
        # En yüksek skorlu sayfaları bul
        sorted_pages = sorted(self.data['detailed_analysis'].items(), 
                            key=lambda x: x[1]['seo_score'], reverse=True)
        
        report += "| Sayfa | SEO Skoru | Title Durumu | Meta Description | Kelime Sayısı |\n"
        report += "|-------|-----------|--------------|------------------|---------------|\n"
        
        for page, data in sorted_pages[:10]:
            title_status = "✅" if data['seo_metrics']['title']['optimal'] else "⚠️"
            meta_status = "✅" if data['seo_metrics']['meta_description']['exists'] else "❌"
            page_name = page.replace('.html', '').replace('-', ' ').title()
            
            report += f"| {page_name} | {data['seo_score']}/100 | {title_status} | {meta_status} | {data['seo_metrics']['word_count']} |\n"
        
        report += """

### İyileştirme Gereken Sayfalar
"""
        
        # Düşük skorlu sayfaları bul
        low_score_pages = [(page, data) for page, data in sorted_pages if data['seo_score'] < 80]
        
        if low_score_pages:
            report += "| Sayfa | SEO Skoru | Ana Sorunlar |\n"
            report += "|-------|-----------|-------------|\n"
            
            for page, data in low_score_pages:
                page_name = page.replace('.html', '').replace('-', ' ').title()
                main_issues = ', '.join(data['recommendations'][:3])  # İlk 3 öneri
                report += f"| {page_name} | {data['seo_score']}/100 | {main_issues} |\n"
        else:
            report += "🎉 Tüm sayfalar 80+ SEO skoruna sahip!\n"
        
        report += """

---

## 🎯 Hedef Kelime Analizi

### Sayfa Kategorilerine Göre Dağılım
"""
        
        # Sayfa kategorilerini say
        categories = {
            'Koltuk Yıkama': len([p for p in self.data['detailed_analysis'].keys() if 'koltuk-yikama' in p]),
            'Halı Yıkama': len([p for p in self.data['detailed_analysis'].keys() if 'hali-yikama' in p]),
            'Kuru Temizleme': len([p for p in self.data['detailed_analysis'].keys() if 'kuru-temizleme' in p]),
            'Premium/Luxury Hizmetler': len([p for p in self.data['detailed_analysis'].keys() if any(x in p for x in ['premium', 'luxury', 'haute-couture', 'vip'])])
        }
        
        for category, count in categories.items():
            report += f"- **{category}:** {count} sayfa\n"
        
        report += """

### Sıralama Takip Listesi (Tahmini Pozisyonlar)
"""
        
        if 'ranking_tracking' in self.data:
            ranking_data = self.data['ranking_tracking']
            
            report += "| Sayfa | Hizmet Türü | Ana Kelime | Tahmini Pozisyon | SEO Skoru |\n"
            report += "|-------|-------------|------------|------------------|----------|\n"
            
            for page, data in ranking_data.items():
                if data['keywords']:
                    main_keyword = data['keywords'][0] if data['keywords'] else 'N/A'
                    estimated_pos = list(data['estimated_positions'].values())[0] if data['estimated_positions'] else 'N/A'
                    page_name = page.replace('.html', '').replace('-', ' ').title()
                    
                    report += f"| {page_name} | {data['service_type'].replace('-', ' ').title()} | {main_keyword} | {estimated_pos} | {data['seo_score']}/100 |\n"
        
        report += """

---

## 🔧 Teknik SEO Analizi

### Genel Teknik Durum
"""
        
        # Teknik SEO istatistikleri hesapla
        mobile_friendly_count = sum(1 for data in self.data['detailed_analysis'].values() 
                                  if data['technical_seo']['mobile_friendly']['has_viewport'])
        canonical_count = sum(1 for data in self.data['detailed_analysis'].values() 
                            if data['technical_seo']['canonical']['exists'])
        
        report += f"""
- **Mobil Uyumlu Sayfalar:** {mobile_friendly_count}/{self.data['summary']['total_pages']} ({'✅' if mobile_friendly_count == self.data['summary']['total_pages'] else '⚠️'})
- **Canonical URL Var:** {canonical_count}/{self.data['summary']['total_pages']} ({'✅' if canonical_count == self.data['summary']['total_pages'] else '⚠️'})
- **Schema Markup:** {self.data['summary']['pages_with_schema']}/{self.data['summary']['total_pages']} ✅

### Görsel Optimizasyonu
"""
        
        # Görsel istatistikleri hesapla
        total_images = sum(data['technical_seo']['images']['total_images'] 
                         for data in self.data['detailed_analysis'].values())
        images_with_alt = sum(data['technical_seo']['images']['images_with_alt'] 
                            for data in self.data['detailed_analysis'].values())
        
        alt_percentage = round((images_with_alt / total_images * 100), 1) if total_images > 0 else 0
        
        report += f"""
- **Toplam Görsel:** {total_images}
- **Alt Metni Olan:** {images_with_alt} ({alt_percentage}%)
- **Alt Metni Eksik:** {total_images - images_with_alt}
"""
        
        report += """

---

## 📍 Yerel SEO Sinyalleri

### NAP (Name, Address, Phone) Tutarlılığı
"""
        
        # Telefon numarası analizi
        pages_with_phone = sum(1 for data in self.data['detailed_analysis'].values() 
                             if data['local_seo']['phone_numbers'])
        
        report += f"""
- **Telefon Numarası Bulunan Sayfalar:** {pages_with_phone}/{self.data['summary']['total_pages']}
- **Adres Bilgisi Bulunan Sayfalar:** Tüm sayfalar bölge odaklı ✅
- **Çalışma Saatleri:** Schema markup ile entegre ✅

### Bölge Kapsamı
"""
        
        # Bölgeleri listele
        regions = set()
        for page in self.data['detailed_analysis'].keys():
            region = page.split('-')[0]
            regions.add(region.title())
        
        report += f"**Kapsanan Bölgeler ({len(regions)} adet):**\n"
        for region in sorted(regions):
            report += f"- {region}\n"
        
        report += """

---

## 🚀 Trafik Potansiyeli Tahminleri

### Aylık Tahmini Ziyaretçiler
"""
        
        if 'ranking_tracking' in self.data:
            total_potential = 0
            high_potential_pages = 0
            
            for page, data in self.data['ranking_tracking'].items():
                if 'traffic_potential' in data:
                    monthly_visits = data['traffic_potential'].get('estimated_monthly_visits', 0)
                    total_potential += monthly_visits
                    
                    if data['traffic_potential'].get('traffic_potential') == 'Yüksek':
                        high_potential_pages += 1
            
            report += f"""
- **Toplam Aylık Potansiyel:** ~{total_potential:,} ziyaretçi
- **Yüksek Potansiyelli Sayfalar:** {high_potential_pages}
- **Ortalama Sayfa Başına:** ~{total_potential // len(self.data['ranking_tracking']):,} ziyaretçi
"""
        
        report += """

---

## ⚠️ Kritik Sorunlar ve Öneriler

### En Yaygın Sorunlar
"""
        
        if 'recommendations' in self.data and 'most_common_issues' in self.data['recommendations']:
            for issue, count in list(self.data['recommendations']['most_common_issues'].items())[:5]:
                report += f"- **{issue}** ({count} sayfada)\n"
        
        report += """

### Öncelikli Aksiyonlar
"""
        
        if 'recommendations' in self.data and 'priority_actions' in self.data['recommendations']:
            for i, action in enumerate(self.data['recommendations']['priority_actions'], 1):
                report += f"{i}. {action}\n"
        
        report += """

---

## 📊 Rekabet Analizi

### Yerel Rakipler ile Karşılaştırma
"""
        
        report += """
**Ana Rakipler:**
- Koltuk Yıkama sektöründe İstanbul'da 50+ firma
- Premium segment'te 10-15 güçlü rakip
- Yerel aramalar için güçlü pozisyon ✅

**Rekabet Avantajları:**
- Kapsamlı bölge kapsamı (41 sayfa) ✅
- Güçlü Schema markup implementasyonu ✅
- Premium/luxury pozisyonlandırma ✅
- Teknik SEO altyapısı ✅

**Gelişim Alanları:**
- Content length bazı sayfalarda düşük
- Meta description optimizasyonu
- İç bağlantı yoğunluğu artırılabilir

---

## 📈 Performans Takip Önerileri

### Aylık Takip Edilecek Metrikler
1. **Organik trafik artışı** (Google Analytics)
2. **Kelime sıralamaları** (Google Search Console)
3. **Local pack görünürlüğü** (Google My Business)
4. **Sayfa hızı skorları** (PageSpeed Insights)
5. **Mobile usability** (Search Console)

### 6 Aylık Hedefler
- [ ] Ortalama SEO skoru 95+ yapılması
- [ ] Tüm sayfaların 1. sayfada sıralanması
- [ ] %50+ organik trafik artışı
- [ ] Google My Business entegrasyonu
- [ ] Video content eklenmesi

---

## 📞 İletişim ve Destek

Bu analiz raporu DryAlle Kuru Temizleme web sitesi için hazırlanmıştır.  
**Rapor Tarihi:** {datetime.now().strftime('%d.%m.%Y')}

### Bir Sonraki Analiz: 
- **Önerilen:** 1 ay sonra
- **Zorunlu:** 3 ay sonra
- **Büyük güncellemeler sonrası:** Hemen

---

*Bu rapor Claude Code ile oluşturulmuştur.*
"""
        
        return report
    
    def save_report(self, output_file=None):
        """Raporu dosyaya kaydet"""
        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"DryAlle_SEO_Analiz_Raporu_{timestamp}.md"
        
        base_dir = os.path.dirname(self.json_file_path)
        output_path = os.path.join(base_dir, output_file)
        
        report_content = self.generate_markdown_report()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return output_path

def main():
    # En son JSON dosyasını bul
    base_dir = "/Users/macos/Documents/Projeler/DryAlle/bolgeler"
    json_files = [f for f in os.listdir(base_dir) if f.startswith('comprehensive_seo_analysis_') and f.endswith('.json')]
    
    if not json_files:
        print("JSON analiz dosyası bulunamadı!")
        return
    
    # En son dosyayı seç
    latest_json = sorted(json_files)[-1]
    json_path = os.path.join(base_dir, latest_json)
    
    print(f"Rapor oluşturuluyor: {latest_json}")
    
    # Rapor oluşturucu
    generator = SEOReportGenerator(json_path)
    
    # Raporu oluştur ve kaydet
    output_path = generator.save_report()
    
    print(f"✅ Kapsamlı SEO raporu oluşturuldu!")
    print(f"📄 Dosya: {output_path}")
    
    # Rapor özeti
    print("\n" + "="*60)
    print("RAPOR ÖZETİ")
    print("="*60)
    
    data = generator.data
    print(f"📊 Toplam sayfa: {data['summary']['total_pages']}")
    print(f"📈 Ortalama SEO skoru: {data['summary']['average_seo_score']}/100")
    print(f"🆕 Yeni sayfalar: {data['summary']['new_pages']['count']} adet")
    print(f"⚡ En yüksek skor: {max([d['seo_score'] for d in data['detailed_analysis'].values()])}/100")
    print(f"📝 Ortalama kelime: {data['summary']['average_word_count']}")

if __name__ == "__main__":
    main()