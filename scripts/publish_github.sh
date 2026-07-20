#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OWNER="SamPetkov"
REPO="zero-atom-right-outliers"
FULL="$OWNER/$REPO"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is required: https://cli.github.com/" >&2
  exit 1
fi

gh auth status
cd "$ROOT"

if [[ ! -d .git ]]; then
  git init -b main
fi

git config user.name "Samuil Petkov"
git config user.email "petkov.sam@gmail.com"

git add -A
if ! git diff --cached --quiet; then
  git commit -m "Publish zero-atom right-outlier manuscript and reproducibility package"
fi

if gh repo view "$FULL" >/dev/null 2>&1; then
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$FULL.git"
  fi
  git push -u origin main
else
  gh repo create "$FULL" \
    --public \
    --description "PRL-style manuscript, proofs, and reproducibility code for zero-atom self-coupled covariance outliers" \
    --source . \
    --remote origin \
    --push
fi

git push origin --tags

printf '\nPublished: https://github.com/%s\n' "$FULL"
