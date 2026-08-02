# Conventions de rédaction des skills

## Structure d’une skill

```text
.claude/skills/<nom-kebab-case>/
  SKILL.md                        obligatoire
  references/quality-checklist.md conseillé
  templates/prompt-template.md    conseillé
```

Créer le squelette avec :

```bash
python scripts/new_skill.py ma-skill --description "Fait X. Utiliser quand l’utilisateur demande Y."
```

## Frontmatter

```yaml
---
name: ma-skill
description: Fait X. Utiliser quand l’utilisateur demande Y ou Z.
---
```

Règles :

- `name` en kebab-case minuscule, identique au nom du dossier.
- `description` en une seule ligne, elle sert à deux choses : dire ce que fait la skill et dire quand la déclencher. C’est le seul élément que Claude lit pour choisir une skill, le corps du `SKILL.md` n’est chargé qu’après sélection.
- Ne pas utiliser ` : ` dans la `description` sans guillemets, la valeur devient un YAML invalide et la description est ignorée. Écrire une virgule, ou entourer la valeur de guillemets doubles.
- Inclure les mots que l’utilisateur emploiera réellement : `photo de profil`, `abstract`, `ATS`, `radar technologique`, `headline`.

## Sections attendues dans le corps

1. `## Principes non négociables`
2. `## Données d’entrée attendues`
3. `## Mission`
4. `## Déclencheurs`
5. `## Méthode`
6. `## Livrables spécifiques`
7. `## Format de sortie recommandé`
8. `## Checklist qualité avant réponse`

Les sections intermédiaires spécifiques au domaine sont libres, voir `technology-watch` avec son format radar ou `linkedin-profile-photo-prompt` avec sa structure de prompt.

## Règles de rédaction

- Ne jamais inventer de donnée, écrire `Je ne sais pas` ou `[à compléter]`.
- Pas d’em dash, la règle est vérifiée automatiquement par le validateur.
- Ton professionnel, sobre et factuel.
- Toujours proposer une version directement copiable.
- Garder chaque skill autonome, ne pas créer de dépendance vers un fichier hors de son dossier, une skill doit rester copiable seule dans `~/.claude/skills`.

## Avant de committer

```bash
python scripts/validate_structure.py --strict
```

Puis référencer la nouvelle skill dans `README.md`, `docs/usage-guide.md` et si pertinent `examples/sample-prompts.md`.
