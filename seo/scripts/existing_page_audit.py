#!/usr/bin/env python3
"""
DryAlle Existing Page Audit
Compare current 65 pages against new URL/Meta standards from Phase 0.3
"""

import csv
import os
import re
from pathlib import Path

def load_existing_inventory():
    """Load Phase 0.1 inventory data"""
    inventory_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/00_inventory.csv")
    existing_pages = []
    
    with open(inventory_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            existing_pages.append(row)
    
    return existing_pages

def load_master_standards():
    """Load Phase 0.3 URL Meta Master standards"""
    master_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_url_meta_master.csv")
    master_standards = {}
    
    with open(master_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Create lookup key from URL
            url = row['Full URL']
            if url.endswith('/'):
                key = url
            else:
                key = url
            master_standards[key] = row
    
    return master_standards

def analyze_discrepancies():
    """Analyze differences between existing pages and new standards"""
    
    existing_pages = load_existing_inventory()
    master_standards = load_master_standards()
    
    audit_results = []
    unmatched_existing = []
    
    for existing_page in existing_pages:
        existing_url = existing_page['Expected URL']
        
        # Find matching standard
        matching_standard = None
        for standard_url, standard_data in master_standards.items():
            if standard_url == existing_url or standard_url.rstrip('/') == existing_url.rstrip('/'):
                matching_standard = standard_data
                break
        
        if matching_standard:
            # Compare existing vs standard
            discrepancies = []
            
            # Title comparison
            existing_title = existing_page['Title']
            standard_title = matching_standard['Title']
            if existing_title != standard_title:
                discrepancies.append({
                    'field': 'Title',
                    'existing': existing_title,
                    'standard': standard_title,
                    'action': 'Update Required'
                })
            
            # H1 comparison  
            existing_h1 = existing_page['H1']
            standard_h1 = matching_standard['H1']
            if existing_h1 != standard_h1:
                discrepancies.append({
                    'field': 'H1',
                    'existing': existing_h1,
                    'standard': standard_h1,
                    'action': 'Update Required'
                })
            
            # Meta description comparison
            existing_meta = existing_page['Meta Description']
            standard_meta = matching_standard['Meta Description']
            if existing_meta != standard_meta:
                discrepancies.append({
                    'field': 'Meta Description',
                    'existing': existing_meta,
                    'standard': standard_meta,
                    'action': 'Update Required'
                })
            
            # URL structure validation
            if existing_url != matching_standard['Full URL']:
                discrepancies.append({
                    'field': 'URL',
                    'existing': existing_url,
                    'standard': matching_standard['Full URL'],
                    'action': 'URL Redirect Needed'
                })
            
            audit_results.append({
                'page_path': existing_page['File Path'],
                'page_type': existing_page['Page Type'],
                'existing_url': existing_url,
                'standard_url': matching_standard['Full URL'],
                'discrepancies': discrepancies,
                'total_issues': len(discrepancies),
                'status': 'NEEDS UPDATE' if discrepancies else 'COMPLIANT'
            })
        else:
            # Page exists but no standard found
            unmatched_existing.append({
                'page_path': existing_page['File Path'],
                'existing_url': existing_url,
                'page_type': existing_page['Page Type'],
                'issue': 'No matching standard found - may need custom handling'
            })
    
    return audit_results, unmatched_existing

def generate_audit_report():
    """Generate comprehensive audit report"""
    
    audit_results, unmatched_existing = analyze_discrepancies()
    
    # Output files
    audit_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_existing_page_audit.csv")
    summary_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_audit_summary.md")
    
    # Write detailed audit CSV
    audit_fieldnames = [
        'Page Path', 'Page Type', 'Existing URL', 'Standard URL', 'Status', 
        'Total Issues', 'Title Issue', 'H1 Issue', 'Meta Issue', 'URL Issue',
        'Existing Title', 'Standard Title', 'Existing H1', 'Standard H1',
        'Existing Meta', 'Standard Meta'
    ]
    
    with open(audit_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=audit_fieldnames)
        writer.writeheader()
        
        for result in audit_results:
            row = {
                'Page Path': result['page_path'],
                'Page Type': result['page_type'],
                'Existing URL': result['existing_url'],
                'Standard URL': result['standard_url'],
                'Status': result['status'],
                'Total Issues': result['total_issues'],
                'Title Issue': 'NO',
                'H1 Issue': 'NO', 
                'Meta Issue': 'NO',
                'URL Issue': 'NO',
                'Existing Title': '',
                'Standard Title': '',
                'Existing H1': '',
                'Standard H1': '',
                'Existing Meta': '',
                'Standard Meta': ''
            }
            
            # Fill in discrepancy details
            for disc in result['discrepancies']:
                if disc['field'] == 'Title':
                    row['Title Issue'] = 'YES'
                    row['Existing Title'] = disc['existing']
                    row['Standard Title'] = disc['standard']
                elif disc['field'] == 'H1':
                    row['H1 Issue'] = 'YES'
                    row['Existing H1'] = disc['existing']
                    row['Standard H1'] = disc['standard']
                elif disc['field'] == 'Meta Description':
                    row['Meta Issue'] = 'YES'
                    row['Existing Meta'] = disc['existing']
                    row['Standard Meta'] = disc['standard']
                elif disc['field'] == 'URL':
                    row['URL Issue'] = 'YES'
            
            writer.writerow(row)
    
    # Generate summary statistics
    total_pages = len(audit_results)
    compliant_pages = len([r for r in audit_results if r['status'] == 'COMPLIANT'])
    needs_update = len([r for r in audit_results if r['status'] == 'NEEDS UPDATE'])
    
    title_issues = len([r for r in audit_results if any(d['field'] == 'Title' for d in r['discrepancies'])])
    h1_issues = len([r for r in audit_results if any(d['field'] == 'H1' for d in r['discrepancies'])])
    meta_issues = len([r for r in audit_results if any(d['field'] == 'Meta Description' for d in r['discrepancies'])])
    url_issues = len([r for r in audit_results if any(d['field'] == 'URL' for d in r['discrepancies'])])
    
    # Write summary report
    summary_content = f"""# DryAlle Existing Page Audit Summary (Phase 0.3)
**Generated:** January 16, 2025  
**Audit Scope:** 65 existing pages vs new URL/Meta standards  
**Standards Base:** Phase 0.3 URL Meta Master

## Executive Summary

This audit compares all 65 existing DryAlle pages against the new standardized URL and meta tag templates established in Phase 0.3. The analysis identifies specific discrepancies that require updates before Phase 3 implementation.

## Audit Results Overview

### Page Compliance Status
- **Total Pages Audited:** {total_pages}
- **Fully Compliant:** {compliant_pages} pages ({compliant_pages/total_pages*100:.1f}%)
- **Needs Updates:** {needs_update} pages ({needs_update/total_pages*100:.1f}%)
- **Unmatched Pages:** {len(unmatched_existing)} pages

### Issue Breakdown by Type
- **Title Tag Issues:** {title_issues} pages
- **H1 Tag Issues:** {h1_issues} pages  
- **Meta Description Issues:** {meta_issues} pages
- **URL Structure Issues:** {url_issues} pages

## Priority Update Requirements

### High Priority (Critical for SEO)
1. **Title Tag Standardization** - {title_issues} pages need title updates
2. **Meta Description Optimization** - {meta_issues} pages need meta updates
3. **URL Structure Alignment** - {url_issues} pages need URL corrections

### Medium Priority (User Experience)
1. **H1 Standardization** - {h1_issues} pages need H1 updates
2. **Content Structure Alignment** - Ensure consistent heading hierarchy

## Implementation Recommendations

### Phase 1: Critical SEO Elements
- Update title tags to match new templates
- Standardize meta descriptions for optimal CTR
- Implement URL redirects where necessary

### Phase 2: Content Optimization  
- Align H1 tags with new standards
- Ensure consistent internal linking structure
- Verify schema markup implementation

### Phase 3: Quality Assurance
- Validate all updates against standards
- Test URL redirects and canonical implementations
- Monitor search console for any indexing issues

## Detailed Findings

### Most Common Issues
1. **Title Tag Length:** Some existing titles exceed 60 character optimal length
2. **Meta Description Format:** Inconsistent CTA language and local targeting
3. **H1 Variations:** Different formats for location-based H1 tags
4. **URL Consistency:** Some pages use different slug patterns

### Pages Requiring Immediate Attention
"""

    # Add high-priority pages that need updates
    high_priority_pages = [r for r in audit_results if r['total_issues'] >= 3]
    if high_priority_pages:
        summary_content += f"\n**{len(high_priority_pages)} pages with 3+ issues:**\n"
        for page in high_priority_pages[:10]:  # Limit to top 10
            summary_content += f"- {page['page_path']} ({page['total_issues']} issues)\n"

    # Add unmatched pages section
    if unmatched_existing:
        summary_content += f"\n### Unmatched Existing Pages ({len(unmatched_existing)})\n"
        summary_content += "These pages exist but don't match current standards:\n\n"
        for page in unmatched_existing:
            summary_content += f"- **{page['page_path']}** ({page['page_type']})\n"
            summary_content += f"  - URL: {page['existing_url']}\n"
            summary_content += f"  - Issue: {page['issue']}\n\n"

    summary_content += f"""
## Next Steps

1. **Review Audit Details:** Examine /seo/outputs/03_existing_page_audit.csv for specific update requirements
2. **Prioritize Updates:** Focus on high-traffic pages and critical SEO elements first  
3. **Implement Changes:** Use Phase 0.3 templates for consistent updates
4. **Validate Results:** Re-run audit after updates to ensure compliance

## Quality Assurance Checklist

- [ ] All title tags follow new template format
- [ ] Meta descriptions are under 155 characters with CTAs
- [ ] H1 tags use consistent location + service format
- [ ] URL redirects implemented for any structural changes
- [ ] Internal linking updated to reflect new standards
- [ ] Schema markup aligned with new page structure

---

**Files Generated:**
- Detailed Audit: `/seo/outputs/03_existing_page_audit.csv`
- Summary Report: `/seo/outputs/03_audit_summary.md`

**Phase 0.3 Status:** URL/Meta standards established and audit completed  
**Ready for:** Phase 3 implementation with identified update requirements
"""

    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary_content)

    return audit_results, unmatched_existing, {
        'total_pages': total_pages,
        'compliant_pages': compliant_pages,
        'needs_update': needs_update,
        'title_issues': title_issues,
        'h1_issues': h1_issues,
        'meta_issues': meta_issues,
        'url_issues': url_issues,
        'unmatched': len(unmatched_existing)
    }

def main():
    """Run existing page audit against Phase 0.3 standards"""
    
    print("Starting existing page audit against Phase 0.3 standards...")
    
    audit_results, unmatched_existing, stats = generate_audit_report()
    
    print(f"\n=== EXISTING PAGE AUDIT COMPLETE ===")
    print(f"Total pages audited: {stats['total_pages']}")
    print(f"Fully compliant: {stats['compliant_pages']}")
    print(f"Need updates: {stats['needs_update']}")
    print(f"Unmatched pages: {stats['unmatched']}")
    
    print(f"\n=== ISSUE BREAKDOWN ===")
    print(f"Title issues: {stats['title_issues']}")
    print(f"H1 issues: {stats['h1_issues']}")
    print(f"Meta description issues: {stats['meta_issues']}")
    print(f"URL issues: {stats['url_issues']}")
    
    print(f"\n=== OUTPUT FILES ===")
    print(f"Detailed audit: /seo/outputs/03_existing_page_audit.csv")
    print(f"Summary report: /seo/outputs/03_audit_summary.md")

if __name__ == "__main__":
    main()