#!/usr/bin/env python3
"""Génère tout le site Croisia (HTML statique) à partir de tools/.

    python tools/build.py

Sources :
  tools/data/requetes.csv     plan de requêtes SEO (une ligne = une requête → une page cible)
  tools/content/hubs.py       pages piliers (solutions, secteurs, audit)
  tools/content/blog/*.md     articles (front matter + markdown léger)
  tools/templates/home.html   page d'accueil (gabarit)

Sortie : index.html, <slug>/index.html, blog/…, sitemap.xml, 404.html.
Aucune dépendance : bibliothèque standard uniquement.
"""
import csv
import datetime
import html as htmllib
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS / "content"))

import hubs as hubs_mod  # noqa: E402
import team as team_mod  # noqa: E402

SITE = "https://croisia.com"
TODAY = datetime.date.today().isoformat()
ASSET_V = "63"
EMAIL = "contact@croisia.com"

SEGMENTS = {
    "pme": {"label": "PME", "full": "Automatisation et IA pour PME", "hub": "/automatisation-pme/"},
    "recrutement": {"label": "Recrutement", "full": "Cabinets de recrutement", "hub": "/recrutement/"},
    "auto": {"label": "Concessions auto", "full": "Concessions automobiles", "hub": "/concessions-automobiles/"},
    "immo": {"label": "Immobilier", "full": "Agences immobilières", "hub": "/immobilier/"},
}

LOGO_SVG = (
    '<svg class="logo__mark" viewBox="-6 10 112 70" aria-hidden="true" focusable="false">'
    '<g opacity="0.1"><polygon points="8,54 20,66 8,78 -4,66"/><polygon points="36,54 48,66 36,78 24,66"/>'
    '<polygon points="64,54 76,66 64,78 52,66"/><polygon points="92,54 104,66 92,78 80,66"/></g>'
    '<g opacity="0.26"><polygon points="22,40 34,52 22,64 10,52"/><polygon points="50,40 62,52 50,64 38,52"/>'
    '<polygon points="78,40 90,52 78,64 66,52"/></g>'
    '<g opacity="0.58"><polygon points="36,26 48,38 36,50 24,38"/><polygon points="64,26 76,38 64,50 52,38"/></g>'
    '<polygon points="50,12 62,24 50,36 38,24"/></svg>'
)
ARROW = ('<svg class="icon btn__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
         '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>')
CHEVRON = ('<svg class="icon nav__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
           '<path d="m6 9 6 6 6-6"/></svg>')

# ----------------------------------------------------------------- texte


def esc(s):
    s = s.replace("&", "&amp;")
    s = re.sub(r"&amp;(#?\w+;)", r"&\1", s)  # garde les entités déjà écrites (&nbsp;…)
    return s.replace("<", "&lt;").replace(">", "&gt;")


def typo(markup):
    """Typographie française sur les seuls nœuds texte (pas dans les balises)."""
    out = []
    for part in re.split(r"(<[^>]+>)", markup):
        if part.startswith("<"):
            out.append(part)
            continue
        part = re.sub(r" ([?!:;»%€])", "\u00a0\\1", part)
        part = re.sub(r"(\d) (h|min|jours?|mois|ans|Mo|Ko|k€)\b", "\\1\u00a0\\2", part)
        part = part.replace("« ", "«\u00a0").replace("'", "\u2019")
        out.append(part)
    return "".join(out)


def inline(s):
    """Markdown en ligne : **gras**, *italique*, [lien](url)."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", s)

    def link(m):
        url = m.group(2)
        ext = ' rel="noopener" target="_blank"' if url.startswith("http") else ""
        return f'<a href="{url}"{ext}>{m.group(1)}</a>'

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    return typo(s)


def plain(s):
    """Texte brut pour balises meta / attributs."""
    return esc(s).replace('"', "&quot;").replace("'", "\u2019")


def strip_tags(s):
    return htmllib.unescape(re.sub(r"<[^>]+>", " ", s))


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def norm(s):
    s = s.replace("’", " ").replace("'", " ").replace(" ", " ")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s)).strip()


def md(text):
    """Markdown léger → HTML : titres, listes, tableaux, citations (encarts), paragraphes."""
    out = []
    blocks = re.split(r"\n\s*\n", text.strip())
    for b in blocks:
        lines = [ln.rstrip() for ln in b.split("\n") if ln.strip()]
        if not lines:
            continue
        first = lines[0]
        if first.startswith("### "):
            out.append(f'<h3>{inline(first[4:])}</h3>')
            rest = "\n".join(lines[1:])
            if rest:
                out.append(md(rest))
        elif first.startswith("## "):
            title = first[3:]
            out.append(f'<h2 id="{slugify(title)}">{inline(title)}</h2>')
            rest = "\n".join(lines[1:])
            if rest:
                out.append(md(rest))
        elif first.startswith("- "):
            items = [inline(re.sub(r"^- ", "", ln)) for ln in lines]
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
        elif re.match(r"\d+\. ", first):
            items = [inline(re.sub(r"^\d+\. ", "", ln)) for ln in lines]
            out.append("<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>")
        elif first.startswith("> "):
            inner = " ".join(re.sub(r"^> ?", "", ln) for ln in lines)
            out.append(f'<aside class="callout"><p>{inline(inner)}</p></aside>')
        elif first.startswith("|"):
            rows = [[c.strip() for c in ln.strip("|").split("|")] for ln in lines
                    if not re.match(r"^\|\s*:?-{2,}", ln)]
            head, body = rows[0], rows[1:]
            t = '<div class="table-wrap"><table><thead><tr>'
            t += "".join(f"<th scope=\"col\">{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            for r in body:
                t += "<tr>" + f'<th scope="row">{inline(r[0])}</th>' + "".join(
                    f"<td>{inline(c)}</td>" for c in r[1:]) + "</tr>"
            out.append(t + "</tbody></table></div>")
        elif first.startswith("<"):
            out.append("\n".join(lines))
        else:
            out.append(f"<p>{inline(' '.join(lines))}</p>")
    return "\n".join(out)


# ---------------------------------------------------------- plan de requêtes


def load_queries():
    """{chemin de page: [(priorité, requête, intention)]} d'après requetes.csv."""
    result = {}
    with open(TOOLS / "data" / "requetes.csv", encoding="utf-8", newline="") as f:
        rd = csv.reader(f)
        next(rd)
        for r in rd:
            if len(r) < 5 or not r[2].strip():
                continue
            target = r[4].strip()
            path = "/" if target.startswith("/ (Accueil)") else target.rstrip("/") + "/"
            result.setdefault(path, []).append((r[0], r[2].strip(), r[3]))
    return result


