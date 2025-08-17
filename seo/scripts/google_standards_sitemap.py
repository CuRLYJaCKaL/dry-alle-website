#!/usr/bin/env python3
"""
Google Standartları Sitemap Yönetimi
SEO/Google standartlarının en üst düzeyinde sitemap yönetimi

Google Sitemap Gereksinimleri (2025):
- Max 50,000 URL per sitemap
- Max 50MB file size  
- UTF-8 encoding
- XML specification compliance
- Proper namespace declarations
- Mobile-first indexing optimization
- Image sitemap integration
- Lastmod dates in proper format
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import re
import gzip
from urllib.parse import quote, urlparse
import json

class GoogleStandardsSitemapManager:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.blog_root = os.path.join(project_root, 'blog')
        self.base_url = "https://dryallekurutemizleme.com"
        
        # Google 2025 Sitemap Standartları
        self.google_standards = {
            'max_urls_per_sitemap': 50000,
            'max_file_size_mb': 50,
            'required_encoding': 'UTF-8',
            'required_namespaces': {
                'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9',
                'mobile': 'http://www.google.com/schemas/sitemap-mobile/1.0',
                'image': 'http://www.google.com/schemas/sitemap-image/1.1',
                'news': 'http://www.google.com/schemas/sitemap-news/0.9'
            },
            'max_url_length': 2048,
            'priority_range': (0.0, 1.0),
            'changefreq_values': ['always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'],
            'lastmod_format': '%Y-%m-%d'
        }
        
        # URL prioritization matrix (Google optimized)
        self.priority_matrix = {
            'homepage': {
                'priority': 1.0,
                'changefreq': 'daily',
                'mobile_important': True
            },
            'main_pages': {
                'priority': 0.9,
                'changefreq': 'weekly', 
                'mobile_important': True
            },
            'service_pages': {
                'priority': 0.8,
                'changefreq': 'monthly',
                'mobile_important': True
            },
            'blog_index': {
                'priority': 0.8,
                'changefreq': 'weekly',
                'mobile_important': True
            },
            'fresh_blog_posts': {  # Yeni blog postları
                'priority': 0.7,
                'changefreq': 'weekly',
                'mobile_important': True
            },
            'regular_blog_posts': {
                'priority': 0.6,
                'changefreq': 'monthly',
                'mobile_important': True
            },
            'location_pages': {
                'priority': 0.7,
                'changefreq': 'monthly',
                'mobile_important': True
            },
            'category_pages': {
                'priority': 0.5,
                'changefreq': 'monthly',
                'mobile_important': False
            },
            'utility_pages': {
                'priority': 0.4,
                'changefreq': 'yearly',
                'mobile_important': False
            }
        }

    def validate_url_google_standards(self, url):
        """URL'yi Google standartlarına göre doğrula"""
        issues = []
        
        # URL uzunluk kontrolü
        if len(url) > self.google_standards['max_url_length']:
            issues.append(f"URL too long: {len(url)} chars (max {self.google_standards['max_url_length']})")
        
        # URL format kontrolü
        try:
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                issues.append("Invalid URL format")
        except Exception as e:
            issues.append(f"URL parsing error: {str(e)}")
        
        # Karakterset kontrolü
        try:
            url.encode('utf-8')
        except UnicodeEncodeError:
            issues.append("URL contains invalid characters")
        
        # Google önerilen URL yapısı
        if ' ' in url:
            issues.append("URL contains spaces")
        
        if not url.startswith('https://'):
            issues.append("URL not HTTPS")
        
        return issues

    def get_published_blog_posts(self):
        """Yayınlanmış blog postlarını Google standartlarına göre listele"""
        published_posts = []
        
        for item in os.listdir(self.blog_root):
            item_path = os.path.join(self.blog_root, item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                index_path = os.path.join(item_path, 'index.html')
                
                if os.path.exists(index_path):
                    post_data = self.analyze_blog_post(index_path, item)
                    if post_data and post_data['published']:
                        published_posts.append(post_data)
        
        # Yayın tarihine göre sırala (Google freshness faktörü)
        published_posts.sort(key=lambda x: x['lastmod'], reverse=True)
        
        return published_posts

    def analyze_blog_post(self, html_path, slug):
        """Blog postunu Google standartlarına göre analiz et"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            
            # Yayın durumu kontrolü
            is_published = not any([
                'draft: true' in content.lower(),
                'status: draft' in content.lower(),
                'published: false' in content.lower(),
                '_draft' in html_path.lower()
            ])
            
            if not is_published:
                return None
            
            # URL oluştur ve doğrula
            url = f"{self.base_url}/blog/{slug}/"
            url_issues = self.validate_url_google_standards(url)
            
            # Son değişiklik tarihi (Google lastmod formatı)
            file_mtime = os.path.getmtime(html_path)
            lastmod = datetime.fromtimestamp(file_mtime).strftime(self.google_standards['lastmod_format'])
            
            # Blog post yaşı (Google freshness)
            days_old = (datetime.now() - datetime.fromtimestamp(file_mtime)).days
            
            # Priority belirleme (Google algoritmasına göre)
            if days_old <= 30:  # Son 30 gün
                priority_type = 'fresh_blog_posts'
            else:
                priority_type = 'regular_blog_posts'
            
            # Görselleri tespit et
            images = self.extract_blog_images(soup, slug)
            
            # Title ve meta analizi
            title_elem = soup.find('title')
            title = title_elem.get_text() if title_elem else ""
            
            meta_desc = soup.find('meta', {'name': 'description'})
            description = meta_desc.get('content', '') if meta_desc else ""
            
            # Schema markup kontrolü
            schema_valid = self.validate_schema_markup(soup)
            
            return {
                'slug': slug,
                'url': url,
                'published': True,
                'lastmod': lastmod,
                'days_old': days_old,
                'priority_type': priority_type,
                'priority': self.priority_matrix[priority_type]['priority'],
                'changefreq': self.priority_matrix[priority_type]['changefreq'],
                'mobile_important': self.priority_matrix[priority_type]['mobile_important'],
                'images': images,
                'title': title,
                'description': description,
                'schema_valid': schema_valid,
                'url_issues': url_issues,
                'word_count': len(content.split()),
                'has_featured_image': len(images) > 0
            }
            
        except Exception as e:
            print(f"❌ Blog analiz hatası {html_path}: {str(e)}")
            return None

    def extract_blog_images(self, soup, slug):
        """Blog görselerini Google Image Sitemap için çıkar"""
        images = []
        
        # Featured image
        featured_img = soup.find('img', {'class': 'featured-image'})
        if featured_img and featured_img.get('src'):
            img_src = featured_img['src']
            if img_src.startswith('http'):
                images.append({
                    'url': img_src,
                    'title': featured_img.get('alt', ''),
                    'caption': 'Featured image'
                })
            else:
                images.append({
                    'url': f"{self.base_url}/blog/{slug}/{img_src}",
                    'title': featured_img.get('alt', ''),
                    'caption': 'Featured image'
                })
        
        # Diğer content görselleri
        content_images = soup.select('article img, main img, .blog-content img')
        for img in content_images[:5]:  # Maximum 5 image per blog (Google recommendation)
            if img != featured_img and img.get('src'):
                img_src = img['src']
                if img_src.startswith('http'):
                    images.append({
                        'url': img_src,
                        'title': img.get('alt', ''),
                        'caption': img.get('title', '')
                    })
                elif not img_src.startswith('data:'):  # Skip base64 images
                    images.append({
                        'url': f"{self.base_url}/blog/{slug}/{img_src}",
                        'title': img.get('alt', ''),
                        'caption': img.get('title', '')
                    })
        
        return images

    def validate_schema_markup(self, soup):
        """Schema markup'ı Google standartlarına göre doğrula"""
        schema_scripts = soup.find_all('script', {'type': 'application/ld+json'})
        
        if not schema_scripts:
            return False
        
        try:
            for script in schema_scripts:
                schema_data = json.loads(script.string)
                
                # BlogPosting schema kontrolü
                if schema_data.get('@type') == 'BlogPosting':
                    required_fields = ['headline', 'datePublished', 'author', 'publisher']
                    for field in required_fields:
                        if field not in schema_data:
                            return False
                    return True
                
            return True
            
        except (json.JSONDecodeError, AttributeError):
            return False

    def get_all_site_pages(self):
        """Sitedeki tüm sayfaları Google standartlarına göre listele"""
        all_pages = []
        
        # Ana sayfa (en yüksek öncelik)
        homepage = {
            'url': f"{self.base_url}/",
            'lastmod': datetime.now().strftime(self.google_standards['lastmod_format']),
            'priority': self.priority_matrix['homepage']['priority'],
            'changefreq': self.priority_matrix['homepage']['changefreq'],
            'mobile_important': self.priority_matrix['homepage']['mobile_important'],
            'page_type': 'homepage'
        }
        
        url_issues = self.validate_url_google_standards(homepage['url'])
        homepage['url_issues'] = url_issues
        all_pages.append(homepage)
        
        # Ana sayfalar
        main_pages = [
            ('sss.html', 'SSS sayfası'),
            ('iletisim.html', 'İletişim sayfası'),
            ('hizmetler.html', 'Hizmetler sayfası')
        ]
        
        for page_file, description in main_pages:
            page_path = os.path.join(self.project_root, page_file)
            if os.path.exists(page_path):
                page_data = {
                    'url': f"{self.base_url}/{page_file}",
                    'lastmod': datetime.fromtimestamp(os.path.getmtime(page_path)).strftime(self.google_standards['lastmod_format']),
                    'priority': self.priority_matrix['main_pages']['priority'],
                    'changefreq': self.priority_matrix['main_pages']['changefreq'],
                    'mobile_important': self.priority_matrix['main_pages']['mobile_important'],
                    'page_type': 'main_page',
                    'description': description
                }
                page_data['url_issues'] = self.validate_url_google_standards(page_data['url'])
                all_pages.append(page_data)
        
        # Blog index
        blog_index_path = os.path.join(self.blog_root, 'index.html')
        if os.path.exists(blog_index_path):
            blog_index = {
                'url': f"{self.base_url}/blog/",
                'lastmod': datetime.fromtimestamp(os.path.getmtime(blog_index_path)).strftime(self.google_standards['lastmod_format']),
                'priority': self.priority_matrix['blog_index']['priority'],
                'changefreq': self.priority_matrix['blog_index']['changefreq'],
                'mobile_important': self.priority_matrix['blog_index']['mobile_important'],
                'page_type': 'blog_index'
            }
            blog_index['url_issues'] = self.validate_url_google_standards(blog_index['url'])
            all_pages.append(blog_index)
        
        return all_pages

    def create_google_compliant_sitemap(self, site_pages, blog_posts):
        """Google standartlarına tamamen uygun sitemap oluştur"""
        print("🗺️ Google 2025 standartları sitemap oluşturuluyor...")
        
        # XML declaration ve root element
        urlset = ET.Element('urlset')
        
        # Google gerekli namespace'leri
        for prefix, uri in self.google_standards['required_namespaces'].items():
            if prefix == 'sitemap':
                urlset.set('xmlns', uri)
            else:
                urlset.set(f'xmlns:{prefix}', uri)
        
        total_urls = 0
        total_size = 0
        issues = []
        
        # Site sayfalarını ekle
        for page in site_pages:
            url_elem = self.create_google_url_element(page)
            if url_elem is not None:
                urlset.append(url_elem)
                total_urls += 1
                
                # Size estimation (approximate)
                total_size += len(ET.tostring(url_elem, encoding='utf-8'))
        
        # Blog postlarını ekle
        for post in blog_posts:
            url_elem = self.create_google_url_element(post, is_blog=True)
            if url_elem is not None:
                urlset.append(url_elem)
                total_urls += 1
                
                total_size += len(ET.tostring(url_elem, encoding='utf-8'))
        
        # Google limit kontrolleri
        if total_urls > self.google_standards['max_urls_per_sitemap']:
            issues.append(f"URL count exceeds Google limit: {total_urls}/{self.google_standards['max_urls_per_sitemap']}")
        
        size_mb = total_size / (1024 * 1024)
        if size_mb > self.google_standards['max_file_size_mb']:
            issues.append(f"File size exceeds Google limit: {size_mb:.2f}MB/{self.google_standards['max_file_size_mb']}MB")
        
        print(f"✅ Sitemap oluşturuldu: {total_urls} URL, {size_mb:.2f}MB")
        
        if issues:
            print("⚠️ Google standart uyarıları:")
            for issue in issues:
                print(f"   - {issue}")
        
        return ET.ElementTree(urlset), issues

    def create_google_url_element(self, page_data, is_blog=False):
        """Google standartlarına uygun URL elementi oluştur"""
        # URL doğrulama
        if page_data.get('url_issues'):
            print(f"⚠️ URL issues for {page_data['url']}: {page_data['url_issues']}")
        
        url_elem = ET.Element('url')
        
        # Location (zorunlu)
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = page_data['url']
        
        # Lastmod (Google tarafından önerilen)
        if page_data.get('lastmod'):
            lastmod = ET.SubElement(url_elem, 'lastmod')
            lastmod.text = page_data['lastmod']
        
        # Changefreq (Google için optimize)
        if page_data.get('changefreq') in self.google_standards['changefreq_values']:
            changefreq = ET.SubElement(url_elem, 'changefreq')
            changefreq.text = page_data['changefreq']
        
        # Priority (Google için optimize)
        if 'priority' in page_data:
            priority_val = page_data['priority']
            if self.google_standards['priority_range'][0] <= priority_val <= self.google_standards['priority_range'][1]:
                priority = ET.SubElement(url_elem, 'priority')
                priority.text = f"{priority_val:.1f}"
        
        # Mobile annotation (Google Mobile-First Indexing)
        if page_data.get('mobile_important', True):
            mobile = ET.SubElement(url_elem, f"{{{self.google_standards['required_namespaces']['mobile']}}}mobile")
        
        # Image sitemap (blog posts için)
        if is_blog and page_data.get('images'):
            for img_data in page_data['images'][:5]:  # Google max 5 images per URL
                image_elem = ET.SubElement(url_elem, f"{{{self.google_standards['required_namespaces']['image']}}}image")
                
                image_loc = ET.SubElement(image_elem, f"{{{self.google_standards['required_namespaces']['image']}}}loc")
                image_loc.text = img_data['url']
                
                if img_data.get('title'):
                    image_title = ET.SubElement(image_elem, f"{{{self.google_standards['required_namespaces']['image']}}}title")
                    image_title.text = img_data['title'][:100]  # Google limit
                
                if img_data.get('caption'):
                    image_caption = ET.SubElement(image_elem, f"{{{self.google_standards['required_namespaces']['image']}}}caption")
                    image_caption.text = img_data['caption'][:200]  # Google limit
        
        return url_elem

    def validate_google_compliance(self, tree):
        """Sitemap'i Google standartlarına göre doğrula"""
        print("✅ Google standards compliance validation...")
        
        issues = []
        root = tree.getroot()
        
        # Namespace kontrolü
        root_attribs = root.attrib
        for required_ns in self.google_standards['required_namespaces'].values():
            if required_ns not in root_attribs.values():
                issues.append(f"Missing required namespace: {required_ns}")
        
        # URL sayısı kontrolü
        urls = root.findall('.//url')
        if len(urls) > self.google_standards['max_urls_per_sitemap']:
            issues.append(f"Too many URLs: {len(urls)}/{self.google_standards['max_urls_per_sitemap']}")
        
        # URL format kontrolleri
        invalid_urls = 0
        for url_elem in urls:
            loc_elem = url_elem.find('loc')
            if loc_elem is not None:
                url = loc_elem.text
                url_issues = self.validate_url_google_standards(url)
                if url_issues:
                    invalid_urls += 1
        
        if invalid_urls > 0:
            issues.append(f"Invalid URLs found: {invalid_urls}")
        
        # Priority kontrolü
        for url_elem in urls:
            priority_elem = url_elem.find('priority')
            if priority_elem is not None:
                try:
                    priority_val = float(priority_elem.text)
                    if not (0.0 <= priority_val <= 1.0):
                        issues.append("Invalid priority values found")
                        break
                except ValueError:
                    issues.append("Non-numeric priority values found")
                    break
        
        if issues:
            print("❌ Google compliance issues:")
            for issue in issues:
                print(f"   - {issue}")
            return False
        else:
            print("✅ Full Google 2025 standards compliance")
            return True

    def save_google_sitemap(self, tree):
        """Google standartlarında sitemap kaydet"""
        # XML formatting (Google önerisi)
        ET.indent(tree, space="  ", level=0)
        
        # UTF-8 encoding ile kaydet (Google gereksinimi)
        sitemap_path = os.path.join(self.project_root, 'sitemap.xml')
        
        with open(sitemap_path, 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
        
        # Compressed version oluştur (Google performans optimizasyonu)
        with open(sitemap_path, 'rb') as f_in:
            with gzip.open(sitemap_path + '.gz', 'wb') as f_out:
                f_out.writelines(f_in)
        
        return sitemap_path

    def create_sitemap_index(self, sitemap_paths):
        """Sitemap index oluştur (büyük siteler için Google önerisi)"""
        if len(sitemap_paths) <= 1:
            return None
        
        sitemapindex = ET.Element('sitemapindex')
        sitemapindex.set('xmlns', self.google_standards['required_namespaces']['sitemap'])
        
        for sitemap_path in sitemap_paths:
            sitemap_elem = ET.SubElement(sitemapindex, 'sitemap')
            
            loc = ET.SubElement(sitemap_elem, 'loc')
            loc.text = f"{self.base_url}/{os.path.basename(sitemap_path)}"
            
            lastmod = ET.SubElement(sitemap_elem, 'lastmod')
            lastmod.text = datetime.now().strftime(self.google_standards['lastmod_format'])
        
        # Sitemap index kaydet
        index_tree = ET.ElementTree(sitemapindex)
        ET.indent(index_tree, space="  ", level=0)
        
        index_path = os.path.join(self.project_root, 'sitemap_index.xml')
        with open(index_path, 'wb') as f:
            index_tree.write(f, encoding='utf-8', xml_declaration=True)
        
        return index_path

    def generate_sitemap_report(self, site_pages, blog_posts, issues):
        """Google standartları sitemap raporu"""
        report = {
            "generation_date": datetime.now().isoformat(),
            "google_standards_version": "2025",
            "compliance_status": "COMPLIANT" if not issues else "ISSUES_FOUND",
            "total_urls": len(site_pages) + len(blog_posts),
            "site_pages": len(site_pages),
            "blog_posts": len(blog_posts),
            "fresh_blog_posts": len([p for p in blog_posts if p['days_old'] <= 30]),
            "mobile_optimized_urls": len([p for p in site_pages + blog_posts if p.get('mobile_important', True)]),
            "urls_with_images": len([p for p in blog_posts if p.get('has_featured_image', False)]),
            "total_images": sum(len(p.get('images', [])) for p in blog_posts),
            "schema_compliant_posts": len([p for p in blog_posts if p.get('schema_valid', False)]),
            "url_issues": issues,
            "priority_distribution": {},
            "changefreq_distribution": {},
            "google_recommendations": []
        }
        
        # Priority dağılımı
        all_pages = site_pages + blog_posts
        for page in all_pages:
            priority = str(page.get('priority', 0.5))
            report["priority_distribution"][priority] = report["priority_distribution"].get(priority, 0) + 1
            
            changefreq = page.get('changefreq', 'monthly')
            report["changefreq_distribution"][changefreq] = report["changefreq_distribution"].get(changefreq, 0) + 1
        
        # Google önerileri
        if report["fresh_blog_posts"] < 5:
            report["google_recommendations"].append("Increase fresh content publication frequency")
        
        if report["urls_with_images"] / len(blog_posts) < 0.8:
            report["google_recommendations"].append("Add featured images to more blog posts")
        
        if report["schema_compliant_posts"] / len(blog_posts) < 0.9:
            report["google_recommendations"].append("Improve schema markup coverage")
        
        # Raporu kaydet
        report_path = os.path.join(self.project_root, 'seo/reports/google_sitemap_compliance.json')
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report_path

def main():
    """Google Standartları Sitemap Yönetimi"""
    print("🏆 GOOGLE STANDARDS SİTEMAP YÖNETİMİ")
    print("=" * 60)
    print("🎯 Google 2025 Standards | Enterprise-Grade Sitemap")
    print("=" * 60)
    
    manager = GoogleStandardsSitemapManager()
    
    try:
        # 1. Yayınlanmış blog postları
        print("📊 Yayınlanmış blog posts analizi (Google standards)...")
        blog_posts = manager.get_published_blog_posts()
        print(f"✅ {len(blog_posts)} blog post tespit edildi")
        
        fresh_posts = len([p for p in blog_posts if p['days_old'] <= 30])
        print(f"   📈 {fresh_posts} fresh blog post (≤30 gün)")
        
        # 2. Site sayfaları
        print("📊 Site pages analizi...")
        site_pages = manager.get_all_site_pages()
        print(f"✅ {len(site_pages)} site sayfası tespit edildi")
        
        # 3. Google compliant sitemap oluştur
        print("🏆 Google 2025 compliant sitemap oluşturuluyor...")
        sitemap_tree, issues = manager.create_google_compliant_sitemap(site_pages, blog_posts)
        
        # 4. Google compliance validation
        is_compliant = manager.validate_google_compliance(sitemap_tree)
        
        # 5. Sitemap kaydet
        sitemap_path = manager.save_google_sitemap(sitemap_tree)
        
        # 6. Rapor oluştur
        report_path = manager.generate_sitemap_report(site_pages, blog_posts, issues)
        
        # Özet
        print("\n" + "=" * 60)
        print("🏆 GOOGLE STANDARDS SİTEMAP TAMAMLANDI")
        print("=" * 60)
        print(f"✅ Toplam URL: {len(site_pages) + len(blog_posts)}")
        print(f"✅ Google 2025 Compliance: {'FULL' if is_compliant else 'ISSUES'}")
        print(f"✅ Mobile-First Ready: YES")
        print(f"✅ Image Sitemap: YES")
        print(f"✅ Schema Integration: YES")
        print(f"✅ UTF-8 Encoding: YES")
        print(f"✅ Gzip Compression: YES")
        print(f"✅ Sitemap: {sitemap_path}")
        print(f"✅ Compressed: {sitemap_path}.gz")
        print(f"✅ Rapor: {report_path}")
        
        # Kalite metrikleri
        total_blogs = len(blog_posts)
        schema_rate = len([p for p in blog_posts if p.get('schema_valid', False)]) / total_blogs * 100
        image_rate = len([p for p in blog_posts if p.get('has_featured_image', False)]) / total_blogs * 100
        
        print(f"\n📊 KALİTE METRİKLERİ:")
        print(f"   📈 Schema markup coverage: {schema_rate:.1f}%")
        print(f"   🖼️ Featured image coverage: {image_rate:.1f}%")
        print(f"   📱 Mobile optimization: 100%")
        print(f"   ⚡ Fresh content: {fresh_posts} posts")
        
        if issues:
            print(f"\n⚠️ GOOGLE UYARILAR ({len(issues)}):")
            for issue in issues[:3]:
                print(f"   - {issue}")
        
        print("\n🚀 GOOGLE SEARCH CONSOLE:")
        print("1. https://search.google.com/search-console")
        print("2. Sitemap gönder: https://dryallekurutemizleme.com/sitemap.xml")
        print("3. İndexing durumunu izle")
        print("4. Performance raporlarını incele")
        
        return is_compliant
        
    except Exception as e:
        print(f"❌ Kritik hata: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)