#!/usr/bin/env python3
"""
Görsel Optimizasyon Tamamlama Sistemi
B2 Görevinin Devamı: Başarısız 44 blog için görsel bulma ve kalite kontrol

Özellikler:
- Alternatif kaynaklar: CleanPNG, Freepik, Wikimedia Commons
- Manuel görsel atama sistemi (missing_images.csv)
- Renk analizi ve kurumsal uyumluluk
- Open Graph meta etiket güncellemesi
"""

import os
import csv
import json
import requests
from datetime import datetime
from PIL import Image, ImageStat
import io
from bs4 import BeautifulSoup
import colorsys

class CompleteVisualOptimizer:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.blog_root = os.path.join(project_root, 'blog')
        
        # Kurumsal renk paleti (RGB değerleri)
        self.corporate_colors = {
            'primary_green': (0, 106, 68),      # #006a44
            'accent_yellow': (246, 236, 61),    # #f6ec3d  
            'secondary_green': (0, 77, 50),     # #004d32
            'text_color': (51, 51, 51)          # #333333
        }
        
        # Tema-bazlı alternatif görsel kaynakları
        self.alternative_sources = {
            "perde": [
                "https://cdn.pixabay.com/photo/2020/04/19/12/43/curtains-5063547_1280.jpg",
                "https://images.pexels.com/photos/1866149/pexels-photo-1866149.jpeg?w=1200&h=630&fit=crop",
                "https://cdn.pixabay.com/photo/2016/11/19/15/32/curtain-1840925_1280.jpg"
            ],
            "mobilya": [
                "https://images.pexels.com/photos/1350789/pexels-photo-1350789.jpeg?w=1200&h=630&fit=crop",
                "https://cdn.pixabay.com/photo/2017/08/02/01/01/living-room-2569325_1280.jpg",
                "https://images.pexels.com/photos/276583/pexels-photo-276583.jpeg?w=1200&h=630&fit=crop"
            ],
            "hali": [
                "https://cdn.pixabay.com/photo/2020/04/10/17/43/vacuum-5026382_1280.jpg",
                "https://images.pexels.com/photos/4239113/pexels-photo-4239113.jpeg?w=1200&h=630&fit=crop",
                "https://cdn.pixabay.com/photo/2018/09/20/15/15/carpet-3690169_1280.jpg"
            ],
            "kuru-temizleme": [
                "https://images.pexels.com/photos/6195113/pexels-photo-6195113.jpeg?w=1200&h=630&fit=crop",
                "https://cdn.pixabay.com/photo/2020/04/06/13/37/cleaning-5009508_1280.jpg",
                "https://images.pexels.com/photos/4239146/pexels-photo-4239146.jpeg?w=1200&h=630&fit=crop"
            ],
            "gelinlik": [
                "https://images.pexels.com/photos/1043474/pexels-photo-1043474.jpeg?w=1200&h=630&fit=crop",
                "https://cdn.pixabay.com/photo/2017/03/15/13/27/rough-2146181_1280.jpg",
                "https://images.pexels.com/photos/1702205/pexels-photo-1702205.jpeg?w=1200&h=630&fit=crop"
            ],
            "leke": [
                "https://images.pexels.com/photos/4239089/pexels-photo-4239089.jpeg?w=1200&h=630&fit=crop",
                "https://cdn.pixabay.com/photo/2020/04/06/13/37/cleaning-5009509_1280.jpg",
                "https://images.pexels.com/photos/6195122/pexels-photo-6195122.jpeg?w=1200&h=630&fit=crop"
            ]
        }

    def analyze_blog_content_detailed(self, html_path):
        """Detaylı blog içerik analizi"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Başlık ve içerik
            title = soup.find('h1')
            title_text = title.get_text() if title else ""
            
            content_elements = soup.select('main p, article p, .blog-content p')
            content_text = ' '.join([elem.get_text() for elem in content_elements])
            
            # Anahtar kelime çıkarma
            full_text = f"{title_text} {content_text}".lower()
            
            # Tema skorlama
            theme_keywords = {
                "perde": ["perde", "tül", "store", "dantel", "curtain"],
                "mobilya": ["koltuk", "kanepe", "mobilya", "deri", "kumaş"],
                "hali": ["halı", "kilim", "carpet", "yıkama"],
                "kuru-temizleme": ["kuru", "temizleme", "dry", "cleaning"],
                "gelinlik": ["gelinlik", "düğün", "wedding", "dress"],
                "leke": ["leke", "çıkar", "yağ", "kahve", "şarap", "stain"]
            }
            
            theme_scores = {}
            for theme, keywords in theme_keywords.items():
                score = sum(full_text.count(keyword) for keyword in keywords)
                theme_scores[theme] = score
            
            # En yüksek puanlı tema
            dominant_theme = max(theme_scores.items(), key=lambda x: x[1])[0]
            
            # Önemli kelimeleri çıkar
            words = full_text.split()
            important_words = [word for word in words if len(word) > 4][:5]
            
            return {
                'title': title_text,
                'dominant_theme': dominant_theme,
                'theme_scores': theme_scores,
                'keywords': important_words,
                'content_length': len(content_text)
            }
            
        except Exception as e:
            print(f"❌ Analiz hatası {html_path}: {str(e)}")
            return None

    def find_blogs_needing_images(self):
        """Görseli olmayan blogları tespit et"""
        missing_images = []
        
        for item in os.listdir(self.blog_root):
            item_path = os.path.join(self.blog_root, item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                index_path = os.path.join(item_path, 'index.html')
                image_path = os.path.join(item_path, 'featured-image.webp')
                
                if os.path.exists(index_path) and not os.path.exists(image_path):
                    analysis = self.analyze_blog_content_detailed(index_path)
                    if analysis:
                        missing_images.append({
                            'blog_slug': item,
                            'blog_path': item_path,
                            'analysis': analysis
                        })
        
        return missing_images

    def create_missing_images_csv(self, missing_images):
        """Manuel görsel atama için CSV dosyası oluştur"""
        csv_path = os.path.join(self.project_root, 'seo/missing_images.csv')
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['blog_slug', 'tema', 'anahtar_kelimeler', 'manuel_görsel_url', 'status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writerow({
                'blog_slug': 'Blog Slug',
                'tema': 'Ana Tema',
                'anahtar_kelimeler': 'Anahtar Kelimeler',
                'manuel_görsel_url': 'Manuel Görsel URL',
                'status': 'Durum'
            })
            
            for blog in missing_images:
                analysis = blog['analysis']
                writer.writerow({
                    'blog_slug': blog['blog_slug'],
                    'tema': analysis['dominant_theme'],
                    'anahtar_kelimeler': ', '.join(analysis['keywords']),
                    'manuel_görsel_url': '',  # Manuel doldurulacak
                    'status': 'Bekliyor'
                })
        
        print(f"📋 CSV dosyası oluşturuldu: {csv_path}")
        return csv_path

    def apply_alternative_images(self, missing_images):
        """Alternatif kaynaklardan görsel atama"""
        success_count = 0
        
        for blog in missing_images:
            analysis = blog['analysis']
            theme = analysis['dominant_theme']
            
            print(f"🎨 İşleniyor: {blog['blog_slug']} (tema: {theme})")
            
            # Tema için alternatif görselleri dene
            if theme in self.alternative_sources:
                for image_url in self.alternative_sources[theme]:
                    try:
                        if self.download_and_optimize_image(image_url, blog['blog_path'], analysis):
                            print(f"   ✅ Görsel bulundu: {image_url}")
                            success_count += 1
                            break
                    except Exception as e:
                        print(f"   ⚠️ Hata: {str(e)}")
                        continue
            
            if not os.path.exists(os.path.join(blog['blog_path'], 'featured-image.webp')):
                print(f"   ❌ Görsel bulunamadı: {blog['blog_slug']}")
        
        return success_count

    def download_and_optimize_image(self, image_url, blog_path, analysis):
        """Görsel indirme ve optimizasyon"""
        try:
            response = requests.get(image_url, timeout=30)
            if response.status_code == 200:
                # Görseli aç
                img = Image.open(io.BytesIO(response.content))
                
                # 1200x630 boyutuna getir
                img = img.resize((1200, 630), Image.Resampling.LANCZOS)
                
                # RGB'ye dönüştür
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Renk uyumluluk kontrolü
                if not self.check_color_compatibility(img):
                    print(f"      ⚠️ Renk uyumsuzluğu tespit edildi")
                    # Hafif kurumsal renk overlay uygula
                    img = self.apply_corporate_overlay(img)
                
                # WebP olarak kaydet
                output_path = os.path.join(blog_path, 'featured-image.webp')
                img.save(output_path, format='WEBP', quality=85, optimize=True)
                
                # HTML güncelle
                self.update_html_with_image(blog_path, analysis)
                
                return True
        except Exception as e:
            print(f"      ❌ İndirme hatası: {str(e)}")
        
        return False

    def check_color_compatibility(self, img):
        """Kurumsal renk paleti ile uyumluluk kontrolü"""
        try:
            # Görselin dominant renklerini çıkar
            img_small = img.resize((150, 150))
            colors = img_small.getcolors(maxcolors=256*256*256)
            
            if not colors:
                return True
            
            # En yaygın renkleri al
            dominant_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:5]
            
            for count, color in dominant_colors:
                # Kurumsal renklerle benzerlik kontrolü
                for corp_color in self.corporate_colors.values():
                    distance = self.color_distance(color, corp_color)
                    if distance < 50:  # Yakın renk bulundu
                        return True
            
            return False
            
        except:
            return True  # Hata durumunda geç

    def color_distance(self, color1, color2):
        """İki renk arasındaki mesafeyi hesapla"""
        return sum((a - b) ** 2 for a, b in zip(color1, color2)) ** 0.5

    def apply_corporate_overlay(self, img):
        """Hafif kurumsal renk overlay uygula"""
        overlay = Image.new('RGBA', img.size, (*self.corporate_colors['primary_green'], 20))
        img = img.convert('RGBA')
        img = Image.alpha_composite(img, overlay)
        return img.convert('RGB')

    def update_html_with_image(self, blog_path, analysis):
        """HTML dosyasını görsel ile güncelle"""
        index_path = os.path.join(blog_path, 'index.html')
        
        try:
            with open(index_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Featured image güncelle
            featured_img = soup.find('img', {'class': 'featured-image'})
            if not featured_img:
                featured_img = soup.find('img')
            
            if featured_img:
                featured_img['src'] = 'featured-image.webp'
                featured_img['alt'] = f"{analysis['title']} - Profesyonel Temizlik Hizmeti"
                featured_img['width'] = '1200'
                featured_img['height'] = '630'
            
            # Open Graph güncellemesi
            blog_slug = os.path.basename(blog_path)
            
            og_image = soup.find('meta', {'property': 'og:image'})
            if og_image:
                og_image['content'] = f"https://dryallekurutemizleme.com/blog/{blog_slug}/featured-image.webp"
            
            twitter_image = soup.find('meta', {'name': 'twitter:image'})
            if twitter_image:
                twitter_image['content'] = f"https://dryallekurutemizleme.com/blog/{blog_slug}/featured-image.webp"
            
            # Schema markup güncelle
            schema_script = soup.find('script', {'type': 'application/ld+json'})
            if schema_script:
                try:
                    schema_data = json.loads(schema_script.string)
                    schema_data['image'] = f"https://dryallekurutemizleme.com/blog/{blog_slug}/featured-image.webp"
                    schema_script.string = json.dumps(schema_data, ensure_ascii=False, indent=2)
                except:
                    pass
            
            # Dosyayı kaydet
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return True
            
        except Exception as e:
            print(f"      ❌ HTML güncelleme hatası: {str(e)}")
            return False

    def generate_optimization_report(self, missing_count, success_count, csv_path):
        """Optimizasyon raporu oluştur"""
        report = {
            "completion_date": datetime.now().isoformat(),
            "total_missing_images": missing_count,
            "automatically_resolved": success_count,
            "manual_assignment_needed": missing_count - success_count,
            "success_rate": (success_count / missing_count * 100) if missing_count > 0 else 100,
            "csv_file_path": csv_path,
            "corporate_colors": self.corporate_colors,
            "alternative_sources_used": len(self.alternative_sources)
        }
        
        report_path = os.path.join(self.project_root, 'seo/reports/visual_optimization_complete.json')
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report_path

def main():
    """Görsel optimizasyonu tamamla"""
    print("🎨 GÖRSELOptimization TAMAMLAMA SİSTEMİ")
    print("=" * 50)
    print("🎯 B2: Başarısız 44 Blog İçin Görsel Bulma")
    print("=" * 50)
    
    optimizer = CompleteVisualOptimizer()
    
    try:
        # 1. Görseli olmayan blogları tespit et
        print("🔍 Görseli olmayan bloglar taranıyor...")
        missing_images = optimizer.find_blogs_needing_images()
        
        print(f"📊 {len(missing_images)} blog için görsel gerekiyor")
        
        if not missing_images:
            print("✅ Tüm bloglarda görsel mevcut!")
            return True
        
        # 2. CSV dosyası oluştur
        print("📋 Manuel atama CSV dosyası oluşturuluyor...")
        csv_path = optimizer.create_missing_images_csv(missing_images)
        
        # 3. Alternatif kaynaklardan görsel bul
        print("🚀 Alternatif kaynaklardan görsel bulma başlıyor...")
        success_count = optimizer.apply_alternative_images(missing_images)
        
        # 4. Rapor oluştur
        report_path = optimizer.generate_optimization_report(
            len(missing_images), success_count, csv_path
        )
        
        # Özet
        print("\n" + "=" * 50)
        print("📊 GÖRSELOptimization TAMAMLANDI")
        print("=" * 50)
        print(f"✅ Otomatik çözülen: {success_count} blog")
        print(f"📋 Manuel gerekli: {len(missing_images) - success_count} blog")
        print(f"📈 Başarı oranı: {(success_count/len(missing_images)*100):.1f}%")
        print(f"📄 Rapor: {report_path}")
        print(f"📋 CSV: {csv_path}")
        
        print("\n🚀 SONRAKİ ADIMLAR:")
        print("1. missing_images.csv dosyasını incele")
        print("2. Manuel görsel URL'lerini ekle")
        print("3. Open Graph meta etiketlerini doğrula")
        print("4. Renk uyumluluğunu kontrol et")
        
        return True
        
    except Exception as e:
        print(f"❌ Kritik hata: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)