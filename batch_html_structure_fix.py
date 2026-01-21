#!/usr/bin/env python3
"""
Batch HTML Structure Fix Script
Fixes header structure for mobile menu in all HTML files
"""

import os
import re
from pathlib import Path

def fix_html_file(filepath):
    """Fix HTML structure for mobile menu"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False

        # Fix 1: Add mobile-menu-toggle button inside header-container if missing
        # Pattern: header-container with contact-button but no mobile-menu-toggle inside
        if 'class="header-container"' in content and 'mobile-menu-toggle' not in content.split('</nav>')[0].split('header-container')[1] if 'header-container' in content and '</nav>' in content else False:
            pass  # Complex check, will use simpler approach

        # Fix 2: Check if mobile-menu-toggle is inside header-container
        # If contact-button exists in header-container but mobile-menu-toggle doesn't follow it

        # Pattern to find contact-button div that's NOT followed by mobile-menu-toggle
        pattern_contact = r'(<div class="contact-button">.*?</div>\s*)(</div>\s*\n\s*(?:<button class="mobile-menu-toggle"|<!--))'

        if '<div class="contact-button">' in content:
            # Check if mobile-menu-toggle button follows contact-button in header-container
            header_section = re.search(r'<div class="header-container">.*?</div>\s*\n\s*(?=<)', content, re.DOTALL)
            if header_section:
                header_html = header_section.group(0)
                if 'mobile-menu-toggle' not in header_html:
                    # Need to add mobile-menu-toggle button after contact-button
                    new_button = '''
            <button class="mobile-menu-toggle" aria-label="Menüyü aç/kapat" aria-expanded="false" aria-controls="main-nav">
                <span class="hamburger-icon">☰</span>
            </button>'''

                    # Find the closing of contact-button div and add button after
                    pattern = r'(<div class="contact-button">.*?</div>)(\s*</div>)'
                    replacement = r'\1' + new_button + r'\2'

                    new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
                    if new_content != content:
                        content = new_content
                        modified = True

        # Fix 3: Add header-separator div if missing
        if 'class="header-separator"' not in content:
            # Add after </nav> before </header>
            pattern = r'(</nav>\s*)(</header>)'
            replacement = r'\1        <!-- Yellow separator line - visible on mobile -->\n        <div class="header-separator" aria-hidden="true"></div>\n    \2'

            new_content = re.sub(pattern, replacement, content, count=1)
            if new_content != content:
                content = new_content
                modified = True

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Fixed"
        else:
            return False, "No changes needed"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/macos/Documents/Projeler/DryAlle')

    # All folders to process
    folders = [
        base_path / 'bolgeler',
        base_path / 'hizmetler',
    ]

    fixed_count = 0
    skipped_count = 0
    error_count = 0

    # Process all HTML files
    for folder in folders:
        if folder.exists():
            for html_file in folder.glob('*.html'):
                success, message = fix_html_file(html_file)
                if success:
                    fixed_count += 1
                    print(f"✓ {html_file.name}")
                elif "No changes" in message:
                    skipped_count += 1
                else:
                    error_count += 1
                    print(f"✗ {html_file.name}: {message}")

    # Also process blog files
    blog_path = base_path / 'blog'
    if blog_path.exists():
        for html_file in blog_path.rglob('*.html'):
            if 'template' in html_file.name.lower():
                continue
            success, message = fix_html_file(html_file)
            if success:
                fixed_count += 1
                print(f"✓ {html_file.relative_to(base_path)}")
            elif "No changes" in message:
                skipped_count += 1
            else:
                error_count += 1
                print(f"✗ {html_file.relative_to(base_path)}: {message}")

    print(f"\n{'='*50}")
    print(f"Fixed: {fixed_count} files")
    print(f"No changes needed: {skipped_count} files")
    print(f"Errors: {error_count} files")

if __name__ == '__main__':
    main()
