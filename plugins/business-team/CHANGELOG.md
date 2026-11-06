# Changelog, business-team

Évolutions du plugin `business-team`. Sa version, dans `.claude-plugin/plugin.json`, suit la dernière version de ce fichier : le validateur fait une erreur si elles divergent.

## [Non publié]

## [0.1.0] - 2026-11-07

### Ajouté

- Quatre sous-agents, chacun limité à son métier par ses consignes et par ses outils :
  - `enqueteur` : recherche web, chaque fait sourcé, seul agent qui accède au web.
  - `redacteur` : fiches produit et posts, tutoiement, phrases courtes.
  - `comptable` : prix, coûts, marges, toujours en tableau. Bash lui sert uniquement à vérifier les calculs.
  - `avocat-du-diable` : liste sans ménagement ce qui peut échouer, sans proposer de solution. Lecture seule.
- Skill `lancement-produit` : enchaîne les quatre agents, de la recherche de marché à la liste des risques, et assemble leurs livrables sans les réécrire. Ses deux cas de déclenchement sont dans `evals/`.
