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
**GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS.**

Passed:
- exact counterexample independence;
- pure-equilibrium globality/nonexistence attack;
- existence/global best-response certification of the symmetric semi-mixed continuation;
- affected-subgame classification.

Scope decision made at Stage 4A:
- unrestricted mixed-equilibrium uniqueness is **not** claimed;
- every high-`z` downstream statement that uses the displayed continuation must be stated explicitly as conditional on the certified symmetric two-point continuation;
- selection-free high-`z` SPE/welfare language is prohibited unless Stage 7.5A later proves equilibrium uniqueness or payoff/welfare invariance.

Formal proof-assistant implementation is carried to Stage 7.5A, which is the workflow's formal-verification closure gate. Stage 4A records applicability and targets but does not rely on Lean as its independent certification evidence.

## Rollback rule
Any failure of the independent primitive evaluator or Lean statement fidelity reopens Stage 4. Discovery of another mixed equilibrium does not invalidate the source correction; it changes the downstream quantifier to an equilibrium correspondence and reopens Stage 7 selection robustness.


## Theorem-certificate table

| ID | Exact claim and domain | Candidate-deviation audit | Alternative-equilibrium audit | Indifference / boundary audit | Independent evidence | Equilibrium-set status | Certificate |
|---|---|---|---|---|---|---|---|
| C4A-1 | For `0<z<=z_c`, the source `UU` profile is the unique pure equilibrium; for `z_c<z<1/3`, no pure equilibrium exists. Prices range over the nonnegative reals. | Primitive global maximization plus analytic active-set proof. | Every smooth branch, kink, flat-demand boundary, and zero-price boundary is exhausted. | At `z=z_c`, the poacher's second payoff-equal reply is tested against the incumbent response and does not generate another mutual pure best response. | `code/stage04a_primitive_evaluator.py`; `derivations/stage04_active_set_certificate.md`; exact regression. | `UNIQUE` below/at `z_c`; `EMPTY` in pure strategies above `z_c`. | **PASS** |
| C4A-2 | For `z_c<z<1/3`, the displayed `p^*,q_L,q_H,lambda` profile is a Nash equilibrium of each `UU` segment game. Claim is existence only. | Both poaching support actions are globally optimal from primitive demand; `p^*` globally maximizes expected incumbent payoff. | Separate two-by-two-support falsification search performed. No distinct low-regret alternative found, but unrestricted uniqueness is not inferred. | Poacher support indifference is material: changing the mixing probability changes the incumbent best-response condition; only the displayed weight is used. | `code/stage04a_primitive_evaluator.py`; `code/stage04a_mixed_alternative_search.py`; `derivations/stage04a_mixed_alternative_search.md`. | `EXISTENCE ONLY`; unrestricted multiplicity remains unresolved and outside the claim. | **PASS AT EXPLICIT EXISTENCE/SELECTION SCOPE** |
| C4A-3 | Type-specific/type-specific (`TT`) continuation profiles used in Eqs. (6)–(7), (9), and (17) are global best-response profiles under `0<z<1/3`. | Direct clipped-demand reconstruction and finite/global deviations. | Type-level interior vertices and clipping boundaries checked. | Zero-demand/full-retention plateaus do not create mutual alternatives. | Stage-4 active-set certificate plus primitive evaluator logic. | Source continuation globally certified on stated domain. | **PASS** |
| C4A-4 | Type-specific-incumbent/uniform-poacher (`TU`) continuation profiles used in Eqs. (10), (11), and (17) are globally valid under `0<z<1/3`. | Each incumbent control checked separately; common poacher tested across type-drop regimes. | Later three-active and one-active vertices lie to the left of their regime boundaries; no recovering branch maximum. | Type-exit kinks and zero-demand groups explicitly tested. | `derivations/stage04_active_set_certificate.md`; primitive reconstruction. | Source `TU` continuation globally certified. | **PASS** |
| C4A-5 | Equation impact map: (8) affected; (9),(11) affected through `UU`; (6)–(7),(10),(17) survive the price-game audit. | Reconstructed by information-set component rather than source FOCs. | No hidden `UU` component found in the unaffected histories. | Off-path price-control availability mapped in Stage 1 and re-used only after primitive certification. | Stage-1 control map; Stage-4/4A certificates. | Classification certified. | **PASS** |

## Quantifier certificate

The maximum certified Stage-4A statements are:

1. **Pure correspondence theorem.** For every `z` with `0<z<1/3`, over nonnegative prices, the `UU` segment has the source profile as its unique pure equilibrium iff `z<=z_c`; it has no pure equilibrium if `z>z_c`.
2. **Mixed existence theorem.** For every `z_c<z<1/3`, there exists the displayed symmetric two-point continuation.
3. **No unrestricted mixed uniqueness theorem is claimed.**
4. High-`z` Stage-II, Stage-I, profit, consumer-surplus, and welfare results derived later are **selected-continuation results**, unless a later gate proves selection invariance.

Prohibited wording at the current certification level:
- “the unique mixed equilibrium”;
- “the complete mixed-equilibrium correspondence”;
- any selection-free high-`z` welfare/SPE statement.

