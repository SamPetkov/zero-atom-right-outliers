# Validation record

Validation date: 20 July 2026.

## LaTeX

- `paper/main.tex` compiled successfully with REVTeX 4.2 to a 3-page PDF.
- `paper/supplement.tex` compiled successfully to an 11-page PDF.
- No undefined citations or references were reported in the final logs.
- No overfull horizontal or vertical boxes were reported in the final logs.
- No deferred-float placement warnings were reported in the final Letter log.
- PDF metadata contains the manuscript title and author.
- All fonts reported by `pdffonts` are embedded.
- Every page of both final PDFs was rendered to PNG and visually inspected; the final post-build renders were pixel-identical to the inspected renders.

## Numerical checks

- Master seed: `20260720`.
- `code/zero_atom_checks.py` ran successfully.
- `code/verify_zero_atom_results.py` reported: `All deterministic verification checks passed.`
- The exact active-rank check, fixed-point residual, regularization identity, scalar determinant residual, and two-construction comparison all satisfied their programmed tolerances.

## Licensing and authorship

- Primary repository license: CC BY 4.0.
- Named author and attribution party: Samuil Petkov.
- Code also has an MIT option through `LICENSE-CODE`.
- `CITATION.cff`, `AUTHORS.md`, and the manuscript byline agree.

## Remaining external action

The repository must be created and pushed through an authenticated GitHub write session. The supplied `scripts/publish_github.sh` performs that operation.
