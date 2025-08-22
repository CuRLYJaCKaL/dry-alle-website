#!/usr/bin/env python3
"""
Corrected MIT-Level SEO Analysis Tool for DryAlle Regional Pages
Re-analyzes files with correct meta description extraction
"""

import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class CorrectedSEOAnalysis:
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
    priority_score: int

class CorrectedDryAlleSEOAnalyzer:
    def __init__(self, directory_path: str):
        self.directory_path = Path(directory_path)
        self.results: List[CorrectedSEOAnalysis] = []
        
    def extract_title(self, content: str) -> tuple[str, int]:
        """Extract title and calculate length"""
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            return title, len(title)
        return "", 0
    
    def extract_meta_description(self, content: str) -> tuple[str, int]:
        """Extract meta description with better parsing"""
        # Look for proper meta description tag
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', content, re.IGNORECASE)
        if desc_match:
            description = desc_match.group(1).strip()
            # Clean up any HTML entities
            description = re.sub(r'&[a-zA-Z]+;', '', description)
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
    
    def analyze_file(self, file_path: Path) -> CorrectedSEOAnalysis:
        """Analyze a single HTML file with corrected parsing"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return CorrectedSEOAnalysis(
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
                recommendations=[],
                priority_score=0
            )
        
        # Extract all metrics
        title, title_length = self.extract_title(content)
        meta_desc, meta_desc_length = self.extract_meta_description(content)
        has_breadcrumb = self.check_breadcrumb_schema(content)
        has_local_business = self.check_local_business_schema(content)
        encoding = self.extract_character_encoding(content)
        
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
        
        return CorrectedSEOAnalysis(
            file_name=file_path.name,
            title=title,
            title_length=title_length,
            meta_description=meta_desc,
            meta_description_length=meta_desc_length,
            has_breadcrumb_schema=has_breadcrumb,
            has_local_business_schema=has_local_business,
            character_encoding=encoding,
            internal_links=[],
            issues=issues,
            recommendations=recommendations,
            priority_score=priority_score
        )
    
    def analyze_all_files(self) -> List[CorrectedSEOAnalysis]:
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
        priority_fixes = sorted([r for r in self.results if r.issues], 
                              key=lambda x: x.priority_score, reverse=True)
        
        return {
            "executive_summary": {
                "total_files_analyzed": total_files,
                "files_with_issues": files_with_issues,
                "clean_files": total_files - files_with_issues,
                "overall_health_score": round(((total_files - files_with_issues) / total_files) * 100, 1) if total_files > 0 else 0,
                "critical_issues": len([r for r in self.results if r.priority_score >= 10]),
                "high_priority_issues": len([r for r in self.results if 7 <= r.priority_score < 10]),
                "medium_priority_issues": len([r for r in self.results if 4 <= r.priority_score < 7]),
                "low_priority_issues": len([r for r in self.results if 1 <= r.priority_score < 4])
            },
            "title_optimization": {
                "status": "NEEDS_ATTENTION" if long_titles or short_titles else "GOOD",
                "optimal_count": len(optimal_titles),
                "long_titles": [{"file": r.file_name, "length": r.title_length, "title": r.title, "recommended_title": self.generate_optimized_title(r)} for r in long_titles],
                "short_titles": [{"file": r.file_name, "length": r.title_length, "title": r.title} for r in short_titles]
            },
            "meta_description_optimization": {
                "status": "CRITICAL" if missing_descriptions or short_descriptions else "GOOD",
                "optimal_count": len(optimal_descriptions),
                "missing_descriptions": [{"file": r.file_name, "recommended_description": self.generate_meta_description(r)} for r in missing_descriptions],
                "short_descriptions": [{"file": r.file_name, "length": r.meta_description_length, "current": r.meta_description, "recommended_description": self.generate_meta_description(r)} for r in short_descriptions],
                "long_descriptions": [{"file": r.file_name, "length": r.meta_description_length, "current": r.meta_description} for r in long_descriptions]
            },
            "breadcrumb_schema_gaps": {
                "status": "CRITICAL" if missing_breadcrumb else "GOOD",
                "missing_count": len(missing_breadcrumb),
                "missing_files": [{"file": r.file_name, "breadcrumb_template": self.generate_breadcrumb_schema(r)} for r in missing_breadcrumb]
            },
            "priority_action_plan": [
                {
                    "file_name": r.file_name,
                    "priority_score": r.priority_score,
                    "severity": self.get_severity_level(r.priority_score),
                    "issues": r.issues,
                    "recommendations": r.recommendations,
                    "estimated_seo_impact": self.estimate_seo_impact(r.priority_score)
                } for r in priority_fixes[:10]  # Top 10 priority fixes
            ],
            "implementation_ready_fixes": {
                "title_optimizations": [self.create_title_fix(r) for r in long_titles],
                "meta_description_additions": [self.create_meta_description_fix(r) for r in short_descriptions + missing_descriptions],
                "breadcrumb_schema_additions": [self.create_breadcrumb_fix(r) for r in missing_breadcrumb]
            }
        }
    
    def generate_optimized_title(self, result: CorrectedSEOAnalysis) -> str:
        """Generate optimized title for long titles"""
        location = result.file_name.split('-')[0].title()
        service = ' '.join(result.file_name.split('-')[1:-1]).title()
        
        # Create shortened title maintaining SEO value
        if 'haute-couture' in result.file_name:
            return f"{location} Haute Couture | Dry Alle | Premium Designer Bakım"
        elif 'premium' in result.file_name:
            return f"{location} Premium Temizlik | Dry Alle | VIP Hizmet"
        elif 'luxury' in result.file_name:
            return f"{location} Luxury Kıyafet | Dry Alle | Elite Temizlik"
        elif 'hali-yikama' in result.file_name:
            return f"{location} Halı Yıkama | Dry Alle | Professional Temizlik"
        elif 'koltuk-yikama' in result.file_name:
            return f"{location} Koltuk Yıkama | Dry Alle | Expert Mobilya Bakım"
        else:
            return f"{location} Kuru Temizleme | Dry Alle | Professional Hizmet"
    
    def generate_meta_description(self, result: CorrectedSEOAnalysis) -> str:
        """Generate optimized meta description"""
        location = result.file_name.split('-')[0]
        
        if 'haute-couture' in result.file_name:
            return f"{location.title()}'de haute couture kıyafet temizleme hizmeti. Designer elbise temizleme, lüks giyim bakımı ve couture gown temizliği. 25 yıllık deneyim. Kapıdan alıp getiriyoruz."
        elif 'premium' in result.file_name:
            return f"{location.title()}'de premium kıyafet temizleme hizmeti. İş kıyafetleri, takım elbise, gömlek temizleme uzmanı. VIP hizmet, 25 yıllık deneyim. Ücretsiz kapıdan teslimat."
        elif 'luxury' in result.file_name:
            return f"{location.title()}'de luxury kıyafet temizleme hizmeti. Lüks giyim bakımı, designer kıyafet temizleme uzmanı. 25 yıllık deneyim. Kapıdan alıp getiriyoruz."
        elif 'hali-yikama' in result.file_name:
            return f"{location.title()}'de profesyonel halı yıkama hizmeti. Antik halı temizleme, modern halı yıkama, halı bakım uzmanı. 25 yıllık deneyim. Kapıdan alıp getiriyoruz."
        elif 'koltuk-yikama' in result.file_name:
            return f"{location.title()}'de koltuk yıkama hizmeti. Mobilya temizleme, deri koltuk bakımı, kumaş koltuk yıkama uzmanı. 25 yıllık deneyim. Kapıdan alıp getiriyoruz."
        elif 'gelinlik' in result.file_name:
            return f"{location.title()}'de gelinlik temizleme hizmeti. Wedding dress temizleme, abiye temizleme, özel günler için kıyafet bakımı. 25 yıllık deneyim. Kapıdan teslimat."
        else:
            return f"{location.title()}'de profesyonel kuru temizleme hizmeti. Takım elbise, elbise, palto, gömlek temizleme uzmanı. 25 yıllık deneyim. Ücretsiz kapıdan teslimat."
    
    def generate_breadcrumb_schema(self, result: CorrectedSEOAnalysis) -> Dict:
        """Generate breadcrumb schema template"""
        location = result.file_name.split('-')[0].title()
        service_parts = result.file_name.replace('.html', '').split('-')[1:]
        service_name = ' '.join([s.title() for s in service_parts])
        
        return {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Ana Sayfa",
                    "item": "https://dryallekurutemizleme.com/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Hizmetlerimiz",
                    "item": "https://dryallekurutemizleme.com/#services"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": f"{location} {service_name}",
                    "item": f"https://dryallekurutemizleme.com/bolgeler/{result.file_name}"
                }
            ]
        }
    
    def get_severity_level(self, priority_score: int) -> str:
        """Get severity level based on priority score"""
        if priority_score >= 10:
            return "CRITICAL"
        elif priority_score >= 7:
            return "HIGH"
        elif priority_score >= 4:
            return "MEDIUM"
        else:
            return "LOW"
    
    def estimate_seo_impact(self, priority_score: int) -> str:
        """Estimate SEO impact of fixing issues"""
        if priority_score >= 10:
            return "Major ranking improvement expected"
        elif priority_score >= 7:
            return "Significant ranking boost likely"
        elif priority_score >= 4:
            return "Moderate improvement in visibility"
        else:
            return "Minor optimization benefit"
    
    def create_title_fix(self, result: CorrectedSEOAnalysis) -> Dict:
        """Create ready-to-implement title fix"""
        return {
            "file": result.file_name,
            "current_title": result.title,
            "current_length": result.title_length,
            "optimized_title": self.generate_optimized_title(result),
            "optimized_length": len(self.generate_optimized_title(result)),
            "implementation": f'<title>{self.generate_optimized_title(result)}</title>'
        }
    
    def create_meta_description_fix(self, result: CorrectedSEOAnalysis) -> Dict:
        """Create ready-to-implement meta description fix"""
        optimized_desc = self.generate_meta_description(result)
        return {
            "file": result.file_name,
            "current_description": result.meta_description,
            "current_length": result.meta_description_length,
            "optimized_description": optimized_desc,
            "optimized_length": len(optimized_desc),
            "implementation": f'<meta name="description" content="{optimized_desc}">'
        }
    
    def create_breadcrumb_fix(self, result: CorrectedSEOAnalysis) -> Dict:
        """Create ready-to-implement breadcrumb schema fix"""
        schema = self.generate_breadcrumb_schema(result)
        return {
            "file": result.file_name,
            "schema_template": schema,
            "implementation": f'<script type="application/ld+json">\n{json.dumps(schema, indent=4, ensure_ascii=False)}\n</script>'
        }

def main():
    analyzer = CorrectedDryAlleSEOAnalyzer("/Users/macos/Documents/Projeler/DryAlle/bolgeler")
    report = analyzer.generate_comprehensive_report()
    
    # Save comprehensive report
    with open("/Users/macos/Documents/Projeler/DryAlle/bolgeler/phase1_seo_analysis_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    return report

if __name__ == "__main__":
    main()