#!/usr/bin/env python3
"""
Cleanup duplicate mobile-menu-toggle buttons and extra closing divs
"""

import re
from pathlib import Path

def cleanup_file(filepath):
    """Remove duplicate mobile-menu-toggle buttons and extra closing divs"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Pattern: After </div> (header-container close), there's duplicate button + extra </div>
        # This pattern matches:
        # </div>
        #
        #
        #     <button class="mobile-menu-toggle"...>
        #         <span class="hamburger-icon">☰</span>
        #     </button>
        # </div>

        pattern = r'(</div>)\s*\n\s*\n\s*<button class="mobile-menu-toggle"[^>]*>\s*<span class="hamburger-icon">☰</span>\s*</button>\s*</div>'

        new_content = re.sub(pattern, r'\1', content)

        if new_content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, "Cleaned"
        else:
            return False, "No duplicates found"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/macos/Documents/Projeler/DryAlle')

    all_html_files = list(base_path.rglob('*.html'))

    cleaned = 0
    skipped = 0

    for html_file in all_html_files:
        if 'template' in html_file.name.lower():
            continue
        if '.git' in str(html_file):
            continue

        success, msg = cleanup_file(html_file)
        if success:
            cleaned += 1
            print(f"✓ {html_file.relative_to(base_path)}")
        else:
            skipped += 1

    print(f"\n{'='*50}")
    print(f"Cleaned: {cleaned} files")
    print(f"Skipped: {skipped} files")

if __name__ == '__main__':
    main()