## Candidate-deviation audit

The independent evaluator reconstructs customer switching from utilities and clips each type mass directly to `[0,1]`. It does not call the Stage-4 symbolic branch solver.

For the source pure profile:
- below `z_c`, no profitable incumbent or poacher deviation is found;
- above `z_c`, the poacher deviation is recovered independently;
- at `(sigma,Delta)=(25,8)`, the dimensioned gain is exactly `23/225`.

For the selected mixed profile:
- both poaching support atoms deliver the same payoff;
- a global nonnegative-price search finds no superior poaching action;
- a global expected-payoff search finds no superior incumbent action.

The analytic Stage-4 certificate, not the numerical optimizer, supplies the proof of pure branch exhaustiveness.

## Alternative-equilibrium / multiplicity audit

The pure game is fully characterized analytically. The mixed game is treated differently.

A separate diagnostic, `code/stage04a_mixed_alternative_search.py`, searches two-atom incumbent by two-atom poacher mixtures at interior high-`z` points using primitive payoffs and maximum unilateral regret. The resulting low-regret profiles collapse the incumbent support near `p^*` and recover the two poaching atoms and probability mass up to numerical tolerance. No numerically distinct low-regret equilibrium was found in that search class.

This diagnostic **does not prove unrestricted mixed uniqueness**. Accordingly:
- C4A-2 is certified as an existence claim only;
- unrestricted mixed multiplicity is recorded as unresolved rather than silently ruled out;
- later economic conclusions must preserve the selected-continuation qualifier.

## Indifference / zero-payoff trigger audit

Two material indifference classes were audited.

### Threshold indifference at z=z_c
At the source incumbent price, the poacher has two payoff-equal best replies at the threshold. Replacing `q=1/3` by the higher reply changes the incumbent's best response; the source incumbent price is then not optimal. Hence the second poaching reply does **not** generate an additional pure equilibrium. Pure-equilibrium uniqueness at `z=z_c` is preserved.

### Mixed-support indifference above z_c
The poacher is indifferent between `q_L` and `q_H`, but the mixing probability is not behaviorally irrelevant. Moving probability mass within the indifferent support changes the incumbent's expected marginal payoff and hence its best-response condition. The displayed `lambda(z)` is therefore part of the equilibrium construction and cannot be dropped as an arbitrary tie-break.

Flat zero-demand/full-capture regions and zero-price boundaries were included in the active-set audit. None generates an omitted mutual pure best response.

## Equilibrium-selection / refinement audit

No ad hoc refinement, weak-dominance deletion, price floor, no-loss restriction, or new tie-breaking assumption is used to eliminate equilibria.

For high `z`, the paper makes an explicit **analysis-scope selection**: it constructs one certified symmetric mixed continuation and reports downstream implications conditional on that continuation. This is not represented as a refinement implied by the original model.

Claims that survive without any mixed selection:
- the exact source counterexample;
- the threshold `z_c`;
- the complete pure-strategy correspondence;
- pure nonexistence on the high-`z` wedge;
- the `TT/TU/UU` affected-subgame classification.

Claims requiring the displayed high-`z` continuation:
- corrected high-`z` investment thresholds;
- high-`z` profit and consumer-surplus crossings;
- high-`z` Stage-I implications;
- high-`z` welfare accounting.

## Global boundary/regime audit

The following were explicitly attacked:
- every smooth positive-slope active-set branch;
- every kink generated by a type entering/exiting switching demand;
- flat zero-demand/full-capture regions;
- `p=0` and `q=0`;
- `z_c-10^{-6}`, `z_c`, and `z_c+10^{-6}`;
- the upper maintained boundary `z -> 1/3`;
- `TT` and `TU` histories with type-specific controls;
- the mixed support at several interior high-`z` points.

No unresolved candidate-deviation class remains for the claims as scoped.

## Continuation audit

Stage 4A certifies the Stage-III price continuations needed by the selected Architecture B:
- `TT+TT`;
- `UU+UU`;
- `TT+UU`;
- `TU+TU`;
- `TU+UU`;
- `TT+TU`.

Stage 7 must regenerate Stage-II and Stage-I behavior from these certified continuation payoffs. It may not reuse a source payoff table where a `UU` component is affected.

## Welfare-selection and benchmark-definition audit

No unconditional high-`z` welfare theorem is certified at Stage 4A. Welfare identities belong to Stage 7.

The only Stage-4A welfare certificate is a scope constraint: any welfare comparison using the selected high-`z` mixed continuation must state that selection. Selection-free welfare language is blocked until equilibrium invariance is proved.

## Evidence ledger

