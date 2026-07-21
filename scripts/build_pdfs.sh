#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PAPER="$ROOT/paper"

if command -v bibtex >/dev/null 2>&1 && bibtex --version >/dev/null 2>&1; then
  BIBTEX="$(command -v bibtex)"
elif command -v bibtex.original >/dev/null 2>&1; then
  BIBTEX="$(command -v bibtex.original)"
else
  echo "A working BibTeX executable is required." >&2
  exit 1
fi

(
  cd "$PAPER"
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  "$BIBTEX" main
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
)

test -s "$PAPER/main.pdf"
if grep -Eq 'LaTeX Warning: (There were undefined references|Citation .* undefined|Reference .* undefined)' "$PAPER/main.log"; then
  echo "The manuscript contains unresolved citations or references." >&2
  exit 1
fi
if grep -q 'Overfull \\hbox' "$PAPER/main.log"; then
  echo "The manuscript contains an overfull box." >&2
  exit 1
fi

echo "Built and checked $PAPER/main.pdf"
