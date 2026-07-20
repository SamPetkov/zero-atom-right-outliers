# Paper build

The Letter uses the APS `revtex4-2` class with the `prl` and `reprint` options. The technical proof is a separate, self-contained Supplemental Material PDF.

```bash
cd ..
make paper
```

Files:

- `main.tex`: concise Letter.
- `supplement.tex`: full proofs and reproducibility details.
- `references.bib`: reference titles are included consistently.
- `macros.tex`: notation shared by both documents.
- `figures/noncentered_outlier_check.png`: the manuscript figure.

The checked PDFs are `main.pdf` and `supplement.pdf`.
