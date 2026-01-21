#!/usr/bin/env python3
"""
Batch Mobile CSS Update Script
Updates all HTML files with premium mobile CSS
"""

import os
import re
from pathlib import Path

# Premium Mobile CSS to inject
PREMIUM_MOBILE_CSS = '''
    <!-- Premium Mobile CSS - Auto-injected -->
    <style>
        /* Premium Mobile Design System */
        .mobile-menu-toggle{
            display:none;
            background:linear-gradient(135deg, #f6ec3d 0%, #e8de35 100%);
            border:none;
            color:#1a1a1a;
            font-size:22px;
            cursor:pointer;
            padding:10px 14px;
            border-radius:10px;
            font-weight:600;
            flex-shrink:0;
            box-shadow:0 2px 8px rgba(0,0,0,0.15), inset 0 1px 0 rgba(255,255,255,0.3);
            transition:all 0.2s cubic-bezier(0.4, 0, 0.2, 1)
        }
        .mobile-menu-toggle:active{transform:scale(0.95);box-shadow:0 1px 4px rgba(0,0,0,0.2)}
        .header-separator{display:none;height:3px;background:linear-gradient(90deg, #f6ec3d 0%, #ffd700 50%, #f6ec3d 100%)}
        @media (max-width: 768px) {
            .header{position:relative;background:linear-gradient(180deg, #006a44 0%, #005a3a 100%) !important;box-shadow:0 2px 12px rgba(0,77,50,0.3)}
            .header-container{display:flex !important;flex-wrap:nowrap !important;justify-content:space-between !important;align-items:center !important;padding:14px 16px !important;gap:12px;min-height:64px}
            .top-bar{background:linear-gradient(135deg, #f6ec3d 0%, #f0e637 100%);padding:10px 0;box-shadow:0 1px 3px rgba(0,0,0,0.1)}
            .top-bar-content{padding:0 16px;font-size:13px;letter-spacing:0.01em}
            .logo{flex-shrink:1;min-width:0}
            .logo svg{width:130px !important;height:auto !important;max-width:130px !important;max-height:38px !important;filter:drop-shadow(0 1px 2px rgba(0,0,0,0.15))}
            .contact-button{display:none !important}
            .mobile-menu-toggle{display:flex !important;align-items:center;justify-content:center;min-width:48px;min-height:48px}
            .header-separator{display:block}
            .main-nav{display:none;position:absolute;top:100%;left:0;right:0;background:linear-gradient(180deg, #ffffff 0%, #fafafa 100%);box-shadow:0 8px 32px rgba(0,0,0,0.12);z-index:1000;border-top:3px solid #f6ec3d}
            .main-nav.open{display:block;animation:slideDown 0.25s cubic-bezier(0.4, 0, 0.2, 1)}
            @keyframes slideDown{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:translateY(0)}}
            .nav-menu{flex-direction:column;gap:0;padding:0}
            .nav-menu li{padding:0;border-bottom:1px solid rgba(0,0,0,0.06)}
            .nav-menu li:last-child{border-bottom:none}
            .nav-menu a{display:flex;align-items:center;padding:16px 20px;font-size:15px;font-weight:500;min-height:52px;text-transform:none;transition:all 0.15s ease}
            .nav-menu a:active{background:rgba(0,106,68,0.06)}
        }
    </style>
'''

# Check marker to avoid duplicate injection
CHECK_MARKER = "Premium Mobile CSS - Auto-injected"

def update_html_file(filepath):
    """Update a single HTML file with premium mobile CSS"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already updated
        if CHECK_MARKER in content:
            return False, "Already has premium CSS"

        # Find </head> and inject CSS before it
        if '</head>' in content:
            updated_content = content.replace('</head>', PREMIUM_MOBILE_CSS + '</head>')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True, "Updated successfully"
        else:
            return False, "No </head> tag found"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/macos/Documents/Projeler/DryAlle')

    # Folders to update
    folders = [
        base_path / 'bolgeler',
        base_path / 'hizmetler',
    ]

    # Also update blog article pages
    blog_path = base_path / 'blog'

    updated_count = 0
    skipped_count = 0
    error_count = 0

    # Process bolgeler and hizmetler
    for folder in folders:
        if folder.exists():
            for html_file in folder.glob('*.html'):
                success, message = update_html_file(html_file)
                if success:
                    updated_count += 1
                    print(f"✓ {html_file.name}")
                elif "Already" in message:
                    skipped_count += 1
                else:
                    error_count += 1
                    print(f"✗ {html_file.name}: {message}")

    # Process blog subdirectories
    if blog_path.exists():
        for html_file in blog_path.rglob('*.html'):
            # Skip main blog index (already updated)
            if html_file.name == 'index.html' and html_file.parent == blog_path:
                continue
            # Skip template files
            if 'template' in html_file.name.lower():
                continue

            success, message = update_html_file(html_file)
            if success:
                updated_count += 1
                print(f"✓ {html_file.relative_to(base_path)}")
            elif "Already" in message:
                skipped_count += 1
            else:
                error_count += 1
                print(f"✗ {html_file.relative_to(base_path)}: {message}")

    print(f"\n{'='*50}")
    print(f"Updated: {updated_count} files")
    print(f"Skipped (already done): {skipped_count} files")
    print(f"Errors: {error_count} files")

if __name__ == '__main__':
    main()
