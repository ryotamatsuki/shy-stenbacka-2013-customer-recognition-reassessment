# Project Status

## Target
Oz Shy and Rune Stenbacka (2013), “Investment in Customer Recognition and Information Exchange,” *Information Economics and Policy* 25(2), 92–106.

## Canonical workflow
`ryotamatsuki/research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7` — v2.4.

## Current routing
**Stage 4A CLOSED. Stage 5 NOT INVOKED. Next gate: Stage 6 — Novelty Re-Kill.**

## Closed stages
- Stage 0 — Evidence Freeze: **CLOSED — CONDITIONAL GO**
  - closure commit: `0481e77caa6fa50860d9bbf02ab9b5597a0aaeca`
  - source-version condition carried forward.
- Stage 1 — Source & Mathematical Audit: **CLOSED — PASS, SOURCE-VERSION QUALIFIED**
  - closure commit: `0d7d2b5d3ae541e4dd78e86a01fc5b898282610e`
  - VOR/WP equation-level comparison remains open.
- Stage 2 — Literature Frontier / Novelty Kill: **CLOSED — GO**
  - closure commit: `dd8d462fdd44472174947b4a7a861f1ce7a1b7d9`
- Stage 3 — Candidate Paper Architecture: **CLOSED — GO, ARCHITECTURE B**
  - closure commit: `65c9b5bfdd29191ce633e161067cbbdad4c4058e`
- Stage 4 — Clipped Stage-III Price-Game Construction: **CLOSED — GO**
  - closure commit: `ee7a065fcd675a3406f56501ba46cefd223df190`
- Stage 4A — Independent Mathematical Adversarial Certification: **CLOSED — GO**
  - canonical closure/revalidation commit: `a61da0f08566fd60bd1b1de7c4e54134e02a84c0`
  - prior closure-record commit: `6f14272b7629d7631cf155504eb0a7daf53ff6d9`
  - verdict: `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`
  - unrestricted mixed-equilibrium uniqueness is not claimed; high-`z` downstream claims must retain the certified selected-continuation qualifier.

## Stage 5 routing
**NOT INVOKED.**

Reason: Stage 4A found no single diagnosed economic deficiency requiring an authorized model modification. No primitive, timing, strategy-set, or equilibrium-concept repair is authorized.

## Frozen Stage-4/4A mathematical scope
Let
[
z=\Delta/\sigma,qquad z_c={-6+4\sqrt3\over3}.
]

Under Assumption 2, `0<z<1/3`:
- `0<z<=z_c`: the source Eq. (8) profile is the unique pure no-information equilibrium;
- `z_c<z<1/3`: no pure-strategy no-information equilibrium exists;
- for every `z_c<z<1/3`, a certified symmetric two-point mixed continuation exists;
- unrestricted mixed-equilibrium uniqueness/completeness is not asserted;
- Eqs. (9) and (11) inherit the corrected `UU` component;
- Eqs. (6)–(7), (10), and (17) survive the global price-game audit.

Permanent exact regression:
[
(\sigma,\Delta)=(25,8),qquad \Delta\pi=23/225>0.
]

## Stage-4A certification status
- independent primitive reconstruction: PASS
- candidate-deviation audit: PASS
- pure alternative-equilibrium audit: PASS / COMPLETE
- high-`z` mixed existence/global best response: PASS
- alternative mixed-equilibrium falsification search: EXECUTED
- unrestricted mixed uniqueness: OUTSIDE CLAIM / UNRESOLVED
- threshold/mixed-support indifference audit: PASS
- zero-demand/boundary/regime audit: PASS
- selection/refinement audit: PASS WITH EXPLICIT SELECTION SCOPE
- formal-verification applicability: APPLICABLE
- formal proof-assistant closure: RESERVED FOR STAGE 7.5A

## Publication-safe quantifier
For the high-`z` wedge, the permitted downstream wording is equivalent to:

> Under the certified symmetric two-point Stage-III continuation constructed here, ...

Prohibited unless a later theorem strengthens the result:
- “the unique mixed equilibrium”;
- “the complete mixed-equilibrium correspondence”;
- selection-free high-`z` SPE or welfare claims.

## Next gate
**Stage 6 — Novelty Re-Kill.**

Stage 6 must re-run exact-correction and theorem-absorption searches against the now-frozen Stage-4/4A theorem set, especially:
1. the exact threshold `z_c`;
2. pure nonexistence on an admissible source-model wedge;
3. the source-specific two-point continuation;
4. corrected downstream investment/sharing/welfare implications.

## Still open beyond Stage 4A
- Stage 6 novelty re-kill;
- Stage 7 final backward-induction/welfare closure;
- Stage 7.5 paper-scale decision;
- Stage 7.5A generality/quantifier red team and formal-verification closure;
- VOR equation-level comparison;
- Stage 8 theory freeze;
- Stages 9–14 reproducibility, paper build, referee gate, positioning, integration, and submission QA.

## Production branch
`research/stage-04-price-game`

## Main-branch policy
No merge to `main` has been performed or authorized.


## Stage-4A final revalidation
Fresh independent execution before final closure reconfirmed:
- `z_c = 0.3094010767585029`;
- source-profile globality below the threshold and profitable poaching deviation above it;
- selected mixed-continuation best-response residuals at numerical roundoff scale;
- two-by-two-support alternative-mixed falsification search with no numerically distinct low-regret equilibrium found.

These numerical searches are diagnostic where stated. The analytic active-set proof remains the certification basis for pure-equilibrium completeness, and unrestricted mixed uniqueness remains outside the certified claim.

Canonical Stage-4A closure/revalidation commit:
`a61da0f08566fd60bd1b1de7c4e54134e02a84c0`.