| Claim | Attack performed | Artifact | Result | Surviving limitation | State |
|---|---|---|---|---|---|
| Eq. (8) source globality | primitive global BR search + analytic active-set exhaustiveness | `code/stage04a_primitive_evaluator.py`; `derivations/stage04_active_set_certificate.md` | threshold reproduced | VOR equation identity remains source-version qualified | PASS |
| exact counterexample | independent clipped-payoff evaluation | `code/stage01_cleanroom_reproduction.py`; Stage-4A evaluator | `23/225>0` | none for inspected model | PASS |
| pure nonexistence | all smooth branches + all kinks/boundaries + direct BR attack | Stage-4 active-set certificate; Stage-4A evaluator | no pure equilibrium above `z_c` | mixed strategies required | PASS |
| selected mixed continuation | primitive support/global BR attack | Stage-4A evaluator | valid Nash equilibrium | unrestricted mixed uniqueness not claimed | PASS at existence scope |
| alternative mixed equilibrium | separate 2x2-support regret search | `code/stage04a_mixed_alternative_search.py` | no distinct low-regret alternative found | diagnostic only; no uniqueness theorem | PASS as falsification search |
| `TT` continuation | type-level clipped-payoff/global vertex attack | Stage-4 certificate | survives | model/source-version qualification | PASS |
| `TU` continuation | type-drop regime and common-price deviation attack | Stage-4 certificate | survives | model/source-version qualification | PASS |
| downstream selection | vary payoff-indifferent poacher support weight conceptually and recompute incumbent condition | mixed construction identities | weight is material | high-`z` results selection-dependent | PASS with explicit qualifier |

## Formal-verification applicability and target map

**FORMALIZATION APPLICABLE.**

The proof-assistant closure gate is Stage 7.5A, not Stage 4A. The target map carried forward is:

1. critical-root identity and root ordering;
2. gain factorization/sign;
3. exact `23/225` counterexample;
4. mixed-support indifference;
5. corrected investment-threshold identities;
6. profit/consumer-surplus/total-welfare identities;
7. any compact algebraic inequality used in the final theorem statements.

The existing Lean artifact is supportive engineering only at this stage and is not counted as the independent Stage-4A certification.

## Permanent regression tests

Permanent artifacts now include:
- exact rational `23/225` counterexample;
- threshold-root/sign regression;
- source-profile primitive global-BR tests around `z_c`;
- selected mixed-support/global-BR tests;
- active-set symbolic certificate;
- related `TT/TU` component identities;
- diagnostic alternative-mixed search.

## Formal closure record

- Stage: 4A — Independent Mathematical Adversarial Certification
- Closure input SHA: `88e27b70ea05e9599252372d1271be3e80be4024`
- Candidate-deviation audit: **PASS**.
- Pure alternative-equilibrium audit: **PASS / COMPLETE**.
- Mixed alternative-equilibrium audit: **EXECUTED; unrestricted uniqueness deliberately not claimed**.
- Indifference audit: **PASS**.
- Boundary/regime audit: **PASS**.
- Selection/refinement audit: **PASS WITH EXPLICIT SELECTED-CONTINUATION SCOPE**.
- Formalization applicability: **APPLICABLE; target map frozen for Stage 7.5A**.
- No model repair is authorized or required by this gate.
- Exact correctness blocker remaining at Stage 4A scope: **NONE**.
- Canonical verdict: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS.**
- Routing: proceed to **Stage 6 — Novelty Re-Kill**. Stage 5 is not invoked because Stage 4A found no diagnosed economic deficiency requiring a model modification.


## Final closure revalidation — 2026-09-23

A fresh independent execution of the primitive payoff logic was performed before treating this gate as formally closed.

Revalidated numerical facts:
- critical ratio: `z_c = 0.3094010767585029`;
- for source-profile tests strictly below `z_c`, no positive incumbent or poacher gain was found beyond numerical tolerance;
- immediately above `z_c`, the primitive poaching optimizer recovers a strictly positive deviation gain;
- for the selected high-`z` mixed continuation, the largest incumbent best-response residual over the revalidation grid was approximately `1.18e-14`;
- the largest poacher best-response residual was approximately `1.33e-15`;
- support-payoff gaps were numerically zero at the tested points.

The separate two-incumbent-atom/two-poacher-atom falsification search was also reproduced at `z=0.318,0.325,0.330`. Continuous exploitabilities were approximately:
- `1.34e-7` at `z=0.318`;
- `1.41e-6` at `z=0.325`;
- `7.74e-7` at `z=0.330`.

These solutions collapse close to the selected incumbent price and selected poaching support. This remains diagnostic falsification evidence only and is not promoted to a mixed-uniqueness theorem.

GitHub combined-status metadata for the earlier closure commit did not expose a completed status check through the connector. This does not weaken Stage 4A because Lean/CI is not used as its closure evidence; the proof-assistant clean-build and axiom-audit gate remains explicitly assigned to Stage 7.5A.

### Final gate decision
- Candidate-deviation completeness at the certified scope: **PASS**.
- Pure equilibrium-set completeness: **PASS**.
- Selected mixed equilibrium existence/global best response: **PASS**.
- Unrestricted mixed uniqueness: **OUTSIDE CLAIM; unresolved**.
- Selection qualifier: **MANDATORY** for high-`z` downstream claims.
- Stage 5 model repair: **NOT INVOKED**.
- Stage-4A exact correctness blocker: **NONE**.

**FINAL VERDICT: STAGE 4A FORMALLY CLOSED — GO.**

The next canonical gate is **Stage 6 — Novelty Re-Kill**. Stage 5 is recorded as not invoked rather than silently skipped.
