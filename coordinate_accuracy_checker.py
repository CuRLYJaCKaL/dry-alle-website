#!/usr/bin/env python3
"""
Coordinate Accuracy Checker
Her bölge için koordinatların doğruluğunu kontrol eder
"""

import re
import os
from pathlib import Path

# Gerçek İstanbul koordinatları (Google Maps referansı)
REAL_COORDINATES = {
    'acibadem': {'lat': 40.9667, 'lon': 29.0333, 'district': 'Acıbadem, Kadıköy'},
    'altunizade': {'lat': 41.0156, 'lon': 29.0661, 'district': 'Altunizade, Üsküdar'},
    'atasehir': {'lat': 41.0188, 'lon': 29.1264, 'district': 'Ataşehir'},
    'bagdat-caddesi': {'lat': 40.9667, 'lon': 29.0667, 'district': 'Bağdat Caddesi, Kadıköy'},
    'barbaros': {'lat': 41.0392, 'lon': 29.0067, 'district': 'Barbaros, Beşiktaş'},
    'bostanci': {'lat': 40.9588, 'lon': 29.0944, 'district': 'Bostancı, Kadıköy'},
    'caddebostan': {'lat': 40.9656, 'lon': 29.0933, 'district': 'Caddebostan, Kadıköy'},
    'camlica': {'lat': 41.0194, 'lon': 29.0664, 'district': 'Çamlıca, Üsküdar'},
    'erenkoy': {'lat': 40.9772, 'lon': 29.0725, 'district': 'Erenköy, Kadıköy'},
    'fenerbahce': {'lat': 40.9633, 'lon': 29.0467, 'district': 'Fenerbahçe, Kadıköy'},
    'fikirtepe': {'lat': 40.9689, 'lon': 29.0533, 'district': 'Fikirtepe, Kadıköy'},
    'goztepe': {'lat': 40.9839, 'lon': 29.0564, 'district': 'Göztepe, Kadıköy'},
    'icerenkoy': {'lat': 40.9711, 'lon': 29.0778, 'district': 'İçerenköy, Ataşehir'},
    'kadikoy': {'lat': 40.9903, 'lon': 29.0275, 'district': 'Kadıköy'},
    'kalamis': {'lat': 40.9628, 'lon': 29.0394, 'district': 'Kalamış, Kadıköy'},
    'kartal': {'lat': 40.9092, 'lon': 29.1822, 'district': 'Kartal'},
    'kozyatagi': {'lat': 40.9711, 'lon': 29.0778, 'district': 'Kozyatağı, Kadıköy'},
    'kucukbakkalkoy': {'lat': 40.9756, 'lon': 29.0853, 'district': 'Küçükbakkalköy, Ataşehir'},
    'maltepe': {'lat': 40.9333, 'lon': 29.1333, 'district': 'Maltepe'},
    'moda': {'lat': 40.9800, 'lon': 29.0333, 'district': 'Moda, Kadıköy'},
    'pendik': {'lat': 40.8783, 'lon': 29.2322, 'district': 'Pendik'},
    'sahrayicedit': {'lat': 40.9667, 'lon': 29.0667, 'district': 'Sahrayıcedit, Kadıköy'},
    'suadiye': {'lat': 40.9583, 'lon': 29.0567, 'district': 'Suadiye, Kadıköy'},
    'umraniye': {'lat': 41.0167, 'lon': 29.1167, 'district': 'Ümraniye'},
    'uskudar': {'lat': 41.0214, 'lon': 29.0144, 'district': 'Üsküdar'}
}

def extract_location_from_filename(filename):
    """Dosya adından lokasyon çıkar"""
    base = filename.replace('.html', '')
    for location in REAL_COORDINATES.keys():
        if base.startswith(location):
            return location
    return None

def extract_coordinates_from_content(content):
    """İçerikten koordinatları çıkar"""
    geo_pos_match = re.search(r'geo\.position["\']?\s*content=["\']([^"\']*)["\']', content)
    if geo_pos_match:
        coords_str = geo_pos_match.group(1)
        if ';' in coords_str:
            lat_str, lon_str = coords_str.split(';')
            try:
                return float(lat_str), float(lon_str)
            except ValueError:
                pass
    return None, None

def calculate_distance(lat1, lon1, lat2, lon2):
    """İki nokta arası mesafeyi hesapla (km)"""
    import math
    
    # Haversine formülü
    R = 6371  # Earth radius in km
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = (math.sin(dlat/2) * math.sin(dlat/2) + 
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
         math.sin(dlon/2) * math.sin(dlon/2))
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance

def check_coordinate_accuracy():
    """Tüm sayfalar için koordinat doğruluğunu kontrol et"""
    bolgeler_dir = Path('/Users/macos/Documents/Projeler/DryAlle/bolgeler')
    html_files = sorted([f for f in bolgeler_dir.glob('*.html')])
    
    print(f"🗺️  CHECKING COORDINATE ACCURACY FOR {len(html_files)} PAGES")
    print("=" * 80)
    
    accurate_count = 0
    total_distance_error = 0
    
    for i, file_path in enumerate(html_files, 1):
        filename = file_path.name
        location = extract_location_from_filename(filename)
        
        if not location:
            print(f"{i:2d}. ❓ {filename} - Location not recognized")
            continue
        
        # İçeriği oku
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"{i:2d}. ❌ {filename} - Error reading file: {e}")
            continue
        
        # Koordinatları çıkar
        file_lat, file_lon = extract_coordinates_from_content(content)
        
        if file_lat is None or file_lon is None:
            print(f"{i:2d}. ❌ {filename} - No coordinates found")
            continue
        
        # Gerçek koordinatları al
        real_coords = REAL_COORDINATES.get(location)
        if not real_coords:
            print(f"{i:2d}. ❓ {filename} - No reference coordinates for {location}")
            continue
        
        real_lat, real_lon = real_coords['lat'], real_coords['lon']
        
        # Mesafe hesapla
        distance = calculate_distance(file_lat, file_lon, real_lat, real_lon)
        total_distance_error += distance
        
        # Doğruluk kontrolü (500m tolerans)
        if distance <= 0.5:  # 500 meter tolerance
            status = "✅ ACCURATE"
            accurate_count += 1
        elif distance <= 2.0:  # 2km tolerance
            status = "⚠️  ACCEPTABLE"
        else:
            status = "❌ INACCURATE"
        
        print(f"{i:2d}. {status} {filename}")
        print(f"    📍 File: {file_lat}, {file_lon}")
        print(f"    🎯 Real: {real_lat}, {real_lon}")
        print(f"    📏 Distance: {distance:.2f} km")
        print()
    
    print("=" * 80)
    print(f"📊 COORDINATE ACCURACY SUMMARY")
    print(f"✅ Accurate (≤500m): {accurate_count}/{len(html_files)}")
    print(f"📈 Accuracy rate: {accurate_count/len(html_files)*100:.1f}%")
    print(f"📏 Average error: {total_distance_error/len(html_files):.2f} km")

if __name__ == "__main__":
    check_coordinate_accuracy()