# Project Status

## Target
Oz Shy and Rune Stenbacka (2013), “Investment in Customer Recognition and Information Exchange,” *Information Economics and Policy* 25(2), 92–106.

## Canonical workflow
\`ryotamatsuki/research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7\` — v2.4.

## Current routing
**Stage 7.5 CLOSED — GO. Stage 7.5A CONDITIONAL GO pending formal build/axiom evidence.**

## Closed stages
- Stage 0 — Evidence Freeze: **CLOSED — CONDITIONAL GO**
  - closure commit: \`0481e77caa6fa50860d9bbf02ab9b5597a0aaeca\`
  - VOR equation-level qualification carried forward.
- Stage 1 — Source & Mathematical Audit: **CLOSED — PASS, SOURCE-VERSION QUALIFIED**
  - closure commit: \`0d7d2b5d3ae541e4dd78e86a01fc5b898282610e\`
- Stage 2 — Literature Frontier / Novelty Kill: **CLOSED — GO**
  - closure commit: \`dd8d462fdd44472174947b4a7a861f1ce7a1b7d9\`
- Stage 3 — Candidate Paper Architecture: **CLOSED — GO, ARCHITECTURE B**
  - closure commit: \`65c9b5bfdd29191ce633e161067cbbdad4c4058e\`
- Stage 4 — Clipped Stage-III Price-Game Construction: **CLOSED — GO**
  - closure commit: \`ee7a065fcd675a3406f56501ba46cefd223df190\`
- Stage 4A — Independent Mathematical Adversarial Certification: **CLOSED — GO**
  - canonical revalidation commit: \`a61da0f08566fd60bd1b1de7c4e54134e02a84c0\`
  - unrestricted mixed-equilibrium uniqueness is not claimed.
- Stage 5 — Minimal Model Repair: **NOT INVOKED**
  - no economic primitive/timing/strategy-set repair was required.
- Stage 6 — Novelty Re-Kill: **CLOSED — GO**
  - closure commit: \`ab72c6db0d670f4cb553b12ca1a6a6991856f79e\`
- Stage 7 — Welfare / Generality / Institutional Validation: **CLOSED — GO**
  - closure commit: \`0c512d37be0c0a195653f62885a4280ac43f0f01\`
  - independent equilibrium-correspondence audit: PASS
  - primitive consumer-surplus/welfare reconstruction: PASS
  - institutional plausibility audit: PASS with no policy-causal claim
  - result-to-exposition triage: complete

## Frozen Stage-7 economic results

### Corrected acquisition thresholds
For \`0<z<=z_c\`:
\[
K_S={2z^2\over9},\qquad K_{NS}={z^2\over2}.
\]

For \`z_c<z<1/3\`, under the certified symmetric two-point Stage-III continuation:
\[
K_S=
{(17+9\sqrt3)z^2-(30+18\sqrt3)z+16\over9},
\]
\[
K_{NS}=
{(39+18\sqrt3)z^2-(60+36\sqrt3)z+32\over18}.
\]

Always:
\[
K_{NS}-K_S={5z^2\over18}>0.
\]

Zeros:
\[
z_S^0\approx0.314086968713884,
\qquad
z_{NS}^0\approx0.320424885817143.
\]

### Stage-II correspondence
For symmetric sharing status \`X in {S,NS}\` with threshold \`K_X\`:
- \`k<K_X\`: unique \`(I,I)\`;
- \`k>K_X\`: unique \`(NI,NI)\`;
- \`k=K_X\`: all four pure investment profiles.

For asymmetric \`(S,NS)\`, the sharer uses threshold \`K_S\` and the non-sharer threshold \`K_{NS}\`, including explicit equality correspondences.

### Stage-I correspondence
- if \`K_{NS}>0\` and \`0<=k<K_{NS}\`: \`(NS,NS)\` is the unique Stage-I action profile compatible with SPE;
- this uniqueness includes the lower equality \`k=K_S\`;
- if \`k>=K_{NS}\`: all four Stage-I sharing profiles are SPE-compatible;
- if \`K_{NS}<=0\`: all four Stage-I sharing profiles are compatible for every feasible \`k>=0\`, because no information acquisition occurs.

### Profit / consumer surplus / welfare
Selected high-\`z\` gross-profit crossings:
- \`M=F\` at \`z≈0.315231824630597\`;
- \`M=N\` at \`z≈0.315991499774449\`.

Consumer-surplus crossings:
- \`CS_M=CS_{NS}\` at \`z≈0.318731295698269\`;
- \`CS_M=CS_S\` at \`z≈0.320586070246451\`.

Total welfare:
\[
W(NI)>W(NS,I)>W(S,I)
\]
survives over the full maintained model domain at the certified quantifier.

### Results 1–10
- Results 1, 2, 3, 5, 8, 9: **corrected**.
- Result 4: **survives** at certified continuation scope.
- Result 6: **false globally; corrected ranking required**.
- Result 7: **survives as outcome-welfare ordering**.
- Result 10: **welfare logic survives with corrected private threshold; source-display typos remain separate**.

## Stage-7 scope boundary
High-\`z\` downstream results remain conditional on the certified symmetric two-point Stage-III continuation.

Not licensed:
- “the unique mixed equilibrium”;
- “the complete mixed-equilibrium correspondence”;
- selection-free high-\`z\` SPE/welfare claims;
- cross-model portability claims;
- policy-causal claims from the institutional anchors.

## Next gate — Stage 7.5
The Full-Theory Freeze Decision must decide whether the surviving contribution is strong enough for full-paper investment rather than a short correction/note. It must assess:
1. whether the mechanism can be stated without model-specific notation;
2. the minimal causal/strategic chain;
3. essential versus tractability assumptions;
4. whether at least one credible alternative formulation has already been tested or must be reserved for Stage 7.5A;
5. whether the welfare/organizational implications are substantive;
6. whether the contribution is more than a parameter exercise;
7. the appropriate full-paper versus research-note route.

Stage 7.5 cannot freeze theory; a GO routes to Stage 7.5A.

## Still open
- Stage 7.5 Full-Theory Freeze Decision;
- Stage 7.5A generality/quantifier/portability red team;
- Stage 7.5A Formal Verification Gate;
- VOR equation-level comparison;
- Stage 8 theory freeze;
- Stages 9–14 reproducibility, manuscript build, referee gate, positioning, integration, and submission QA.

## Production branch
\`research/stage-07-backward-welfare\`

## Main-branch policy
No merge to \`main\` has been performed or authorized.


## Stage-7.5A portability state
Two pre-specified attacks were re-solved:
- Beta(2,2) switching-cost distribution;
- unequal type masses (1,1.25,0.75,1).

Both retain pure profiles at attacked high-z points where the baseline equal-mass/uniform-switching model has no pure equilibrium. Stop rule triggered. No generality rescue is authorized.

## Formal gate state
Draft verification PR: #3 (verification only; do not merge).
Workflow run #67 is currently the evidence source for the formal-verification gate.
