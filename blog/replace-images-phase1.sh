#!/bin/bash

# Image Replacement Script - Phase 1: Kuru Temizleme
# Run this after downloading and optimizing all 12 images

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

BLOG_DIR="/Users/macos/Documents/Projeler/DryAlle/blog"
SOURCE_DIR="/tmp/kuru-temizleme-optimized"

echo -e "${BLUE}=== KURU TEMİZLEME IMAGE REPLACEMENT - PHASE 1 ===${NC}\n"

# Image mapping: source_file:target_directory
images=(
    "kuru-temizleme-kapsamli-rehber-turkiye-2025.webp:ultimate-turkish-dry-cleaning-guide"
    "istanbul-anadolu-yakasi-kuru-temizleme-profesyonel.webp:istanbul-anatolian-side-dry-cleaning"
    "kuru-temizleme-kimyasal-guvenlik-cevre-dostu.webp:dry-cleaning-kimyasallari-guvenligi"
    "cevre-dostu-kuru-temizleme-alternatif-yontemler.webp:dry-cleaning-eco-friendly-alternatifler"
    "sicak-hava-kuru-temizleme-yaz-bakimi.webp:hot-weather-dry-cleaning"
    "kis-kuru-temizleme-ipuclari-mont-palto.webp:winter-dry-cleaning-tips"
    "mukemmel-kuru-temizleme-sonuclari-kalite.webp:dry-cleaning-perfect-results"
    "kuru-temizleme-kalite-kontrol-standardlari.webp:dry-cleaning-quality-control"
    "kuru-temizleme-hatalari-cozum-onerileri.webp:dry-cleaning-hatalari-ve-cozumleri"
    "kuru-temizleme-sigorta-garanti-koruma.webp:dry-cleaning-sigorta-ve-garanti"
    "is-kiyafetleri-profesyonel-bakim-takimelbise.webp:is-kiyafetleri-professional-care"
    "ipek-kumash-hassas-kuru-temizleme-bakim.webp:ipek-kumaslar-dry-cleaning-guide"
)

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}ERROR: Source directory not found: $SOURCE_DIR${NC}"
    echo -e "${YELLOW}Please ensure you have downloaded and optimized images to this directory first.${NC}"
    exit 1
fi

echo -e "${YELLOW}Checking for optimized images...${NC}"

# Count available images
available_count=0
missing_images=()

for image_mapping in "${images[@]}"; do
    source_file=$(echo "$image_mapping" | cut -d: -f1)
    source_path="$SOURCE_DIR/$source_file"
    
    if [ -f "$source_path" ]; then
        file_size=$(stat -f%z "$source_path" 2>/dev/null)
        file_size_kb=$((file_size / 1024))
        echo -e "${GREEN}  ✓ $source_file (${file_size_kb}KB)${NC}"
        ((available_count++))
    else
        echo -e "${RED}  ✗ $source_file (MISSING)${NC}"
        missing_images+=("$source_file")
    fi
done

echo -e "\n${BLUE}Status: $available_count/12 images ready${NC}"

if [ $available_count -eq 0 ]; then
    echo -e "${RED}No optimized images found. Please download and optimize images first.${NC}"
    echo -e "${YELLOW}Follow the instructions in DOWNLOAD-GUIDE-PHASE1.md${NC}"
    exit 1
fi

if [ $available_count -lt 12 ]; then
    echo -e "${YELLOW}Missing images:${NC}"
    for missing in "${missing_images[@]}"; do
        echo -e "  - $missing"
    done
    echo -e "\n${YELLOW}Do you want to proceed with partial replacement? (y/N):${NC}"
    read -r proceed
    if [[ ! "$proceed" =~ ^[Yy]$ ]]; then
        echo -e "${BLUE}Aborted. Complete all downloads first.${NC}"
        exit 0
    fi
fi

echo -e "\n${BLUE}Starting image replacement...${NC}"

# Replace images
replaced_count=0
failed_count=0

for image_mapping in "${images[@]}"; do
    source_file=$(echo "$image_mapping" | cut -d: -f1)
    target_dir=$(echo "$image_mapping" | cut -d: -f2)
    
    source_path="$SOURCE_DIR/$source_file"
    target_path="$BLOG_DIR/$target_dir/featured-image.webp"
    
    if [ -f "$source_path" ]; then
        if [ -d "$BLOG_DIR/$target_dir" ]; then
            # Create backup of current image
            if [ -f "$target_path" ]; then
                cp "$target_path" "$target_path.backup-$(date +%Y%m%d-%H%M%S)"
            fi
            
            # Replace image
            cp "$source_path" "$target_path"
            
            if [ $? -eq 0 ]; then
                new_size=$(stat -f%z "$target_path" 2>/dev/null)
                new_size_kb=$((new_size / 1024))
                echo -e "${GREEN}  ✓ $target_dir (${new_size_kb}KB)${NC}"
                ((replaced_count++))
            else
                echo -e "${RED}  ✗ $target_dir (COPY FAILED)${NC}"
                ((failed_count++))
            fi
        else
            echo -e "${RED}  ✗ $target_dir (DIRECTORY NOT FOUND)${NC}"
            ((failed_count++))
        fi
    else
        echo -e "${YELLOW}  ⚠ $target_dir (SOURCE IMAGE MISSING)${NC}"
    fi
done

echo -e "\n${BLUE}Replacement Summary:${NC}"
echo -e "  Successful: $replaced_count"
echo -e "  Failed: $failed_count"
echo -e "  Skipped: $((12 - replaced_count - failed_count))"

# Verify results
echo -e "\n${YELLOW}Verifying uniqueness...${NC}"

temp_file="/tmp/verification_md5.txt"
> "$temp_file"

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

for dir in "${directories[@]}"; do
    image_path="$BLOG_DIR/$dir/featured-image.webp"
    if [ -f "$image_path" ]; then
        md5_result=$(md5 "$image_path")
        echo "$md5_result" >> "$temp_file"
    fi
done

unique_count=$(cut -d' ' -f4 "$temp_file" | sort | uniq | wc -l | tr -d ' ')
total_count=$(wc -l < "$temp_file" | tr -d ' ')

echo -e "${BLUE}Final Verification:${NC}"
echo -e "  Total images: $total_count"
echo -e "  Unique checksums: $unique_count"

if [ "$unique_count" -eq "$total_count" ] && [ "$total_count" -eq 12 ]; then
    echo -e "${GREEN}🎉 SUCCESS: All 12 images are now unique!${NC}"
    echo -e "${GREEN}Phase 1 (Kuru Temizleme) completed successfully.${NC}"
elif [ "$unique_count" -eq "$total_count" ]; then
    echo -e "${YELLOW}✓ PARTIAL SUCCESS: All available images are unique (${total_count}/12)${NC}"
else
    echo -e "${RED}⚠ WARNING: Some duplicates still exist${NC}"
    echo -e "${YELLOW}Duplicate checksums found - manual review needed${NC}"
fi

rm "$temp_file"

# Final recommendations
echo -e "\n${BLUE}Next Steps:${NC}"
if [ "$unique_count" -eq 12 ] && [ "$total_count" -eq 12 ]; then
    echo -e "1. ✅ Phase 1 complete - proceed to Phase 2 (Halı Yıkama category)"
    echo -e "2. ✅ Test website loading performance"
    echo -e "3. ✅ Verify images display correctly in browsers"
else
    echo -e "1. Complete any missing image downloads"
    echo -e "2. Re-run this script after all 12 images are ready"
    echo -e "3. Verify final uniqueness before proceeding to Phase 2"
fi

echo -e "\n${GREEN}Phase 1 Image Replacement Process Complete!${NC}"