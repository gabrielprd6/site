#!/usr/bin/env python3
"""Prépare les photos de villes : assets/img/villes/<ville>.webp (3:2, hero) et <ville>-sq.webp (carré).

    python tools/images.py <dossier des originaux>

Les originaux sont attendus sous la forme <ville>.<ext> (toulouse.webp, paris.jpg…) ou, à défaut,
numérotés 1 à 10 dans l'ordre de ORDER. Nécessite Pillow (pip install pillow), uniquement pour
cette étape : le build du site, lui, n'en a pas besoin.
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "villes"

ORDER = ["toulouse", "marseille", "paris", "lyon", "bordeaux", "nantes", "lille", "nice", "montpellier", "strasbourg"]

# Point d'intérêt horizontal (0 = gauche, 1 = droite) pour les recadrages carrés.
FOCUS = {"toulouse": 0.55, "marseille": 0.4, "paris": 0.66, "lyon": 0.5, "bordeaux": 0.5,
         "nantes": 0.45, "lille": 0.45, "nice": 0.42, "montpellier": 0.5, "strasbourg": 0.4}


def find_source(folder, slug):
    for p in folder.glob(f"{slug}.*"):
        return p
    n = ORDER.index(slug) + 1
    for p in folder.glob(f"{n}.*"):
        return p
    raise SystemExit(f"photo introuvable pour {slug}")


def main(folder):
    OUT.mkdir(parents=True, exist_ok=True)
    for slug in ORDER:
        im = Image.open(find_source(folder, slug)).convert("RGB")
        w = min(1200, im.width)
        hero = ImageOps.fit(im, (w, round(w / 1.5)), Image.LANCZOS, centering=(FOCUS[slug], 0.5))
        hero.save(OUT / f"{slug}.webp", "WEBP", quality=78, method=6)
        sq = ImageOps.fit(im, (240, 240), Image.LANCZOS, centering=(FOCUS[slug], 0.5))
        sq.save(OUT / f"{slug}-sq.webp", "WEBP", quality=80, method=6)
        print(f"{slug:12s} source {im.width}x{im.height} -> hero {hero.width}x{hero.height}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(Path(sys.argv[1]))
