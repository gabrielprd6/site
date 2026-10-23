#!/usr/bin/env python3
"""Mesure la ressemblance entre les pages villes (contenu dupliqué = risque de « doorway pages »).

    python tools/similarity.py

Pour chaque page /automatisation-pme-<ville>/ : on isole le contenu de <main>, on remplace le nom
de la ville par VILLE (un simple échange de nom ne compte pas comme du contenu différent), puis on
découpe en « shingles » de 5 mots consécutifs.

  ressemblance  = part de shingles communs entre deux pages (Jaccard) ; plus c'est bas, mieux c'est
  gabarit       = part des shingles d'une page qui figurent aussi dans au moins 3 autres pages
  unique        = part des shingles qui ne figurent dans AUCUNE autre page ville

Repères (règles empiriques, pas des seuils officiels de Google) :
  ressemblance moyenne < 15 %, gabarit < 25 %, unique > 65 %.
"""
import itertools
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent / "content"))
import cities  # noqa: E402

N = 5


def norm(s):
    s = s.replace("’", " ").replace("'", " ").replace(" ", " ")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s)).strip()


def main_text(slug, name):
    html = (ROOT / f"automatisation-pme-{slug}" / "index.html").read_text(encoding="utf-8")
    m = re.search(r'<main id="contenu">(.*?)</main>', html, re.S)
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", m.group(1), flags=re.S)
    text = re.sub(r"<[^>]+>", " ", body)
    text = re.sub(r"&\w+;", " ", text)
    text = norm(text).replace(norm(name), "ville")
    return text


def shingles(text):
    w = text.split()
    return {" ".join(w[i:i + N]) for i in range(len(w) - N + 1)}, len(w)


def main():
    data = {}
    for c in cities.CITIES:
        sh, n = shingles(main_text(c["slug"], c["name"]))
        data[c["slug"]] = (sh, n)

    slugs = list(data)
    pairs = []
    for a, b in itertools.combinations(slugs, 2):
        sa, sb = data[a][0], data[b][0]
        pairs.append((len(sa & sb) / len(sa | sb), a, b))
    avg = sum(p[0] for p in pairs) / len(pairs)

    print(f"{'ville':12s} {'mots':>5s} {'gabarit':>8s} {'unique':>7s}")
    for s in slugs:
        sh, n = data[s]
        others = [data[o][0] for o in slugs if o != s]
        shared3 = sum(1 for x in sh if sum(x in o for o in others) >= 3)
        alone = sum(1 for x in sh if not any(x in o for o in others))
        print(f"{s:12s} {n:5d} {shared3 / len(sh):8.0%} {alone / len(sh):7.0%}")
    print(f"\nressemblance moyenne entre deux pages : {avg:.1%}")
    worst = max(pairs)
    print(f"paire la plus proche : {worst[1]} / {worst[2]} = {worst[0]:.1%}")


if __name__ == "__main__":
    main()
