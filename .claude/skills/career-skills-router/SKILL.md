---
name: career-skills-router
version: 1.0.0
updated: 2026-08-03
description: Oriente une demande carrière, LinkedIn, CV ou personal branding vers la ou les skills adaptées du dépôt, et propose l’enchaînement de travail. Utiliser quand la demande couvre plusieurs sujets, quand l’utilisateur ne sait pas par où commencer, quand il demande quelle skill utiliser, ou quand aucune skill spécifique ne s’impose clairement.
---

# Career Skills Router

## Principes non négociables

- Ne pas produire le livrable final à la place de la skill spécialisée, sauf demande explicite de l’utilisateur.
- Ne jamais inventer d’information sur le profil de l’utilisateur pour justifier une orientation.
- Poser au maximum deux questions avant d’orienter, l’objectif est de débloquer, pas d’interroger.
- Si la demande correspond clairement à une seule skill, l’annoncer et enchaîner directement.
- Ne pas utiliser d’em dash.

## Données d’entrée attendues

Demander ou utiliser si disponible :

- Objectif réel derrière la demande : trouver un poste, gagner en visibilité, préparer une prise de parole, cadrer une pratique.
- Échéance : immédiate, quelques semaines, démarche de fond.
- Matériel déjà disponible : CV, profil LinkedIn, notes de projet, offre cible.

## Mission

Identifier la skill la plus adaptée à une demande carrière, proposer l’enchaînement de skills quand le besoin est composite, et éviter que l’utilisateur passe par une skill trop générale.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur :

- demande quelle skill utiliser ;
- formule un besoin large du type `aide moi sur ma carrière` ou `je veux être plus visible` ;
- présente un besoin qui couvre plusieurs livrables, par exemple CV, LinkedIn et entretien ;
- hésite entre deux approches.

## Méthode

1. Identifier l’objectif final, pas le livrable demandé. Un utilisateur qui demande un post LinkedIn cherche parfois un poste.
2. Identifier l’horizon de temps, il détermine s’il faut un livrable rapide ou une démarche de fond.
3. Vérifier le matériel disponible, une skill de réécriture sans matière produit du vide.
4. Orienter vers une skill unique si le besoin est net, vers un enchaînement si le besoin est composite.
5. Annoncer l’enchaînement complet dès le départ, puis démarrer par la première étape.
6. Rappeler la matière à préparer pour les étapes suivantes.

## Table d’orientation

| Besoin exprimé | Skill |
| --- | --- |
| Auditer tout le profil à partir de son export PDF | `linkedin-pdf-profile-audit` |
| Réécrire headline, About, expériences LinkedIn | `linkedin-profile-optimizer` |
| Photo de profil, bannière, identité visuelle | `linkedin-profile-photo-prompt` |
| CV, adaptation à une offre, ATS | `cv-optimizer` |
| Transformer des notes de projet en réalisations chiffrées | `achievement-extractor` |
| Savoir ce que voit un recruteur, relecture critique | `recruiter-perspective-reviewer` |
| Préparer un entretien, questions probables, STAR à l’oral | `interview-preparation` |
| Discuter salaire, package, contre-offre | `salary-negotiation` |
| Message de mise en relation, approche, relance | `networking-outreach` |
| Positionnement, différenciation, pitch personnel | `executive-personal-branding` |
| Idées de posts, angles, calendrier éditorial | `thought-leadership-generator` |
| Rédiger un post, une newsletter, un message à un dirigeant | `executive-content-writer` |
| Raconter un projet d’architecture | `architecture-storytelling-expert` |
| Répondre à un appel à conférenciers | `call-for-papers-responder` |
| Préparer le contenu et la trame d’un talk, bio de speaker | `conference-speaker-coach` |
| Note de veille, radar technologique | `technology-watch` |
| Cadre de gouvernance IA, politique d’usage | `ai-governance` |
| Évolution de carrière, choix de trajectoire | `it-architect-career-advisor` |

## Enchaînements recommandés

| Objectif | Enchaînement |
| --- | --- |
| Recherche de poste complète | `achievement-extractor`, `cv-optimizer`, `linkedin-profile-optimizer`, `recruiter-perspective-reviewer`, `interview-preparation`, `salary-negotiation` |
| Refonte du profil LinkedIn | `linkedin-pdf-profile-audit`, `achievement-extractor`, `linkedin-profile-optimizer`, `linkedin-profile-photo-prompt`, `recruiter-perspective-reviewer` |
| Gagner en visibilité experte | `executive-personal-branding`, `technology-watch`, `thought-leadership-generator`, `executive-content-writer` |
| Prise de parole publique | `call-for-papers-responder`, `conference-speaker-coach`, `architecture-storytelling-expert` |
| Approche directe d’une entreprise | `networking-outreach`, `achievement-extractor`, `interview-preparation` |
| Cadrer une pratique interne | `technology-watch`, `ai-governance` |

## Règles de désambiguïsation

- `linkedin-pdf-profile-audit` diagnostique tout le profil et priorise, `linkedin-profile-optimizer` réécrit une section une fois la priorité connue. Si l’utilisateur dispose de son export PDF, commencer par l’audit.
- `achievement-extractor` produit la matière, `cv-optimizer` et `linkedin-profile-optimizer` la mettent en forme. En cas de doute, commencer par la matière.
- `thought-leadership-generator` produit des angles, `executive-content-writer` rédige le texte final.
- `call-for-papers-responder` traite la candidature à un événement, `conference-speaker-coach` traite la préparation du talk retenu.
- `executive-personal-branding` définit le positionnement, `linkedin-profile-optimizer` le traduit sur un support précis.
- `it-architect-career-advisor` traite la trajectoire, `interview-preparation` et `salary-negotiation` traitent une opportunité identifiée.

## Format de sortie recommandé

Toujours produire :

1. Reformulation de l’objectif réel en une phrase.
2. Skill retenue ou enchaînement proposé, avec justification courte.
3. Matière à réunir avant de démarrer.
4. Proposition de démarrer immédiatement la première étape.

## Checklist qualité avant réponse

- L’orientation repose-t-elle sur l’objectif final et non sur le livrable demandé ?
- L’enchaînement est-il ordonné de la matière vers la mise en forme ?
- Le nombre de questions posées reste-t-il inférieur ou égal à deux ?
- L’utilisateur sait-il quoi préparer pour l’étape suivante ?
