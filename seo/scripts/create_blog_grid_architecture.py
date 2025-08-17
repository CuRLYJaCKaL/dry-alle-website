#!/usr/bin/env python3
"""
Blog Grid Mimarisi Oluşturma Sistemi (C2)
3 sütunlu responsive grid, filtreleme ve arama sistemi

Özellikler:
- 3 sütunlu grid (responsive: mobil 1, tablet 2, desktop 3)
- Tema filtreleme (perde, mobilya, halı, leke, gelinlik, kuru-temizleme)
- Arama fonksiyonu (başlık/içerik)
- Lazy loading görsel optimizasyonu
- Sayfalandırma sistemi
"""

import os
import json
from datetime import datetime
from bs4 import BeautifulSoup
import re

class BlogGridArchitect:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.blog_root = os.path.join(project_root, 'blog')
        
        # Tema kategorileri
        self.theme_categories = {
            'perde': {
                'name': 'Perde Temizliği',
                'color': '#006a44',
                'icon': '🪟',
                'keywords': ['perde', 'tül', 'store', 'dantel']
            },
            'mobilya': {
                'name': 'Mobilya & Koltuk',
                'color': '#004d32', 
                'icon': '🛋️',
                'keywords': ['koltuk', 'kanepe', 'mobilya', 'deri']
            },
            'hali': {
                'name': 'Halı Yıkama',
                'color': '#00623b',
                'icon': '🧽',
                'keywords': ['halı', 'kilim', 'carpet']
            },
            'kuru-temizleme': {
                'name': 'Kuru Temizleme',
                'color': '#006a44',
                'icon': '👔',
                'keywords': ['kuru', 'temizleme', 'dry', 'cleaning']
            },
            'gelinlik': {
                'name': 'Özel Giyim',
                'color': '#f6ec3d',
                'icon': '👗',
                'keywords': ['gelinlik', 'düğün', 'özel']
            },
            'leke': {
                'name': 'Leke Çıkarma',
                'color': '#004d32',
                'icon': '🧼',
                'keywords': ['leke', 'çıkar', 'stain']
            }
        }

    def analyze_all_blogs(self):
        """Tüm blogları analiz et ve metadata oluştur"""
        blogs_data = []
        
        for item in os.listdir(self.blog_root):
            item_path = os.path.join(self.blog_root, item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                index_path = os.path.join(item_path, 'index.html')
                
                if os.path.exists(index_path):
                    blog_data = self.extract_blog_metadata(index_path, item)
                    if blog_data:
                        blogs_data.append(blog_data)
        
        # Yayın tarihine göre sırala (en yeni en üstte)
        blogs_data.sort(key=lambda x: x['publish_date'], reverse=True)
        
        return blogs_data

    def extract_blog_metadata(self, html_path, slug):
        """Blog metadatalarını çıkar"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Başlık
            title_elem = soup.find('title')
            title = title_elem.get_text() if title_elem else slug.replace('-', ' ').title()
            
            # H1 başlığı (daha temiz olabilir)
            h1_elem = soup.find('h1')
            h1_title = h1_elem.get_text() if h1_elem else title
            
            # Meta açıklama
            meta_desc = soup.find('meta', {'name': 'description'})
            description = meta_desc.get('content', '') if meta_desc else ""
            
            # İçerik analizi
            content_elements = soup.select('main p, article p, .article-body p')
            content_text = ' '.join([elem.get_text() for elem in content_elements])
            
            # Okuma süresi hesaplama (ortalama 200 kelime/dakika)
            word_count = len(content_text.split())
            reading_time = max(1, round(word_count / 200))
            
            # Tema belirleme
            theme = self.determine_theme(title + ' ' + content_text)
            
            # Yayın tarihi (schema'dan veya dosya tarihinden)
            publish_date = self.extract_publish_date(soup, html_path)
            
            # Featured image
            featured_img = soup.find('img', {'class': 'featured-image'})
            if not featured_img:
                featured_img = soup.find('img')
            
            image_url = f"/blog/{slug}/featured-image.webp"
            if featured_img and featured_img.get('src'):
                if featured_img['src'].startswith('http'):
                    image_url = featured_img['src']
                else:
                    image_url = f"/blog/{slug}/{featured_img['src']}"
            
            # Blog kartı için özet oluştur (120 karakter max)
            summary = self.create_summary(description, content_text)
            
            return {
                'slug': slug,
                'title': self.truncate_title(h1_title),  # 70 karakter max
                'summary': summary,  # 120 karakter max
                'theme': theme,
                'reading_time': reading_time,
                'publish_date': publish_date,
                'image_url': image_url,
                'word_count': word_count
            }
            
        except Exception as e:
            print(f"❌ Blog analiz hatası {html_path}: {str(e)}")
            return None

    def determine_theme(self, text):
        """İçeriğe göre tema belirle"""
        text_lower = text.lower()
        theme_scores = {}
        
        for theme, data in self.theme_categories.items():
            score = sum(text_lower.count(keyword) for keyword in data['keywords'])
            theme_scores[theme] = score
        
        # En yüksek puanlı tema
        if theme_scores:
            return max(theme_scores.items(), key=lambda x: x[1])[0]
        
        return 'kuru-temizleme'  # varsayılan

    def extract_publish_date(self, soup, html_path):
        """Yayın tarihini çıkar"""
        # Schema markup'tan dene
        schema_script = soup.find('script', {'type': 'application/ld+json'})
        if schema_script:
            try:
                import json
                schema_data = json.loads(schema_script.string)
                if 'datePublished' in schema_data:
                    return schema_data['datePublished']
            except:
                pass
        
        # Dosya değişiklik tarihini kullan
        try:
            import os
            from datetime import datetime
            timestamp = os.path.getmtime(html_path)
            return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        except:
            return datetime.now().strftime('%Y-%m-%d')

    def truncate_title(self, title, max_length=70):
        """Başlığı 70 karaktere kısalt"""
        if len(title) <= max_length:
            return title
        
        # Kelime sınırında kes
        truncated = title[:max_length].rsplit(' ', 1)[0]
        return truncated + '...'

    def create_summary(self, description, content, max_length=120):
        """Blog kartı için özet oluştur"""
        # Önce meta description'ı dene
        if description and len(description.strip()) > 20:
            summary = description.strip()
        else:
            # İçerikten ilk cümleleri al
            sentences = content.split('. ')
            summary = '. '.join(sentences[:2]) + '.'
        
        # 120 karaktere kısalt
        if len(summary) <= max_length:
            return summary
        
        # Kelime sınırında kes
        truncated = summary[:max_length].rsplit(' ', 1)[0]
        return truncated + '...'

    def create_blog_index_html(self, blogs_data):
        """Ana blog index sayfasını oluştur"""
        
        html_content = f'''<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog | Dry Alle Kuru Temizleme - Profesyonel Tekstil Bakım Rehberleri</title>
    <meta name="description" content="İstanbul'da kuru temizleme, halı yıkama, mobilya temizliği hakkında uzman rehberleri. 25 yıllık deneyimle hazırlanmış kapsamlı blog yazıları.">
    <meta name="keywords" content="kuru temizleme blog, halı yıkama rehberi, mobilya temizliği, perde temizleme, leke çıkarma">
    
    <!-- Open Graph -->
    <meta property="og:title" content="Profesyonel Temizlik Blog | Dry Alle">
    <meta property="og:description" content="Kuru temizleme, halı yıkama ve tekstil bakımı hakkında uzman rehberleri">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://dryallekurutemizleme.com/blog/">
    <meta property="og:image" content="https://dryallekurutemizleme.com/blog/blog-featured.webp">
    
    <!-- CSS -->
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../blog-corporate.css">
    
    <!-- Blog Index Styles -->
    <style>
        /* Blog Grid Sistemleri */
        .blog-hero {{
            background: linear-gradient(135deg, #006a44 0%, #004d32 50%, #00623b 100%);
            color: white;
            padding: 80px 0;
            text-align: center;
        }}
        
        .blog-controls {{
            background: #f8f9fa;
            padding: 40px 0;
            border-bottom: 1px solid #eee;
        }}
        
        .controls-container {{
            max-width: 1600px;
            margin: 0 auto;
            padding: 0 60px;
            display: flex;
            gap: 30px;
            align-items: center;
            flex-wrap: wrap;
        }}
        
        .search-box {{
            flex: 1;
            min-width: 300px;
        }}
        
        .search-input {{
            width: 100%;
            padding: 12px 20px;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
            transition: border-color 0.3s;
        }}
        
        .search-input:focus {{
            outline: none;
            border-color: #006a44;
        }}
        
        .filter-controls {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}
        
        .filter-btn {{
            padding: 8px 16px;
            border: 2px solid #006a44;
            background: white;
            color: #006a44;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s;
            white-space: nowrap;
        }}
        
        .filter-btn:hover,
        .filter-btn.active {{
            background: #006a44;
            color: white;
        }}
        
        .reading-time-filter {{
            display: flex;
            gap: 10px;
        }}
        
        .blog-grid {{
            max-width: 1600px;
            margin: 0 auto;
            padding: 60px 60px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
        }}
        
        .blog-card {{
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
        }}
        
        .blog-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        }}
        
        .blog-card-image {{
            width: 100%;
            height: 220px;
            object-fit: cover;
            border-bottom: 3px solid #f6ec3d;
        }}
        
        .blog-card-content {{
            padding: 25px;
        }}
        
        .blog-theme-badge {{
            position: absolute;
            top: 15px;
            left: 15px;
            padding: 5px 12px;
            background: rgba(0,0,0,0.8);
            color: white;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
        }}
        
        .blog-card-title {{
            color: #006a44;
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 12px;
            line-height: 1.4;
            text-decoration: none;
            display: block;
        }}
        
        .blog-card-title:hover {{
            color: #22c55e;
        }}
        
        .blog-card-summary {{
            color: #666;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 15px;
        }}
        
        .blog-card-meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
            color: #999;
            margin-bottom: 15px;
        }}
        
        .read-more-btn {{
            color: #006a44;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 2px solid transparent;
            transition: border-color 0.3s ease;
        }}
        
        .read-more-btn:hover {{
            border-color: #006a44;
        }}
        
        .pagination {{
            text-align: center;
            padding: 40px 0;
        }}
        
        .pagination-btn {{
            display: inline-block;
            padding: 10px 20px;
            margin: 0 5px;
            background: #006a44;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s;
        }}
        
        .pagination-btn:hover {{
            background: #22c55e;
        }}
        
        .pagination-btn.disabled {{
            background: #ccc;
            pointer-events: none;
        }}
        
        .no-results {{
            text-align: center;
            padding: 60px 20px;
            color: #666;
        }}
        
        /* Responsive Design */
        @media (max-width: 768px) {{
            .blog-grid {{
                grid-template-columns: 1fr;
                padding: 40px 20px;
                gap: 30px;
            }}
            
            .controls-container {{
                padding: 0 20px;
                flex-direction: column;
                align-items: stretch;
            }}
            
            .filter-controls {{
                justify-content: center;
            }}
            
            .blog-hero {{
                padding: 60px 20px;
            }}
        }}
        
        @media (max-width: 480px) {{
            .blog-card {{
                margin: 0 10px;
            }}
            
            .filter-btn {{
                font-size: 12px;
                padding: 6px 12px;
            }}
        }}
    </style>
    
    <!-- Schema Markup -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "Dry Alle Kuru Temizleme Blog",
        "description": "Kuru temizleme, halı yıkama ve tekstil bakımı hakkında uzman rehberleri",
        "url": "https://dryallekurutemizleme.com/blog/",
        "publisher": {{
            "@type": "Organization",
            "name": "Dry Alle Kuru Temizleme",
            "url": "https://dryallekurutemizleme.com"
        }},
        "blogPost": [
            {json.dumps([{"@type": "BlogPosting", "headline": blog["title"], "url": f"https://dryallekurutemizleme.com/blog/{blog['slug']}/"} for blog in blogs_data[:10]], ensure_ascii=False)}
        ]
    }}
    </script>
</head>
<body>
    <!-- Corporate Header -->
    <div class="top-bar">
        <div class="top-bar-content">
            <strong>ÜCRETSİZ KAPIDAN TESLİMAT</strong> • İstanbul'un Her Yerine • 0530 468 5858
        </div>
    </div>
    
    <header class="header">
        <div class="header-container">
            <div class="logo">
                <svg width="120" height="40" viewBox="0 0 120 40" fill="none">
                    <text x="10" y="25" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="white">DRY ALLE</text>
                </svg>
            </div>
            <nav>
                <ul class="nav-menu">
                    <li><a href="../index.html">ANASAYFA</a></li>
                    <li><a href="../hizmetler.html">HİZMETLER</a></li>
                    <li><a href="index.html" class="active">BLOG</a></li>
                    <li><a href="../sss.html">SSS</a></li>
                    <li><a href="../iletisim.html">İLETİŞİM</a></li>
                </ul>
            </nav>
        </div>
    </header>
    
    <!-- Blog Hero -->
    <section class="blog-hero">
        <div class="container">
            <h1>Tekstil Bakım Rehberleri</h1>
            <p>25 yıllık deneyimimizle hazırladığımız kapsamlı rehberler</p>
        </div>
    </section>
    
    <!-- Blog Controls -->
    <section class="blog-controls">
        <div class="controls-container">
            <div class="search-box">
                <input type="text" class="search-input" placeholder="Blog yazılarında ara..." id="searchInput">
            </div>
            
            <div class="filter-controls">
                <button class="filter-btn active" data-theme="all">Tümü</button>
                {self.generate_theme_filter_buttons()}
            </div>
            
            <div class="reading-time-filter">
                <button class="filter-btn" data-time="quick">Hızlı (≤5dk)</button>
                <button class="filter-btn" data-time="medium">Orta (6-10dk)</button>
                <button class="filter-btn" data-time="long">Detaylı (>10dk)</button>
            </div>
        </div>
    </section>
    
    <!-- Blog Grid -->
    <section class="blog-grid-container">
        <div class="blog-grid" id="blogGrid">
            {self.generate_blog_cards(blogs_data)}
        </div>
        
        <div class="no-results" id="noResults" style="display: none;">
            <h3>Aradığınız içerik bulunamadı</h3>
            <p>Farklı anahtar kelimeler deneyebilir veya filtrelerinizi değiştirebilirsiniz.</p>
            <div style="margin-top: 20px;">
                <strong>Önerilen konular:</strong><br>
                <a href="#" onclick="filterByTheme('kuru-temizleme')">Kuru Temizleme</a> • 
                <a href="#" onclick="filterByTheme('hali')">Halı Yıkama</a> • 
                <a href="#" onclick="filterByTheme('mobilya')">Mobilya Temizliği</a>
            </div>
        </div>
        
        <div class="pagination" id="pagination">
            <!-- Pagination will be generated by JavaScript -->
        </div>
    </section>
    
    <!-- JavaScript -->
    <script>
        // Blog verisi
        const blogsData = {json.dumps(blogs_data, ensure_ascii=False)};
        const itemsPerPage = 12;
        let currentPage = 1;
        let filteredBlogs = [...blogsData];
        
        // DOM elementleri
        const searchInput = document.getElementById('searchInput');
        const blogGrid = document.getElementById('blogGrid');
        const noResults = document.getElementById('noResults');
        const pagination = document.getElementById('pagination');
        
        // Tema filtreleme
        function filterByTheme(theme) {{
            // Tüm filter butonlarından active sınıfını kaldır
            document.querySelectorAll('.filter-btn[data-theme]').forEach(btn => {{
                btn.classList.remove('active');
            }});
            
            // Seçilen butona active sınıfı ekle
            const activeBtn = document.querySelector(`[data-theme="${{theme}}"]`);
            if (activeBtn) activeBtn.classList.add('active');
            
            // Filtreleme
            if (theme === 'all') {{
                filteredBlogs = [...blogsData];
            }} else {{
                filteredBlogs = blogsData.filter(blog => blog.theme === theme);
            }}
            
            currentPage = 1;
            displayBlogs();
        }}
        
        // Okuma süresi filtreleme
        function filterByReadingTime(timeRange) {{
            // Reading time butonlarını güncelle
            document.querySelectorAll('.filter-btn[data-time]').forEach(btn => {{
                btn.classList.remove('active');
            }});
            
            const activeBtn = document.querySelector(`[data-time="${{timeRange}}"]`);
            if (activeBtn) activeBtn.classList.add('active');
            
            // Filtreleme
            switch(timeRange) {{
                case 'quick':
                    filteredBlogs = blogsData.filter(blog => blog.reading_time <= 5);
                    break;
                case 'medium':
                    filteredBlogs = blogsData.filter(blog => blog.reading_time >= 6 && blog.reading_time <= 10);
                    break;
                case 'long':
                    filteredBlogs = blogsData.filter(blog => blog.reading_time > 10);
                    break;
                default:
                    filteredBlogs = [...blogsData];
            }}
            
            currentPage = 1;
            displayBlogs();
        }}
        
        // Arama fonksiyonu
        function searchBlogs() {{
            const query = searchInput.value.toLowerCase().trim();
            
            if (query === '') {{
                filteredBlogs = [...blogsData];
            }} else {{
                filteredBlogs = blogsData.filter(blog => 
                    blog.title.toLowerCase().includes(query) ||
                    blog.summary.toLowerCase().includes(query)
                );
            }}
            
            currentPage = 1;
            displayBlogs();
        }}
        
        // Blog kartlarını görüntüle
        function displayBlogs() {{
            const startIndex = (currentPage - 1) * itemsPerPage;
            const endIndex = startIndex + itemsPerPage;
            const currentBlogs = filteredBlogs.slice(startIndex, endIndex);
            
            if (currentBlogs.length === 0) {{
                blogGrid.style.display = 'none';
                noResults.style.display = 'block';
                pagination.innerHTML = '';
                return;
            }}
            
            blogGrid.style.display = 'grid';
            noResults.style.display = 'none';
            
            // Blog kartlarını oluştur
            blogGrid.innerHTML = currentBlogs.map(blog => createBlogCard(blog)).join('');
            
            // Sayfalandırma oluştur
            createPagination();
        }}
        
        // Blog kartı oluştur
        function createBlogCard(blog) {{
            const themeData = {json.dumps(self.theme_categories, ensure_ascii=False)};
            const theme = themeData[blog.theme] || themeData['kuru-temizleme'];
            
            return `
                <article class="blog-card">
                    <div class="blog-theme-badge" style="background: ${{theme.color}}">
                        ${{theme.icon}} ${{theme.name}}
                    </div>
                    <img src="${{blog.image_url}}" alt="${{blog.title}}" class="blog-card-image" loading="lazy">
                    <div class="blog-card-content">
                        <a href="${{blog.slug}}/" class="blog-card-title">${{blog.title}}</a>
                        <p class="blog-card-summary">${{blog.summary}}</p>
                        <div class="blog-card-meta">
                            <span>📅 ${{formatDate(blog.publish_date)}}</span>
                            <span>⏱️ ${{blog.reading_time}} dk okuma</span>
                        </div>
                        <a href="${{blog.slug}}/" class="read-more-btn">Devamını Oku</a>
                    </div>
                </article>
            `;
        }}
        
        // Tarih formatlama
        function formatDate(dateString) {{
            const date = new Date(dateString);
            const options = {{ year: 'numeric', month: 'long', day: 'numeric' }};
            return date.toLocaleDateString('tr-TR', options);
        }}
        
        // Sayfalandırma oluştur
        function createPagination() {{
            const totalPages = Math.ceil(filteredBlogs.length / itemsPerPage);
            
            if (totalPages <= 1) {{
                pagination.innerHTML = '';
                return;
            }}
            
            let paginationHTML = '';
            
            // Önceki sayfa
            if (currentPage > 1) {{
                paginationHTML += `<a href="#" class="pagination-btn" onclick="changePage(${{currentPage - 1}})">← Önceki</a>`;
            }}
            
            // Sayfa numaraları
            for (let i = 1; i <= totalPages; i++) {{
                if (i === currentPage) {{
                    paginationHTML += `<span class="pagination-btn active">${{i}}</span>`;
                }} else {{
                    paginationHTML += `<a href="#" class="pagination-btn" onclick="changePage(${{i}})">${{i}}</a>`;
                }}
            }}
            
            // Sonraki sayfa
            if (currentPage < totalPages) {{
                paginationHTML += `<a href="#" class="pagination-btn" onclick="changePage(${{currentPage + 1}})">Sonraki →</a>`;
            }}
            
            pagination.innerHTML = paginationHTML;
        }}
        
        // Sayfa değiştir
        function changePage(page) {{
            currentPage = page;
            displayBlogs();
            // Sayfanın üstüne scroll
            document.querySelector('.blog-controls').scrollIntoView({{ behavior: 'smooth' }});
        }}
        
        // Event listener'lar
        searchInput.addEventListener('input', searchBlogs);
        
        // Tema filtre butonları
        document.querySelectorAll('.filter-btn[data-theme]').forEach(btn => {{
            btn.addEventListener('click', () => filterByTheme(btn.dataset.theme));
        }});
        
        // Okuma süresi filtre butonları
        document.querySelectorAll('.filter-btn[data-time]').forEach(btn => {{
            btn.addEventListener('click', () => filterByReadingTime(btn.dataset.time));
        }});
        
        // Sayfa yüklendiğinde
        document.addEventListener('DOMContentLoaded', () => {{
            displayBlogs();
        }});
    </script>
</body>
</html>'''
        
        return html_content

    def generate_theme_filter_buttons(self):
        """Tema filtre butonlarını oluştur"""
        buttons = []
        for theme_key, theme_data in self.theme_categories.items():
            buttons.append(f'<button class="filter-btn" data-theme="{theme_key}">{theme_data["icon"]} {theme_data["name"]}</button>')
        
        return '\n                '.join(buttons)

    def generate_blog_cards(self, blogs_data):
        """Blog kartlarını oluştur (JavaScript ile güncellenecek)"""
        return '''
            <!-- Blog kartları JavaScript ile dinamik olarak oluşturulacak -->
            <div class="loading-spinner" style="grid-column: 1 / -1; text-align: center; padding: 40px;">
                <p>Blog yazıları yükleniyor...</p>
            </div>
        '''

    def save_blog_metadata(self, blogs_data):
        """Blog metadata'sını JSON olarak kaydet"""
        metadata_path = os.path.join(self.project_root, 'blog/blogs-metadata.json')
        
        metadata = {
            "generated_date": datetime.now().isoformat(),
            "total_blogs": len(blogs_data),
            "themes": self.theme_categories,
            "blogs": blogs_data
        }
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        
        return metadata_path

def main():
    """Blog Grid Mimarisini Oluştur"""
    print("🏗️ BLOG GRID MİMARİSİ SİSTEMİ")
    print("=" * 50)
    print("🎯 C2: 3 Sütunlu Grid + Filtreleme + Arama")
    print("=" * 50)
    
    architect = BlogGridArchitect()
    
    try:
        # 1. Tüm blogları analiz et
        print("📊 Blog analizi başlıyor...")
        blogs_data = architect.analyze_all_blogs()
        
        print(f"✅ {len(blogs_data)} blog analiz edildi")
        
        # 2. Tema dağılımını göster
        theme_counts = {}
        for blog in blogs_data:
            theme = blog['theme']
            theme_counts[theme] = theme_counts.get(theme, 0) + 1
        
        print("\n📊 Tema Dağılımı:")
        for theme, count in theme_counts.items():
            theme_name = architect.theme_categories[theme]['name']
            print(f"   {architect.theme_categories[theme]['icon']} {theme_name}: {count} blog")
        
        # 3. Blog index sayfasını oluştur
        print("\n🏗️ Blog index sayfası oluşturuluyor...")
        html_content = architect.create_blog_index_html(blogs_data)
        
        # Blog index dosyasını kaydet
        index_path = os.path.join(architect.blog_root, 'index.html')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # 4. Metadata kaydet
        metadata_path = architect.save_blog_metadata(blogs_data)
        
        # Özet
        print("\n" + "=" * 50)
        print("📊 BLOG GRID MİMARİSİ TAMAMLANDI")
        print("=" * 50)
        print(f"✅ Ana index sayfası: {index_path}")
        print(f"✅ Metadata dosyası: {metadata_path}")
        print(f"✅ Toplam blog: {len(blogs_data)}")
        print(f"✅ Tema kategorisi: {len(architect.theme_categories)}")
        
        print("\n🚀 ÖZELLİKLER:")
        print("✅ 3 sütunlu responsive grid (desktop)")
        print("✅ 2 sütunlu grid (tablet)")
        print("✅ 1 sütunlu grid (mobil)")
        print("✅ Tema filtreleme sistemi")
        print("✅ Okuma süresi filtreleme")
        print("✅ Arama fonksiyonu")
        print("✅ Lazy loading görseller")
        print("✅ Sayfalandırma (12 blog/sayfa)")
        print("✅ SEO optimizasyonu")
        
        return True
        
    except Exception as e:
        print(f"❌ Kritik hata: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)