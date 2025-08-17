#!/usr/bin/env python3
"""
Corporate Design Integration for Blog Redesign & SEO Overhaul
B1: Integrates main site CSS design system into blog pages

Features:
- Extracts corporate color scheme (#006a44, #f6ec3d)
- Applies consistent typography (Roboto font)
- Integrates navigation structure
- Maintains responsive design patterns
- Preserves SEO-optimized blog functionality
"""

import os
import re
from datetime import datetime

class CorporateDesignIntegrator:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        
        # Corporate design tokens from main site
        self.design_tokens = {
            'primary_green': '#006a44',
            'accent_yellow': '#f6ec3d',
            'secondary_green': '#004d32',
            'light_green': '#00623b',
            'hover_green': '#22c55e',
            'text_color': '#333',
            'font_family': "'Roboto', sans-serif",
            'max_width': '1600px',
            'padding_desktop': '60px',
            'padding_mobile': '20px'
        }

    def extract_main_site_components(self):
        """Extract reusable components from main site"""
        main_css_path = os.path.join(self.project_root, 'styles.css')
        
        try:
            with open(main_css_path, 'r', encoding='utf-8') as f:
                main_css = f.read()
            
            # Extract key component styles
            components = {
                'reset': self.extract_css_section(main_css, r'\* {.*?}', re.DOTALL),
                'body': self.extract_css_section(main_css, r'body {.*?}', re.DOTALL),
                'top_bar': self.extract_css_section(main_css, r'\.top-bar.*?(?=\/\*|$)', re.DOTALL),
                'header': self.extract_css_section(main_css, r'\.header.*?(?=\/\*|$)', re.DOTALL),
                'navigation': self.extract_css_section(main_css, r'\.nav-menu.*?(?=\/\*|$)', re.DOTALL),
                'responsive': self.extract_css_section(main_css, r'@media.*?(?=@media|$)', re.DOTALL)
            }
            
            return components
            
        except Exception as e:
            print(f"❌ Error extracting main site components: {str(e)}")
            return {}

    def extract_css_section(self, css_content, pattern, flags=0):
        """Extract CSS section based on regex pattern"""
        match = re.search(pattern, css_content, flags)
        return match.group(0) if match else ""

    def create_integrated_blog_css(self, components):
        """Create new blog CSS with corporate design integration"""
        
        integrated_css = f"""/*
Corporate Blog Design System
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Integrated with main site design tokens

Brand Colors:
- Primary Green: {self.design_tokens['primary_green']}
- Accent Yellow: {self.design_tokens['accent_yellow']}
- Typography: {self.design_tokens['font_family']}
*/

/* ============================================
   CORPORATE FOUNDATION STYLES
   ============================================ */

/* CSS Reset & Base */
{components.get('reset', '')}

{components.get('body', '')}

/* Corporate Header & Navigation */
{components.get('top_bar', '')}

{components.get('header', '')}

{components.get('navigation', '')}

/* ============================================
   BLOG-SPECIFIC STYLES
   ============================================ */

/* Blog Container */
.blog-container {{
    max-width: {self.design_tokens['max_width']};
    margin: 0 auto;
    padding: 0 {self.design_tokens['padding_desktop']};
}}

/* Blog Hero Section */
.blog-hero {{
    padding: 100px 0 80px 0;
    background: linear-gradient(135deg, {self.design_tokens['primary_green']} 0%, {self.design_tokens['secondary_green']} 50%, {self.design_tokens['light_green']} 100%);
    color: white;
    text-align: center;
    position: relative;
    overflow: hidden;
}}

.blog-hero::before {{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="rgba(255,255,255,0.03)"/><circle cx="75" cy="75" r="1" fill="rgba(255,255,255,0.03)"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
    opacity: 0.3;
}}

.blog-hero-content {{
    position: relative;
    z-index: 2;
    max-width: {self.design_tokens['max_width']};
    margin: 0 auto;
    padding: 0 {self.design_tokens['padding_desktop']};
}}

.blog-hero h1 {{
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 20px;
    line-height: 1.2;
}}

.blog-hero .meta {{
    font-size: 16px;
    opacity: 0.9;
    margin-bottom: 30px;
}}

.blog-hero .breadcrumb {{
    font-size: 14px;
    opacity: 0.8;
}}

.blog-hero .breadcrumb a {{
    color: {self.design_tokens['accent_yellow']};
    text-decoration: none;
}}

.blog-hero .breadcrumb a:hover {{
    text-decoration: underline;
}}

/* Blog Content */
.blog-content {{
    padding: 80px 0;
    background: white;
}}

.blog-article {{
    max-width: 900px;
    margin: 0 auto;
    padding: 0 {self.design_tokens['padding_desktop']};
}}

.blog-article h2 {{
    color: {self.design_tokens['primary_green']};
    font-size: 32px;
    font-weight: 700;
    margin: 40px 0 20px 0;
    line-height: 1.3;
}}

.blog-article h3 {{
    color: {self.design_tokens['primary_green']};
    font-size: 24px;
    font-weight: 600;
    margin: 30px 0 15px 0;
    line-height: 1.4;
}}

.blog-article p {{
    font-size: 18px;
    line-height: 1.8;
    margin-bottom: 20px;
    color: {self.design_tokens['text_color']};
}}

.blog-article ul, .blog-article ol {{
    margin: 20px 0;
    padding-left: 30px;
}}

.blog-article li {{
    font-size: 18px;
    line-height: 1.7;
    margin-bottom: 10px;
    color: {self.design_tokens['text_color']};
}}

/* Corporate Call-to-Action Boxes */
.cta-box {{
    background: linear-gradient(135deg, {self.design_tokens['primary_green']} 0%, {self.design_tokens['light_green']} 100%);
    color: white;
    padding: 40px;
    border-radius: 12px;
    margin: 40px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}}

.cta-box::before {{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23dots)"/></svg>');
}}

.cta-box h3 {{
    font-size: 24px;
    margin-bottom: 15px;
    position: relative;
    z-index: 1;
}}

.cta-box p {{
    font-size: 16px;
    margin-bottom: 25px;
    position: relative;
    z-index: 1;
    opacity: 0.95;
}}

.cta-button {{
    display: inline-block;
    background: {self.design_tokens['accent_yellow']};
    color: {self.design_tokens['text_color']} !important;
    padding: 15px 30px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    position: relative;
    z-index: 1;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.cta-button:hover {{
    background: #f4e91d;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}}

/* FAQ Section */
.faq-section {{
    background: #f8f9fa;
    padding: 60px 0;
    margin-top: 60px;
}}

.faq-container {{
    max-width: 900px;
    margin: 0 auto;
    padding: 0 {self.design_tokens['padding_desktop']};
}}

.faq-item {{
    background: white;
    border-radius: 8px;
    margin-bottom: 20px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}}

.faq-question {{
    background: {self.design_tokens['primary_green']};
    color: white;
    padding: 20px;
    font-weight: 600;
    font-size: 18px;
    cursor: pointer;
    position: relative;
}}

.faq-question::after {{
    content: '+';
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 24px;
    transition: transform 0.3s ease;
}}

.faq-question.active::after {{
    transform: translateY(-50%) rotate(45deg);
}}

.faq-answer {{
    padding: 20px;
    font-size: 16px;
    line-height: 1.7;
    color: {self.design_tokens['text_color']};
    display: none;
}}

.faq-answer.active {{
    display: block;
}}

/* Related Articles */
.related-articles {{
    background: white;
    padding: 60px 0;
}}

.related-container {{
    max-width: {self.design_tokens['max_width']};
    margin: 0 auto;
    padding: 0 {self.design_tokens['padding_desktop']};
}}

.related-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 40px;
}}

.related-card {{
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.related-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}}

.related-card img {{
    width: 100%;
    height: 200px;
    object-fit: cover;
}}

.related-card-content {{
    padding: 25px;
}}

.related-card h3 {{
    color: {self.design_tokens['primary_green']};
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 15px;
    line-height: 1.4;
}}

.related-card p {{
    font-size: 14px;
    color: #666;
    line-height: 1.6;
    margin-bottom: 15px;
}}

.related-card a {{
    color: {self.design_tokens['primary_green']};
    text-decoration: none;
    font-weight: 500;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.related-card a:hover {{
    color: {self.design_tokens['hover_green']};
}}

/* ============================================
   RESPONSIVE DESIGN
   ============================================ */

@media (max-width: 768px) {{
    .blog-container,
    .blog-hero-content,
    .blog-article,
    .faq-container,
    .related-container {{
        padding: 0 {self.design_tokens['padding_mobile']};
    }}
    
    .blog-hero {{
        padding: 60px 0 40px 0;
    }}
    
    .blog-hero h1 {{
        font-size: 32px;
    }}
    
    .blog-article h2 {{
        font-size: 26px;
    }}
    
    .blog-article h3 {{
        font-size: 20px;
    }}
    
    .blog-article p,
    .blog-article li {{
        font-size: 16px;
    }}
    
    .cta-box {{
        padding: 25px;
        margin: 30px 0;
    }}
    
    .cta-box h3 {{
        font-size: 20px;
    }}
    
    .related-grid {{
        grid-template-columns: 1fr;
        gap: 20px;
    }}
    
    .nav-menu {{
        flex-direction: column;
        gap: 20px;
        padding: 0 {self.design_tokens['padding_mobile']};
    }}
}}

@media (max-width: 480px) {{
    .blog-hero h1 {{
        font-size: 28px;
    }}
    
    .blog-article h2 {{
        font-size: 22px;
    }}
    
    .cta-button {{
        padding: 12px 24px;
        font-size: 14px;
    }}
}}

/* ============================================
   BLOG INDEX GRID STYLES
   ============================================ */

.blog-index-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 40px;
    padding: 80px 0;
}}

.blog-post-card {{
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.blog-post-card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}}

.blog-post-card img {{
    width: 100%;
    height: 250px;
    object-fit: cover;
}}

.blog-post-card-content {{
    padding: 30px;
}}

.blog-post-card h2 {{
    color: {self.design_tokens['primary_green']};
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 15px;
    line-height: 1.4;
}}

.blog-post-card .meta {{
    font-size: 14px;
    color: #666;
    margin-bottom: 15px;
}}

.blog-post-card p {{
    font-size: 16px;
    line-height: 1.6;
    color: {self.design_tokens['text_color']};
    margin-bottom: 20px;
}}

.read-more {{
    color: {self.design_tokens['primary_green']};
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 2px solid transparent;
    transition: border-color 0.3s ease;
}}

.read-more:hover {{
    border-color: {self.design_tokens['primary_green']};
}}"""

        return integrated_css

    def update_blog_html_files(self):
        """Update all blog HTML files to use new integrated CSS"""
        blog_dirs = []
        
        # Find all blog directories with index.html
        blog_root = os.path.join(self.project_root, 'blog')
        
        for item in os.listdir(blog_root):
            item_path = os.path.join(blog_root, item)
            if os.path.isdir(item_path) and item not in ['pillar-content']:
                index_path = os.path.join(item_path, 'index.html')
                if os.path.exists(index_path):
                    blog_dirs.append(item_path)
        
        updated_count = 0
        
        for blog_dir in blog_dirs:
            index_path = os.path.join(blog_dir, 'index.html')
            
            try:
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update CSS references
                content = self.update_css_references(content)
                
                # Add corporate header if missing
                content = self.add_corporate_header(content)
                
                # Write updated content
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
                
            except Exception as e:
                print(f"❌ Error updating {index_path}: {str(e)}")
        
        return updated_count

    def update_css_references(self, html_content):
        """Update CSS file references in HTML"""
        # Update blog-styles.css reference to new integrated CSS
        html_content = re.sub(
            r'<link rel="stylesheet" href="[^"]*blog-styles\.css">',
            '<link rel="stylesheet" href="../../blog-corporate.css">',
            html_content
        )
        
        # Ensure main styles.css is referenced
        if 'styles.css' not in html_content:
            # Add after charset meta tag
            html_content = re.sub(
                r'(<meta name="viewport"[^>]*>)',
                r'\1\n    <link rel="stylesheet" href="../../styles.css">',
                html_content
            )
        
        return html_content

    def add_corporate_header(self, html_content):
        """Add corporate header structure if missing"""
        # Check if header already exists
        if '<header class="header">' in html_content:
            return html_content
        
        # Corporate header HTML
        header_html = '''
    <!-- Corporate Header -->
    <div class="top-bar">
        <div class="top-bar-content">
            <strong>ÜCRETSİZ KAPIDAN TESLİMAT</strong> • İstanbul'un Her Yerine • 0530 468 5858
        </div>
    </div>
    
    <header class="header">
        <div class="header-container">
            <div class="logo">
                <svg width="120" height="40" viewBox="0 0 120 40" fill="none">
                    <text x="10" y="25" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="white">DRY ALLE</text>
                </svg>
            </div>
            <nav>
                <ul class="nav-menu">
                    <li><a href="../../index.html">ANASAYFA</a></li>
                    <li><a href="../../hizmetler.html">HİZMETLER</a></li>
                    <li><a href="../index.html">BLOG</a></li>
                    <li><a href="../../sss.html">SSS</a></li>
                    <li><a href="../../iletisim.html">İLETİŞİM</a></li>
                </ul>
            </nav>
        </div>
    </header>
'''
        
        # Insert after <body> tag
        html_content = re.sub(
            r'(<body[^>]*>)',
            r'\\1' + header_html,
            html_content
        )
        
        return html_content

    def save_integrated_css(self, css_content):
        """Save the new integrated CSS file"""
        css_path = os.path.join(self.project_root, 'blog-corporate.css')
        
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        return css_path

