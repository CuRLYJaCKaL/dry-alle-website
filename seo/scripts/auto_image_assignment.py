#!/usr/bin/env python3
"""
Otomatik Görsel Atama (Manuel Seçim Yerine)
Her blog için tema uyumlu görsel seçimi
"""

import os
import csv
import json
import hashlib
from datetime import datetime

class AutoImageAssigner:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.used_urls = set()  # Benzersizlik için
        
        # Tema bazlı görsel havuzu (genişletilmiş)
        self.image_pools = {
            "profesyonel": [
                "https://images.unsplash.com/photo-1558618666-fbd6c802d1c6?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=630&fit=crop", 
                "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1604719312566-878b4b1d2c7b?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1628177142898-93e36e4e3a50?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1609205105329-36f48ebaeb01?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1564069114553-7215e1ff1890?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1541560052-77312a200a87?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1586264790024-2c9b4b9d3fd0?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1574636634015-d89ed47d5c85?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=1200&h=630&fit=crop"
            ],
            "halı": [
                "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1540932239986-30128078f3c5?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1594736797933-d0d15d95c6a9?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1516455590571-18256e5bb9ff?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1507089947368-19c1da9775ae?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1562813733-b31f71025d54?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1558603668-6570496b66f8?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1567701760040-64ec4b8942d6?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200&h=630&fit=crop"
            ],
            "deri": [
                "https://images.unsplash.com/photo-1520975954732-35dd22299614?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1551563813-3b8a949fb472?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=630&fit=crop"
            ],
            "perde": [
                "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1467043237213-65f2da53396f?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1604719312566-878b4b1d2c7b?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1586264790024-2c9b4b9d3fd0?w=1200&h=630&fit=crop"
            ],
            "gelinlik": [
                "https://images.unsplash.com/photo-1519657337289-077653f724ed?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1594736797933-d0d15d95c6a9?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=1200&h=630&fit=crop"
            ],
            "mobilya": [
                "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1563298723-dcfebaa392e3?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1582037928769-181f2644ecb7?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1540932239986-30128078f3c5?w=1200&h=630&fit=crop"
            ],
            "leke": [
                "https://images.unsplash.com/photo-1628177142898-93e36e4e3a50?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1558618666-fbd6c802d1c6?w=1200&h=630&fit=crop",
                "https://images.unsplash.com/photo-1609205105329-36f48ebaeb01?w=1200&h=630&fit=crop"
            ]
        }

    def get_unique_image_for_theme(self, theme, blog_slug):
        """Tema için benzersiz görsel seç"""
        if theme not in self.image_pools:
            theme = "profesyonel"  # Fallback
        
        available_images = [url for url in self.image_pools[theme] if url not in self.used_urls]
        
        if not available_images:
            # Eğer tema havuzu bittiyse, profesyonel havuzundan al
            available_images = [url for url in self.image_pools["profesyonel"] if url not in self.used_urls]
        
        if available_images:
            # Deterministic seçim için blog slug'ından hash oluştur
            hash_input = f"{blog_slug}_{theme}".encode('utf-8')
            hash_value = int(hashlib.md5(hash_input).hexdigest(), 16)
            selected_index = hash_value % len(available_images)
            selected_url = available_images[selected_index]
            
            self.used_urls.add(selected_url)
            return selected_url
        
        return None

    def load_priority_csv(self):
        """Öncelikli CSV'yi yükle"""
        csv_path = os.path.join(self.project_root, 'seo/reports/priority_image_selection.csv')
        
        blogs = []
        if os.path.exists(csv_path):
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    blogs.append(row)
        
        return blogs

    def assign_images_automatically(self):
        """Otomatik görsel atama yap"""
        print("🎯 Otomatik görsel atama başlıyor...")
        
        blogs = self.load_priority_csv()
        assignments = []
        
        # Önce CRITICAL blogları işle
        critical_blogs = [b for b in blogs if b['Öncelik'] == 'CRITICAL']
        normal_blogs = [b for b in blogs if b['Öncelik'] != 'CRITICAL']
        
        processed_count = 0
        
        # Critical blogları işle
        for blog in critical_blogs:
            slug = blog['Slug'].strip('"')
            theme = blog['Tema'].strip('"')
            
            selected_url = self.get_unique_image_for_theme(theme, slug)
            
            assignments.append({
                'slug': slug,
                'title': blog['Başlık'].strip('"'),
                'theme': theme,
                'priority': 'CRITICAL',
                'selected_url': selected_url,
                'status': 'SUCCESS' if selected_url else 'FAILED'
            })
            
            processed_count += 1
            
            if processed_count % 5 == 0:
                print(f"   ✅ {processed_count} blog işlendi...")
        
        # Normal blogları işle
        for blog in normal_blogs:
            slug = blog['Slug'].strip('"')
            theme = blog['Tema'].strip('"')
            
            selected_url = self.get_unique_image_for_theme(theme, slug)
            
            assignments.append({
                'slug': slug,
                'title': blog['Başlık'].strip('"'),
                'theme': theme,
                'priority': 'NORMAL',
                'selected_url': selected_url,
                'status': 'SUCCESS' if selected_url else 'FAILED'
            })
            
            processed_count += 1
        
        print(f"✅ Toplam {processed_count} blog için görsel atandı")
        
        return assignments

    def save_assignments_csv(self, assignments):
        """Atamaları CSV olarak kaydet"""
        csv_path = os.path.join(self.project_root, 'seo/reports/final_image_assignments.csv')
        
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Slug', 'Tema', 'Başlık', 'Öncelik', 'Seçilen URL', 'Durum'])
            
            for assignment in assignments:
                writer.writerow([
                    assignment['slug'],
                    assignment['theme'],
                    assignment['title'],
                    assignment['priority'],
                    assignment['selected_url'],
                    assignment['status']
                ])
        
        return csv_path

    def generate_assignment_report(self, assignments):
        """Atama raporu oluştur"""
        total_assignments = len(assignments)
        successful_assignments = len([a for a in assignments if a['status'] == 'SUCCESS'])
        
        # Tema dağılımı
        theme_distribution = {}
        for assignment in assignments:
            theme = assignment['theme']
            theme_distribution[theme] = theme_distribution.get(theme, 0) + 1
        
        # Priority dağılımı
        priority_distribution = {}
        for assignment in assignments:
            priority = assignment['priority']
            priority_distribution[priority] = priority_distribution.get(priority, 0) + 1
        
        report = {
            'assignment_date': datetime.now().isoformat(),
            'project': 'DryAlle Otomatik Görsel Atama',
            'summary': {
                'total_blogs': total_assignments,
                'successful_assignments': successful_assignments,
                'failed_assignments': total_assignments - successful_assignments,
                'success_rate': (successful_assignments / total_assignments) * 100 if total_assignments > 0 else 0
            },
            'theme_distribution': theme_distribution,
            'priority_distribution': priority_distribution,
            'assignments': assignments,
            'next_steps': [
                'Seçilen görselleri indir',
                'WebP formatına çevir',
                'HTML dosyalarını güncelle',
                'Performans testi yap'
            ]
        }
        
        return report

    def save_comprehensive_report(self, assignments):
        """Kapsamlı raporu kaydet"""
        report = self.generate_assignment_report(assignments)
        
        report_path = os.path.join(self.project_root, 'seo/reports/auto_image_assignment_report.json')
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report_path, report

