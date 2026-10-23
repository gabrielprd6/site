"""Pages piliers du site (solutions, secteurs, audit).

Chaque entrée de HUBS devient /<slug>/. Les requêtes SEO visées par la page viennent
de tools/data/requetes.csv (colonne « Page cible ») : elles servent de contrôle de
couverture à chaque build, pas de texte à copier.

Texte : markdown en ligne accepté (**gras**, [lien](/url/)). Les apostrophes droites
et les espaces avant : ; ? ! sont corrigées automatiquement.
"""

HOME_LD = (
    '{"@context":"https://schema.org","@type":"ProfessionalService","name":"Croisia","url":"https://croisia.com/",'
    '"logo":"https://croisia.com/icon-192.png","image":"https://croisia.com/assets/img/og-image.png",'
    '"description":"Agence et consultants en automatisation et en IA pour PME : audit gratuit, automatisations Make et n8n, '
    'agents IA, création de sites web.","email":"contact@croisia.com","areaServed":{"@type":"Country","name":"France"},'
    '"knowsLanguage":"fr","founder":[{"@type":"Person","name":"Gabriel Praud"},{"@type":"Person","name":"Oscar Javelle"}],'
    '"serviceType":["Automatisation des processus","Agents IA","Création de sites web"]}'
)
HOME_HEAD_EXTRA = ""

FOOTER_ARTICLES = [
    "/blog/comment-automatiser-une-pme/",
    "/blog/exemples-automatisation-pme/",
    "/blog/make-vs-n8n-vs-zapier/",
    "/blog/prix-automatisation/",
]
HOME_ARTICLES = [
    "/blog/comment-automatiser-une-pme/",
    "/blog/exemples-automatisation-pme/",
    "/blog/make-vs-n8n-vs-zapier/",
]

SECTOR_STEPS = [
    ("Audit gratuit", "30 minutes en visio pour comprendre votre quotidien et repérer ce qui prend le plus de temps."),
    ("Devis sur mesure", "Un plan chiffré, chantier par chantier, avec le gain de temps estimé pour chacun."),
    ("Mise en place", "On branche vos outils actuels, on teste sur des cas réels, on forme vos équipes."),
    ("Suivi", "On mesure, on ajuste, et on ajoute les automatisations suivantes quand vous êtes prêts."),
]

