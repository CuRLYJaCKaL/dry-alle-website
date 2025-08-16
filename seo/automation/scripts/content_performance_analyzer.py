#!/usr/bin/env python3
"""
Content Performance Analyzer
Analyzes blog and page performance, suggests optimizations
"""

import requests
import json
from datetime import datetime, timedelta
from collections import defaultdict

class ContentPerformanceAnalyzer:
    def __init__(self):
        self.base_url = "https://dryallekurutemizleme.com"
        self.blog_posts = []
        self.service_pages = []
        self.performance_data = defaultdict(dict)
    
    def analyze_blog_performance(self):
        """Analyze blog post performance"""
        # This would integrate with Google Analytics API
        # For demo, we'll simulate the data
        
        blog_performance = [
            {
                'url': '/blog/2025-01/2025-yilinda-istanbul-kuru-temizleme-trendleri.html',
                'title': '2025 Yılında İstanbul Kuru Temizleme Trendleri',
                'pageviews': 1250,
                'unique_visitors': 980,
                'avg_time_on_page': 245,  # seconds
                'bounce_rate': 0.32,
                'conversions': 15,
                'publication_date': '2025-01-01',
                'last_updated': '2025-01-01'
            },
            {
                'url': '/blog/2025-01/gelinlik-temizleme-ultimate-rehber-2025.html', 
                'title': 'Gelinlik Temizleme Ultimate Rehber 2025',
                'pageviews': 2180,
                'unique_visitors': 1650,
                'avg_time_on_page': 380,
                'bounce_rate': 0.25,
                'conversions': 28,
                'publication_date': '2025-01-15',
                'last_updated': '2025-01-15'
            },
            {
                'url': '/blog/2025-02/istanbul-elit-semtlerde-tekstil-bakimi.html',
                'title': 'İstanbul Elit Semtlerde Tekstil Bakımı', 
                'pageviews': 890,
                'unique_visitors': 720,
                'avg_time_on_page': 190,
                'bounce_rate': 0.45,
                'conversions': 8,
                'publication_date': '2025-02-01',
                'last_updated': '2025-02-01'
            }
        ]
        
        return blog_performance
    
    def identify_content_gaps(self, performance_data):
        """Identify content that needs optimization"""
        gaps = {
            'low_performing': [],
            'high_bounce_rate': [],
            'low_conversion': [],
            'needs_update': []
        }
        
        for content in performance_data:
            # Low performing (less than average pageviews)
            avg_pageviews = sum(c['pageviews'] for c in performance_data) / len(performance_data)
            if content['pageviews'] < avg_pageviews * 0.7:
                gaps['low_performing'].append(content)
            
            # High bounce rate (over 40%)
            if content['bounce_rate'] > 0.40:
                gaps['high_bounce_rate'].append(content)
            
            # Low conversion (less than 1% conversion rate)
            conversion_rate = content['conversions'] / content['unique_visitors']
            if conversion_rate < 0.01:
                gaps['low_conversion'].append(content)
            
            # Needs update (older than 6 months)
            last_update = datetime.strptime(content['last_updated'], '%Y-%m-%d')
            if (datetime.now() - last_update).days > 180:
                gaps['needs_update'].append(content)
        
        return gaps
    
    def suggest_optimizations(self, content_gaps):
        """Suggest specific optimizations for identified gaps"""
        suggestions = []
        
        for content in content_gaps['low_performing']:
            suggestions.append({
                'url': content['url'],
                'issue': 'Low Performance',
                'suggestions': [
                    'Improve title SEO optimization',
                    'Add more internal links',
                    'Update with current information',
                    'Enhance meta description',
                    'Add more engaging visuals'
                ]
            })
        
        for content in content_gaps['high_bounce_rate']:
            suggestions.append({
                'url': content['url'],
                'issue': 'High Bounce Rate',
                'suggestions': [
                    'Improve page loading speed',
                    'Add engaging introduction',
                    'Include table of contents',
                    'Add related content recommendations',
                    'Optimize for mobile experience'
                ]
            })
        
        for content in content_gaps['low_conversion']:
            suggestions.append({
                'url': content['url'],
                'issue': 'Low Conversion',
                'suggestions': [
                    'Add stronger call-to-action buttons',
                    'Include customer testimonials',
                    'Add urgency elements',
                    'Improve trust signals',
                    'Optimize form placement'
                ]
            })
        
        for content in content_gaps['needs_update']:
            suggestions.append({
                'url': content['url'],
                'issue': 'Content Outdated',
                'suggestions': [
                    'Update statistics and data',
                    'Refresh examples and case studies',
                    'Add current industry trends',
                    'Update pricing information',
                    'Refresh meta tags'
                ]
            })
        
        return suggestions
    
    def generate_content_report(self):
        """Generate comprehensive content performance report"""
        # Analyze performance
        blog_performance = self.analyze_blog_performance()
        
        # Identify gaps
        content_gaps = self.identify_content_gaps(blog_performance)
        
        # Generate suggestions
        optimization_suggestions = self.suggest_optimizations(content_gaps)
        
        # Calculate overall metrics
        total_pageviews = sum(c['pageviews'] for c in blog_performance)
        total_conversions = sum(c['conversions'] for c in blog_performance)
        avg_bounce_rate = sum(c['bounce_rate'] for c in blog_performance) / len(blog_performance)
        
        report = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'summary': {
                'total_posts_analyzed': len(blog_performance),
                'total_pageviews': total_pageviews,
                'total_conversions': total_conversions,
                'overall_conversion_rate': round(total_conversions / sum(c['unique_visitors'] for c in blog_performance) * 100, 2),
                'average_bounce_rate': round(avg_bounce_rate * 100, 1)
            },
            'top_performing': sorted(blog_performance, key=lambda x: x['pageviews'], reverse=True)[:3],
            'content_gaps': {
                'low_performing_count': len(content_gaps['low_performing']),
                'high_bounce_rate_count': len(content_gaps['high_bounce_rate']),
                'low_conversion_count': len(content_gaps['low_conversion']),
                'needs_update_count': len(content_gaps['needs_update'])
            },
            'optimization_suggestions': optimization_suggestions,
            'priority_actions': self.prioritize_actions(optimization_suggestions)
        }
        
        return report
    
    def prioritize_actions(self, suggestions):
        """Prioritize optimization actions by impact"""
        priority_matrix = {
            'Low Conversion': 3,  # High impact
            'High Bounce Rate': 2,  # Medium impact
            'Low Performance': 2,  # Medium impact  
            'Content Outdated': 1   # Low impact
        }
        
        prioritized = sorted(suggestions, key=lambda x: priority_matrix.get(x['issue'], 0), reverse=True)
        
        return prioritized[:5]  # Top 5 priority actions

