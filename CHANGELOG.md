# Changelog

Toutes les évolutions notables de ce dépôt. Le format suit une logique proche de Keep a Changelog. Chaque skill porte sa propre version dans le frontmatter de son `SKILL.md`.

## [Non publié]

## [0.3.1] - 2026-08-03

### Modifié

- `linkedin-profile-photo-prompt` passe en version 1.2.1.
  - Nouveau principe non négociable en tête de liste, vérifier que le sujet de la photo est bien l’utilisateur. Sinon, demander l’identité de la personne et son accord, et se limiter à une analyse sans produire de prompt portant sur son visage.
  - Nouveau motif en tête du tri d’admissibilité, avec une décision `Suspendre` distincte de `Écarter`.
  - Indices de détection d’une photo exportée depuis un profil tiers, format 400 x 400 exact, nom de fichier horodaté, poids très faible, rendu studio isolé.
  - Ligne correspondante ajoutée aux deux checklists qualité.

  L’angle mort était le suivant. La règle sur les tiers ne couvrait que les personnes en arrière-plan d’une photo de l’utilisateur, pas le cas où le visage traité n’est pas le sien.

## [0.3.0] - 2026-08-03

### Modifié

- `linkedin-profile-photo-prompt` passe en version 1.2.0, après six tests sur photos réelles.
  - Étape `Tri d’admissibilité` en tête de méthode, tiers identifiables, tenue, contexte, nudité, avec motif d’écartement toujours explicite.
  - Étape `Diagnostic de la photo source`, séparant les défauts corrigeables des défauts non corrigeables.
  - Mode `Sélection parmi plusieurs photos`, avec grille comparative, règles de classement et annonce de la photo retenue.
  - `Échelle de fabrication` en cinq niveaux, du remplacement de fond à la génération de pose, avec le risque de rendu associé à chacun.
  - Section `Frontière entre correction et modification`, distinguant correction d’objectif, changement de tenue et modification d’apparence.
  - Mode de production `Reprise au téléphone`, protocole en 7 points, placé avant la retouche dans l’ordre de préférence.
  - `Contrôle de résolution` calculé sur le côté du recadrage carré, avec seuils et détection de recompression.
  - Principe non négociable sur les personnes tierces et le droit à l’image.
  - Bloc négatif consolidé et enrichi, angle de prise de vue, narines, plafond, peau mouillée, impression sur vêtement, défauts de col et de mains.
  - Templates de prompt par niveau de fabrication, avec le nombre de générations à prévoir pour chacun.
  - Exemple de sortie réécrit sur un cas à trois photos candidates.

### Ajouté

- `.gitignore`, exclusion des fichiers image à la racine, pour éviter de committer des photos personnelles utilisées lors des tests.

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