HUBS = [
    # ====================================================================== SOLUTIONS
    {
        "slug": "automatisation-pme",
        "group": "solutions",
        "nav_label": "Automatisation PME",
        "nav_desc": "Fini la double saisie et les tâches répétitives",
        "card_title": "Automatisation pour PME",
        "card_text": "Devis, relances, reporting, CRM : vos outils reliés, vos tâches répétitives qui tournent seules.",
        "title": "Automatisation PME : automatiser son entreprise | Croisia",
        "description": "Automatisez les tâches répétitives de votre PME (devis, relances, reporting, CRM) sans changer vos outils. Audit gratuit de 30 minutes.",
        "eyebrow": "Automatisation pour PME",
        "h1": "Automatiser son entreprise, sans changer d'outils",
        "lede": "Croisia automatise les tâches répétitives de votre PME : devis, relances, facturation, reporting, CRM. "
                "On relie les logiciels que vous utilisez déjà, pour que votre équipe gagne du temps là où ça compte.",
        "points": ["Première automatisation en 1 à 2 semaines", "Vos outils actuels conservés", "Chiffrage chantier par chantier"],
        "blocks": [
            {"type": "pains", "eyebrow": "Le constat", "title": "Gagner du temps en entreprise : d'abord repérer où il part",
             "lede": "Ce n'est presque jamais un problème d'effort. C'est un problème d'outillage : les mêmes gestes, chaque semaine, à la main.",
             "items": [
                 ("La double saisie", "Un devis dans un tableur, la même info ressaisie dans le CRM, puis dans la facture. Chaque copie est une occasion d'erreur."),
                 ("Les relances oubliées", "Impayés, devis sans réponse, prospects à rappeler : tout dépend de la mémoire de quelqu'un."),
                 ("Le reporting du lundi matin", "Des chiffres rassemblés à la main dans trois fichiers, obsolètes dès qu'ils sont envoyés."),
                 ("Des outils qui ne se parlent pas", "Chaque logiciel fait bien son travail, mais personne ne fait le lien entre eux. Sauf vous."),
             ]},
            {"type": "cards", "tint": True, "eyebrow": "Ce qu'on automatise", "title": "Sept chantiers qui rapportent vite",
             "lede": "On commence par un chantier court et visible, pour que le gain soit mesurable avant d'aller plus loin.",
             "items": [
                 {"title": "Devis et factures", "text": "Pré-remplis depuis votre CRM, envoyés et archivés sans ressaisie.", "href": "/blog/automatiser-devis-factures/", "more": "Lire le guide"},
                 {"title": "Relances clients", "text": "Un scénario de relance poli et régulier, qui s'arrête dès que le client répond ou paie.", "href": "/blog/automatiser-relances-clients/", "more": "Lire le guide"},
                 {"title": "Reporting", "text": "Un tableau de bord alimenté automatiquement, livré chaque semaine.", "href": "/blog/automatiser-reporting/", "more": "Lire le guide"},
                 {"title": "Tâches administratives", "text": "Classement, saisie, notifications, validations : le travail de fond qui ne devrait pas vous occuper.", "href": "/blog/automatiser-taches-administratives/", "more": "Lire le guide"},
                 {"title": "Prospection commerciale", "text": "Sourcer, qualifier, relancer : les étapes répétitives passent en automatique.", "href": "/blog/automatiser-prospection/", "more": "Lire le guide"},
                 {"title": "CRM à jour", "text": "Chaque email, chaque appel, chaque devis remonte seul dans la bonne fiche.", "href": "/blog/automatisation-crm/", "more": "Lire le guide"},
                 {"title": "Emails de l'entreprise", "text": "Tri, accusés de réception, réponses types, transferts : la boîte mail qui se range seule.", "href": "/blog/automatisation-emails/", "more": "Lire le guide"},
             ]},
            {"type": "split", "eyebrow": "Logiciel ou intégration ?", "title": "Un logiciel d'automatisation pour PME, ou plutôt une couche qui relie vos logiciels ?",
             "md": "Dans la plupart des PME, il n'y a pas besoin d'un énième logiciel. Il y a besoin de **faire parler entre eux ceux qui existent déjà** : CRM, messagerie, facturation, tableurs, outils métier.\n\n"
                   "C'est l'intégration de logiciels d'entreprise par l'automatisation : des scénarios, construits avec des plateformes comme Make ou n8n, qui déplacent l'information d'un outil à l'autre au bon moment.\n\n"
                   "Vous gardez vos outils. On ne remplace un logiciel que s'il vous bloque vraiment, et jamais sans en avoir discuté. Pour comparer les plateformes, voir notre [comparatif Make, n8n et Zapier](/blog/make-vs-n8n-vs-zapier/).",
             "bullets": ["Pas de migration de données", "Vous restez propriétaire de vos automatisations", "Accès limités au strict nécessaire, révocables à tout moment", "Alertes en cas d'échec d'un scénario"],
             "meta": "Make · n8n · intégrations sur mesure"},
            {"type": "steps", "tint": True},
            {"type": "links", "title": "Aller plus loin dans l'automatisation", "slugs": ["automatisation-make-n8n", "agents-ia", "ia-pour-pme"]},
            {"type": "articles", "title": "Guides pour automatiser votre PME", "max": 9},
            {"type": "faq"},
        ],
        "faq": [
            ("Que peut-on automatiser dans une PME ?",
             "Tout ce qui est répétitif et suit des règles : création de devis et de factures, relances, mise à jour du CRM, reporting, tri des emails, saisie de données entre deux logiciels. Si une personne refait les mêmes gestes chaque semaine, c'est un candidat."),
            ("Faut-il changer tous mes outils ?",
             "Non, c'est même l'inverse. Le principe est de faire parler entre eux les outils que vous utilisez déjà. On ne remplace un logiciel que s'il vous bloque vraiment."),
            ("Combien de temps avant de voir un résultat ?",
             "La première automatisation tourne généralement en une à deux semaines après l'audit. On commence par un chantier court et visible, pour que le gain soit mesurable."),
            ("Combien ça coûte ?",
             "L'audit est gratuit. Ensuite, un devis sur mesure, chantier par chantier, avec le gain de temps estimé en face de chaque ligne. Voir [combien coûte l'automatisation d'une entreprise](/blog/prix-automatisation/)."),
            ("Mon entreprise est-elle trop petite ?",
             "À partir du moment où au moins une personne répète les mêmes tâches chaque semaine, c'est utile. Le point idéal se situe entre 5 et 100 salariés."),
        ],
    },
    {
        "slug": "ia-pour-pme",
        "group": "solutions",
        "nav_label": "IA pour PME",
        "nav_desc": "Des cas d'usage concrets, sans jargon",
        "card_title": "IA pour PME",
        "card_text": "L'intelligence artificielle appliquée à vos tâches : rédiger, trier, extraire, retrouver l'information.",
        "title": "IA pour PME : cas d'usage concrets | Croisia",
        "description": "L'intelligence artificielle pour PME : rédaction, tri d'emails, extraction de documents, recherche interne. Des cas d'usage concrets et mesurables.",
        "eyebrow": "Intelligence artificielle pour PME",
        "h1": "IA pour PME : des usages concrets, pas de la science-fiction",
        "lede": "L'intelligence artificielle pour PME n'a rien d'un projet de laboratoire. Bien employée, elle rédige vos premières réponses, "
                "trie vos emails, lit vos documents et retrouve l'information, pendant que votre équipe se concentre sur le travail qui demande du jugement.",
        "points": ["Cas d'usage choisis sur votre quotidien", "Un humain valide ce qui compte", "Données maîtrisées, RGPD pris en compte"],
        "blocks": [
            {"type": "cards", "eyebrow": "Cas d'usage", "title": "Six usages de l'IA qui font gagner du temps aux PME",
             "items": [
                 {"title": "Rédiger des premières réponses", "text": "Réponses aux demandes entrantes, relances, comptes rendus : l'IA propose, vous validez en dix secondes."},
                 {"title": "Trier et classer les emails", "text": "Demande de devis, réclamation, facture : chaque message est reconnu et envoyé au bon endroit."},
                 {"title": "Extraire les données des documents", "text": "Factures, bons de commande, CV : les informations utiles sont lues et saisies à votre place."},
                 {"title": "Retrouver l'information", "text": "Poser une question en langage naturel à vos propres documents et obtenir la réponse, avec sa source."},
                 {"title": "Résumer et compte-rendre", "text": "Appels, réunions, entretiens : un résumé structuré, prêt à être classé dans le bon dossier."},
                 {"title": "Qualifier les demandes", "text": "Budget, urgence, service concerné : chaque prospect est évalué avant d'arriver sur le bureau d'un commercial.", "href": "/agents-ia/", "more": "Voir les agents IA"},
             ]},
            {"type": "split", "tint": True, "eyebrow": "Choisir", "title": "Par quel cas d'usage commencer ?",
             "md": "Le bon premier projet d'IA n'est pas le plus impressionnant. C'est celui qui coche ces quatre cases :",
             "bullets": ["Une tâche **répétitive**, faite souvent", "Un **volume** suffisant pour que le gain se voie", "Un **résultat vérifiable** par une personne en quelques secondes", "Une **erreur** qui ne coûte pas cher si elle passe inaperçue"],
             "meta": "L'audit gratuit sert précisément à classer vos tâches selon ces critères."},
            {"type": "prose", "eyebrow": "Garde-fous", "title": "L'IA en entreprise : ce qu'on met en place pour que ça reste fiable",
             "md": "Une IA peut se tromper. On le sait, donc on conçoit autour de cette réalité :\n\n"
                   "- **L'humain valide** tout ce qui engage l'entreprise (devis, réponse sensible, décision).\n"
                   "- **Les réponses s'appuient sur vos documents**, avec la source indiquée, plutôt que sur la mémoire du modèle.\n"
                   "- **Les données personnelles sont minimisées** et les accès documentés. Voir notre guide sur [l'IA conforme au RGPD en entreprise](/blog/ia-rgpd-entreprise/).\n"
                   "- **Chaque automatisation est journalisée**, avec une alerte quand quelque chose sort de l'ordinaire.\n\n"
                   "Pour aller plus loin sur les assistants qui répondent et qualifient à votre place, voir nos [agents IA](/agents-ia/)."},
            {"type": "steps", "tint": True},
            {"type": "links", "slugs": ["agents-ia", "automatisation-pme", "automatisation-make-n8n"]},
            {"type": "faq"},
        ],
        "faq": [
            ("L'intelligence artificielle est-elle adaptée à une petite entreprise ?",
             "Oui, parce que les usages utiles sont modestes et ciblés : rédiger, trier, extraire, résumer. Pas besoin d'équipe de data scientists ni d'infrastructure lourde."),
            ("L'IA va-t-elle remplacer mes collaborateurs ?",
             "Elle prend en charge les gestes répétitifs pour laisser du temps au travail à valeur ajoutée : relation client, conseil, décision. Un humain reste dans la boucle pour ce qui compte."),
            ("Mes données sont-elles envoyées à un service américain ?",
             "Ça dépend des outils choisis, et on le décide avec vous. On privilégie des solutions qui n'entraînent pas leurs modèles sur vos données et, quand c'est possible, un hébergement en Europe."),
            ("Quelle différence entre automatisation et IA ?",
             "L'automatisation exécute des règles fixes (si ceci, alors cela). L'IA traite ce qui est flou : un email mal écrit, un document scanné, une demande ambiguë. Les deux se combinent très bien."),
        ],
    },
    {
        "slug": "agents-ia",
        "group": "solutions",
        "nav_label": "Agents IA",
        "nav_desc": "Des assistants qui répondent et qualifient",
        "card_title": "Agents IA",
        "card_text": "Des assistants qui répondent, qualifient vos leads et rédigent à votre place, même quand vous êtes débordé.",
        "title": "Agents IA pour PME et entreprises | Croisia",
        "description": "Agents IA sur mesure pour PME : réponse immédiate, qualification de leads, chatbot et assistant interne. Déploiement encadré, garde-fous et suivi.",
        "eyebrow": "Agents IA sur mesure",
        "h1": "Agents IA pour PME : répondre, qualifier et rédiger à votre place",
        "lede": "Un agent IA pour PME est un assistant qui accomplit une tâche de bout en bout : lire une demande, la comprendre, "
                "consulter vos données et répondre ou agir. Croisia conçoit des agents IA pour entreprise, cadrés, testés et suivis.",
        "points": ["Réponse immédiate aux demandes entrantes", "Escalade vers un humain quand il le faut", "Périmètre et règles définis avec vous"],
        "blocks": [
            {"type": "cards", "eyebrow": "Ce qu'un agent peut faire", "title": "Quatre agents qui rendent service dès les premières semaines",
             "cols": 2,
             "items": [
                 {"title": "Agent de qualification de leads", "text": "Il répond à chaque demande entrante et pose les bonnes questions.",
                  "bullets": ["Budget, urgence, service concerné", "Fiche prête dans votre CRM", "Les demandes chaudes remontent en premier"]},
                 {"title": "Chatbot IA pour entreprise", "text": "Il répond aux questions fréquentes de vos clients, à toute heure.",
                  "bullets": ["Réponses fondées sur vos documents", "Aucune invention hors périmètre", "Passage de relais vers vous si besoin"]},
                 {"title": "Assistant IA d'entreprise", "text": "Un collègue numérique pour vos équipes.",
                  "bullets": ["Retrouve l'info dans vos documents", "Rédige les premières versions", "Prépare comptes rendus et synthèses"]},
                 {"title": "Agent de tri et de réponse", "text": "Il lit la boîte mail ou le support, classe, répond au simple et transmet le reste.",
                  "bullets": ["Classement par type de demande", "Réponses types personnalisées", "Rien ne reste sans réponse"]},
             ]},
            {"type": "table", "tint": True, "eyebrow": "Repères", "title": "Chatbot, automatisation ou agent : de quoi avez-vous besoin ?",
             "md": "| | Automatisation | Chatbot | Agent IA |\n|---|---|---|---|\n"
                   "| Principe | Exécute des règles fixes | Répond à des questions | Comprend, décide, agit |\n"
                   "| Bon pour | Tâches prévisibles | FAQ, premier contact | Demandes variées, multi-étapes |\n"
                   "| Exemple | Facture envoyée à la validation | « Quels sont vos horaires ? » | Qualifier un lead puis créer sa fiche |\n"
                   "| Risque | Faible, très prévisible | Moyen | À encadrer avec des garde-fous |"},
            {"type": "steps", "eyebrow": "Déploiement IA en entreprise", "title": "Comment on déploie un agent, sans mauvaise surprise",
             "lede": "Un déploiement IA en entreprise réussi tient plus à son cadrage qu'à la technologie.",
             "items": [
                 ("Cadrer le périmètre", "Ce que l'agent fait, ce qu'il ne fait jamais, et quand il passe la main à un humain."),
                 ("Le nourrir de vos données", "Vos documents, vos règles, votre ton. L'agent s'appuie sur vos sources, pas sur son imagination."),
                 ("Tester sur des cas réels", "Des centaines de demandes passées, rejouées pour mesurer la qualité avant toute mise en ligne."),
                 ("Lancer et suivre", "Mise en ligne progressive, journal des échanges, ajustements réguliers."),
             ]},
            {"type": "links", "tint": True, "slugs": ["ia-pour-pme", "automatisation-pme", "automatisation-make-n8n"]},
            {"type": "faq"},
        ],
        "faq": [
            ("Un agent IA peut-il se tromper ?",
             "Oui, comme n'importe quel collaborateur. C'est pourquoi on le limite à un périmètre précis, on l'ancre dans vos documents, on lui interdit d'improviser hors sujet et on prévoit une escalade vers un humain."),
            ("Quelle différence entre un chatbot IA et un agent IA ?",
             "Un chatbot répond à des questions. Un agent va plus loin : il peut enchaîner plusieurs étapes, par exemple lire un message, consulter un outil, créer une fiche et répondre."),
            ("Combien de temps pour mettre un agent en place ?",
             "Un premier agent sur un périmètre simple peut être en test en quelques semaines. Le temps dépend surtout de la qualité de vos documents de référence."),
            ("Où sont stockées mes données ?",
             "On le définit avec vous. Les accès sont limités au strict nécessaire, documentés et révocables. Voir [l'IA conforme au RGPD en entreprise](/blog/ia-rgpd-entreprise/)."),
            ("Un agent IA qualifie-t-il vraiment mes leads ?",
             "Il pose les questions que vos commerciaux posent toujours en premier (budget, délai, besoin) et classe la demande. Les décisions commerciales restent les vôtres."),
        ],
    },
    {
        "slug": "automatisation-make-n8n",
        "group": "solutions",
        "nav_label": "Make & n8n",
        "nav_desc": "Experts des plateformes d'automatisation",
        "card_title": "Expert Make et n8n",
        "card_text": "Des scénarios Make et n8n robustes, documentés et à vous, construits par des ingénieurs.",
        "title": "Expert Make et n8n : automatisation sur mesure | Croisia",
        "description": "Expert Make et expert n8n pour PME : scénarios d'automatisation robustes, documentés, supervisés. Vous restez propriétaire. Audit gratuit.",
        "eyebrow": "Make · n8n",
        "h1": "Expert Make et n8n : vos outils reliés, vos process automatisés",
        "lede": "Make et n8n sont les deux plateformes que nous utilisons au quotidien pour relier vos logiciels. "
                "Croisia conçoit des scénarios fiables, documentés et supervisés, dont vous restez propriétaire.",
        "service_type": "Automatisation Make et n8n",
        "points": ["Scénarios documentés", "Alertes en cas d'échec", "Comptes et accès à votre nom"],
        "blocks": [
            {"type": "cards", "eyebrow": "Pourquoi nous", "title": "Un expert Make ou n8n, ce n'est pas qu'un assembleur de blocs",
             "items": [
                 {"title": "Des scénarios conçus pour durer", "text": "Gestion des erreurs, nouvelles tentatives, journaux : un scénario qui plante en silence est pire que pas de scénario."},
                 {"title": "Une approche d'ingénieurs", "text": "On vient de l'aviation civile : on pense en flux, en cas limites et en sécurité avant de construire."},
                 {"title": "Vous restez propriétaire", "text": "Les comptes, les scénarios et la documentation sont à votre nom. Pas de dépendance cachée envers nous."},
             ]},
            {"type": "table", "tint": True, "eyebrow": "Choisir", "title": "Make ou n8n : lequel pour votre PME ?",
             "md": "| | Make | n8n |\n|---|---|---|\n"
                   "| Prise en main | Éditeur visuel très accessible | Plus technique, très flexible |\n"
                   "| Hébergement | Service en ligne | Service en ligne **ou auto-hébergé** |\n"
                   "| Idéal pour | Équipes qui veulent suivre et modifier elles-mêmes | Flux complexes, données sensibles, besoins sur mesure |\n"
                   "| Intégrations | Très large catalogue d'applications | Large catalogue + code personnalisé |\n\n"
                   "Le détail, avec Zapier en prime, est dans notre [comparatif Make, n8n et Zapier](/blog/make-vs-n8n-vs-zapier/). "
                   "Et si vous hésitez entre plusieurs plateformes, voir nos [outils d'automatisation pour PME](/blog/outils-automatisation-pme/)."},
            {"type": "split", "eyebrow": "Exemples", "title": "Ce que nous construisons avec Make et n8n",
             "md": "Chaque scénario part d'un déclencheur (un email reçu, une ligne ajoutée, un formulaire envoyé) et enchaîne les actions utiles, sans que personne n'ait à y penser.",
             "bullets": ["Devis → CRM → facture, sans ressaisie", "Formulaire web → qualification → fiche CRM + notification", "Relances automatiques, avec arrêt dès la réponse", "Rapports hebdomadaires envoyés par email", "Synchronisation entre deux logiciels qui n'ont pas d'intégration native"]},
            {"type": "steps", "tint": True},
            {"type": "links", "slugs": ["automatisation-pme", "agents-ia", "ia-pour-pme"]},
            {"type": "articles", "title": "Pour choisir et comparer", "max": 3},
            {"type": "faq"},
        ],
        "faq": [
            ("Make ou n8n : lequel choisir ?",
             "Make est parfait si votre équipe veut comprendre et modifier ses scénarios elle-même. n8n est préférable pour les flux complexes ou si vous voulez héberger la plateforme vous-même. On vous conseille après l'audit."),
            ("Et Zapier ?",
             "Zapier est très simple, mais devient vite coûteux et limité dès que les flux se complexifient. Voir notre [comparatif](/blog/make-vs-n8n-vs-zapier/)."),
            ("Que se passe-t-il si un scénario plante ?",
             "Chaque scénario est conçu avec une gestion d'erreurs et une alerte. Vous êtes prévenu, et on corrige. Aucune donnée n'est perdue en silence."),
            ("À qui appartiennent les scénarios ?",
             "À vous. Les comptes sont créés à votre nom, la documentation vous est remise, et vous pouvez reprendre la main à tout moment."),
        ],
    },
    {
        "slug": "visibilite-web",
        "group": "solutions",
        "nav_label": "Visibilité web",
        "nav_desc": "Site vitrine, SEO, fiche Google",
        "card_title": "Visibilité web",
        "card_text": "Un site vitrine rapide, un référencement SEO sérieux et une fiche Google qui travaille pour vous.",
        "title": "Création de site vitrine PME et SEO | Croisia",
        "description": "Création de site vitrine pour PME et référencement SEO : site rapide, pages de conversion, fiche Google. Pour être trouvé par vos futurs clients.",
        "eyebrow": "Visibilité web",
        "h1": "Création de site vitrine PME et référencement SEO",
        "lede": "Vos futurs clients cherchent, trouvent un concurrent. Croisia crée des sites vitrines rapides et lisibles, "
                "et travaille leur référencement SEO pour que votre PME soit trouvée au bon moment.",
        "points": ["Site rapide et lisible", "Contenu pensé pour la conversion", "Suivi du référencement"],
        "blocks": [
            {"type": "cards", "eyebrow": "Ce qu'on fait", "title": "Trois piliers pour être trouvé, puis choisi",
             "items": [
                 {"title": "Site vitrine", "text": "Création de site vitrine pour PME : rapide, lisible sur mobile, avec des pages qui présentent clairement vos services."},
                 {"title": "Référencement SEO", "text": "Structure technique, contenus qui répondent aux vraies recherches de vos clients, maillage interne, suivi des positions."},
                 {"title": "Fiche Google", "text": "Une fiche Google entreprise complète, à jour, avec des avis qui rassurent.", "href": "/blog/fiche-google-entreprise/", "more": "Lire le guide"},
             ]},
            {"type": "split", "tint": True, "eyebrow": "Méthode", "title": "Un site qui sert votre activité, pas seulement votre image",
             "md": "Un site vitrine n'a de valeur que s'il amène des demandes. On part donc de **ce que cherchent vos clients**, puis on construit les pages qui répondent à ces recherches, avec un appel à l'action clair à chaque étape.\n\n"
                   "Côté technique : pages légères, structure propre, balises soignées. Côté contenu : un vocabulaire de vos clients, pas du jargon d'agence.",
             "bullets": ["Recherche des requêtes de vos clients", "Une page par offre, par secteur ou par besoin", "Mesure : positions, visites, demandes reçues"]},
            {"type": "prose", "eyebrow": "Résultat réel", "title": "Ce que ça donne",
             "md": "> « Une refonte de notre site et un vrai travail sur le référencement naturel : nous sommes passés d'environ 60 à près de 150 pages positionnées sur Google, et nous avons atteint la 2e place sur notre requête la plus stratégique. » **Pierre-Emmanuel Saliou**, dirigeant de Skaelia"},
            {"type": "steps"},
            {"type": "links", "tint": True, "slugs": ["automatisation-pme", "recrutement", "immobilier"]},
            {"type": "articles", "max": 3},
            {"type": "faq"},
        ],
        "faq": [
            ("Combien de temps pour être bien référencé ?",
             "Le SEO est un travail de fond : comptez plusieurs mois pour voir des positions s'installer, plus vite sur des requêtes précises et locales. On vous donne des repères réalistes dès l'audit."),
            ("Faut-il un site neuf ou améliorer l'existant ?",
             "On regarde d'abord l'existant. Si la base est saine, on l'améliore. Si elle bloque le référencement ou la lecture mobile, on le refait proprement."),
            ("Pouvez-vous gérer ma fiche Google ?",
             "Oui : renseignement complet, catégories, photos, publications, réponses aux avis. Voir [comment optimiser votre fiche Google entreprise](/blog/fiche-google-entreprise/)."),
            ("Le site pourra-t-il s'automatiser aussi ?",
             "C'est tout l'intérêt : formulaire vers CRM, notification, réponse automatique, qualification par un [agent IA](/agents-ia/). La visibilité et l'automatisation se renforcent."),
        ],
    },
    # ======================================================================= SECTEURS
    {
        "slug": "recrutement",
        "group": "secteurs",
        "nav_label": "Cabinets de recrutement",
        "nav_desc": "ATS, relances candidats, CV, entretiens",
        "card_title": "Cabinets de recrutement",
        "card_text": "Relances candidats, double saisie ATS, recherche dans votre base, comptes rendus : le temps rendu aux recruteurs.",
        "breadcrumb": "Cabinets de recrutement",
        "title": "Automatisation et IA pour cabinets de recrutement | Croisia",
        "description": "Automatisation et IA pour cabinets de recrutement : relances candidats, fin de la double saisie ATS, recherche dans la base, comptes rendus d'entretien.",
        "eyebrow": "Pour les cabinets de recrutement",
        "h1": "Automatisation et IA pour cabinets de recrutement",
        "lede": "Vos recruteurs devraient parler à des candidats et à des clients, pas ressaisir des CV. Croisia automatise les tâches "
                "administratives d'un cabinet de recrutement et branche l'IA là où elle fait gagner du temps.",
        "service_type": "Automatisation pour cabinets de recrutement",
        "points": ["Compatible avec votre ATS et votre CRM", "L'humain décide, l'IA prépare", "RGPD pris en compte dès la conception"],
        "blocks": [
            {"type": "pains", "eyebrow": "Le quotidien", "title": "Gagner du temps en cabinet de recrutement : où part-il ?",
             "items": [
                 ("Les mêmes données saisies deux fois", "Le CV arrive par email, puis il est recopié dans l'ATS. Chaque candidature coûte des minutes de saisie."),
                 ("Les relances candidats", "Accusés de réception, retours après entretien, rappels : tout le monde sait qu'il faut le faire, peu de cabinets y arrivent systématiquement."),
                 ("Une base de candidats qui dort", "Des milliers de profils déjà qualifiés, introuvables parce que la recherche par mots-clés ne retrouve pas les bons."),
                 ("Les plannings d'entretiens", "Des allers-retours d'emails pour caser un rendez-vous entre trois agendas."),
             ]},
            {"type": "cards", "tint": True, "eyebrow": "Ce qu'on met en place", "title": "Les automatisations qui comptent pour un cabinet de recrutement",
             "items": [
                 {"title": "Relances candidats automatiques", "text": "Chaque candidat reçoit un retour au bon moment, personnalisé, sans que le recruteur y pense.", "href": "/blog/automatiser-relances-candidats/", "more": "Lire le guide"},
                 {"title": "Fin de la double saisie ATS", "text": "Le CV reçu par email crée ou met à jour la fiche candidat, sans recopie.", "href": "/blog/double-saisie-ats/", "more": "Lire le guide"},
                 {"title": "Retrouver d'anciens candidats", "text": "Recherche sémantique dans votre base : décrivez le profil, retrouvez ceux qui y ressemblent.", "href": "/blog/retrouver-anciens-candidats/", "more": "Lire le guide"},
                 {"title": "Planification des entretiens", "text": "Le candidat choisit un créneau libre, l'invitation et les rappels partent seuls.", "href": "/blog/planification-entretiens/", "more": "Lire le guide"},
                 {"title": "Comptes rendus d'entretien", "text": "Notes ou enregistrement transformés en compte rendu structuré, que le recruteur relit et valide.", "href": "/blog/ia-comptes-rendus/", "more": "Lire le guide"},
                 {"title": "Prospection de clients", "text": "Veille sur les entreprises qui recrutent et séquences de relance cadrées.", "href": "/blog/prospection-cabinet-recrutement/", "more": "Lire le guide"},
             ]},
            {"type": "split", "eyebrow": "Votre outillage", "title": "Votre ATS reste en place, on le branche",
             "md": "Que vous travailliez avec T4S ou un autre ATS, l'enjeu est le même : **faire circuler l'information** entre la messagerie, l'agenda, l'ATS et la facturation, sans ressaisie.\n\n"
                   "Selon l'outil, la connexion passe par son API, ses webhooks, des imports ou des exports automatisés. On vérifie ce qui est possible pendant l'audit. Voir [l'intégration d'un ATS avec Make ou n8n](/blog/automatisation-ats/) et [l'automatisation avec T4S](/blog/t4s-automatisation/).",
             "bullets": ["CV reçus → fiche ATS", "Entretien planifié → agenda + relance", "Placement validé → facture", "Mission ouverte → alerte et matching"],
             "meta": "Make · n8n · API de votre ATS"},
            {"type": "prose", "eyebrow": "Données candidats", "title": "L'IA en recrutement et le RGPD",
             "md": "Les données de candidats sont sensibles et la réglementation les encadre. L'IA peut résumer, classer et rechercher, **mais elle ne doit pas décider seule** d'écarter un candidat. Un agent IA pour le recrutement prépare le travail, le recruteur décide. On conçoit donc des automatisations qui préparent le travail du recruteur, qui reste décisionnaire, avec des durées de conservation maîtrisées. Détails dans notre guide [IA en recrutement et RGPD](/blog/ia-recrutement-rgpd/)."},
            {"type": "cards", "tint": True, "title": "Votre cabinet est aussi une vitrine", "eyebrow": "Site web",
             "lede": "Un cabinet est jugé par deux publics : les entreprises qui recrutent et les candidats. Une refonte de site web de cabinet de recrutement doit parler aux deux.",
             "cols": 2,
             "items": [{"title": "Refonte de site pour cabinet", "text": "Pages par métier et par secteur, offres lisibles, formulaires reliés à votre ATS.", "href": "/visibilite-web/", "more": "Voir la visibilité web"},
                       {"title": "Facturation automatisée", "text": "Une facture créée au bon moment, avec les bonnes informations, dès qu'un placement est validé.", "href": "/blog/facturation-cabinet-recrutement/", "more": "Lire le guide"}]},
            {"type": "steps", "items": SECTOR_STEPS},
            {"type": "articles", "segment": "recrutement", "max": 9},
            {"type": "faq"},
        ],
        "faq": [
            ("Quels ATS pouvez-vous connecter ?",
             "Tout outil qui expose une API, des webhooks ou des imports automatisés. La faisabilité se vérifie pendant l'audit, avant tout engagement."),
            ("L'IA peut-elle présélectionner mes candidats ?",
             "Elle peut résumer un profil, extraire les compétences, rapprocher une candidature d'une mission. La décision d'écarter ou de retenir doit rester humaine, ce qui est aussi la meilleure pratique RGPD."),
            ("Comment gérez-vous les données des candidats ?",
             "Accès limités, durées de conservation définies avec vous, pas de réutilisation à d'autres fins. Voir [IA en recrutement et RGPD](/blog/ia-recrutement-rgpd/)."),
            ("Un cabinet de 5 personnes est-il concerné ?",
             "Oui : c'est souvent là que la double saisie et les relances pèsent le plus, puisqu'il n'y a pas d'assistant dédié."),
        ],
    },
    {
        "slug": "concessions-automobiles",
        "group": "secteurs",
        "nav_label": "Concessions automobiles",
        "nav_desc": "Sourcing VO, leads, relances, CRM",
        "card_title": "Concessions automobiles",
        "card_text": "Sourcing de véhicules d'occasion, qualification des leads, relances clients et reporting pour concessionnaires.",
        "breadcrumb": "Concessions automobiles",
        "title": "Automatisation et IA pour concessions automobiles | Croisia",
        "description": "Automatisation et IA pour concessions automobiles : sourcing de véhicules d'occasion, qualification des leads, relances clients et suivi des commissions.",
        "eyebrow": "Pour les concessionnaires et marchands",
        "h1": "Automatisation et IA pour concessions automobiles",
        "lede": "Trouver les bonnes affaires avant les autres, répondre vite à chaque lead, relancer sans oublier : "
                "Croisia automatise les tâches chronophages d'une concession automobile pour que vos équipes vendent plus et cherchent moins.",
        "service_type": "Automatisation pour concessions automobiles",
        "points": ["Complète votre logiciel existant", "Veille et alertes sur mesure", "Leads traités en quelques minutes"],
        "blocks": [
            {"type": "pains", "eyebrow": "Le quotidien", "title": "Gagner du temps en concession automobile",
             "items": [
                 ("Le sourcing de véhicules d'occasion", "Des heures à parcourir les annonces pour dénicher les rares véhicules vraiment bien placés."),
                 ("Des leads qui refroidissent", "Une demande reçue un vendredi soir, rappelée le mardi : le client a déjà vu ailleurs."),
                 ("Les relances au bon moment", "Après un essai, un devis, ou à l'approche d'un entretien : tout repose sur la mémoire des vendeurs."),
                 ("Un reporting laborieux", "Ventes, commissions, stocks : des chiffres rassemblés à la main."),
             ]},
            {"type": "cards", "tint": True, "eyebrow": "Ce qu'on met en place", "title": "Un logiciel de concessionnaire automobile, ou des automatisations autour du vôtre ?",
             "lede": "On ne remplace pas votre logiciel métier : on le complète pour qu'il communique avec le reste et travaille pour vous.",
             "items": [
                 {"title": "Sourcing de véhicules d'occasion", "text": "Une veille continue des annonces correspondant à vos critères, avec alerte sur les opportunités.", "href": "/blog/veille-annonces-vehicules/", "more": "Lire le guide"},
                 {"title": "Trouver les bonnes affaires", "text": "Comparer chaque annonce au prix du marché pour faire remonter les écarts intéressants.", "href": "/blog/bonnes-affaires-vehicules-occasion/", "more": "Lire le guide"},
                 {"title": "Qualification des leads par agent IA", "text": "Un agent IA pour concessionnaire qualifie chaque demande (projet, budget, reprise, délai) avant son arrivée chez le vendeur.", "href": "/blog/leads-concession-automobile/", "more": "Lire le guide"},
                 {"title": "Relances clients", "text": "Suites d'essais, devis en attente, entretiens à venir : les bons messages partent au bon moment.", "href": "/blog/relances-concession-auto/", "more": "Lire le guide"},
                 {"title": "CRM automatisé", "text": "Chaque interaction remonte seule dans la bonne fiche. Fini les fiches incomplètes.", "href": "/blog/crm-concession-auto/", "more": "Lire le guide"},
                 {"title": "Commission des vendeurs et reporting", "text": "Calcul de la commission de chaque vendeur selon vos règles, et tableau de bord des ventes alimentés automatiquement."},
             ]},
            {"type": "split", "eyebrow": "Recherche de véhicules", "title": "Un logiciel de recherche de véhicules d'occasion pour concessionnaire, sur mesure",
             "md": "Les plateformes d'annonces proposent des alertes, mais chacune dans son coin. Notre approche rassemble vos sources, applique **vos** critères (marque, kilométrage, marge visée, distance) et fait remonter les annonces qui méritent un appel. Voir aussi notre [alternative au scraping d'annonces](/blog/veille-annonces-vehicules/).\n\n"
                   "Nous restons attentifs aux conditions d'utilisation de chaque source : on privilégie les flux et alertes autorisés.",
             "bullets": ["Critères définis par vous", "Comparaison au prix du marché", "Alerte immédiate (mail, message)", "Historique pour suivre les prix"]},
            {"type": "steps", "tint": True, "items": SECTOR_STEPS},
            {"type": "articles", "segment": "auto", "max": 9},
            {"type": "faq"},
        ],
        "faq": [
            ("Remplacez-vous notre logiciel de gestion de concession ?",
             "Non. On se branche à vos outils actuels (CRM, logiciel de gestion, messagerie, tableurs) et on automatise ce qui se passe entre eux."),
            ("Comment trouvez-vous les bonnes affaires de véhicules d'occasion ?",
             "On suit les annonces correspondant à vos critères et on les compare au marché pour repérer les écarts. Vous recevez une alerte sur les meilleures opportunités, avec les éléments pour décider vite."),
            ("Est-ce légal de surveiller des annonces ?",
             "Ça dépend des sources et de leurs conditions d'utilisation. On privilégie les alertes, flux et API autorisés, et on vous le dit clairement quand une source pose problème."),
            ("Les leads seront-ils vraiment traités plus vite ?",
             "Oui : la qualification démarre dès la réception, à toute heure, et le vendeur reçoit une fiche déjà renseignée."),
        ],
    },
    {
        "slug": "immobilier",
        "group": "secteurs",
        "nav_label": "Agences immobilières",
        "nav_desc": "Veille d'annonces, leads, relances, estimations",
        "card_title": "Agences immobilières",
        "card_text": "Veille d'annonces, qualification des leads acquéreurs et vendeurs, relances et rédaction : le temps rendu aux agents.",
        "breadcrumb": "Immobilier",
        "title": "Automatisation et IA pour agences immobilières | Croisia",
        "description": "Automatisation et IA pour agences immobilières et chasseurs : veille d'annonces, qualification des leads, relances, estimation et rédaction d'annonces.",
        "eyebrow": "Pour les agences et les chasseurs immobiliers",
        "h1": "Automatisation et IA pour agences immobilières",
        "lede": "Un agent immobilier vend du conseil et de la confiance, pas des heures de saisie. Croisia automatise la veille, "
                "la qualification des leads et les relances d'une agence immobilière, pour que chaque contact ait la réponse qu'il mérite.",
        "service_type": "Automatisation pour agences immobilières",
        "points": ["Branché à votre CRM actuel", "Veille d'annonces sur vos critères", "Rédaction relue par vos agents"],
        "blocks": [
            {"type": "pains", "eyebrow": "Le quotidien", "title": "Gagner du temps en agence immobilière",
             "items": [
                 ("La veille d'annonces", "Trouver des biens immobiliers automatiquement, plutôt qu'actualiser dix sites chaque matin."),
                 ("Des demandes qui s'accumulent", "Acquéreurs, vendeurs, curieux : sans tri, les contacts sérieux se noient parmi les autres."),
                 ("Les relances", "Un acquéreur qui a visité sans suite, un vendeur à recontacter : tout se perd faute de rappel."),
                 ("La rédaction", "Estimations, annonces, comptes rendus de visite : des textes à produire en série."),
             ]},
            {"type": "cards", "tint": True, "eyebrow": "Ce qu'on met en place", "title": "Un logiciel d'automatisation pour agence immobilière, sur mesure",
             "items": [
                 {"title": "Veille d'annonces", "text": "Un suivi automatique des nouvelles annonces selon vos critères, avec alerte immédiate.", "href": "/blog/veille-annonces-immobilieres/", "more": "Lire le guide"},
                 {"title": "Détection des bonnes affaires", "text": "Comparaison au marché pour faire ressortir les biens à étudier en priorité.", "href": "/blog/veille-annonces-immobilieres/", "more": "Lire le guide"},
                 {"title": "Qualification des leads", "text": "Un agent IA pose les premières questions et prépare une fiche acquéreur ou vendeur.", "href": "/blog/leads-immobilier/", "more": "Lire le guide"},
                 {"title": "Relances acquéreurs et vendeurs", "text": "Chaque contact est relancé au bon moment, avec un message adapté à son stade.", "href": "/blog/relances-immobilier/", "more": "Lire le guide"},
                 {"title": "Aide à l'estimation", "text": "Des données de marché rassemblées pour accélérer l'estimation, que l'agent valide.", "href": "/blog/estimation-immobiliere-ia/", "more": "Lire le guide"},
                 {"title": "Rédaction d'annonces", "text": "Une première version rédigée à partir de la fiche du bien, relue par l'agent.", "href": "/blog/annonces-immobilieres-ia/", "more": "Lire le guide"},
             ]},
            {"type": "split", "eyebrow": "Pour les chasseurs", "title": "Un logiciel de chasseur immobilier : la veille qui travaille à votre place",
             "md": "Si vous cherchez des biens pour vos clients, la rapidité fait la différence. On met en place une veille construite autour du **cahier des charges de chaque mandat** : secteur, budget, critères, et on vous prévient dès qu'un bien correspond.\n\n"
                   "Et côté commissions : suivi des mandats, des ventes et des honoraires dans un tableau de bord qui se met à jour seul, y compris le calcul de la commission de chaque agent.",
             "bullets": ["Veille adaptée à chaque mandat", "Alerte immédiate sur les correspondances", "Fiche de bien pré-remplie", "Suivi des commissions par agent"]},
            {"type": "steps", "tint": True, "items": SECTOR_STEPS},
            {"type": "articles", "segment": "immo", "max": 9},
            {"type": "faq"},
        ],
        "faq": [
            ("Pouvez-vous connecter le CRM de notre agence ?",
             "Dans la grande majorité des cas, oui : via son API, des imports ou des exports automatisés. On le vérifie pendant l'audit gratuit."),
            ("L'IA peut-elle estimer un bien ?",
             "Elle peut rassembler et comparer des données (ventes proches, annonces similaires) pour accélérer le travail. L'estimation finale reste celle de l'agent. Voir [l'estimation immobilière avec l'IA](/blog/estimation-immobiliere-ia/)."),
            ("Les annonces rédigées par IA sont-elles conformes ?",
             "Un texte généré est une première version. L'agent relit, et les mentions obligatoires (honoraires, classe énergétique…) sont ajoutées par un modèle fixe, pas laissées à l'IA."),
            ("Comment trouvez-vous des biens automatiquement ?",
             "Par une veille de sources d'annonces selon des critères précis, avec alerte quand un bien correspond. On tient compte des conditions d'utilisation de chaque source."),
        ],
    },
    # ===================================================================== CONVERSION
    {
        "slug": "audit-gratuit",
        "group": "conversion",
        "nav_label": "Audit gratuit",
        "nav_desc": "30 minutes pour repérer ce qui s'automatise",
        "card_title": "Audit gratuit",
        "card_text": "30 minutes en visio pour repérer ce qui peut être automatisé chez vous.",
        "title": "Audit d'automatisation gratuit pour PME | Croisia",
        "description": "Audit d'automatisation gratuit : 30 minutes en visio pour repérer les tâches à automatiser dans votre entreprise. Sans engagement, réponse sous 24 h.",
        "eyebrow": "Audit gratuit et sans engagement",
        "h1": "Audit d'automatisation gratuit : 30 minutes pour repérer ce qui peut l'être",
        "lede": "Un audit IA pour entreprise, sans jargon et sans engagement : on identifie ensemble les tâches qui vous coûtent le plus d'heures, "
                "et on vous dit ce qui peut être automatisé, avec quels outils, pour quel gain.",
        "cta": "Remplir le formulaire",
        "cta_href": "#contact",
        "points": ["30 minutes en visio", "Sans préparation", "Réponse sous 24 h"],
        "blocks": [
            {"type": "steps", "eyebrow": "Déroulé", "title": "Ce qui se passe, concrètement",
             "lede": "Un audit, trois temps. Rien à préparer.",
             "items": [
                 ("Vous décrivez", "Par le formulaire ci-dessous, en une phrase : la tâche qui vous coûte le plus de temps."),
                 ("On échange 30 minutes", "En visio, on passe en revue vos outils, vos tâches répétitives et vos priorités."),
                 ("Vous recevez une liste priorisée", "Ce qui peut être automatisé, avec quels outils, et le gain de temps estimé pour chaque point."),
             ]},
            {"type": "split", "tint": True, "eyebrow": "Livrable", "title": "Ce que vous recevez à l'issue de l'audit",
             "md": "Une liste claire, classée par rapport gain/effort. Vous pouvez en faire ce que vous voulez : la mettre en œuvre avec nous, avec vos équipes, ou l'oublier. **Aucune relance commerciale.**",
             "bullets": ["Les tâches à automatiser, classées par priorité", "Les outils concernés et ce qu'on peut brancher", "Le gain de temps estimé, tâche par tâche", "Une idée du coût et du délai avant tout devis"]},
            {"type": "form", "eyebrow": "Contact", "title": "Prêt à gagner du temps **dès ce mois-ci** ?",
             "lede": "Décrivez-nous la tâche qui vous coûte le plus d'heures. On vous répond sous 24 h avec une première piste, même si on ne travaille pas ensemble.",
             "bullets": ["30 minutes en visio, sans préparation", "Une liste priorisée de ce qui peut être automatisé", "Aucun engagement, aucune relance commerciale"]},
            {"type": "faq", "title": "Questions sur l'audit"},
        ],
        "faq": [
            ("L'audit est-il vraiment gratuit ?",
             "Oui, sans condition et sans engagement. C'est notre façon de montrer ce qu'on sait faire, et de vous donner une vision utile même si vous décidez de ne pas continuer avec nous."),
            ("Que dois-je préparer ?",
             "Rien. Pensez simplement à la tâche qui vous fait perdre le plus de temps, et aux outils que vous utilisez. On construit le reste ensemble."),
            ("Quelles entreprises sont concernées ?",
             "Les PME à partir du moment où au moins une personne répète les mêmes tâches chaque semaine. Nous avons une expérience particulière auprès des cabinets de recrutement, concessions automobiles et agences immobilières."),
            ("Et après l'audit ?",
             "Vous recevez un devis sur mesure, chantier par chantier, si vous le souhaitez. Vous choisissez ce que vous lancez, et vous pouvez commencer par une seule automatisation."),
            ("Mes données restent-elles confidentielles ?",
             "Oui. Vous n'avez rien à transmettre de sensible pour l'audit, et nous ne réutilisons pas vos informations à d'autres fins."),
        ],
    },
]
