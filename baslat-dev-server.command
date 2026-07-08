#!/bin/bash
# DryPrestijKuruTemizleme dev server başlatıcı
cd "$(dirname "$0")"
echo "==========================================="
echo " DryPrestij Kuru Temizleme - Dev Server"
echo "==========================================="
echo ""

# node_modules yoksa kur
if [ ! -d "node_modules" ] || [ ! -f "node_modules/.bin/astro" ]; then
  echo "→ Bağımlılıklar kuruluyor (ilk kez, ~1 dakika sürebilir)..."
  npm install
fi

echo ""
echo "→ Dev server başlatılıyor: http://localhost:4321"
echo "→ Tarayıcı 3 saniye sonra açılacak. Durdurmak için Ctrl+C."
echo ""

# 3 saniye sonra tarayıcıyı arka planda aç
(sleep 3 && open "http://localhost:4321") &

# Astro dev'i başlat (foreground)
npm run dev
