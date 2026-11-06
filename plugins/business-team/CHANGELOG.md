# Changelog, business-team

Évolutions du plugin `business-team`. Sa version, dans `.claude-plugin/plugin.json`, suit la dernière version de ce fichier : le validateur fait une erreur si elles divergent.

## [Non publié]

## [0.2.0] - 2026-11-07

Décider s’il faut démarrer, renforcer, attendre ou abandonner une activité, en partant d’un brainstorm ou d’une étude déjà faits.

### Ajouté

- Agent `stratege` : pèse risques et potentiel, propose parades et tests peu coûteux, fixe conditions et critères d’arrêt, rend un verdict parmi quatre (démarrer, démarrer sous conditions, pas maintenant, abandonner). Lecture seule.
- Skill `etude-opportunite` : vérification du document de départ par l’Enquêteur, scénarios et sensibilité par le Comptable, Avocat du diable, Stratège, seconde passe de l’Avocat du diable sur le plan renforcé, texte de test de la demande en option. Deux modes, démarrer ou renforcer une activité existante. Ses deux cas de déclenchement sont dans `evals/`.

### Modifié

- `enqueteur` : mode vérification. Chaque affirmation d’un document fourni est classée confirmée, contredite, nuancée ou non trouvée, dans un tableau.
- `comptable` : trésorerie nécessaire, délai d’équilibre, analyse de sensibilité, chiffres réels distingués des projections.
- `avocat-du-diable` : relève les biais du document de départ, et sait repasser une fois sur un plan renforcé sans répéter sa première liste.
- `redacteur` : page ou post de test de la demande, avec un appel à l’action mesurable.
- `lancement-produit` 1.0.1 : renvoie vers `etude-opportunite` tant que la décision de lancer n’est pas prise.

## [0.1.0] - 2026-11-07

### Ajouté

- Quatre sous-agents, chacun limité à son métier par ses consignes et par ses outils :
  - `enqueteur` : recherche web, chaque fait sourcé, seul agent qui accède au web.
  - `redacteur` : fiches produit et posts, tutoiement, phrases courtes.
  - `comptable` : prix, coûts, marges, toujours en tableau. Bash lui sert uniquement à vérifier les calculs.
  - `avocat-du-diable` : liste sans ménagement ce qui peut échouer, sans proposer de solution. Lecture seule.
- Skill `lancement-produit` : enchaîne les quatre agents, de la recherche de marché à la liste des risques, et assemble leurs livrables sans les réécrire. Ses deux cas de déclenchement sont dans `evals/`.
