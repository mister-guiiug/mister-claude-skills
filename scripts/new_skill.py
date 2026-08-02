#!/usr/bin/env python3
"""Crée le squelette d’une nouvelle skill conforme aux conventions du dépôt.

Utilisation :

    python scripts/new_skill.py ma-nouvelle-skill --title "Ma Nouvelle Skill" \
        --description "Fait X. Utiliser quand l’utilisateur demande Y."
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".claude" / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

SKILL_TEMPLATE = """---
name: {name}
version: 1.0.0
updated: {updated}
description: {description}
---

# {title}

## Principes non négociables

- Ne jamais inventer de donnée, chiffre, date, source ou responsabilité.
- Si une information n’est pas fournie ou vérifiable, écrire `Je ne sais pas` ou `[à compléter]`.
- Distinguer clairement fait, hypothèse et suggestion.
- Préserver la confidentialité des informations internes.
- Ne pas utiliser d’em dash.
- Produire des contenus directement copiables.

## Données d’entrée attendues

Demander ou utiliser si disponible :

- [à compléter]

## Mission

[à compléter]

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur demande :

- [à compléter]

## Méthode

1. [à compléter]

## Livrables spécifiques

- [à compléter]

## Format de sortie recommandé

Toujours produire :

1. Diagnostic ou synthèse.
2. Version proposée prête à copier.
3. Justification des choix.
4. Points à vérifier ou compléter.

## Checklist qualité avant réponse

- Les informations sensibles sont-elles neutralisées ?
- Les chiffres proviennent-ils de l’utilisateur ?
- Les zones incertaines sont-elles marquées clairement ?
"""

CHECKLIST_TEMPLATE = """# Quality checklist

## Exactitude

- Aucun chiffre inventé.
- Aucun diplôme, certification ou poste inventé.
- Les hypothèses sont libellées comme hypothèses.

## Pertinence

- [à compléter]

## Confidentialité

- Les noms de projets internes, clients ou données sensibles sont anonymisés si diffusion publique.
"""

EXAMPLE_TEMPLATE = """# Exemple de sortie

Exemple fictif produit à des fins d’illustration. Les données ne correspondent à aucune personne ni organisation réelle.

## Entrée fournie par l’utilisateur

```text
[à compléter]
```

## Sortie attendue

[à compléter]

## Contrôles appliqués

| Point | Statut |
| --- | --- |
| [à compléter] | [à compléter] |

## Points à vérifier ou compléter

- [à compléter]
"""

PROMPT_TEMPLATE = """# Prompt template - {title}

Utilise la skill `{name}`.

Objectif : [décrire l’objectif]
Audience cible : [à compléter]
Ton souhaité : [sobre, exécutif, technique, direct]
Langue : [français ou anglais]

Données disponibles :
- [à compléter]

Contraintes :
- Ne rien inventer.
- Marquer les informations manquantes avec `[à compléter]`.
- Proposer une version directement copiable.
"""


def title_from_name(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Crée une nouvelle skill.")
    parser.add_argument("name", help="nom en kebab-case, identique au nom de dossier")
    parser.add_argument("--title", help="titre affiché dans le SKILL.md")
    parser.add_argument(
        "--description",
        default="[à compléter]. Utiliser quand [à compléter].",
        help="description du frontmatter, doit inclure la condition de déclenchement",
    )
    parser.add_argument(
        "--updated",
        default="[à compléter]",
        help="date de dernière mise à jour au format AAAA-MM-JJ",
    )
    args = parser.parse_args()

    if not NAME_PATTERN.match(args.name):
        print(f"Nom invalide : {args.name}. Utiliser du kebab-case minuscule.")
        return 1

    skill_dir = SKILLS_DIR / args.name
    if skill_dir.exists():
        print(f"La skill existe déjà : {skill_dir}")
        return 1

    title = args.title or title_from_name(args.name)

    (skill_dir / "references").mkdir(parents=True)
    (skill_dir / "templates").mkdir(parents=True)

    (skill_dir / "SKILL.md").write_text(
        SKILL_TEMPLATE.format(
            name=args.name,
            description=args.description,
            title=title,
            updated=args.updated,
        ),
        encoding="utf-8",
    )
    (skill_dir / "references" / "quality-checklist.md").write_text(
        CHECKLIST_TEMPLATE, encoding="utf-8"
    )
    (skill_dir / "references" / "example-output.md").write_text(
        EXAMPLE_TEMPLATE, encoding="utf-8"
    )
    (skill_dir / "templates" / "prompt-template.md").write_text(
        PROMPT_TEMPLATE.format(name=args.name, title=title), encoding="utf-8"
    )

    print(f"Skill créée : {skill_dir.relative_to(ROOT).as_posix()}")
    print("Étapes suivantes :")
    print("1. Compléter les sections marquées [à compléter].")
    print("2. Référencer la skill dans README.md et docs/usage-guide.md.")
    print("3. Lancer python scripts/validate_structure.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