QUERIES = load_queries()

# ------------------------------------------------------------- contenu

HUBS = hubs_mod.HUBS
HUB_BY_PATH = {f"/{h['slug']}/": h for h in HUBS}


def parse_article(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
    meta, body = {}, raw
    if m:
        for ln in m.group(1).split("\n"):
            if ":" in ln:
                k, v = ln.split(":", 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    slug = path.stem
    words = len(re.findall(r"\w+", strip_tags(md(body))))
    return {
        "slug": slug,
        "path": f"/blog/{slug}/",
        "title": meta["title"],
        "h1": meta.get("h1", meta["title"]),
        "description": meta["description"],
        "segment": meta["segment"],
        "hub": meta.get("hub") or SEGMENTS[meta["segment"]]["hub"],
        "related": [s.strip() for s in meta.get("related", "").split(",") if s.strip()],
        "body": body,
        "minutes": max(2, round(words / 200)),
        "date": meta.get("date", TODAY),
    }


ARTICLES = [parse_article(p) for p in sorted((TOOLS / "content" / "blog").glob("*.md"))]
ART_BY_PATH = {a["path"]: a for a in ARTICLES}

# --------------------------------------------------------------- gabarits


def abs_url(path):
    return SITE + path


def head(title, description, path, *, jsonld=(), og_type="website", noindex=False, extra_head=""):
    ld = "".join(f'<script type="application/ld+json">{j}</script>\n' for j in jsonld)
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    t, d = plain(title), plain(description)
    return f"""<!DOCTYPE html>
<html lang="fr" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="theme-color" content="#FFFFFF">
<link rel="canonical" href="{abs_url(path)}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Croisia">
<meta property="og:url" content="{abs_url(path)}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{SITE}/assets/img/og-image.png">
{ld}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/css/styles.css?v={ASSET_V}">
<link rel="stylesheet" href="/assets/css/pages.css?v={ASSET_V}">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{extra_head}<script>
  // Avant le premier rendu : évite le flash de contenu masqué.
  (function () {{
    var el = document.documentElement;
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {{
      el.classList.add('js-anim');
      window.setTimeout(function () {{
        if (!el.classList.contains('anim-ready')) el.classList.remove('js-anim');
      }}, 2500);
    }}
  }})();
</script>
</head>
"""


def nav_items(group):
    return [h for h in HUBS if h.get("group") == group]


def header(current=""):
    def sub(group, ident, label):
        def item(h):
            here = ' aria-current="page"' if current == f"/{h['slug']}/" else ""
            return (f'<li><a href="/{h["slug"]}/"{here}><b>{inline(h["nav_label"])}</b>'
                    f'<span>{inline(h["nav_desc"])}</span></a></li>')

        items = "".join(item(h) for h in nav_items(group))
        return (f'<li class="nav__item has-sub"><button type="button" class="nav__btn" aria-expanded="false" '
                f'aria-controls="{ident}">{label}{CHEVRON}</button>'
                f'<ul class="nav__sub" id="{ident}">{items}</ul></li>')

    def cur(p):
        return ' aria-current="page"' if current == p or (p != "/" and current.startswith(p)) else ""

    mobile = ""
    for group, label in (("solutions", "Solutions"), ("secteurs", "Secteurs")):
        mobile += f'<p class="mobile-nav__h">{label}</p><ul>' + "".join(
            f'<li><a href="/{h["slug"]}/">{inline(h["nav_label"])}</a></li>' for h in nav_items(group)) + "</ul>"
    mobile += ('<p class="mobile-nav__h">Croisia</p><ul><li><a href="/blog/">Blog</a></li>'
               '<li><a href="/a-propos/notre-equipe/">À propos · Notre équipe</a></li></ul>')

    return f"""<body>
<a class="skip-link" href="#contenu">Aller au contenu principal</a>
<header class="header" id="header">
  <div class="shell header__inner">
    <a class="logo" href="/" aria-label="Croisia, accueil">
      {LOGO_SVG}
      <span class="logo__word">CROISIA</span>
    </a>
    <nav class="nav" id="nav" aria-label="Navigation principale">
      <ul class="nav__list">
        {sub("solutions", "sub-solutions", "Solutions")}
        {sub("secteurs", "sub-secteurs", "Secteurs")}
        <li><a href="/blog/"{cur("/blog/")}>Blog</a></li>
        <li><a href="/a-propos/notre-equipe/"{cur("/a-propos/")}>À propos</a></li>
      </ul>
    </nav>
    <div class="header__actions">
      <a class="btn btn--ink btn--sm header__cta" href="/audit-gratuit/">Audit gratuit</a>
      <button class="icon-btn nav-toggle" id="nav-toggle" type="button"
              aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-nav">
        <svg class="icon icon--menu" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 8h16"/><path d="M4 16h16"/></svg>
        <svg class="icon icon--close" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
      </button>
    </div>
  </div>
  <div class="header__progress" aria-hidden="true"><span id="scroll-progress"></span></div>
</header>

<div class="mobile-nav" id="mobile-nav" hidden>
  <nav aria-label="Navigation mobile">{mobile}</nav>
  <a class="btn btn--ink btn--block" href="/audit-gratuit/">Demander mon audit gratuit</a>
</div>
"""


def footer():
    def col(title, group):
        return (f'<nav class="footer__nav" aria-label="{title}"><h2 class="footer__h">{title}</h2><ul>' + "".join(
            f'<li><a href="/{h["slug"]}/">{inline(h["nav_label"])}</a></li>' for h in nav_items(group)) + "</ul></nav>")

    popular = [ART_BY_PATH[p] for p in hubs_mod.FOOTER_ARTICLES if p in ART_BY_PATH]
    guides = "".join(f'<li><a href="{a["path"]}">{inline(a["title"])}</a></li>' for a in popular)
    zones = ('<nav class="footer__zones" aria-label="Automatisation et IA par ville"><h2 class="footer__h">Automatisation et IA à</h2><ul>'
             + "".join(f'<li><a href="/{h["slug"]}/">{inline(h["nav_label"])}</a></li>' for h in HUBS if h.get("group") == "villes")
             + '</ul></nav>')
    return f"""<footer class="footer">
  <div class="shell">
    <div class="footer__inner footer__inner--wide">
      <div class="footer__brand">
        <p class="footer__baseline">Faites monter votre entreprise d'un cran.</p>
        <a class="btn btn--ink btn--sm" href="/audit-gratuit/">Audit gratuit</a>
      </div>
      {col("Solutions", "solutions")}
      {col("Secteurs", "secteurs")}
      <nav class="footer__nav" aria-label="Ressources"><h2 class="footer__h">Ressources</h2><ul>
        <li><a href="/blog/">Tous les guides</a></li>{guides}</ul></nav>
      <div class="footer__contact">
        <h2 class="footer__h">Contact</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="/audit-gratuit/">Audit gratuit</a></li>
          <li><a href="/a-propos/notre-equipe/">Notre équipe</a></li>
        </ul>
      </div>
    </div>
    {zones}
    <a class="footer__word" href="/" aria-label="Croisia, accueil"><span aria-hidden="true">CROISIA</span></a>
    <div class="footer__legal">
      <p>© <span id="year">2026</span> Croisia. Tous droits réservés.</p>
      <ul>
        <li><a href="/mentions-legales.html">Mentions légales</a></li>
        <li><a href="/confidentialite.html">Politique de confidentialité</a></li>
      </ul>
    </div>
  </div>
</footer>
"""


def scripts(home=False):
    if home:
        return """<script src="/assets/js/intro.js?v=%s" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
<script src="/assets/js/main.js?v=%s" defer></script>
<script src="/assets/js/motion.js?v=%s" defer></script>
</body>
</html>
""" % (ASSET_V, ASSET_V, ASSET_V)
    return f"""<script src="/assets/js/main.js?v={ASSET_V}" defer></script>
</body>
</html>
"""


def breadcrumb(trail):
    """trail : [(label, path)] ; le dernier élément est la page courante."""
    items = []
    for i, (label, path) in enumerate(trail):
        if i == len(trail) - 1:
            items.append(f'<li aria-current="page">{inline(label)}</li>')
        else:
            items.append(f'<li><a href="{path}">{inline(label)}</a></li>')
    return f'<nav class="crumbs" aria-label="Fil d\'Ariane"><ol>{"".join(items)}</ol></nav>'


def breadcrumb_ld(trail):
    import json
    return json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": strip_tags(inline(label)), "item": abs_url(path)}
            for i, (label, path) in enumerate(trail)],
    }, ensure_ascii=False, separators=(",", ":"))


