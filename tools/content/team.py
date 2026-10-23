"""Page « Notre équipe » (/a-propos/notre-equipe/).

Mise en page calquée sur la page équivalente d'un autre site (fil d'Ariane, hero photo, chiffres clés,
grille d'équipe, avis, galerie, panneaux « rejoindre l'aventure », liste des expertises).
Contenu : uniquement des faits vrais pour Croisia. Rien n'est repris du site qui a servi de modèle.

Pour ajouter quelqu'un : une entrée dans MEMBERS + sa photo (4:5, 800x1000) dans assets/img/team/.
Pour ajouter un profil LinkedIn : champ "linkedin": "https://www.linkedin.com/in/…" (l'icône apparaît).
"""

TITLE = "Notre équipe | Croisia"
DESCRIPTION = ("Rencontrez l'équipe Croisia : Gabriel et Oscar, ingénieurs de l'ENAC, spécialistes de l'automatisation et des agents IA pour PME.")

HERO = {
    "image": "/assets/img/equipe-croisia.jpg",
    "alt": "Gabriel et Oscar, fondateurs de Croisia, en réunion de travail",
    "tagline": "Deux ingénieurs qui connaissent votre quotidien d'entreprise avant de parler d'outils.",
}

STATS = [
    ("2", "ingénieurs fondateurs"),
    ("3", "expertises : automatisation, agents IA, visibilité web"),
    ("30 min", "d'audit gratuit pour démarrer"),
    ("24 h", "pour vous répondre"),
]

MEMBERS = [
    {"name": "Gabriel Praud", "role": "Cofondateur · Automatisations & intégrations",
     "photo": "/assets/img/team/gabriel.jpg"},
    {"name": "Oscar Javelle", "role": "Cofondateur · Agents IA & traitement de données",
     "photo": "/assets/img/team/oscar.jpg"},
]

TESTIMONIAL = {
    "text": "Une refonte de notre site et un vrai travail sur le référencement naturel : nous sommes passés d'environ 60 à près de 150 pages positionnées sur Google, "
            "et nous avons atteint la 2ᵉ place sur notre requête la plus stratégique. Professionnel, autonome et impliqué : une collaboration que je recommande volontiers.",
    "name": "Pierre-Emmanuel Saliou", "role": "Dirigeant · Skaelia", "photo": "/assets/img/pe-saliou.jpg",
}

# Section « La vie chez Croisia » : masquée tant que la liste est vide.
# Ajoutez 3 ou 4 vraies photos (bureau, travail en équipe, rencontres clients, événements) :
#   ("/assets/img/vie/atelier.jpg", "Légende courte", 1600, 1200),
GALLERY = []

JOIN = [
    {"title": "Vous dirigez une PME ?",
     "text": "Dites-nous quelle tâche vous coûte le plus de temps. En 30 minutes de visio, on repère ce qui peut être automatisé, sans engagement.",
     "buttons": [("Demander mon audit gratuit", "/audit-gratuit/", True), ("Nous écrire", "mailto:contact@croisia.com", False)]},
    {"title": "Vous êtes dans le recrutement, l'automobile ou l'immobilier ?",
     "text": "Nous connaissons les outils et les tâches répétitives de ces trois métiers. Découvrez ce qu'on met en place pour le vôtre.",
     "buttons": [("Cabinets de recrutement", "/recrutement/", True), ("Concessions auto", "/concessions-automobiles/", False), ("Immobilier", "/immobilier/", False)]},
]

EXPERTISES = [
    ("Automatisation PME", "/automatisation-pme/"),
    ("IA pour PME", "/ia-pour-pme/"),
    ("Agents IA", "/agents-ia/"),
    ("Experts Make et n8n", "/automatisation-make-n8n/"),
    ("Visibilité web et SEO", "/visibilite-web/"),
]
