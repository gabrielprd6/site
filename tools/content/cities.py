"""Pages locales : une page par ville (/automatisation-pme-<ville>/) + index /zones-intervention/.

Chaque ville a son propre texte (contexte économique, priorités, lignes par secteur, deux questions).
Le gabarit est commun, le contenu ne l'est pas : une page de ville qui ne change que le nom de la
ville est du contenu dupliqué, que Google déclasse. Ne dupliquez pas un paragraphe d'une ville à l'autre.

Faits locaux : volontairement généraux et stables (pas de chiffres, pas de noms d'entreprises).
Croisia travaille à distance : on ne revendique aucune agence locale.
"""

SOLUTION_SLUGS = ["automatisation-pme", "ia-pour-pme", "agents-ia", "automatisation-make-n8n", "visibilite-web"]

REMOTE = ("L'audit gratuit, la mise en place et le suivi se font en visio, ce qui suffit dans la grande majorité des cas. "
          "Un rendez-vous sur place peut être étudié selon le projet.")

CITIES = [
    {
        "slug": "toulouse", "name": "Toulouse", "priority": "Haute",
        "context": "Toulouse est un pôle majeur de l'aéronautique et du spatial, entouré d'un tissu dense de sous-traitants, "
                   "de bureaux d'études et de PME de services. C'est aussi la ville de l'ENAC, l'école où nous étudions : "
                   "nous connaissons ce tissu économique de l'intérieur. Beaucoup de ces entreprises vivent avec des exigences "
                   "de traçabilité et de documentation qui se prêtent bien à l'automatisation.",
        "priorities": ["Suivi des devis et des commandes chez les sous-traitants et bureaux d'études",
                       "Classement et circulation des documents techniques et qualité",
                       "Relances clients et facturation dans les PME de services",
                       "Reporting d'activité sans ressaisie"],
        "sectors": {
            "recrutement": "De nombreux cabinets recrutent des ingénieurs et des techniciens : relances candidats, base de profils interrogeable, comptes rendus d'entretien.",
            "auto": "Pour les concessionnaires de l'agglomération, le sourcing d'occasion et la qualification des demandes libèrent du temps de vente.",
            "immo": "Un marché porté par l'attractivité de la métropole : veille des annonces, qualification des acquéreurs et relances.",
        },
        "faq": [("Intervenez-vous en personne à Toulouse ?",
                 "L'audit se fait en visio, ce qui suffit dans la plupart des cas. Un rendez-vous sur place à Toulouse peut être étudié selon le projet."),
                ("Pouvez-vous travailler avec des entreprises de l'aéronautique ?",
                 "Nous venons de l'aviation civile et connaissons ses exigences de rigueur et de traçabilité. Les automatisations sont documentées et contrôlées ; "
                 "pour des données sensibles, on privilégie un hébergement maîtrisé, par exemple l'auto-hébergement avec n8n.")],
        "nearby": ["bordeaux", "montpellier", "marseille"],
    },
    {
        "slug": "paris", "name": "Paris", "priority": "Moyenne",
        "context": "Paris et l'Île-de-France concentrent sièges sociaux, cabinets de conseil et de recrutement, agences immobilières "
                   "et un très grand nombre de PME de services. La concurrence y est forte et les équipes sont sollicitées de toutes parts : "
                   "répondre vite et ne rien laisser tomber fait la différence.",
        "priorities": ["Réponse immédiate et qualification des demandes entrantes",
                       "Relances clients et suivi des paiements",
                       "Mise à jour automatique du CRM",
                       "Reporting hebdomadaire pour la direction"],
        "sectors": {
            "recrutement": "La plus forte densité de cabinets de France : relances candidats, double saisie ATS, prospection de clients.",
            "auto": "Pour les concessions et marchands d'Île-de-France : veille d'annonces, qualification des leads, relances.",
            "immo": "Un marché très concurrentiel, où la réactivité compte : veille des annonces, qualification des contacts, suivi des mandats.",
        },
        "faq": [("Travaillez-vous avec des entreprises parisiennes à distance ?",
                 "Oui. L'audit et le suivi se font en visio, ce qui est courant à Paris. Une rencontre sur place peut être étudiée selon le projet."),
                ("Quelles entreprises d'Île-de-France accompagnez-vous ?",
                 "Principalement des PME, dès qu'une personne répète les mêmes tâches chaque semaine. Le point idéal se situe entre 5 et 100 salariés.")],
        "nearby": ["lille", "nantes", "lyon"],
    },
    {
        "slug": "lyon", "name": "Lyon", "priority": "Moyenne",
        "context": "Lyon et sa métropole réunissent industrie, santé, numérique, logistique et services, avec un tissu de PME très diversifié. "
                   "Cette diversité est un atout : chaque entreprise a ses propres outils, et l'enjeu est de les faire communiquer plutôt que d'en changer.",
        "priorities": ["Liaison entre outils métier, CRM et facturation",
                       "Suivi des commandes et des délais",
                       "Relances clients et recouvrement",
                       "Tableaux de bord alimentés automatiquement"],
        "sectors": {
            "recrutement": "Des cabinets souvent spécialisés (industrie, santé, tech) : base de candidats interrogeable, relances, comptes rendus.",
            "auto": "Pour les concessions de la métropole : sourcing d'occasion, qualification des leads, relances après essai.",
            "immo": "Agences et chasseurs : veille d'annonces par mandat, qualification des contacts, estimation assistée.",
        },
        "faq": [("Pouvez-vous nous aider si nos outils sont très variés ?",
                 "C'est le cas le plus fréquent. On relie vos outils existants via leurs API ou des échanges de fichiers, sans les remplacer."),
                ("Faut-il être sur place pour démarrer ?",
                 "Non. L'audit se fait en visio et la mise en place à distance ; un rendez-vous à Lyon peut être étudié selon le projet.")],
        "nearby": ["paris", "marseille", "strasbourg"],
    },
    {
        "slug": "marseille", "name": "Marseille", "priority": "Moyenne",
        "context": "Marseille et la région Provence-Alpes-Côte d'Azur s'appuient sur le port, la logistique, le commerce, le tourisme "
                   "et un marché immobilier actif. Beaucoup d'entreprises y sont de petite taille et débordées par l'administratif : "
                   "c'est précisément là que l'automatisation rend du temps.",
        "priorities": ["Devis, bons de commande et facturation",
                       "Relances clients et suivi des paiements",
                       "Gestion des demandes entrantes (téléphone, mail, formulaire)",
                       "Notifications et suivi de dossiers"],
        "sectors": {
            "recrutement": "Cabinets et intermédiaires : relances candidats, planification d'entretiens, facturation des placements.",
            "auto": "Concessions et marchands : veille d'annonces d'occasion, qualification des demandes, relances clients.",
            "immo": "Un marché actif : veille d'annonces, qualification des acquéreurs et des vendeurs, relances.",
        },
        "faq": [("Accompagnez-vous les petites entreprises à Marseille ?",
                 "Oui. Une seule automatisation bien choisie suffit souvent pour commencer ; on la chiffre avant tout engagement."),
                ("L'audit est-il gratuit pour une entreprise marseillaise ?",
                 "Oui, partout en France : 30 minutes en visio, sans engagement.")],
        "nearby": ["nice", "montpellier", "lyon"],
    },
    {
        "slug": "bordeaux", "name": "Bordeaux", "priority": "Moyenne",
        "context": "Bordeaux et sa métropole combinent négoce et viticulture, aéronautique et défense, numérique, tourisme et forte attractivité résidentielle. "
                   "Le négoce comme les services reposent sur des relations clients à entretenir et des documents à produire : "
                   "deux terrains favorables à l'automatisation.",
        "priorities": ["Suivi des commandes et des relations clients",
                       "Génération de devis et de documents",
                       "Relances et suivi des paiements",
                       "Veille et reporting commercial"],
        "sectors": {
            "recrutement": "Cabinets de la métropole : relances candidats, base de profils interrogeable, planification des entretiens.",
            "auto": "Concessions et marchands : qualification des leads, relances après essai, sourcing d'occasion.",
            "immo": "Un marché attractif où les contacts affluent : veille d'annonces, qualification, relances.",
        },
        "faq": [("Pouvez-vous intervenir pour une entreprise de négoce ou de services à Bordeaux ?",
                 "Oui. Les tâches répétitives (devis, relances, suivi de commandes, reporting) se retrouvent dans la plupart des secteurs ; l'audit gratuit sert à repérer les plus rentables."),
                ("Intervenez-vous sur place à Bordeaux ?", REMOTE)],
        "nearby": ["toulouse", "nantes", "paris"],
    },
    {
        "slug": "nantes", "name": "Nantes", "priority": "Moyenne",
        "context": "Nantes est un territoire dynamique, avec un écosystème numérique actif, de l'industrie (naval, aéronautique) et de nombreux services. "
                   "Les équipes y sont souvent à l'aise avec les outils en ligne, ce qui facilite l'adoption : on part de ce qui existe et on fait communiquer les outils.",
        "priorities": ["Intégration entre les outils en ligne déjà en place",
                       "Qualification et routage des demandes entrantes",
                       "Reporting automatique",
                       "Automatisations internes : accueil, validations, notifications"],
        "sectors": {
            "recrutement": "Cabinets spécialisés tech et industrie : fin de la double saisie ATS, relances candidats, comptes rendus.",
            "auto": "Pour les concessions de l'agglomération : suivi des leads, relances clients, CRM à jour.",
            "immo": "Agences et chasseurs : veille d'annonces, qualification des contacts, rédaction assistée.",
        },
        "faq": [("Notre équipe utilise déjà beaucoup d'outils en ligne : est-ce un avantage ?",
                 "Oui. Plus vos outils exposent d'API ou d'intégrations, plus on peut les relier simplement avec Make ou n8n."),
                ("Intervenez-vous sur place à Nantes ?", REMOTE)],
        "nearby": ["bordeaux", "paris", "lyon"],
    },
    {
        "slug": "lille", "name": "Lille", "priority": "Moyenne",
        "context": "Lille et les Hauts-de-France sont un carrefour de la distribution, du commerce en ligne, de la logistique et des services, au contact de la Belgique. "
                   "Ces activités génèrent un grand volume de commandes, de demandes et de relances : c'est un terrain idéal pour automatiser le répétitif.",
        "priorities": ["Traitement des commandes et des demandes clients",
                       "Suivi des livraisons et notifications",
                       "Relances et facturation",
                       "Synchronisation entre outils de vente et de gestion"],
        "sectors": {
            "recrutement": "Cabinets de la métropole : relances candidats, planification d'entretiens, facturation des placements.",
            "auto": "Concessions et marchands : veille d'annonces d'occasion, qualification des leads, relances.",
            "immo": "Agences de la métropole : veille d'annonces, qualification des acquéreurs, suivi des vendeurs.",
        },
        "faq": [("Pouvez-vous gérer un gros volume de demandes ou de commandes ?",
                 "Oui, c'est justement là que l'automatisation rapporte le plus. On dimensionne les scénarios selon le volume, et on prévoit des alertes en cas d'anomalie."),
                ("Intervenez-vous sur place à Lille ?", REMOTE)],
        "nearby": ["paris", "strasbourg", "nantes"],
    },
    {
        "slug": "nice", "name": "Nice", "priority": "Moyenne",
        "context": "Nice et la Côte d'Azur vivent du tourisme, des services haut de gamme, de l'immobilier et, à proximité, du pôle technologique de Sophia Antipolis. "
                   "Une clientèle exigeante, souvent internationale, attend des réponses rapides et soignées : l'automatisation y sert avant tout la réactivité.",
        "priorities": ["Réponse immédiate aux demandes, y compris hors horaires",
                       "Premiers messages en plusieurs langues, relus par vos équipes",
                       "Suivi de la relation client et relances",
                       "Gestion des réservations ou des rendez-vous"],
        "sectors": {
            "recrutement": "Cabinets de la Côte d'Azur : relances candidats, planification d'entretiens, prospection de clients.",
            "auto": "Concessions et marchands : qualification des leads, relances, veille d'annonces.",
            "immo": "Un marché où la rapidité de réponse compte : qualification des contacts, relances, rédaction d'annonces assistée.",
        },
        "faq": [("L'IA peut-elle répondre à des clients étrangers ?",
                 "Elle peut préparer des premières réponses dans plusieurs langues. Votre équipe relit ce qui engage l'entreprise avant l'envoi."),
                ("Intervenez-vous sur place à Nice ?", REMOTE)],
        "nearby": ["marseille", "montpellier", "lyon"],
    },
    {
        "slug": "montpellier", "name": "Montpellier", "priority": "Moyenne",
        "context": "Montpellier est une métropole jeune et en croissance, avec un écosystème numérique et santé actif, de grandes universités et un marché immobilier dynamique. "
                   "Beaucoup de petites structures y grandissent vite, et l'administratif devient le goulot d'étranglement : on le traite avant qu'il ne freine la croissance.",
        "priorities": ["Structurer les processus d'une entreprise en croissance",
                       "Automatiser l'accueil et le suivi des clients",
                       "Facturation et relances",
                       "Tableaux de bord de pilotage"],
        "sectors": {
            "recrutement": "Cabinets en croissance : double saisie ATS, relances candidats, comptes rendus d'entretien.",
            "auto": "Concessions et marchands : leads, relances, CRM automatisé.",
            "immo": "Un marché dynamique : veille d'annonces, qualification des contacts, aide à l'estimation.",
        },
        "faq": [("Quand faut-il automatiser, pour une entreprise qui grandit vite ?",
                 "Dès que les mêmes tâches reviennent chaque semaine. Automatiser tôt évite de recruter pour de l'administratif et garde les process propres."),
                ("Intervenez-vous sur place à Montpellier ?", REMOTE)],
        "nearby": ["toulouse", "marseille", "nice"],
    },
    {
        "slug": "strasbourg", "name": "Strasbourg", "priority": "Moyenne",
        "context": "Strasbourg combine institutions européennes, industrie et commerce transfrontalier avec l'Allemagne. "
                   "Les entreprises y manipulent souvent plusieurs langues et des documents variés : l'IA et l'automatisation aident à les traiter et à les classer sans y passer des heures.",
        "priorities": ["Traitement de documents en plusieurs langues",
                       "Classement et extraction d'informations",
                       "Relances et suivi clients",
                       "Reporting pour la direction"],
        "sectors": {
            "recrutement": "Cabinets de la région : relances candidats, base de profils interrogeable, planification d'entretiens.",
            "auto": "Concessions et marchands : sourcing d'occasion, leads, relances clients.",
            "immo": "Agences et chasseurs : veille d'annonces, qualification des contacts, suivi des mandats.",
        },
        "faq": [("L'IA sait-elle traiter des documents en allemand ?",
                 "Les modèles actuels lisent et résument bien plusieurs langues. On teste sur vos documents réels avant toute mise en service, et un humain valide ce qui compte."),
                ("Intervenez-vous sur place à Strasbourg ?", REMOTE)],
        "nearby": ["lyon", "lille", "paris"],
    },
]