def cta_band(title="Prêt à gagner du temps ?", text=None, label="Demander mon audit gratuit"):
    text = text or ("30 minutes en visio, sans engagement. On identifie ensemble les tâches à automatiser en "
                    "priorité et on vous répond sous 24 h.")
    return f"""<section class="section cta-band" aria-labelledby="cta-title">
  <div class="shell cta-band__inner" data-reveal="up">
    <div>
      <h2 class="sec-title" id="cta-title">{inline(title)}</h2>
      <p class="sec-lede">{inline(text)}</p>
    </div>
    <div class="cta-band__actions">
      <a class="btn btn--ink btn--lg" href="/audit-gratuit/">{inline(label)}{ARROW}</a>
      <p class="hero__note">Sans engagement · Réponse sous 24 h</p>
    </div>
  </div>
</section>
"""


def article_cards(arts, with_segment=True):
    cards = []
    for a in arts:
        seg = SEGMENTS[a["segment"]]["label"]
        tag = f'<span class="card__tag">{seg}</span>' if with_segment else ""
        cards.append(
            f'<li class="card card--article" data-reveal="up"><a class="card__link" href="{a["path"]}">'
            f'{tag}<h3>{inline(a["title"])}</h3><p>{inline(a["description"])}</p>'
            f'<span class="card__meta">{a["minutes"]} min de lecture</span></a></li>')
    return '<ul class="cards cards--3">' + "".join(cards) + "</ul>"


# ------------------------------------------------------------ blocs de hub

STEPS_DEFAULT = [
    ("Audit gratuit", "On identifie ensemble vos tâches à fort potentiel. 30 minutes, en visio."),
    ("Devis sur mesure", "Un plan clair et chiffré, avec le gain de temps estimé pour chaque chantier."),
    ("Mise en place", "On construit et on connecte. Vos équipes sont formées en même temps."),
    ("Suivi", "Ajustements, mesure des résultats et accompagnement dans le temps."),
]


