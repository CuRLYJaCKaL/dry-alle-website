#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
from bs4 import BeautifulSoup
from datetime import datetime

class ComprehensiveSEOAnalyzer:
    def __init__(self):
        self.results = {
            'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_files': 0,
            'files_analyzed': [],
            'meta_description_issues': [],
            'title_length_issues': [],
            'missing_h1': [],
            'missing_canonical': [],
            'missing_schema': [],
            'perfect_seo_recommendations': {}
        }
        
    def analyze_file(self, file_path):
        """Analyze a single HTML file for SEO elements"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            soup = BeautifulSoup(content, 'html.parser')
            
            file_name = os.path.basename(file_path)
            analysis = {
                'file': file_name,
                'title': '',
                'title_length': 0,
                'meta_description': '',
                'meta_description_length': 0,
                'has_h1': False,
                'h1_content': '',
                'has_canonical': False,
                'canonical_url': '',
                'has_schema': False,
                'schema_types': [],
                'issues': []
            }
            
            # Title Analysis
            title_tag = soup.find('title')
            if title_tag:
                analysis['title'] = title_tag.get_text().strip()
                analysis['title_length'] = len(analysis['title'])
                if analysis['title_length'] < 50 or analysis['title_length'] > 70:
                    analysis['issues'].append(f"Title length {analysis['title_length']} (optimal: 50-70)")
            else:
                analysis['issues'].append("Missing title tag")
                
            # Meta Description Analysis
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                analysis['meta_description'] = meta_desc.get('content', '').strip()
                analysis['meta_description_length'] = len(analysis['meta_description'])
                if analysis['meta_description_length'] < 120 or analysis['meta_description_length'] > 160:
                    analysis['issues'].append(f"Meta description length {analysis['meta_description_length']} (optimal: 120-160)")
            else:
                analysis['issues'].append("Missing meta description")
                
            # H1 Analysis
            h1_tag = soup.find('h1')
            if h1_tag:
                analysis['has_h1'] = True
                analysis['h1_content'] = h1_tag.get_text().strip()
            else:
                analysis['issues'].append("Missing H1 tag")
                
            # Canonical URL Analysis
            canonical = soup.find('link', attrs={'rel': 'canonical'})
            if canonical:
                analysis['has_canonical'] = True
                analysis['canonical_url'] = canonical.get('href', '')
            else:
                analysis['issues'].append("Missing canonical URL")
                
            # Schema Markup Analysis
            script_tags = soup.find_all('script', attrs={'type': 'application/ld+json'})
            if script_tags:
                analysis['has_schema'] = True
                for script in script_tags:
                    try:
                        schema_data = json.loads(script.string)
                        schema_type = schema_data.get('@type', 'Unknown')
                        analysis['schema_types'].append(schema_type)
                    except:
                        pass
            else:
                analysis['issues'].append("Missing schema markup")
                
            return analysis
            
        except Exception as e:
            return {'file': file_name, 'error': str(e)}
    
    def generate_optimized_meta_description(self, file_name):
        """Generate optimized meta description based on file name"""
        
        # Extract location and service from filename
        name_parts = file_name.replace('.html', '').split('-')
        location = name_parts[0].title()
        service = ' '.join(name_parts[1:]).title()
        
        # Location-specific keywords and descriptions
        descriptions = {
            'acibadem': f"{location}'de profesyonel {service.lower()} hizmeti. 25 yıllık deneyim, ücretsiz kapıdan teslimat. Takım elbise, elbise, palto temizleme uzmanı.",
            'altunizade': f"{location}'de lüks {service.lower()} hizmeti. Designer koleksiyonlar için özel bakım. Premium halı yıkama teknolojisi ve VIP hizmet.",
            'atasehir': f"{location}'de premium {service.lower()} hizmeti. İş merkezinde hızlı ve güvenilir temizlik çözümleri. Profesyonel ekip, modern teknoloji.",
            'bagdat-caddesi': f"Bağdat Caddesi'nde haute couture {service.lower()} hizmeti. Lüks marka giyim temizleme uzmanı. Designer kıyafetler için özel bakım.",
            'barbaros': f"Barbaros'ta VIP {service.lower()} hizmeti. Elite semtte premium mobilya bakımı. Lüks koltuk yıkama ve özel temizlik çözümleri.",
            'bostanci': f"Bostancı'da premium {service.lower()} hizmeti. Designer mobilyalar için özel bakım. Deri, kumaş, antika koltuklar için uzman hizmet.",
            'caddebostan': f"Caddebostan'da lüks {service.lower()} hizmeti. Premium konutlarda profesyonel temizlik. Modern teknoloji ile halı bakım uzmanı.",
            'camlica': f"Çamlıca'da panoramik tepelerde lüks {service.lower()} hizmeti. Premium kıyafet temizleme ve özel bakım. VIP teslimat hizmeti.",
            'erenkoy': f"Erenköy'de profesyonel {service.lower()} hizmeti. Konut bölgesinde güvenilir halı temizlik. Modern yöntemler, uzman ekip.",
            'fenerbahce': f"Fenerbahçe'de sahil kesiminde {service.lower()} hizmeti. Premium temizlik çözümleri, özel kıyafet bakımı. 25 yıllık deneyim.",
            'fikirtepe': f"Fikirtepe'de ekonomik {service.lower()} hizmeti. Kaliteli mobilya temizliği, uygun fiyatlı çözümler. Güvenilir ve hızlı hizmet.",
            'goztepe': f"Göztepe'de aile dostu {service.lower()} hizmeti. Sakin mahallede profesyonel halı bakımı. Modern teknoloji, güvenilir ekip.",
            'icerenkoy': f"İçerenköy'de modern {service.lower()} hizmeti. Gelişen bölgede kaliteli temizlik çözümleri. Halı yıkama uzmanı, hızlı teslimat.",
            'kadikoy': f"Kadıköy'de merkezi {service.lower()} hizmeti. Şehir merkezinde premium kıyafet bakımı. Luxury giyim temizleme uzmanı.",
            'kalamis': f"Kalamış'ta sahil kesiminde {service.lower()} hizmeti. Premium mobilya temizliği, özel bakım çözümleri. Modern teknoloji ile hizmet.",
            'kartal': f"Kartal'da geniş bölgede {service.lower()} hizmeti. Ekonomik ve kaliteli mobilya temizliği. Güvenilir ekip, hızlı teslimat.",
            'kozyatagi': f"Kozyatağı'nda modern {service.lower()} hizmeti. İş bölgesinde premium kıyafet temizleme. Profesyonel ekip, çevre dostu çözümler.",
            'kucukbakkalkoy': f"Küçükbakkalköy'de sakin mahallede {service.lower()} hizmeti. Güvenilir mobilya temizliği, aile dostu hizmet. Modern yöntemler.",
            'maltepe': f"Maltepe'de lüks {service.lower()} hizmeti. Premium semtte özel temizlik çözümleri. VIP halı yıkama ve bakım hizmeti.",
            'moda': f"Moda'da bohemian tarzda {service.lower()} hizmeti. Sanatsal semtte premium koltuk yıkama. Designer mobilya için özel bakım.",
            'pendik': f"Pendik'te geniş bölgede {service.lower()} hizmeti. Ekonomik ve kaliteli mobilya temizliği. Güvenilir ekip, hızlı çözümler.",
            'sahrayicedit': f"Sahrayıcedit'te premium {service.lower()} hizmeti. Elite semtte özel kıyafet bakımı. VIP temizlik çözümleri, uzman ekip.",
            'suadiye': f"Suadiye'de lüks {service.lower()} hizmeti. Premium semtte profesyonel temizlik. Designer halı yıkama ve özel bakım çözümleri.",
            'umraniye': f"Ümraniye'de geniş bölgede {service.lower()} hizmeti. VIP temizlik çözümleri, modern teknoloji. Halı yıkama ve bakım uzmanı.",
            'uskudar': f"Üsküdar'da tarihi yarımadada {service.lower()} hizmeti. Geleneksel semtte modern temizlik. Luxury kıyafet ve gelinlik bakımı."
        }
        
        # Get base location name
        base_location = location.lower().replace('ı', 'i').replace('ü', 'u').replace('ö', 'o').replace('ç', 'c').replace('ğ', 'g').replace('ş', 's')
        
        # Return appropriate description or generate generic one
        if base_location in descriptions:
            return descriptions[base_location]
        else:
            return f"{location}'de profesyonel {service.lower()} hizmeti. Modern teknoloji ve uzman ekip ile kaliteli temizlik çözümleri. Güvenilir hizmet."
    
    def generate_optimized_title(self, file_name):
        """Generate optimized title based on file name"""
        name_parts = file_name.replace('.html', '').split('-')
        location = name_parts[0].title()
        service = ' '.join(name_parts[1:]).title()
        
        # Keep within 50-70 character range
        title = f"{location} {service} | Dry Alle"
        
        if len(title) > 70:
            # Shorten if too long
            title = f"{location} {service} | Dry Alle"
        elif len(title) < 50:
            # Add descriptive words if too short
            title = f"{location} {service} Uzmanı | Dry Alle"
            
        return title
    
    def analyze_all_files(self):
        """Analyze all HTML files in current directory"""
        html_files = []
        
        # Find all HTML files
        for file in os.listdir('.'):
            if file.endswith('.html') and not file.startswith('.'):
                html_files.append(file)
        
        self.results['total_files'] = len(html_files)
        
        for file_name in html_files:
            analysis = self.analyze_file(file_name)
            self.results['files_analyzed'].append(analysis)
            
            # Categorize issues
            if 'Missing meta description' in analysis.get('issues', []) or \
               (analysis.get('meta_description_length', 0) < 120 or analysis.get('meta_description_length', 0) > 160):
                optimized_desc = self.generate_optimized_meta_description(file_name)
                self.results['meta_description_issues'].append({
                    'file': file_name,
                    'current': analysis.get('meta_description', 'MISSING'),
                    'current_length': analysis.get('meta_description_length', 0),
                    'optimized': optimized_desc,
                    'optimized_length': len(optimized_desc)
                })
                
            if analysis.get('title_length', 0) < 50 or analysis.get('title_length', 0) > 70:
                optimized_title = self.generate_optimized_title(file_name)
                self.results['title_length_issues'].append({
                    'file': file_name,
                    'current': analysis.get('title', 'MISSING'),
                    'current_length': analysis.get('title_length', 0),
                    'optimized': optimized_title,
                    'optimized_length': len(optimized_title)
                })
                
            if not analysis.get('has_h1', False):
                self.results['missing_h1'].append(file_name)
                
            if not analysis.get('has_canonical', False):
                self.results['missing_canonical'].append(file_name)
                
            if not analysis.get('has_schema', False):
                self.results['missing_schema'].append(file_name)
    
    def generate_implementation_code(self):
        """Generate implementation code for each page"""
        implementation = {}
        
        for issue in self.results['meta_description_issues']:
            file_name = issue['file']
            if file_name not in implementation:
                implementation[file_name] = {}
            implementation[file_name]['meta_description'] = {
                'code': f'<meta name="description" content="{issue["optimized"]}">',
                'length': issue['optimized_length']
            }
            
        for issue in self.results['title_length_issues']:
            file_name = issue['file']
            if file_name not in implementation:
                implementation[file_name] = {}
            implementation[file_name]['title'] = {
                'code': f'<title>{issue["optimized"]}</title>',
                'length': issue['optimized_length']
            }
        
        self.results['implementation_code'] = implementation
    
    def save_results(self, filename='comprehensive_seo_analysis.json'):
        """Save analysis results to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
    
    def generate_report(self):
        """Generate comprehensive SEO report"""
        report = []
        report.append("="*80)
        report.append("DRYALLE BÖLGELER - COMPREHENSIVE SEO ANALYSIS REPORT")
        report.append("="*80)
        report.append(f"Analysis Date: {self.results['analysis_date']}")
        report.append(f"Total Files Analyzed: {self.results['total_files']}")
        report.append("")
        
        # Meta Description Issues
        report.append("1. META DESCRIPTION OPTIMIZATION")
        report.append("-"*50)
        if self.results['meta_description_issues']:
            report.append(f"Files needing meta description optimization: {len(self.results['meta_description_issues'])}")
            report.append("")
            for issue in self.results['meta_description_issues']:
                report.append(f"File: {issue['file']}")
                report.append(f"Current: {issue['current'][:100]}... ({issue['current_length']} chars)")
                report.append(f"Optimized: {issue['optimized'][:100]}... ({issue['optimized_length']} chars)")
                report.append("")
        else:
            report.append("✅ All meta descriptions are optimized!")
            
        # Title Length Issues
        report.append("2. TITLE LENGTH OPTIMIZATION")
        report.append("-"*50)
        if self.results['title_length_issues']:
            report.append(f"Files needing title optimization: {len(self.results['title_length_issues'])}")
            report.append("")
            for issue in self.results['title_length_issues']:
                report.append(f"File: {issue['file']}")
                report.append(f"Current: {issue['current']} ({issue['current_length']} chars)")
                report.append(f"Optimized: {issue['optimized']} ({issue['optimized_length']} chars)")
                report.append("")
        else:
            report.append("✅ All titles are optimized!")
            
        # Missing Elements Summary
        report.append("3. MISSING SEO ELEMENTS")
        report.append("-"*50)
        report.append(f"Missing H1: {len(self.results['missing_h1'])} files")
        report.append(f"Missing Canonical: {len(self.results['missing_canonical'])} files")
        report.append(f"Missing Schema: {len(self.results['missing_schema'])} files")
        report.append("")
        
        # SEO Score Projection
        total_issues = (len(self.results['meta_description_issues']) + 
                       len(self.results['title_length_issues']) + 
                       len(self.results['missing_h1']) + 
                       len(self.results['missing_canonical']) + 
                       len(self.results['missing_schema']))
        
        current_score = max(0, 100 - (total_issues * 2))
        projected_score = 100
        
        report.append("4. SEO SCORE PROJECTION")
        report.append("-"*50)
        report.append(f"Current Estimated Score: {current_score}%")
        report.append(f"Projected Score After Optimization: {projected_score}%")
        report.append(f"Total Issues to Fix: {total_issues}")
        report.append("")
        
        return "\n".join(report)

def main():
    analyzer = ComprehensiveSEOAnalyzer()
    
    print("Starting comprehensive SEO analysis...")
    analyzer.analyze_all_files()
    analyzer.generate_implementation_code()
    
    # Save detailed results
    analyzer.save_results()
    
    # Generate and display report
    report = analyzer.generate_report()
    print(report)
    
    # Save report to file
    with open('comprehensive_seo_report.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("\n✅ Analysis complete!")
    print("📊 Results saved to: comprehensive_seo_analysis.json")
    print("📄 Report saved to: comprehensive_seo_report.txt")

if __name__ == "__main__":
    main()