def main():
    analyzer = ContentPerformanceAnalyzer()
    
    print("📊 Starting content performance analysis...")
    
    # Generate report
    report = analyzer.generate_content_report()
    
    # Save report
    with open(f'/tmp/content_performance_report_{report["date"]}.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    # Print summary
    print(f"📈 Content Performance Summary:")
    print(f"   Total Posts Analyzed: {report['summary']['total_posts_analyzed']}")
    print(f"   Total Pageviews: {report['summary']['total_pageviews']:,}")
    print(f"   Total Conversions: {report['summary']['total_conversions']}")
    print(f"   Overall Conversion Rate: {report['summary']['overall_conversion_rate']}%")
    print(f"   Average Bounce Rate: {report['summary']['average_bounce_rate']}%")
    
    print(f"\n🎯 Content Issues Identified:")
    print(f"   Low Performing: {report['content_gaps']['low_performing_count']} posts")
    print(f"   High Bounce Rate: {report['content_gaps']['high_bounce_rate_count']} posts")
    print(f"   Low Conversion: {report['content_gaps']['low_conversion_count']} posts")
    print(f"   Needs Update: {report['content_gaps']['needs_update_count']} posts")
    
    print(f"\n⚡ Top Priority Actions:")
    for i, action in enumerate(report['priority_actions'], 1):
        print(f"   {i}. {action['issue']}: {action['url']}")

if __name__ == "__main__":
    main()