def sec_head(b, center=False):
    eyebrow = (f'<p class="eyebrow{" eyebrow--center" if center else ""}"><span class="eyebrow__rule" '
               f'aria-hidden="true"></span>{inline(b["eyebrow"])}</p>') if b.get("eyebrow") else ""
    lede = f'<p class="sec-lede">{inline(b["lede"])}</p>' if b.get("lede") else ""
    cls = "sec-head sec-head--flat" + (" sec-head--center" if center else "")
    return (f'<header class="{cls}" data-reveal="up">{eyebrow}<h2 class="sec-title">{inline(b["title"])}</h2>'
            f'{lede}</header>')


def faq_html(items, uid):
    out = []
    for i, (q, a) in enumerate(items, 1):
        out.append(f"""<div class="faq__item">
  <h3><button type="button" class="faq__q" aria-expanded="false" aria-controls="{uid}-{i}" id="{uid}-{i}-btn">
    <span>{inline(q)}</span><span class="faq__sign" aria-hidden="true"></span></button></h3>
  <div class="faq__a" id="{uid}-{i}" role="region" aria-labelledby="{uid}-{i}-btn"><div class="faq__a-inner">{md(a)}</div></div>
</div>""")
    return '<div class="faq">' + "".join(out) + "</div>"


def render_block(b, hub, n):
    t = b["type"]
    tint = " section--tint" if b.get("tint") else ""
    if t == "pains":
        items = "".join(f'<li class="pain" data-reveal="up"><h3>{inline(h)}</h3><p>{inline(p)}</p></li>'
                        for h, p in b["items"])
        return f'<section class="section{tint}"><div class="shell">{sec_head(b)}<ul class="pains">{items}</ul></div></section>'
    if t == "cards":
        cols = b.get("cols", 3)
        cards = []
        for it in b["items"]:
            bullets = ("<ul class=\"card__list\">" + "".join(f"<li>{inline(x)}</li>" for x in it["bullets"]) + "</ul>"
                       if it.get("bullets") else "")
            body = f'<h3>{inline(it["title"])}</h3><p>{inline(it["text"])}</p>{bullets}'
            if it.get("href"):
                body = (f'<a class="card__link" href="{it["href"]}">{body}'
                        f'<span class="card__more">{inline(it.get("more", "En savoir plus"))} →</span></a>')
            cards.append(f'<li class="card" data-reveal="up">{body}</li>')
        return (f'<section class="section{tint}"><div class="shell">{sec_head(b)}'
                f'<ul class="cards cards--{cols}">{"".join(cards)}</ul></div></section>')
    if t == "split":
        bullets = "".join(f"<li>{inline(x)}</li>" for x in b.get("bullets", []))
        paras = md(b["md"]) if b.get("md") else ""
        meta = f'<p class="feature__meta">{inline(b["meta"])}</p>' if b.get("meta") else ""
        rev = " feature__inner--reverse" if b.get("reverse") else ""
        sid = f' id="{b["id"]}"' if b.get("id") else ""
        return f"""<section{sid} class="section{tint}"><div class="shell feature__inner{rev}">
  <div class="feature__text prose" data-reveal="up">
    {('<p class="eyebrow"><span class="eyebrow__rule" aria-hidden="true"></span>' + inline(b["eyebrow"]) + '</p>') if b.get("eyebrow") else ''}
    <h2 class="sec-title">{inline(b["title"])}</h2>{paras}{meta}
  </div>
  <ul class="feature__list" data-reveal="up">{bullets}</ul>
</div></section>"""
    if t == "prose":
        return (f'<section class="section{tint}"><div class="shell shell--prose">{sec_head(b)}'
                f'<div class="prose">{md(b["md"])}</div></div></section>')
    if t == "steps":
        steps = b.get("items", STEPS_DEFAULT)
        lis = "".join(f'<li class="step" data-reveal="up"><span class="step__n" aria-hidden="true">0{i}</span>'
                      f'<h3>{inline(h)}</h3><p>{inline(p)}</p></li>' for i, (h, p) in enumerate(steps, 1))
        head_b = {"eyebrow": b.get("eyebrow", "Méthode"), "title": b.get("title", "Comment ça se passe"),
                  "lede": b.get("lede", "Quatre étapes, zéro jargon. Vous savez à tout moment où vous en êtes et ce que ça coûte.")}
        return (f'<section class="section{tint}"><div class="shell">{sec_head(head_b)}'
                f'<ol class="steps steps--plain">{lis}</ol></div></section>')
    if t == "table":
        return (f'<section class="section{tint}"><div class="shell">{sec_head(b)}'
                f'{md(b["md"])}</div></section>')
    if t == "faq":
        return (f'<section class="section{tint}" id="faq"><div class="shell faq__layout">'
                f'<div class="faq__aside"><p class="eyebrow"><span class="eyebrow__rule" aria-hidden="true"></span>FAQ</p>'
                f'<h2 class="sec-title">{inline(b.get("title", "Questions fréquentes"))}</h2></div>'
                f'{faq_html(hub["faq"], "faq")}</div></section>')
    if t == "articles":
        arts = [a for a in ARTICLES if a["hub"] == f"/{hub['slug']}/"]
        if b.get("segment"):
            arts += [a for a in ARTICLES if a["segment"] == b["segment"] and a not in arts]
        arts = arts[: b.get("max", 9)]
        if not arts:
            return ""
        head_b = {"eyebrow": "Guides", "title": b.get("title", "Nos guides sur le sujet"), "lede": b.get("lede")}
        return (f'<section class="section section--tint"><div class="shell">{sec_head(head_b)}'
                f'{article_cards(arts, with_segment=False)}'
                f'<p class="more-link"><a class="link-u" href="/blog/">Tous les guides →</a></p></div></section>')
    if t == "links":
        cards = []
        for slug in b["slugs"]:
            h = next(x for x in HUBS if x["slug"] == slug)
            cards.append({"title": h["card_title"], "text": h["card_text"], "href": f"/{slug}/"})
        return render_block({"type": "cards", "eyebrow": b.get("eyebrow", "À lire aussi"),
                             "title": b.get("title", "Pour aller plus loin"), "items": cards,
                             "cols": min(3, len(cards))}, hub, n)
    if t == "cities":
        label = {"automatisation": ("Automatisation PME à", "automatisation", "Automatisation PME"),
                 "ia": ("IA pour PME à", "ia-pour-pme", "IA pour PME"),
                 "agents": ("Agent IA à", "agents-ia", "Agents IA")}[b["service"]]
        lis = "".join(
            f'<li><a class="city-tile" href="/{h["slug"]}/">'
            f'<img src="/assets/img/villes/{h["city"]}-sq.webp" alt="" width="240" height="240" loading="lazy" decoding="async">'
            f'<span class="city-tile__txt"><span class="sr-only">{label[0]} </span><b>{inline(h["nav_label"])}</b></span></a></li>'
            for h in HUBS if h.get("group") == "villes")
        head_b = {"eyebrow": "Près de chez vous", "title": b.get("title", f"{label[2]} dans votre ville"),
                  "lede": "Le contexte local, les priorités et les cas d'usage, ville par ville. Tout se fait en visio, partout en France."}
        return (f'<section class="section{tint}"><div class="shell">{sec_head(head_b)}'
                f'<ul class="city-tiles">{lis}</ul></div></section>')
    if t == "form":
        bullets = "".join(f"<li>{inline(x)}</li>" for x in b.get("bullets", []))
        return (f'<section class="section section--tint" id="contact"><div class="shell cta-final__inner">'
                f'<div class="cta-final__copy" data-reveal="up"><p class="eyebrow"><span class="eyebrow__rule" '
                f'aria-hidden="true"></span>{inline(b["eyebrow"])}</p>'
                f'<h2 class="cta-final__title">{inline(b["title"])}</h2>'
                f'<p class="cta-final__lede">{inline(b["lede"])}</p><ul class="cta-final__list">{bullets}</ul></div>'
                f'{b["html"]}</div></section>')
    raise ValueError(f"bloc inconnu : {t}")


