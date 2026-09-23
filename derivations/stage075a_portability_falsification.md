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

A dense \(1601\times1601\) price-grid revalidation at
\[
z\in\{0.31,0.32,0.33\}
\]
found pure profiles with zero grid regret at the displayed numerical resolution. Representative pairs were approximately:
- \(z=0.31\): \((p,q)=(0.64125,0.29850)\);
- \(z=0.32\): \((0.65025,0.30675)\);
- \(z=0.33\): \((0.65925,0.31575)\).

### Result
**PORTABILITY FAILURE.**

The baseline claim that the upper admissible region loses pure equilibrium does not survive this alternative. The smooth distribution changes the global best-response geometry enough to retain a pure profile throughout the attacked high-\`z\` points.

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
The weighted demand is rebuilt from primitive clipped switching masses and the game is re-solved on the same dense grid.

At
\[
z\in\{0.31,0.32,0.33\},
\]
the revalidation again found near-zero/zero-grid-regret pure profiles, approximately:
- \(z=0.31\): \((p,q)=(0.67950,0.32025)\);
- \(z=0.32\): \((0.67950,0.31950)\);
- \(z=0.33\): \((0.68025,0.31950)\).

### Result
**PORTABILITY FAILURE.**

The exact pure-nonexistence mechanism is not robust to this plausible unequal-mass perturbation.

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
