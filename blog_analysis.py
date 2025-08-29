#!/usr/bin/env python3
"""
Comprehensive Blog Articles Consistency Analysis
Analyzes all blog articles for consistency across multiple criteria
"""

import os
import re
from bs4 import BeautifulSoup
import json
from collections import defaultdict

class BlogAnalyzer:
    def __init__(self, blog_directory):
        self.blog_directory = blog_directory
        self.results = {
            'total_articles': 0,
            'navigation_issues': [],
            'meta_tags_issues': [],
            'schema_issues': [],
            'content_structure_issues': [],
            'seo_issues': [],
            'overall_score': 0
        }
        
    def analyze_all_articles(self):
        """Main analysis function"""
        article_files = []
        
        # Find all index.html files in blog subdirectories
        for root, dirs, files in os.walk(self.blog_directory):
            for file in files:
                if file == 'index.html':
                    filepath = os.path.join(root, file)
                    # Skip main blog index
                    if root != self.blog_directory:
                        article_files.append(filepath)
        
        self.results['total_articles'] = len(article_files)
        print(f"Found {len(article_files)} blog articles to analyze")
        
        # Analyze each article
        for i, filepath in enumerate(article_files, 1):
            print(f"Analyzing article {i}/{len(article_files)}: {os.path.basename(os.path.dirname(filepath))}")
            self.analyze_single_article(filepath)
        
        # Calculate overall score
        self.calculate_overall_score()
        
    def analyze_single_article(self, filepath):
        """Analyze a single article for all criteria"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            soup = BeautifulSoup(content, 'html.parser')
            article_name = os.path.basename(os.path.dirname(filepath))
            
            # 1. Navigation Consistency
            self.check_navigation(soup, article_name)
            
            # 2. Meta Tags Standards
            self.check_meta_tags(soup, article_name)
            
            # 3. Schema Markup Validation
            self.check_schema_markup(soup, article_name)
            
            # 4. Content Structure
            self.check_content_structure(soup, article_name)
            
            # 5. SEO Elements
            self.check_seo_elements(soup, article_name)
            
        except Exception as e:
            print(f"Error analyzing {filepath}: {str(e)}")
    
    def check_navigation(self, soup, article_name):
        """Check navigation consistency"""
        nav_menu = soup.find('ul', class_='nav-menu')
        
        if not nav_menu:
            self.results['navigation_issues'].append(f"{article_name}: Navigation menu not found")
            return
            
        nav_items = nav_menu.find_all('li')
        
        # Check for expected 5 navigation items
        expected_nav_count = 5
        if len(nav_items) != expected_nav_count:
            self.results['navigation_issues'].append(
                f"{article_name}: Expected {expected_nav_count} nav items, found {len(nav_items)}"
            )
        
        # Check navigation links
        expected_links = ['ANASAYFA', 'HİZMETLER', 'BLOG', 'SSS', 'İLETİŞİM']
        actual_links = [item.get_text().strip() for item in nav_items if item.get_text().strip()]
        
        # Check for variations in navigation text (old navigation structure)
        old_nav_variations = ['Ana Sayfa', 'Hizmetlerimiz', 'Hakkımızda']
        
        has_old_nav = any(old_nav in actual_links for old_nav in old_nav_variations)
        
        if has_old_nav:
            self.results['navigation_issues'].append(
                f"{article_name}: Using OLD navigation structure - Found: {actual_links}"
            )
        
        # Check for missing SSS or İLETİŞİM in new navigation
        if not has_old_nav:
            if 'SSS' not in actual_links:
                self.results['navigation_issues'].append(
                    f"{article_name}: Missing SSS in navigation"
                )
            if 'İLETİŞİM' not in actual_links:
                self.results['navigation_issues'].append(
                    f"{article_name}: Missing İLETİŞİM in navigation"
                )
    
    def check_meta_tags(self, soup, article_name):
        """Check meta tags standards"""
        # Check meta description length
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            desc_content = meta_desc.get('content', '')
            desc_length = len(desc_content)
            
            if desc_length < 120 or desc_length > 160:
                self.results['meta_tags_issues'].append(
                    f"{article_name}: Meta description length ({desc_length} chars) not optimal (120-160 chars)"
                )
        else:
            self.results['meta_tags_issues'].append(f"{article_name}: Meta description missing")
        
        # Check title tag
        title_tag = soup.find('title')
        if not title_tag:
            self.results['meta_tags_issues'].append(f"{article_name}: Title tag missing")
        else:
            title_length = len(title_tag.get_text())
            if title_length > 60:
                self.results['meta_tags_issues'].append(
                    f"{article_name}: Title too long ({title_length} chars) - should be under 60"
                )
        
        # Check og:image
        og_image = soup.find('meta', property='og:image')
        if not og_image:
            self.results['meta_tags_issues'].append(f"{article_name}: og:image missing")
        
        # Check og:description
        og_desc = soup.find('meta', property='og:description')
        if not og_desc:
            self.results['meta_tags_issues'].append(f"{article_name}: og:description missing")
    
    def check_schema_markup(self, soup, article_name):
        """Check schema markup validation"""
        # Check for BlogPosting schema
        script_tags = soup.find_all('script', type='application/ld+json')
        
        has_blog_schema = False
        has_author = False
        has_date_published = False
        has_date_modified = False
        has_breadcrumb = False
        
        for script in script_tags:
            try:
                schema_data = json.loads(script.string)
                
                if schema_data.get('@type') == 'BlogPosting':
                    has_blog_schema = True
                    
                    if schema_data.get('author'):
                        has_author = True
                    
                    if schema_data.get('datePublished'):
                        has_date_published = True
                        
                    if schema_data.get('dateModified'):
                        has_date_modified = True
                
                if schema_data.get('@type') == 'BreadcrumbList':
                    has_breadcrumb = True
                    
            except json.JSONDecodeError:
                continue
        
        if not has_blog_schema:
            self.results['schema_issues'].append(f"{article_name}: BlogPosting schema missing")
        
        if not has_author:
            self.results['schema_issues'].append(f"{article_name}: Author field missing in schema")
            
        if not has_date_published:
            self.results['schema_issues'].append(f"{article_name}: datePublished missing in schema")
            
        if not has_date_modified:
            self.results['schema_issues'].append(f"{article_name}: dateModified missing in schema")
    
    def check_content_structure(self, soup, article_name):
        """Check content structure"""
        # Check H1 tag - should be exactly 1
        h1_tags = soup.find_all('h1')
        if len(h1_tags) != 1:
            self.results['content_structure_issues'].append(
                f"{article_name}: Found {len(h1_tags)} H1 tags, should be exactly 1"
            )
        
        # Check H2/H3 hierarchy
        h2_tags = soup.find_all('h2')
        h3_tags = soup.find_all('h3')
        
        if len(h2_tags) == 0:
            self.results['content_structure_issues'].append(f"{article_name}: No H2 tags found")
        
        # Check featured image
        featured_img = soup.find('img', class_='featured-image')
        if not featured_img:
            self.results['content_structure_issues'].append(f"{article_name}: Featured image missing")
    
    def check_seo_elements(self, soup, article_name):
        """Check SEO elements"""
        # Check canonical URL
        canonical = soup.find('link', rel='canonical')
        if not canonical:
            self.results['seo_issues'].append(f"{article_name}: Canonical URL missing")
        
        # Check hreflang tags
        hreflang = soup.find('link', attrs={'rel': 'alternate', 'hreflang': 'tr'})
        if not hreflang:
            self.results['seo_issues'].append(f"{article_name}: Hreflang tags missing")
        
        # Check social media meta tags
        og_type = soup.find('meta', property='og:type')
        if not og_type:
            self.results['seo_issues'].append(f"{article_name}: og:type missing")
    
    def calculate_overall_score(self):
        """Calculate overall consistency score"""
        total_issues = (
            len(self.results['navigation_issues']) +
            len(self.results['meta_tags_issues']) +
            len(self.results['schema_issues']) +
            len(self.results['content_structure_issues']) +
            len(self.results['seo_issues'])
        )
        
        # Maximum possible issues (assuming worst case scenario)
        max_possible_issues = self.results['total_articles'] * 15  # Approximately 15 checks per article
        
        if max_possible_issues > 0:
            score = max(0, 100 - (total_issues / max_possible_issues * 100))
            self.results['overall_score'] = round(score, 1)
        else:
            self.results['overall_score'] = 100
    
    def generate_report(self):
        """Generate comprehensive report"""
        report = f"""
