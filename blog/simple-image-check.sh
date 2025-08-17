#!/bin/bash

# Simple Image Optimization Check Script
# Compatible with macOS default bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

BLOG_DIR="/Users/macos/Documents/Projeler/DryAlle/blog"

echo -e "${BLUE}=== DRY ALLE BLOG IMAGE OPTIMIZATION CHECK ===${NC}\n"

# List of Kuru Temizleme directories
directories=(
    "ultimate-turkish-dry-cleaning-guide"
    "istanbul-anatolian-side-dry-cleaning"
    "dry-cleaning-kimyasallari-guvenligi"
    "dry-cleaning-eco-friendly-alternatifler"
    "hot-weather-dry-cleaning"
    "winter-dry-cleaning-tips"
    "dry-cleaning-perfect-results"
    "dry-cleaning-quality-control"
    "dry-cleaning-hatalari-ve-cozumleri"
    "dry-cleaning-sigorta-ve-garanti"
    "is-kiyafetleri-professional-care"
    "ipek-kumaslar-dry-cleaning-guide"
)

echo -e "${YELLOW}Checking current image status...${NC}"

# Create temp file for MD5 checks
temp_file="/tmp/image_md5_check.txt"
> "$temp_file"

# Check each directory
for dir in "${directories[@]}"; do
    image_path="$BLOG_DIR/$dir/featured-image.webp"
    if [ -f "$image_path" ]; then
        md5_result=$(md5 "$image_path")
        echo "$md5_result" >> "$temp_file"
        file_size=$(stat -f%z "$image_path" 2>/dev/null)
        echo -e "  $dir: ${file_size} bytes"
    else
        echo -e "${RED}  $dir: IMAGE NOT FOUND${NC}"
    fi
done

echo -e "\n${BLUE}Duplicate Analysis:${NC}"
unique_count=$(cut -d' ' -f4 "$temp_file" | sort | uniq | wc -l | tr -d ' ')
total_count=$(wc -l < "$temp_file" | tr -d ' ')

echo -e "Total images found: $total_count"
echo -e "Unique checksums: $unique_count"

if [ "$unique_count" -eq 1 ] && [ "$total_count" -gt 1 ]; then
    echo -e "${RED}CONFIRMED: All images are duplicates${NC}"
    echo -e "Common MD5: $(cut -d' ' -f4 "$temp_file" | head -1)"
elif [ "$unique_count" -eq "$total_count" ]; then
    echo -e "${GREEN}SUCCESS: All images are unique${NC}"
else
    echo -e "${YELLOW}MIXED: Some duplicates exist${NC}"
fi

# Create backup if duplicates exist
if [ "$unique_count" -eq 1 ] && [ "$total_count" -gt 1 ]; then
    echo -e "\n${YELLOW}Creating backup of duplicate images...${NC}"
    backup_dir="$BLOG_DIR/duplicate-backup-$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$backup_dir"
    
    for dir in "${directories[@]}"; do
        image_path="$BLOG_DIR/$dir/featured-image.webp"
        if [ -f "$image_path" ]; then
            cp "$image_path" "$backup_dir/${dir}-featured-image.webp"
        fi
    done
    
    echo -e "${GREEN}Backup created: $backup_dir${NC}"
fi

rm "$temp_file"

echo -e "\n${BLUE}NEXT STEPS:${NC}"
echo -e "1. Download 12 unique dry cleaning images from Unsplash"
echo -e "2. Optimize them to WebP format (50-150KB each)"
echo -e "3. Replace featured-image.webp in each directory"
echo -e "4. Verify all images are unique\n"

# Show required image naming
echo -e "${YELLOW}Required SEO-optimized image names:${NC}"
echo -e "  1. ultimate-turkish-dry-cleaning-guide → kuru-temizleme-kapsamli-rehber-turkiye-2025.webp"
echo -e "  2. istanbul-anatolian-side-dry-cleaning → istanbul-anadolu-yakasi-kuru-temizleme-profesyonel.webp"
echo -e "  3. dry-cleaning-kimyasallari-guvenligi → kuru-temizleme-kimyasal-guvenlik-cevre-dostu.webp"
echo -e "  4. dry-cleaning-eco-friendly-alternatifler → cevre-dostu-kuru-temizleme-alternatif-yontemler.webp"
echo -e "  5. hot-weather-dry-cleaning → sicak-hava-kuru-temizleme-yaz-bakimi.webp"
echo -e "  6. winter-dry-cleaning-tips → kis-kuru-temizleme-ipuclari-mont-palto.webp"
echo -e "  7. dry-cleaning-perfect-results → mukemmel-kuru-temizleme-sonuclari-kalite.webp"
echo -e "  8. dry-cleaning-quality-control → kuru-temizleme-kalite-kontrol-standardlari.webp"
echo -e "  9. dry-cleaning-hatalari-ve-cozumleri → kuru-temizleme-hatalari-cozum-onerileri.webp"
echo -e " 10. dry-cleaning-sigorta-ve-garanti → kuru-temizleme-sigorta-garanti-koruma.webp"
echo -e " 11. is-kiyafetleri-professional-care → is-kiyafetleri-profesyonel-bakim-takimelbise.webp"
echo -e " 12. ipek-kumaslar-dry-cleaning-guide → ipek-kumash-hassas-kuru-temizleme-bakim.webp"