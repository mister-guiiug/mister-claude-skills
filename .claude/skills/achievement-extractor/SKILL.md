---
name: achievement-extractor
description: Transforme des expériences brutes en réalisations vérifiables, orientées impact, avec méthode STAR et métriques explicites. Utiliser quand l’utilisateur veut convertir des notes de projet en bullets de CV, quantifier des résultats, formuler des accomplissements ou préparer des exemples STAR pour un entretien.
metadata:
  version: "1.1.0"
  updated: "2026-10-28"
---

# Achievement Extractor


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

- Notes de projet, tâches ou responsabilités telles que l’utilisateur les décrit.
- Pour chaque projet : contexte, problème, action personnelle, résultat.
- Métriques disponibles et leur source : coût, délai, risque, qualité, adoption, disponibilité, performance.
- Périmètre et dates : taille d’équipe, budget, nombre d’applications ou d’utilisateurs, durée.
- Usage visé : CV, profil LinkedIn, entretien annuel ou entretien de recrutement.
- Rôle cible, si les réalisations doivent servir une candidature.

## Mission

Transformer des tâches, responsabilités ou projets en réalisations professionnelles solides, factuelles et vérifiables.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur veut :

- enrichir son CV ;
- préparer son entretien annuel ;
- valoriser ses résultats ;
- reformuler des expériences en achievements.

## Méthode

1. Collecter les faits : contexte, problème, action, résultat, métrique.
2. Appliquer la structure STAR : Situation, Task, Action, Result.
3. Identifier les métriques possibles : coût, délai, risque, qualité, adoption, disponibilité, performance.
4. Ne jamais inventer de métriques. Si elles manquent, proposer des questions pour les obtenir.
5. Réécrire sous forme de bullets orientées impact.

## Livrables spécifiques

- Liste de réalisations en format CV.
- Version LinkedIn plus narrative.
- Version entretien en STAR.
- Questions de clarification pour chiffrer l’impact.


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