# Textes propres à chaque ville pour les deux autres services (IA pour PME, agent IA).
LOCAL = {
    "toulouse": {
        "ia": ("Dans un tissu de bureaux d'études et de sous-traitants, l'IA sert d'abord à retrouver et à lire : documents techniques, comptes rendus, cahiers des charges. Une IA bien cadrée répond à partir de vos propres documents, avec la source indiquée.",
               ["Recherche dans vos documents techniques et qualité", "Résumé de comptes rendus et de cahiers des charges", "Extraction de données de devis et de commandes"]),
        "agents": ("À Toulouse, un agent IA absorbe le flux de demandes que les équipes techniques n'ont pas le temps de traiter : demandes de devis, questions de suivi, relances. Il qualifie, répond au simple et passe la main à un humain pour le reste.",
                   ["Qualification des demandes de devis", "Réponse aux questions de suivi de commande", "Escalade vers l'expert concerné"]),
    },
    "paris": {
        "ia": ("À Paris, la sollicitation permanente est le vrai problème : emails, appels, messages. L'IA aide à trier, à résumer et à préparer des premières réponses, pour que les équipes traitent d'abord ce qui compte.",
               ["Tri et résumé des emails entrants", "Premières réponses relues avant envoi", "Synthèse de réunions et d'appels"]),
        "agents": ("Sur un marché où le client compare vite, un agent IA répond en quelques secondes, à toute heure, et qualifie la demande avant de la transmettre au bon interlocuteur.",
                   ["Réponse immédiate aux demandes entrantes", "Qualification : budget, urgence, besoin", "Transmission avec une fiche déjà remplie"]),
    },
    "lyon": {
        "ia": ("Avec des outils très variés d'une entreprise à l'autre, l'IA est utile là où les données ne sont pas structurées : documents scannés, emails libres, notes. Elle les lit et les transforme en données exploitables par vos outils existants.",
               ["Extraction de données de documents et de factures", "Classement automatique des emails", "Résumés de dossiers pour les équipes commerciales"]),
        "agents": ("Un agent IA peut servir de point d'entrée commun à plusieurs outils : il reçoit la demande, consulte le CRM, la facturation ou le stock, puis répond ou crée la bonne tâche.",
                   ["Consultation de plusieurs outils pour répondre", "Création de tâches dans le bon logiciel", "Suivi des demandes jusqu'à leur clôture"]),
    },
    "marseille": {
        "ia": ("Pour les petites structures débordées, l'IA doit rester simple : rédiger un premier jet de devis ou de réponse, résumer un échange, trier le courrier. Pas de projet lourd, un usage à la fois.",
               ["Premier jet de devis et de réponses", "Tri du courrier et des demandes", "Résumé des échanges avec un client"]),
        "agents": ("Un agent IA tient le standard numérique : il répond aux demandes de renseignements, prend les coordonnées et fixe un rendez-vous, pendant que l'équipe est sur le terrain.",
                   ["Réponse aux demandes de renseignements", "Prise de coordonnées et de rendez-vous", "Relais vers un humain pour les cas particuliers"]),
    },
    "bordeaux": {
        "ia": ("Dans le négoce et les services, l'IA aide à gérer la relation client à grande échelle sans la déshumaniser : personnaliser un message, résumer l'historique d'un client avant un appel, préparer une proposition.",
               ["Résumé de l'historique d'un client avant un appel", "Messages personnalisés relus par vos équipes", "Préparation de propositions à partir de vos modèles"]),
        "agents": ("Un agent IA peut répondre aux questions courantes des clients et des partenaires (disponibilités, délais, état d'une commande) à partir de vos données, et alerter votre équipe dès qu'une demande sort du cadre.",
                   ["Réponses sur les disponibilités et les délais", "Suivi de l'état d'une commande", "Alerte de l'équipe en cas d'exception"]),
    },
    "nantes": {
        "ia": ("Les équipes nantaises, déjà à l'aise avec les outils en ligne, peuvent aller vite : brancher des modèles d'IA sur les outils existants pour résumer, classer, rédiger, sans changer de logiciel.",
               ["IA branchée sur vos outils en ligne existants", "Classement et résumé automatiques", "Rédaction assistée de réponses et de contenus"]),
        "agents": ("Un agent IA s'intègre à une pile d'outils déjà en place : il lit un formulaire, enrichit une fiche, prévient l'équipe sur la messagerie et propose une réponse.",
                   ["Lecture de formulaires et enrichissement de fiches", "Notification sur votre messagerie d'équipe", "Réponse proposée pour validation"]),
    },
    "lille": {
        "ia": ("Quand le volume de commandes et de demandes est élevé, l'IA absorbe la variabilité : emails libres, pièces jointes, messages mal formulés. Elle les comprend et les range avant qu'ils ne saturent l'équipe.",
               ["Compréhension des demandes mal formulées", "Lecture de pièces jointes et de bons de commande", "Priorisation des urgences"]),
        "agents": ("Un agent IA traite en première ligne les questions répétitives sur les commandes et les livraisons, et ne remonte à l'équipe que les cas où une décision est nécessaire.",
                   ["Réponses sur les commandes et les livraisons", "Détection des retards à signaler", "Remontée des seuls cas à décision"]),
    },
    "nice": {
        "ia": ("Face à une clientèle internationale, l'IA prépare des premières réponses dans plusieurs langues et résume chaque demande en une ligne. Vos équipes relisent, ajustent le ton, et gardent la relation.",
               ["Premières réponses multilingues relues", "Résumé des demandes en une ligne", "Adaptation du ton à la clientèle"]),
        "agents": ("Un agent IA répond à toute heure, y compris le week-end et en haute saison, qualifie la demande et propose un créneau ou un rendez-vous, sans que personne n'ait à décrocher.",
                   ["Réponse à toute heure, y compris en saison", "Qualification et proposition de créneaux", "Transmission des demandes importantes"]),
    },
    "montpellier": {
        "ia": ("Pour une entreprise qui grandit vite, l'IA évite d'embaucher pour de l'administratif : saisie de données, tri, premiers brouillons. On l'introduit sur les tâches qui reviennent chaque semaine.",
               ["Saisie et extraction de données", "Brouillons de documents et de réponses", "Tri des demandes entrantes"]),
        "agents": ("Un agent IA devient le premier contact d'une structure en croissance : il accueille, renseigne, qualifie, et laisse l'équipe se concentrer sur le développement.",
                   ["Accueil et renseignement des prospects", "Qualification des demandes", "Passage de relais à l'équipe commerciale"]),
    },
    "strasbourg": {
        "ia": ("Avec des documents et des échanges en plusieurs langues, l'IA traduit, résume et classe. Elle aide aussi à retrouver un passage précis dans un contrat ou une notice, quelle que soit sa langue.",
               ["Résumé et traduction de documents", "Recherche d'un passage dans vos contrats et notices", "Classement automatique par type de document"]),
        "agents": ("Un agent IA peut répondre dans la langue du client, à partir de vos documents, et passer la main à un collaborateur dès que la demande exige de l'expertise.",
                   ["Réponse dans la langue du client", "Réponses fondées sur vos documents", "Passage de relais vers un expert"]),
    },
}