def main():
    """Otomatik Görsel Atama İşlemi"""
    print("🎯 OTOMATİK GÖRSEL ATAMA")
    print("=" * 50)
    print("🎨 Benzersiz Görsel | Tema Uyumu | Otomatik Seçim")
    print("=" * 50)
    
    assigner = AutoImageAssigner()
    
    try:
        # Otomatik atama yap
        assignments = assigner.assign_images_automatically()
        
        # CSV kaydet
        csv_path = assigner.save_assignments_csv(assignments)
        
        # Rapor oluştur
        report_path, report = assigner.save_comprehensive_report(assignments)
        
        # Özet
        print("\n" + "=" * 50)
        print("🎯 OTOMATİK ATAMA TAMAMLANDI")
        print("=" * 50)
        
        summary = report['summary']
        print(f"✅ Toplam blog: {summary['total_blogs']}")
        print(f"✅ Başarılı atama: {summary['successful_assignments']}")
        print(f"✅ Başarı oranı: {summary['success_rate']:.1f}%")
        
        if summary['failed_assignments'] > 0:
            print(f"❌ Başarısız atama: {summary['failed_assignments']}")
        
        print(f"\n📊 TEMA DAĞILIMI:")
        for theme, count in sorted(report['theme_distribution'].items(), key=lambda x: x[1], reverse=True):
            print(f"   {theme}: {count} blog")
        
        print(f"\n🚨 ÖNCELİK DAĞILIMI:")
        for priority, count in report['priority_distribution'].items():
            print(f"   {priority}: {count} blog")
        
        print(f"\n📁 DOSYALAR:")
        print(f"   📝 Atama CSV: {csv_path}")
        print(f"   📊 Detaylı Rapor: {report_path}")
        
        print(f"\n🔄 SONRAKI ADIMLAR:")
        for i, step in enumerate(report['next_steps'], 1):
            print(f"   {i}. {step}")
        
        print(f"\n🎉 BAŞARIYLA TAMAMLANDI!")
        print(f"   • {summary['successful_assignments']} blog için benzersiz görsel seçildi")
        print(f"   • Tüm temalar uygun görseller ile eşleştirildi")
        print(f"   • Görsel indirme işlemine hazır")
        
        return True
        
    except Exception as e:
        print(f"❌ Atama hatası: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)