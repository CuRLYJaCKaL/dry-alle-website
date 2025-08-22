#!/usr/bin/env python3
"""
Comprehensive SEO Analysis Tool for DryAlle Regional Pages
Performs fresh analysis of all 36 regional pages to validate improvements
"""

import os
import re
import json
import unicodedata
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin
import html

class ComprehensiveSEOAnalyzer:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.results = {}
        self.summary_stats = {
            'total_pages': 0,
            'perfect_titles': 0,
            'good_descriptions': 0,
            'breadcrumb_schema_count': 0,
            'localbusiness_schema_count': 0,
            'canonical_urls': 0,
            'avg_seo_score': 0,
            'pages_with_issues': 0,
            'top_performers': [],
            'pages_needing_attention': []
        }
        
    def analyze_all_pages(self):
        """Analyze all HTML files in the directory"""
        html_files = [f for f in os.listdir(self.directory_path) 
                     if f.endswith('.html')]
        
        print(f"Found {len(html_files)} HTML files to analyze")
        self.summary_stats['total_pages'] = len(html_files)
        
        for filename in sorted(html_files):
            file_path = os.path.join(self.directory_path, filename)
            print(f"Analyzing: {filename}")
            
            try:
                analysis = self.analyze_page(file_path, filename)
                self.results[filename] = analysis
            except Exception as e:
                print(f"Error analyzing {filename}: {str(e)}")
                self.results[filename] = {'error': str(e), 'seo_score': 0}
        
        self.calculate_summary_statistics()
        return self.results
    
    def analyze_page(self, file_path, filename):
        """Comprehensive analysis of a single page"""
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        analysis = {
            'filename': filename,
            'meta_tags': self.analyze_meta_tags(soup),
            'schema_markup': self.analyze_schema_markup(soup, content),
            'technical_seo': self.analyze_technical_seo(soup, content),
            'content_analysis': self.analyze_content(soup),
            'issues': [],
            'strengths': [],
            'seo_score': 0
        }
        
        # Calculate SEO score
        analysis['seo_score'] = self.calculate_seo_score(analysis)
        
        # Identify issues and strengths
        self.identify_issues_and_strengths(analysis)
        
        return analysis
    
    def analyze_meta_tags(self, soup):
        """Analyze meta tags"""
        meta_analysis = {}
        
        # Title tag
        title_tag = soup.find('title')
        if title_tag:
            title_text = title_tag.get_text().strip()
            meta_analysis['title'] = {
                'content': title_text,
                'length': len(title_text),
                'is_optimal': 30 <= len(title_text) <= 70,
                'has_location': any(city in title_text.lower() for city in 
                                  ['kadıköy', 'üsküdar', 'ataşehir', 'maltepe', 'kartal', 'pendik', 'ümraniye']),
                'has_service': any(service in title_text.lower() for service in 
                                 ['halı yıkama', 'koltuk yıkama', 'kuru temizleme', 'temizlik'])
            }
        else:
            meta_analysis['title'] = {'content': '', 'length': 0, 'is_optimal': False}
        
        # Meta description
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        if desc_tag:
            desc_content = desc_tag.get('content', '').strip()
            meta_analysis['description'] = {
                'content': desc_content,
                'length': len(desc_content),
                'is_optimal': 120 <= len(desc_content) <= 160,
                'has_location': any(city in desc_content.lower() for city in 
                                  ['kadıköy', 'üsküdar', 'ataşehir', 'maltepe', 'kartal', 'pendik', 'ümraniye']),
                'has_cta': any(cta in desc_content.lower() for cta in 
                             ['hemen ara', 'ücretsiz keşif', 'rezervasyon', 'iletişim'])
            }
        else:
            meta_analysis['description'] = {'content': '', 'length': 0, 'is_optimal': False}
        
        # Keywords
        keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
        if keywords_tag:
            keywords_content = keywords_tag.get('content', '').strip()
            keywords_list = [k.strip() for k in keywords_content.split(',') if k.strip()]
            meta_analysis['keywords'] = {
                'content': keywords_content,
                'count': len(keywords_list),
                'list': keywords_list,
                'is_optimal': 5 <= len(keywords_list) <= 15
            }
        else:
            meta_analysis['keywords'] = {'content': '', 'count': 0, 'is_optimal': False}
        
        # Open Graph tags
        og_tags = {}
        for og_tag in soup.find_all('meta', attrs={'property': re.compile(r'^og:')}):
            property_name = og_tag.get('property')
            og_tags[property_name] = og_tag.get('content', '')
        meta_analysis['open_graph'] = og_tags
        
        return meta_analysis
    
    def analyze_schema_markup(self, soup, content):
        """Analyze Schema.org markup"""
        schema_analysis = {
            'json_ld_count': 0,
            'breadcrumb_schema': False,
            'localbusiness_schema': False,
            'service_schema': False,
            'organization_schema': False,
            'webpage_schema': False,
            'postaladdress_schema': False,
            'contactpoint_schema': False,
            'schemas_found': [],
            'syntax_errors': []
        }
        
        # Find all JSON-LD scripts
        json_ld_scripts = soup.find_all('script', type='application/ld+json')
        schema_analysis['json_ld_count'] = len(json_ld_scripts)
        
        for script in json_ld_scripts:
            try:
                schema_data = json.loads(script.string)
                if isinstance(schema_data, list):
                    for item in schema_data:
                        self.process_schema_item(item, schema_analysis)
                else:
                    self.process_schema_item(schema_data, schema_analysis)
            except json.JSONDecodeError as e:
                schema_analysis['syntax_errors'].append(f"JSON syntax error: {str(e)}")
        
        return schema_analysis
    
    def process_schema_item(self, item, schema_analysis):
        """Process individual schema item"""
        if not isinstance(item, dict):
            return
            
        schema_type = item.get('@type', '').lower()
        context = item.get('@context', '')
        
        if 'schema.org' in context:
            schema_analysis['schemas_found'].append(schema_type)
            
            if schema_type == 'breadcrumblist':
                schema_analysis['breadcrumb_schema'] = True
            elif schema_type == 'localbusiness':
                schema_analysis['localbusiness_schema'] = True
            elif schema_type in ['service', 'cleaningservice']:
                schema_analysis['service_schema'] = True
            elif schema_type == 'organization':
                schema_analysis['organization_schema'] = True
            elif schema_type == 'webpage':
                schema_analysis['webpage_schema'] = True
            elif schema_type == 'postaladdress':
                schema_analysis['postaladdress_schema'] = True
            elif schema_type == 'contactpoint':
                schema_analysis['contactpoint_schema'] = True
    
    def analyze_technical_seo(self, soup, content):
        """Analyze technical SEO aspects"""
        technical = {}
        
        # Canonical URL
        canonical_tag = soup.find('link', rel='canonical')
        technical['canonical_url'] = {
            'present': canonical_tag is not None,
            'url': canonical_tag.get('href') if canonical_tag else None
        }
        
        # Character encoding
        charset_meta = soup.find('meta', charset=True)
        if not charset_meta:
            charset_meta = soup.find('meta', attrs={'http-equiv': 'Content-Type'})
        
        technical['charset'] = {
            'present': charset_meta is not None,
            'value': charset_meta.get('charset') or 
                    (charset_meta.get('content') if charset_meta else None)
        }
        
        # Turkish character handling
        turkish_chars = ['ç', 'ğ', 'ı', 'ö', 'ş', 'ü', 'Ç', 'Ğ', 'İ', 'Ö', 'Ş', 'Ü']
        has_turkish_chars = any(char in content for char in turkish_chars)
        
        # Check for encoding issues
        encoding_issues = []
        for char in turkish_chars:
            if char in content:
                # Check if properly encoded
                try:
                    char.encode('utf-8').decode('utf-8')
                except UnicodeDecodeError:
                    encoding_issues.append(f"Encoding issue with: {char}")
        
        technical['turkish_characters'] = {
            'present': has_turkish_chars,
            'encoding_issues': encoding_issues,
            'properly_encoded': len(encoding_issues) == 0
        }
        
        # Internal links
        internal_links = soup.find_all('a', href=True)
        internal_count = 0
        external_count = 0
        
        for link in internal_links:
            href = link.get('href', '')
            if href.startswith('http://') or href.startswith('https://'):
                if 'dryalle.com' in href:
                    internal_count += 1
                else:
                    external_count += 1
            elif href.startswith('/') or not href.startswith(('http', 'mailto:', 'tel:')):
                internal_count += 1
        
        technical['internal_links'] = {
            'count': internal_count,
            'external_count': external_count,
            'total_links': len(internal_links)
        }
        
        # URL structure (extracted from canonical or filename)
        url_structure = technical['canonical_url']['url'] or 'Unknown'
        technical['url_structure'] = {
            'url': url_structure,
            'has_hyphens': '-' in url_structure,
            'has_location': any(city in url_structure for city in 
                              ['kadikoy', 'uskudar', 'atasehir', 'maltepe', 'kartal', 'pendik', 'umraniye']),
            'has_service': any(service in url_structure for service in 
                             ['hali-yikama', 'koltuk-yikama', 'kuru-temizleme', 'temizlik'])
        }
        
        return technical
    
    def analyze_content(self, soup):
        """Analyze content quality and optimization"""
        content_analysis = {}
        
        # H1 tag
        h1_tags = soup.find_all('h1')
        if h1_tags:
            h1_text = h1_tags[0].get_text().strip()
            content_analysis['h1'] = {
                'content': h1_text,
                'length': len(h1_text),
                'count': len(h1_tags),
                'is_optimal': len(h1_tags) == 1 and 20 <= len(h1_text) <= 70,
                'has_location': any(city in h1_text.lower() for city in 
                                  ['kadıköy', 'üsküdar', 'ataşehir', 'maltepe', 'kartal', 'pendik', 'ümraniye']),
                'has_service': any(service in h1_text.lower() for service in 
                                 ['halı yıkama', 'koltuk yıkama', 'kuru temizleme', 'temizlik'])
            }
        else:
            content_analysis['h1'] = {'content': '', 'count': 0, 'is_optimal': False}
        
        # Other headings
        h2_tags = soup.find_all('h2')
        h3_tags = soup.find_all('h3')
        
        content_analysis['headings'] = {
            'h2_count': len(h2_tags),
            'h3_count': len(h3_tags),
            'total_headings': len(h1_tags) + len(h2_tags) + len(h3_tags),
            'proper_hierarchy': len(h1_tags) == 1 and len(h2_tags) >= 2
        }
        
        # Word count
        text_content = soup.get_text()
        # Clean text
        text_content = re.sub(r'\s+', ' ', text_content).strip()
        word_count = len(text_content.split())
        
        content_analysis['word_count'] = {
            'total': word_count,
            'is_optimal': word_count >= 300,
            'category': 'excellent' if word_count >= 500 else 
                       'good' if word_count >= 300 else 
                       'needs_improvement'
        }
        
        # Keyword density analysis
        # Extract location and service from filename or content
        location_keywords = ['kadıköy', 'üsküdar', 'ataşehir', 'maltepe', 'kartal', 'pendik', 'ümraniye',
                           'acibadem', 'altunizade', 'bağdat caddesi', 'barbaros', 'bostancı', 
                           'caddebostan', 'çamlıca', 'erenköy', 'fenerbahçe', 'fikirtepe', 
                           'göztepe', 'içerenköy', 'kalamış', 'kozyatağı', 'küçükbakkalköy',
                           'moda', 'sahrayıcedit', 'suadiye']
        
        service_keywords = ['halı yıkama', 'koltuk yıkama', 'kuru temizleme', 'temizlik', 
                          'luxury', 'premium', 'haute couture', 'gelinlik']
        
        text_lower = text_content.lower()
        
        location_mentions = sum(text_lower.count(keyword) for keyword in location_keywords)
        service_mentions = sum(text_lower.count(keyword) for keyword in service_keywords)
        
        content_analysis['keyword_density'] = {
            'location_mentions': location_mentions,
            'service_mentions': service_mentions,
            'location_density': (location_mentions / word_count * 100) if word_count > 0 else 0,
            'service_density': (service_mentions / word_count * 100) if word_count > 0 else 0,
            'is_optimal': 1 <= (location_mentions + service_mentions) / word_count * 100 <= 3
        }
        
        return content_analysis
    
    def calculate_seo_score(self, analysis):
        """Calculate overall SEO score (1-10 scale)"""
        score = 0
        max_score = 100
        
        # Meta tags (25 points)
        if analysis['meta_tags']['title']['is_optimal']:
            score += 10
        elif analysis['meta_tags']['title']['length'] > 0:
            score += 5
        
        if analysis['meta_tags']['description']['is_optimal']:
            score += 10
        elif analysis['meta_tags']['description']['length'] > 0:
            score += 5
        
        if analysis['meta_tags']['keywords']['is_optimal']:
            score += 5
        
        # Schema markup (25 points)
        schema_score = 0
        if analysis['schema_markup']['breadcrumb_schema']:
            schema_score += 8
        if analysis['schema_markup']['localbusiness_schema']:
            schema_score += 8
        if analysis['schema_markup']['service_schema']:
            schema_score += 3
        if analysis['schema_markup']['organization_schema']:
            schema_score += 3
        if analysis['schema_markup']['webpage_schema']:
            schema_score += 3
        score += min(schema_score, 25)
        
        # Technical SEO (25 points)
        if analysis['technical_seo']['canonical_url']['present']:
            score += 8
        if analysis['technical_seo']['charset']['present']:
            score += 5
        if analysis['technical_seo']['turkish_characters']['properly_encoded']:
            score += 7
        if analysis['technical_seo']['internal_links']['count'] >= 3:
            score += 5
        
        # Content (25 points)
        if analysis['content_analysis']['h1']['is_optimal']:
            score += 8
        elif analysis['content_analysis']['h1']['count'] == 1:
            score += 5
        
        if analysis['content_analysis']['word_count']['is_optimal']:
            score += 10
        elif analysis['content_analysis']['word_count']['total'] >= 200:
            score += 6
        
        if analysis['content_analysis']['headings']['proper_hierarchy']:
            score += 4
        
        if analysis['content_analysis']['keyword_density']['is_optimal']:
            score += 3
        
        # Convert to 1-10 scale
        final_score = round((score / max_score) * 10, 1)
        return max(1.0, min(10.0, final_score))
    
    def identify_issues_and_strengths(self, analysis):
        """Identify specific issues and strengths"""
        issues = []
        strengths = []
        
        # Title issues
        title_len = analysis['meta_tags']['title']['length']
        if title_len == 0:
            issues.append("Missing title tag")
        elif title_len > 70:
            issues.append(f"Title too long ({title_len} chars, should be ≤70)")
        elif title_len < 30:
            issues.append(f"Title too short ({title_len} chars, should be ≥30)")
        else:
            strengths.append("Optimal title length")
        
        # Description issues
        desc_len = analysis['meta_tags']['description']['length']
        if desc_len == 0:
            issues.append("Missing meta description")
        elif desc_len < 120:
            issues.append(f"Meta description too short ({desc_len} chars)")
        elif desc_len > 160:
            issues.append(f"Meta description too long ({desc_len} chars)")
        else:
            strengths.append("Optimal meta description length")
        
        # Schema issues
        if not analysis['schema_markup']['breadcrumb_schema']:
            issues.append("Missing BreadcrumbList schema")
        else:
            strengths.append("BreadcrumbList schema present")
        
        if not analysis['schema_markup']['localbusiness_schema']:
            issues.append("Missing LocalBusiness schema")
        else:
            strengths.append("LocalBusiness schema present")
        
        # Technical issues
        if not analysis['technical_seo']['canonical_url']['present']:
            issues.append("Missing canonical URL")
        else:
            strengths.append("Canonical URL present")
        
        if not analysis['technical_seo']['turkish_characters']['properly_encoded']:
            issues.append("Turkish character encoding issues")
        else:
            strengths.append("Proper Turkish character encoding")
        
        # Content issues
        if analysis['content_analysis']['h1']['count'] == 0:
            issues.append("Missing H1 tag")
        elif analysis['content_analysis']['h1']['count'] > 1:
            issues.append("Multiple H1 tags found")
        else:
            strengths.append("Single H1 tag present")
        
        if analysis['content_analysis']['word_count']['total'] < 300:
            issues.append(f"Low word count ({analysis['content_analysis']['word_count']['total']} words)")
        else:
            strengths.append("Adequate word count")
        
        analysis['issues'] = issues
        analysis['strengths'] = strengths
    
    def calculate_summary_statistics(self):
        """Calculate summary statistics"""
        if not self.results:
            return
        
        scores = []
        perfect_titles = 0
        good_descriptions = 0
        breadcrumb_count = 0
        localbusiness_count = 0
        canonical_count = 0
        pages_with_issues = 0
        
        for filename, analysis in self.results.items():
            if 'error' in analysis:
                continue
                
            score = analysis.get('seo_score', 0)
            scores.append(score)
            
            # Count perfect titles
            if analysis['meta_tags']['title']['is_optimal']:
                perfect_titles += 1
            
            # Count good descriptions
            if analysis['meta_tags']['description']['is_optimal']:
                good_descriptions += 1
            
            # Count schema implementations
            if analysis['schema_markup']['breadcrumb_schema']:
                breadcrumb_count += 1
            
            if analysis['schema_markup']['localbusiness_schema']:
                localbusiness_count += 1
            
            # Count canonical URLs
            if analysis['technical_seo']['canonical_url']['present']:
                canonical_count += 1
            
            # Count pages with issues
            if len(analysis['issues']) > 0:
                pages_with_issues += 1
        
        # Update summary statistics
        self.summary_stats.update({
            'perfect_titles': perfect_titles,
            'good_descriptions': good_descriptions,
            'breadcrumb_schema_count': breadcrumb_count,
            'localbusiness_schema_count': localbusiness_count,
            'canonical_urls': canonical_count,
            'avg_seo_score': round(sum(scores) / len(scores), 2) if scores else 0,
            'pages_with_issues': pages_with_issues
        })
        
        # Identify top performers and pages needing attention
        scored_pages = [(filename, analysis['seo_score']) for filename, analysis in self.results.items() 
                       if 'error' not in analysis]
        scored_pages.sort(key=lambda x: x[1], reverse=True)
        
        self.summary_stats['top_performers'] = scored_pages[:5]
        self.summary_stats['pages_needing_attention'] = scored_pages[-5:]
    
    def generate_report(self):
        """Generate comprehensive analysis report"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = {
            'analysis_metadata': {
                'timestamp': timestamp,
                'analyzer_version': '2.0',
                'directory_analyzed': self.directory_path,
                'analysis_type': 'comprehensive_fresh_analysis'
            },
            'summary_statistics': self.summary_stats,
            'detailed_results': self.results,
            'recommendations': self.generate_recommendations(),
            'improvement_opportunities': self.identify_improvement_opportunities()
        }
        
        return report
    
    def generate_recommendations(self):
        """Generate specific recommendations"""
        recommendations = []
        
        total_pages = self.summary_stats['total_pages']
        
        # Title recommendations
        if self.summary_stats['perfect_titles'] < total_pages:
            missing = total_pages - self.summary_stats['perfect_titles']
            recommendations.append(f"Optimize {missing} page titles to 30-70 character range")
        
        # Description recommendations
        if self.summary_stats['good_descriptions'] < total_pages:
            missing = total_pages - self.summary_stats['good_descriptions']
            recommendations.append(f"Optimize {missing} meta descriptions to 120-160 character range")
        
        # Schema recommendations
        if self.summary_stats['breadcrumb_schema_count'] < total_pages:
            missing = total_pages - self.summary_stats['breadcrumb_schema_count']
            recommendations.append(f"Add BreadcrumbList schema to {missing} pages")
        
        if self.summary_stats['localbusiness_schema_count'] < total_pages:
            missing = total_pages - self.summary_stats['localbusiness_schema_count']
            recommendations.append(f"Add LocalBusiness schema to {missing} pages")
        
        # Technical recommendations
        if self.summary_stats['canonical_urls'] < total_pages:
            missing = total_pages - self.summary_stats['canonical_urls']
            recommendations.append(f"Add canonical URLs to {missing} pages")
        
        return recommendations
    
    def identify_improvement_opportunities(self):
        """Identify specific improvement opportunities"""
        opportunities = []
        
        # Analyze common issues across pages
        all_issues = []
        for filename, analysis in self.results.items():
            if 'error' not in analysis:
                all_issues.extend(analysis['issues'])
        
        # Count issue frequency
        issue_counts = {}
        for issue in all_issues:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
        
        # Sort by frequency
        sorted_issues = sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)
        
        for issue, count in sorted_issues[:10]:  # Top 10 most common issues
            opportunities.append(f"{issue} (affects {count} pages)")
        
        return opportunities

def main():
    analyzer = ComprehensiveSEOAnalyzer('/Users/macos/Documents/Projeler/DryAlle/bolgeler')
    
    print("Starting comprehensive SEO analysis of all regional pages...")
    print("=" * 60)
    
    # Perform analysis
    results = analyzer.analyze_all_pages()
    
    # Generate report
    report = analyzer.generate_report()
    
    # Save detailed report
    report_filename = f"comprehensive_seo_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_path = os.path.join(analyzer.directory_path, report_filename)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"Detailed report saved to: {report_filename}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("COMPREHENSIVE SEO ANALYSIS SUMMARY")
    print("=" * 60)
    
    stats = report['summary_statistics']
    print(f"Total pages analyzed: {stats['total_pages']}")
    print(f"Average SEO score: {stats['avg_seo_score']}/10")
    print(f"Pages with optimal titles: {stats['perfect_titles']}/{stats['total_pages']}")
    print(f"Pages with good descriptions: {stats['good_descriptions']}/{stats['total_pages']}")
    print(f"Pages with BreadcrumbList schema: {stats['breadcrumb_schema_count']}/{stats['total_pages']}")
    print(f"Pages with LocalBusiness schema: {stats['localbusiness_schema_count']}/{stats['total_pages']}")
    print(f"Pages with canonical URLs: {stats['canonical_urls']}/{stats['total_pages']}")
    print(f"Pages needing attention: {stats['pages_with_issues']}")
    
    print("\nTOP PERFORMING PAGES:")
    for filename, score in stats['top_performers']:
        print(f"  {filename}: {score}/10")
    
    print("\nPAGES NEEDING ATTENTION:")
    for filename, score in stats['pages_needing_attention']:
        print(f"  {filename}: {score}/10")
    
    print("\nTOP RECOMMENDATIONS:")
    for i, rec in enumerate(report['recommendations'][:5], 1):
        print(f"  {i}. {rec}")
    
    print("\nTOP IMPROVEMENT OPPORTUNITIES:")
    for i, opp in enumerate(report['improvement_opportunities'][:5], 1):
        print(f"  {i}. {opp}")
    
    return report_path

if __name__ == "__main__":
    main()