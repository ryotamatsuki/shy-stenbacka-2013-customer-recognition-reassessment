# Shy–Stenbacka Customer Recognition Reassessment

## Project

A source-specific reassessment of the model directly inspected in Shy and Stenbacka, Federal Reserve Bank of Boston Working Paper 12-4 (15 February 2012), the verified predecessor of the 2013 *Information Economics and Policy* article “Investment in Customer Recognition and Information Exchange.”

## Current status

**Stage 8 — Canonical Theory Freeze: CLOSED — GO.**

Theory is frozen at commit \`555683b26500c0213d04f96dbde8d66b28969df2\`. The next canonical gate is Stage 9 — Repository / Reproducibility Setup.

## Frozen headline result

Let \`z=Delta/sigma\` and
\[
z_c=(-6+4\sqrt3)/3.
\]

In the inspected baseline \`UU\` price game:
- \`0<z<=z_c\`: the source pure profile is the unique pure equilibrium;
- \`z_c<z<1/3\`: no pure equilibrium exists;
- on the high-\`z\` wedge, the project constructs and certifies a symmetric two-point mixed continuation.

High-\`z\` downstream investment, sharing, profit, consumer-surplus, and welfare conclusions are conditional on that certified continuation. Unrestricted mixed-equilibrium uniqueness is not claimed.

## Research-strength boundary

Stage 7.5A falsification tests show that the high-\`z\` pure-nonexistence result does not survive two pre-specified alternatives (Beta(2,2) switching costs and unequal type masses). The headline mechanism is therefore **MODEL-SPECIFIC**, not a general theory theorem.

## Formal verification

Lean 4/mathlib verification of the proof-critical algebraic core: **PASS**.

GitHub Actions run #71:
- clean build: PASS;
- axiom audit: PASS;
- placeholder audit: PASS.

Formal verification does not cover consumer primitives, active-set exhaustiveness, complete equilibrium correspondence, mixed uniqueness, or portability.

## Source qualification

The full Boston Fed working-paper body has been directly inspected. The 2013 VOR bibliographic identity and lineage are verified, but equation-level VOR/WP identity has not been directly verified. Publication-facing equation claims therefore remain explicitly working-paper/source-version qualified.

## Repository policy

- no merge to \`main\` before authorized integration;
- no Stage 15 / submission freeze in the current mandate;
- theory changes after Stage 8 require rollback and recertification;
- draft verification PR #3 exists only to run CI and must not be merged as part of this workflow.
