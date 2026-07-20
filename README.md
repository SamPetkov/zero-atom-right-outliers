# Zero-Atom Right-Outlier Theory

**Author:** Samuil Petkov  
**Status:** research manuscript/preprint; not peer reviewed  
**Version:** 0.1.0  
**License:** CC BY 4.0 for the manuscript, proof text, figures, and numerical results. The Python code is additionally available under the MIT License.

This repository contains a proposed resolution of the nonnegative zero-gap case of right-outlier theory for self-coupled sample covariance matrices with exact zero diagonal weights. The central mechanism is an exact active-column reduction: inactive samples are deleted before linearization, the random factor \(N_{\mathrm{active}}/n\) is retained, and the invertible-weight theorem is applied to the exact conditional mark law of the active samples.

## Manuscript files

- `paper/main.tex` and `paper/main.pdf`: concise Physical Review Letters-style Letter.
- `paper/supplement.tex` and `paper/supplement.pdf`: complete proof supplement.
- `paper/references.bib`: bibliography with reference titles.
- `report/full_technical_report.md`: full theorem, proof, literature audit, computational checks, and adversarial audit.
- `submission/`: cover letter, 100-word PRL justification, formatting notes, and submission checklist.

## Reproducibility

The numerical checks use the fixed master seed `20260720`.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python code/zero_atom_checks.py --outdir results/generated
python code/verify_zero_atom_results.py results/generated/zero_atom_results.json
```

To compile both PDFs:

```bash
make paper
```

The build script accepts either the standard `bibtex` executable or the Debian/TeX Live fallback `bibtex.original`.

## Repository layout

```text
paper/       REVTeX sources, PDFs, bibliography, and manuscript figure
report/      full technical report
code/        simulation and independent verification scripts
results/     recorded JSON diagnostics
figures/     diagnostic plots
submission/  PRL submission support files
prompt/      original research specification
archive/     prior packaged resolution
```

## Main result represented in the manuscript

For nonnegative coupled weights satisfying

\[
h_b(g)\in\{0\}\cup[\tau,M],
\]

the limiting measure acquires the atom

\[
\nu_G(\{0\})=(1-\phi\pi)_+,
\]

but positive right outliers are still governed by

\[
\det\!\bigl(zI_q-F_G(z)\bigr)=0,\qquad z>\lambda_+(G).
\]

The manuscript also states multiplicity-preserving eigenvalue counts, absence of spurious right outliers, simple-root eigenvector normalization, the repeated-root spectral-projection limit, and the exact finite-dimensional rank.

## Citation

Use `CITATION.cff`, or cite:

> Samuil Petkov, *Spectral Outliers of Self-Coupled Covariance Matrices with Exact Zero Weights*, version 0.1.0 (2026), repository manuscript and reproducibility package.

## Attribution and licensing

Except where explicitly noted, the manuscript, supplement, report, figures, prompt copy, and numerical results are © 2026 Samuil Petkov and licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Recommended attribution:

> Petkov, Samuil (2026), *Zero-Atom Right-Outlier Theory*, version 0.1.0, CC BY 4.0.

The files in `code/` are dual-licensed under CC BY 4.0 and the MIT License; users may choose either license. See `LICENSE`, `LICENSE-CODE`, and `LICENSE-NOTICE.md`.

## Research and AI-use notice

OpenAI GPT-5.6 Pro was used substantively for literature synthesis, proof drafting, code generation, numerical checking, and manuscript preparation under the author's direction. The repository includes deterministic verification checks, but the mathematical work remains a preprint and requires independent expert review before journal submission or reliance.