=======================================================
COMPREHENSIVE BLOG ARTICLES CONSISTENCY ANALYSIS REPORT
=======================================================

SUMMARY:
- Total Articles Analyzed: {self.results['total_articles']}
- Overall Consistency Score: {self.results['overall_score']}%

CRITICAL ISSUES FOUND:

1. NAVIGATION CONSISTENCY ISSUES ({len(self.results['navigation_issues'])}):
"""
        for issue in self.results['navigation_issues'][:10]:  # Show first 10
            report += f"   • {issue}\n"
        
        if len(self.results['navigation_issues']) > 10:
            report += f"   ... and {len(self.results['navigation_issues']) - 10} more issues\n"

        report += f"""
2. META TAGS ISSUES ({len(self.results['meta_tags_issues'])}):
"""
        for issue in self.results['meta_tags_issues'][:10]:
            report += f"   • {issue}\n"
            
        if len(self.results['meta_tags_issues']) > 10:
            report += f"   ... and {len(self.results['meta_tags_issues']) - 10} more issues\n"

        report += f"""
3. SCHEMA MARKUP ISSUES ({len(self.results['schema_issues'])}):
"""
        for issue in self.results['schema_issues'][:10]:
            report += f"   • {issue}\n"
            
        if len(self.results['schema_issues']) > 10:
            report += f"   ... and {len(self.results['schema_issues']) - 10} more issues\n"

        report += f"""
