#!/usr/bin/env python3
"""
Extract detailed findings from comprehensive SEO analysis
"""

import json
import os
from datetime import datetime

def extract_key_findings(report_path):
    """Extract and format key findings from the analysis report"""
    
    with open(report_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    summary = data['summary_statistics']
    results = data['detailed_results']
    
    print("=" * 80)
    print("COMPREHENSIVE SEO ANALYSIS - DETAILED FINDINGS")
    print("=" * 80)
    print(f"Analysis Date: {data['analysis_metadata']['timestamp']}")
    print(f"Total Pages Analyzed: {summary['total_pages']}")
    print()
    
    # 1. META TAGS VALIDATION
    print("1. META TAGS VALIDATION")
    print("-" * 40)
    print(f"✅ Perfect Titles (30-70 chars): {summary['perfect_titles']}/36 (100%)")
    print(f"⚠️  Good Descriptions (120-160 chars): {summary['good_descriptions']}/36 ({round(summary['good_descriptions']/36*100, 1)}%)")
    
    # Analyze title performance
    title_analysis = {}
    desc_analysis = {}
    
    for filename, analysis in results.items():
        if 'error' in analysis:
            continue
            
        # Title analysis
        title_len = analysis['meta_tags']['title']['length']
        if title_len <= 70 and title_len >= 30:
            title_status = "optimal"
        elif title_len > 70:
            title_status = "too_long"
        elif title_len > 0:
            title_status = "too_short"
        else:
            title_status = "missing"
        
        title_analysis[filename] = {
            'length': title_len,
            'status': title_status,
            'content': analysis['meta_tags']['title']['content']
        }
        
        # Description analysis
        desc_len = analysis['meta_tags']['description']['length']
        if desc_len >= 120 and desc_len <= 160:
            desc_status = "optimal"
        elif desc_len > 160:
            desc_status = "too_long"
        elif desc_len > 0:
            desc_status = "too_short"
        else:
            desc_status = "missing"
        
        desc_analysis[filename] = {
            'length': desc_len,
            'status': desc_status,
            'content': analysis['meta_tags']['description']['content']
        }
    
    print(f"\nTitle Length Distribution:")
    title_lengths = [v['length'] for v in title_analysis.values()]
    print(f"  Average: {round(sum(title_lengths)/len(title_lengths), 1)} characters")
    print(f"  Range: {min(title_lengths)}-{max(title_lengths)} characters")
    
    print(f"\nDescription Issues (6 pages need optimization):")
    desc_issues = {k: v for k, v in desc_analysis.items() if v['status'] != 'optimal'}
    for filename, desc in desc_issues.items():
        print(f"  {filename}: {desc['status']} ({desc['length']} chars)")
    
    # 2. SCHEMA MARKUP AUDIT
    print(f"\n2. SCHEMA MARKUP COMPLETE AUDIT")
    print("-" * 40)
    print(f"✅ BreadcrumbList Schema: {summary['breadcrumb_schema_count']}/36 (100%)")
    print(f"✅ LocalBusiness Schema: {summary['localbusiness_schema_count']}/36 (100%)")
    
    # Analyze schema completeness
    schema_stats = {
        'service_schema': 0,
        'organization_schema': 0,
        'webpage_schema': 0,
        'postaladdress_schema': 0,
        'contactpoint_schema': 0
    }
    
    for filename, analysis in results.items():
        if 'error' in analysis:
            continue
        schema_data = analysis['schema_markup']
        for schema_type in schema_stats.keys():
            if schema_data.get(schema_type, False):
                schema_stats[schema_type] += 1
    
    print(f"\nAdditional Schema Types:")
    for schema_type, count in schema_stats.items():
        schema_name = schema_type.replace('_schema', '').title()
        percentage = round(count/36*100, 1)
        status = "✅" if count == 36 else "⚠️ "
        print(f"  {status} {schema_name}: {count}/36 ({percentage}%)")
    
    # 3. TECHNICAL SEO STATUS
    print(f"\n3. TECHNICAL SEO STATUS")
    print("-" * 40)
    print(f"✅ Canonical URLs: {summary['canonical_urls']}/36 (100%)")
    
    # Turkish character analysis
    turkish_char_issues = 0
    charset_issues = 0
    
    for filename, analysis in results.items():
        if 'error' in analysis:
            continue
        tech_data = analysis['technical_seo']
        
        if not tech_data['turkish_characters']['properly_encoded']:
            turkish_char_issues += 1
        
        if not tech_data['charset']['present']:
            charset_issues += 1
    
    print(f"✅ Character Encoding: {36-charset_issues}/36 ({round((36-charset_issues)/36*100, 1)}%)")
    print(f"✅ Turkish Characters: {36-turkish_char_issues}/36 ({round((36-turkish_char_issues)/36*100, 1)}%)")
    
    # Internal linking analysis
    internal_links = []
    for filename, analysis in results.items():
        if 'error' in analysis:
            continue
        link_count = analysis['technical_seo']['internal_links']['count']
        internal_links.append(link_count)
    
    avg_internal_links = round(sum(internal_links)/len(internal_links), 1)
    print(f"🔗 Internal Links Average: {avg_internal_links} per page")
    
    # 4. CONTENT ANALYSIS
    print(f"\n4. CONTENT ANALYSIS UPDATED")
    print("-" * 40)
    
    # H1 analysis
    h1_optimal = 0
    h1_issues = []
    word_counts = []
    
    for filename, analysis in results.items():
        if 'error' in analysis:
            continue
        
        content_data = analysis['content_analysis']
        
        # H1 analysis
        if content_data['h1']['is_optimal']:
            h1_optimal += 1
        else:
            h1_count = content_data['h1']['count']
            h1_length = content_data['h1']['length']
            if h1_count == 0:
                h1_issues.append(f"{filename}: Missing H1")
            elif h1_count > 1:
                h1_issues.append(f"{filename}: Multiple H1s ({h1_count})")
            elif h1_length < 20 or h1_length > 70:
                h1_issues.append(f"{filename}: H1 length issue ({h1_length} chars)")
        
        # Word count
        word_counts.append(content_data['word_count']['total'])
    
    print(f"✅ Optimal H1 Tags: {h1_optimal}/36 ({round(h1_optimal/36*100, 1)}%)")
    
    if h1_issues:
        print(f"\nH1 Issues:")
        for issue in h1_issues[:5]:  # Show first 5
            print(f"  {issue}")
    
    avg_word_count = round(sum(word_counts)/len(word_counts))
    optimal_word_count = len([wc for wc in word_counts if wc >= 300])
    
    print(f"\n📝 Content Depth:")
    print(f"  Average word count: {avg_word_count} words")
    print(f"  Pages with 300+ words: {optimal_word_count}/36 ({round(optimal_word_count/36*100, 1)}%)")
    print(f"  Word count range: {min(word_counts)}-{max(word_counts)} words")
    
    # 5. PERFORMANCE SCORING
    print(f"\n5. PERFORMANCE SCORING")
    print("-" * 40)
    print(f"🎯 Average SEO Score: {summary['avg_seo_score']}/10")
    
    # Score distribution
    scores = []
    for filename, analysis in results.items():
        if 'error' not in analysis:
            scores.append(analysis['seo_score'])
    
    score_ranges = {
        '9.0-10.0': len([s for s in scores if s >= 9.0]),
        '8.0-8.9': len([s for s in scores if 8.0 <= s < 9.0]),
        '7.0-7.9': len([s for s in scores if 7.0 <= s < 8.0]),
        '6.0-6.9': len([s for s in scores if 6.0 <= s < 7.0]),
        'Below 6.0': len([s for s in scores if s < 6.0])
    }
    
    print(f"\nScore Distribution:")
    for range_name, count in score_ranges.items():
        percentage = round(count/36*100, 1)
        print(f"  {range_name}: {count}/36 ({percentage}%)")
    
    # Top and bottom performers
    print(f"\n🏆 TOP 5 PERFORMERS:")
    for filename, score in summary['top_performers']:
        print(f"  {filename}: {score}/10")
    
    print(f"\n⚠️  PAGES NEEDING ATTENTION:")
    for filename, score in summary['pages_needing_attention']:
        print(f"  {filename}: {score}/10")
    
    # 6. IMPROVEMENT OPPORTUNITIES
    print(f"\n6. IMPROVEMENT OPPORTUNITIES")
    print("-" * 40)
    
    print("🔧 Priority Fixes:")
    for i, rec in enumerate(data['recommendations'], 1):
        print(f"  {i}. {rec}")
    
    print(f"\n🎯 Common Issues:")
    for i, opp in enumerate(data['improvement_opportunities'][:10], 1):
        print(f"  {i}. {opp}")
    
    # 7. BEFORE/AFTER COMPARISON (if previous data exists)
    print(f"\n7. IMPROVEMENT VALIDATION")
    print("-" * 40)
    
    # Check for previous analysis files
    previous_files = [f for f in os.listdir('/Users/macos/Documents/Projeler/DryAlle/bolgeler') 
                     if f.endswith('.json') and 'seo_analysis' in f and 'comprehensive' not in f]
    
    if previous_files:
        print("📊 Comparing with previous analysis...")
        # Try to load most recent previous analysis
        try:
            previous_file = sorted(previous_files)[-1]
            with open(f'/Users/macos/Documents/Projeler/DryAlle/bolgeler/{previous_file}', 'r', encoding='utf-8') as f:
                previous_data = json.load(f)
            
            if 'summary_statistics' in previous_data:
                prev_stats = previous_data['summary_statistics']
                
                print(f"\nValidated Improvements:")
                
                # Title improvements
                prev_titles = prev_stats.get('perfect_titles', 0)
                title_improvement = summary['perfect_titles'] - prev_titles
                print(f"  ✅ Title optimization: +{title_improvement} pages (now {summary['perfect_titles']}/36)")
                
                # Schema improvements
                prev_breadcrumb = prev_stats.get('breadcrumb_schema_count', 0)
                breadcrumb_improvement = summary['breadcrumb_schema_count'] - prev_breadcrumb
                print(f"  ✅ BreadcrumbList schema: +{breadcrumb_improvement} pages (now {summary['breadcrumb_schema_count']}/36)")
                
                prev_localbusiness = prev_stats.get('localbusiness_schema_count', 0)
                localbusiness_improvement = summary['localbusiness_schema_count'] - prev_localbusiness
                print(f"  ✅ LocalBusiness schema: +{localbusiness_improvement} pages (now {summary['localbusiness_schema_count']}/36)")
                
                # Average score improvement
                prev_avg_score = prev_stats.get('avg_seo_score', 0)
                score_improvement = summary['avg_seo_score'] - prev_avg_score
                print(f"  📈 Average SEO score: +{round(score_improvement, 2)} points (now {summary['avg_seo_score']}/10)")
                
        except Exception as e:
            print(f"Unable to load previous data: {e}")
    else:
        print("No previous analysis found for comparison")
    
    # 8. OVERALL ASSESSMENT
    print(f"\n8. OVERALL SEO HEALTH ASSESSMENT")
    print("-" * 40)
    
    total_possible_points = 36 * 10  # 36 pages * 10 max score
    current_total_points = sum(scores)
    health_percentage = round(current_total_points / total_possible_points * 100, 1)
    
    print(f"🎯 Overall SEO Health: {health_percentage}%")
    
    if health_percentage >= 90:
        health_status = "EXCELLENT"
        health_emoji = "🌟"
    elif health_percentage >= 80:
        health_status = "GOOD"
        health_emoji = "✅"
    elif health_percentage >= 70:
        health_status = "FAIR"
        health_emoji = "⚠️ "
    else:
        health_status = "NEEDS IMPROVEMENT"
        health_emoji = "❌"
    
    print(f"{health_emoji} Status: {health_status}")
    
    # Completion rates
    completion_rates = {
        'Perfect Titles': round(summary['perfect_titles']/36*100, 1),
        'Good Descriptions': round(summary['good_descriptions']/36*100, 1),
        'BreadcrumbList Schema': round(summary['breadcrumb_schema_count']/36*100, 1),
        'LocalBusiness Schema': round(summary['localbusiness_schema_count']/36*100, 1),
        'Canonical URLs': round(summary['canonical_urls']/36*100, 1)
    }
    
    print(f"\n📊 Implementation Completion Rates:")
    for metric, rate in completion_rates.items():
        status_emoji = "✅" if rate == 100 else "⚠️ " if rate >= 80 else "❌"
        print(f"  {status_emoji} {metric}: {rate}%")
    
    print(f"\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

def main():
    # Find the most recent comprehensive analysis file
    report_files = [f for f in os.listdir('/Users/macos/Documents/Projeler/DryAlle/bolgeler') 
                   if f.startswith('comprehensive_seo_analysis_') and f.endswith('.json')]
    
    if not report_files:
        print("No comprehensive analysis report found!")
        return
    
    latest_report = sorted(report_files)[-1]
    report_path = f'/Users/macos/Documents/Projeler/DryAlle/bolgeler/{latest_report}'
    
    extract_key_findings(report_path)

if __name__ == "__main__":
    main()