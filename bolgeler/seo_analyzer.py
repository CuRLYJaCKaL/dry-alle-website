#!/usr/bin/env python3
"""
MIT-Level SEO Analysis Tool for DryAlle Regional Pages
Analyzes all 36 regional pages for Phase 1 optimization requirements
"""

import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class SEOAnalysis:
    file_name: str
    title: str
    title_length: int
    meta_description: str
    meta_description_length: int
    has_breadcrumb_schema: bool
    has_local_business_schema: bool
    character_encoding: str
    internal_links: List[str]
    issues: List[str]
    recommendations: List[str]

class DryAlleSEOAnalyzer:
    def __init__(self, directory_path: str):
        self.directory_path = Path(directory_path)
        self.results: List[SEOAnalysis] = []
        
    def extract_title(self, content: str) -> tuple[str, int]:
        """Extract title and calculate length"""
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            return title, len(title)
        return "", 0
    
    def extract_meta_description(self, content: str) -> tuple[str, int]:
        """Extract meta description and calculate length"""
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', content, re.IGNORECASE)
        if desc_match:
            description = desc_match.group(1).strip()
            return description, len(description)
        return "", 0
    
    def check_breadcrumb_schema(self, content: str) -> bool:
        """Check for BreadcrumbList schema presence"""
        return '"@type": "BreadcrumbList"' in content
    
    def check_local_business_schema(self, content: str) -> bool:
        """Check for LocalBusiness schema presence"""
        return '"@type": "LocalBusiness"' in content
    
    def extract_character_encoding(self, content: str) -> str:
        """Extract character encoding"""
        encoding_match = re.search(r'<meta\s+charset=["\']([^"\']*)["\']', content, re.IGNORECASE)
        if encoding_match:
            return encoding_match.group(1).upper()
        return "NOT_FOUND"
    
    def extract_internal_links(self, content: str) -> List[str]:
        """Extract internal links for consistency checking"""
        links = []
        # Extract navigation links
        nav_links = re.findall(r'<a\s+href=["\']([^"\']*)["\'][^>]*>', content, re.IGNORECASE)
        for link in nav_links:
            if link.startswith('../') or link.startswith('./') or not link.startswith('http'):
                links.append(link)
        return links[:10]  # Limit to first 10 for analysis
    
    def analyze_file(self, file_path: Path) -> SEOAnalysis:
        """Analyze a single HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return SEOAnalysis(
                file_name=file_path.name,
                title="ERROR_READING_FILE",
                title_length=0,
                meta_description="ERROR_READING_FILE",
                meta_description_length=0,
                has_breadcrumb_schema=False,
                has_local_business_schema=False,
                character_encoding="ERROR",
                internal_links=[],
                issues=[f"Failed to read file: {str(e)}"],
                recommendations=[]
            )
        
        # Extract all metrics
        title, title_length = self.extract_title(content)
        meta_desc, meta_desc_length = self.extract_meta_description(content)
        has_breadcrumb = self.check_breadcrumb_schema(content)
        has_local_business = self.check_local_business_schema(content)
        encoding = self.extract_character_encoding(content)
        internal_links = self.extract_internal_links(content)
        
        # Identify issues and recommendations
        issues = []
        recommendations = []
        
        # Title analysis
        if title_length == 0:
            issues.append("Missing title tag")
            recommendations.append("Add proper title tag")
        elif title_length > 70:
            issues.append(f"Title too long: {title_length} chars (>70)")
            recommendations.append(f"Shorten title to ≤70 characters (currently {title_length})")
        elif title_length < 30:
            issues.append(f"Title too short: {title_length} chars (<30)")
            recommendations.append(f"Expand title to 30-70 characters (currently {title_length})")
        
        # Meta description analysis
        if meta_desc_length == 0:
            issues.append("Missing meta description")
            recommendations.append("Add meta description (120-160 chars)")
        elif meta_desc_length < 120:
            issues.append(f"Meta description too short: {meta_desc_length} chars (<120)")
            recommendations.append(f"Expand meta description to 120-160 chars (currently {meta_desc_length})")
        elif meta_desc_length > 160:
            issues.append(f"Meta description too long: {meta_desc_length} chars (>160)")
            recommendations.append(f"Shorten meta description to ≤160 chars (currently {meta_desc_length})")
        
        # Schema analysis
        if not has_breadcrumb:
            issues.append("Missing BreadcrumbList schema")
            recommendations.append("Add BreadcrumbList structured data")
        
        if not has_local_business:
            issues.append("Missing LocalBusiness schema")
            recommendations.append("Add LocalBusiness structured data")
        
        # Character encoding
        if encoding != "UTF-8":
            issues.append(f"Non-UTF-8 encoding: {encoding}")
            recommendations.append("Set charset to UTF-8")
        
        return SEOAnalysis(
            file_name=file_path.name,
            title=title,
            title_length=title_length,
            meta_description=meta_desc,
            meta_description_length=meta_desc_length,
            has_breadcrumb_schema=has_breadcrumb,
            has_local_business_schema=has_local_business,
            character_encoding=encoding,
            internal_links=internal_links,
            issues=issues,
            recommendations=recommendations
        )
    
    def analyze_all_files(self) -> List[SEOAnalysis]:
        """Analyze all HTML files in the directory"""
        html_files = list(self.directory_path.glob("*.html"))
        
        for file_path in sorted(html_files):
            analysis = self.analyze_file(file_path)
            self.results.append(analysis)
        
        return self.results
    
    def generate_comprehensive_report(self) -> Dict:
        """Generate comprehensive analysis report"""
        if not self.results:
            self.analyze_all_files()
        
        # Summary statistics
        total_files = len(self.results)
        files_with_issues = len([r for r in self.results if r.issues])
        
        # Title analysis
        long_titles = [r for r in self.results if r.title_length > 70]
        short_titles = [r for r in self.results if r.title_length < 30]
        
        # Meta description analysis
        short_descriptions = [r for r in self.results if 0 < r.meta_description_length < 120]
        long_descriptions = [r for r in self.results if r.meta_description_length > 160]
        missing_descriptions = [r for r in self.results if r.meta_description_length == 0]
        
        # Schema analysis
        missing_breadcrumb = [r for r in self.results if not r.has_breadcrumb_schema]
        missing_local_business = [r for r in self.results if not r.has_local_business_schema]
        
        # Character encoding issues
        encoding_issues = [r for r in self.results if r.character_encoding != "UTF-8"]
        
        return {
            "summary": {
                "total_files_analyzed": total_files,
                "files_with_issues": files_with_issues,
                "clean_files": total_files - files_with_issues,
                "overall_health_score": round(((total_files - files_with_issues) / total_files) * 100, 1) if total_files > 0 else 0
            },
            "title_analysis": {
                "total_files": total_files,
                "long_titles_count": len(long_titles),
                "short_titles_count": len(short_titles),
                "optimal_titles_count": total_files - len(long_titles) - len(short_titles),
                "long_titles": [{"file": r.file_name, "length": r.title_length, "title": r.title} for r in long_titles],
                "short_titles": [{"file": r.file_name, "length": r.title_length, "title": r.title} for r in short_titles]
            },
            "meta_description_analysis": {
                "total_files": total_files,
                "missing_count": len(missing_descriptions),
                "short_count": len(short_descriptions),
                "long_count": len(long_descriptions),
                "optimal_count": total_files - len(missing_descriptions) - len(short_descriptions) - len(long_descriptions),
                "missing_descriptions": [{"file": r.file_name} for r in missing_descriptions],
                "short_descriptions": [{"file": r.file_name, "length": r.meta_description_length, "description": r.meta_description} for r in short_descriptions],
                "long_descriptions": [{"file": r.file_name, "length": r.meta_description_length, "description": r.meta_description} for r in long_descriptions]
            },
            "schema_analysis": {
                "missing_breadcrumb_count": len(missing_breadcrumb),
                "missing_local_business_count": len(missing_local_business),
                "missing_breadcrumb": [{"file": r.file_name} for r in missing_breadcrumb],
                "missing_local_business": [{"file": r.file_name} for r in missing_local_business]
            },
            "encoding_analysis": {
                "issues_count": len(encoding_issues),
                "encoding_issues": [{"file": r.file_name, "encoding": r.character_encoding} for r in encoding_issues]
            },
            "priority_fixes": self._generate_priority_list(),
            "detailed_results": [
                {
                    "file_name": r.file_name,
                    "title_length": r.title_length,
                    "meta_description_length": r.meta_description_length,
                    "has_breadcrumb_schema": r.has_breadcrumb_schema,
                    "has_local_business_schema": r.has_local_business_schema,
                    "issues_count": len(r.issues),
                    "issues": r.issues,
                    "recommendations": r.recommendations
                } for r in self.results
            ]
        }
    
    def _generate_priority_list(self) -> List[Dict]:
        """Generate priority list for fixes based on SEO impact"""
        priority_fixes = []
        
        for result in self.results:
            if not result.issues:
                continue
                
            priority_score = 0
            fix_categories = []
            
            # High priority: Missing critical elements
            if not result.has_breadcrumb_schema:
                priority_score += 10
                fix_categories.append("Missing BreadcrumbList Schema")
            
            if result.meta_description_length == 0:
                priority_score += 9
                fix_categories.append("Missing Meta Description")
            
            if result.title_length > 70:
                priority_score += 8
                fix_categories.append("Title Too Long")
            
            # Medium priority: Suboptimal lengths
            if result.meta_description_length > 160:
                priority_score += 6
                fix_categories.append("Meta Description Too Long")
            
            if result.meta_description_length < 120 and result.meta_description_length > 0:
                priority_score += 5
                fix_categories.append("Meta Description Too Short")
            
            if result.title_length < 30:
                priority_score += 4
                fix_categories.append("Title Too Short")
            
            # Lower priority
            if not result.has_local_business_schema:
                priority_score += 3
                fix_categories.append("Missing LocalBusiness Schema")
            
            if result.character_encoding != "UTF-8":
                priority_score += 2
                fix_categories.append("Character Encoding Issue")
            
            if priority_score > 0:
                priority_fixes.append({
                    "file_name": result.file_name,
                    "priority_score": priority_score,
                    "fix_categories": fix_categories,
                    "total_issues": len(result.issues)
                })
        
        # Sort by priority score (highest first)
        priority_fixes.sort(key=lambda x: x["priority_score"], reverse=True)
        
        return priority_fixes

def main():
    # Analyze all files
    analyzer = DryAlleSEOAnalyzer("/Users/macos/Documents/Projeler/DryAlle/bolgeler")
    report = analyzer.generate_comprehensive_report()
    
    # Save comprehensive report
    with open("/Users/macos/Documents/Projeler/DryAlle/bolgeler/seo_analysis_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    return report

if __name__ == "__main__":
    main()