def page_hero(hub, trail):
    actions = (f'<a class="btn btn--ink btn--lg" href="{hub.get("cta_href", "/audit-gratuit/")}">{inline(hub.get("cta", "Demander mon audit gratuit"))}{ARROW}</a>')
    if hub.get("secondary"):
        s = hub["secondary"]
        actions += f'<a class="link-u" href="{s[1]}">{inline(s[0])}</a>'
    points = ""
    if hub.get("points"):
        points = '<ul class="phero__points">' + "".join(f"<li>{inline(p)}</li>" for p in hub["points"]) + "</ul>"
    text = f"""<p class="eyebrow"><span class="eyebrow__rule" aria-hidden="true"></span>{inline(hub["eyebrow"])}</p>
    <h1 class="phero__title">{inline(hub["h1"])}</h1>
    <p class="phero__lede">{inline(hub["lede"])}</p>
    <div class="phero__actions">{actions}</div>
    <p class="hero__note">Sans engagement · Réponse sous 24 h · 30 min de votre temps</p>
    {points}"""
    if hub.get("photo"):
        return f"""<section class="phero phero--photo">
  <div class="shell phero__inner">
    {breadcrumb(trail)}
    <div class="phero__grid">
      <div class="phero__text">
    {text}
      </div>
      <figure class="phero__photo"><img src="{hub["photo"]}" alt="{plain(hub["photo_alt"])}" width="1200" height="800" fetchpriority="high" decoding="async"></figure>
    </div>
  </div>
</section>"""
    return f"""<section class="phero">
  <div class="shell phero__inner">
    {breadcrumb(trail)}
    {text}
  </div>
</section>"""


def faq_ld(items):
    """Schéma FAQPage : réponses en texte brut (sans liens ni gras markdown)."""
    import json
    def plain_md(a):
        a = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", a)
        return re.sub(r"\*\*|\*", "", a)
    return json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": plain_md(a)}} for q, a in items],
    }, ensure_ascii=False, separators=(",", ":"))


def service_ld(hub, path):
    import json
    area = {"@type": "City", "name": hub["area"]} if hub.get("area") else {"@type": "Country", "name": "France"}
    return json.dumps({
        "@context": "https://schema.org", "@type": "Service", "name": strip_tags(inline(hub["h1"])),
        "description": hub["description"], "url": abs_url(path), "serviceType": hub.get("service_type", hub["nav_label"]),
        "areaServed": area,
        "provider": {"@type": "ProfessionalService", "name": "Croisia", "url": SITE + "/"},
    }, ensure_ascii=False, separators=(",", ":"))


def render_hub(hub, form_html):
    path = f"/{hub['slug']}/"
    trail = [("Accueil", "/")]
    if hub.get("parent"):
        trail.append(hub["parent"])
    trail.append((hub["breadcrumb"] if hub.get("breadcrumb") else hub["nav_label"], path))
    blocks = []
    for i, b in enumerate(hub["blocks"]):
        if b["type"] == "form":
            b = dict(b, html=form_html)
        blocks.append(render_block(b, hub, i))
    has_form = any(b["type"] == "form" for b in hub["blocks"])
    jsonld = [service_ld(hub, path), breadcrumb_ld(trail)]
    if hub.get("faq"):
        jsonld.append(faq_ld(hub["faq"]))
    page = head(hub["title"], hub["description"], path, jsonld=jsonld)
    page += header(path)
    page += f'<main id="contenu">\n{page_hero(hub, trail)}\n' + "\n".join(blocks)
    if not has_form:
        page += "\n" + cta_band(hub.get("cta_title", "Prêt à gagner du temps ?"), hub.get("cta_text"))
    page += "</main>\n" + footer() + scripts()
    return page


# -------------------------------------------------------------- blog


