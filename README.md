# Site Croisia (croisia.com)

Site statique, hébergé sur GitHub Pages. Les pages sont **générées** par un script Python
(bibliothèque standard uniquement) à partir de `tools/` ; le HTML généré est versionné, donc
rien à installer ni à compiler côté hébergement.

```bash
python tools/build.py        # régénère toutes les pages + sitemap.xml + 404.html
python tools/check_links.py  # vérifie liens internes, ancres et assets
python -m http.server 4321   # aperçu local : http://localhost:4321/
```

## Architecture

L'arborescence vient du plan de requêtes SEO (`tools/data/requetes.csv`, une ligne par requête
avec sa page cible). Chaque page cible existe ; le build vérifie à chaque exécution que les mots
de chaque requête figurent bien dans sa page.

```
/                              Accueil (marque, agence, consultants, avis)
├─ /automatisation-pme/        Pilier : automatiser son entreprise
├─ /ia-pour-pme/               Pilier : IA pour PME
├─ /agents-ia/                 Pilier : agents IA, chatbot, assistant, qualification de leads
├─ /automatisation-make-n8n/   Pilier : expert Make / n8n
├─ /visibilite-web/            Pilier : site vitrine, SEO, fiche Google
├─ /recrutement/               Secteur : cabinets de recrutement
├─ /concessions-automobiles/   Secteur : concessions auto
├─ /immobilier/                Secteur : agences, agents, chasseurs
├─ /audit-gratuit/             Conversion : audit + formulaire
└─ /blog/                      Index, puis /blog/<slug>/ (35 articles)
```

Maillage : chaque article remonte vers son pilier (encart + fil d'Ariane) ; chaque pilier liste
ses articles ; piliers et secteurs se renvoient entre eux ; le pied de page liste tous les piliers.
Chaque page se termine sur un appel vers `/audit-gratuit/`.

## Où modifier quoi

| Je veux… | Je modifie |
|---|---|
| Changer le texte d'un pilier, d'un secteur ou de l'audit | `tools/content/hubs.py` |
| Écrire ou corriger un article | `tools/content/blog/<slug>.md` |
| Ajouter un article | créer `tools/content/blog/<slug>.md` (modèle ci-dessous), puis `python tools/build.py` |
| Modifier la page d'accueil | `tools/templates/home.html` |
| Modifier le menu, le pied de page, les balises `<head>` | `tools/build.py` (fonctions `header`, `footer`, `head`) |
| Suivre les requêtes visées | `tools/data/requetes.csv` |
| Styles | `assets/css/styles.css` (accueil), `assets/css/pages.css` (autres pages) |

**Ne modifiez jamais `index.html` ni les dossiers générés à la main** : ils sont écrasés au prochain build.

### Modèle d'article

```markdown
---
title: Titre de l'article (sert aussi de H1 et de <title>)
description: Une phrase de 120 à 155 caractères (meta description).
segment: pme            # pme | recrutement | auto | immo
hub: /automatisation-pme/   # facultatif : pilier de rattachement (par défaut, celui du segment)
related: slug-a, slug-b     # facultatif : articles à lire aussi
---
Introduction.

## Un titre de section
Texte, **gras**, [lien interne](/audit-gratuit/), listes (`- `), listes numérotées (`1. `),
encart (`> texte`), tableau (`| a | b |`).
```

Apostrophes droites et espaces insécables (avant `: ; ? !`) sont corrigées automatiquement.
Le sommaire, le fil d'Ariane, les données structurées (BlogPosting, BreadcrumbList), l'encart
vers le pilier et les « à lire aussi » sont générés.

## SEO

- URL propres en dossier (`/slug/`), canonical en `https://croisia.com/slug/`.
- `sitemap.xml` généré (46 URL). `robots.txt` pointe dessus.
- Données structurées : ProfessionalService (accueil), Service (piliers), BlogPosting, BreadcrumbList.
- Un seul `<h1>` par page ; titres < 60 caractères et meta descriptions < 160 caractères.

## À renseigner

| Quoi | Où |
|---|---|
| Lien Calendly | `tools/templates/home.html`, lien `data-calendly` (encore `href="#"`) |
| Lien LinkedIn | à ajouter dans `footer()` de `tools/build.py` |
| Volumes, difficulté, positions | le tableur de suivi (non repris dans le dépôt) |

## Front

Charte : graphite + bleu électrique `#2346E0`, Source Serif 4 (titres) et Hanken Grotesk (texte).
Tout passe par les variables CSS de `:root` dans `styles.css`.

- **Accueil** : loader, GSAP + ScrollTrigger (CDN), `intro.js`, `main.js`, `motion.js`.
- **Autres pages** : `main.js` seul, sans GSAP (menus, FAQ, formulaire, révélations par
  `IntersectionObserver`). Tout le contenu reste lisible sans JavaScript et en `prefers-reduced-motion`.
- **Formulaire** : FormSubmit vers `contact@croisia.com`, présent sur l'accueil et sur `/audit-gratuit/`
  (même code, extrait du gabarit d'accueil entre `<!--FORM-->` et `<!--/FORM-->`).
- Pages légales (`mentions-legales.html`, `confidentialite.html`) : écrites à la main, feuille `legal.css`.
