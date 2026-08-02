#!/usr/bin/env bash
# Installe les skills du dépôt dans le dossier utilisateur Claude.
# Usage : bash scripts/install.sh [destination]
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/.claude/skills"
target_dir="${1:-$HOME/.claude/skills}"

if [ ! -d "$source_dir" ]; then
  echo "Dossier source introuvable : $source_dir" >&2
  exit 1
fi

mkdir -p "$target_dir"

count=0
for skill in "$source_dir"/*/; do
  name="$(basename "$skill")"
  rm -rf "${target_dir:?}/$name"
  cp -R "$skill" "$target_dir/$name"
  echo "installée : $name"
  count=$((count + 1))
done

echo ""
echo "$count skills installées dans $target_dir"
echo "Redémarrer Claude Code pour les charger."
