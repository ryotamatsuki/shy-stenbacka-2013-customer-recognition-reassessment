# Stage 7.5A — Generality / Quantifier / Portability Red-Team

Date: 2026-09-23  
Workflow: \`research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7\` (v2.4)

## Scope attack
This gate attacks claim strength, not baseline algebra.

## Quantifier freeze

### Pure price theorem
For every \`z\` in \`(0,1/3)\`, over nonnegative baseline \`UU\` prices:
- if \`z<=z_c\`, the source profile is the unique **pure** equilibrium;
- if \`z>z_c\`, the baseline \`UU\` game has no **pure** equilibrium.

This is global over pure prices in the inspected baseline model only.

### Mixed continuation
For every \`z_c<z<1/3\`, **there exists** the displayed symmetric two-point mixed continuation.

No unrestricted mixed uniqueness theorem is claimed.

### Downstream results
Every high-\`z\` Stage-II, Stage-I, profit, consumer-surplus, and welfare result using the mixed continuation is a **selected-continuation** statement.

## Portability red team
Two pre-specified non-cosmetic alternatives were re-solved from primitives:
1. Beta(2,2) switching-cost distribution;
2. unequal type masses \`(1,1.25,0.75,1)\`.

Both retain pure profiles at attacked high-\`z\` points where the baseline game has no pure equilibrium.

Therefore the baseline pure-nonexistence/two-point-mixing mechanism is **MODEL-SPECIFIC**.

The workflow stop rule is triggered. No further alternative is redesigned to rescue portability.

## Benchmark terminology
The paper compares total welfare across model outcomes \`NI\`, \`NS,I\`, and \`S,I\`. It does not solve an unrestricted planner problem over all feasible mechanisms, information structures, prices, transfers, or investment technologies.

Therefore:
- permitted: “total-welfare ordering,” “outcome welfare,” “socially preferred among the compared outcomes” where exact;
- prohibited: “first best” unless a separate unrestricted planner problem is actually solved.

## Claim-scope audit
- exact threshold: baseline/model-specific;
- pure correspondence: baseline/model-specific;
- selected mixed continuation: existence only;
- corrected acquisition thresholds: baseline/model-specific;
- Stage-I SPE correspondence: selected-continuation high-\`z\`;
- profit/CS crossings: selected-continuation, model-specific;
- total-welfare ordering: selected-continuation where high-\`z\`, model-specific;
- institutional discussion: plausibility only, not external-validity proof;
- VOR defect attribution: still WP/VOR-qualified until equation-level VOR verification.

## Contribution robustness
Canonical certificate: \`theorem_certificates/STAGE_075A_CONTRIBUTION_ROBUSTNESS.md\`.

## Formal verification
Canonical certificate: \`theorem_certificates/FORMAL_VERIFICATION_CERTIFICATE.md\`.

The pinned Lean project has passed GitHub Actions run #71:
- clean project build: PASS;
- axiom audit: PASS;
- placeholder audit: PASS.

Formal coverage remains **PROOF-CRITICAL CORE** only.

## Current verdict

**GO — GENERALITY / QUANTIFIER / PORTABILITY CERTIFICATION PASS.**

- contribution robustness certificate: COMPLETE;
- two pre-specified portability attacks: COMPLETE;
- stop rule: TRIGGERED, with headline claims classified MODEL-SPECIFIC;
- equilibrium and welfare quantifiers: FROZEN;
- benchmark terminology: FROZEN;
- formal verification gate: **FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE**;
- exact correctness blocker at Stage-7.5A scope: NONE.

## Routing

**STAGE 7.5A CLOSED — GO. Route to Stage 8 — Canonical Theory Freeze.**


## Stage-11 reopening and recertification

Stage 11 detected that the original portability tests certified only grid regret. This was recorded as a certification regression and Stage 7.5A was reopened for the affected diagnostic evidence only.

The repaired implementation performs continuous best-response refinement and continuous unilateral-regret checks. Both pre-specified alternatives continue to admit numerical pure best-response fixed points at the attacked high-`z` values, with continuous regret below (10^{-8}).

**RECERTIFIED VERDICT: GO — GENERALITY / QUANTIFIER / PORTABILITY CERTIFICATION PASS.**

The contribution classification, stop-rule decision, and theory-freeze scope are unchanged. No baseline theorem or formal theorem statement was modified.
