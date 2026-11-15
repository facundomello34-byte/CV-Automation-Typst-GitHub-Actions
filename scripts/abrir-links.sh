#!/usr/bin/env bash
#
# abrir-links.sh — abre en el navegador las ofertas del reporte del día.
#
# Uso:
#   bash scripts/abrir-links.sh              # abre todas en pestañas
#   bash scripts/abrir-links.sh --dry-run    # solo lista las URLs
#   bash scripts/abrir-links.sh reports/otros-links.md
#
# Toma las URLs del archivo indicado (por defecto el reporte de hoy).
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DRY=0
FILE=""
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    -h|--help) sed -n '1,10p' "$0"; exit 0 ;;
    *) FILE="$arg" ;;
  esac
done

if [[ -z "$FILE" ]]; then
  FILE="$(ls -1t "$REPO_DIR"/reports/busqueda-avanzada-*.md 2>/dev/null | head -1 || true)"
fi
[[ -z "$FILE" || ! -f "$FILE" ]] && { echo "No encontré el archivo de links. Pasalo como argumento." >&2; exit 1; }

command -v xdg-open >/dev/null || { echo "Falta xdg-open (paquete xdg-utils)." >&2; exit 1; }

mapfile -t URLS < <(grep -oE 'https://[^ )>]+' "$FILE" | grep -vE 'bumeran.com.ar/en-buenos-aires$' | awk '!seen[$0]++')

if [[ ${#URLS[@]} -eq 0 ]]; then
  echo "No hay URLs en $FILE" >&2
  exit 1
fi

echo "Links encontrados en $(basename "$FILE"): ${#URLS[@]}"
for u in "${URLS[@]}"; do
  echo "  $u"
  if [[ $DRY -eq 0 ]]; then
    xdg-open "$u" >/dev/null 2>&1 &
    sleep 1
  fi
done
[[ $DRY -eq 0 ]] && echo "Listo: se abrieron en pestañas del navegador."
