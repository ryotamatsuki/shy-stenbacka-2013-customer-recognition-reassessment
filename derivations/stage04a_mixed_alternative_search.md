# Stage 4A — Alternative Mixed-Equilibrium Falsification Search

Date: 2026-09-23

## Purpose
This diagnostic attacks the possibility that the Stage-4 high-`z` continuation is merely one member of an easily discoverable competing mixed family.

It is **not** a proof of unrestricted mixed-equilibrium uniqueness.

## Search class
For each selected interior point `z in {0.318, 0.325, 0.330}`, search over:
- at most two incumbent price atoms;
- at most two poaching price atoms;
- unrestricted mixing probabilities on those atoms.

The objective is maximum unilateral regret computed from primitive clipped customer masses. Candidate low-regret solutions are then re-checked with continuous one-dimensional best-response optimization.

Artifact: `code/stage04a_mixed_alternative_search.py`.

## Diagnostic result
Deterministic multistart-style optimization with the fixed production seed returned low-regret representations that collapse the incumbent support around the Stage-4 `p^*` and place the poacher support near the Stage-4 `q_L,q_H` atoms with the corresponding probability mass.

Representative continuous exploitabilities from the independent run on 2026-09-23 were of order:
- `1.4e-7` at `z=0.318`;
- `1.4e-6` at `z=0.325`;
- `7.8e-7` at `z=0.330`.

No numerically distinct low-regret two-by-two-support equilibrium was found in this diagnostic attack.

## Interpretation
This is evidence against an obvious nearby alternative mixed equilibrium, not a uniqueness theorem. The admissible publication quantifier remains:

> for `z_c<z<1/3`, the paper constructs and analyzes a certified symmetric two-point mixed continuation.

The manuscript must not replace that wording by “the unique mixed equilibrium” unless a later theorem proves unrestricted uniqueness or payoff equivalence.

## Closure role
Stage 4A treats this diagnostic as a falsification search only. The logical basis for downstream work is the independently certified validity of the displayed continuation plus an explicit selection scope, not an inferred uniqueness result.