def render_article(a):
    trail = [("Accueil", "/"), ("Blog", "/blog/"), (a["h1"], a["path"])]
    hub = HUB_BY_PATH.get(a["hub"])
    body = md(a["body"])
    h2s = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    toc = ""
    if len(h2s) >= 3:
        toc = ('<nav class="toc" aria-label="Sommaire"><p class="toc__h">Dans cet article</p><ol>' +
               "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in h2s) + "</ol></nav>")

    related = [ART_BY_PATH[f"/blog/{s}/"] for s in a["related"] if f"/blog/{s}/" in ART_BY_PATH]
    for other in ARTICLES:
        if len(related) >= 3:
            break
        if other is not a and other not in related and (other["hub"] == a["hub"] or other["segment"] == a["segment"]):
            related.append(other)
    related = related[:3]

    seg = SEGMENTS[a["segment"]]
    hub_box = ""
    if hub:
        hub_box = (f'<aside class="callout callout--hub"><p><strong>{inline(hub["card_title"])}.</strong> '
                   f'{inline(hub["card_text"])} <a href="{a["hub"]}">Voir la page →</a></p></aside>')
    import json
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": strip_tags(inline(a["h1"])),
        "description": a["description"], "datePublished": a["date"], "dateModified": TODAY,
        "mainEntityOfPage": abs_url(a["path"]), "inLanguage": "fr",
        "image": SITE + "/assets/img/og-image.png",
        "author": {"@type": "Organization", "name": "Croisia", "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": "Croisia", "url": SITE + "/",
                      "logo": {"@type": "ImageObject", "url": SITE + "/icon-192.png"}},
    }, ensure_ascii=False, separators=(",", ":"))

    page = head(a["title"] + (" | Croisia" if len(a["title"]) <= 50 else ""), a["description"], a["path"], jsonld=[ld, breadcrumb_ld(trail)], og_type="article")
    page += header("/blog/")
    page += f"""<main id="contenu">
<article class="article">
  <header class="article__head shell shell--prose">
    {breadcrumb(trail)}
    <p class="card__tag"><a href="/blog/#{a["segment"]}">{seg["label"]}</a></p>
    <h1 class="article__title">{inline(a["h1"])}</h1>
    <p class="article__lede">{inline(a["description"])}</p>
    <p class="article__meta">Par l'équipe Croisia · {a["minutes"]} min de lecture · mis à jour le {fr_date(TODAY)}</p>
  </header>
  <div class="shell shell--prose">
    {toc}
    <div class="prose">{body}</div>
    {hub_box}
    <aside class="article__cta" aria-label="Audit gratuit">
      <h2>Un cas concret à automatiser ?</h2>
      <p>Décrivez-nous la tâche qui vous coûte le plus de temps. L'audit dure 30 minutes, il est gratuit et sans engagement.</p>
      <a class="btn btn--ink btn--lg" href="/audit-gratuit/">Demander mon audit gratuit{ARROW}</a>
    </aside>
  </div>
</article>
"""
    if related:
        page += (f'<section class="section section--tint"><div class="shell"><header class="sec-head sec-head--flat">'
                 f'<p class="eyebrow"><span class="eyebrow__rule" aria-hidden="true"></span>À lire aussi</p>'
                 f'<h2 class="sec-title">Dans la même série</h2></header>{article_cards(related)}</div></section>')
    page += "</main>\n" + footer() + scripts()
    return page


MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre",
          "novembre", "décembre"]


def fr_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def render_blog_index():
    trail = [("Accueil", "/"), ("Blog", "/blog/")]
    sections = []
    chips = []
    for key, seg in SEGMENTS.items():
        arts = [a for a in ARTICLES if a["segment"] == key]
        if not arts:
            continue
        chips.append(f'<li><a href="#{key}">{seg["label"]} <span>{len(arts)}</span></a></li>')
        sections.append(f"""<section class="section blog-seg" id="{key}">
  <div class="shell">
    <header class="sec-head sec-head--flat"><h2 class="sec-title">{inline(seg["full"])}</h2>
    <p class="sec-lede"><a class="link-u" href="{seg["hub"]}">Voir la page {inline(HUB_BY_PATH[seg["hub"]]["nav_label"])} →</a></p></header>
    {article_cards(arts, with_segment=False)}
  </div>
</section>""")
    title = "Blog Croisia : guides d'automatisation et d'IA pour PME"
    desc = ("Guides pratiques pour automatiser votre PME : devis, relances, CRM, agents IA, Make et n8n, "
            "avec des cas concrets en recrutement, auto et immobilier.")
    page = head(title, desc, "/blog/", jsonld=[breadcrumb_ld(trail)])
    page += header("/blog/")
    page += f"""<main id="contenu">
<section class="phero phero--compact"><div class="shell phero__inner">
  {breadcrumb(trail)}
  <p class="eyebrow"><span class="eyebrow__rule" aria-hidden="true"></span>Blog</p>
  <h1 class="phero__title">Guides d'automatisation et d'IA pour PME</h1>
  <p class="phero__lede">Des guides concrets, sans jargon : ce qu'on peut automatiser, avec quels outils, et par où commencer.</p>
  <ul class="chips" aria-label="Filtrer par thème">{"".join(chips)}</ul>
</div></section>
{"".join(sections)}
{cta_band("Un sujet qui vous concerne ?", "Parlons-en pendant l'audit gratuit : 30 minutes pour repérer ce qui peut être automatisé chez vous.")}
</main>
""" + footer() + scripts()
    return page


# ------------------------------------------------------------- accueil


