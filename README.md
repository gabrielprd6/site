# Site vitrine Altiora

Site one-page en HTML / CSS / JS, sans build ni dépendance à installer.
Ouvrez `index.html` ou déposez le dossier chez n'importe quel hébergeur statique.

```
index.html
assets/
  css/styles.css
  js/main.js
```

Seules dépendances externes : Google Fonts (Space Grotesk + DM Sans) et GSAP via CDN.
Si le CDN GSAP est bloqué, un fallback `IntersectionObserver` prend le relais et le
contenu reste entièrement visible.

## Lancer en local

```bash
python -m http.server 4321
# puis http://127.0.0.1:4321/index.html
```

---

## Ce qu'il reste à renseigner

Chaque point ci-dessous est un placeholder volontaire, repérable dans le code.

| Quoi | Où | Comment |
|---|---|---|
| Endpoint du formulaire | `index.html`, `<form id="audit-form" data-endpoint="">` | Voir « Brancher le formulaire » ci-dessous |
| Photo du portrait | `index.html`, section `#a-propos` | Commentaire HTML en place, remplacer le bloc `.about__photo` |
| Bio personnalisée | `index.html`, section `#a-propos` | Remplacer les 2 paragraphes + supprimer le bloc `.about__todo` |
| Chiffres réels | `index.html`, section `#resultats` | Attribut `data-to` de chaque `.counter` |
| Témoignage Skaelia | `index.html`, section `#temoignage` | Retirer la classe `is-placeholder` sur `<figure>` |
| Lien Calendly | `index.html`, `<a … data-calendly>` | Remplacer `href="#"` |
| Lien LinkedIn | `index.html`, `<a … data-linkedin>` | Remplacer `href="#"` |
| Email pro | `index.html`, footer + message d'erreur dans `main.js` | `contact@altiora.fr` par défaut |
| Mentions légales | `index.html`, `<a … data-legal>` | Remplacer `href="#"` |

Tant que `href="#"`, ces liens sont neutralisés en JS pour éviter un saut en haut de page.

### Brancher le formulaire

Sans `data-endpoint`, le site tourne en **mode démo** : la validation s'exécute, la
confirmation s'affiche, mais rien n'est envoyé (un message le rappelle dans la console).

Pour l'activer, renseignez une URL qui accepte un `POST` en `multipart/form-data`
et répond en 2xx — Formspree, Basin, Getform, un webhook Make ou n8n :

```html
<form class="form" id="audit-form" novalidate data-endpoint="https://formspree.io/f/VOTRE_ID">
```

Champs envoyés : `nom`, `email`, `entreprise`, `telephone`, `tache`.
Le champ `site` est un honeypot anti-spam : s'il est rempli, la soumission est
silencieusement ignorée.

---

## Design system

Tout est piloté par des variables CSS en haut de `styles.css` (bloc `:root` et
`[data-theme="dark"]`). Changer une couleur se fait à un seul endroit.

| Rôle | Clair | Usage |
|---|---|---|
| Primary | `#6D28D9` | liens, accents, icônes |
| Secondary | `#6366F1` | dégradés, éléments secondaires |
| Accent CTA | `#DB2777` | **uniquement** le bouton d'action |
| Foreground | `#0F172A` | texte |
| Background | `#FFFFFF` / `#FAF7FF` | fonds |

Deux écarts assumés par rapport au brief, tous deux pour tenir le contraste 4.5:1 :

- **CTA rose `#DB2777` au lieu de `#EC4899`.** Le rose du brief ne donne que 3.5:1
  avec du texte blanc. `#DB2777` donne 4.6:1. `#EC4899` reste utilisé comme
  couleur d'ambiance (`--accent-glow`) sur les orbes et les fonds.
- **Fin du dégradé du titre `#4F46E5` au lieu de `#6366F1`** (`--grad-end`).
  L'indigo du brief tombe à 4.4:1 sur blanc.

Typographie : Space Grotesk (titres) + DM Sans (corps), base 16px, interligne 1.5.

### Thème clair / sombre

Le thème est choisi dans cet ordre : préférence enregistrée (`localStorage`),
sinon `prefers-color-scheme`. Il est appliqué par un script inline dans le `<head>`
pour éviter le flash au chargement. Le bouton du header force un choix explicite ;
tant qu'aucun choix n'est fait, le site suit l'OS en direct.

---

## Animations

| Élément | Comportement |
|---|---|
| Hero | cascade titre → sous-titre → CTA → visuel (`expo.out`, 800ms) |
| Sections | fondu + translation 24px, déclenché à 85% du viewport, une seule fois |
| Mot du titre | frappe / effacement en boucle sur 3 formulations |
| Orbes | dérive lente en CSS + parallaxe légère au scroll |
| Cartes services | élévation + lueur suivant le curseur |
| Compteurs | 0 → valeur (easeOutCubic) à l'entrée dans l'écran |
| Mockup de flux | étapes qui s'allument en boucle, en pause hors écran et onglet inactif |

Seuls `opacity` et `transform` sont animés. L'accordéon FAQ utilise
`grid-template-rows: 0fr → 1fr`, la seule exception (une hauteur doit s'animer).

**`prefers-reduced-motion: reduce`** coupe tout : pas de cascade, pas de frappe,
pas de dérive d'orbes, compteurs affichés à leur valeur finale, scroll instantané.

---

## Accessibilité

Vérifié au rendu réel (Playwright) sur 375 / 768 / 1024 / 1440px, en clair et en sombre :

- aucun débordement horizontal
- aucune cible interactive sous 44×44px
- aucun texte sous le seuil AA (4.5:1, ou 3:1 pour le grand texte)
- aucune erreur console
- lien d'évitement en premier arrêt de tabulation
- contenu entièrement visible sans JavaScript et en `reduced-motion`

Autres points : `aria-expanded` sur la FAQ et le menu mobile, fermeture à `Échap`
avec retour du focus, erreurs de formulaire liées par `aria-describedby`,
confirmation annoncée via `role="status"`, icônes SVG en `aria-hidden`.

---

## Performance

Pas d'images pour l'instant : le poids vient des polices et de GSAP (~70 ko gzip).
Quand la photo et le logo Skaelia arriveront :

- exporter en WebP
- ajouter `loading="lazy"` et `decoding="async"`
- toujours renseigner `width` et `height` pour réserver la place (éviter le CLS)

Le conteneur `.about__photo` a déjà un `aspect-ratio: 4/5` : la place est réservée.

---

## SEO

Hors périmètre, conformément au brief. Le minimum est en place : `<title>`,
meta description, Open Graph, `lang="fr"`, hiérarchie de titres correcte
(un seul `<h1>`, sections en `<h2>`).
