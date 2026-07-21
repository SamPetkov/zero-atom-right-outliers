#!/usr/bin/env python3
from pathlib import Path

path = Path("paper/chapters/chapter01.tex")
text = path.read_text(encoding="utf-8")
old = (
    "The question is therefore not whether the zero modes exist--they do--but "
    "whether deleting them changes the positive outlier equation.\n\n"
    "This manuscript proves that it does not under the zero-gap condition needed "
    "by the active-block argument:"
)
new = (
    "The question is therefore not whether the zero modes exist--they do--but "
    "whether deleting them changes the positive outlier equation.  This is the "
    "nonnegative zero-gap special case of the SolveAll problem \\emph{Outlier "
    "theory beyond non-degeneracy/invertibility assumptions (ReLU and zero "
    "diagonal entries)} \\cite{SolveAllProblem}.\n\n"
    "This manuscript proves that it does not under the zero-gap condition needed "
    "by the active-block argument:"
)
if old not in text:
    raise SystemExit("introduction marker not found")
if text.count(old) != 1:
    raise SystemExit("introduction marker is not unique")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
print("SolveAll citation added to the introduction.")