def main():
    """Execute corporate design integration"""
    print("🎨 CORPORATE DESIGN INTEGRATION")
    print("=" * 40)
    print("B1: Main Site CSS → Blog Integration")
    print("=" * 40)
    
    integrator = CorporateDesignIntegrator()
    
    try:
        # Extract main site components
        print("🔍 Extracting main site design components...")
        components = integrator.extract_main_site_components()
        
        # Create integrated CSS
        print("🎨 Creating integrated blog CSS...")
        integrated_css = integrator.create_integrated_blog_css(components)
        
        # Save new CSS file
        css_path = integrator.save_integrated_css(integrated_css)
        print(f"✅ Saved integrated CSS: {css_path}")
        
        # Update blog HTML files
        print("📝 Updating blog HTML files...")
        updated_count = integrator.update_blog_html_files()
        print(f"✅ Updated {updated_count} blog files")
        
        # Summary
        print("\\n" + "=" * 40)
        print("📊 CORPORATE INTEGRATION COMPLETE")
        print("=" * 40)
        print(f"✅ CSS Integration: Complete")
        print(f"✅ Files Updated: {updated_count}")
        print(f"✅ Design System: Unified")
        print(f"✅ Corporate Colors: Applied")
        print(f"✅ Typography: Standardized")
        
        print("\\n🚀 NEXT STEPS:")
        print("1. Test blog design in browser")
        print("2. Verify responsive behavior")
        print("3. Check corporate brand consistency")
        print("4. Optimize for mobile devices")
        
        return True
        
    except Exception as e:
        print(f"❌ Critical error during integration: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)