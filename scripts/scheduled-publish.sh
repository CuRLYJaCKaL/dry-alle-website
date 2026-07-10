#!/bin/bash
# Dry Alle — zamanlanmis otomatik yayin (launchd ile gunluk calisir).
# Tarih-kapisi (date-gating): astro build yalnizca yayin tarihi gelmis (date <= bugun)
# bloglari uretir. Bu script gunluk build alir; cikti degistiyse (o gun bir yazinin
# tarihi geldiyse) astro-live'a deploy eder ve GitHub Pages build'ini tetikler.
# Cikti degismediyse deploy atlanir (bos commit/gereksiz build olusmaz).
set -euo pipefail
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

PROJ="/Users/macos/Documents/Projeler/DryAlleAstro"
LIVE="$PROJ/.deploy/live"
REPO="https://github.com/CuRLYJaCKaL/dry-alle-website.git"
LOG="$PROJ/.deploy/publish.log"
GH="/usr/local/bin/gh"

mkdir -p "$PROJ/.deploy"
ts() { date '+%Y-%m-%d %H:%M:%S'; }
log() { echo "[$(ts)] $*" >> "$LOG"; }

log "=== scheduled-publish basladi ==="

cd "$PROJ"
# Build — tarih-kapisi bugune kadar yayinlanacak yazilari dahil eder.
if ! npm run build >> "$LOG" 2>&1; then
  log "HATA: build basarisiz, deploy iptal."
  exit 1
fi
log "build tamam"

# astro-live klonunu hazirla (kalici .deploy/live)
if [ ! -d "$LIVE/.git" ]; then
  git clone --branch astro-live "$REPO" "$LIVE" >> "$LOG" 2>&1
  git -C "$LIVE" config credential.helper "!$GH auth git-credential"
else
  git -C "$LIVE" fetch origin astro-live >> "$LOG" 2>&1
  git -C "$LIVE" reset --hard origin/astro-live >> "$LOG" 2>&1
fi

# dist -> live
rsync -a --delete --exclude .git "$PROJ/dist/" "$LIVE/"

cd "$LIVE"
git add -A
if git diff --cached --quiet; then
  log "cikti degismedi — bu gun yayina girecek yeni yazi yok, deploy atlandi."
else
  git commit -q -m "Otomatik yayin: $(date '+%Y-%m-%d') tarih-kapili icerik guncellemesi"
  git push -q origin astro-live >> "$LOG" 2>&1
  "$GH" api -X POST repos/CuRLYJaCKaL/dry-alle-website/pages/builds >> "$LOG" 2>&1 || log "UYARI: Pages build tetigi basarisiz (push yine de yapildi)."
  log "DEPLOY edildi + Pages build tetiklendi."
fi
log "=== bitti ==="
