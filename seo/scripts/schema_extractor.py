#!/usr/bin/env python3
"""
Extract and validate schema markup from homepage
"""

import re
import json
from pathlib import Path

def extract_schema_from_homepage():
    """Extract schema markup from index.html"""
    
    homepage_path = Path("/Users/macos/Documents/Projeler/DryAlle/index.html")
    
    with open(homepage_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract schema content
    schema_match = re.search(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', 
                            content, re.DOTALL)
    
    if schema_match:
        schema_content = schema_match.group(1).strip()
        print("Found schema content:")
        print("=" * 50)
        print(schema_content)
        print("=" * 50)
        
        # Try to parse as JSON
        try:
            schema_data = json.loads(schema_content)
            print("✅ Schema is valid JSON")
            print(f"Schema type: {schema_data.get('@type', 'Unknown')}")
            
            return schema_data, None
        except json.JSONDecodeError as e:
            print(f"❌ Schema JSON is invalid: {e}")
            return None, str(e)
    else:
        print("❌ No schema markup found")
        return None, "No schema found"

if __name__ == "__main__":
    schema, error = extract_schema_from_homepage()