def _city_hub(c):
    name = c["name"]
    page = f"automatisation-pme-{c['slug']}"
    sectors = c["sectors"]
    ia_text, ia_bullets = LOCAL[c["slug"]]["ia"]
    ag_text, ag_bullets = LOCAL[c["slug"]]["agents"]
    return {
        "slug": page,
        "group": "villes",
        "city": c["slug"],
        "photo": f"/assets/img/villes/{c['slug']}.webp",
        "photo_alt": f"Vue de {name}",
        "parent": ("Automatisation PME", "/automatisation-pme/"),
        "nav_label": name,
        "nav_desc": f"Automatisation et IA pour PME à {name}",
        "card_title": f"Automatisation PME à {name}",
        "card_text": f"Agence d'automatisation et d'IA pour les PME de {name} : audit gratuit en visio.",
        "service_type": f"Automatisation et IA pour PME à {name}",
        "title": f"Automatisation PME à {name} : agence IA | Croisia",
        "description": f"Agence d'automatisation et d'IA pour PME à {name} : automatisations Make et n8n, agents IA, audit gratuit en visio. Consultants à votre écoute.",
        "eyebrow": f"Automatisation et IA à {name}",
        "h1": f"Automatisation PME à {name} : agence IA et consultants",
        "lede": f"Croisia est une agence d'automatisation et d'IA qui accompagne les PME de {name}. Nos consultants en automatisation "
                f"relient vos outils, déploient l'IA là où elle sert et mettent en place des agents IA, pour que vos équipes gagnent du temps.",
        "points": ["Audit gratuit en visio", "Vos outils actuels conservés", "Chiffrage chantier par chantier"],
        "blocks": [
            {"type": "split", "id": "automatisation", "eyebrow": "Automatisation PME", "title": f"Automatisation PME à {name}",
             "md": c["context"] + "\n\nLe détail de la méthode est sur notre page [automatisation pour PME](/automatisation-pme/) ; "
                   "pour les plateformes, voir nos [experts Make et n8n](/automatisation-make-n8n/).",
             "bullets": c["priorities"], "meta": "Ce qu'on automatise en priorité"},
            {"type": "split", "id": "ia-pour-pme", "tint": True, "reverse": True, "eyebrow": "IA pour PME", "title": f"IA pour PME à {name}",
             "md": ia_text + "\n\nDes cas d'usage concrets sont décrits sur la page [IA pour PME](/ia-pour-pme/).",
             "bullets": ia_bullets},
            {"type": "split", "id": "agents-ia", "eyebrow": "Agents IA", "title": f"Agent IA à {name}",
             "md": ag_text + "\n\nVoir aussi nos [agents IA](/agents-ia/) : périmètre, garde-fous et déploiement.",
             "bullets": ag_bullets},
            {"type": "cards", "tint": True, "eyebrow": "Secteurs", "title": f"Recrutement, automobile, immobilier à {name}",
             "items": [
                 {"title": "Cabinets de recrutement", "text": sectors["recrutement"], "href": "/recrutement/"},
                 {"title": "Concessions automobiles", "text": sectors["auto"], "href": "/concessions-automobiles/"},
                 {"title": "Agences immobilières", "text": sectors["immo"], "href": "/immobilier/"},
             ]},
            {"type": "split", "eyebrow": "Mode de travail", "title": f"Comment nous travaillons avec les entreprises de {name}",
             "md": f"Faire appel à un consultant en automatisation à {name}, c'est avoir un interlocuteur qui parle métier avant de parler outils. " + REMOTE
                   + "\n\nVous parlez directement aux deux ingénieurs qui construisent, de l'audit au suivi. Voir [l'audit gratuit](/audit-gratuit/).",
             "bullets": ["30 minutes en visio, sans préparation", "Une liste priorisée de ce qui peut être automatisé", "Un devis sur mesure, chantier par chantier", "Aucun engagement"]},
            {"type": "steps", "tint": True},
            {"type": "links", "eyebrow": "Autres villes", "title": "Nous accompagnons aussi les PME de",
             "slugs": [f"automatisation-pme-{s}" for s in c["nearby"]]},
            {"type": "faq", "tint": True, "title": f"Questions sur l'automatisation à {name}"},
        ],
        "faq": c["faq"] + [
            (f"L'audit est-il gratuit pour une entreprise de {name} ?",
             "Oui. L'audit dure 30 minutes, il est gratuit et sans engagement. Il débouche sur une liste priorisée de ce qui peut être automatisé."),
            ("Faut-il changer nos outils ?",
             "Non. On fait communiquer ceux que vous utilisez déjà, et on ne remplace un logiciel que s'il vous bloque vraiment."),
        ],
    }


CITY_HUBS = [_city_hub(c) for c in CITIES]
