# Claude Skills - LinkedIn, CV et Personal Branding

Ce dépôt fournit une structure complète de skills Claude pour améliorer un CV, un profil LinkedIn, la préparation de contenus professionnels et la mise en avant d’un profil senior IT / architecture.

## Structure

```text
.claude-plugin/marketplace.json        place de marché Claude Code
plugins/
  career-skills/
    .claude-plugin/plugin.json         le plugin, sa version
    skills/
      <nom-de-la-skill>/
        SKILL.md
        references/quality-checklist.md
        references/example-output.md
        templates/prompt-template.md
    evals/                             tests de déclenchement
docs/
examples/
scripts/
.github/workflows/
```

19 skills, chacune autonome et copiable seule.

## Installation

### Option 1 - Plugin Claude Code, conseillé

Dans Claude Code :

```text
/plugin marketplace add mister-guiiug/mister-claude-skills
/plugin install career-skills@mister-guiiug
```

Claude choisit la skill d’après sa description. Pour en appeler une explicitement, la préfixer du nom du plugin, par exemple `/career-skills:cv-optimizer`. Une nouvelle version du plugin arrive avec chaque version de ce dépôt, voir [CHANGELOG.md](CHANGELOG.md).

### Option 2 - Dépôt projet Claude Code

Copier le dossier `plugins/career-skills/skills` dans le dossier `.claude/skills` du dépôt où Claude Code est utilisé.

### Option 3 - Installation utilisateur, sans plugin

Script d’installation, macOS et Linux :

```bash
bash scripts/install.sh
```

Script d’installation, Windows :

```bash
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
```

Les deux scripts remplacent toute skill du même nom déjà présente dans le dossier cible. Ne pas les combiner avec le plugin : les skills seraient en double.

Installation manuelle :

```bash
mkdir -p ~/.claude/skills
cp -R plugins/career-skills/skills/* ~/.claude/skills/
```

Sur Windows, `~/.claude` correspond généralement à `%USERPROFILE%\.claude`.

### Hors de Claude Code

Chaque dossier de skill est aussi importable sur claude.ai ou par l’API Skills : son frontmatter n’utilise que les clés qu’ils acceptent (`name`, `description`, `metadata`), ce que le validateur contrôle.

## Utilisation

Exemple de demande :

```text
Utilise la skill linkedin-profile-optimizer.
Voici mon profil LinkedIn actuel : [...]
Objectif : me positionner comme Enterprise Architect / Lead Integration Architect.
Contraintes : ne rien inventer, marquer les informations manquantes.
```

En cas de doute sur la skill à utiliser, passer par le routeur :

```text
Utilise la skill career-skills-router.
Je veux être plus visible dans mon domaine, je ne sais pas par où commencer.
```

## Tester le déclenchement

Claude choisit une skill d’après sa seule description. `plugins/career-skills/evals/` contient, pour chaque skill, une demande qui doit la déclencher (`<skill>-oui`) et une demande voisine, qui relève d’une autre skill, et ne doit pas la déclencher (`<skill>-non`). Les deux cas de `career-skills-router` mesurent en plus s’il capte une demande précise qui devrait aller directement à une skill.

```bash
claude plugin eval ./plugins/career-skills --ablation none --threshold 0.8
```

Il faut Claude Code 2.1.269 ou plus. Chaque cas est joué trois fois, chaque fois dans une vraie session : la suite complète en ouvre 114. La lancer après une modification de description, pas à chaque commit. Le rapport s’écrit dans `plugins/career-skills/evals/results/`.

## Skills incluses

### Orientation

| Skill                  | Usage                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| `career-skills-router` | Oriente vers la bonne skill et propose l’enchaînement de travail |

### Candidature et recrutement

| Skill                            | Usage                                                         |
| -------------------------------- | ------------------------------------------------------------- |
| `achievement-extractor`          | Transforme des notes de projet en réalisations mesurables     |
| `cv-optimizer`                   | Adapte un CV à un rôle cible, ATS compris                     |
| `recruiter-perspective-reviewer` | Relecture du point de vue recruteur et hiring manager         |
| `interview-preparation`          | Réponses, récits STAR à l’oral, objections, questions à poser |
| `salary-negotiation`             | Package, argumentaire, fourchette, scénarios de réponse       |

