#!/usr/bin/env python3
"""
InfoJunior - Generator automat data.json
Rulează automat prin GitHub Actions la fiecare push.
Scanează folderele din /lucrari/ și /rezultate/ și generează data.json.
"""

import os
import json
from pathlib import Path
from datetime import datetime

# ── Configurare secțiuni ──────────────────────────────────────────────────────
SECTIUNI = {
    "basme": {
        "label": "Lumea Basmelor",
        "ciclu": "primar",
        "icon": "🎨",
        "color": "#fff3cd",
        "extensii_imagine": True,
    },
    "grafica": {
        "label": "Grafică pe Calculator",
        "ciclu": "gimnaziu",
        "icon": "🖼️",
        "color": "#d4edda",
        "extensii_imagine": True,
    },
    "powerpoint": {
        "label": "Prezentări PowerPoint",
        "ciclu": "gimnaziu",
        "icon": "📊",
        "color": "#d1ecf1",
        "extensii_imagine": False,
    },
    "soft": {
        "label": "Soft Educațional & Jocuri",
        "ciclu": "gimnaziu",
        "icon": "🎮",
        "color": "#ede8fa",
        "extensii_imagine": False,
    },
    "web": {
        "label": "Pagini Web",
        "ciclu": "gimnaziu",
        "icon": "🌐",
        "color": "#e8f0fd",
        "extensii_imagine": False,
    },
    "scratch": {
        "label": "Scratch & Alice",
        "ciclu": "gimnaziu",
        "icon": "🐱",
        "color": "#fef2e2",
        "extensii_imagine": False,
    },
    "programare": {
        "label": "Programare C++",
        "ciclu": "direct",
        "icon": "💻",
        "color": "#e6f5ed",
        "extensii_imagine": False,
    },
    "robotica": {
        "label": "Robotică",
        "ciclu": "direct",
        "icon": "🤖",
        "color": "#fde8e8",
        "extensii_imagine": True,
    },
}

EXTENSII_IMAGINI = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}
EXTENSII_ASCUNSE = {".gitkeep", ".gitignore", ".ds_store"}

def format_nume(filename: str) -> str:
    """Transformă numele fișierului într-un titlu lizibil."""
    stem = Path(filename).stem
    # Elimină prefixe tip BASME_, GRAFICA_ etc.
    for prefix in ["BASME_", "GRAFICA_", "PPT_", "SOFT_", "WEB_",
                   "PROGRAMARE_", "ROBOTI_", "SCRATCH_"]:
        if stem.upper().startswith(prefix):
            stem = stem[len(prefix):]
            break
    return stem.replace("_", " ").replace("-", " ").title()

def scan_sectiune(folder: Path, sectiune_key: str) -> list:
    """Returnează lista fișierelor dintr-o secțiune."""
    fisiere = []
    if not folder.exists():
        return fisiere

    for f in sorted(folder.iterdir()):
        if f.is_dir():
            continue
        if f.suffix.lower() in EXTENSII_ASCUNSE:
            continue
        if f.name.startswith("."):
            continue

        ext = f.suffix.lower()
        este_imagine = ext in EXTENSII_IMAGINI

        entry = {
            "fisier": f.name,
            "cale": f"lucrari/{sectiune_key}/{f.name}",
            "titlu": format_nume(f.name),
            "sectiune": sectiune_key,
            "este_imagine": este_imagine,
            "extensie": ext.lstrip("."),
        }
        fisiere.append(entry)

    return fisiere

def scan_rezultate(folder: Path) -> list:
    """Returnează lista PDF-urilor din /rezultate/."""
    rezultate = []
    if not folder.exists():
        return rezultate

    for f in sorted(folder.iterdir()):
        if f.is_dir():
            continue
        if f.suffix.lower() != ".pdf":
            continue
        if f.name.startswith("."):
            continue

        rezultate.append({
            "fisier": f.name,
            "cale": f"rezultate/{f.name}",
            "titlu": format_nume(f.name),
        })

    return rezultate

def main():
    root = Path(__file__).parent

    lucrari_toate = []
    for key in SECTIUNI:
        folder = root / "lucrari" / key
        lucrari = scan_sectiune(folder, key)
        lucrari_toate.extend(lucrari)
        print(f"  {key}: {len(lucrari)} fișiere")

    rezultate = scan_rezultate(root / "rezultate")
    print(f"  rezultate: {len(rezultate)} PDF-uri")

    # ── Statistici ───────────────────────────────────────────────────────────
    total_imagini = sum(1 for l in lucrari_toate if l["este_imagine"])
    total_lucrari = len(lucrari_toate)

    data = {
        "actualizat": datetime.utcnow().strftime("%d.%m.%Y %H:%M UTC"),
        "stats": {
            "total_lucrari": total_lucrari,
            "total_imagini": total_imagini,
            "total_rezultate": len(rezultate),
            "total_sectiuni": len(SECTIUNI),
        },
        "sectiuni": SECTIUNI,
        "lucrari": lucrari_toate,
        "rezultate": rezultate,
    }

    output = root / "data.json"
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ data.json generat: {total_lucrari} lucrări, {len(rezultate)} rezultate PDF")

if __name__ == "__main__":
    main()