4. CONTENT STRUCTURE ISSUES ({len(self.results['content_structure_issues'])}):
"""
        for issue in self.results['content_structure_issues'][:10]:
            report += f"   • {issue}\n"
            
        if len(self.results['content_structure_issues']) > 10:
            report += f"   ... and {len(self.results['content_structure_issues']) - 10} more issues\n"

        report += f"""
5. SEO ELEMENTS ISSUES ({len(self.results['seo_issues'])}):
"""
        for issue in self.results['seo_issues'][:10]:
            report += f"   • {issue}\n"
            
        if len(self.results['seo_issues']) > 10:
            report += f"   ... and {len(self.results['seo_issues']) - 10} more issues\n"

        report += f"""
PRIORITY ACTIONS NEEDED:

HIGH PRIORITY:
- Fix navigation inconsistencies across all articles
- Standardize meta description lengths (120-160 characters)
- Ensure all articles have exactly one H1 tag

MEDIUM PRIORITY:
- Add missing schema markup elements
- Fix canonical URL issues
- Standardize social media meta tags

LOW PRIORITY:
- Optimize title tag lengths
- Add missing hreflang tags
- Ensure featured images are properly implemented

OVERALL ASSESSMENT:
"""

        if self.results['overall_score'] >= 90:
            report += "EXCELLENT - Blog articles are highly consistent with minimal issues."
        elif self.results['overall_score'] >= 75:
            report += "GOOD - Most articles follow standards with some minor inconsistencies."
        elif self.results['overall_score'] >= 60:
            report += "NEEDS IMPROVEMENT - Significant inconsistencies that should be addressed."
        else:
            report += "CRITICAL - Major consistency issues requiring immediate attention."

        report += f"""

=======================================================
Analysis completed successfully.
=======================================================
"""
        
        return report

if __name__ == "__main__":
    blog_directory = "/Users/macos/Documents/Projeler/DryAlle/blog"
    
    analyzer = BlogAnalyzer(blog_directory)
    analyzer.analyze_all_articles()
    report = analyzer.generate_report()
    
    print(report)
    
    # Save detailed results
    with open("/Users/macos/Documents/Projeler/DryAlle/blog_analysis_detailed_results.json", 'w', encoding='utf-8') as f:
        json.dump(analyzer.results, f, indent=2, ensure_ascii=False)