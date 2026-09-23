# Formal Verification Certificate — Proof-Critical Core

Date: 2026-09-23

## Applicability
**FORMALIZATION APPLICABLE.**

The project corrects a published mathematical result and relies on exact threshold algebra, quantified sign identities, mixed-support indifference, investment-threshold differences, and welfare identities.

## Formal coverage
Coverage classification: **PROOF-CRITICAL CORE**.

Formal source: \`formal/SS2013Reassessment.lean\`.

### Paper claim -> Lean theorem map
- critical threshold is a root of the gain numerator -> \`critical_is_root\`
- gain factorization -> \`gain_numerator_factor\`
- strict positive gain above the critical root -> \`gain_positive_above_critical\`
- exact \`(Delta,sigma)=(8,25)\` gain -> \`exact_counterexample_gain\`
- positivity of exact counterexample -> \`exact_counterexample_positive\`
- selected mixed-support poaching indifference -> \`mixed_support_indifference\`
- corrected threshold gap \`K_NS-K_S=5z^2/18\` -> \`corrected_threshold_gap\`
- no-share minus share gross-profit difference -> \`noShare_minus_share_profit\`
- consumer-surplus difference -> \`cs_noShare_minus_share\`
- total-welfare no-share/share difference -> \`total_noShare_minus_share\`

## Explicitly not formalized
The Lean file does **not** formalize:
- consumer primitives and clipping from utility inequalities;
- exhaustive active-set partition;
- global best-response proof;
- pure nonexistence theorem as a full game object;
- unrestricted mixed-equilibrium uniqueness;
- Stage-I/Stage-II equilibrium correspondence;
- portability diagnostics;
- VOR/WP source identity.

Those objects remain certified analytically/numerically by the corresponding workflow stages.

## Placeholder / axiom policy
The formal source contains no \`sorry\` or \`admit\`. The workflow requires a clean build plus axiom audit before Stage 8.

## Toolchain provenance
- Lean: \`leanprover/lean4:v4.35.0-rc2\`
- mathlib commit: \`b1007d8abfd0c776eb8a75e8f6bf26db5eae4a69\`
- dependency lock: \`lake-manifest.json\`
- project config: \`lakefile.lean\`

## Build / axiom evidence

GitHub Actions verification run #71, run id `35840067654`, formal job id `107112751294`, on commit `01d8f266b413518ae9bb719dd0bdba177adacfa4`:

- `lake build`: **SUCCESS** — 8,940 jobs completed;
- axiom-audit: **SUCCESS** — 58 declarations under `SS2013Reassessment` audited;
- allowed axioms only: `propext`, `Classical.choice`, `Quot.sound`;
- proof-placeholder grep for `sorry|admit`: **SUCCESS / none found**;
- toolchain and mathlib revisions match the pinned files recorded above.

One non-blocking linter warning reports that `simpa` could be simplified to `simp`; it has no proof-semantic consequence.

## Gate state

**FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE.**

This PASS certifies only the theorem map above. It does not enlarge formal coverage to unencoded economic primitives, case exhaustiveness, equilibrium uniqueness, or portability.
