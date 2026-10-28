---
name: linkedin-profile-optimizer
description: Optimise un profil LinkedIn pour clarifier le positionnement, améliorer la lisibilité recruteur et renforcer les mots-clés sans sur-promesse. Utiliser quand l’utilisateur veut réécrire son headline, sa section About, ses expériences LinkedIn, ses compétences ou améliorer sa visibilité auprès des recruteurs.
metadata:
  version: "1.1.0"
  updated: "2026-10-28"
---

# LinkedIn Profile Optimizer


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

- Profil actuel : headline, section About, expériences, compétences, section Featured.
- Rôle cible ou audiences visées.
- Mots-clés recherchés pour ce rôle, et 3 à 5 offres d’emploi d’exemple si disponibles.
- Réalisations vérifiables avec chiffres, dates, périmètre et outils.
- CV actuel, pour vérifier la cohérence entre les deux.
- Langue du profil et contraintes de ton.

## Mission

Améliorer un profil LinkedIn en travaillant le positionnement, la lisibilité, la crédibilité et la découvrabilité par recherche.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur demande :

- d’améliorer son profil LinkedIn ;
- de réécrire le titre, le résumé ou les expériences ;
- d’aligner son profil avec un rôle cible ;
- d’augmenter sa visibilité recruteur ou son positionnement expert.

## Délimitation avec les autres skills

Si l’utilisateur fournit l’export PDF de son profil ou demande un bilan d’ensemble, passer par `linkedin-pdf-profile-audit`. Cette skill travaille en profondeur une ou plusieurs sections, une fois la priorité connue.

## Méthode

1. Identifier le positionnement actuel : métier, séniorité, domaines d’expertise, différenciants.
2. Vérifier la cohérence entre titre, résumé, expériences, compétences et mots-clés.
3. Réécrire sans générer de claims invérifiables.
4. Prioriser les mots-clés métier naturels plutôt que le bourrage de mots-clés.
5. Proposer plusieurs variantes lorsque le profil vise plusieurs audiences.

## Livrables spécifiques

- Headline LinkedIn en 3 variantes : sobre, expert, exécutif.
- Section About en version courte et longue.
- Expériences réécrites en bullets orientées impact.
- Liste de skills LinkedIn à ajouter ou prioriser.
- Suggestions pour la section Featured.


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
