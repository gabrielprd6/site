---
title: Intégrer son ATS avec Make ou n8n
description: Intégration ATS et automatisation avec Make ou n8n : ce qu'on peut relier, les prérequis (API, webhooks), un exemple de scénario et les limites.
segment: recrutement
related: double-saisie-ats, t4s-automatisation, retrouver-anciens-candidats
---
Un ATS est le cœur d'un cabinet de recrutement, mais il fonctionne rarement seul : messagerie, agenda, job boards, facturation, outil de visio. Une **intégration ATS par automatisation avec Make ou n8n** relie ces éléments sans développement lourd.

## Ce qu'on peut relier à un ATS

- la **messagerie** : candidatures reçues, accusés de réception ;
- l'**agenda** : planification des entretiens ;
- les **job boards** : diffusion des offres, récupération des candidatures ;
- la **facturation** : facture créée à la validation d'un placement ;
- le **CRM** ou le suivi commercial ;
- les **outils d'IA** : extraction de CV, résumés, recherche ;
- la **messagerie d'équipe** : notifications d'événements importants.

## Les trois portes d'entrée

Selon l'ATS, l'accès aux données passe par :

1. **Une API** : le plus souple. On lit et écrit des candidats, des offres, des statuts.
2. **Des webhooks** : l'ATS prévient en temps réel quand quelque chose change.
3. **Des imports et exports** (fichiers, emails dédiés) : moins élégant, mais souvent suffisant.

Avant tout projet, on vérifie ce que votre ATS propose, et à quelles conditions (certains éditeurs réservent l'API à certaines formules).

## Exemple de scénario

> **Candidature reçue → fiche ATS → accusé de réception.**
> Un email arrive sur l'adresse du poste. Le scénario récupère le CV, une étape d'IA en extrait les champs, le système cherche si le candidat existe déjà, crée ou met à jour la fiche via l'API de l'ATS, puis envoie l'accusé de réception. Le recruteur n'a rien saisi.

## Make ou n8n pour un ATS ?

Les deux conviennent. **Make** est parfait si l'équipe veut suivre et modifier ses scénarios elle-même. **n8n** s'impose quand les flux sont complexes ou que l'on veut maîtriser l'hébergement des données, particulièrement pertinent avec des CV. Le détail est dans notre [comparatif](/blog/make-vs-n8n-vs-zapier/).

## Les limites à connaître

- **Pas d'API, pas de miracle** : sans point d'entrée, on peut devoir passer par des fichiers ou des emails.
- **Limites de débit** : l'ATS peut plafonner le nombre de requêtes.
- **Évolutions** : une mise à jour de l'ATS peut casser un scénario, d'où l'intérêt des alertes et d'un suivi.
- **Données personnelles** : voir [IA en recrutement et RGPD](/blog/ia-recrutement-rgpd/).

## Par où commencer

Choisissez un flux simple et fréquent, comme les candidatures par email, et mesurez le temps gagné. Pour vérifier ce qui est faisable avec votre outil, c'est l'[audit gratuit](/audit-gratuit/). Notre offre complète est sur la page [cabinets de recrutement](/recrutement/).
