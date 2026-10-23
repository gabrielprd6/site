#!/usr/bin/env python3
"""Vérifie les liens internes et les ancres du site généré (python tools/check_links.py)."""
import re
import sys
from pathlib import Path
from urllib.parse import urldefrag

ROOT = Path(__file__).resolve().parent.parent
pages = [p for p in ROOT.rglob("*.html") if not any(x in p.parts for x in ("tools", "Claude outputs", ".git"))]


def target(url):
    path = url.split("?")[0]
    f = ROOT / path.lstrip("/")
    if path.endswith("/"):
        f = f / "index.html"
    return f


ids = {}
for p in pages:
    ids[p] = set(re.findall(r'\sid="([^"]+)"', p.read_text(encoding="utf-8")))

bad = 0
for p in sorted(pages):
    html = p.read_text(encoding="utf-8")
    for href in re.findall(r'<a [^>]*href="([^"]+)"', html):
        if href.startswith(("http", "mailto:", "tel:")) or href == "#":
            continue
        base, frag = urldefrag(href)
        f = p if not base else target(base)
        if not f.exists():
            print(f"CASSÉ  {p.relative_to(ROOT)} → {href}")
            bad += 1
        elif frag and f.suffix == ".html" and f in ids and frag not in ids[f]:
            print(f"ANCRE  {p.relative_to(ROOT)} → {href}")
            bad += 1
    for src in re.findall(r'(?:src|href)="(/assets/[^"?]+)', html):
        if not (ROOT / src.lstrip("/")).exists():
            print(f"ASSET  {p.relative_to(ROOT)} → {src}")
            bad += 1
print(f"{len(pages)} pages vérifiées, {bad} problème(s).")
sys.exit(1 if bad else 0)
