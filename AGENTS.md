# Instructions projet pour les agents

Ce dépôt est une place de marché de deux plugins Claude Code :

- `career-skills` : skills dédiées à l’optimisation LinkedIn, CV, personal branding et contenu professionnel.
- `business-team` : quatre sous-agents et une skill pour lancer un produit.

## Règles générales

- Ne jamais inventer d’information.
- Si une donnée manque, écrire `Je ne sais pas` ou `[à compléter]`.
- Préserver la confidentialité des informations internes.
- Toujours proposer une version directement copiable.
- Préférer un ton professionnel, sobre et factuel.
- Ne pas utiliser d’em dash.

Exception voulue : l’agent `redacteur` de `business-team` écrit au tutoiement et en phrases courtes, et l’agent `avocat-du-diable` s’exprime sans ménagement. Ne pas les ramener au ton professionnel et sobre.

## Usage recommandé

Quand une demande concerne LinkedIn, CV, carrière, personal branding, conférence ou contenu professionnel, sélectionner la skill la plus spécifique dans `plugins/career-skills/skills`.

Quand une demande concerne le lancement d’un produit, confier chaque tâche à l’agent de `plugins/business-team/agents` dont c’est le métier, ou passer par la skill `lancement-produit` pour les enchaîner.

Pour les avoir en travaillant dans ce dépôt, installer les plugins depuis la copie locale : `/plugin marketplace add ./`, puis `/plugin install career-skills@mister-guiiug` et `/plugin install business-team@mister-guiiug`.
