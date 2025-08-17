#!/bin/bash

# Blog Image Optimization Implementation Script
# Phase 1: Kuru Temizleme Category

set -e

# Check bash version for associative array support
if [[ ${BASH_VERSION%%.*} -lt 4 ]]; then
    echo "Warning: This script requires Bash 4.0+ for associative arrays"
    echo "Current version: $BASH_VERSION"
fi

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Base directory
BLOG_DIR="/Users/macos/Documents/Projeler/DryAlle/blog"
TEMP_DIR="/tmp/kuru-temizleme-images"

echo -e "${BLUE}=== DRY ALLE BLOG IMAGE OPTIMIZATION - PHASE 1 ===${NC}"
echo -e "${BLUE}Target: Kuru Temizleme Category (12 unique images)${NC}\n"

# Create temporary directory
mkdir -p "$TEMP_DIR"

# Array of target directories and their SEO-optimized image names
declare -A DIRECTORIES=(
    ["ultimate-turkish-dry-cleaning-guide"]="kuru-temizleme-kapsamli-rehber-turkiye-2025.webp"
    ["istanbul-anatolian-side-dry-cleaning"]="istanbul-anadolu-yakasi-kuru-temizleme-profesyonel.webp"
    ["dry-cleaning-kimyasallari-guvenligi"]="kuru-temizleme-kimyasal-guvenlik-cevre-dostu.webp"
    ["dry-cleaning-eco-friendly-alternatifler"]="cevre-dostu-kuru-temizleme-alternatif-yontemler.webp"
    ["hot-weather-dry-cleaning"]="sicak-hava-kuru-temizleme-yaz-bakimi.webp"
    ["winter-dry-cleaning-tips"]="kis-kuru-temizleme-ipuclari-mont-palto.webp"
    ["dry-cleaning-perfect-results"]="mukemmel-kuru-temizleme-sonuclari-kalite.webp"
    ["dry-cleaning-quality-control"]="kuru-temizleme-kalite-kontrol-standardlari.webp"
    ["dry-cleaning-hatalari-ve-cozumleri"]="kuru-temizleme-hatalari-cozum-onerileri.webp"
    ["dry-cleaning-sigorta-ve-garanti"]="kuru-temizleme-sigorta-garanti-koruma.webp"
    ["is-kiyafetleri-professional-care"]="is-kiyafetleri-profesyonel-bakim-takimelbise.webp"
    ["ipek-kumaslar-dry-cleaning-guide"]="ipek-kumash-hassas-kuru-temizleme-bakim.webp"
)

# Function to check if directory exists
check_directory() {
    local dir="$1"
    if [ ! -d "$BLOG_DIR/$dir" ]; then
        echo -e "${RED}ERROR: Directory not found: $BLOG_DIR/$dir${NC}"
        return 1
    fi
    return 0
}

# Function to backup current images
backup_images() {
    echo -e "${YELLOW}Creating backup of current images...${NC}"
    local backup_dir="$BLOG_DIR/image-backups-$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$backup_dir"
    
    for dir in "${!DIRECTORIES[@]}"; do
        if check_directory "$dir"; then
            cp "$BLOG_DIR/$dir/featured-image.webp" "$backup_dir/${dir}-featured-image.webp" 2>/dev/null || true
        fi
    done
    
    echo -e "${GREEN}Backup created at: $backup_dir${NC}"
}

# Function to verify current duplicate status
verify_duplicates() {
    echo -e "${YELLOW}Verifying current duplicate status...${NC}"
    
    local temp_file="/tmp/md5_check.txt"
    > "$temp_file"
    
    for dir in "${!DIRECTORIES[@]}"; do
        if check_directory "$dir" && [ -f "$BLOG_DIR/$dir/featured-image.webp" ]; then
            md5 "$BLOG_DIR/$dir/featured-image.webp" >> "$temp_file"
        fi
    done
    
    local unique_count=$(cut -d' ' -f4 "$temp_file" | sort | uniq | wc -l)
    local total_count=$(wc -l < "$temp_file")
    
    echo -e "Total images: $total_count"
    echo -e "Unique images: $unique_count"
    
    if [ "$unique_count" -eq 1 ]; then
        echo -e "${RED}CONFIRMED: All images are duplicates (as expected)${NC}"
    else
        echo -e "${YELLOW}WARNING: Some images may already be unique${NC}"
    fi
    
    rm "$temp_file"
}

