#!/usr/bin/env bash
#
# Standardises a fresh Node/TS repo:
#   • Adds Node‑flavoured .gitignore if missing
#   • Appends dist/ and .env to ignore list
#   • Removes node_modules from tracking
#   • Creates a first "clean‑repo" commit
#   • Pushes if a remote is wired
set -euo pipefail

[[ -f .gitignore ]] || npx gitignore node
grep -qxF 'dist/' .gitignore || echo 'dist/' >> .gitignore
grep -qxF '.env'  .gitignore || echo '.env'  >> .gitignore

git rm -r --cached --ignore-unmatch node_modules >/dev/null 2>&1 || true
git add .gitignore
git commit -m "chore: apply standard .gitignore & untrack node_modules" || true

if git remote get-url origin &>/dev/null; then
  git push -u origin "$(git branch --show-current)"
fi
echo "✅ Repo housekeeping complete" 