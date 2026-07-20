.PHONY: all paper checks clean

all: paper checks

paper:
	bash scripts/build_pdfs.sh

checks:
	python code/zero_atom_checks.py --outdir results/generated
	python code/verify_zero_atom_results.py results/generated/zero_atom_results.json

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.fdb_latexmk \
	      paper/*.fls paper/*.log paper/*.out paper/*Notes.bib \
	      paper/*.pass*.log paper/*.bibtex.log
