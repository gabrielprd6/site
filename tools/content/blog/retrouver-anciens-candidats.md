---
title: Retrouver d'anciens candidats dans votre base ATS
description: Retrouver d'anciens candidats dans une base ATS grâce à la recherche sémantique : principe, avantages sur les mots-clés et mise en place.
segment: recrutement
related: double-saisie-ats, ia-recrutement-rgpd, automatisation-ats
---
Votre ATS contient des milliers de profils déjà rencontrés, évalués et parfois même excellents. Pourtant, pour une nouvelle mission, on repart souvent d'une recherche sur les job boards. La raison : **retrouver d'anciens candidats dans la base ATS** est difficile avec une recherche par mots-clés.

## Pourquoi la recherche par mots-clés échoue

Elle ne trouve que ce qui est écrit exactement comme vous le cherchez. Un « responsable des achats » ne sera pas trouvé par « acheteur senior ». Un « développeur Python » ne remontera pas pour « ingénieur logiciel, backend ». Et les mots-clés ignorent le contexte : secteur, niveau, évolution de carrière.

## La recherche sémantique : le principe

La **recherche sémantique dans une base de candidats** compare le **sens** plutôt que les mots. Chaque profil est transformé en une représentation numérique de son contenu (par un modèle d'IA). Votre recherche l'est aussi. Le système renvoie les profils dont le sens se rapproche de votre demande.

Vous pouvez donc décrire le poste en langage naturel (« directeur commercial dans l'industrie, habitué à manager une équipe de dix personnes ») et obtenir des candidats pertinents, même s'ils n'emploient pas vos mots.

## Ce que ça permet

- **Réactiver** une base dormante pour de nouvelles missions.
- **Gagner en rapidité** sur un sourcing : une première liste en quelques secondes.
- **Aider les juniors** à bénéficier de la connaissance accumulée par le cabinet.
- **Mieux valoriser** le travail d'évaluation déjà fait.

## Comment on le met en place

1. **Récupérer les données** de l'ATS (CV, notes, statuts) via l'API, un export ou un flux automatisé.
2. **Indexer** les profils avec un modèle d'analyse du texte, dans une base adaptée à cette recherche.
3. **Brancher la recherche** : une interface simple, ou directement dans l'outil que vos équipes utilisent.
4. **Maintenir à jour** : chaque nouveau CV ou changement alimente l'index.

## Les points de vigilance

- **RGPD** : il faut une base légale, une information des candidats et des durées de conservation cohérentes. Les profils anciens ne peuvent pas être gardés indéfiniment. Voir [IA en recrutement et RGPD](/blog/ia-recrutement-rgpd/).
- **Explicabilité** : le système doit montrer pourquoi un profil est proposé, pour que le recruteur juge.
- **Décision humaine** : la recherche suggère, elle ne sélectionne pas.
- **Qualité des données** : des CV mal extraits donnent des résultats médiocres, d'où l'intérêt de l'[extraction à l'entrée](/blog/double-saisie-ats/).

## Résultat attendu

Une base qui travaille, au lieu de coûter en stockage. Pour étudier la faisabilité sur votre ATS, demandez l'[audit gratuit](/audit-gratuit/) ou découvrez notre offre pour les [cabinets de recrutement](/recrutement/).
