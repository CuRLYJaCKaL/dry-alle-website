#!/usr/bin/env python3
"""
URL Standardization System for Blog Redesign & SEO Overhaul
Turkish to English URL Slug Conversion & 301 Redirect Generation

Converts Turkish blog URLs to SEO-optimized English slugs:
- Old: /blog/2025-01/kis-aylarinda-kuru-temizleme-ipuclari.html
- New: /blog/winter-dry-cleaning-tips/

Features:
- Turkish character removal (ç→c, ğ→g, ı→i, ş→s, ü→u, ö→o)
- Date removal from URLs for timeless SEO
- 301 redirect generation for old→new URL mapping
- SEO-optimized slug creation
"""

import os
import re
import json
from datetime import datetime
from urllib.parse import quote
import unicodedata

class URLStandardizer:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.url_mappings = {}
        self.redirects = []
        
        # Turkish to English character mapping
        self.char_map = {
            'ç': 'c', 'Ç': 'C',
            'ğ': 'g', 'Ğ': 'G',
            'ı': 'i', 'I': 'I',
            'î': 'i', 'Î': 'I',
            'ö': 'o', 'Ö': 'O',
            'ş': 's', 'Ş': 'S',
            'ü': 'u', 'Ü': 'U',
            'â': 'a', 'Â': 'A',
            'û': 'u', 'Û': 'U'
        }
        
        # Common Turkish-English keyword translations for SEO
        self.keyword_translations = {
            'kuru-temizleme': 'dry-cleaning',
            'hali-yikama': 'carpet-cleaning',
            'koltuk-yikama': 'sofa-cleaning',
            'perde-temizleme': 'curtain-cleaning',
            'ev-tekstili': 'home-textiles',
            'canta-temizleme': 'bag-cleaning',
            'lostra-hizmeti': 'leather-care',
            'kumas-deri-boyama': 'fabric-leather-dyeing',
            'utu-hizmetleri': 'ironing-services',
            'gelinlik': 'wedding-dress',
            'ipuclari': 'tips',
            'rehberi': 'guide',
            'karsilastirma': 'comparison',
            'bakim': 'care',
            'temizlik': 'cleaning',
            'yikama': 'washing',
            'teknolojileri': 'technologies',
            'yontemleri': 'methods',
            'hizmetleri': 'services',
            'profesyonel': 'professional',
            'istanbul': 'istanbul',
            'sevgililer-gunu': 'valentines-day',
            'bahar-temizligi': 'spring-cleaning',
            'yaz-hazarligi': 'summer-preparation',
            'kis-hazarligi': 'winter-preparation',
            'sonbahar': 'autumn',
            'kis-aylarinda': 'winter',
            'yaz-kiyafetleri': 'summer-clothes',
            'kis-kiyafetleri': 'winter-clothes',
            'duggun-sezonu': 'wedding-season',
            'tatil-donusu': 'post-vacation',
            'okul-oncesi': 'back-to-school',
            'yilbasi': 'new-year',
            'elite-semtlerde': 'luxury-districts',
            'anadolu-yakasi': 'anatolian-side',
            'sicak-havalarda': 'hot-weather',
            'klimali-ortamda': 'air-conditioned',
            'vintage-kiyafetler': 'vintage-clothing',
            'antik-hali': 'antique-carpet',
            'lux-tekstil': 'luxury-textile',
            'outdoor-tekstil': 'outdoor-textile',
            'uniform-bakimi': 'uniform-care',
            'hijyen-rehberi': 'hygiene-guide',
            'sigorta-garanti': 'insurance-warranty',
            'mukemmel-sonuclar': 'perfect-results',
            'quality-control': 'quality-control',
            'teknoloji-yenilikleri': 'technology-innovations',
            'cevre-dostu': 'eco-friendly',
            'allerjik-reaksiyonlar': 'allergic-reactions',
            'renk-solmasi': 'color-fading',
            'kaplama-yenileme': 'upholstery-renewal'
        }

    def convert_turkish_to_english(self, text):
        """Convert Turkish characters to English equivalents"""
        # First apply character mapping
        for tr_char, en_char in self.char_map.items():
            text = text.replace(tr_char, en_char)
        
        # Apply keyword translations
        for tr_word, en_word in self.keyword_translations.items():
            text = text.replace(tr_word, en_word)
        
        # Normalize unicode and remove accents
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        
        return text

    def create_seo_slug(self, filename, remove_date=True):
        """Create SEO-optimized English slug from Turkish filename"""
        # Remove file extension
        slug = os.path.splitext(filename)[0]
        
        # Remove date patterns if requested
        if remove_date:
            # Remove YYYY-MM- pattern
            slug = re.sub(r'^\d{4}-\d{2}-', '', slug)
            # Remove year patterns
            slug = re.sub(r'-20\d{2}$', '', slug)
            slug = re.sub(r'-20\d{2}-', '-', slug)
        
        # Convert Turkish to English
        slug = self.convert_turkish_to_english(slug)
        
        # Clean and optimize
        slug = slug.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special chars
        slug = re.sub(r'[-\s]+', '-', slug)   # Normalize separators
        slug = slug.strip('-')                # Remove leading/trailing dashes
        
        # Ensure reasonable length (max 60 chars for SEO)
        if len(slug) > 60:
            # Split and keep most important words
            words = slug.split('-')
            slug = '-'.join(words[:8])  # Keep first 8 words max
        
        return slug

    def analyze_current_structure(self):
        """Analyze current blog URL structure"""
        print("🔍 Analyzing Current Blog URL Structure...")
        
        blog_files = []
        
        # Find all blog HTML files
        for root, dirs, files in os.walk(os.path.join(self.project_root, 'blog')):
            for file in files:
                if file.endswith('.html') and file != 'index.html':
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, self.project_root)
                    
                    blog_files.append({
                        'full_path': full_path,
                        'relative_path': relative_path,
                        'filename': file,
                        'directory': os.path.relpath(root, self.project_root)
                    })
        
        print(f"✅ Found {len(blog_files)} blog files to standardize")
        
        return blog_files

    def generate_new_url_structure(self, blog_files):
        """Generate new URL structure with English slugs"""
        print("🔄 Generating New URL Structure...")
        
        new_structure = {}
        conflicts = []
        
        for file_info in blog_files:
            old_url = f"/{file_info['relative_path']}"
            
            # Create new slug
            new_slug = self.create_seo_slug(file_info['filename'])
            new_url = f"/blog/{new_slug}/"
            
            # Check for conflicts
            if new_url in new_structure:
                conflicts.append({
                    'slug': new_slug,
                    'files': [new_structure[new_url]['old_url'], old_url]
                })
                # Add suffix to resolve conflict
                counter = 2
                while f"/blog/{new_slug}-{counter}/" in new_structure:
                    counter += 1
                new_url = f"/blog/{new_slug}-{counter}/"
            
            new_structure[new_url] = {
                'old_url': old_url,
                'old_path': file_info['full_path'],
                'new_slug': new_slug,
                'filename': file_info['filename'],
                'directory': file_info['directory']
            }
        
        if conflicts:
            print(f"⚠️ Resolved {len(conflicts)} slug conflicts")
        
        print(f"✅ Generated {len(new_structure)} new URL mappings")
        
        return new_structure

    def create_301_redirects(self, url_mappings):
        """Create 301 redirect rules for .htaccess"""
        print("📋 Creating 301 Redirect Rules...")
        
        redirect_rules = []
        
        # Header comment
        redirect_rules.append("# Blog URL Standardization - 301 Redirects")
        redirect_rules.append("# Generated: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        redirect_rules.append("# Turkish to English URL Migration")
        redirect_rules.append("")
        
        # Sort by old URL for better organization
        sorted_mappings = sorted(url_mappings.items(), key=lambda x: x[1]['old_url'])
        
        for new_url, mapping in sorted_mappings:
            old_url = mapping['old_url']
            
            # Create Apache rewrite rule
            # Escape special characters
            old_pattern = old_url.replace('.html', r'\.html')
            old_pattern = old_pattern.replace('/', r'\/')
            
            # Remove leading slash and add anchors
            old_pattern = f"^{old_pattern[1:]}$"
            new_target = new_url
            
            redirect_rules.append(f"RewriteRule {old_pattern} {new_target} [R=301,L]")
        
        redirect_rules.append("")
        redirect_rules.append("# End Blog URL Redirects")
        
        return redirect_rules

    def create_nginx_redirects(self, url_mappings):
        """Create Nginx redirect rules"""
        print("📋 Creating Nginx Redirect Rules...")
        
        redirect_rules = []
        
        # Header comment
        redirect_rules.append("# Blog URL Standardization - Nginx Redirects")
        redirect_rules.append("# Generated: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        redirect_rules.append("")
        
        for new_url, mapping in url_mappings.items():
            old_url = mapping['old_url']
            redirect_rules.append(f"location = {old_url} {{")
            redirect_rules.append(f"    return 301 {new_url};")
            redirect_rules.append("}")
            redirect_rules.append("")
        
        return redirect_rules

    def generate_file_migration_plan(self, url_mappings):
        """Generate plan for moving files to new structure"""
        print("📁 Creating File Migration Plan...")
        
        migration_plan = []
        
        for new_url, mapping in url_mappings.items():
            old_path = mapping['old_path']
            new_slug = mapping['new_slug']
            
            # New file structure: /blog/{slug}/index.html
            new_dir = os.path.join(self.project_root, 'blog', new_slug)
            new_path = os.path.join(new_dir, 'index.html')
            
            migration_plan.append({
                'old_path': old_path,
                'new_dir': new_dir,
                'new_path': new_path,
                'new_url': new_url,
                'old_url': mapping['old_url'],
                'slug': new_slug
            })
        
        return migration_plan

    def save_standardization_report(self, url_mappings, redirects, migration_plan):
        """Save comprehensive standardization report"""
        print("💾 Saving URL Standardization Report...")
        
        report = {
            "generation_date": datetime.now().isoformat(),
            "total_urls_processed": len(url_mappings),
            "url_mappings": {},
            "redirect_rules_count": len([r for r in redirects if r.startswith('RewriteRule')]),
            "migration_plan_count": len(migration_plan),
            "seo_benefits": [
                "Turkish character removal for better international SEO",
                "Date removal creates timeless URLs",
                "Keyword-optimized English slugs",
                "Clean /blog/{slug}/ structure",
                "Proper 301 redirects preserve link juice"
            ]
        }
        
        # Convert URL mappings to serializable format
        for new_url, mapping in url_mappings.items():
            report["url_mappings"][new_url] = {
                "old_url": mapping['old_url'],
                "new_slug": mapping['new_slug'],
                "filename": mapping['filename']
            }
        
        # Save main report
        report_path = os.path.join(self.project_root, 'seo/analysis/url_standardization_report.json')
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        # Save redirect rules
        htaccess_path = os.path.join(self.project_root, 'seo/redirects/blog_redirects.htaccess')
        os.makedirs(os.path.dirname(htaccess_path), exist_ok=True)
        
        with open(htaccess_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(redirects))
        
        # Save migration plan
        migration_path = os.path.join(self.project_root, 'seo/migration/file_migration_plan.json')
        os.makedirs(os.path.dirname(migration_path), exist_ok=True)
        
        with open(migration_path, 'w', encoding='utf-8') as f:
            json.dump(migration_plan, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Report saved: {report_path}")
        print(f"✅ Redirects saved: {htaccess_path}")
        print(f"✅ Migration plan: {migration_path}")
        
        return report_path

def main():
    """Execute URL standardization process"""
    print("🚀 BLOG URL STANDARDIZATION SYSTEM")
    print("=" * 50)
    print("🎯 Turkish → English URL Migration")
    print("=" * 50)
    
    standardizer = URLStandardizer()
    
    try:
        # Analyze current structure
        blog_files = standardizer.analyze_current_structure()
        
        # Generate new URL structure
        url_mappings = standardizer.generate_new_url_structure(blog_files)
        
        # Create redirect rules
        apache_redirects = standardizer.create_301_redirects(url_mappings)
        nginx_redirects = standardizer.create_nginx_redirects(url_mappings)
        
        # Generate migration plan
        migration_plan = standardizer.generate_file_migration_plan(url_mappings)
        
        # Save everything
        report_path = standardizer.save_standardization_report(
            url_mappings, apache_redirects, migration_plan
        )
        
        # Summary
        print("\n" + "=" * 50)
        print("📊 URL STANDARDIZATION COMPLETE")
        print("=" * 50)
        print(f"✅ URLs Processed: {len(url_mappings)}")
        print(f"✅ Redirect Rules: {len([r for r in apache_redirects if r.startswith('RewriteRule')])}")
        print(f"✅ Migration Plan: {len(migration_plan)} files")
        print(f"✅ Report Location: {report_path}")
        
        # Sample mappings
        print("\n🔗 Sample URL Mappings:")
        count = 0
        for new_url, mapping in list(url_mappings.items())[:5]:
            print(f"   {mapping['old_url']} → {new_url}")
            count += 1
        
        if len(url_mappings) > 5:
            print(f"   ... and {len(url_mappings) - 5} more")
        
        print("\n🚀 NEXT STEPS:")
        print("1. Review generated redirect rules")
        print("2. Test URL mappings before implementation")
        print("3. Execute file migration plan")
        print("4. Deploy redirect rules to server")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during URL standardization: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)