### Présence professionnelle

| Skill                           | Usage                                              |
| ------------------------------- | -------------------------------------------------- |
| `linkedin-pdf-profile-audit`    | Audit complet du profil à partir de son export PDF |
| `linkedin-profile-optimizer`    | Headline, About, expériences, compétences          |
| `linkedin-profile-photo-prompt` | Prompts de photo de profil et de bannière          |
| `executive-personal-branding`   | Positionnement et proposition de valeur            |
| `networking-outreach`           | Messages d’approche, relances, remerciements       |

### Contenu et prise de parole

| Skill                              | Usage                                     |
| ---------------------------------- | ----------------------------------------- |
| `thought-leadership-generator`     | Angles de contenu et calendrier éditorial |
| `executive-content-writer`         | Rédaction finale, posts, notes, messages  |
| `architecture-storytelling-expert` | Récit de projet d’architecture            |
| `call-for-papers-responder`        | Candidature à un appel à conférenciers    |
| `conference-speaker-coach`         | Préparation du talk, trame, biographie    |

### Expertise et trajectoire

| Skill                         | Usage                                              |
| ----------------------------- | -------------------------------------------------- |
| `it-architect-career-advisor` | Trajectoire d’architecte, options et contreparties |
| `technology-watch`            | Note de veille, radar technologique                |
| `ai-governance`               | Cadre de gouvernance IA, rôles, risques, contrôles |

## Tooling

| Commande                                                       | Usage                                                                                  |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `python scripts/validate_structure.py`                         | Valide frontmatter, nommage, version, sections, fichiers annexes et règle sans em dash |
| `python scripts/validate_structure.py --strict`                | Même validation, les avertissements deviennent bloquants                               |
| `python scripts/new_skill.py <nom-kebab-case>`                 | Crée le squelette complet d’une nouvelle skill                                         |
| `claude plugin validate . --strict`                            | Valide la place de marché, rejoué en CI                                                |
| `claude plugin validate plugins/career-skills --strict`        | Valide le plugin et ses skills, rejoué en CI                                           |
| `bash scripts/install.sh`                                      | Installe les skills dans `~/.claude/skills`                                            |
| `powershell -ExecutionPolicy Bypass -File scripts/install.ps1` | Installe les skills sous Windows                                                       |

La validation est rejouée automatiquement par GitHub Actions, voir `.github/workflows/validate.yml`.

## Principes de conception

- Chaque skill est autonome et copiable seule, aucune dépendance vers un fichier hors de son dossier.
- Chaque skill contient un `SKILL.md` avec frontmatter YAML, versionné.
- La `description` décrit ce que fait la skill et les cas de déclenchement, c’est le seul élément lu par Claude pour choisir la skill.
- Chaque skill fournit une checklist qualité spécifique à son domaine et un exemple de sortie fictif.
- Les ressources additionnelles sont rangées dans `references/` et `templates/`.
- Les instructions valorisent la précision, la confidentialité et l’absence d’invention.

Les conventions détaillées sont dans [docs/conventions.md](docs/conventions.md), l’historique dans [CHANGELOG.md](CHANGELOG.md).

## Sources utilisées pour la structure

- Anthropic, `anthropics/skills`, dépôt public de démonstration des Agent Skills : https://github.com/anthropics/skills
- Anthropic, `The Complete Guide to Building Skills for Claude`, guide indiquant qu’une skill contient un dossier avec `SKILL.md`, et éventuellement `scripts/`, `references/` et `assets/` : https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en
- Anthropic Claude Code Docs, `.claude` directory, documentation sur l’emplacement `.claude/skills` : https://code.claude.com/docs/en/claude-directory
- Anthropic Claude Code Docs, skills, fichiers annexes et frontmatter : https://code.claude.com/docs/en/skills
- Anthropic Claude Code Docs, création d’une place de marché de plugins : https://code.claude.com/docs/en/plugins/create-marketplace

## Avertissement

Ces skills sont des modèles opérationnels. Elles doivent être testées et adaptées à ton environnement, au niveau de confidentialité attendu et aux politiques internes avant usage sur des données sensibles.
