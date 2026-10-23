---
title: Éviter la double saisie dans l'ATS
description: Comment éviter la double saisie ATS : du CV reçu par mail à la fiche candidat, sans recopier. Les méthodes, leurs limites et la mise en place.
segment: recrutement
related: automatisation-ats, retrouver-anciens-candidats, automatiser-relances-candidats
---
Un CV arrive par mail. Le recruteur l'ouvre, le lit, puis recopie l'identité, le poste, les coordonnées dans l'ATS. Multipliez par plusieurs dizaines de candidatures par semaine : la **double saisie CV, mail et ATS** est l'un des plus gros consommateurs de temps d'un cabinet. Voici comment **éviter la double saisie dans l'ATS**.

## Où se produit la double saisie

- **CV reçu par email** puis recopié dans l'ATS.
- **Candidature d'un job board** à ressaisir parce que l'import est partiel.
- **Informations d'entretien** notées dans un document puis reprises dans la fiche.
- **Coordonnées du client** présentes à la fois dans l'ATS, le CRM et la facturation.

## Trois façons de supprimer la ressaisie

### 1. L'import natif de l'ATS

Beaucoup d'ATS savent lire un CV transmis à une adresse dédiée et créer la fiche. À essayer en premier : c'est gratuit.

### 2. L'automatisation par plateforme

Quand l'import natif est limité, une plateforme comme [Make ou n8n](/automatisation-make-n8n/) joue les intermédiaires : l'email arrive, la pièce jointe est récupérée, les informations sont extraites, la fiche est créée ou mise à jour via l'API de l'ATS. Voir [l'intégration ATS avec Make ou n8n](/blog/automatisation-ats/).

### 3. L'extraction par IA

Un CV n'a pas de format fixe. Un modèle d'IA lit le document, quelle que soit sa présentation, et en extrait les champs : identité, expériences, compétences, langues, formation. Le recruteur vérifie en un coup d'œil, au lieu de saisir.

## Les précautions

- **Doublons** : avant de créer une fiche, le système cherche si le candidat existe déjà (par email, par nom).
- **Qualité de l'extraction** : un échantillon de CV réels sert à vérifier avant la mise en service. Une alerte signale les documents illisibles.
- **Données personnelles** : le CV contient des données personnelles. Il faut limiter les accès, définir une durée de conservation et choisir des outils adaptés. Voir [IA en recrutement et RGPD](/blog/ia-recrutement-rgpd/).
- **L'ATS doit offrir une API** ou un point d'entrée par email ou fichier. Sinon, il faut envisager d'autres approches.

## Mettre en place

1. Cartographier où arrivent les candidatures (mail, job boards, site, cooptation).
2. Choisir l'ATS comme référence unique.
3. Automatiser d'abord la source la plus volumineuse.
4. Mesurer le temps gagné par candidature.

Vous voulez vérifier ce qui est possible avec votre ATS ? L'[audit gratuit](/audit-gratuit/) permet d'examiner ses possibilités d'intégration. Retrouvez aussi notre offre pour les [cabinets de recrutement](/recrutement/).
