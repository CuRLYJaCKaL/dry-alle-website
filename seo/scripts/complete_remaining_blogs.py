#!/usr/bin/env python3
"""
Kalan Bloglar İçin Görsel Entegrasyonu
Görseli olmayan 13 blog için kapsamlı görsel seçimi ve optimizasyonu
"""

import os
import json
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

class RemainingBlogsCompleter:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.blog_root = os.path.join(project_root, 'blog')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        # Kalan bloglar için görsel havuzu (yeni URL'ler)
        self.remaining_image_pool = [
            "https://images.unsplash.com/photo-1604719312566-878b4b1d2c7b?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1564069114553-7215e1ff1890?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1628177142898-93e36e4e3a50?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1609205105329-36f48ebaeb01?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1541560052-77312a200a87?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1586264790024-2c9b4b9d3fd0?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1558618666-fbd6c802d1c6?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=630&fit=crop",
            "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=1200&h=630&fit=crop"
        ]
        self.used_urls = set()

    def find_blogs_without_images(self):
        """Görseli olmayan blogları bul"""
        blogs_without_images = []
        
        for blog_dir in os.listdir(self.blog_root):
            if blog_dir.startswith('.') or blog_dir == 'index.html':
                continue
            
            blog_path = os.path.join(self.blog_root, blog_dir)
            if not os.path.isdir(blog_path):
                continue
            
            # Featured image kontrolü
            featured_webp = os.path.join(blog_path, 'featured-image.webp')
            
            if not os.path.exists(featured_webp):
                # Blog analizi
                index_path = os.path.join(blog_path, 'index.html')
                if os.path.exists(index_path):
                    analysis = self.analyze_blog_for_theme(index_path, blog_dir)
                    if analysis:
                        blogs_without_images.append(analysis)
        
        return blogs_without_images

    def analyze_blog_for_theme(self, html_path, slug):
        """Blog temasını analiz et"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Başlık ve içerik
            title = soup.find('title')
            title_text = title.get_text() if title else ""
            
            # Ana içerik
            main_content = ""
            for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'li']):
                main_content += tag.get_text() + " "
            
            full_text = (title_text + " " + main_content).lower()
            
            # Tema tespiti
            theme_keywords = {
                "profesyonel": ["kuru", "temizleme", "profesyonel", "uzman", "hizmet"],
                "halı": ["halı", "hali", "yıkama", "kilim", "dokuma"],
                "deri": ["deri", "çanta", "ayakkabı", "süet", "nubuk"],
                "perde": ["perde", "tül", "ev tekstili", "pencere"],
                "gelinlik": ["gelinlik", "düğün", "abiye", "özel gün"],
                "mobilya": ["koltuk", "mobilya", "döşeme", "kumaş"],
                "leke": ["leke", "çıkarma", "temizlik", "yağ"]
            }
            
            theme_scores = {}
            for theme, keywords in theme_keywords.items():
                score = sum(full_text.count(keyword) for keyword in keywords)
                if score > 0:
                    theme_scores[theme] = score
            
            primary_theme = max(theme_scores, key=theme_scores.get) if theme_scores else "profesyonel"
            
            return {
                'slug': slug,
                'title': title_text.strip(),
                'theme': primary_theme,
                'content_length': len(main_content.split())
            }
            
        except Exception as e:
            return None

    def download_and_convert_image(self, url, blog_slug):
        """Görseli indir ve WebP'ye çevir"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # PIL ile aç
            image = Image.open(BytesIO(response.content))
            
            # RGB moduna çevir
            if image.mode in ('RGBA', 'LA', 'P'):
                image = image.convert('RGB')
            
            # 1200x630 boyutuna resize et
            target_size = (1200, 630)
            image = image.resize(target_size, Image.Resampling.LANCZOS)
            
            # Blog dizinine kaydet
            blog_dir = os.path.join(self.blog_root, blog_slug)
            webp_path = os.path.join(blog_dir, 'featured-image.webp')
            image.save(webp_path, 'WebP', quality=85, optimize=True)
            
            file_size = os.path.getsize(webp_path)
            
            return {
                'success': True,
                'file_path': webp_path,
                'file_size_kb': file_size // 1024,
                'dimensions': f"{image.width}x{image.height}"
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def update_blog_html(self, blog_slug):
        """Blog HTML dosyasını güncelle"""
        try:
            blog_dir = os.path.join(self.blog_root, blog_slug)
            html_path = os.path.join(blog_dir, 'index.html')
            
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Featured image ekle
            h1_tag = soup.find('h1')
            if h1_tag:
                new_img = soup.new_tag('img')
                new_img['class'] = 'featured-image'
                new_img['src'] = 'featured-image.webp'
                new_img['alt'] = f"{blog_slug} - Professional Dry Cleaning Service"
                new_img['width'] = '1200'
                new_img['height'] = '630'
                new_img['loading'] = 'lazy'
                new_img['style'] = 'width: 100%; height: auto; margin: 20px 0;'
                
                h1_tag.insert_after(new_img)
            
            # Meta tags güncelle
            head = soup.find('head')
            if head:
                # OG image
                og_image = soup.new_tag('meta')
                og_image['property'] = 'og:image'
                og_image['content'] = f"https://dryallekurutemizleme.com/blog/{blog_slug}/featured-image.webp"
                head.append(og_image)
                
                # Twitter card
                twitter_image = soup.new_tag('meta')
                twitter_image['name'] = 'twitter:image'
                twitter_image['content'] = f"https://dryallekurutemizleme.com/blog/{blog_slug}/featured-image.webp"
                head.append(twitter_image)
            
            # HTML'i kaydet
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return {'success': True}
            
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def get_next_available_image(self):
        """Kullanılmamış görsel URL'i al"""
        available_images = [url for url in self.remaining_image_pool if url not in self.used_urls]
        
        if available_images:
            selected_url = available_images[0]
            self.used_urls.add(selected_url)
            return selected_url
        
        return None

    def complete_remaining_blogs(self):
        """Kalan blogları tamamla"""
        print("🔄 Kalan bloglar için görsel entegrasyonu başlıyor...")
        
        # Görseli olmayan blogları bul
        blogs_without_images = self.find_blogs_without_images()
        print(f"📊 Görseli olmayan blog sayısı: {len(blogs_without_images)}")
        
        results = []
        successful = 0
        failed = 0
        
        for blog in blogs_without_images:
            slug = blog['slug']
            theme = blog['theme']
            
            print(f"📥 İşleniyor: {slug} ({theme})...")
            
            # Görsel URL'i al
            image_url = self.get_next_available_image()
            
            if not image_url:
                print(f"   ❌ Uygun görsel bulunamadı")
                failed += 1
                continue
            
            # Görseli indir
            download_result = self.download_and_convert_image(image_url, slug)
            
            if download_result['success']:
                # HTML'i güncelle
                html_result = self.update_blog_html(slug)
                
                if html_result['success']:
                    successful += 1
                    print(f"   ✅ Başarılı: {download_result['file_size_kb']}KB")
                else:
                    failed += 1
                    print(f"   ❌ HTML güncelleme hatası")
            else:
                failed += 1
                print(f"   ❌ İndirme hatası: {download_result.get('error', 'Unknown')}")
            
            results.append({
                'slug': slug,
                'theme': theme,
                'url': image_url,
                'status': 'SUCCESS' if download_result['success'] else 'FAILED',
                'download_result': download_result
            })
        
        return {
            'total_processed': len(blogs_without_images),
            'successful': successful,
            'failed': failed,
            'results': results
        }

def main():
    """Kalan Bloglar İçin Görsel Entegrasyonu"""
    print("🔄 KALAN BLOGLAR İÇİN GÖRSEL ENTEGRASYONU")
    print("=" * 60)
    print("🎯 Eksik Görseller | WebP Optimizasyon | HTML Entegrasyon")
    print("=" * 60)
    
    completer = RemainingBlogsCompleter()
    
    try:
        # Kalan blogları tamamla
        results = completer.complete_remaining_blogs()
        
        # Özet
        print("\n" + "=" * 60)
        print("🔄 KALAN BLOG ENTEGRASYONİ TAMAMLANDI")
        print("=" * 60)
        
        print(f"✅ Toplam işlenen: {results['total_processed']}")
        print(f"✅ Başarılı: {results['successful']}")
        print(f"❌ Başarısız: {results['failed']}")
        
        if results['total_processed'] > 0:
            success_rate = (results['successful'] / results['total_processed']) * 100
            print(f"✅ Başarı oranı: {success_rate:.1f}%")
        
        if results['successful'] > 0:
            print(f"\n🎉 {results['successful']} blog için görsel entegrasyonu tamamlandı!")
            print(f"   • Tüm görseller WebP formatında optimize edildi")
            print(f"   • HTML ve meta tag'ler güncellendi")
            print(f"   • 1200x630px boyutunda standardize edildi")
        
        return True
        
    except Exception as e:
        print(f"❌ Entegrasyon hatası: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)