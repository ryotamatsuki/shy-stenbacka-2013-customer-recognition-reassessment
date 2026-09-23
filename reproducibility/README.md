# Reproducibility

Canonical entry points:

- \`make verify\` — Python mathematical/regression suite.
- \`make tables\` — deterministic LaTeX table generation.
- \`make formal\` — pinned Lean build.
- \`make manuscript\` — generated tables + LaTeX/BibTeX manuscript build.

Pinned Python package versions are in \`requirements.txt\`. Lean/mathlib are pinned by \`lean-toolchain\`, \`lakefile.lean\`, and \`lake-manifest.json\`.

The Lean build certifies the proof-critical algebraic core only. Economic globality and equilibrium-set claims remain supported by the Stage 4/4A analytic and independent artifacts.
