#!/usr/bin/env python3
"""Valide la structure des skills du dépôt.

Sans dépendance externe. Utilisation :

    python scripts/validate_structure.py
    python scripts/validate_structure.py --strict   # les avertissements deviennent bloquants
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".claude" / "skills"

NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
UPDATED_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
NAME_MAX_LENGTH = 64
DESCRIPTION_MIN_LENGTH = 40
DESCRIPTION_MAX_LENGTH = 1024
EM_DASH = "—"
# Les seules clés de premier niveau qu'acceptent claude.ai et l'API Skills.
PORTABLE_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

REQUIRED_SECTIONS = [
    "## Principes non négociables",
    "## Mission",
    "## Déclencheurs",
    "## Méthode",
    "## Format de sortie recommandé",
    "## Checklist qualité avant réponse",
    "## Ressources",
]

ANNEX_FOLDERS = ["references", "templates"]

RECOMMENDED_FILES = [
    Path("references") / "quality-checklist.md",
    Path("references") / "example-output.md",
    Path("templates") / "prompt-template.md",
]

INDEX_FILES = [
    Path("README.md"),
    Path("docs") / "usage-guide.md",
]

ROUTER_NAME = "career-skills-router"


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    """Retourne les paires clé/valeur du frontmatter YAML simple et une erreur eventuelle."""
    if not text.startswith("---"):
        return {}, "frontmatter YAML absent, le fichier doit commencer par ---"

    lines = text.splitlines()
    closing = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing = index
            break
    if closing is None:
        return {}, "frontmatter YAML non fermé, délimiteur --- manquant"

    # Un seul niveau d'imbrication suffit : les clés indentées sous `metadata:`
    # sont rangées sous la forme `metadata.version`.
    fields: dict[str, str] = {}
    parent: str | None = None
    for line in lines[1:closing]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if line[0] in " \t" and parent:
            fields[f"{parent}.{key}"] = value
            continue
        parent = key if not value else None
        fields[key] = value
    return fields, None


def raw_description_is_quoted(text: str) -> bool:
    """Indique si la valeur brute de description est entourée de guillemets."""
    for line in text.splitlines():
        if line.startswith("description:"):
            value = line.split(":", 1)[1].strip()
            return len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}
    return False


def check_skill(skill_dir: Path, report: Report) -> str | None:
    """Valide une skill et retourne son nom si le frontmatter est exploitable."""
    rel = skill_dir.relative_to(ROOT).as_posix()
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        report.error(f"{rel} : SKILL.md manquant")
        return None

    text = skill_file.read_text(encoding="utf-8")
    fields, error = parse_frontmatter(text)
    if error:
        report.error(f"{rel}/SKILL.md : {error}")
        return None

    name = fields.get("name")
    description = fields.get("description")

    if not name:
        report.error(f"{rel}/SKILL.md : champ name manquant")
    else:
        if name != skill_dir.name:
            report.error(
                f"{rel}/SKILL.md : name '{name}' différent du nom de dossier '{skill_dir.name}'"
            )
        if not NAME_PATTERN.match(name):
            report.error(f"{rel}/SKILL.md : name '{name}' doit être en kebab-case minuscule")
        if len(name) > NAME_MAX_LENGTH:
            report.error(f"{rel}/SKILL.md : name de {len(name)} caractères, maximum {NAME_MAX_LENGTH}")

    if not description:
        report.error(f"{rel}/SKILL.md : champ description manquant")
    else:
        if len(description) < DESCRIPTION_MIN_LENGTH:
            report.warn(
                f"{rel}/SKILL.md : description de {len(description)} caractères, "
                f"minimum conseillé {DESCRIPTION_MIN_LENGTH}"
            )
        if len(description) > DESCRIPTION_MAX_LENGTH:
            report.error(
                f"{rel}/SKILL.md : description de {len(description)} caractères, "
                f"maximum {DESCRIPTION_MAX_LENGTH}"
            )
        if " : " in description and not raw_description_is_quoted(text):
            report.error(
                f"{rel}/SKILL.md : description contenant ' : ' sans guillemets, "
                "YAML invalide, remplacer le deux-points ou entourer la valeur de guillemets"
            )
        if "utiliser quand" not in description.lower():
            report.warn(
                f"{rel}/SKILL.md : description sans condition de déclenchement, "
                "ajouter une formulation du type 'Utiliser quand ...'"
            )

    # claude.ai et l'API Skills refusent toute autre clé de premier niveau ;
    # Claude Code, lui, l'ignorerait sans rien dire.
    for key in fields:
        if "." not in key and key not in PORTABLE_KEYS:
            report.error(
                f"{rel}/SKILL.md : clé '{key}' refusée par claude.ai et l'API Skills, "
                "la ranger sous metadata"
            )

    version = fields.get("metadata.version")
    if not version:
        report.warn(f"{rel}/SKILL.md : metadata.version absent, ajouter version: \"1.0.0\" sous metadata")
    elif not VERSION_PATTERN.match(version):
        report.error(f"{rel}/SKILL.md : metadata.version '{version}' non conforme au format x.y.z")

    updated = fields.get("metadata.updated")
    if not updated:
        report.warn(f"{rel}/SKILL.md : metadata.updated absent, ajouter updated: \"AAAA-MM-JJ\" sous metadata")
    elif not UPDATED_PATTERN.match(updated):
        report.error(f"{rel}/SKILL.md : metadata.updated '{updated}' non conforme au format AAAA-MM-JJ")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            report.warn(f"{rel}/SKILL.md : section conseillée absente, {section}")

    for relative_file in RECOMMENDED_FILES:
        if not (skill_dir / relative_file).exists():
            report.warn(f"{rel} : fichier conseillé absent, {relative_file.as_posix()}")

    # Claude ne lit un fichier annexe que si SKILL.md lui dit quand le faire.
    for folder in ANNEX_FOLDERS:
        for annex in sorted(p for p in (skill_dir / folder).glob("*") if p.is_file()):
            relative = annex.relative_to(skill_dir).as_posix()
            if relative not in text:
                report.error(
                    f"{rel}/SKILL.md : {relative} n'est cité nulle part, Claude ne le lira pas ; "
                    "le citer dans la section Ressources en disant quand le lire"
                )

    for markdown_file in sorted(skill_dir.rglob("*.md")):
        content = markdown_file.read_text(encoding="utf-8")
        for line_number, line in enumerate(content.splitlines(), start=1):
            if EM_DASH in line:
                location = markdown_file.relative_to(ROOT).as_posix()
                report.error(f"{location}:{line_number} : em dash interdit par CLAUDE.md")

    return name


def check_indexes(names: list[str], report: Report) -> None:
    for index_file in INDEX_FILES:
        path = ROOT / index_file
        if not path.exists():
            report.warn(f"{index_file.as_posix()} : fichier absent, index non vérifié")
            continue
        content = path.read_text(encoding="utf-8")
        for name in names:
            if name not in content:
                report.warn(f"{index_file.as_posix()} : skill '{name}' non référencée")

    # La table d'orientation du routeur, que docs/conventions.md impose aussi de tenir à jour.
    router = SKILLS_DIR / ROUTER_NAME / "SKILL.md"
    if router.exists():
        content = router.read_text(encoding="utf-8")
        location = router.relative_to(ROOT).as_posix()
        for name in names:
            if name != ROUTER_NAME and f"`{name}`" not in content:
                report.warn(f"{location} : skill '{name}' absente de la table d'orientation")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Valide la structure des skills.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="traite les avertissements comme des erreurs",
    )
    args = parser.parse_args()

    report = Report()

    if not SKILLS_DIR.is_dir():
        print(f"Dossier introuvable : {SKILLS_DIR}")
        return 1

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        print(f"Aucune skill trouvée dans {SKILLS_DIR}")
        return 1

    names: list[str] = []
    for skill_dir in skill_dirs:
        name = check_skill(skill_dir, report)
        if name:
            names.append(name)

    check_indexes(names, report)

    for warning in report.warnings:
        print(f"WARN  {warning}")
    for error in report.errors:
        print(f"ERROR {error}")

    print(
        f"\n{len(skill_dirs)} skills analysées, "
        f"{len(report.errors)} erreurs, {len(report.warnings)} avertissements"
    )

    if report.errors:
        return 1
    if args.strict and report.warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
