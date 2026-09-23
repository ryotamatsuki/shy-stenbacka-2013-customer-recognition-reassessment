# Stage 9 — Repository / Reproducibility Setup

Date: 2026-09-23  
Input: Stage-8 frozen theory.

## Production structure established

- modular LaTeX manuscript under \`manuscript/\`;
- section-by-section source files;
- verified bibliography seed in \`manuscript/references.bib\`;
- deterministic table generator \`code/generate_tables.py\`;
- pinned Python dependencies in \`requirements.txt\`;
- pinned Lean/mathlib through \`lean-toolchain\`, \`lakefile.lean\`, and \`lake-manifest.json\`;
- Stage 4A / Stage 7.5A theorem and robustness certificates retained;
- \`Makefile\` orchestration for verification, tables, formal build, manuscript build, and clean;
- GitHub Actions mathematical regression + formal verification workflow;
- submission and reproducibility workspaces;
- counterexample, alternative-equilibrium, equilibrium-correspondence, welfare, and portability regression artifacts retained.

## Reproducibility entry points

\`make verify\`
runs the independent Python verification suite.

\`make tables\`
generates manuscript quantitative tables from frozen formulas.

\`make formal\`
rebuilds the pinned Lean project.

\`make manuscript\`
generates tables and runs the LaTeX/BibTeX build sequence.

## Evidence separation

The production repository preserves distinct evidence classes:
- analytic construction;
- independent primitive/adversarial evaluation;
- diagnostic numerical falsification;
- formal proof-critical algebra;
- source/version evidence.

No green CI result is described as proving an economic object that is not encoded.

## Stage-9 verdict

**GO — REPRODUCIBILITY / PRODUCTION SETUP COMPLETE.**

The manuscript scaffold contains no new economic claim. Stage 10 must fill sections only from the Stage-8 freeze and create an explicit figure/table architecture.

## Formal closure record

- Stage: 9 — Repository / Reproducibility Setup.
- Canonical verdict: **STAGE 9 CLOSED — GO.**
- Theory changes: NONE.
- Next gate: **Stage 10 — Section-by-Section Paper Construction.**
