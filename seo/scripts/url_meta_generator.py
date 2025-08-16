#!/usr/bin/env python3
"""
DryAlle URL Meta Master Generator
Creates comprehensive CSV with all 341 planned pages for Phase 3 implementation
"""

import csv
import os
from pathlib import Path

def turkish_to_slug(text):
    """Convert Turkish text to URL-friendly slug"""
    # Turkish character mapping
    char_map = {
        'ç': 'c', 'Ç': 'c',
        'ğ': 'g', 'Ğ': 'g', 
        'ö': 'o', 'Ö': 'o',
        'ş': 's', 'Ş': 's',
        'ü': 'u', 'Ü': 'u',
        'ı': 'i', 'I': 'i',
        'İ': 'i', 'i': 'i'
    }
    
    # Apply character mapping
    for turkish, latin in char_map.items():
        text = text.replace(turkish, latin)
    
    # Convert to lowercase and replace spaces/special chars with hyphens
    text = text.lower()
    text = text.replace(' ', '-')
    text = text.replace("'", '')
    text = text.replace('.', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    
    return text

def generate_meta_data():
    """Generate all URL and meta data for 341 planned pages"""
    
    # District definitions
    districts = {
        'kadikoy': {
            'name': 'Kadıköy',
            'slug': 'kadikoy',
            'neighborhoods': [
                'Moda', 'Fenerbahçe', 'Çamlıca', 'Sahrayı Cedit', 'Kızıltoprak',
                'Hasanpaşa', 'Rasimpaşa', 'Zühtüpaşa', 'Osmanağa', 'Göztepe',
                'Erenköy', 'Suadiye', 'Caddebostan', 'Bostancı', 'Kalamış',
                'Feneryolu', 'Koşuyolu', 'Altıntepe', 'Fikirtepe'
            ]
        },
        'atasehir': {
            'name': 'Ataşehir',
            'slug': 'atasehir', 
            'neighborhoods': [
                'Ataşehir', 'Küçükbakkalköy', 'Ferhatpaşa', 'Barbaros',
                'Kayışdağı', 'Esatpaşa', 'Mustafa Kemal', 'Yenisahra',
                'İnönü', 'Örnek', 'Ataşehir OSB', 'Batı Ataşehir'
            ]
        }
    }
    
    # Service definitions
    services = [
        {'name': 'Kuru Temizleme', 'slug': 'kuru-temizleme', 'priority': 'High'},
        {'name': 'Gelinlik Temizleme', 'slug': 'gelinlik-temizleme', 'priority': 'High'},
        {'name': 'Abiye Temizleme', 'slug': 'abiye-temizleme', 'priority': 'High'},
        {'name': 'Valiz Temizleme', 'slug': 'valiz-temizleme', 'priority': 'Medium'},
        {'name': 'Bavul Temizleme', 'slug': 'bavul-temizleme', 'priority': 'Medium'},
        {'name': 'Halı Yıkama', 'slug': 'hali-yikama', 'priority': 'High'},
        {'name': 'Koltuk Yıkama', 'slug': 'koltuk-yikama', 'priority': 'High'},
        {'name': 'Perde Temizleme', 'slug': 'perde-temizleme', 'priority': 'Medium'},
        {'name': 'Ev Tekstili Temizliği', 'slug': 'ev-tekstili-temizligi', 'priority': 'Medium'},
        {'name': 'Çanta Temizleme', 'slug': 'canta-temizleme', 'priority': 'Medium'},
        {'name': 'Kumaş Deri Boyama', 'slug': 'kumas-deri-boyama', 'priority': 'Medium'},
        {'name': 'Lostra Hizmeti', 'slug': 'lostra-hizmeti', 'priority': 'Medium'},
        {'name': 'Ütü Hizmetleri', 'slug': 'utu-hizmetleri', 'priority': 'Low'}
    ]
    
    master_data = []
    
    # 1. Homepage
    master_data.append({
        'Page Type': 'Homepage',
        'District': '',
        'Neighborhood': '',
        'Service': '',
        'URL Slug': '/',
        'Full URL': 'https://dryallekurutemizleme.com/',
        'Title': 'Kuru Temizleme Halı Yıkama Koltuk Yıkama İstanbul Kadıköy Ataşehir | Dry Alle',
        'H1': 'İstanbul Anadolu Yakası Kuru Temizleme, Halı Yıkama ve Koltuk Yıkama Uzmanı',
        'Meta Description': 'İstanbul Anadolu Yakası\'nda 25 yıllık deneyimle kuru temizleme, halı yıkama, koltuk yıkama hizmeti. Kadıköy ve Ataşehir\'e ücretsiz teslimat. Hemen arayın!',
        'Priority': '1.0',
        'Status': 'Exists'
    })
    
    # 2. Service Hub
    master_data.append({
        'Page Type': 'Service Hub',
        'District': '',
        'Neighborhood': '',
        'Service': '',
        'URL Slug': '/hizmetler/',
        'Full URL': 'https://dryallekurutemizleme.com/hizmetler/',
        'Title': 'Hizmetlerimiz | Kuru Temizleme Halı Yıkama İstanbul | Dry Alle',
        'H1': 'İstanbul Anadolu Yakası Tekstil Hizmetleri',
        'Meta Description': 'İstanbul Kadıköy ve Ataşehir\'de kuru temizleme, halı yıkama, koltuk yıkama, gelinlik temizleme hizmetleri. 25 yıllık deneyim, ücretsiz teslimat.',
        'Priority': '0.9',
        'Status': 'Create'
    })
    
    # 3. Service Pages
    for service in services:
        service_name = service['name']
        service_slug = service['slug']
        
        title = f"{service_name} İstanbul Kadıköy Ataşehir | Dry Alle"
        h1 = f"İstanbul {service_name} Hizmeti"
        meta_desc = f"İstanbul Kadıköy ve Ataşehir'de profesyonel {service_name.lower()} hizmeti. 25 yıllık deneyim, ücretsiz teslimat. Anadolu Yakası'nın tüm semtlerine hizmet."
        
        # Ensure meta description is under 155 characters
        if len(meta_desc) > 155:
            meta_desc = meta_desc[:152] + "..."
        
        priority = '0.9' if service['priority'] == 'High' else '0.8'
        status = 'Exists' if service_slug in ['kuru-temizleme', 'hali-yikama', 'koltuk-yikama', 
                                              'perde-temizleme', 'ev-tekstili-temizligi', 
                                              'canta-temizleme', 'kumas-deri-boyama', 
                                              'lostra-hizmeti', 'utu-hizmetleri'] else 'Create'
        
        master_data.append({
            'Page Type': 'Service Page',
            'District': '',
            'Neighborhood': '',
            'Service': service_name,
            'URL Slug': f'/hizmetler/{service_slug}.html',
            'Full URL': f'https://dryallekurutemizleme.com/hizmetler/{service_slug}.html',
            'Title': title,
            'H1': h1,
            'Meta Description': meta_desc,
            'Priority': priority,
            'Status': status
        })
    
    # 4. District Hub Pages
    for district_key, district_data in districts.items():
        district_name = district_data['name']
        district_slug = district_data['slug']
        
        title = f"{district_name} Kuru Temizleme Halı Yıkama Hizmetleri | Dry Alle İstanbul"
        h1 = f"{district_name} Kuru Temizleme ve Tekstil Hizmetleri"
        meta_desc = f"{district_name}'de kuru temizleme, halı yıkama, koltuk yıkama hizmetleri. 25 yıllık deneyim, ücretsiz alma-getirme. Tüm semtlere hizmet."
        
        master_data.append({
            'Page Type': 'District Hub',
            'District': district_name,
            'Neighborhood': '',
            'Service': '',
            'URL Slug': f'/bolgeler/{district_slug}/',
            'Full URL': f'https://dryallekurutemizleme.com/bolgeler/{district_slug}/',
            'Title': title,
            'H1': h1,
            'Meta Description': meta_desc,
            'Priority': '0.85',
            'Status': 'Create'
        })
    
    # 5. Location Landing Pages
    for district_key, district_data in districts.items():
        district_name = district_data['name']
        district_slug = district_data['slug']
        
        for neighborhood in district_data['neighborhoods']:
            neighborhood_slug = turkish_to_slug(neighborhood)
            
            # Handle special neighborhood name cases
            if neighborhood == 'Sahrayı Cedit':
                neighborhood_slug = 'sahrayicedit'
            elif neighborhood == 'Ataşehir' and district_key == 'atasehir':
                neighborhood_slug = 'merkez'
            elif neighborhood == 'Ataşehir OSB':
                neighborhood_slug = 'osb'
            elif neighborhood == 'Batı Ataşehir':
                neighborhood_slug = 'bati'
            
            for service in services:
                service_name = service['name']
                service_slug = service['slug']
                
                # Generate meta content
                title = f"{neighborhood} {service_name} | {district_name} | Dry Alle"
                h1 = f"{neighborhood}'de {service_name}" if neighborhood.endswith('a') or neighborhood.endswith('e') or neighborhood.endswith('i') or neighborhood.endswith('o') or neighborhood.endswith('u') else f"{neighborhood}'te {service_name}"
                
                # Adjust H1 for specific neighborhoods
                if neighborhood in ['Moda', 'Camlıca', 'Sahrayı Cedit', 'Suadiye']:
                    h1 = f"{neighborhood}'da {service_name}"
                elif neighborhood in ['Fenerbahçe', 'Göztepe', 'Erenköy', 'Bostancı', 'Kalamış', 'Barbaros']:
                    h1 = f"{neighborhood}'de {service_name}"
                elif neighborhood in ['Kızıltoprak', 'Hasanpaşa', 'Rasimpaşa', 'Zühtüpaşa', 'Osmanağa', 'Feneryolu', 'Koşuyolu', 'Altıntepe', 'Fikirtepe']:
                    h1 = f"{neighborhood}'ta {service_name}"
                else:
                    h1 = f"{neighborhood}'de {service_name}"
                
                meta_desc = f"{neighborhood} {service_name.lower()} için kapıdan alım, hızlı teslim, lüks kumaş uzmanlığı. 25 yıllık deneyim ile güvenilir hizmet. Hemen arayın!"
                
                # Ensure meta description is under 155 characters
                if len(meta_desc) > 155:
                    meta_desc = f"{neighborhood} {service_name.lower()} için kapıdan alım, hızlı teslim. 25 yıllık deneyim ile güvenilir hizmet. Hemen arayın!"
                
                # Priority based on service importance
                if service['priority'] == 'High':
                    priority = '0.95'
                elif service['priority'] == 'Medium':
                    priority = '0.90'
                else:
                    priority = '0.85'
                
                # Status determination (check existing pages)
                url_path = f'/bolgeler/{district_slug}/{neighborhood_slug}-{service_slug}.html'
                
                # Known existing pages (from Phase 0.1 inventory)
                existing_pages = [
                    'moda-koltuk-yikama', 'fenerbahce-kuru-temizleme', 'camlica-kuru-temizleme',
                    'goztepe-hali-yikama', 'erenkoy-hali-yikama', 'suadiye-hali-yikama',
                    'caddebostan-hali-yikama', 'bostanci-koltuk-yikama', 'kalamis-koltuk-yikama',
                    'fikirtepe-koltuk-yikama', 'merkez-hali-yikama', 'kucukbakkalkoy-hali-yikama',
                    'barbaros-koltuk-yikama', 'kadikoy-kuru-temizleme', 'kadikoy-koltuk-yikama',
                    'uskudar-hali-yikama', 'uskudar-koltuk-yikama', 'uskudar-gelinlik-temizleme',
                    'uskudar-luxury-kiyafet', 'maltepe-hali-yikama', 'altunizade-hali-yikama',
                    'umraniye-hali-yikama', 'kartal-koltuk-yikama', 'pendik-koltuk-yikama'
                ]
                
                page_key = f"{neighborhood_slug}-{service_slug}"
                status = 'Exists' if page_key in existing_pages else 'Create'
                
                master_data.append({
                    'Page Type': 'Location Landing',
                    'District': district_name,
                    'Neighborhood': neighborhood,
                    'Service': service_name,
                    'URL Slug': url_path,
                    'Full URL': f'https://dryallekurutemizleme.com{url_path}',
                    'Title': title,
                    'H1': h1,
                    'Meta Description': meta_desc,
                    'Priority': priority,
                    'Status': status
                })
    
    # 6. Blog Hub
    master_data.append({
        'Page Type': 'Blog Hub',
        'District': '',
        'Neighborhood': '',
        'Service': '',
        'URL Slug': '/blog/',
        'Full URL': 'https://dryallekurutemizleme.com/blog/',
        'Title': 'Kuru Temizleme Blog | Dry Alle Kuru Temizleme İstanbul',
        'H1': 'Tekstil Bakım ve Temizlik Rehberi',
        'Meta Description': 'Kuru temizleme, halı yıkama, koltuk temizleme ve tekstil bakımı hakkında uzman tavsiyeleri. İstanbul Anadolu Yakası\'nda 25 yıllık deneyim.',
        'Priority': '0.9',
        'Status': 'Exists'
    })
    
    # 7. Blog Categories (existing)
    blog_categories = [
        'Kuru Temizleme', 'Halı Yıkama', 'Koltuk Yıkama', 'Perde Temizleme',
        'Ev Tekstili', 'Çanta Temizleme', 'Lostra Hizmeti', 'Kumaş Deri Boyama', 'Ütü Hizmetleri'
    ]
    
    for category in blog_categories:
        category_slug = turkish_to_slug(category)
        if category == 'Ev Tekstili':
            category_slug = 'ev-tekstili'
        elif category == 'Kumaş Deri Boyama':
            category_slug = 'kumas-deri-boyama'
        
        title = f"{category} Blog | İstanbul Anadolu Yakası {category} Rehberleri"
        h1 = f"{category} Rehberleri"
        meta_desc = f"İstanbul Anadolu Yakası {category.lower()} hakkında uzman rehberleri ve tavsiyeleri. Profesyonel bakım ipuçları ve hizmet bilgileri."
        
        master_data.append({
            'Page Type': 'Blog Category',
            'District': '',
            'Neighborhood': '',
            'Service': category,
            'URL Slug': f'/blog/{category_slug}/',
            'Full URL': f'https://dryallekurutemizleme.com/blog/{category_slug}/',
            'Title': title,
            'H1': h1,
            'Meta Description': meta_desc,
            'Priority': '0.8',
            'Status': 'Exists'
        })
    
    # 8. Support Pages
    support_pages = [
        {
            'type': 'FAQ',
            'slug': '/sss/',
            'title': 'Sıkça Sorulan Sorular | Dry Alle Kuru Temizleme',
            'h1': 'Sıkça Sorulan Sorular',
            'meta': 'Kuru temizleme, halı yıkama, koltuk yıkama hizmetleri hakkında sıkça sorulan sorular ve cevapları. Dry Alle uzman ekibinden yanıtlar.'
        },
        {
            'type': 'Contact',
            'slug': '/iletisim/',
            'title': 'İletişim | Dry Alle Kuru Temizleme İstanbul',
            'h1': 'İletişim Bilgileri',
            'meta': 'Dry Alle Kuru Temizleme ile iletişime geçin. İstanbul Kadıköy ve Ataşehir\'e ücretsiz teslimat. Telefon, WhatsApp, adres bilgileri.'
        },
        {
            'type': 'About',
            'slug': '/hakkimizda/',
            'title': 'Hakkımızda | 25 Yıllık Deneyim | Dry Alle İstanbul',
            'h1': 'Hakkımızda',
            'meta': 'İstanbul Anadolu Yakası\'nda 25 yıllık deneyimle kuru temizleme hizmeti. Dry Alle\'nin hikayesi, kalite anlayışı ve uzman ekibi.'
        },
        {
            'type': 'References',
            'slug': '/referanslar/',
            'title': 'Referanslar | Müşteri Yorumları | Dry Alle İstanbul',
            'h1': 'Müşteri Referansları',
            'meta': 'Dry Alle müşterilerinden gelen referanslar ve yorumlar. 25 yıllık deneyimle İstanbul\'da binlerce mutlu müşteri.'
        }
    ]
    
    for page in support_pages:
        master_data.append({
            'Page Type': page['type'],
            'District': '',
            'Neighborhood': '',
            'Service': '',
            'URL Slug': page['slug'],
            'Full URL': f'https://dryallekurutemizleme.com{page["slug"]}',
            'Title': page['title'],
            'H1': page['h1'],
            'Meta Description': page['meta'],
            'Priority': '0.7',
            'Status': 'Create'
        })
    
    return master_data

def main():
    """Generate and save URL Meta Master CSV"""
    
    # Generate all meta data
    master_data = generate_meta_data()
    
    # Output file path
    output_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_url_meta_master.csv")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # CSV fieldnames
    fieldnames = [
        'Page Type', 'District', 'Neighborhood', 'Service', 'URL Slug', 'Full URL',
        'Title', 'H1', 'Meta Description', 'Priority', 'Status'
    ]
    
    # Write CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(master_data)
    
    # Generate summary statistics
    total_pages = len(master_data)
    existing_pages = len([p for p in master_data if p['Status'] == 'Exists'])
    new_pages = len([p for p in master_data if p['Status'] == 'Create'])
    
    page_types = {}
    for page in master_data:
        page_type = page['Page Type']
        page_types[page_type] = page_types.get(page_type, 0) + 1
    
    # Title length validation
    long_titles = [p for p in master_data if len(p['Title']) > 60]
    long_metas = [p for p in master_data if len(p['Meta Description']) > 155]
    
    print(f"\n=== URL META MASTER GENERATION COMPLETE ===")
    print(f"Total pages generated: {total_pages}")
    print(f"Existing pages: {existing_pages}")
    print(f"New pages to create: {new_pages}")
    print(f"Output saved to: {output_file}")
    
    print(f"\n=== PAGE TYPE BREAKDOWN ===")
    for page_type, count in page_types.items():
        print(f"{page_type}: {count}")
    
    print(f"\n=== VALIDATION RESULTS ===")
    print(f"Titles over 60 characters: {len(long_titles)}")
    print(f"Meta descriptions over 155 characters: {len(long_metas)}")
    
    if long_titles:
        print(f"\nLong titles to review:")
        for page in long_titles[:5]:  # Show first 5
            print(f"  - {page['Title']} ({len(page['Title'])} chars)")
    
    if long_metas:
        print(f"\nLong meta descriptions to review:")
        for page in long_metas[:5]:  # Show first 5
            print(f"  - {page['Meta Description'][:80]}... ({len(page['Meta Description'])} chars)")

if __name__ == "__main__":
    main()