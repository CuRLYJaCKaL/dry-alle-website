#!/usr/bin/env python3
"""
DryAlle Content Generator
Programmatically generates 403 location landing pages using templates
"""

import csv
import os
import re
from pathlib import Path
import json
from datetime import datetime

def load_url_master_data():
    """Load URL master data with all location-service combinations"""
    master_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_url_meta_master.csv")
    pages = []
    
    with open(master_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pages.append(row)
    
    return pages

def load_landing_page_template():
    """Load the landing page template"""
    template_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/templates/landing_page_template.md")
    
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    return template_content

def generate_location_content(page_data, template):
    """Generate content for a specific location-service combination"""
    
    # Extract variables
    district = page_data.get("District", "")
    neighborhood = page_data.get("Neighborhood", "")
    service = page_data.get("Service", "")
    
    # Create service variations
    service_lower = service.lower() if service else ""
    service_slug = service_lower.replace(" ", "-").replace("ç", "c").replace("ş", "s").replace("ğ", "g").replace("ü", "u").replace("ö", "o").replace("ı", "i")
    
    # Phone and contact info
    phone = "+90-543-352-7474"
    whatsapp = "+905433527474"
    brand = "Dry Alle"
    
    # Content variables
    variables = {
        "{NEIGHBORHOOD}": neighborhood,
        "{DISTRICT}": district,
        "{SERVICE}": service,
        "{SERVICE_LOWER}": service_lower,
        "{PHONE}": phone,
        "{WHATSAPP}": whatsapp,
        "{BRAND}": brand
    }
    
    # Generate content from template
    content = template
    for var, value in variables.items():
        content = content.replace(var, value)
    
    # Extract just the content sections (remove template documentation)
    content_sections = extract_content_sections(content)
    
    return content_sections

def extract_content_sections(full_template):
    """Extract only the actual content sections from template"""
    
    # Find the content template structure section
    start_marker = "## 2. Content Template Structure"
    end_marker = "## 3. Service-Specific Content Variations"
    
    start_idx = full_template.find(start_marker)
    end_idx = full_template.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        return "Template content extraction failed"
    
    content_section = full_template[start_idx:end_idx]
    
    # Extract just the markdown content examples
    lines = content_section.split('\n')
    content_lines = []
    in_content_block = False
    
    for line in lines:
        if line.startswith('```markdown'):
            in_content_block = True
            continue
        elif line.startswith('```') and in_content_block:
            in_content_block = False
            continue
        elif in_content_block:
            content_lines.append(line)
    
    return '\n'.join(content_lines)

def generate_html_page(page_data, content):
    """Generate complete HTML page with content and meta tags"""
    
    # Extract meta information
    title = page_data.get("Title", "")
    h1 = page_data.get("H1", "")
    meta_desc = page_data.get("Meta Description", "")
    
    # Generate schema markup
    schema_markup = generate_schema_markup(page_data)
    
    # Generate HTML
    html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="keywords" content="{generate_keywords(page_data)}">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{page_data.get('Full URL', '')}">
    <meta property="og:image" content="https://dryallekurutemizleme.com/asset/hero-image.png">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{meta_desc}">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="{page_data.get('Full URL', '')}">
    
    <!-- CSS -->
    <link rel="stylesheet" href="../../styles.css">
    <link rel="stylesheet" href="../../service-detail-styles.css">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Schema Markup -->
    <script type="application/ld+json">
    {schema_markup}
    </script>
</head>
<body>
    <!-- Navigation -->
    <nav class="main-nav">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="../../index.html">Dry Alle</a>
            </div>
            <div class="nav-menu">
                <a href="../../hizmetler/">Hizmetler</a>
                <a href="../../bolgeler/">Bölgeler</a>
                <a href="../../blog/">Blog</a>
                <a href="../../hakkimizda.html">Hakkımızda</a>
                <a href="../../iletisim.html">İletişim</a>
            </div>
            <div class="nav-cta">
                <a href="tel:+905433527474" class="nav-phone">0543 352 74 74</a>
            </div>
        </div>
    </nav>
    
    <!-- Main Content -->
    <main class="location-page">
        <div class="container">
            <header class="page-header">
                <h1>{h1}</h1>
            </header>
            
            <article class="location-content">
                {convert_markdown_to_html(content)}
            </article>
            
            <!-- Related Services -->
            <section class="related-services">
                {generate_related_services(page_data)}
            </section>
            
            <!-- Contact CTA -->
            <section class="contact-cta">
                {generate_contact_cta(page_data)}
            </section>
        </div>
    </main>
    
    <!-- Footer -->
    <footer class="main-footer">
        <div class="footer-container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Hizmetlerimiz</h3>
                    <ul>
                        <li><a href="../../hizmetler/kuru-temizleme.html">Kuru Temizleme</a></li>
                        <li><a href="../../hizmetler/hali-yikama.html">Halı Yıkama</a></li>
                        <li><a href="../../hizmetler/koltuk-yikama.html">Koltuk Yıkama</a></li>
                        <li><a href="../../hizmetler/gelinlik-temizleme.html">Gelinlik Temizleme</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Bölgelerimiz</h3>
                    <ul>
                        <li><a href="../../bolgeler/kadikoy/">Kadıköy</a></li>
                        <li><a href="../../bolgeler/atasehir/">Ataşehir</a></li>
                        <li><a href="../../bolgeler/maltepe/">Maltepe</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>İletişim</h3>
                    <p>📞 <a href="tel:+905433527474">0543 352 74 74</a></p>
                    <p>💬 <a href="https://wa.me/905433527474">WhatsApp</a></p>
                    <p>📧 info@dryallekurutemizleme.com</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Dry Alle Kuru Temizleme. Tüm hakları saklıdır.</p>
            </div>
        </div>
    </footer>
    
    <!-- JavaScript -->
    <script src="../../script.js"></script>
    
    <!-- Mobile Sticky CTA -->
    <div class="mobile-sticky-cta">
        <a href="tel:+905433527474" class="mobile-cta-call">📞 Ara</a>
        <a href="https://wa.me/905433527474?text={page_data.get('Neighborhood', '')}%20{page_data.get('Service', '')}%20için%20randevu%20almak%20istiyorum" class="mobile-cta-whatsapp">💬 WhatsApp</a>
    </div>
</body>
</html>"""
    
    return html_content

def generate_keywords(page_data):
    """Generate SEO keywords for the page"""
    district = page_data.get("District", "").lower()
    neighborhood = page_data.get("Neighborhood", "").lower()
    service = page_data.get("Service", "").lower()
    
    keywords = [
        f"{neighborhood} {service}",
        f"{district} {service}",
        f"{service} {neighborhood}",
        f"{service} {district}",
        f"istanbul {service}",
        f"{neighborhood} kuru temizleme",
        f"{district} tekstil hizmetleri",
        "dry alle",
        "kapıdan alım teslim",
        "aynı gün servis"
    ]
    
    return ", ".join(keywords)

def generate_schema_markup(page_data):
    """Generate JSON-LD schema markup for location page"""
    
    district = page_data.get("District", "")
    neighborhood = page_data.get("Neighborhood", "")
    service = page_data.get("Service", "")
    
    schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": f"Dry Alle {neighborhood} {service}",
        "description": page_data.get("Meta Description", ""),
        "url": page_data.get("Full URL", ""),
        "serviceType": service,
        "areaServed": {
            "@type": "Place",
            "name": f"{neighborhood}, {district}, İstanbul"
        },
        "address": {
            "@type": "PostalAddress",
            "addressLocality": district,
            "addressRegion": "İstanbul",
            "addressCountry": "TR"
        },
        "telephone": "+90-543-352-7474",
        "email": "info@dryallekurutemizleme.com",
        "openingHours": "Mo-Sa 09:00-18:00",
        "priceRange": "$$",
        "paymentAccepted": "Cash, Credit Card",
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": f"{service} Hizmetleri",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": service,
                        "description": f"Profesyonel {service.lower()} hizmeti"
                    }
                }
            ]
        }
    }
    
    return json.dumps(schema, indent=2, ensure_ascii=False)

def convert_markdown_to_html(markdown_content):
    """Convert markdown content to HTML"""
    
    # Basic markdown to HTML conversion
    html = markdown_content
    
    # Headers
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Lists
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
    
    # Paragraphs
    lines = html.split('\n')
    in_list = False
    html_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        elif line.startswith('<h') or line.startswith('<ul') or line.startswith('</ul'):
            html_lines.append(line)
        elif line.startswith('<li'):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(line)
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<p>{line}</p>')
    
    if in_list:
        html_lines.append('</ul>')
    
    return '\n'.join(html_lines)

def generate_related_services(page_data):
    """Generate related services section"""
    district = page_data.get("District", "")
    neighborhood = page_data.get("Neighborhood", "")
    current_service = page_data.get("Service", "")
    
    services = [
        "Kuru Temizleme",
        "Halı Yıkama", 
        "Koltuk Yıkama",
        "Gelinlik Temizleme",
        "Perde Temizleme",
        "Çanta Temizleme"
    ]
    
    related_html = '<h3>Diğer Hizmetlerimiz</h3>\n<div class="related-services-grid">\n'
    
    for service in services:
        if service != current_service:
            service_slug = service.lower().replace(" ", "-").replace("ç", "c").replace("ş", "s").replace("ğ", "g").replace("ü", "u").replace("ö", "o").replace("ı", "i")
            related_html += f'    <a href="{neighborhood.lower()}-{service_slug}.html" class="related-service-card">\n'
            related_html += f'        <h4>{neighborhood} {service}</h4>\n'
            related_html += f'        <p>Profesyonel {service.lower()} hizmeti</p>\n'
            related_html += f'    </a>\n'
    
    related_html += '</div>'
    return related_html

def generate_contact_cta(page_data):
    """Generate contact CTA section"""
    neighborhood = page_data.get("Neighborhood", "")
    service = page_data.get("Service", "")
    
    cta_html = f"""
    <div class="contact-cta-content">
        <h3>{neighborhood} {service} İçin Hemen İletişime Geçin</h3>
        <p>Tekstil bakım ihtiyaçlarınız için {neighborhood}'da en güvenilir adres Dry Alle.</p>
        
        <div class="cta-buttons">
            <a href="tel:+905433527474" class="btn-primary btn-call">
                📞 Hemen Ara: 0543 352 74 74
            </a>
            <a href="https://wa.me/905433527474?text={neighborhood}%20{service}%20için%20randevu%20almak%20istiyorum" class="btn-primary btn-whatsapp">
                💬 WhatsApp Randevu
            </a>
        </div>
        
        <div class="cta-benefits">
            <div class="benefit">
                <span class="benefit-icon">🏠</span>
                <span>Kapıdan Alım-Teslim</span>
            </div>
            <div class="benefit">
                <span class="benefit-icon">⚡</span>
                <span>Hızlı Teslimat</span>
            </div>
            <div class="benefit">
                <span class="benefit-icon">🏆</span>
                <span>25 Yıllık Deneyim</span>
            </div>
        </div>
    </div>
    """
    
    return cta_html

def generate_batch_content():
    """Generate content for all location landing pages"""
    
    print("DryAlle Content Generator başlatılıyor...")
    
    # Load data
    pages_data = load_url_master_data()
    template = load_landing_page_template()
    
    # Filter for location landing pages
    location_pages = [p for p in pages_data if p["Page Type"] == "Location Landing"]
    
    print(f"Generating content for {len(location_pages)} location landing pages...")
    
    # Create output directory
    output_dir = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/generated_pages")
    output_dir.mkdir(exist_ok=True)
    
    # Track generation results
    generation_log = []
    
    for i, page_data in enumerate(location_pages):
        try:
            # Generate content
            content = generate_location_content(page_data, template)
            html_page = generate_html_page(page_data, content)
            
            # Create filename
            url_slug = page_data.get("URL Slug", "").replace("/", "").replace(".html", "")
            filename = f"{url_slug}.html"
            
            # Save file
            file_path = output_dir / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_page)
            
            # Log result
            generation_log.append({
                "file_name": filename,
                "url": page_data.get("Full URL", ""),
                "neighborhood": page_data.get("Neighborhood", ""),
                "district": page_data.get("District", ""),
                "service": page_data.get("Service", ""),
                "title_length": len(page_data.get("Title", "")),
                "meta_length": len(page_data.get("Meta Description", "")),
                "status": "success",
                "timestamp": datetime.now().isoformat()
            })
            
            if (i + 1) % 50 == 0:
                print(f"Generated {i + 1}/{len(location_pages)} pages...")
        
        except Exception as e:
            generation_log.append({
                "file_name": f"ERROR_{url_slug}.html",
                "url": page_data.get("Full URL", ""),
                "neighborhood": page_data.get("Neighborhood", ""),
                "district": page_data.get("District", ""),
                "service": page_data.get("Service", ""),
                "title_length": 0,
                "meta_length": 0,
                "status": f"error: {str(e)}",
                "timestamp": datetime.now().isoformat()
            })
            print(f"Error generating page {i+1}: {e}")
    
    # Save generation log
    log_file = Path("/Users/macos/Documents/Projeler/DryAlle/seo/outputs/03_content_generation_log.csv")
    
    with open(log_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["file_name", "url", "neighborhood", "district", "service", 
                     "title_length", "meta_length", "status", "timestamp"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(generation_log)
    
    # Print summary
    successful = len([log for log in generation_log if log["status"] == "success"])
    failed = len(generation_log) - successful
    
    print(f"\n=== CONTENT GENERATION SUMMARY ===")
    print(f"Total pages: {len(location_pages)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Generated files saved to: {output_dir}")
    print(f"Generation log saved to: {log_file}")
    
    return generation_log

if __name__ == "__main__":
    generation_log = generate_batch_content()