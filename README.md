# Claude Skills - LinkedIn, CV et Personal Branding

Ce dépôt fournit une structure complète de skills Claude pour améliorer un CV, un profil LinkedIn, la préparation de contenus professionnels et la mise en avant d’un profil senior IT / architecture.

## Structure

```text
.claude/
  skills/
    <nom-de-la-skill>/
      SKILL.md
      references/quality-checklist.md
      references/example-output.md
      templates/prompt-template.md
docs/
examples/
scripts/
.github/workflows/
```

18 skills, chacune autonome et copiable seule.

## Installation

### Option 1 - Dépôt projet Claude Code

Copier le dossier `.claude/skills` dans le dépôt où Claude Code est utilisé.

### Option 2 - Installation utilisateur

Script d’installation, macOS et Linux :

```bash
bash scripts/install.sh
```

Script d’installation, Windows :

```bash
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
```

Installation manuelle :

```bash
mkdir -p ~/.claude/skills
cp -R .claude/skills/* ~/.claude/skills/
```

Sur Windows, `~/.claude` correspond généralement à `%USERPROFILE%\.claude`.

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

## Skills incluses

### Orientation

| Skill | Usage |
| --- | --- |
| `career-skills-router` | Oriente vers la bonne skill et propose l’enchaînement de travail |

### Candidature et recrutement

| Skill | Usage |
| --- | --- |
| `achievement-extractor` | Transforme des notes de projet en réalisations mesurables |
| `cv-optimizer` | Adapte un CV à un rôle cible, ATS compris |
| `recruiter-perspective-reviewer` | Relecture du point de vue recruteur et hiring manager |
| `interview-preparation` | Réponses, récits STAR à l’oral, objections, questions à poser |
| `salary-negotiation` | Package, argumentaire, fourchette, scénarios de réponse |

### Présence professionnelle

| Skill | Usage |
| --- | --- |
| `linkedin-profile-optimizer` | Headline, About, expériences, compétences |
| `linkedin-profile-photo-prompt` | Prompts de photo de profil et de bannière |
| `executive-personal-branding` | Positionnement et proposition de valeur |
| `networking-outreach` | Messages d’approche, relances, remerciements |

### Contenu et prise de parole

| Skill | Usage |
| --- | --- |
| `thought-leadership-generator` | Angles de contenu et calendrier éditorial |
| `executive-content-writer` | Rédaction finale, posts, notes, messages |
| `architecture-storytelling-expert` | Récit de projet d’architecture |
| `call-for-papers-responder` | Candidature à un appel à conférenciers |
| `conference-speaker-coach` | Préparation du talk, trame, biographie |

### Expertise et trajectoire

| Skill | Usage |
| --- | --- |
| `it-architect-career-advisor` | Trajectoire d’architecte, options et contreparties |
| `technology-watch` | Note de veille, radar technologique |
| `ai-governance` | Cadre de gouvernance IA, rôles, risques, contrôles |

## Tooling

| Commande | Usage |
| --- | --- |
| `python scripts/validate_structure.py` | Valide frontmatter, nommage, version, sections, fichiers annexes et règle sans em dash |
| `python scripts/validate_structure.py --strict` | Même validation, les avertissements deviennent bloquants |
| `python scripts/new_skill.py <nom-kebab-case>` | Crée le squelette complet d’une nouvelle skill |
| `bash scripts/install.sh` | Installe les skills dans `~/.claude/skills` |
| `powershell -File scripts/install.ps1` | Installe les skills sous Windows |

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

## Avertissement

Ces skills sont des modèles opérationnels. Elles doivent être testées et adaptées à ton environnement, au niveau de confidentialité attendu et aux politiques internes avant usage sur des données sensibles.
