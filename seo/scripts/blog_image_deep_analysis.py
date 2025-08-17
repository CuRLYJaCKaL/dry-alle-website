#!/usr/bin/env python3
"""
Derinlemesine Blog Görsel Optimizasyonu
Tematik çeşitlilik ve anlam bütünlüğü sağlama
"""

import os
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup
from collections import Counter

class BlogImageAnalyzer:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.blog_root = os.path.join(project_root, 'blog')
        
        # Tematik kategoriler ve anahtar kelimeler
        self.themes = {
            "perde": ["perde", "tül", "stor", "pencere", "cam", "kapı", "ev tekstili", "dekorasyon"],
            "mobilya": ["koltuk", "kanepe", "kumaş", "döşeme", "sandalye", "berjer", "minder", "yastık"],
            "halı": ["halı", "kilim", "yün", "el dokuma", "kaymaz", "antika", "vintage", "dokuma"],
            "leke": ["leke çıkarma", "yağ lekesi", "kahve lekesi", "kan lekesi", "mürekkep", "pas", "temizlik"],
            "gelinlik": ["gelinlik", "düğün", "özel gün", "abiye", "tüvit", "gece elbisesi", "kostüm"],
            "deri": ["deri", "süet", "nubuk", "vintage deri", "deri ceket", "ayakkabı", "çanta"],
            "ipek": ["ipek", "saten", "şifon", "organze", "brokat", "jakarlı", "kadife"],
            "yün": ["yün", "kaşmir", "angora", "yünlü", "triko", "kazak", "mont", "palto"],
            "profesyonel": ["kuru temizleme", "profesyonel", "makine", "kimyasal", "uzman", "teknisyen"]
        }
        
        # Kurumsal renkler ve stil gereksinimleri
        self.brand_requirements = {
            "primary_colors": ["#006a44", "#f6ec3d", "#e1e1e1", "#f0f0f0"],
            "style": "temiz, profesyonel, güvenilir",
            "mood": "temizlik, kalite, güven"
        }

    def analyze_blog_content(self, blog_dir, html_path):
        """Blog içeriğini derinlemesine analiz et"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Başlık ve meta bilgileri
            title = soup.find('title')
            title_text = title.get_text() if title else ""
            
            meta_desc = soup.find('meta', {'name': 'description'})
            description = meta_desc.get('content', '') if meta_desc else ""
            
            # Ana içerik
            main_content = ""
            for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li']):
                main_content += tag.get_text() + " "
            
            # Tüm metni temizle ve analiz et
            full_text = (title_text + " " + description + " " + main_content).lower()
            
            # Tema analizi
            theme_scores = {}
            for theme, keywords in self.themes.items():
                score = sum(full_text.count(keyword) for keyword in keywords)
                if score > 0:
                    theme_scores[theme] = score
            
            # Birincil tema
            primary_theme = max(theme_scores, key=theme_scores.get) if theme_scores else "genel"
            
            # Anahtar kelime çıkarımı
            words = re.findall(r'\b\w{4,}\b', full_text)
            stop_words = {'için', 'olan', 'ile', 'bir', 'bu', 'şu', 'olarak', 'kadar', 'sonra', 'önce', 'sırasında', 'esnasında', 'sebebiyle', 'nedeniyle'}
            filtered_words = [w for w in words if w not in stop_words and not w.isdigit()]
            
            word_counts = Counter(filtered_words)
            top_keywords = [word for word, count in word_counts.most_common(8) if count > 1]
            
            # Özel gereksinimler
            special_requirements = []
            
            # Lokasyon bazlı
            if any(loc in full_text for loc in ['istanbul', 'ankara', 'izmir']):
                special_requirements.append("Türkiye lokasyonu")
            
            # Sezon bazlı
            if any(season in full_text for season in ['kış', 'yaz', 'sonbahar', 'ilkbahar']):
                special_requirements.append("Mevsimsel")
            
            # Özel durum
            if any(special in full_text for special in ['acil', 'hızlı', '24 saat', 'express']):
                special_requirements.append("Hızlı servis")
            
            # Mevcut görsel analizi
            current_image = soup.find('img', {'class': 'featured-image'})
            current_image_info = {
                'exists': current_image is not None,
                'src': current_image.get('src', '') if current_image else '',
                'alt': current_image.get('alt', '') if current_image else '',
                'size_info': self.get_image_size_info(blog_dir, current_image.get('src', '')) if current_image else None
            }
            
            return {
                'slug': blog_dir,
                'title': title_text.strip(),
                'description': description.strip(),
                'primary_theme': primary_theme,
                'theme_scores': theme_scores,
                'keywords': top_keywords[:5],
                'special_requirements': special_requirements,
                'content_length': len(main_content.split()),
                'current_image': current_image_info,
                'seo_analysis': {
                    'has_title': bool(title_text),
                    'has_description': bool(description),
                    'title_length': len(title_text),
                    'description_length': len(description)
                }
            }
            
        except Exception as e:
            print(f"❌ Error analyzing {blog_dir}: {str(e)}")
            return None

    def get_image_size_info(self, blog_dir, img_src):
        """Mevcut görsel boyut bilgisini al"""
        if not img_src:
            return None
            
        img_path = os.path.join(self.blog_root, blog_dir, img_src)
        if os.path.exists(img_path):
            try:
                from PIL import Image
                with Image.open(img_path) as img:
                    return {
                        'width': img.width,
                        'height': img.height,
                        'format': img.format,
                        'size_kb': os.path.getsize(img_path) // 1024
                    }
            except Exception:
                return {'error': 'Cannot read image'}
        return None

    def generate_image_requirements(self, analysis):
        """Her blog için görsel gereksinimleri oluştur"""
        requirements = {
            'primary_subject': analysis['primary_theme'],
            'context': 'kuru temizleme, profesyonel temizlik',
            'style': 'temiz, modern, profesyonel',
            'color_harmony': self.brand_requirements['primary_colors'],
            'mood': self.brand_requirements['mood']
        }
        
        # Tema bazlı özel gereksinimler
        theme_specific = {
            'perde': {
                'subjects': ['perde temizliği', 'ev tekstili', 'pencere dekorasyonu'],
                'settings': ['ev ortamı', 'modern salon', 'temiz pencere'],
                'props': ['temiz perde', 'ütü', 'temizlik malzemeleri']
            },
            'mobilya': {
                'subjects': ['koltuk temizliği', 'kumaş bakımı', 'döşeme temizliği'],
                'settings': ['modern salon', 'oturma odası', 'temiz ev'],
                'props': ['temiz koltuk', 'temizlik ekipmanı', 'kumaş bakım ürünleri']
            },
            'halı': {
                'subjects': ['halı temizliği', 'kilim bakımı', 'zemin temizliği'],
                'settings': ['ev içi', 'salon', 'temiz zemin'],
                'props': ['temiz halı', 'temizlik makinesi', 'bakım ürünleri']
            },
            'leke': {
                'subjects': ['leke çıkarma', 'temizlik işlemi', 'önce-sonra'],
                'settings': ['temizlik atölyesi', 'profesyonel ortam'],
                'props': ['temizlik ürünleri', 'leke çıkarma malzemeleri']
            },
            'gelinlik': {
                'subjects': ['gelinlik bakımı', 'özel gün hazırlığı', 'nazik temizlik'],
                'settings': ['butik ortamı', 'temiz, şık mekan'],
                'props': ['beyaz gelinlik', 'özenli ambalaj', 'premium hizmet']
            }
        }
        
        if analysis['primary_theme'] in theme_specific:
            requirements.update(theme_specific[analysis['primary_theme']])
        
        # Anahtar kelime bazlı ek gereksinimler
        for keyword in analysis['keywords']:
            if keyword in ['istanbul', 'ankara', 'izmir']:
                requirements['location'] = f'{keyword} şehir manzarası'
            elif keyword in ['acil', 'hızlı', 'express']:
                requirements['urgency'] = 'hızlı servis, acil durum'
            elif keyword in ['premium', 'lüks', 'özel']:
                requirements['quality_level'] = 'premium, lüks hizmet'
        
        return requirements

    def create_manual_selection_data(self):
        """Manuel seçim için veri hazırla"""
        print("📊 Blog içeriklerini analiz ediliyor...")
        
        all_analyses = []
        
        for blog_dir in os.listdir(self.blog_root):
            if blog_dir.startswith('.') or blog_dir == 'index.html':
                continue
            
            blog_path = os.path.join(self.blog_root, blog_dir)
            index_path = os.path.join(blog_path, 'index.html')
            
            if os.path.isdir(blog_path) and os.path.exists(index_path):
                analysis = self.analyze_blog_content(blog_dir, index_path)
                if analysis:
                    # Görsel gereksinimleri ekle
                    analysis['image_requirements'] = self.generate_image_requirements(analysis)
                    all_analyses.append(analysis)
        
        return all_analyses

    def generate_image_search_queries(self, analysis):
        """Her blog için özel arama sorguları oluştur"""
        base_queries = []
        
        # Temel tema sorguları
        theme = analysis['primary_theme']
        base_queries.extend([
            f"{theme} cleaning professional",
            f"{theme} care service",
            f"dry cleaning {theme}",
            f"professional {theme} maintenance"
        ])
        
        # Anahtar kelime kombinasyonları
        for keyword in analysis['keywords'][:3]:
            if len(keyword) > 3:
                base_queries.append(f"{keyword} professional cleaning")
        
        # Özel durum sorguları
        if 'Türkiye lokasyonu' in analysis['special_requirements']:
            base_queries.append(f"{theme} cleaning Turkey Istanbul")
        
        if 'Hızlı servis' in analysis['special_requirements']:
            base_queries.append(f"fast {theme} cleaning service")
        
        # Görsel tarzı sorguları
        base_queries.extend([
            f"clean modern {theme}",
            f"professional laundry {theme}",
            f"before after {theme} cleaning"
        ])
        
        return base_queries[:8]  # En fazla 8 sorgu

    def create_selection_csv(self, analyses):
        """Manuel seçim için CSV dosyası oluştur"""
        csv_content = "Slug,Tema,Başlık,Anahtar Kelimeler,Özel Gereksinimler,Mevcut Görsel,Görsel Gereksinimleri,Arama Sorguları,Seçilen Görsel URL,Notlar\n"
        
        for analysis in analyses:
            slug = analysis['slug']
            theme = analysis['primary_theme']
            title = analysis['title'].replace(',', ';')
            keywords = '; '.join(analysis['keywords'])
            requirements = '; '.join(analysis['special_requirements'])
            current_img = analysis['current_image']['src'] if analysis['current_image']['exists'] else 'Yok'
            
            # Görsel gereksinimleri özet
            img_req = analysis['image_requirements']
            req_summary = f"Konu: {img_req['primary_subject']}, Stil: {img_req['style']}"
            
            # Arama sorguları
            search_queries = self.generate_image_search_queries(analysis)
            queries_text = '; '.join(search_queries)
            
            csv_content += f'"{slug}","{theme}","{title}","{keywords}","{requirements}","{current_img}","{req_summary}","{queries_text}","",""\n'
        
        return csv_content

    def generate_theme_distribution_report(self, analyses):
        """Tema dağılım raporu oluştur"""
        theme_distribution = {}
        for analysis in analyses:
            theme = analysis['primary_theme']
            theme_distribution[theme] = theme_distribution.get(theme, 0) + 1
        
        return {
            'total_blogs': len(analyses),
            'theme_distribution': theme_distribution,
            'diversity_score': len(theme_distribution) / len(analyses) * 100,
            'recommendations': self.get_diversity_recommendations(theme_distribution)
        }

    def get_diversity_recommendations(self, theme_distribution):
        """Çeşitlilik önerileri oluştur"""
        recommendations = []
        
        # En çok kullanılan tema
        most_common = max(theme_distribution, key=theme_distribution.get)
        most_count = theme_distribution[most_common]
        
        if most_count > len(theme_distribution) * 0.4:  # %40'tan fazla
            recommendations.append(f"'{most_common}' teması çok baskın ({most_count} blog). Çeşitlilik için diğer temalar güçlendirilmeli.")
        
        # Az kullanılan temalar
        rare_themes = [theme for theme, count in theme_distribution.items() if count == 1]
        if rare_themes:
            recommendations.append(f"Tek blog ile temsil edilen temalar: {', '.join(rare_themes)}")
        
        # Eksik temalar
        all_possible_themes = set(self.themes.keys())
        used_themes = set(theme_distribution.keys())
        missing_themes = all_possible_themes - used_themes
        
        if missing_themes:
            recommendations.append(f"Hiç kullanılmayan temalar: {', '.join(missing_themes)}")
        
        return recommendations

    def generate_comprehensive_report(self):
        """Kapsamlı analiz raporu oluştur"""
        print("📊 Kapsamlı blog görsel analizi başlıyor...")
        
        # Tüm analizleri yap
        analyses = self.create_manual_selection_data()
        
        # Tema dağılım analizi
        theme_report = self.generate_theme_distribution_report(analyses)
        
        # Manuel seçim CSV'si oluştur
        csv_content = self.create_selection_csv(analyses)
        
        # Ana rapor
        report = {
            'analysis_date': datetime.now().isoformat(),
            'project': 'DryAlle Blog Görsel Optimizasyonu',
            'total_blogs_analyzed': len(analyses),
            'theme_distribution': theme_report,
            'detailed_analyses': analyses,
            'optimization_priorities': self.get_optimization_priorities(analyses),
            'next_steps': [
                'Manuel görsel seçimi için CSV dosyasını incele',
                'Her blog için en uygun 3 görsel adayını belirle', 
                'Seçilen görselleri WebP formatına dönüştür',
                'HTML dosyalarını güncelle',
                'Lighthouse performans testi yap'
            ]
        }
        
        # Dosyaları kaydet
        analysis_path = os.path.join(self.project_root, 'seo/reports/blog_image_analysis.json')
        csv_path = os.path.join(self.project_root, 'seo/reports/image_selection.csv')
        
        os.makedirs(os.path.dirname(analysis_path), exist_ok=True)
        
        with open(analysis_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write(csv_content)
        
        return analysis_path, csv_path, report

    def get_optimization_priorities(self, analyses):
        """Optimizasyon önceliklerini belirle"""
        priorities = []
        
        # Görseli olmayan bloglar
        no_image_blogs = [a for a in analyses if not a['current_image']['exists']]
        if no_image_blogs:
            priorities.append({
                'level': 'CRITICAL',
                'issue': f'{len(no_image_blogs)} blog hiç görseli yok',
                'blogs': [b['slug'] for b in no_image_blogs]
            })
        
        # Düşük kaliteli görseller
        low_quality_blogs = []
        for a in analyses:
            if a['current_image']['exists']:
                size_info = a['current_image'].get('size_info')
                if size_info and size_info.get('size_kb', 0) > 200:
                    low_quality_blogs.append(a['slug'])
        
        if low_quality_blogs:
            priorities.append({
                'level': 'HIGH',
                'issue': f'{len(low_quality_blogs)} blog büyük boyutlu görsel kullanıyor (>200KB)',
                'blogs': low_quality_blogs
            })
        
        # Tema uyumsuzluğu (bu aşamada analiz edemiyoruz, placeholder)
        priorities.append({
            'level': 'MEDIUM',
            'issue': 'Tüm bloglar için tema-görsel uyumluluğu kontrol edilmeli',
            'blogs': [a['slug'] for a in analyses]
        })
        
        return priorities

def main():
    """Blog Görsel Analizi ve Optimizasyon Planı"""
    print("🖼️ BLOG GÖRSEL OPTİMİZASYONU - DERİNLEMESİNE ANALİZ")
    print("=" * 70)
    print("🎯 Tematik Çeşitlilik | Anlam Bütünlüğü | Görsel Kalite")
    print("=" * 70)
    
    analyzer = BlogImageAnalyzer()
    
    try:
        # Kapsamlı analiz
        analysis_path, csv_path, report = analyzer.generate_comprehensive_report()
        
        # Özet
        print("\n" + "=" * 70)
        print("🖼️ BLOG GÖRSEL ANALİZİ TAMAMLANDI")
        print("=" * 70)
        
        print(f"✅ Analiz edilen blog sayısı: {report['total_blogs_analyzed']}")
        
        # Tema dağılımı
        theme_dist = report['theme_distribution']['theme_distribution']
        print(f"✅ Tema dağılımı:")
        for theme, count in sorted(theme_dist.items(), key=lambda x: x[1], reverse=True):
            print(f"   {theme}: {count} blog")
        
        # Çeşitlilik skoru
        diversity = report['theme_distribution']['diversity_score']
        print(f"✅ Çeşitlilik skoru: {diversity:.1f}%")
        
        # Öncelikli sorunlar
        priorities = report['optimization_priorities']
        critical_issues = [p for p in priorities if p['level'] == 'CRITICAL']
        if critical_issues:
            print(f"\n🚨 KRİTİK SORUNLAR:")
            for issue in critical_issues:
                print(f"   • {issue['issue']}")
        
        # Öneriler
        recommendations = report['theme_distribution']['recommendations']
        if recommendations:
            print(f"\n💡 ÖNERİLER:")
            for i, rec in enumerate(recommendations[:3], 1):
                print(f"   {i}. {rec}")
        
        print(f"\n📋 MANUEL SEÇİM İÇİN:")
        print(f"   📊 Detaylı Analiz: {analysis_path}")
        print(f"   📝 Seçim Tablosu: {csv_path}")
        
        print(f"\n🔄 SONRAKI ADIMLAR:")
        for i, step in enumerate(report['next_steps'][:3], 1):
            print(f"   {i}. {step}")
        
        print(f"\n💻 MANUEL KONTROL GEREKSİNİMİ:")
        print(f"   • CSV dosyasını açın: {csv_path}")
        print(f"   • Her blog için 'Seçilen Görsel URL' sütununu doldurun")
        print(f"   • Ardından görsel indirme ve optimizasyon scriptini çalıştırın")
        
        return True
        
    except Exception as e:
        print(f"❌ Analiz hatası: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)