def render_home(form_html):
    tpl = (TOOLS / "templates" / "home.html").read_text(encoding="utf-8")
    h = head(
        "Croisia — Agence d'automatisation et d'IA pour PME",
        "Croisia, agence et consultants en automatisation et en IA pour PME : automatisations Make et n8n, "
        "agents IA sur mesure, audit gratuit et sans engagement.",
        "/", jsonld=[hubs_mod.HOME_LD], extra_head=hubs_mod.HOME_HEAD_EXTRA)
    sectors = "".join(
        f'<li class="card" data-reveal="up"><a class="card__link" href="/{x["slug"]}/"><h3>{inline(x["card_title"])}</h3>'
        f'<p>{inline(x["card_text"])}</p><span class="card__more">En savoir plus →</span></a></li>'
        for x in nav_items("secteurs"))
    solutions = "".join(
        f'<li class="card" data-reveal="up"><a class="card__link" href="/{x["slug"]}/"><h3>{inline(x["card_title"])}</h3>'
        f'<p>{inline(x["card_text"])}</p><span class="card__more">En savoir plus →</span></a></li>'
        for x in nav_items("solutions"))
    picks = [ART_BY_PATH[p] for p in hubs_mod.HOME_ARTICLES if p in ART_BY_PATH]
    out = (tpl.replace("{{HEAD}}", h).replace("{{HEADER}}", header("/"))
           .replace("{{FOOTER}}", footer()).replace("{{SCRIPTS}}", scripts(home=True))
           .replace("{{SOLUTIONS}}", solutions).replace("{{SECTEURS}}", sectors)
           .replace("{{ARTICLES}}", article_cards(picks)))
    return out


def extract_form(home_tpl):
    m = re.search(r"<!--FORM-->(.*?)<!--/FORM-->", home_tpl, re.S)
    return m.group(1).strip()


# ------------------------------------------------------------- 404 / plan


def render_404():
    page = head("Page introuvable | Croisia", "Cette page n'existe pas ou a changé d'adresse.", "/404.html", noindex=True)
    page += header("")
    links = "".join(f'<li><a href="/{h["slug"]}/">{inline(h["nav_label"])}</a></li>'
                    for h in HUBS if h.get("group") in ("solutions", "secteurs"))
    page += f"""<main id="contenu"><section class="phero"><div class="shell phero__inner">
<p class="eyebrow"><span class="eyebrow__rule" aria-hidden="true"></span>Erreur 404</p>
<h1 class="phero__title">Cette page n'existe pas (ou plus).</h1>
<p class="phero__lede">Vous cherchiez peut-être l'une de ces pages :</p>
<ul class="chips chips--wrap">{links}<li><a href="/blog/">Blog</a></li><li><a href="/">Accueil</a></li></ul>
</div></section></main>
""" + footer() + scripts()
    return page


def write(path, content):
    p = ROOT / path.lstrip("/")
    if p.suffix != ".html" and p.suffix != ".xml":
        p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8", newline="\n")


def sitemap(urls):
    rows = "".join(
        f"  <url><loc>{abs_url(p)}</loc><lastmod>{TODAY}</lastmod><changefreq>{cf}</changefreq>"
        f"<priority>{pr}</priority></url>\n" for p, cf, pr in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "</urlset>\n")


# ------------------------------------------------------------ Notre équipe

LINKEDIN = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3V9.75zm6.5 0h3.83v1.54h.05c.53-1 1.84-2.05 3.78-2.05 4.04 0 4.79 2.66 4.79 6.12V21h-4v-4.92c0-1.17-.02-2.68-1.63-2.68-1.63 0-1.88 1.28-1.88 2.6V21h-4V9.75z"/></svg>')


