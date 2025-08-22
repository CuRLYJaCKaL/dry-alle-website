#!/usr/bin/env python3
"""
Final MIT-Level SEO Analysis Tool for DryAlle Regional Pages
Provides accurate analysis of all 36 regional pages
"""

import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class FinalSEOAnalysis:
    file_name: str
    title: str
    title_length: int
    meta_description: str
    meta_description_length: int
    has_breadcrumb_schema: bool
    has_local_business_schema: bool
    character_encoding: str
    issues: List[str]
    recommendations: List[str]
    priority_score: int
    seo_health_score: int

class FinalDryAlleSEOAnalyzer:
    def __init__(self, directory_path: str):
        self.directory_path = Path(directory_path)
        self.results: List[FinalSEOAnalysis] = []
        
    def extract_title(self, content: str) -> tuple[str, int]:
        """Extract title and calculate length"""
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            return title, len(title)
        return "", 0
    
    def extract_meta_description(self, content: str) -> tuple[str, int]:
        """Extract meta description with proper content attribute parsing"""
        # Use more precise regex to extract content from meta description
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', content, re.IGNORECASE | re.DOTALL)
        if desc_match:
            description = desc_match.group(1).strip()
            # Clean up any escaped characters
            description = description.replace('\\"', '"').replace("\\'", "'")
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
    
    def calculate_seo_health_score(self, title_length: int, meta_desc_length: int, 
                                 has_breadcrumb: bool, has_local_business: bool) -> int:
        """Calculate overall SEO health score (0-100)"""
        score = 0
        
        # Title scoring (30 points max)
        if 30 <= title_length <= 70:
            score += 30
        elif title_length > 0:
            score += max(0, 30 - abs(title_length - 50) * 2)
        
        # Meta description scoring (40 points max)
        if 120 <= meta_desc_length <= 160:
            score += 40
        elif meta_desc_length > 0:
            score += max(0, 40 - abs(meta_desc_length - 140) * 2)
        
        # Schema scoring (20 points max)
        if has_breadcrumb:
            score += 10
        if has_local_business:
            score += 10
        
        # Encoding scoring (10 points max)
        score += 10  # Assume UTF-8 is present
        
        return min(100, max(0, score))
    
    def calculate_priority_score(self, issues: List[str]) -> int:
        """Calculate priority score based on SEO impact"""
        score = 0
        for issue in issues:
            if "Missing BreadcrumbList schema" in issue:
                score += 10
            elif "Meta description too short" in issue and "0 chars" in issue:
                score += 9
            elif "Title too long" in issue:
                score += 8
            elif "Meta description too long" in issue:
                score += 6
            elif "Meta description too short" in issue:
                score += 5
            elif "Title too short" in issue:
                score += 4
            elif "Missing LocalBusiness schema" in issue:
                score += 3
            else:
                score += 2
        return score
    
    def analyze_file(self, file_path: Path) -> FinalSEOAnalysis:
        """Analyze a single HTML file with accurate parsing"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return FinalSEOAnalysis(
                file_name=file_path.name,
                title="ERROR_READING_FILE",
                title_length=0,
                meta_description="ERROR_READING_FILE",
                meta_description_length=0,
                has_breadcrumb_schema=False,
                has_local_business_schema=False,
                character_encoding="ERROR",
                issues=[f"Failed to read file: {str(e)}"],
                recommendations=[],
                priority_score=0,
                seo_health_score=0
            )
        
        # Extract all metrics
        title, title_length = self.extract_title(content)
        meta_desc, meta_desc_length = self.extract_meta_description(content)
        has_breadcrumb = self.check_breadcrumb_schema(content)
        has_local_business = self.check_local_business_schema(content)
        encoding = self.extract_character_encoding(content)
        
        # Calculate SEO health score
        seo_health_score = self.calculate_seo_health_score(
            title_length, meta_desc_length, has_breadcrumb, has_local_business
        )
        
        # Identify issues and recommendations
        issues = []
        recommendations = []
        
        # Title analysis
        if title_length == 0:
            issues.append("Missing title tag")
            recommendations.append("Add proper title tag")
        elif title_length > 70:
            issues.append(f"Title too long: {title_length} chars (optimal: ≤70)")
            recommendations.append(f"Shorten title to ≤70 characters (currently {title_length})")
        elif title_length < 30:
            issues.append(f"Title too short: {title_length} chars (optimal: 30-70)")
            recommendations.append(f"Expand title to 30-70 characters (currently {title_length})")
        
        # Meta description analysis
        if meta_desc_length == 0:
            issues.append("Missing meta description")
            recommendations.append("Add meta description (120-160 chars)")
        elif meta_desc_length < 120:
            issues.append(f"Meta description too short: {meta_desc_length} chars (optimal: 120-160)")
            recommendations.append(f"Expand meta description to 120-160 chars (currently {meta_desc_length})")
        elif meta_desc_length > 160:
            issues.append(f"Meta description too long: {meta_desc_length} chars (optimal: 120-160)")
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
        
        priority_score = self.calculate_priority_score(issues)
        
        return FinalSEOAnalysis(
            file_name=file_path.name,
            title=title,
            title_length=title_length,
            meta_description=meta_desc,
            meta_description_length=meta_desc_length,
            has_breadcrumb_schema=has_breadcrumb,
            has_local_business_schema=has_local_business,
            character_encoding=encoding,
            issues=issues,
            recommendations=recommendations,
            priority_score=priority_score,
            seo_health_score=seo_health_score
        )
    
    def analyze_all_files(self) -> List[FinalSEOAnalysis]:
        """Analyze all HTML files in the directory"""
        html_files = list(self.directory_path.glob("*.html"))
        
        for file_path in sorted(html_files):
            analysis = self.analyze_file(file_path)
            self.results.append(analysis)
        
        return self.results
    
    def generate_final_report(self) -> Dict:
        """Generate final comprehensive analysis report"""
        if not self.results:
            self.analyze_all_files()
        
        # Summary statistics
        total_files = len(self.results)
        files_with_issues = len([r for r in self.results if r.issues])
        average_health_score = sum(r.seo_health_score for r in self.results) / total_files if total_files > 0 else 0
        
        # Title analysis
        long_titles = [r for r in self.results if r.title_length > 70]
        short_titles = [r for r in self.results if r.title_length < 30]
        optimal_titles = [r for r in self.results if 30 <= r.title_length <= 70]
        
        # Meta description analysis
        short_descriptions = [r for r in self.results if 0 < r.meta_description_length < 120]
        long_descriptions = [r for r in self.results if r.meta_description_length > 160]
        missing_descriptions = [r for r in self.results if r.meta_description_length == 0]
        optimal_descriptions = [r for r in self.results if 120 <= r.meta_description_length <= 160]
        
        # Schema analysis
        missing_breadcrumb = [r for r in self.results if not r.has_breadcrumb_schema]
        missing_local_business = [r for r in self.results if not r.has_local_business_schema]
        
        # Character encoding issues
        encoding_issues = [r for r in self.results if r.character_encoding != "UTF-8"]
        
        # Priority ranking
        critical_issues = [r for r in self.results if r.priority_score >= 10]
        high_priority_issues = [r for r in self.results if 7 <= r.priority_score < 10]
        medium_priority_issues = [r for r in self.results if 4 <= r.priority_score < 7]
        low_priority_issues = [r for r in self.results if 1 <= r.priority_score < 4]
        clean_files = [r for r in self.results if r.priority_score == 0]
        
        return {
            "PHASE_1_EXECUTIVE_SUMMARY": {
                "total_files_analyzed": total_files,
                "average_seo_health_score": round(average_health_score, 1),
                "files_with_issues": files_with_issues,
                "clean_files_count": len(clean_files),
                "overall_status": "NEEDS_OPTIMIZATION" if files_with_issues > 0 else "EXCELLENT",
                "critical_issues_count": len(critical_issues),
                "high_priority_count": len(high_priority_issues),
                "medium_priority_count": len(medium_priority_issues),
                "low_priority_count": len(low_priority_issues)
            },
            "TITLE_OPTIMIZATION_ANALYSIS": {
                "status": "CRITICAL" if long_titles else "GOOD",
                "optimal_titles_count": len(optimal_titles),
                "long_titles_needing_fix": len(long_titles),
                "short_titles_needing_fix": len(short_titles),
                "problematic_titles": [
                    {
                        "file": r.file_name,
                        "current_title": r.title,
                        "current_length": r.title_length,
                        "issue": "TOO_LONG" if r.title_length > 70 else "TOO_SHORT",
                        "seo_impact": "HIGH" if r.title_length > 80 else "MEDIUM"
                    } for r in long_titles + short_titles
                ]
            },
            "META_DESCRIPTION_ANALYSIS": {
                "status": "GOOD" if len(optimal_descriptions) > len(short_descriptions + long_descriptions + missing_descriptions) else "NEEDS_ATTENTION",
                "optimal_descriptions_count": len(optimal_descriptions),
                "short_descriptions_count": len(short_descriptions),
                "long_descriptions_count": len(long_descriptions),
                "missing_descriptions_count": len(missing_descriptions),
                "problematic_descriptions": [
                    {
                        "file": r.file_name,
                        "current_description": r.meta_description,
                        "current_length": r.meta_description_length,
                        "issue": "MISSING" if r.meta_description_length == 0 else ("TOO_SHORT" if r.meta_description_length < 120 else "TOO_LONG"),
                        "seo_impact": "HIGH" if r.meta_description_length == 0 else "MEDIUM"
                    } for r in missing_descriptions + short_descriptions + long_descriptions
                ]
            },
            "BREADCRUMB_SCHEMA_AUDIT": {
                "status": "CRITICAL" if missing_breadcrumb else "EXCELLENT",
                "pages_with_breadcrumbs": total_files - len(missing_breadcrumb),
                "pages_missing_breadcrumbs": len(missing_breadcrumb),
                "missing_breadcrumb_files": [r.file_name for r in missing_breadcrumb],
                "schema_completeness_percentage": round(((total_files - len(missing_breadcrumb)) / total_files) * 100, 1) if total_files > 0 else 0
            },
            "LOCAL_BUSINESS_SCHEMA_AUDIT": {
                "status": "EXCELLENT" if len(missing_local_business) == 0 else "NEEDS_ATTENTION",
                "pages_with_local_business": total_files - len(missing_local_business),
                "pages_missing_local_business": len(missing_local_business),
                "missing_local_business_files": [r.file_name for r in missing_local_business],
                "schema_completeness_percentage": round(((total_files - len(missing_local_business)) / total_files) * 100, 1) if total_files > 0 else 0
            },
            "PRIORITY_ACTION_PLAN": {
                "immediate_fixes_required": [
                    {
                        "file_name": r.file_name,
                        "priority_level": "CRITICAL",
                        "seo_health_score": r.seo_health_score,
                        "issues": r.issues,
                        "estimated_impact": "MAJOR_RANKING_BOOST",
                        "implementation_complexity": "LOW" if len(r.issues) <= 2 else "MEDIUM"
                    } for r in critical_issues
                ],
                "high_priority_optimizations": [
                    {
                        "file_name": r.file_name,
                        "priority_level": "HIGH",
                        "seo_health_score": r.seo_health_score,
                        "issues": r.issues,
                        "estimated_impact": "SIGNIFICANT_IMPROVEMENT",
                        "implementation_complexity": "LOW"
                    } for r in high_priority_issues
                ],
                "medium_priority_optimizations": [
                    {
                        "file_name": r.file_name,
                        "priority_level": "MEDIUM", 
                        "seo_health_score": r.seo_health_score,
                        "issues": r.issues,
                        "estimated_impact": "MODERATE_IMPROVEMENT",
                        "implementation_complexity": "LOW"
                    } for r in medium_priority_issues[:10]  # Limit to top 10
                ]
            },
            "IMPLEMENTATION_READY_SOLUTIONS": {
                "title_optimizations": [
                    {
                        "file": r.file_name,
                        "current_title": r.title,
                        "current_length": r.title_length,
                        "recommended_action": "SHORTEN" if r.title_length > 70 else "EXPAND",
                        "priority": "HIGH" if r.title_length > 80 else "MEDIUM"
                    } for r in long_titles + short_titles
                ],
                "breadcrumb_schema_fixes": [
                    {
                        "file": r.file_name,
                        "missing_schema": "BreadcrumbList",
                        "implementation_priority": "CRITICAL",
                        "estimated_time": "5 minutes"
                    } for r in missing_breadcrumb
                ]
            },
            "SEO_HEALTH_SCORES": [
                {
                    "file_name": r.file_name,
                    "seo_health_score": r.seo_health_score,
                    "title_length": r.title_length,
                    "meta_description_length": r.meta_description_length,
                    "has_breadcrumb_schema": r.has_breadcrumb_schema,
                    "has_local_business_schema": r.has_local_business_schema,
                    "issues_count": len(r.issues),
                    "grade": self.get_grade(r.seo_health_score)
                } for r in sorted(self.results, key=lambda x: x.seo_health_score, reverse=True)
            ]
        }
    
    def get_grade(self, score: int) -> str:
        """Convert SEO health score to letter grade"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

def main():
    analyzer = FinalDryAlleSEOAnalyzer("/Users/macos/Documents/Projeler/DryAlle/bolgeler")
    report = analyzer.generate_final_report()
    
    # Save final comprehensive report
    with open("/Users/macos/Documents/Projeler/DryAlle/bolgeler/PHASE1_FINAL_SEO_ANALYSIS.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    return report

if __name__ == "__main__":
    main()