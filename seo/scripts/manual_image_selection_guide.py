#!/usr/bin/env python3
"""
Manuel Görsel Seçim Rehberi
API olmadan elle görsel seçimi için detaylı rehber ve öneriler
"""

import os
import json
import csv
from datetime import datetime

class ManualImageSelectionGuide:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        
        # Tema bazlı görsel önerileri
        self.theme_suggestions = {
            "profesyonel": {
                "keywords": ["professional dry cleaning", "laundry service", "textile care", "cleaning equipment", "uniform care"],
                "style": "Modern, temiz, profesyonel ortam",
                "colors": "Beyaz, yeşil tonları, minimalist",
                "examples": [
                    "https://images.unsplash.com/photo-1558618666-fbd6c802d1c6?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=1200&h=630&fit=crop"
                ]
            },
            "halı": {
                "keywords": ["carpet cleaning", "rug care", "floor cleaning", "textile maintenance"],
                "style": "Ev ortamı, temiz zemin, modern iç mekan",
                "colors": "Doğal tonlar, beyaz, temiz görünüm",
                "examples": [
                    "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1540932239986-30128078f3c5?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=1200&h=630&fit=crop"
                ]
            },
            "deri": {
                "keywords": ["leather care", "leather cleaning", "leather jacket", "leather maintenance"],
                "style": "Şık, premium, kaliteli deri ürünler",
                "colors": "Kahverengi tonlar, siyah, premium görünüm",
                "examples": [
                    "https://images.unsplash.com/photo-1520975954732-35dd22299614?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1200&h=630&fit=crop"
                ]
            },
            "perde": {
                "keywords": ["curtain cleaning", "window treatment", "home textile", "curtain care"],
                "style": "Ev ortamı, pencere, temiz perde",
                "colors": "Açık renkler, doğal ışık, temiz görünüm",
                "examples": [
                    "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1467043237213-65f2da53396f?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=1200&h=630&fit=crop"
                ]
            },
            "gelinlik": {
                "keywords": ["wedding dress", "bridal gown", "dress care", "special occasion"],
                "style": "Şık, özel, temiz, premium",
                "colors": "Beyaz, krem, elegant tonlar",
                "examples": [
                    "https://images.unsplash.com/photo-1519657337289-077653f724ed?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1594736797933-d0d15d95c6a9?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?w=1200&h=630&fit=crop"
                ]
            },
            "mobilya": {
                "keywords": ["furniture cleaning", "upholstery care", "sofa cleaning", "furniture maintenance"],
                "style": "Modern ev, temiz mobilya, iç mekan",
                "colors": "Nötr tonlar, temiz görünüm, modern",
                "examples": [
                    "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1563298723-dcfebaa392e3?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1582037928769-181f2644ecb7?w=1200&h=630&fit=crop"
                ]
            },
            "leke": {
                "keywords": ["stain removal", "cleaning process", "before after", "stain treatment"],
                "style": "Önce-sonra, temizlik süreci, professional",
                "colors": "Temiz, açık tonlar, süreç gösterimi",
                "examples": [
                    "https://images.unsplash.com/photo-1628177142898-93e36e4e3a50?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1200&h=630&fit=crop",
                    "https://images.unsplash.com/photo-1558618666-fbd6c802d1c6?w=1200&h=630&fit=crop"
                ]
            }
        }

    def load_analysis_data(self):
        """Analiz verilerini yükle"""
        analysis_path = os.path.join(self.project_root, 'seo/reports/blog_image_analysis.json')
        
        if os.path.exists(analysis_path):
            with open(analysis_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def create_priority_selection_guide(self):
        """Öncelikli bloglar için manuel seçim rehberi"""
        data = self.load_analysis_data()
        if not data:
            return None
        
        priority_blogs = []
        
        # Görseli olmayan blogları bul
        for blog in data['detailed_analyses']:
            if not blog['current_image']['exists']:
                priority_blogs.append({
                    'slug': blog['slug'],
                    'title': blog['title'],
                    'theme': blog['primary_theme'],
                    'keywords': blog['keywords'],
                    'priority': 'CRITICAL',
                    'reason': 'Hiç görseli yok'
                })
        
        # Her tema için en iyi örnekleri bul
        theme_examples = {}
        for blog in data['detailed_analyses']:
            theme = blog['primary_theme']
            if theme not in theme_examples:
                theme_examples[theme] = []
            
            if len(theme_examples[theme]) < 3:  # Her temadan en fazla 3 örnek
                theme_examples[theme].append({
                    'slug': blog['slug'],
                    'title': blog['title'],
                    'keywords': blog['keywords'],
                    'content_length': blog['content_length']
                })
        
        return {
            'priority_blogs': priority_blogs,
            'theme_examples': theme_examples,
            'total_critical': len(priority_blogs)
        }

    def generate_detailed_recommendations(self):
        """Detaylı görsel önerileri oluştur"""
        guide = self.create_priority_selection_guide()
        if not guide:
            return None
        
        recommendations = {
            'generation_date': datetime.now().isoformat(),
            'project': 'Manuel Görsel Seçim Rehberi',
            'critical_priorities': guide['priority_blogs'],
            'theme_based_suggestions': {}
        }
        
        # Her tema için detaylı öneriler
        for theme, examples in guide['theme_examples'].items():
            if theme in self.theme_suggestions:
                suggestions = self.theme_suggestions[theme]
                
                recommendations['theme_based_suggestions'][theme] = {
                    'description': f"{theme.title()} teması için öneriler",
                    'search_keywords': suggestions['keywords'],
                    'visual_style': suggestions['style'],
                    'color_palette': suggestions['colors'],
                    'example_urls': suggestions['examples'],
                    'blogs_in_theme': examples,
                    'selection_criteria': [
                        "Temaya uygunluk",
                        "Profesyonel görünüm",
                        "Marka renklerine uyum",
                        "Yüksek çözünürlük",
                        "Telif hakkı durumu"
                    ]
                }
        
        return recommendations

    def create_csv_with_suggestions(self):
        """Önerilerle birlikte yeni CSV oluştur"""
        recommendations = self.generate_detailed_recommendations()
        if not recommendations:
            return None
        
        csv_content = "Slug,Tema,Başlık,Öncelik,Örnek URL 1,Örnek URL 2,Örnek URL 3,Önerilen Arama,Seçilen URL,Notlar\n"
        
        # Kritik öncelikli bloglar
        for blog in recommendations['critical_priorities']:
            theme = blog['theme']
            if theme in self.theme_suggestions:
                examples = self.theme_suggestions[theme]['examples']
                search_terms = '; '.join(self.theme_suggestions[theme]['keywords'])
                
                csv_content += f'"{blog["slug"]}","{theme}","{blog["title"]}","CRITICAL","{examples[0]}","{examples[1]}","{examples[2]}","{search_terms}","",""\n'
        
        # Tema bazlı örnekler
        for theme, data in recommendations['theme_based_suggestions'].items():
            for blog in data['blogs_in_theme']:
                if blog['slug'] not in [p['slug'] for p in recommendations['critical_priorities']]:
                    examples = data['example_urls']
                    search_terms = '; '.join(data['search_keywords'])
                    
                    csv_content += f'"{blog["slug"]}","{theme}","{blog["title"]}","NORMAL","{examples[0]}","{examples[1]}","{examples[2]}","{search_terms}","",""\n'
        
        return csv_content

    def generate_selection_workflow(self):
        """Görsel seçim iş akışı oluştur"""
        workflow = {
            'title': 'Manuel Görsel Seçim İş Akışı',
            'steps': [
                {
                    'step': 1,
                    'title': 'Kritik Öncelik - Görseli Olmayan Bloglar',
                    'description': 'İlk olarak hiç görseli olmayan 21 blog için görsel seç',
                    'action': 'CSV dosyasında CRITICAL işaretli blogları işle',
                    'time_estimate': '2-3 saat'
                },
                {
                    'step': 2,
                    'title': 'Tema Bazlı Görsel Seçimi',
                    'description': 'Her tema için uygun görseller seç',
                    'action': 'Tema önerilerini kullanarak görsel bul',
                    'time_estimate': '4-5 saat'
                },
                {
                    'step': 3,
                    'title': 'Kalite Kontrolü',
                    'description': 'Seçilen tüm görselleri kontrol et',
                    'action': 'Çözünürlük, telif, tema uyumu kontrol',
                    'time_estimate': '1-2 saat'
                },
                {
                    'step': 4,
                    'title': 'İndirme ve Optimizasyon',
                    'description': 'Seçilen görselleri indir ve WebP\'ye çevir',
                    'action': 'Otomatik script çalıştır',
                    'time_estimate': '30 dakika'
                }
            ],
            'quality_checklist': [
                '✓ Çözünürlük: 1200x630 piksel',
                '✓ Format: WebP destekli',
                '✓ Boyut: < 150KB',
                '✓ Tema uyumu: %100',
                '✓ Marka renkleri: Uyumlu',
                '✓ Telif durumu: CC0 veya benzer',
                '✓ Benzersizlik: Her blog farklı görsel'
            ]
        }
        
        return workflow

    def save_comprehensive_guide(self):
        """Kapsamlı rehberi kaydet"""
        print("📋 Manuel görsel seçim rehberi oluşturuluyor...")
        
        # Önerileri oluştur
        recommendations = self.generate_detailed_recommendations()
        workflow = self.generate_selection_workflow()
        
        # Yeni CSV oluştur
        csv_content = self.create_csv_with_suggestions()
        
        # Dosya yolları
        guide_path = os.path.join(self.project_root, 'seo/reports/manual_image_selection_guide.json')
        csv_path = os.path.join(self.project_root, 'seo/reports/priority_image_selection.csv')
        
        # Rehberi kaydet
        complete_guide = {
            'guide_date': datetime.now().isoformat(),
            'project': 'DryAlle Manuel Görsel Seçim Rehberi',
            'recommendations': recommendations,
            'workflow': workflow,
            'summary': {
                'total_blogs': 69,
                'critical_priority': len(recommendations['critical_priorities']) if recommendations else 0,
                'themes_covered': len(recommendations['theme_based_suggestions']) if recommendations else 0,
                'estimated_completion_time': '7-10 saat'
            }
        }
        
        with open(guide_path, 'w', encoding='utf-8') as f:
            json.dump(complete_guide, f, ensure_ascii=False, indent=2)
        
        # Öncelikli CSV kaydet
        if csv_content:
            with open(csv_path, 'w', encoding='utf-8') as f:
                f.write(csv_content)
        
        return guide_path, csv_path, complete_guide

def main():
    """Manuel Görsel Seçim Rehberi Oluştur"""
    print("📋 MANUEL GÖRSEL SEÇİM REHBERİ")
    print("=" * 60)
    print("🎯 API'siz Manuel Seçim | Tema Önerileri | İş Akışı")
    print("=" * 60)
    
    guide_generator = ManualImageSelectionGuide()
    
    try:
        # Kapsamlı rehber oluştur
        guide_path, csv_path, guide_data = guide_generator.save_comprehensive_guide()
        
        print("\n" + "=" * 60)
        print("📋 MANUEL SEÇİM REHBERİ HAZIR")
        print("=" * 60)
        
        summary = guide_data['summary']
        print(f"✅ Toplam blog: {summary['total_blogs']}")
        print(f"🚨 Kritik öncelik: {summary['critical_priority']} blog")
        print(f"🎨 Tema sayısı: {summary['themes_covered']}")
        print(f"⏱️ Tahmini süre: {summary['estimated_completion_time']}")
        
        print(f"\n📊 TEMA DAĞILIMI:")
        if 'recommendations' in guide_data and guide_data['recommendations']:
            for theme, data in guide_data['recommendations']['theme_based_suggestions'].items():
                blog_count = len(data['blogs_in_theme'])
                print(f"   {theme}: {blog_count} blog")
        
        print(f"\n🔄 İŞ AKIŞI ADIMLARI:")
        if 'workflow' in guide_data:
            for step_data in guide_data['workflow']['steps']:
                print(f"   {step_data['step']}. {step_data['title']} ({step_data['time_estimate']})")
        
        print(f"\n📁 DOSYALAR:")
        print(f"   📋 Detaylı Rehber: {guide_path}")
        print(f"   📝 Öncelikli CSV: {csv_path}")
        
        print(f"\n💡 SONRAKI ADIMLAR:")
        print(f"   1. Öncelikli CSV dosyasını aç: {csv_path}")
        print(f"   2. CRITICAL işaretli bloglardan başla")
        print(f"   3. Örnek URL'lerden birini seç veya benzerini bul")
        print(f"   4. 'Seçilen URL' sütununa URL'yi yapıştır")
        print(f"   5. Tüm blogları tamamladıktan sonra indirme scriptini çalıştır")
        
        print(f"\n⚠️  ÖNEMLİ HATIRLATMALAR:")
        print(f"   • Her blog için farklı görsel seç")
        print(f"   • Telif hakkı açık görseller tercih et")
        print(f"   • Marka renklerine uyumlu görseller seç")
        print(f"   • 1200x630 çözünürlüğe uygun görseller bul")
        
        return True
        
    except Exception as e:
        print(f"❌ Rehber oluşturma hatası: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)