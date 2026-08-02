# Changelog

Toutes les évolutions notables de ce dépôt. Le format suit une logique proche de Keep a Changelog. Chaque skill porte sa propre version dans le frontmatter de son `SKILL.md`.

## [Non publié]

## [0.2.0] - 2026-08-03

### Ajouté

- Skill `career-skills-router`, oriente une demande vers la bonne skill et propose l’enchaînement de travail.
- Skill `interview-preparation`, préparation d’entretien, récits STAR à l’oral, objections, questions à poser.
- Skill `salary-negotiation`, négociation de package, argumentaire factuel, scénarios de réponse.
- Skill `networking-outreach`, messages de mise en relation, approche, relance, remerciement.
- Skill `call-for-papers-responder`, candidature à un appel à conférenciers de bout en bout.
- Un fichier `references/example-output.md` pour chacune des 18 skills, exemple fictif signalé comme tel.
- Champs `version` et `updated` dans le frontmatter de toutes les skills.
- Ce fichier CHANGELOG.

### Modifié

- Les 12 checklists qualité génériques sont spécialisées par domaine, plus aucune duplication entre skills.
- `scripts/validate_structure.py` contrôle désormais le format de `version` et `updated`, et la présence de `references/example-output.md`.
- `scripts/new_skill.py` génère le frontmatter versionné et un squelette d’exemple de sortie.
- README réorganisé par famille d’usage, guide d’usage complété avec les nouvelles skills.

## [0.1.0] - 2026-08-03

### Ajouté

- 12 skills initiales, LinkedIn, CV, personal branding, veille technologique et gouvernance IA.
- Skill `linkedin-profile-photo-prompt`, génération de prompts de photo de profil et de bannière LinkedIn.
- `scripts/validate_structure.py`, découverte automatique des skills et contrôle du frontmatter, du nommage, des sections et de la règle sans em dash.
- `scripts/new_skill.py`, scaffolder de skill.
- `scripts/install.sh` et `scripts/install.ps1`.
- Workflow GitHub Actions de validation.
- `docs/conventions.md` et `.gitattributes`.

### Corrigé

- Description de `ai-governance` contenant un deux-points suivi d’un espace, ce qui rendait le frontmatter YAML invalide et faisait ignorer la description.

### Modifié

- Descriptions des 12 skills initiales enrichies avec leurs conditions de déclenchement.
