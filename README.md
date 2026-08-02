# Claude Skills - LinkedIn, CV et Personal Branding

Ce dépôt fournit une structure complète de skills Claude pour améliorer un CV, un profil LinkedIn, la préparation de contenus professionnels et la mise en avant d’un profil senior IT / architecture.

## Structure

```text
.claude/
  skills/
    linkedin-profile-optimizer/
      SKILL.md
      references/quality-checklist.md
      templates/prompt-template.md
    executive-personal-branding/
    achievement-extractor/
    thought-leadership-generator/
    architecture-storytelling-expert/
    conference-speaker-coach/
    cv-optimizer/
    executive-content-writer/
    recruiter-perspective-reviewer/
    it-architect-career-advisor/
    technology-watch/
    ai-governance/
    linkedin-profile-photo-prompt/
docs/
examples/
scripts/
.github/workflows/
```

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

## Skills incluses

1. LinkedIn Profile Optimizer
2. Executive Personal Branding
3. Achievement Extractor
4. Thought Leadership Generator
5. Architecture Storytelling Expert
6. Conference Speaker Coach
7. CV Optimizer
8. Executive Content Writer
9. Recruiter Perspective Reviewer
10. IT Architect Career Advisor
11. Technology Watch
12. AI Governance
13. LinkedIn Profile Photo Prompt

## Tooling

| Commande | Usage |
| --- | --- |
| `python scripts/validate_structure.py` | Valide frontmatter, nommage, sections, doublons et règle sans em dash |
| `python scripts/validate_structure.py --strict` | Même validation, les avertissements deviennent bloquants |
| `python scripts/new_skill.py <nom-kebab-case>` | Crée le squelette complet d’une nouvelle skill |
| `bash scripts/install.sh` | Installe les skills dans `~/.claude/skills` |
| `powershell -File scripts/install.ps1` | Installe les skills sous Windows |

La validation est rejouée automatiquement par GitHub Actions, voir `.github/workflows/validate.yml`.

## Principes de conception

- Chaque skill est autonome.
- Chaque skill contient un `SKILL.md` avec frontmatter YAML.
- La `description` décrit ce que fait la skill et les cas de déclenchement, c’est le seul élément lu par Claude pour choisir la skill.
- Les ressources additionnelles sont rangées dans `references/` et `templates/`.
- Les instructions valorisent la précision, la confidentialité et l’absence d’invention.

Les conventions détaillées sont dans [docs/conventions.md](docs/conventions.md).

## Sources utilisées pour la structure

- Anthropic, `anthropics/skills`, dépôt public de démonstration des Agent Skills : https://github.com/anthropics/skills
- Anthropic, `The Complete Guide to Building Skills for Claude`, guide indiquant qu’une skill contient un dossier avec `SKILL.md`, et éventuellement `scripts/`, `references/` et `assets/` : https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en
- Anthropic Claude Code Docs, `.claude` directory, documentation sur l’emplacement `.claude/skills` : https://code.claude.com/docs/en/claude-directory

## Avertissement

Ces skills sont des modèles opérationnels. Elles doivent être testées et adaptées à ton environnement, au niveau de confidentialité attendu et aux politiques internes avant usage sur des données sensibles.
