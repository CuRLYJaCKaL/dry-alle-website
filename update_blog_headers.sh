#!/bin/bash

# Script to update all blog article headers with the new professional template

BLOG_DIR="/Users/macos/Documents/Projeler/DryAlle/blog"

# Define the old header pattern to replace
OLD_HEADER_START="<!-- Corporate Header - STANDARDIZED -->"
OLD_HEADER_END="</header>"

# Define the new professional header
NEW_HEADER='<!-- Professional Blog Header - 30 Year UX Expert Design -->
<div class="top-bar">
<div class="top-bar-content">
<strong>ÜCRETSİZ KAPIDAN TESLİMAT</strong> • İstanbul'"'"'un Her Yerine • <strong>ARAYINIZ: <a href="tel:+905433527474">0 (543) 352 74 74</a></strong>
</div>
</div>

<!-- Unified Header with Navigation -->
<header class="header">
<div class="header-container">
<div class="logo">
<a href="../../index.html" style="text-decoration: none;">
<svg width="200" height="60" viewBox="0 0 390 105" xmlns="http://www.w3.org/2000/svg">
<text x="195" y="58" font-family="Dancing Script, cursive" font-size="60" font-weight="700" fill="#f6ec3d" text-anchor="middle">Dry Alle</text>
<text x="195" y="86" font-family="Roboto, sans-serif" font-size="16" font-weight="600" fill="white" letter-spacing="2px" text-anchor="middle">KURU TEMİZLEME</text>
</svg>
</a>
</div>

<nav>
<ul class="nav-menu">
<li><a href="../../index.html">ANASAYFA</a></li>
<li><a href="../../hizmetler.html">HİZMETLER</a></li>
<li><a href="../index.html" class="active">BLOG</a></li>
<li><a href="../../sss.html">SSS</a></li>
<li><a href="../../iletisim.html">İLETİŞİM</a></li>
</ul>
</nav>

<div class="contact-button">
<div class="phone-icon">📞</div>
<span>İletişim</span>
</div>
</div>
</header>'

# Count of files processed
count=0

# Find all blog article index.html files and process them
find "$BLOG_DIR" -name "index.html" -path "*/blog/*/index.html" | while read -r file; do
    if [[ "$file" != *"/blog/index.html" && "$file" != *"/blog/template-header.html" ]]; then
        echo "Processing: $file"
        
        # Create a temporary file
        temp_file=$(mktemp)
        
        # Process the file to replace the header section
        awk -v new_header="$NEW_HEADER" '
        BEGIN { in_header = 0; header_replaced = 0 }
        /<!-- Corporate Header - STANDARDIZED -->/ { 
            in_header = 1
            print new_header
            header_replaced = 1
            next
        }
        /<\/header>/ && in_header == 1 { 
            in_header = 0
            next
        }
        in_header == 0 { print }
        ' "$file" > "$temp_file"
        
        # Replace the original file
        mv "$temp_file" "$file"
        
        count=$((count + 1))
        echo "Updated: $file"
    fi
done

echo "Total files updated: $count"