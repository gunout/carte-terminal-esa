#!/usr/bin/env python3
# carte_esa.py - Carte du monde ASCII avec logo ESA

import shapefile
from pathlib import Path

BASE = Path(__file__).parent
SHP = BASE / "data" / "ne_110m_land.shp"

COLS, ROWS = 120, 50

# Codes ANSI
BLEU = "\033[94m"
BLEU_FONCE = "\033[34m"
JAUNE = "\033[93m"
ROUGE = "\033[91m"
RESET = "\033[0m"
GRAS = "\033[1m"

# --- Logo ESA en ASCII ---
LOGO_ESA = f"""{BLEU}{GRAS}
   ███████ ███████  █████
   ██      ██      ██   ██
   █████   ███████ ███████
   ██           ██ ██   ██
   ███████ ███████ ██   ██
{RESET}{JAUNE}   ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★{RESET}
"""

# --- Charger les polygones ---
sf = shapefile.Reader(str(SHP))
shapes = sf.shapes()

def point_in_polygon(x, y, points, parts):
    n = len(points)
    for i in range(len(parts)):
        start = parts[i]
        end = parts[i+1] if i+1 < len(parts) else n
        inside = False
        j = end - 1
        for k in range(start, end):
            xi, yi = points[k]
            xj, yj = points[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside
            j = k
        if inside:
            return True
    return False

def est_terre(lon, lat):
    for shape in shapes:
        bbox = shape.bbox
        if not (bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]):
            continue
        if point_in_polygon(lon, lat, shape.points, shape.parts):
            return True
    return False

# --- Générer la grille ---
grid = []
for i in range(ROWS):
    lat = 90 - i * 180 / ROWS
    row = []
    for j in range(COLS):
        lon = -180 + j * 360 / COLS
        if est_terre(lon, lat):
            row.append(f"{BLEU}•{RESET}" if (i + j) % 2 == 0 else f"{BLEU_FONCE}·{RESET}")
        else:
            row.append(" ")
    grid.append(row)

# Marquer Paris
paris_i = int((90 - 48.85) / 180 * ROWS)
paris_j = int((2.35 + 180) / 360 * COLS)
grid[paris_i][paris_j] = f"{ROUGE}X{RESET}"

# --- Affichage ---
print(LOGO_ESA)
print(f"{BLEU}+" + "-" * COLS + f"+{RESET}")
for row in grid:
    print(f"{BLEU}|{RESET}" + "".join(row) + f"{BLEU}|{RESET}")
print(f"{BLEU}+" + "-" * COLS + f"+{RESET}")
print(f"{ROUGE}X{RESET} = Paris (48.85°N, 2.35°E)   {BLEU}• ·{RESET} = Terre")
print(f"{JAUNE}★{RESET} Agence spatiale européenne — ESA")