# Changelog, business-team

Évolutions du plugin `business-team`. Sa version, dans `.claude-plugin/plugin.json`, suit la dernière version de ce fichier : le validateur fait une erreur si elles divergent.

## [Non publié]

## [0.1.0] - 2026-11-07

### Ajouté

- Cinq sous-agents, chacun limité à son métier par ses consignes et par ses outils :
  - `enqueteur` : recherche web, chaque fait sourcé, seul agent qui accède au web. Vérifie aussi, ligne à ligne, les affirmations d’un brainstorm ou d’une étude existants.
  - `comptable` : prix, coûts, marges, scénarios, trésorerie et analyse de sensibilité, toujours en tableau. Bash lui sert uniquement à vérifier les calculs.
  - `avocat-du-diable` : liste sans ménagement ce qui peut échouer, sans proposer de solution, y compris les biais du document de départ. Repasse une fois sur un plan renforcé. Lecture seule.
  - `stratege` : pèse risques et potentiel, propose parades et tests peu coûteux, fixe conditions et critères d’arrêt, rend un verdict parmi quatre. Lecture seule.
  - `redacteur` : fiches produit, posts et textes de test de la demande, tutoiement, phrases courtes.
- Skill `etude-opportunite` : décide s’il faut démarrer, renforcer, attendre ou abandonner une activité. Vérifie d’abord les recherches déjà faites, puis enchaîne Comptable, Avocat du diable, Stratège et une seconde passe de l’Avocat du diable.
- Skill `lancement-produit` : une fois la décision prise, enchaîne Enquêteur, Comptable, Rédacteur et Avocat du diable, et assemble leurs livrables sans les réécrire.
- Deux cas de déclenchement par skill dans `evals/`.
