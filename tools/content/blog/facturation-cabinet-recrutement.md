---
title: Automatiser la facturation d'un cabinet de recrutement
description: Automatisation de la facturation d'un cabinet de recrutement : déclencher la facture à la validation du placement, honoraires, acomptes et relances.
segment: recrutement
related: automatiser-devis-factures, automatisation-ats, prospection-cabinet-recrutement
---
Dans un cabinet de recrutement, la facture est l'aboutissement de tout le travail. Pourtant, elle est souvent préparée à la main, longtemps après le placement, avec les risques d'oubli et de retard de trésorerie que cela suppose. L'**automatisation de la facturation d'un cabinet de recrutement** consiste à la déclencher au bon moment avec les bonnes informations.

## Les événements qui déclenchent une facture

Selon le contrat, la facturation intervient à des étapes différentes :

- **acompte** à la signature de la mission ;
- **facturation à l'avancement** (présentation de candidats, entretiens) ;
- **solde** à la validation du placement, ou à l'arrivée du candidat ;
- **facture de garantie ou d'ajustement** si besoin.

Dans l'ATS, ces événements correspondent à des changements de statut. Ils peuvent donc servir de déclencheur.

## Le scénario type

1. Le statut du placement passe à « validé » dans l'ATS.
2. Le système rassemble les informations utiles : client, poste, candidat placé, rémunération annuelle, taux d'honoraires.
3. Il **calcule le montant** selon les conditions du contrat.
4. Il crée la facture dans le logiciel de facturation.
5. Un **recruteur valide**, puis la facture est envoyée.
6. Le suivi du paiement et les [relances](/blog/automatiser-relances-clients/) prennent le relais.

## Les points qui comptent

- **Conditions contractuelles** : chaque client peut avoir un taux ou un barème différent. Ils doivent être stockés dans une source fiable (CRM ou ATS) et non dans la mémoire des consultants.
- **Validation humaine** : le montant d'une facture de placement est élevé, un contrôle avant envoi est raisonnable.
- **Cohérence des données** : si la rémunération saisie est fausse, la facture le sera. L'automatisation met en lumière la qualité de la saisie.
- **Obligations de facturation** : mentions légales et évolutions réglementaires restent gérées par votre logiciel de facturation. L'automatisation transporte les données, elle ne remplace pas ce cadre.

## Reporting et trésorerie

Une facturation reliée aux statuts permet aussi un **suivi du chiffre d'affaires** en temps réel : placements en cours, factures à émettre, impayés. Voir [l'automatisation du reporting](/blog/automatiser-reporting/).

## Pour approfondir

La logique générale est détaillée dans [automatiser les devis et factures](/blog/automatiser-devis-factures/). Pour l'appliquer à votre cabinet, voir nos solutions pour les [cabinets de recrutement](/recrutement/) et demandez l'[audit gratuit](/audit-gratuit/).
