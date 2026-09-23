# Stage 4A — Independent Mathematical Adversarial Certification

Date: 2026-09-23  
Workflow: `research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7` (v2.4)

## Scope
This gate independently attacks the Stage-4 clipped-price construction. The independent implementation does not call the Stage-4 symbolic branch solver and reconstructs demand directly from consumer-level switching inequalities.

## Independent implementation
Artifact: `code/stage04a_primitive_evaluator.py`.

For each valuation type, the evaluator:
1. forms the primitive stay/switch utility difference;
2. clips the switching mass to `[0,1]`;
3. computes revenue directly from the resulting customer masses;
4. globally maximizes a deviating price over a nonnegative domain by a separately written numerical optimizer.

The production branch labels `R1/R2/... ` and the symbolic active-set formulas are not inputs to this evaluator.

## Adversarial parameter set
The evaluator attacks:
[
z=0.01,0.05,0.10,0.20,0.28,0.30,
z_c\pm10^{-6},z_c,0.31,0.32,1/3-10^{-6},
]
with additional points inside the high-`z` mixed region.

It also contains the exact dimensioned regression
[
(\sigma,\Delta)=(25,8).
]

## Findings

### A. Source pure profile
For `z<z_c`, no positive unilateral improvement is found for either segment control at the source profile.

For `z>z_c`, the independent poaching optimizer finds the same strict profitable deviation predicted by the symbolic gain polynomial.

At `(sigma,Delta)=(25,8)`, the independently evaluated total gain equals `23/225`.

### B. Pure nonexistence wedge
The symbolic proof that no kink can be a mutual local best response is attacked by direct best-response maximization on both sides of every relevant threshold. No alternative pure fixed point is found in `z_c<z<1/3`.

This numerical evidence is diagnostic; the analytic active-set/exhaustiveness proof remains the certification basis for pure nonexistence.

### C. Symmetric semi-mixed continuation
For every attacked high-`z` point, the candidate
[
p^*=z(3+2\sqrt3)/3,
quad q_L=p^*/2,
quad q_H=z(2+\sqrt3)/3,
]
with
[
\lambda=[4-(5+3\sqrt3)z]/[z(1+\sqrt3)]
]
passes all three independent tests:
- `q_L` and `q_H` deliver the same primitive poaching payoff;
- no other nonnegative poaching price yields a larger primitive payoff;
- `p^*` globally maximizes the incumbent's expected primitive payoff against the two-point poaching mixture.

The support and mixture therefore define a valid Nash equilibrium of each `UU` segment game.

### D. Related Stage-III profiles
The same independent global-deviation logic reproduces the structural classification:
- no information (8): affected;
- one invests/shares (9): affected through one `UU` segment;
- both invest/no share (10): no corresponding profitable `UU` deviation;
- one invests/no share (11): affected through one `UU` segment;
- asymmetric sharing/both invest (17): no corresponding profitable `UU` deviation;
- full information (6)–(7): no corresponding profitable `UU` deviation.

## Quantifier / alternative-equilibrium audit
Two different questions are separated:

1. **Does the displayed mixed profile constitute an equilibrium?**  
   PASS.

2. **Is it the unique equilibrium in the unrestricted mixed-strategy space?**  
   NOT YET CERTIFIED.

The second question is not inferred from the first. Therefore the publication-safe wording is currently “a certified symmetric mixed continuation” rather than “the unique mixed equilibrium.”

## Welfare-selection consequence
Until mixed uniqueness or payoff-equivalence across all mixed equilibria is established, high-`z` Stage-II and welfare statements derived from this continuation must carry a selection qualifier.

This limitation does not affect:
- the exact source-profile counterexample;
- the complete pure-strategy correspondence;
- pure nonexistence on the high-`z` wedge.

## Formal-verification applicability
**APPLICABLE.**

Proof-critical targets:
1. critical-root identity for `z_c`;
2. gain factorization/sign direction;
3. exact `23/225` counterexample;
4. mixed-support poaching-profit indifference;
5. corrected investment-threshold algebra;
6. selected profit/consumer-surplus/total-welfare identities.

Artifacts:
- `formal/SS2013Reassessment.lean`
- `lean-toolchain`
- `lakefile.lean`
- `lake-manifest.json`
- `.github/workflows/verify.yml`

The formal file explicitly does **not** encode branch exhaustiveness or mixed-equilibrium uniqueness. Those remain economic/mathematical certification tasks outside the proof assistant.

## Current verdict
**CONDITIONAL PASS.**

Passed:
- exact counterexample independence;
- pure-equilibrium globality/nonexistence attack;
- existence/global best-response certification of the symmetric semi-mixed continuation;
- affected-subgame classification.

Open before Stage 8:
- formal Lean clean-build / axiom audit evidence;
- unrestricted mixed-equilibrium uniqueness or an explicit final-paper selection-scope decision.

## Rollback rule
Any failure of the independent primitive evaluator or Lean statement fidelity reopens Stage 4. Discovery of another mixed equilibrium does not invalidate the source correction; it changes the downstream quantifier to an equilibrium correspondence and reopens Stage 7 selection robustness.
