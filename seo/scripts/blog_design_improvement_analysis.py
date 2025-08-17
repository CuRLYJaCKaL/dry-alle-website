#!/usr/bin/env python3
"""
Blog Tasarım İyileştirme Analizi
Blog sayfalarının profesyonel görünüm ve kullanıcı deneyimi analizi
"""

import os
import json
from datetime import datetime
from bs4 import BeautifulSoup

class BlogDesignAnalyzer:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.blog_root = os.path.join(project_root, 'blog')
        
        # Tasarım kalitesi kriterleri
        self.design_criteria = {
            'visual_hierarchy': {
                'proper_heading_structure': True,
                'consistent_typography': True,
                'clear_content_sections': True,
                'proper_spacing': True
            },
            'professional_appearance': {
                'modern_layout': True,
                'brand_consistency': True,
                'clean_design': True,
                'high_quality_images': True
            },
            'user_experience': {
                'easy_navigation': True,
                'fast_loading': True,
                'mobile_responsive': True,
                'accessible_design': True
            },
            'content_presentation': {
                'readable_fonts': True,
                'proper_contrast': True,
                'organized_layout': True,
                'engaging_visuals': True
            }
        }

    def analyze_blog_index_design(self):
        """Blog ana sayfa tasarım analizi"""
        index_path = os.path.join(self.blog_root, 'index.html')
        
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        analysis = {
            'page_type': 'Blog Index',
            'design_issues': [],
            'css_problems': [],
            'layout_issues': [],
            'improvement_suggestions': []
        }
        
        # CSS dosyaları analizi
        css_links = soup.find_all('link', rel='stylesheet')
        css_files = [link.get('href') for link in css_links]
        
        if len(css_files) > 3:
            analysis['css_problems'].append({
                'issue': 'Too many CSS files',
                'count': len(css_files),
                'files': css_files,
                'recommendation': 'Consolidate CSS files for better performance'
            })
        
        # Inline styles analizi
        style_tags = soup.find_all('style')
        if len(style_tags) > 2:
            analysis['css_problems'].append({
                'issue': 'Excessive inline styles',
                'count': len(style_tags),
                'recommendation': 'Move inline styles to external CSS files'
            })
        
        # Layout structure analizi
        main_sections = soup.find_all(['section', 'main', 'article'])
        if len(main_sections) < 3:
            analysis['layout_issues'].append({
                'issue': 'Insufficient content structure',
                'sections_found': len(main_sections),
                'recommendation': 'Add more semantic HTML sections for better organization'
            })
        
        # Grid system analizi
        blog_grid = soup.find(class_='blog-grid')
        if blog_grid:
            grid_styles = str(blog_grid.get('style', ''))
            if 'grid-template-columns' not in grid_styles:
                analysis['layout_issues'].append({
                    'issue': 'Grid system not properly defined',
                    'recommendation': 'Implement responsive CSS Grid with proper breakpoints'
                })
        
        # Design recommendations
        analysis['improvement_suggestions'] = [
            'Implement modern card-based design with proper shadows and hover effects',
            'Add proper spacing and typography hierarchy',
            'Improve color scheme consistency with brand guidelines',
            'Enhance mobile responsiveness with better breakpoints',
            'Add loading states and micro-interactions',
            'Implement proper image optimization and lazy loading'
        ]
        
        return analysis

    def analyze_blog_post_design(self, blog_slug):
        """Blog yazı sayfası tasarım analizi"""
        blog_path = os.path.join(self.blog_root, blog_slug, 'index.html')
        
        if not os.path.exists(blog_path):
            return None
        
        with open(blog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        analysis = {
            'page_type': 'Blog Post',
            'slug': blog_slug,
            'design_issues': [],
            'content_issues': [],
            'navigation_issues': [],
            'improvement_suggestions': []
        }
        
        # Article structure analizi
        article = soup.find('article')
        if not article:
            analysis['content_issues'].append({
                'issue': 'Missing semantic article element',
                'recommendation': 'Wrap main content in <article> tag'
            })
        
        # Heading hierarchy kontrolü
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        h1_count = len(soup.find_all('h1'))
        
        if h1_count != 1:
            analysis['content_issues'].append({
                'issue': f'Incorrect H1 count: {h1_count}',
                'recommendation': 'Use exactly one H1 per page'
            })
        
        # Featured image analizi
        featured_img = soup.find('img', class_='featured-image')
        if featured_img:
            if not featured_img.get('alt'):
                analysis['content_issues'].append({
                    'issue': 'Featured image missing alt text',
                    'recommendation': 'Add descriptive alt text for accessibility'
                })
        
        # Navigation analizi
        breadcrumb = soup.find(class_='breadcrumb')
        if not breadcrumb:
            analysis['navigation_issues'].append({
                'issue': 'Missing breadcrumb navigation',
                'recommendation': 'Add breadcrumb for better user orientation'
            })
        
        # Reading experience
        article_body = soup.find(class_='article-body')
        if article_body:
            paragraphs = article_body.find_all('p')
            if len(paragraphs) < 5:
                analysis['content_issues'].append({
                    'issue': 'Content too short for engagement',
                    'paragraph_count': len(paragraphs),
                    'recommendation': 'Expand content for better user engagement'
                })
        
        analysis['improvement_suggestions'] = [
            'Add table of contents for longer articles',
            'Implement related posts section',
            'Add social sharing buttons',
            'Improve typography with better line spacing',
            'Add estimated reading time display',
            'Implement print-friendly styles'
        ]
        
        return analysis

    def analyze_css_structure(self):
        """CSS dosya yapısı analizi"""
        css_files = []
        
        # Ana CSS dosyalarını bul
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith('.css'):
                    css_files.append(os.path.join(root, file))
        
        css_analysis = {
            'total_css_files': len(css_files),
            'main_stylesheets': [],
            'redundant_files': [],
            'optimization_opportunities': []
        }
        
        # CSS dosyalarını kategorize et
        for css_file in css_files:
            file_size = os.path.getsize(css_file)
            relative_path = os.path.relpath(css_file, self.project_root)
            
            css_analysis['main_stylesheets'].append({
                'path': relative_path,
                'size_kb': file_size // 1024,
                'purpose': self.determine_css_purpose(relative_path)
            })
        
        # Optimizasyon önerileri
        if len(css_files) > 5:
            css_analysis['optimization_opportunities'].append({
                'type': 'Consolidation',
                'description': 'Too many CSS files - consider combining',
                'impact': 'Reduce HTTP requests and improve loading speed'
            })
        
        return css_analysis

    def determine_css_purpose(self, css_path):
        """CSS dosyasının amacını belirleme"""
        if 'blog' in css_path.lower():
            return 'Blog-specific styles'
        elif 'main' in css_path.lower() or 'styles.css' in css_path:
            return 'Main site styles'
        elif 'responsive' in css_path.lower():
            return 'Responsive design'
        elif 'component' in css_path.lower():
            return 'Component styles'
        else:
            return 'General purpose'

    def create_design_improvement_plan(self):
        """Tasarım iyileştirme planı oluştur"""
        
        # Blog ana sayfa analizi
        index_analysis = self.analyze_blog_index_design()
        
        # Örnek blog yazısı analizi
        sample_blogs = ['vintage-clothing-ozel-care', 'kuru-temizleme', 'hali-yikama']
        post_analyses = []
        
        for blog_slug in sample_blogs:
            analysis = self.analyze_blog_post_design(blog_slug)
            if analysis:
                post_analyses.append(analysis)
        
        # CSS yapısı analizi
        css_analysis = self.analyze_css_structure()
        
        # Comprehensive improvement plan
        improvement_plan = {
            'analysis_date': datetime.now().isoformat(),
            'project': 'DryAlle Blog Design Improvement Analysis',
            'current_state': {
                'blog_index_analysis': index_analysis,
                'blog_post_analyses': post_analyses,
                'css_structure_analysis': css_analysis
            },
            'priority_improvements': {
                'high_priority': [
                    {
                        'area': 'CSS Consolidation',
                        'description': 'Merge multiple CSS files into optimized structure',
                        'impact': 'Faster loading, easier maintenance',
                        'effort': 'Medium'
                    },
                    {
                        'area': 'Visual Hierarchy',
                        'description': 'Improve typography, spacing, and content organization',
                        'impact': 'Better readability and user experience',
                        'effort': 'High'
                    },
                    {
                        'area': 'Mobile Responsiveness',
                        'description': 'Enhanced mobile design with proper breakpoints',
                        'impact': 'Better mobile user experience',
                        'effort': 'High'
                    }
                ],
                'medium_priority': [
                    {
                        'area': 'Card Design System',
                        'description': 'Modern card-based layout with hover effects',
                        'impact': 'More professional appearance',
                        'effort': 'Medium'
                    },
                    {
                        'area': 'Navigation Enhancement',
                        'description': 'Improved breadcrumbs and internal linking',
                        'impact': 'Better site navigation',
                        'effort': 'Low'
                    }
                ],
                'low_priority': [
                    {
                        'area': 'Micro-interactions',
                        'description': 'Subtle animations and hover effects',
                        'impact': 'Enhanced user engagement',
                        'effort': 'Medium'
                    }
                ]
            },
            'implementation_roadmap': {
                'phase_1_immediate': {
                    'duration': '1-2 days',
                    'tasks': [
                        'CSS file consolidation',
                        'Fix responsive breakpoints',
                        'Improve typography'
                    ]
                },
                'phase_2_design': {
                    'duration': '3-5 days',
                    'tasks': [
                        'Modern card design implementation',
                        'Enhanced visual hierarchy',
                        'Color scheme optimization'
                    ]
                },
                'phase_3_enhancement': {
                    'duration': '2-3 days',
                    'tasks': [
                        'Navigation improvements',
                        'Loading states',
                        'Micro-interactions'
                    ]
                }
            },
            'specific_fixes': {
                'blog_index_fixes': [
                    'Reduce CSS file count from 3+ to 2 optimized files',
                    'Implement proper grid system with CSS Grid',
                    'Add hover effects for blog cards',
                    'Improve filter button design',
                    'Enhanced search functionality UI'
                ],
                'blog_post_fixes': [
                    'Better article layout with proper spacing',
                    'Improved featured image presentation',
                    'Enhanced typography for reading experience',
                    'Add related posts section',
                    'Social sharing integration'
                ]
            }
        }
        
        return improvement_plan

    def save_analysis_report(self):
        """Analiz raporunu kaydet"""
        improvement_plan = self.create_design_improvement_plan()
        
        # JSON raporu kaydet
        reports_dir = os.path.join(self.project_root, 'seo/reports')
        os.makedirs(reports_dir, exist_ok=True)
        
        report_path = os.path.join(reports_dir, 'blog_design_improvement_analysis.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(improvement_plan, f, ensure_ascii=False, indent=2)
        
        return report_path, improvement_plan

def main():
    """Blog Tasarım İyileştirme Analizi"""
    print("📊 BLOG TASARIM İYİLEŞTİRME ANALİZİ")
    print("=" * 60)
    print("🎯 Design Quality | CSS Structure | UX Analysis")
    print("=" * 60)
    
    analyzer = BlogDesignAnalyzer()
    
    try:
        # Analiz raporunu oluştur
        report_path, improvement_plan = analyzer.save_analysis_report()
        
        # Özet
        print("\n" + "=" * 60)
        print("📊 BLOG TASARIM ANALİZİ TAMAMLANDI")
        print("=" * 60)
        
        # Mevcut durum
        current_state = improvement_plan['current_state']
        print(f"✅ Blog index analizi: {len(current_state['blog_index_analysis']['design_issues'])} sorun tespit edildi")
        print(f"✅ Blog post analizi: {len(current_state['blog_post_analyses'])} sayfa incelendi")
        print(f"✅ CSS yapısı: {current_state['css_structure_analysis']['total_css_files']} dosya analiz edildi")
        
        # Öncelikli iyileştirmeler
        priorities = improvement_plan['priority_improvements']
        print(f"\n🔴 YÜKSEK ÖNCELİKLİ İYİLEŞTİRMELER:")
        for item in priorities['high_priority']:
            print(f"   • {item['area']}: {item['description']}")
        
        print(f"\n🟡 ORTA ÖNCELİKLİ İYİLEŞTİRMELER:")
        for item in priorities['medium_priority']:
            print(f"   • {item['area']}: {item['description']}")
        
        # Implementation roadmap
        roadmap = improvement_plan['implementation_roadmap']
        print(f"\n⏱️ UYGULAMA TAKVIMI:")
        for phase, details in roadmap.items():
            print(f"   📅 {phase}: {details['duration']}")
            for task in details['tasks'][:2]:
                print(f"      - {task}")
        
        # Specific fixes
        fixes = improvement_plan['specific_fixes']
        print(f"\n🔧 ÖZELLİKLE DÜZELTİLMESİ GEREKENLER:")
        print(f"   📄 Blog Index: {len(fixes['blog_index_fixes'])} düzeltme")
        print(f"   📝 Blog Posts: {len(fixes['blog_post_fixes'])} düzeltme")
        
        print(f"\n📁 RAPOR DOSYASI:")
        print(f"   📊 Detaylı Analiz: {report_path}")
        
        print(f"\n🎯 ÖNERİLER:")
        print(f"   • CSS dosyalarını birleştir ve optimize et")
        print(f"   • Modern kart tasarımı uygula")
        print(f"   • Mobil deneyimi iyileştir")
        print(f"   • Typography ve spacing'i düzelt")
        
        print(f"\n🎉 TASARIM ANALİZİ HAZIR!")
        print(f"   • Detaylı sorun analizi tamamlandı")
        print(f"   • Öncelikli iyileştirme planı oluşturuldu")
        print(f"   • Aşamalı uygulama takvimi hazırlandı")
        
        return True
        
    except Exception as e:
        print(f"❌ Analiz hatası: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)