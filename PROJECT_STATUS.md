# Project Status

## Target
Oz Shy and Rune Stenbacka (2013), “Investment in Customer Recognition and Information Exchange,” *Information Economics and Policy* 25(2), 92–106.

## Canonical workflow
`ryotamatsuki/research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7` — v2.4.

## Current stage
**Stage 4A — Independent Mathematical Adversarial Certification**

## Closed stages
- Stage 0 — Evidence Freeze: **CLOSED — CONDITIONAL GO**
  - closure commit: `0481e77caa6fa50860d9bbf02ab9b5597a0aaeca`
  - source-version condition carried forward.
- Stage 1 — Source & Mathematical Audit: **CLOSED — PASS, SOURCE-VERSION QUALIFIED**
  - closure commit: `0d7d2b5d3ae541e4dd78e86a01fc5b898282610e`
  - VOR/WP equation-level comparison remains open.
- Stage 2 — Literature Frontier / Novelty Kill: **CLOSED — GO**
  - closure commit: `dd8d462fdd44472174947b4a7a861f1ce7a1b7d9`
  - generic mixed-pricing novelty rejected; source-specific correction/reassessment survives.
- Stage 3 — Candidate Paper Architecture: **CLOSED — GO, ARCHITECTURE B**
  - closure commit: `65c9b5bfdd29191ce633e161067cbbdad4c4058e`
- Stage 4 — Clipped Stage-III Price-Game Construction: **CLOSED — GO**
  - closure commit: `ee7a065fcd675a3406f56501ba46cefd223df190`
  - construction scope: complete pure correspondence plus an explicit selected symmetric semi-mixed continuation; unrestricted mixed-equilibrium uniqueness is not claimed.

## Frozen Stage-4 construction result
Let
[
z=\Delta/\sigma,qquad
z_c={-6+4\sqrt3\over3}.
]

Under Assumption 2, `0<z<1/3`:
- `0<z<=z_c`: Eq. (8) is the unique pure no-information price equilibrium;
- `z_c<z<1/3`: no pure-strategy no-information price equilibrium exists;
- on the high-`z` wedge, a closed-form symmetric semi-mixed continuation has been constructed;
- Eqs. (9) and (11) inherit the corrected `UU` component;
- Eqs. (6)–(7), (10), and (17) survive the Stage-4 global construction audit.

Permanent exact regression:
[
(\sigma,\Delta)=(25,8),qquad \Delta\pi=23/225>0.
]

## Current Stage-4A obligations
- independently reconstruct primitive clipped demand without the Stage-4 branch labels;
- attack every candidate/global deviation;
- separately search for alternative mixed equilibria;
- distinguish candidate-equilibrium validity from uniqueness/completeness;
- decide the downstream equilibrium-selection quantifier;
- preserve the exact counterexample and threshold regressions;
- record formal-verification applicability and targets.

## Still open
- unrestricted mixed-equilibrium uniqueness/completeness;
- Stage 4A independent certification closure;
- Stage 6 novelty re-kill;
- Stage 7 final backward-induction/welfare closure;
- Stage 7.5/7.5A scope and formal-verification closure;
- VOR equation-level comparison;
- Stage 8 theory freeze and all manuscript/submission stages.

## Production branch
`research/stage-04-price-game`

## Main-branch policy
No merge to `main` has been performed or authorized.
