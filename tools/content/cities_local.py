"""Contenu local propre à chaque ville (pôles d'activité, cas concret, secteurs, FAQ, appels à l'action).

Objectif : que deux pages villes ne partagent pas de paragraphes entiers. Mesurer avec
`python tools/similarity.py` après toute modification.

Règles d'écriture :
- Faits locaux généraux et vérifiables (quartiers d'affaires, parcs d'activité, filières connues).
  Ni chiffres, ni noms d'entreprises, ni clients cités.
- Les « exemples types » sont des scénarios illustratifs, annoncés comme tels. Jamais présentés comme des clients.
- Aucune agence locale revendiquée : Croisia travaille à distance.
"""

EXTRA = {
    "toulouse": {
        "tagline": "Aéronautique, spatial et bureaux d'études",
        "lede": "Entre les sous-traitants de l'aéronautique, les acteurs du spatial et les bureaux d'études, les PME toulousaines vivent de documents, "
                "de devis techniques et de suivi de commandes. Croisia, agence d'automatisation et d'IA, relie vos outils pour que ce travail de fond "
                "ne repose plus sur la mémoire de vos équipes.",
        "desc": "Agence d'automatisation et d'IA pour PME à Toulouse : sous-traitance aéronautique, bureaux d'études, Labège, Blagnac. Audit gratuit en visio.",
        "title": "Automatisation PME Toulouse : guide et conseil | Croisia",
        "h1": "Automatisation à Toulouse pour les PME",
        "h_auto": "Automatisation PME à Toulouse : la sous-traitance et ses documents",
        "h_ia": "IA pour PME à Toulouse : lire, retrouver, résumer",
        "h_agents": "Agent IA à Toulouse : filtrer les demandes techniques",
        "poles_title": "Où se concentrent les PME de l'agglomération toulousaine",
        "poles": [
            ("Blagnac et la filière aéronautique", "Autour de l'aéroport, sous-traitants et prestataires de l'industrie aéronautique gèrent des commandes, des révisions de documents et des exigences de traçabilité. Les relances de pièces et la mise à jour des dossiers sont des tâches typiques à automatiser."),
            ("Labège et son parc d'affaires", "Un grand parc d'affaires au sud-est de Toulouse, avec beaucoup d'éditeurs, de sociétés de services et d'entreprises du numérique. Leur quotidien : support, facturation récurrente et suivi d'abonnements."),
            ("Montaudran et le spatial", "Sur l'ancien site de l'Aéropostale, un campus s'est développé autour de l'aérospatial et de la recherche. Les besoins portent surtout sur les comptes rendus, la gestion de projets et la circulation de documents."),
            ("Le centre et les services", "Cabinets, agences et professions libérales du centre-ville : prise de rendez-vous, relances clients et facturation, souvent gérées à la main."),
        ],
        "scenario_title": "Exemple : le suivi de devis d'un bureau d'études",
        "scenario": "Exemple type, à adapter à votre cas. Un bureau d'études d'une vingtaine de personnes reçoit des demandes de devis par email, avec des cahiers des charges en pièce jointe.\n\n"
                    "Avant : chaque demande est lue, ressaisie dans le CRM, puis relancée à la main. Après :\n\n"
                    "1. l'email entrant crée la fiche dans le CRM ;\n2. une IA lit le cahier des charges et en résume les points clés ;\n"
                    "3. le chargé d'affaires reçoit la fiche et le résumé, et prépare le devis ;\n4. une relance part si le client n'a pas répondu au bout de quelques jours.",
        "sectors": {
            "recrutement": "De nombreux cabinets toulousains recrutent des ingénieurs et des techniciens pour l'aéronautique, le spatial et le numérique. Les relances candidats, la base de profils interrogeable et les comptes rendus d'entretien y font gagner un temps précieux.",
            "auto": "Dans l'agglomération, les concessions et les marchands de véhicules d'occasion gagnent du temps sur le sourcing d'annonces et sur la qualification des demandes reçues par le site, le téléphone et les plateformes.",
            "immo": "Toulouse attire de nouveaux habitants et son marché immobilier est actif : veille d'annonces, qualification des acquéreurs et relances aident les agences à répondre vite.",
        },
        "faq": [
            ("Un consultant en automatisation peut-il se déplacer à Toulouse ?", "L'audit se fait en visio, ce qui suffit dans la plupart des cas. Comme notre école, l'ENAC, est à Toulouse, un rendez-vous sur place dans l'agglomération peut être étudié selon le projet."),
            ("Pouvez-vous travailler avec des entreprises de l'aéronautique ?", "Nous venons de l'aviation civile et connaissons ses exigences de rigueur et de traçabilité. Les automatisations sont documentées et contrôlées ; pour des données sensibles, on privilégie un hébergement maîtrisé, par exemple l'auto-hébergement avec n8n."),
            ("Mes documents techniques peuvent-ils être traités par une IA ?", "Oui, à condition de cadrer l'usage : l'IA lit vos documents, résume et retrouve l'information, mais ne diffuse rien en dehors de l'environnement choisi. Pour des documents confidentiels, on limite les accès et on définit l'hébergement avec vous."),
            ("Par quoi commencer pour un bureau d'études ?", "Par le flux d'entrée : les demandes de devis et leurs pièces jointes. Créer la fiche, résumer le cahier des charges et relancer automatiquement sont trois gains rapides, mesurables dès les premières semaines."),
        ],
        "cta_title": "Un projet à Toulouse ? Parlons-en 30 minutes.",
        "cta_text": "Décrivez-nous la tâche qui vous coûte le plus de temps dans votre bureau d'études, votre atelier ou votre cabinet toulousain. L'audit est gratuit, en visio, sans engagement.",
    },
    "paris": {
        "tagline": "Sièges sociaux, conseil et services",
        "lede": "À Paris et en Île-de-France, les équipes sont sollicitées en permanence et la concurrence est forte sur chaque demande. Croisia, agence d'automatisation "
                "et d'IA, aide les PME à répondre vite, à ne rien laisser tomber et à garder leurs outils à jour sans y passer leurs soirées.",
        "desc": "Agence d'automatisation et d'IA pour PME à Paris et en Île-de-France : réponse rapide, CRM à jour, relances. Audit gratuit en visio.",
        "h_auto": "Automatisation PME à Paris : tenir la cadence sans embaucher",
        "h_ia": "IA pour PME à Paris : trier la sollicitation permanente",
        "h_agents": "Agent IA à Paris : répondre en quelques secondes",
        "poles_title": "Les grands bassins d'activité de l'Île-de-France",
        "poles": [
            ("La Défense et les sièges sociaux", "Un quartier d'affaires qui concentre sièges sociaux et filiales. Les PME qui y gravitent (prestataires, cabinets, sous-traitants de services) jonglent avec des référencements fournisseurs, des demandes de devis et de longs cycles de validation."),
            ("Station F et l'écosystème startup", "Autour de ce campus, des jeunes entreprises qui grandissent vite et mettent en place leurs processus au fil de l'eau : facturation, accueil des clients, suivi. Automatiser tôt leur évite de recruter pour de l'administratif."),
            ("Paris-Saclay et la recherche", "Sur le plateau de Saclay, des laboratoires, des écoles et des entreprises techniques. Les besoins : gestion de documents, comptes rendus et suivi de projets de recherche et développement."),
            ("Le centre et le Sentier", "Agences, cabinets de conseil, juristes, recruteurs : de petites structures très sollicitées, dont la valeur tient à la réactivité, à la précision et au suivi de chaque contact."),
        ],
        "scenario_title": "Exemple : un cabinet de conseil submergé de demandes",
        "scenario": "Exemple type. Un cabinet de conseil parisien de douze personnes reçoit des demandes par son site, par email et par LinkedIn. Chaque demande est lue, classée et répartie à la main, parfois avec un jour de retard.\n\n"
                    "Avec une automatisation et un agent IA :\n\n"
                    "- toutes les demandes arrivent dans un seul CRM, sans doublon ;\n- l'agent pose les questions habituelles (besoin, calendrier, budget) et résume la demande ;\n"
                    "- la fiche est attribuée au bon associé, avec un accusé de réception envoyé immédiatement ;\n- les demandes sans suite sont relancées automatiquement.",
        "sectors": {
            "recrutement": "Paris concentre un grand nombre de cabinets de recrutement. Entre la double saisie dans l'ATS, les relances candidats et la prospection de clients, l'automatisation rend du temps de conversation avec les candidats.",
            "auto": "Pour les concessions et les marchands d'Île-de-France, où le stock se renouvelle vite, la veille d'annonces, la qualification des leads et les relances après essai font la différence.",
            "immo": "Dans un marché très concurrentiel, répondre en quelques minutes à un contact change l'issue. Veille d'annonces, qualification et suivi des mandats se prêtent bien à l'automatisation.",
        },
        "faq": [
            ("Un consultant en automatisation peut-il intervenir chez nous à Paris ?", "L'audit et le suivi se font en visio, ce qui est la norme à Paris. Une rencontre sur place peut être étudiée selon le projet."),
            ("Quelle taille d'entreprise accompagnez-vous en Île-de-France ?", "Des PME, dès qu'une personne répète les mêmes tâches chaque semaine. Le point idéal se situe entre 5 et 100 salariés, qu'il s'agisse d'une société de conseil, d'une agence ou d'une startup en croissance."),
            ("Comment une startup peut-elle automatiser sans alourdir ses outils ?", "En branchant ce qu'elle utilise déjà : formulaire, CRM, facturation, messagerie. On commence par un seul flux (l'arrivée des demandes, par exemple) et on étend ensuite, sans changer de logiciel."),
            ("Faut-il être à Paris intra-muros ?", "Non, l'Île-de-France entière est concernée, de La Défense à Saclay en passant par la Plaine Saint-Denis : le travail se fait à distance."),
        ],
        "cta_title": "Une demande à traiter plus vite à Paris ?",
        "cta_text": "Dites-nous quelle tâche mange le temps de votre équipe en Île-de-France. L'audit dure 30 minutes, il est gratuit et sans engagement.",
    },
    "lyon": {
        "tagline": "Industrie, santé, numérique et logistique",
        "lede": "Lyon et sa métropole réunissent industrie, santé, numérique et logistique, avec des entreprises qui n'utilisent presque jamais les mêmes outils. "
                "Croisia, agence d'automatisation et d'IA, relie ces outils entre eux plutôt que de vous demander d'en changer.",
        "desc": "Agence d'automatisation et d'IA pour PME à Lyon : industrie, santé, numérique, logistique. Relier vos outils sans les remplacer. Audit gratuit.",
        "h_auto": "Automatisation PME à Lyon : faire parler des outils très différents",
        "h_ia": "IA pour PME à Lyon : transformer des documents en données",
        "h_agents": "Agent IA à Lyon : un point d'entrée pour plusieurs outils",
        "poles_title": "Les quartiers et les filières de la métropole lyonnaise",
        "poles": [
            ("La Part-Dieu et le tertiaire", "Le principal quartier d'affaires de la ville regroupe cabinets, banques, assurances et services. Leurs PME partenaires ont des cycles de validation longs et beaucoup de relances à gérer."),
            ("Gerland et la santé", "Autour de Gerland, un pôle consacré aux biotechnologies et à la santé. Traçabilité, documents réglementaires et comptes rendus y pèsent lourd, ce qui rend l'extraction et le classement documentaires utiles."),
            ("Confluence et le numérique", "Un quartier récent où se côtoient entreprises de services, éditeurs et agences. Leur quotidien : facturation récurrente, support client et suivi de projets."),
            ("L'est lyonnais et la logistique", "Autour de l'aéroport Saint-Exupéry et des plateformes de l'est de l'agglomération, la logistique et la distribution génèrent des volumes de commandes, de livraisons et de relances."),
        ],
        "scenario_title": "Exemple : un négociant qui jongle avec trois logiciels",
        "scenario": "Exemple type. Une PME de négoce de trente personnes utilise un logiciel de devis, un outil de gestion de stock et un tableur pour le suivi des livraisons. Les trois ne communiquent pas : chaque commande est saisie deux fois.\n\n"
                    "Après automatisation :\n\n"
                    "1. le devis accepté crée automatiquement la commande dans l'outil de gestion ;\n2. le stock disponible est vérifié avant confirmation ;\n"
                    "3. le tableur de livraisons se met à jour tout seul ;\n4. le client reçoit un email de suivi aux étapes clés.\n\n"
                    "Aucun logiciel n'est remplacé : c'est la liaison qui change.",
        "sectors": {
            "recrutement": "Les cabinets lyonnais sont souvent spécialisés par filière (industrie, santé, tech). Une base de candidats interrogeable en langage naturel retrouve les bons profils parmi les anciens contacts.",
            "auto": "Pour les concessions de la métropole, un agent IA qualifie les demandes reçues par le site et les plateformes, et les relances après essai partent au bon moment.",
            "immo": "Agences et chasseurs lyonnais : une veille d'annonces par mandat, une qualification des contacts et une aide à l'estimation, reliées à votre CRM.",
        },
        "faq": [
            ("Nos outils sont très variés, est-ce un problème ?", "C'est même la situation la plus courante. On relie vos outils par leurs API ou des échanges de fichiers, sans les remplacer ni migrer vos données."),
            ("Un consultant en automatisation vient-il sur place à Lyon ?", "Non, ce n'est pas nécessaire : l'audit se fait en visio et la mise en place à distance. Un rendez-vous dans la métropole peut être étudié selon le projet."),
            ("L'IA peut-elle lire des documents réglementaires en santé ?", "Elle peut les résumer, les classer et retrouver un passage précis, avec la source indiquée. Pour des données sensibles, le choix de l'hébergement et des accès est défini avec vous avant toute mise en place."),
            ("Combien de temps pour relier trois logiciels ?", "Une première liaison simple se met en place en une à deux semaines. On commence par le flux le plus répétitif, puis on étend."),
        ],
        "cta_title": "Des outils qui ne se parlent pas à Lyon ?",
        "cta_text": "Décrivez-nous les logiciels que votre équipe utilise. En 30 minutes d'audit gratuit, on repère ce qui peut être relié en premier.",
    },
    "marseille": {
        "tagline": "Port, logistique, commerce et tourisme",
        "lede": "À Marseille, entre le port, la logistique, le commerce et le tourisme, beaucoup de petites structures sont débordées par l'administratif. Croisia, agence "
                "d'automatisation et d'IA, prend en charge les tâches répétitives pour redonner du temps à ceux qui travaillent sur le terrain.",
        "desc": "Agence d'automatisation et d'IA pour PME à Marseille : port, logistique, commerce, tourisme. Devis, relances, suivi de dossiers. Audit gratuit.",
        "h_auto": "Automatisation PME à Marseille : moins d'administratif, plus de terrain",
        "h_ia": "IA pour PME à Marseille : un usage à la fois, sans projet lourd",
        "h_agents": "Agent IA à Marseille : le standard numérique qui ne dort pas",
        "poles_title": "Les zones d'activité de Marseille et de sa région",
        "poles": [
            ("Euroméditerranée et les services", "Un grand quartier de bureaux et de projets urbains, près du port. Sociétés de services, cabinets et prestataires y ont besoin de devis rapides, de suivi client et d'une facturation fluide."),
            ("Le port et la logistique", "Transporteurs, transitaires, manutention et sous-traitants du port : des dossiers, des documents d'expédition et des relances à suivre en continu."),
            ("Château-Gombert et la technologie", "Un technopôle d'entreprises et de laboratoires au nord-est de la ville. Les besoins y sont proches de ceux d'une PME technique : suivi de projets, documentation et reporting."),
            ("Le Vieux-Port, le commerce et le tourisme", "Restaurants, hébergeurs, commerces, activités de loisirs en saison : des demandes de réservation et d'information à toute heure, souvent traitées au téléphone ou sur les messageries."),
        ],
        "scenario_title": "Exemple : un transitaire qui perd du temps sur les relances",
        "scenario": "Exemple type. Un petit transitaire suit une quarantaine de dossiers en cours. Chaque matin, une personne relit ses emails pour savoir quel client attend quel document, puis relance à la main.\n\n"
                    "Avec une automatisation :\n\n"
                    "- chaque dossier a un statut tenu à jour dans un tableau partagé ;\n- quand un document manque depuis plus de deux jours, un message poli part au client ;\n"
                    "- l'équipe reçoit chaque matin la liste des dossiers bloqués, triée par urgence ;\n- les clients qui répondent sortent automatiquement de la liste.",
        "sectors": {
            "recrutement": "À Marseille, cabinets et intermédiaires de recrutement gagnent du temps sur les relances candidats, la planification des entretiens et la facturation des placements.",
            "auto": "Concessions et marchands de la région : veille d'annonces d'occasion, qualification des demandes et relances clients, pour répondre vite dans un marché très actif.",
            "immo": "Marseille a un marché immobilier animé, avec beaucoup de contacts à traiter : veille d'annonces, qualification des acquéreurs et vendeurs, relances au bon moment.",
        },
        "faq": [
            ("Un consultant en automatisation accompagne-t-il les petites structures à Marseille ?", "Oui. Une seule automatisation bien choisie suffit souvent pour démarrer, et on la chiffre avant tout engagement."),
            ("Peut-on automatiser des tâches très terrain ?", "On n'automatise pas le terrain, mais ce qui l'entoure : devis, planning, relances, suivi de dossiers, documents. C'est ce qui libère du temps pour y être."),
            ("Comment gérer les demandes qui arrivent au téléphone et sur messagerie ?", "Un agent IA peut tenir le premier niveau sur les messageries et le site : renseigner, prendre les coordonnées, proposer un créneau. Les appels importants vous sont signalés."),
            ("L'audit est-il gratuit pour une entreprise marseillaise ?", "Oui, partout en France : 30 minutes en visio, sans engagement, avec une liste priorisée à la clé."),
        ],
        "cta_title": "Moins d'administratif à Marseille ?",
        "cta_text": "Parlez-nous de ce qui prend le plus de temps dans votre entreprise marseillaise. L'audit est gratuit, en visio, sans engagement.",
    },
    "bordeaux": {
        "tagline": "Négoce, aéronautique, numérique et tourisme",
        "lede": "Bordeaux mêle négoce et viticulture, aéronautique, numérique et tourisme. Croisia, agence d'automatisation et d'IA, aide les PME de la métropole à "
                "entretenir leurs relations clients et à produire leurs documents sans y passer des heures.",
        "desc": "Agence d'automatisation et d'IA pour PME à Bordeaux : négoce, aéronautique, numérique, tourisme. Devis, relances, reporting. Audit gratuit en visio.",
        "h_auto": "Automatisation PME à Bordeaux : relation client et documents",
        "h_ia": "IA pour PME à Bordeaux : personnaliser sans déshumaniser",
        "h_agents": "Agent IA à Bordeaux : répondre aux clients et aux partenaires",
        "poles_title": "Les pôles d'activité de la métropole bordelaise",
        "poles": [
            ("Euratlantique et le quartier d'affaires", "Autour de la gare Saint-Jean, un quartier d'affaires en développement qui accueille sociétés de services et cabinets. Besoins courants : suivi de clients, devis, facturation."),
            ("Mérignac et l'aéronautique", "Autour de l'aéroport, des entreprises de l'aéronautique et de la défense et leurs sous-traitants, avec des documents techniques et des exigences de suivi proches de celles d'autres bassins industriels."),
            ("Pessac et l'enseignement supérieur", "Un grand campus universitaire et des laboratoires, entourés de jeunes entreprises. Gestion de projets, comptes rendus et suivi de financements y reviennent souvent."),
            ("Les chais et le négoce du vin", "Châteaux, négociants et courtiers gèrent des commandes à l'export, des documents d'expédition et des relations clients sur le long terme."),
        ],
        "scenario_title": "Exemple : un négociant et ses commandes à l'export",
        "scenario": "Exemple type. Un négociant en vins traite des commandes de clients français et étrangers. Chaque commande donne lieu à un devis, un bon de commande, des documents d'expédition et plusieurs relances de paiement.\n\n"
                    "Avec une automatisation :\n\n"
                    "1. la commande acceptée génère le bon de commande et la facture d'acompte ;\n2. les documents d'expédition sont préparés à partir des mêmes données ;\n"
                    "3. le suivi du paiement déclenche des relances échelonnées ;\n4. un tableau de bord montre les commandes en attente, par pays.",
        "sectors": {
            "recrutement": "Les cabinets de la métropole bordelaise gagnent du temps sur les relances candidats, la base de profils interrogeable et la planification des entretiens.",
            "auto": "Concessions et marchands de Gironde : qualification des leads, relances après essai et sourcing d'occasion, le tout relié à votre CRM.",
            "immo": "Bordeaux attire de nouveaux habitants et les contacts affluent : veille d'annonces, qualification et relances aident les agences à répondre au bon moment.",
        },
        "faq": [
            ("Pouvez-vous intervenir pour une entreprise de négoce ou de services à Bordeaux ?", "Oui. Devis, relances, suivi de commandes et reporting se retrouvent dans la plupart des secteurs ; l'audit gratuit sert à repérer les tâches les plus rentables."),
            ("L'IA peut-elle aider à gérer des clients à l'international ?", "Elle prépare des premières réponses dans plusieurs langues, résume les échanges et classe les demandes. Votre équipe relit ce qui engage l'entreprise avant l'envoi."),
            ("Un consultant en automatisation intervient-il sur place à Bordeaux ?", "L'audit et le suivi se font en visio. Un rendez-vous sur place dans la métropole peut être étudié selon le projet, notamment pour un atelier avec votre équipe."),
            ("L'automatisation change-t-elle la relation client dans le négoce ?", "Non, elle la protège : les tâches répétitives sont prises en charge, ce qui laisse du temps pour les échanges qui comptent, comme ceux avec vos clients historiques."),
        ],
        "cta_title": "Un flux de commandes à fluidifier à Bordeaux ?",
        "cta_text": "Racontez-nous comment une commande circule dans votre entreprise. En 30 minutes d'audit gratuit, on repère où elle ralentit.",
    },
    "nantes": {
        "tagline": "Numérique, industrie et services",
        "lede": "À Nantes, l'écosystème numérique, l'industrie et les services forment un tissu d'entreprises déjà à l'aise avec les outils en ligne. Croisia, agence "
                "d'automatisation et d'IA, relie ces outils entre eux pour que l'information circule sans ressaisie.",
        "desc": "Agence d'automatisation et d'IA pour PME à Nantes : numérique, industrie, services. Relier vos outils en ligne, agents IA. Audit gratuit en visio.",
        "h_auto": "Automatisation PME à Nantes : relier une pile d'outils en ligne",
        "h_ia": "IA pour PME à Nantes : brancher l'IA sur ce qui existe",
        "h_agents": "Agent IA à Nantes : s'intégrer à votre pile d'outils",
        "poles_title": "Les quartiers et parcs d'activité nantais",
        "poles": [
            ("L'Île de Nantes et le Quartier de la Création", "Un quartier dédié aux industries culturelles et créatives et au numérique, où se côtoient agences, studios et jeunes entreprises. Facturation par projet, suivi de clients et gestion de prestataires y sont au cœur du quotidien."),
            ("EuroNantes et les services", "Le quartier d'affaires proche de la gare : cabinets, sociétés de conseil et services aux entreprises, avec un besoin constant de relances et de reporting."),
            ("Saint-Herblain, Carquefou et les parcs d'activité", "À l'ouest et à l'est de la métropole, des parcs d'entreprises accueillent PME industrielles et de services. Commandes, stocks et documents qualité y sont des sources de ressaisie."),
            ("Bouguenais et l'industrie technique", "Autour de plateformes technologiques comme le Technocampus, des entreprises de l'industrie, notamment en matériaux composites. Leur quotidien : documents techniques, suivi de projets et d'équipements."),
        ],
        "scenario_title": "Exemple : une agence digitale et ses projets clients",
        "scenario": "Exemple type. Une agence digitale de quinze personnes suit ses projets dans un outil de gestion, ses clients dans un CRM et ses factures dans un logiciel de facturation. Les trois ne communiquent pas.\n\n"
                    "Avec une automatisation :\n\n"
                    "- un projet signé crée la fiche client, le projet et l'échéancier de facturation ;\n- les temps passés remontent dans le tableau de bord de rentabilité ;\n"
                    "- les factures partent à l'échéance et les retards déclenchent une relance ;\n- un récapitulatif hebdomadaire arrive dans la messagerie de l'équipe.",
        "sectors": {
            "recrutement": "Les cabinets nantais, souvent spécialisés en tech et en industrie, gagnent du temps sur la double saisie dans l'ATS, les relances candidats et les comptes rendus d'entretien.",
            "auto": "Pour les concessions de l'agglomération, le suivi des leads, les relances clients et un CRM tenu à jour se font sans saisie supplémentaire pour les vendeurs.",
            "immo": "Agences et chasseurs nantais : veille d'annonces, qualification des contacts et rédaction d'annonces assistée, relue par l'agent.",
        },
        "faq": [
            ("Notre équipe utilise déjà beaucoup d'outils en ligne : est-ce un avantage ?", "Oui. Plus vos outils proposent d'API et d'intégrations, plus on peut les relier simplement avec Make ou n8n, sans développement lourd."),
            ("Une agence créative peut-elle vraiment automatiser son suivi de projets ?", "Oui : la création de projets, le suivi des temps, la facturation par jalons et les récapitulatifs sont des flux très réguliers, donc bien adaptés."),
            ("Faut-il quitter nos outils pour que ça marche ?", "Non, on les garde. L'objectif est de faire circuler l'information entre eux, pas de tout migrer."),
            ("Un consultant en automatisation peut-il venir à Nantes ?", "L'audit et la mise en place se font en visio. Un atelier sur place dans la métropole peut être étudié selon le projet."),
        ],
        "cta_title": "Une pile d'outils à relier à Nantes ?",
        "cta_text": "Listez-nous les logiciels que vous utilisez. En 30 minutes d'audit gratuit, on repère les liaisons qui feront gagner le plus de temps.",
    },
    "lille": {
        "tagline": "Distribution, e-commerce, logistique et services",
        "lede": "Lille et les Hauts-de-France sont un carrefour de la distribution, du commerce en ligne, de la logistique et des services, avec un grand volume de commandes "
                "à traiter. Croisia, agence d'automatisation et d'IA, aide les PME à absorber ce volume sans alourdir leurs équipes.",
        "desc": "Agence d'automatisation et d'IA pour PME à Lille : distribution, e-commerce, logistique, services. Commandes, livraisons, relances. Audit gratuit.",
        "h_auto": "Automatisation PME à Lille : encaisser le volume sans embaucher",
        "h_ia": "IA pour PME à Lille : comprendre des demandes mal formulées",
        "h_agents": "Agent IA à Lille : la première ligne des commandes et livraisons",
        "poles_title": "Les pôles d'activité de la métropole lilloise",
        "poles": [
            ("Euralille et le tertiaire", "Le quartier d'affaires autour des gares réunit services, conseil et assurances. Les PME partenaires y gèrent surtout des devis, des relances et du reporting."),
            ("EuraTechnologies et le numérique", "Un pôle consacré aux entreprises du numérique, à proximité du centre. Support client, facturation d'abonnements et suivi des prospects y reviennent sans cesse."),
            ("Roubaix, Tourcoing et la vente à distance", "Ancien territoire textile devenu terre de distribution et de vente à distance : commandes, retours, service client et gestion des stocks mobilisent beaucoup de temps."),
            ("Lesquin, Villeneuve-d'Ascq et la logistique", "Autour de l'aéroport, des campus et des zones d'activité, des entreprises de transport, de logistique et de services avec de forts volumes de livraisons à suivre."),
        ],
        "scenario_title": "Exemple : un e-commerçant et ses retours clients",
        "scenario": "Exemple type. Une PME de vente en ligne reçoit chaque jour des emails de clients : où est ma commande, je veux retourner mon colis, ma commande est incomplète. Trois personnes y répondent à la main.\n\n"
                    "Avec un agent IA et une automatisation :\n\n"
                    "1. l'agent reconnaît le type de demande, même mal formulée ;\n2. il consulte l'état de la commande dans votre outil de gestion ;\n"
                    "3. il répond aux cas simples (suivi, procédure de retour) ;\n4. il transmet à un collaborateur les cas particuliers, avec le dossier déjà rassemblé.",
        "sectors": {
            "recrutement": "Les cabinets de la métropole lilloise gagnent du temps sur les relances candidats, la planification des entretiens et la facturation des placements.",
            "auto": "Dans une région de forte circulation et de nombreux échanges, concessions et marchands automatisent la veille d'annonces d'occasion, la qualification des leads et les relances.",
            "immo": "Agences lilloises : veille d'annonces, qualification des acquéreurs, suivi des vendeurs et rédaction assistée, reliés à votre CRM.",
        },
        "faq": [
            ("Pouvez-vous gérer un gros volume de demandes ou de commandes ?", "Oui, c'est là que l'automatisation rapporte le plus. On dimensionne les scénarios selon le volume et on prévoit des alertes en cas d'anomalie."),
            ("Un agent IA peut-il répondre sur l'état d'une commande ?", "Oui, s'il peut consulter votre outil de gestion. Il répond aux questions de suivi et transmet à un humain ce qu'il ne peut pas traiter."),
            ("Notre activité est saisonnière, est-ce un obstacle ?", "Au contraire : l'automatisation absorbe les pics (soldes, fêtes) sans recrutement temporaire pour les tâches répétitives."),
            ("Un consultant en automatisation se déplace-t-il à Lille ?", "L'audit se fait en visio. Un rendez-vous dans la métropole peut être étudié selon le projet."),
        ],
        "cta_title": "Un pic de commandes à absorber à Lille ?",
        "cta_text": "Dites-nous où vos équipes passent le plus de temps sur les commandes, les retours ou les relances. L'audit dure 30 minutes et reste gratuit.",
    },
    "nice": {
        "tagline": "Tourisme, services haut de gamme et Sophia Antipolis",
        "lede": "Sur la Côte d'Azur, le tourisme, l'immobilier, les services haut de gamme et le pôle technologique de Sophia Antipolis attirent une clientèle exigeante, souvent "
                "internationale. Croisia, agence d'automatisation et d'IA, aide les PME niçoises à répondre vite et bien, à toute heure.",
        "desc": "Agence d'automatisation et d'IA pour PME à Nice : tourisme, immobilier, Sophia Antipolis. Réponses rapides, multilingues, relances. Audit gratuit.",
        "h_auto": "Automatisation PME à Nice : réservations, rendez-vous et suivi",
        "h_ia": "IA pour PME à Nice : répondre dans plusieurs langues",
        "h_agents": "Agent IA à Nice : répondre à toute heure, même en pleine saison",
        "poles_title": "Les pôles d'activité de Nice et de la Côte d'Azur",
        "poles": [
            ("Nice Méridia et la plaine du Var", "Un nouveau quartier d'activité dans la plaine du Var, consacré à l'innovation et aux entreprises. Jeunes structures, facturation et suivi clients y demandent des processus simples dès le départ."),
            ("Sophia Antipolis et la technologie", "Le technopole voisin accueille des entreprises technologiques et de services, avec des équipes souvent internationales : support client, accueil des clients et facturation récurrente."),
            ("L'aéroport et le tourisme d'affaires", "L'aéroport de Nice est l'un des plus fréquentés de France et irrigue l'hôtellerie, l'événementiel et les services aux voyageurs. Réservations, devis événementiels et relances sont des tâches répétées toute l'année."),
            ("La Promenade, l'hôtellerie et la restauration", "Établissements, agences de location et commerces saisonniers : demandes de renseignements et de réservation à toute heure, en plusieurs langues."),
        ],
        "scenario_title": "Exemple : une agence de location saisonnière",
        "scenario": "Exemple type. Une agence de location saisonnière reçoit des demandes en français, en anglais et en italien, par son site, par email et par messagerie, souvent le soir et le week-end. Certaines demandes sont traitées avec deux jours de retard.\n\n"
                    "Avec un agent IA et une automatisation :\n\n"
                    "- l'agent répond immédiatement, dans la langue du voyageur, et vérifie les disponibilités dans votre calendrier ;\n- il propose un créneau de visite ou un devis, et prend les coordonnées ;\n"
                    "- la fiche arrive dans le CRM, avec un résumé en français pour l'équipe ;\n- une relance part si le voyageur n'a pas confirmé sous quarante-huit heures.",
        "sectors": {
            "recrutement": "Les cabinets de la Côte d'Azur gagnent du temps sur les relances candidats, la planification des entretiens et la prospection de nouveaux clients entreprises.",
            "auto": "Concessions et marchands de la région : qualification des leads, relances après essai et veille d'annonces d'occasion, reliées à votre CRM.",
            "immo": "Sur la Côte d'Azur, la clientèle est souvent internationale et attend des réponses rapides. Qualification des contacts, relances et rédaction d'annonces assistée y gagnent en réactivité.",
        },
        "faq": [
            ("L'IA peut-elle répondre à des clients étrangers ?", "Elle prépare des premières réponses dans plusieurs langues. Votre équipe relit ce qui engage l'entreprise avant l'envoi, notamment pour les tarifs et les conditions."),
            ("Comment gérer la haute saison sans embaucher ?", "En automatisant les demandes répétitives : disponibilités, informations pratiques, confirmation de réservation, relances. Les pics ne saturent plus l'équipe."),
            ("Pouvez-vous nous aider si notre activité est à Sophia Antipolis ?", "Oui, le travail se fait à distance et couvre l'ensemble de la Côte d'Azur, de Nice à Sophia Antipolis."),
            ("Un consultant en automatisation peut-il venir à Nice ?", "L'audit et le suivi se font en visio. Un rendez-vous sur place sur la Côte d'Azur peut être étudié selon le projet."),
        ],
        "cta_title": "Répondre plus vite à vos clients à Nice ?",
        "cta_text": "Racontez-nous comment arrivent vos demandes, et à quelle heure. L'audit est gratuit, en visio, sans engagement.",
    },
    "montpellier": {
        "tagline": "Numérique, santé, recherche et croissance",
        "lede": "Montpellier est une métropole jeune et en croissance, portée par le numérique, la santé, la recherche et l'agronomie. Croisia, agence d'automatisation et d'IA, aide "
                "les PME en développement à structurer leurs processus avant que l'administratif ne freine leur croissance.",
        "desc": "Agence d'automatisation et d'IA pour PME à Montpellier : numérique, santé, recherche, croissance rapide. Processus, facturation. Audit gratuit en visio.",
        "h_auto": "Automatisation PME à Montpellier : structurer avant de grossir",
        "h_ia": "IA pour PME à Montpellier : éviter d'embaucher pour de l'administratif",
        "h_agents": "Agent IA à Montpellier : le premier contact d'une structure en croissance",
        "poles_title": "Les parcs et pôles de la métropole montpelliéraine",
        "poles": [
            ("Parc Eurêka et Cap Alpha", "Des parcs d'entreprises tournés vers l'innovation et le numérique, au nord de la ville. Équipes jeunes, outils en ligne, besoins de facturation et de suivi clients qui évoluent vite."),
            ("Euromédecine et la santé", "Autour des hôpitaux et des facultés de santé, un pôle de médecine, de biotechnologies et de recherche. Documents, comptes rendus et suivi administratif y sont lourds."),
            ("Agropolis et la recherche agronomique", "Un grand pôle de recherche et d'enseignement en agronomie et environnement : projets, financements et partenariats à suivre, avec beaucoup de documents."),
            ("Odysseum et les commerces", "Au sud-est, un quartier de commerces et de loisirs. Réservations, ventes et relation client à gérer sur plusieurs canaux."),
        ],
        "scenario_title": "Exemple : une startup qui structure sa facturation",
        "scenario": "Exemple type. Une jeune entreprise du numérique de dix personnes vend des abonnements. Les factures sont préparées à la main chaque mois et les relances dépendent de la mémoire de l'un des associés.\n\n"
                    "Avec une automatisation :\n\n"
                    "1. un nouveau contrat signé crée le client et son échéancier ;\n2. les factures partent à chaque échéance, sans intervention ;\n"
                    "3. un impayé déclenche une relance échelonnée, puis une alerte à l'associé ;\n4. un tableau de bord suit le chiffre d'affaires récurrent.",
        "sectors": {
            "recrutement": "Les cabinets montpelliérains, souvent en croissance, gagnent du temps sur la double saisie dans l'ATS, les relances candidats et les comptes rendus d'entretien.",
            "auto": "Pour les concessions et marchands de la métropole, le suivi des leads, les relances et un CRM automatisé évitent de perdre des demandes en période d'affluence.",
            "immo": "Montpellier est une ville dynamique et le nombre de contacts augmente : veille d'annonces, qualification et aide à l'estimation, reliées à votre CRM.",
        },
        "faq": [
            ("À partir de quand automatiser, pour une entreprise qui grandit vite ?", "Dès que les mêmes tâches reviennent chaque semaine. Automatiser tôt évite de recruter pour de l'administratif et garde vos processus propres."),
            ("Pouvez-vous nous accompagner si nous sommes dans la santé ou la recherche ?", "Oui, avec des précautions adaptées : accès limités, hébergement défini avec vous et durées de conservation maîtrisées, surtout lorsque des données personnelles sont concernées."),
            ("Un petit budget suffit-il pour commencer ?", "On commence par un seul chantier court et visible, chiffré avant tout engagement. Le gain de temps estimé figure en face de chaque ligne du devis."),
            ("Un consultant en automatisation peut-il venir à Montpellier ?", "L'audit se fait en visio. Un rendez-vous dans la métropole peut être étudié selon le projet."),
        ],
        "cta_title": "Structurer vos processus à Montpellier ?",
        "cta_text": "Dites-nous ce qui devient pénible à mesure que vous grandissez. L'audit dure 30 minutes, il est gratuit et sans engagement.",
    },
    "strasbourg": {
        "tagline": "Institutions européennes, industrie et commerce transfrontalier",
        "lede": "Strasbourg abrite des institutions européennes, de l'industrie et un commerce transfrontalier avec l'Allemagne. Croisia, agence d'automatisation et d'IA, aide les PME "
                "strasbourgeoises à traiter des documents et des échanges en plusieurs langues sans y passer des heures.",
        "desc": "Agence d'automatisation et d'IA pour PME à Strasbourg : documents multilingues, commerce transfrontalier, industrie. Audit gratuit en visio.",
        "h_auto": "Automatisation PME à Strasbourg : des flux à cheval sur deux pays",
        "h_ia": "IA pour PME à Strasbourg : traduire, résumer, classer",
        "h_agents": "Agent IA à Strasbourg : répondre dans la langue du client",
        "poles_title": "Les pôles d'activité de Strasbourg et de l'Eurométropole",
        "poles": [
            ("Le quartier européen", "Parlement européen, Conseil de l'Europe et leur écosystème de prestataires, traducteurs, cabinets et agences. Documents multilingues et délais serrés y sont la norme."),
            ("Illkirch-Graffenstaden et l'innovation", "Un parc d'innovation consacré aux biotechnologies, à la santé et aux technologies, proche des laboratoires. Gestion documentaire, comptes rendus et suivi de projets y reviennent sans cesse."),
            ("Le port du Rhin et la logistique", "Le port de Strasbourg, grand port fluvial du Rhin, génère transport, logistique et négoce. Dossiers d'expédition, documents douaniers et relances sont à suivre."),
            ("Kehl et le commerce transfrontalier", "De l'autre côté du Rhin, en Allemagne, la ville de Kehl est à quelques minutes. Entreprises et indépendants travaillent des deux côtés, avec des devis, des factures et des échanges dans deux langues."),
        ],
        "scenario_title": "Exemple : un prestataire de traduction et ses devis",
        "scenario": "Exemple type. Un petit cabinet de traduction reçoit des demandes de devis en français, en allemand et en anglais, avec des documents en pièce jointe de formats très variés.\n\n"
                    "Avec une automatisation et de l'IA :\n\n"
                    "- l'email entrant crée la fiche dans le CRM ;\n- l'IA détecte la langue, le type de document et le volume approximatif ;\n"
                    "- un devis préliminaire est préparé à partir de vos tarifs, que le responsable valide ;\n- un rappel part si le client ne répond pas, dans sa langue.",
        "sectors": {
            "recrutement": "Les cabinets de la région, souvent à l'interface de plusieurs langues, gagnent du temps sur les relances candidats, la base de profils interrogeable et la planification d'entretiens.",
            "auto": "Concessions et marchands strasbourgeois : sourcing d'occasion, qualification des leads et relances clients, y compris pour des clients venus d'outre-Rhin.",
            "immo": "Agences et chasseurs de l'agglomération : veille d'annonces, qualification des contacts et suivi des mandats, reliés à votre CRM.",
        },
        "faq": [
            ("L'IA sait-elle traiter des documents en allemand ?", "Les modèles actuels lisent et résument bien plusieurs langues. On teste sur vos documents réels avant toute mise en service, et un humain valide ce qui compte."),
            ("Pouvez-vous gérer des devis et factures dans deux langues ?", "Oui : on prépare des modèles bilingues et l'automatisation choisit le bon selon le client. Les mentions et formats propres à chaque pays restent à valider avec votre comptable."),
            ("Travaillez-vous avec des entreprises proches de la frontière ?", "Le travail se fait à distance, la localisation n'a donc pas d'incidence. Les spécificités transfrontalières (TVA, mentions) restent à confirmer avec vos conseils."),
            ("Un consultant en automatisation peut-il venir à Strasbourg ?", "L'audit se fait en visio. Un rendez-vous dans l'Eurométropole peut être étudié selon le projet."),
        ],
        "cta_title": "Des flux multilingues à simplifier à Strasbourg ?",
        "cta_text": "Décrivez-nous les langues et les documents que votre équipe traite. L'audit est gratuit, en visio, sans engagement.",
    },
}
