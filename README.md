# Right Outliers with Exact Zero Weights

**Author:** Samuil Petkov  
**Affiliation:** École normale supérieure - PSL, Université PSL, 45 rue d’Ulm, 75005 Paris, France  
**Email:** `samuil.petkov@ens.psl.eu`  
**Version:** 0.4.1  
**Status:** self-contained research manuscript/preprint; not peer reviewed

This repository contains one canonical submission:

- `paper/main.tex` — root TeX file;
- `paper/parts/` and `paper/chapters/` — source modules included by that root file;
- the checked PDF is produced as `paper/main.pdf` by the build and CI workflows.

The source is modular only for maintainability. It compiles into one manuscript; there is no separate Letter or Supplemental Material.

## Main result

For coupled nonnegative weights satisfying

\[
h_b(g)\in\{0\}\cup[\tau,M],
\]

let \(\pi\) be the active probability. The limiting spectral measure has zero atom

\[
\nu_G(\{0\})=(1-\phi\pi)_+,
\]

while positive right outliers are governed by the effective determinant

\[
\det\!\bigl(zI_q-F_G(z)\bigr)=0,\qquad z>\lambda_+(G).
\]

The manuscript states compact-interval outlier counts with multiplicity, absence of spurious right outliers, existence of empirical outliers, simple-root eigenvector normalization, the repeated-root spectral-projection limit, and the exact finite-dimensional rank.

## Proof mechanism

The singular diagonal is split before linearization:

\[
M_d=\frac{N_{\mathrm{active}}}{n}
\left(\frac1{N_{\mathrm{active}}}A_+D_+A_+^{\mathsf T}\right),
\qquad \tau I\preceq D_+\preceq MI.
\]

The conditional low-dimensional variables are retained under their exact truncated or reweighted law. Only the independent orthogonal Gaussian block is passed to the weighted-Wishart local-law input. The proof tracks \(N_{\mathrm{active}}/n\), \(N_{\mathrm{active}}/d\), and \(N_{\mathrm{active}}/(d-q)\) separately.

## Build

A TeX Live installation containing REVTeX 4.2, `pdflatex`, and BibTeX is required.

```bash
make paper
```

This produces `paper/main.pdf`. The CI workflow additionally fails on undefined citations, undefined references, overfull boxes, missing output, or an empty PDF.

## Reproducibility

The numerical checks use master seed `20260720`.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-reproduction.txt
make checks
```

The verifier must print:

```text
All deterministic verification checks passed.
```

Exact package versions for the recorded run are stored in `results/zero_atom_results.json`; CI uses compatible version ranges so that wheels remain installable.

## Repository layout

```text
paper/       one self-contained REVTeX manuscript
code/        simulations and deterministic verifier
results/     recorded numerical output and generated diagnostics
figures/     diagnostic plots
report/      proof audit and validation notes, not a second manuscript
submission/  one-manuscript submission notes
prompt/      original research specification
```

## Citation

Use `CITATION.cff`, or cite:

> Samuil Petkov, “Right Outliers of Self-Coupled Sample Covariance Matrices with Exact Zero Weights,” version 0.4.1 (2026), preprint and reproducibility package.

## License

Except where explicitly noted, the manuscript, proof-audit text, figures, numerical results, and documentation are © 2026 Samuil Petkov and licensed under CC BY 4.0. The Python code is dual-licensed under CC BY 4.0 and MIT. See `LICENSE`, `LICENSE-CODE`, and `LICENSE-NOTICE.md`.

## AI-use disclosure

OpenAI GPT-5.6 Pro was used substantively for literature synthesis, proof drafting, code generation, numerical checking, and manuscript preparation under the author’s direction. It is not an author. Samuil Petkov remains responsible for independent verification, attribution, and any submission.
