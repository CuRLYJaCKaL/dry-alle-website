#!/bin/bash

# Read the new related section template
NEW_TEMPLATE=$(cat temp_related_section.html)

# Counter for processed files
count=0

# Process each file
while IFS= read -r file; do
    if [ -f "$file" ]; then
        echo "Processing: $file"
        
        # Create backup
        cp "$file" "${file}.backup"
        
        # Use sed to replace the old section with new template
        # First, find the start and end of the old section and replace it
        python3 -c "
import sys
import re

with open('$file', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match the entire related-articles section
old_pattern = r'<!-- Related Articles -->\s*<section class=\"related-articles\">.*?</section>'

# New template
new_template = '''$NEW_TEMPLATE'''

# Replace
updated_content = re.sub(old_pattern, new_template, content, flags=re.DOTALL)

with open('$file', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print('Updated successfully')
"
        
        if [ $? -eq 0 ]; then
            ((count++))
            echo "✅ Updated $file ($count/27)"
        else
            echo "❌ Failed to update $file"
            # Restore backup if failed
            mv "${file}.backup" "$file"
        fi
    fi
done < temp_files_to_update.txt

echo "Total files updated: $count"