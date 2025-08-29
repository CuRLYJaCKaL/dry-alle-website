#!/usr/bin/env python3
"""
Navigation Structure Analysis
"""

import os
import re
from bs4 import BeautifulSoup

def analyze_navigation():
    blog_directory = "/Users/macos/Documents/Projeler/DryAlle/blog"
    old_nav_articles = []
    new_nav_articles = []
    
    # Find all index.html files in blog subdirectories
    for root, dirs, files in os.walk(blog_directory):
        for file in files:
            if file == 'index.html':
                filepath = os.path.join(root, file)
                # Skip main blog index
                if root != blog_directory:
                    article_name = os.path.basename(os.path.dirname(filepath))
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Check for old navigation patterns
                        if any(nav in content for nav in ["Ana Sayfa", "Hizmetlerimiz", "Hakkımızda"]):
                            old_nav_articles.append(article_name)
                        else:
                            new_nav_articles.append(article_name)
                            
                    except Exception as e:
                        print(f"Error reading {filepath}: {e}")
    
    print(f"Articles with OLD navigation structure: {len(old_nav_articles)}")
    print(f"Articles with NEW navigation structure: {len(new_nav_articles)}")
    
    print("\nOLD NAVIGATION ARTICLES:")
    for article in sorted(old_nav_articles):
        print(f"  • {article}")
    
    print("\nNEW NAVIGATION ARTICLES:")  
    for article in sorted(new_nav_articles):
        print(f"  • {article}")

if __name__ == "__main__":
    analyze_navigation()