def render_team():
    t = team_mod
    path = "/a-propos/notre-equipe/"
    trail = [("Accueil", "/"), ("Notre équipe", path)]
    import json
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "AboutPage", "name": "Notre équipe", "url": abs_url(path),
        "mainEntity": {"@type": "Organization", "name": "Croisia", "url": SITE + "/",
                       "member": [{"@type": "Person", "name": m["name"], "jobTitle": m["role"].split("·")[-1].strip(),
                                   "worksFor": {"@type": "Organization", "name": "Croisia"}} for m in t.MEMBERS]},
    }, ensure_ascii=False, separators=(",", ":"))

    stats = "".join(f'<li><b>{inline(n)}</b><span>{inline(l)}</span></li>' for n, l in t.STATS)
    cards = []
    for m in t.MEMBERS:
        li = (f'<a class="member__in" href="{m["linkedin"]}" rel="noopener" target="_blank" aria-label="LinkedIn de {plain(m["name"])}">{LINKEDIN}</a>'
              if m.get("linkedin") else "")
        rdv = '<a class="btn btn--ink btn--sm" href="/audit-gratuit/">Prendre RDV</a>' if m.get("rdv") else ""
        cards.append(f'''<li class="member" data-reveal="up">
  <div class="member__photo"><img src="{m["photo"]}" alt="Portrait de {plain(m["name"])}" width="800" height="1000"></div>
  <h3>{inline(m["name"])}</h3><p>{inline(m["role"])}</p>
  <div class="member__actions">{rdv}{li}</div>
</li>''')
    q = t.TESTIMONIAL
    gallery = "".join(
        f'<li><img src="{src}" alt="{plain(cap)}" width="{w}" height="{h}" loading="lazy" decoding="async"><span>{inline(cap)}</span></li>'
        for src, cap, w, h in t.GALLERY)
    panels = []
    for p in t.JOIN:
        btns = "".join(f'<a class="btn {"btn--ink" if main else "btn--ghost"} btn--sm" href="{href}">{inline(label)}</a>' for label, href, main in p["buttons"])
        panels.append(f'<div class="join__panel" data-reveal="up"><h3>{inline(p["title"])}</h3><p>{inline(p["text"])}</p><div class="join__btns">{btns}</div></div>')
    exp = "".join(f'<li><a href="{href}">{inline(label)} →</a></li>' for label, href in t.EXPERTISES)
    gallery_section = (f'''<section class="section" aria-labelledby="vie-title">
  <div class="shell">
    <header class="sec-head sec-head--flat" data-reveal="up"><h2 class="sec-title" id="vie-title">La vie chez Croisia</h2></header>
    <ul class="tgallery">{gallery}</ul>
  </div>
</section>''' if t.GALLERY else "")

    page = head(t.TITLE, t.DESCRIPTION, path, jsonld=[ld, breadcrumb_ld(trail)])
    page += header(path)
    page += f"""<main id="contenu">
<section class="thero">
  <img class="thero__bg" src="{t.HERO["image"]}" alt="{plain(t.HERO["alt"])}" width="1136" height="941" fetchpriority="high" decoding="async">
  <div class="shell thero__inner">
    <div class="thero__crumbs">{breadcrumb(trail)}</div>
    <h1 class="thero__title">Notre équipe</h1>
    <p class="thero__lede">{inline(t.HERO["tagline"])}</p>
    <div class="thero__actions">
      <a class="btn btn--ink btn--lg" href="/audit-gratuit/">Parler à nos experts{ARROW}</a>
      <a class="btn btn--light btn--lg" href="/automatisation-pme/">Découvrir nos services</a>
    </div>
  </div>
</section>

<section class="stats-strip" aria-label="Croisia en chiffres"><div class="shell"><ul>{stats}</ul></div></section>

<section class="section" id="equipe">
  <div class="shell">
    <header class="sec-head sec-head--flat" data-reveal="up"><h2 class="sec-title">L'équipe</h2></header>
    <ul class="members">{"".join(cards)}</ul>
  </div>
</section>

<section class="section section--tint" aria-labelledby="avis-title">
  <div class="shell">
    <header class="sec-head sec-head--flat" data-reveal="up">
      <h2 class="sec-title" id="avis-title">Qui de mieux que nos clients pour parler de nous ?</h2>
    </header>
    <figure class="bubble bubble--feature" data-reveal="up">
      <p class="bubble__text">{inline(q["text"])}</p>
      <figcaption class="bubble__cite">
        <span class="bubble__ava"><img src="{q["photo"]}" alt="{plain(q["name"])}" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="bubble__by"><span class="bubble__name">{inline(q["name"])}</span><span class="bubble__role">{inline(q["role"])}</span></span>
      </figcaption>
    </figure>
  </div>
</section>

{gallery_section}

<section class="section section--tint" aria-labelledby="join-title">
  <div class="shell">
    <header class="sec-head sec-head--flat" data-reveal="up">
      <h2 class="sec-title" id="join-title">Envie de travailler avec nous ?</h2>
      <p class="sec-lede">Deux façons de nous rencontrer.</p>
    </header>
    <div class="join">{"".join(panels)}</div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <header class="sec-head sec-head--flat" data-reveal="up"><h2 class="sec-title">Nos expertises</h2></header>
    <ul class="exp-list">{exp}</ul>
  </div>
</section>
</main>
""" + footer() + scripts()
    return page


# --------------------------------------------------------------- main


def main():
    home_tpl = (TOOLS / "templates" / "home.html").read_text(encoding="utf-8")
    form_html = extract_form(home_tpl)

    pages = {}  # chemin → html (pour le contrôle de couverture)
    pages["/"] = render_home(form_html)
    for hub in HUBS:
        pages[f"/{hub['slug']}/"] = render_hub(hub, form_html)
    pages["/blog/"] = render_blog_index()
    pages["/a-propos/notre-equipe/"] = render_team()
    for a in ARTICLES:
        pages[a["path"]] = render_article(a)

    for path, content in pages.items():
        write("/index.html" if path == "/" else path, content)
    write("/404.html", render_404())

    urls = [("/", "monthly", "1.0")]
    prio = {"audit-gratuit": "0.8"}
    urls += [(f"/{h['slug']}/", "monthly", prio.get(h["slug"], "0.7" if h.get("group") == "villes" else "0.9")) for h in HUBS]
    urls += [("/a-propos/notre-equipe/", "monthly", "0.6")]
    urls += [("/blog/", "weekly", "0.7")] + [(a["path"], "monthly", "0.6") for a in ARTICLES]
    write("/sitemap.xml", sitemap(urls))

    coverage(pages)
    print(f"\n{len(pages)} pages + 404 + sitemap ({len(urls)} URL).")


STOPWORDS = {"de", "des", "du", "la", "le", "les", "d", "l", "et", "a", "un", "une", "pour", "en", "sa", "son", "ses", "au", "aux"}


def coverage(pages):
    """Contrôle que chaque requête du plan est couverte par sa page cible.

    exacte  : l'expression apparaît telle quelle ;
    mots    : tous les mots significatifs sont dans la page, mais pas l'expression exacte
              (normal : les requêtes sont écrites en « mots-clés », pas en phrases) ;
    lacune  : au moins un mot significatif manque → à corriger dans le contenu.
    """
    total = exact = words_only = 0
    gaps, missing_page = [], []
    for path, rows in QUERIES.items():
        if path not in pages:
            missing_page.append(path)
            continue
        text = norm(strip_tags(re.sub(r"<(script|style)[^>]*>.*?</>", " ", pages[path], flags=re.S)))
        vocab = set(text.split())
        for prio, q, _ in rows:
            total += 1
            nq = norm(q)
            if nq in text:
                exact += 1
                continue
            miss = [w for w in nq.split() if w not in STOPWORDS and w not in vocab]
            if miss:
                gaps.append((path, q, miss))
            else:
                words_only += 1
    print(f"Couverture des {total} requêtes : {exact} exactes, {words_only} par les mots, {len(gaps)} lacunes.")
    for path in missing_page:
        print(f"  ! page cible absente : {path}")
    for path, q, miss in gaps:
        print(f"  LACUNE {path:44s} « {q} »  mots absents : {', '.join(miss)}")


if __name__ == "__main__":
    main()
