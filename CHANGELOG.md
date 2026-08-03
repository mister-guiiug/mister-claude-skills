# Changelog

Toutes les évolutions notables de ce dépôt. Le format suit une logique proche de Keep a Changelog. Chaque skill porte sa propre version dans le frontmatter de son `SKILL.md`.

## [Non publié]

## [0.4.2] - 2026-08-03

### Modifié

- `linkedin-pdf-profile-audit` passe en version 1.1.1, après un second test sur le même export.
  - Règle de repli quand le persona n’est pas déclaré. `Accompagnement` par défaut, annoncé explicitement, avec l’indication de ce que le livrable deviendrait en évaluation de candidature. `Auto-audit` n’est jamais retenu par défaut, rien ne permet de supposer que le profil est celui de l’utilisateur.
  - Section `Contrôles de cohérence entre blocs`, six contrôles croisés. Une langue citée en compétence doit figurer dans le bloc `Langues` avec un niveau, un outil déclaré doit apparaître dans une expérience, une certification citée dans une expérience doit figurer dans le bloc dédié, une formation chevauchant un emploi doit être expliquée.
  - Ligne correspondante dans la grille d’audit et dans les deux checklists.

  Ces contrôles répondent à un défaut trouvé en test et invisible bloc par bloc, une langue déclarée en compétence alors que la section `Langues` est vide, donc non indexée par les filtres recruteur.

## [0.4.1] - 2026-08-03

### Modifié

- `linkedin-pdf-profile-audit` passe en version 1.1.0, après un premier test sur un export réel.
  - Section `Personas et adaptation du livrable`. La skill n’est plus centrée sur le profil de l’utilisateur. Quatre cas, auto-audit, accompagnement, évaluation de candidature et comparaison, chacun avec son livrable. Aucune reformulation n’est produite en évaluation de candidature.
  - Section `Structure de l’export, format fixe`, avec les deux zones, les libellés français et anglais de chaque bloc et l’ordre des champs d’une expérience.
  - Deux règles de lecture tirées du format fixe. Un bloc n’apparaît que s’il a du contenu, donc son absence sur une extraction complète est un constat de section vide, pas un angle mort. L’ordre stable des blocs permet de confirmer une absence.
  - Section `Contrôle de complétude de l’extraction`, cinq vérifications à faire avant tout constat d’absence.
  - Points techniques d’extraction ajoutés dans `pdf-export-map.md`, séparation des deux colonnes par coordonnées, polices sous-ensembles à identifiants de glyphes, flux compressés multiples.
  - Correction, l’URL du profil figure dans le bloc `Coordonnées` et n’est donc pas un angle mort, contrairement à ce qu’indiquait la version 1.0.0.

## [0.4.0] - 2026-08-03

### Ajouté

- Skill `linkedin-pdf-profile-audit`, audit complet d’un profil LinkedIn à partir de son export PDF.
  - Section `Ce que l’export PDF ne montre pas`, déclarée avant toute conclusion. L’export omet la photo, la bannière, la section Sélection, les recommandations, l’activité, les compétences au delà des premières et l’URL personnalisée.
  - Grille d’audit couvrant 10 sections, du titre aux coordonnées, avec les défauts fréquents associés.
  - Grille de priorisation P1 à P4 sur deux axes, effet sur la décision et effort de correction, avec un plafond de cinq P1.
  - Reconstitution de chronologie, trous et chevauchements signalés comme constats et jamais interprétés.
  - Reformulations en avant et après pour toutes les priorités P1 et P2.
  - `references/pdf-export-map.md`, contenu et omissions de l’export, limites d’extraction et signaux à repérer en priorité.

### Modifié

- Délimitation explicite entre `linkedin-pdf-profile-audit` et `linkedin-profile-optimizer`, ajoutée dans les deux skills, dans `career-skills-router`, dans le README et dans le guide d’usage. L’audit diagnostique et priorise, l’optimizer réécrit une section une fois la priorité connue.

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
