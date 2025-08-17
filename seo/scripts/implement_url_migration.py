#!/usr/bin/env python3
"""
URL Migration Implementation Script
Creates new directory structure and migrates blog files to SEO-optimized URLs

Phase A1: URL Standardization Implementation
- Creates /blog/{slug}/ directory structure
- Moves HTML files to new locations
- Updates internal links
- Generates proper 301 redirects
"""

import os
import json
import shutil
import re
from datetime import datetime

class URLMigrationImplementer:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.base_url = "https://dryallekurutemizleme.com"
        self.migration_report = {
            "start_time": datetime.now().isoformat(),
            "files_migrated": 0,
            "directories_created": 0,
            "links_updated": 0,
            "errors": []
        }

    def load_migration_plan(self):
        """Load the generated migration plan"""
        plan_path = os.path.join(self.project_root, 'seo/migration/file_migration_plan.json')
        
        try:
            with open(plan_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Migration plan not found: {plan_path}")
            print("Please run url_standardization.py first")
            return []

    def create_directory_structure(self, migration_plan):
        """Create new directory structure for migrated files"""
        print("📁 Creating New Directory Structure...")
        
        created_dirs = 0
        
        for item in migration_plan:
            new_dir = item['new_dir']
            
            if not os.path.exists(new_dir):
                os.makedirs(new_dir, exist_ok=True)
                created_dirs += 1
                print(f"   Created: {os.path.relpath(new_dir, self.project_root)}")
        
        self.migration_report["directories_created"] = created_dirs
        print(f"✅ Created {created_dirs} new directories")

    def copy_and_update_file(self, old_path, new_path, new_url, old_url):
        """Copy file to new location and update internal links"""
        try:
            # Read original file
            with open(old_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update internal links within the content
            content = self.update_internal_links(content, old_url, new_url)
            
            # Update canonical URL
            content = self.update_canonical_url(content, new_url)
            
            # Update meta tags for new URL structure
            content = self.update_meta_tags(content, new_url)
            
            # Write to new location
            with open(new_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"   ✅ Migrated: {os.path.basename(old_path)} → {os.path.basename(new_path)}")
            return True
            
        except Exception as e:
            error_msg = f"Failed to migrate {old_path}: {str(e)}"
            self.migration_report["errors"].append(error_msg)
            print(f"   ❌ {error_msg}")
            return False

    def update_internal_links(self, content, old_url, new_url):
        """Update internal blog links in content"""
        # This is a placeholder - in a real implementation, you'd update
        # all internal links that reference the old URL structure
        updated_content = content
        
        # Update any self-references
        if old_url in content:
            updated_content = content.replace(old_url, new_url)
        
        return updated_content

    def update_canonical_url(self, content, new_url):
        """Update canonical URL in HTML head"""
        full_url = self.base_url + new_url
        
        # Look for existing canonical link
        canonical_pattern = r'<link\s+rel=["\']canonical["\']\s+href=["\'][^"\']*["\']\s*/?>'
        new_canonical = f'<link rel="canonical" href="{full_url}">'
        
        if re.search(canonical_pattern, content, re.IGNORECASE):
            content = re.sub(canonical_pattern, new_canonical, content, flags=re.IGNORECASE)
        else:
            # Add canonical if not exists
            head_pattern = r'</head>'
            if re.search(head_pattern, content, re.IGNORECASE):
                content = re.sub(head_pattern, f'    {new_canonical}\n</head>', content, flags=re.IGNORECASE)
        
        return content

    def update_meta_tags(self, content, new_url):
        """Update meta tags for new URL structure"""
        # Update og:url if exists
        og_url_pattern = r'<meta\s+property=["\']og:url["\']\s+content=["\'][^"\']*["\']\s*/?>'
        full_url = self.base_url + new_url
        new_og_url = f'<meta property="og:url" content="{full_url}">'
        
        if re.search(og_url_pattern, content, re.IGNORECASE):
            content = re.sub(og_url_pattern, new_og_url, content, flags=re.IGNORECASE)
        
        return content

    def execute_migration(self, migration_plan):
        """Execute the file migration"""
        print("🚀 Executing File Migration...")
        
        successful_migrations = 0
        
        for item in migration_plan:
            old_path = item['old_path']
            new_path = item['new_path']
            new_url = item['new_url']
            old_url = item['old_url']
            
            if os.path.exists(old_path):
                if self.copy_and_update_file(old_path, new_path, new_url, old_url):
                    successful_migrations += 1
            else:
                error_msg = f"Source file not found: {old_path}"
                self.migration_report["errors"].append(error_msg)
                print(f"   ❌ {error_msg}")
        
        self.migration_report["files_migrated"] = successful_migrations
        print(f"✅ Successfully migrated {successful_migrations} files")

    def create_redirect_htaccess(self):
        """Create .htaccess file with redirect rules"""
        print("📋 Creating .htaccess Redirect File...")
        
        htaccess_source = os.path.join(self.project_root, 'seo/redirects/blog_redirects.htaccess')
        htaccess_dest = os.path.join(self.project_root, '.htaccess')
        
        try:
            # Read existing .htaccess if it exists
            existing_content = ""
            if os.path.exists(htaccess_dest):
                with open(htaccess_dest, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
            
            # Read new redirects
            with open(htaccess_source, 'r', encoding='utf-8') as f:
                new_redirects = f.read()
            
            # Combine content
            if existing_content and not "# Blog URL Standardization" in existing_content:
                combined_content = existing_content + "\n\n" + new_redirects
            else:
                combined_content = new_redirects
            
            # Write to .htaccess
            with open(htaccess_dest, 'w', encoding='utf-8') as f:
                f.write(combined_content)
            
            print(f"✅ Updated .htaccess with blog redirects")
            
        except Exception as e:
            error_msg = f"Failed to create .htaccess: {str(e)}"
            self.migration_report["errors"].append(error_msg)
            print(f"❌ {error_msg}")

    def update_blog_index(self):
        """Update blog index page with new URL structure"""
        print("📝 Updating Blog Index Page...")
        
        blog_index_path = os.path.join(self.project_root, 'blog/index.html')
        
        try:
            with open(blog_index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # This is a placeholder for updating the blog index
            # In a real implementation, you'd update all the links to point to new URLs
            print("   📌 Blog index update: Manual review recommended")
            print("   📌 Update all blog post links to new /blog/{slug}/ format")
            
        except Exception as e:
            error_msg = f"Failed to read blog index: {str(e)}"
            self.migration_report["errors"].append(error_msg)
            print(f"❌ {error_msg}")

    def cleanup_old_files(self, migration_plan, confirm=False):
        """Remove old files after successful migration"""
        if not confirm:
            print("⚠️ Old file cleanup skipped (safety measure)")
            print("   Run with confirm=True after verifying migration success")
            return
        
        print("🗑️ Cleaning Up Old Files...")
        
        removed_files = 0
        
        for item in migration_plan:
            old_path = item['old_path']
            new_path = item['new_path']
            
            # Only remove if new file exists and is not empty
            if os.path.exists(new_path) and os.path.getsize(new_path) > 0:
                try:
                    os.remove(old_path)
                    removed_files += 1
                    print(f"   🗑️ Removed: {os.path.relpath(old_path, self.project_root)}")
                except Exception as e:
                    error_msg = f"Failed to remove {old_path}: {str(e)}"
                    self.migration_report["errors"].append(error_msg)
        
        print(f"✅ Removed {removed_files} old files")

    def save_migration_report(self):
        """Save migration completion report"""
        self.migration_report["end_time"] = datetime.now().isoformat()
        
        report_path = os.path.join(self.project_root, 'seo/reports/migration_completion_report.json')
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.migration_report, f, ensure_ascii=False, indent=2)
        
        return report_path

def main():
    """Execute URL migration implementation"""
    print("🚀 BLOG URL MIGRATION IMPLEMENTATION")
    print("=" * 50)
    print("🎯 Phase A1: URL Standardization")
    print("=" * 50)
    
    implementer = URLMigrationImplementer()
    
    try:
        # Load migration plan
        migration_plan = implementer.load_migration_plan()
        if not migration_plan:
            return False
        
        print(f"📋 Loaded migration plan: {len(migration_plan)} files to migrate")
        
        # Create new directory structure
        implementer.create_directory_structure(migration_plan)
        
        # Execute file migration
        implementer.execute_migration(migration_plan)
        
        # Create redirect rules
        implementer.create_redirect_htaccess()
        
        # Update blog index
        implementer.update_blog_index()
        
        # Save report
        report_path = implementer.save_migration_report()
        
        # Summary
        print("\n" + "=" * 50)
        print("📊 MIGRATION IMPLEMENTATION COMPLETE")
        print("=" * 50)
        print(f"✅ Files Migrated: {implementer.migration_report['files_migrated']}")
        print(f"✅ Directories Created: {implementer.migration_report['directories_created']}")
        print(f"✅ Errors: {len(implementer.migration_report['errors'])}")
        print(f"✅ Report: {report_path}")
        
        if implementer.migration_report['errors']:
            print("\n⚠️ ERRORS ENCOUNTERED:")
            for error in implementer.migration_report['errors'][:5]:
                print(f"   - {error}")
            if len(implementer.migration_report['errors']) > 5:
                print(f"   ... and {len(implementer.migration_report['errors']) - 5} more")
        
        print("\n🚀 NEXT STEPS:")
        print("1. Test new URL structure manually")
        print("2. Verify 301 redirects work correctly")
        print("3. Update sitemap.xml with new URLs")
        print("4. Update internal navigation links")
        print("5. Test in staging before production deploy")
        
        return True
        
    except Exception as e:
        print(f"❌ Critical error during migration: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)