# Function to display download instructions
show_download_instructions() {
    echo -e "\n${BLUE}=== MANUAL DOWNLOAD INSTRUCTIONS ===${NC}"
    echo -e "${YELLOW}Visit the following URLs to download appropriate images:${NC}\n"
    
    echo -e "1. Unsplash - Primary Source:"
    echo -e "   https://unsplash.com/s/photos/dry-cleaning"
    echo -e "   https://unsplash.com/s/photos/commercial-laundry"
    echo -e "   https://unsplash.com/s/photos/business-suits"
    echo -e "   https://unsplash.com/s/photos/steam-cleaning\n"
    
    echo -e "2. Search Terms to Use:"
    echo -e "   - 'professional dry cleaning equipment'"
    echo -e "   - 'business suits hanging'"
    echo -e "   - 'commercial laundry machines'"
    echo -e "   - 'steam iron professional'"
    echo -e "   - 'textile care industrial'"
    echo -e "   - 'dry cleaning shop interior'\n"
    
    echo -e "${GREEN}Download 12 unique, high-quality images and save them to:${NC}"
    echo -e "${BLUE}$TEMP_DIR/${NC}\n"
    
    echo -e "${YELLOW}Naming Convention:${NC}"
    local counter=1
    for dir in "${!DIRECTORIES[@]}"; do
        echo -e "  $counter. ${DIRECTORIES[$dir]} → $dir/"
        ((counter++))
    done
}

# Function to optimize and replace images (when images are available)
replace_images() {
    echo -e "\n${BLUE}=== IMAGE REPLACEMENT PROCESS ===${NC}"
    
    # Check if optimized images exist in temp directory
    local images_found=0
    for image_name in "${DIRECTORIES[@]}"; do
        if [ -f "$TEMP_DIR/$image_name" ]; then
            ((images_found++))
        fi
    done
    
    if [ $images_found -eq 0 ]; then
        echo -e "${RED}No optimized images found in $TEMP_DIR${NC}"
        echo -e "${YELLOW}Please download and prepare images first.${NC}"
        return 1
    fi
    
    echo -e "${GREEN}Found $images_found optimized images${NC}"
    
    # Replace images
    for dir in "${!DIRECTORIES[@]}"; do
        local image_name="${DIRECTORIES[$dir]}"
        local source_file="$TEMP_DIR/$image_name"
        local target_file="$BLOG_DIR/$dir/featured-image.webp"
        
        if [ -f "$source_file" ] && check_directory "$dir"; then
            echo -e "Replacing: $dir/featured-image.webp"
            cp "$source_file" "$target_file"
            
            # Verify file size
            local file_size=$(stat -f%z "$target_file" 2>/dev/null || stat -c%s "$target_file" 2>/dev/null)
            if [ "$file_size" -gt 0 ]; then
                echo -e "${GREEN}  ✓ Success (${file_size} bytes)${NC}"
            else
                echo -e "${RED}  ✗ Failed (0 bytes)${NC}"
            fi
        else
            echo -e "${YELLOW}  ⚠ Skipping: $source_file not found${NC}"
        fi
    done
}

# Function to verify final results
verify_results() {
    echo -e "\n${BLUE}=== VERIFICATION ===${NC}"
    
    echo -e "${YELLOW}Checking for unique images...${NC}"
    local temp_file="/tmp/final_md5_check.txt"
    > "$temp_file"
    
    for dir in "${!DIRECTORIES[@]}"; do
        if check_directory "$dir" && [ -f "$BLOG_DIR/$dir/featured-image.webp" ]; then
            local md5_result=$(md5 "$BLOG_DIR/$dir/featured-image.webp")
            echo "$md5_result" >> "$temp_file"
            
            # Get file size
            local file_size=$(stat -f%z "$BLOG_DIR/$dir/featured-image.webp" 2>/dev/null || stat -c%s "$BLOG_DIR/$dir/featured-image.webp" 2>/dev/null)
            echo -e "  $dir: ${file_size} bytes"
        fi
    done
    
    local unique_count=$(cut -d' ' -f4 "$temp_file" | sort | uniq | wc -l)
    local total_count=$(wc -l < "$temp_file")
    
    echo -e "\n${BLUE}Final Results:${NC}"
    echo -e "Total images: $total_count"
    echo -e "Unique images: $unique_count"
    
    if [ "$unique_count" -eq "$total_count" ]; then
        echo -e "${GREEN}✓ SUCCESS: All images are now unique!${NC}"
    else
        echo -e "${RED}✗ WARNING: Some duplicates still exist${NC}"
        echo -e "${YELLOW}Duplicate checksums:${NC}"
        cut -d' ' -f4 "$temp_file" | sort | uniq -d
    fi
    
    rm "$temp_file"
}

# Main execution
main() {
    echo -e "${BLUE}Starting Phase 1 Implementation...${NC}\n"
    
    # Step 1: Verify current state
    verify_duplicates
    
    # Step 2: Create backup
    backup_images
    
    # Step 3: Show download instructions
    show_download_instructions
    
    echo -e "\n${YELLOW}=== NEXT STEPS ===${NC}"
    echo -e "1. Download 12 unique images following the instructions above"
    echo -e "2. Save them with the exact names specified to: $TEMP_DIR"
    echo -e "3. Run this script again with the 'replace' argument: $0 replace"
    echo -e "4. Verify results with: $0 verify\n"
    
    # If user provided 'replace' argument, attempt replacement
    if [ "$1" = "replace" ]; then
        replace_images
        verify_results
    elif [ "$1" = "verify" ]; then
        verify_results
    fi
}

# Execute main function with all arguments
main "$@"