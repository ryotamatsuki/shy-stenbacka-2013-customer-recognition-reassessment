# Stage 7.5A — Portability Falsification Diagnostics

Date: 2026-09-23

## Pre-specified mechanism invariant

The candidate cross-model mechanism was:

> A common price over heterogeneous switching segments can become globally unstable because crossing a demand kink sacrifices one segment and improves poaching profit, producing a qualitative equilibrium-regime change.

The test is deliberately weaker than preserving the exact baseline threshold or two-point support. Portability would require an analogous global-equilibrium failure to survive credible changes in a result-driving primitive.

## Attack A — non-uniform switching costs

### Pre-specification
Replace the baseline uniform switching-cost distribution on \([0,1]\) by Beta(2,2), with CDF
\[
H(s)=3s^2-2s^3,\qquad s\in[0,1].
\]
Retain the four valuation offsets and common-price \`UU\` information structure.

### Why economically meaningful
The baseline linear clipped demand and piecewise-quadratic profits come directly from uniform switching costs. A smooth hump-shaped switching-cost distribution is a direct attack on that result-driving assumption.

### Re-solution
The alternative game is solved directly from
\[
D_P(q,p)=\sum_t H(p-q-d_t),
\qquad
D_I(p,q)=4-D_P(q,p),
\]
not by substituting \`H\` into baseline equilibrium formulas.

An initial (801\times801) grid is used only to initialize the alternative-game search. Stage 11 identified that grid regret alone was insufficient evidence against continuous deviations, so the alternatives were revalidated by alternating continuous incumbent and poacher best responses using deterministic differential evolution over prices in ([0,2]), followed by a fresh continuous unilateral-regret calculation.

For (z\in\{0.31,0.32,0.33\}), the Beta(2,2) game converges approximately to:
- (z=0.31): ((p,q)=(0.64150110,0.29847275));
- (z=0.32): ((0.64994906,0.30677534));
- (z=0.33): ((0.65898220,0.31565385)).

The continuous unilateral regret is below (10^{-8}) at each tested point.

### Result
**PORTABILITY FAILURE — CONTINUOUS-BEST-RESPONSE REVALIDATED.**

The baseline high-`z` pure-nonexistence claim does not survive this alternative at the attacked parameter points. This remains numerical diagnostic evidence about the alternative model, not an analytic existence theorem.

This does not affect the correctness of the baseline theorem.

## Attack B — unequal valuation-type masses

### Pre-specification
Keep uniform switching costs and the common-price \`UU\` control, but perturb type masses from
\[
(1,1,1,1)
\]
to
\[
(1,1.25,0.75,1).
\]

### Why economically meaningful
Equal segment masses determine the baseline cancellation and branch payoffs. Customer populations need not place equal weight on the \(+\Delta\) and \(-\Delta\) mismatch groups.

### Re-solution
The weighted demand is rebuilt from primitive clipped switching masses. As in Attack A, the grid is only an initializer; Stage-11 recertification uses continuous alternating best responses and a fresh continuous regret calculation.

At (z\in\{0.31,0.32,0.33\}), the unequal-mass game converges approximately to:
- (z=0.31): ((p,q)=(0.67958336,0.32041668));
- (z=0.32): ((0.67999998,0.31999997));
- (z=0.33): ((0.68041678,0.31958339)).

Continuous unilateral regret is below (10^{-8}) at each tested point.

### Result
**PORTABILITY FAILURE — CONTINUOUS-BEST-RESPONSE REVALIDATED.**

The exact pure-nonexistence mechanism is not robust to this plausible unequal-mass perturbation at the attacked points.

## Stop-rule implication

Two pre-specified, non-cosmetic, result-driving alternatives fail to preserve the baseline high-\`z\` pure-nonexistence claim.

Accordingly, the workflow stop rule applies:

- do not redesign further alternatives to rescue a broad claim;
- classify the exact pure-nonexistence / two-point-mixed mechanism as **MODEL-SPECIFIC**;
- preserve the negative portability evidence;
- do not market the paper as a general theorem about customer recognition or common-price competition.

## What remains portable at a weaker conceptual level

Only a cautious conceptual statement survives:

> Common controls over heterogeneous segments require global, not merely local, equilibrium analysis because segment-entry/exit boundaries can matter.

That statement is methodological/economic intuition, not a certified cross-model theorem.

## Artifact

\`code/stage075a_portability_attacks.py\`

The code intentionally reports numerical diagnostic evidence only. It is not used to prove the baseline Stage-4 theorem.


## Stage-11 certification-regression record

Stage 11 classified the original grid-only portability implementation as a **certification regression** because a grid Nash candidate does not exclude profitable off-grid deviations.

Repair:
- grid retained only as initialization;
- continuous incumbent and poacher best responses added;
- final continuous unilateral regret required to be below (10^{-8});
- both pre-specified portability failures survive the stronger audit.

The Stage-7.5A portability classification is therefore recertified without changing the frozen baseline theorem or contribution scope.
