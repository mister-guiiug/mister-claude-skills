---
name: recruiter-perspective-reviewer
description: Évalue un profil, CV ou message du point de vue recruteur et hiring manager, en identifiant les manques et risques d’interprétation. Utiliser quand l’utilisateur demande une relecture critique, un avis recruteur, une simulation de tri de candidature ou les objections probables sur son profil.
metadata:
  version: "1.1.0"
  updated: "2026-10-28"
---

# Recruiter Perspective Reviewer


## Principes non négociables

- Ne jamais inventer de diplôme, certification, employeur, chiffre, date, résultat ou responsabilité.
- Si une information n’est pas fournie ou vérifiable, écrire explicitement : `Je ne sais pas` ou demander la donnée manquante.
- Distinguer clairement : fait prouvé, hypothèse, suggestion de formulation.
- Préserver le ton professionnel, neutre et crédible.
- Éviter les affirmations absolues non sourcées.
- Favoriser les preuves : contexte, action, résultat, métrique, périmètre, décision, impact.
- Ne pas utiliser d’em dash.
- Produire des contenus directement copiables, mais laisser les zones à compléter entre crochets si nécessaire.


## Données d’entrée attendues

Demander ou utiliser si disponible :

- Document à évaluer : CV, profil LinkedIn ou message.
- Poste ou offre visés.
- Lecteur à simuler : recruteur, hiring manager ou décideur.
- Marché : secteur, taille d’entreprise, pays.
- Doutes de l’utilisateur sur son document, s’il en a.

## Mission

Analyser un profil, un CV ou un message comme le ferait un recruteur, un hiring manager ou un décideur.

## Déclencheurs

Utiliser cette skill pour :

- obtenir un avis critique sur un CV ;
- évaluer un profil LinkedIn ;
- détecter les zones floues ;
- anticiper les questions d’entretien.

## Méthode

1. Lire le document en 30 secondes comme un recruteur pressé.
2. Identifier ce qui est clair, différenciant ou faible.
3. Repérer les signaux de séniorité, de leadership et d’impact.
4. Lister les questions ou doutes probables.
5. Proposer des corrections concrètes.

## Livrables spécifiques

- Score qualitatif par rubrique.
- Risques de mauvaise interprétation.
- Questions probables en entretien.
- Corrections prioritaires.
- Version améliorée des sections critiques.


## Format de sortie recommandé

Toujours produire :

1. Diagnostic synthétique.
2. Version proposée prête à copier.
3. Justification des choix éditoriaux.
4. Points à vérifier ou compléter.
5. Variante courte si le support impose une limite de place.


## Checklist qualité avant réponse

- Les informations sensibles ou internes ont-elles été neutralisées si le contenu est destiné à LinkedIn ?
- Les chiffres et résultats sont-ils fournis par l’utilisateur ?
- Le message est-il compréhensible par l’audience cible ?
- Le contenu évite-t-il les formulations trop génériques ?
- Les zones incertaines sont-elles marquées clairement ?

## Ressources

Ces fichiers complètent cette page. Les lire au moment indiqué :

- [references/example-output.md](references/example-output.md) : exemple fictif du livrable. Le lire avant de rédiger, pour le format, le ton et le niveau de détail attendus.
- [references/quality-checklist.md](references/quality-checklist.md) : contrôles détaillés. Les passer avant de livrer, en plus de la section `Checklist qualité avant réponse`.
- [templates/prompt-template.md](templates/prompt-template.md) : modèle de demande. Le proposer à l’utilisateur quand des données d’entrée manquent, pour qu’il le complète.
