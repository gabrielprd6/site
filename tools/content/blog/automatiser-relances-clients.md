---
title: Automatiser les relances clients
description: Mettre en place des relances clients automatiques, dont la relance de facture impayée, avec un ton juste et un arrêt dès que le client répond.
segment: pme
related: automatiser-devis-factures, automatisation-emails, automatisation-crm
---
Relancer un devis resté sans réponse, rappeler une facture, reprendre contact avec un prospect : tout le monde sait que c'est utile, et presque tout le monde le fait trop peu. La raison est simple : c'est une tâche qui dépend de la mémoire. **Automatiser les relances clients** la sort de la mémoire pour la mettre dans un scénario.

## Les relances qui valent la peine d'être automatisées

- **Devis sans réponse** : un rappel poli quelques jours après l'envoi, puis un second plus tard.
- **Facture impayée** : une relance automatique avant l'échéance, puis après si le paiement n'arrive pas.
- **Prospect qui a téléchargé un document** ou demandé une démonstration, sans suite.
- **Rendez-vous à confirmer** : rappels la veille ou le matin même.
- **Avis client** : une demande envoyée quand la prestation est terminée.

## La relance de facture impayée, automatiquement

C'est le cas le plus demandé. Une **relance de facture impayée automatique** suit une logique simple :

1. un rappel courtois quelques jours **avant** l'échéance ;
2. une première relance le lendemain de l'échéance si rien n'est payé ;
3. une relance plus ferme après une à deux semaines, avec la facture en pièce jointe ;
4. au-delà, une alerte envoyée à un humain, qui décide de la suite (appel, courrier, procédure).

Le point crucial : le scénario **vérifie le paiement avant chaque envoi**. Rien n'est plus désagréable pour un client qui a payé que de recevoir une relance.

## Les règles qui évitent les maladresses

- **Arrêt automatique** dès que le client répond, signe ou paie.
- **Ton adapté** au type de client : un grand compte et un particulier ne reçoivent pas le même message.
- **Plages d'envoi raisonnables** : pas de relance un dimanche à 23 h.
- **Exceptions humaines** : on peut marquer un dossier « ne pas relancer » (litige, geste commercial en cours).

## Comment c'est construit

Le scénario lit l'état des devis ou factures dans votre logiciel de facturation ou votre CRM, applique les règles de délai et prépare l'email. Selon votre préférence, il l'envoie directement ou le soumet à validation. Il consigne chaque envoi dans la fiche client, pour que toute l'équipe sache ce qui a été fait.

Un [agent IA](/agents-ia/) peut ensuite lire les réponses : confirmer un paiement annoncé, repérer une contestation, router un message vers la bonne personne.

## Par où commencer

Choisissez **une seule** relance, celle qui vous coûte le plus (souvent la facture impayée ou le devis sans réponse), et mesurez avant et après. Pour voir ce que ça donne chez vous, demandez l'[audit gratuit](/audit-gratuit/).
