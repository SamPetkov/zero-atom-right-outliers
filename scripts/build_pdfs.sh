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

compile_one() {
  local stem="$1"
  (
    cd "$PAPER"
    pdflatex -interaction=nonstopmode -halt-on-error "$stem.tex"
    "$BIBTEX" "$stem"
    pdflatex -interaction=nonstopmode -halt-on-error "$stem.tex"
    pdflatex -interaction=nonstopmode -halt-on-error "$stem.tex"
  )
}

compile_one main
compile_one supplement

echo "Built:"
echo "  $PAPER/main.pdf"
echo "  $PAPER/supplement.pdf"
