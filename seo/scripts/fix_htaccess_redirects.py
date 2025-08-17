#!/usr/bin/env python3
"""
Fix .htaccess 301 Redirects for Blog URL Standardization
Corrects syntax errors and creates proper Apache redirect rules

Issues to fix:
1. Remove leading slashes from RewriteRule patterns
2. Ensure proper escaping
3. Add RewriteEngine On directive
4. Test redirect rules
"""

import os
import json
import re

def fix_htaccess_redirects():
    """Generate corrected .htaccess file"""
    project_root = "/Users/macos/Documents/Projeler/DryAlle"
    
    # Load URL mappings
    mappings_path = os.path.join(project_root, 'seo/analysis/url_standardization_report.json')
    
    try:
        with open(mappings_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        url_mappings = data['url_mappings']
        
        # Create corrected .htaccess content
        htaccess_content = []
        
        # Add Apache directives
        htaccess_content.extend([
            "# Blog URL Standardization - 301 Redirects",
            "# Generated: " + "2025-08-17 (Fixed)",
            "# Turkish to English URL Migration",
            "",
            "RewriteEngine On",
            "",
            "# Blog URL Redirects - Old to New Structure"
        ])
        
        # Sort mappings for better organization
        sorted_mappings = sorted(url_mappings.items(), key=lambda x: x[1]['old_url'])
        
        for new_url, mapping in sorted_mappings:
            old_url = mapping['old_url']
            
            # Remove leading slash and escape for Apache
            old_pattern = old_url[1:]  # Remove leading /
            old_pattern = old_pattern.replace('.html', r'\.html')
            old_pattern = re.escape(old_pattern).replace(r'\/', '/')
            
            # Add anchor to ensure exact match
            old_pattern = f"^{old_pattern}$"
            
            # Create redirect rule (no leading slash in target)
            redirect_rule = f"RewriteRule {old_pattern} {new_url} [R=301,L]"
            htaccess_content.append(redirect_rule)
        
        htaccess_content.extend([
            "",
            "# End Blog URL Redirects",
            ""
        ])
        
        # Write corrected .htaccess
        htaccess_path = os.path.join(project_root, '.htaccess')
        with open(htaccess_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(htaccess_content))
        
        print(f"✅ Fixed .htaccess with {len(url_mappings)} redirect rules")
        print(f"📁 Location: {htaccess_path}")
        
        # Test a few redirect patterns
        print("\n🔍 Sample Fixed Redirect Rules:")
        for i, line in enumerate(htaccess_content[7:12]):  # Show first 5 redirect rules
            if line.startswith('RewriteRule'):
                print(f"   {line}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing .htaccess: {str(e)}")
        return False

def create_nginx_config():
    """Create Nginx configuration for those using Nginx"""
    project_root = "/Users/macos/Documents/Projeler/DryAlle"
    
    try:
        # Load URL mappings
        mappings_path = os.path.join(project_root, 'seo/analysis/url_standardization_report.json')
        with open(mappings_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        url_mappings = data['url_mappings']
        
        # Create Nginx config
        nginx_content = []
        nginx_content.extend([
            "# Blog URL Standardization - Nginx Redirects",
            "# Generated: 2025-08-17",
            "# Add to your server block",
            ""
        ])
        
        for new_url, mapping in url_mappings.items():
            old_url = mapping['old_url']
            nginx_content.extend([
                f"location = {old_url} {{",
                f"    return 301 {new_url};",
                "}",
                ""
            ])
        
        # Save Nginx config
        nginx_path = os.path.join(project_root, 'seo/redirects/nginx_blog_redirects.conf')
        os.makedirs(os.path.dirname(nginx_path), exist_ok=True)
        
        with open(nginx_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(nginx_content))
        
        print(f"✅ Created Nginx config: {nginx_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating Nginx config: {str(e)}")
        return False

def validate_redirects():
    """Validate redirect rules syntax"""
    project_root = "/Users/macos/Documents/Projeler/DryAlle"
    htaccess_path = os.path.join(project_root, '.htaccess')
    
    try:
        with open(htaccess_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for common issues
        issues = []
        
        if 'RewriteEngine On' not in content:
            issues.append("Missing 'RewriteEngine On' directive")
        
        # Check for double slashes in patterns
        if '//' in content:
            issues.append("Double slashes found in redirect rules")
        
        # Count redirect rules
        redirect_count = len(re.findall(r'^RewriteRule', content, re.MULTILINE))
        
        if issues:
            print("⚠️ Validation Issues Found:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print(f"✅ .htaccess validation passed")
            print(f"📊 {redirect_count} redirect rules found")
        
        return len(issues) == 0
        
    except Exception as e:
        print(f"❌ Error validating .htaccess: {str(e)}")
        return False

def main():
    """Execute .htaccess fixes"""
    print("🔧 FIXING .HTACCESS REDIRECT RULES")
    print("=" * 40)
    
    try:
        # Fix .htaccess
        if fix_htaccess_redirects():
            print("✅ .htaccess redirects fixed")
        
        # Create Nginx alternative
        if create_nginx_config():
            print("✅ Nginx config created")
        
        # Validate results
        if validate_redirects():
            print("✅ Redirect validation passed")
        
        print("\n🚀 NEXT STEPS:")
        print("1. Test redirects on staging server")
        print("2. Monitor redirect performance")
        print("3. Update sitemap with new URLs")
        print("4. Deploy to production")
        
        return True
        
    except Exception as e:
        print(f"❌ Critical error: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)