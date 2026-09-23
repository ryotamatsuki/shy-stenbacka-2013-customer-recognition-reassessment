# Stage 8 — Canonical Theory Freeze

Date: 2026-09-23  
Workflow: \`research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7\` (v2.4)

## Entry hard gate

- Stage 4A mathematical adversarial certification: **GO**.
- Stage 7.5A generality / quantifier / portability certification: **GO**.
- Formal Verification Gate: **FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE**.
- Stage 6 novelty re-kill: **GO**.
- Stage 7 backward-induction/welfare reconstruction: **GO**.

Entry gate: **PASS**.

## 1. Frozen research question

In the directly inspected Shy–Stenbacka working-paper model, when is the no-information common-price profile globally valid, what equilibrium object is available when the pure profile fails, and how does the corrected Stage-III continuation alter the model's customer-recognition investment, information-sharing, switching, profit, consumer-surplus, and welfare conclusions?

## 2. Frozen source/version scope

The complete mathematical source directly inspected is the Federal Reserve Bank of Boston Working Paper 12-4, dated 15 February 2012, which the Boston Fed identifies as preceding a revised version published in *Information Economics and Policy* 25(2), 92–106 (2013).

The 2013 bibliographic VOR identity, DOI \`10.1016/j.infoecopol.2013.03.002\`, PII \`S0167624513000115\`, volume/issue/pages, and publication lineage are verified.

**Equation-level VOR/WP identity has not been directly verified.**

Therefore frozen publication wording must:
- identify the mathematical object as the directly inspected working-paper model / verified predecessor model;
- avoid “published Eq. (8) is wrong” or equivalent VOR-specific equation attribution;
- state that equation-level VOR comparison remains outside the verified source scope.

A later direct VOR equation comparison may strengthen attribution if identical. A mismatch reopens the source claim map.

## 3. Frozen baseline primitives

Three stages:

1. Stage I: each firm chooses whether to share customer information, \`S\` or \`NS\`.
2. Stage II: each firm chooses whether to acquire recognition information, \`I\` or \`NI\`, paying cost \`c\` if it invests.
3. Stage III: each firm chooses incumbent and poaching prices allowed by its information state.

Consumers have four valuation-type offsets:
\[
d\in\{0,+\Delta,-\Delta,0\},
\]
switching cost \(\sigma s\), with baseline \(s\sim U[0,1]\), and source restriction
\[
0<z\equiv\Delta/\sigma<1/3.
\]

The Stage-III information-control components are:
- \`TT\`: type-specific incumbent and poaching controls;
- \`UU\`: uniform incumbent and poaching controls;
- \`TU\`: type-specific incumbent, uniform poaching control.

The affected no-information component is
\[
F_z(x)=2[x]_0^1+[x+z]_0^1+[x-z]_0^1,\qquad x=p-q,
\]
with normalized payoffs
\[
u_I(p,q)=p[4-F_z(p-q)],\qquad
u_P(q,p)=qF_z(p-q).
\]

## 4. Frozen equilibrium concept and strategy domain

- Stage-III prices: nonnegative real numbers.
- Stage-II investment and Stage-I sharing: pure binary actions for the backward-induction correspondence.
- Stage-III high-\`z\` continuation: a certified mixed Nash equilibrium is used where no pure equilibrium exists.
- Overall sequential solution: subgame-perfect equilibrium compatibility using certified Stage-III continuations and explicit Stage-II multiplicity.

No refinement, price floor, no-loss restriction, or new tie-breaking assumption is added.

## 5. Frozen Stage-III propositions

Let
\[
z_c={-6+4\sqrt3\over3}\approx0.309401076758503.
\]

### P1 — Pure \`UU\` correspondence
**PROVED.**

For every baseline \(z\in(0,1/3)\), over nonnegative pure prices:
- if \(z\le z_c\), \((p,q)=(2/3,1/3)\) is the unique pure segment equilibrium;
- if \(z>z_c\), no pure segment equilibrium exists.

Formal coverage: **PROOF-CRITICAL CORE only**, not the full equilibrium correspondence.

### P2 — Exact counterexample
**PROVED.**

At \((\sigma,\Delta)=(25,8)\), deviating from \(q=25/3\) to \(q=29/3\) against the source incumbent price yields exact gain
\[
23/225>0.
\]

Formal coverage: **FULL ALGEBRAIC CLAIM**.

### P3 — Selected high-\`z\` mixed continuation
**PROVED AS EXISTENCE / GLOBAL BEST-RESPONSE VALIDITY.**

For \(z_c<z<1/3\), a symmetric two-point continuation exists:
\[
p^*=z{3+2\sqrt3\over3},\quad
q_L=z{3+2\sqrt3\over6},\quad
q_H=z{2+\sqrt3\over3},
\]
with
\[
\lambda(z)
={4-(5+3\sqrt3)z\over z(1+\sqrt3)}
\]
on \(q_L\).

**Not proved / not claimed:** unrestricted mixed-equilibrium uniqueness or complete mixed-equilibrium correspondence.

Formal coverage: mixed-support indifference only.

### P4 — Related Stage-III components
**PROVED.**

\`TT\` and \`TU\` source continuations survive global clipped-demand auditing throughout the maintained baseline domain.

Impact map:
- source (6)–(7): survives;
- source (8): corrected;
- source (9): affected through \`UU\`;
- source (10): survives;
- source (11): affected through \`UU\`;
- source (17): survives.

## 6. Frozen Stage-II thresholds and correspondence

Normalize \(k=c/\sigma\).

For \(z\le z_c\):
\[
K_S={2z^2\over9},\qquad K_{NS}={z^2\over2}.
\]

For \(z>z_c\), under P3:
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
z_S^0\approx0.314086968713884,\qquad
z_{NS}^0\approx0.320424885817143.
\]

### Symmetric Stage-I status
For \(X\in\{S,NS\}\):
- \(k<K_X\): unique \((I,I)\);
- \(k>K_X\): unique \((NI,NI)\);
- \(k=K_X\): all four pure Stage-II investment profiles.

### Asymmetric \((S,NS)\)
- sharer invests iff \(k<K_S\);
- non-sharer invests iff \(k<K_{NS}\);
- equality correspondences are retained explicitly.

Classification: **PROVED within the baseline; high-z formulas are selected-continuation results.**

## 7. Frozen Stage-I correspondence

Under the certified continuation:
- if \(K_{NS}>0\) and \(0\le k<K_{NS}\), \((NS,NS)\) is the unique Stage-I action profile compatible with SPE; this includes \(k=K_S\);
- if \(k\ge K_{NS}\), all four Stage-I sharing profiles are SPE-compatible;
- if \(K_{NS}\le0\), no recognition information is acquired for any feasible \(k\ge0\), and all four Stage-I sharing labels are payoff irrelevant / SPE-compatible.

Classification: **PROVED at the certified continuation scope.**

## 8. Frozen switching, profit, consumer surplus, welfare

Selected high-\`z\` per-firm gross profits:
\[
F={4(z^2+5)\over9},\quad
N={9z^2+40\over18},\quad
M={z[(2+\sqrt3)z+10+6\sqrt3]\over3}.
\]

Crossings:
\[
M=F:\ z\approx0.315231824630597,
\]
\[
M=N:\ z\approx0.315991499774449.
\]

Consumer-surplus crossings:
\[
CS_M=CS_{NS}:\ z\approx0.318731295698269,
\]
\[
CS_M=CS_S:\ z\approx0.320586070246451.
\]

The source-style consumer-surplus ordering therefore fails globally in the baseline high-\`z\` region under the selected continuation.

Total welfare:
\[
W(NI)>W(NS,I)>W(S,I)
\]
survives over the maintained baseline domain at the certified quantifier.

The manuscript must distinguish algebraic outcome welfare from equilibrium welfare.

## 9. Frozen Results 1–10 disposition

- Results 1, 2, 3, 5, 8, 9: **CORRECTED**.
- Result 4: **SURVIVES** under the certified continuation.
- Result 6: **FALSE GLOBALLY in the inspected baseline / corrected ranking required**.
- Result 7: **SURVIVES as outcome-welfare ordering**.
- Result 10: **WELFARE LOGIC SURVIVES with corrected private threshold; source-display typo ledger separate**.

These labels refer to the directly inspected source version unless VOR identity is independently verified.

## 10. Portability freeze

Stage 7.5A pre-specified two economically meaningful alternative models:

1. Beta(2,2) switching-cost distribution;
2. unequal type masses \((1,1.25,0.75,1)\).

Both retain pure high-\`z\` profiles at attacked points where the baseline uniform/equal-mass game has no pure equilibrium.

Therefore:
- P1/P3 and downstream high-\`z\` mechanism claims are **MODEL-SPECIFIC**;
- the stop rule is triggered;
- no further result-driven generality rescue is authorized;
- only the methodological intuition that common controls over heterogeneous segments require global regime-aware analysis may be stated generally.

## 11. Formal verification freeze

State: **FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE**.

Evidence:
- GitHub Actions run #71, id \`35840067654\`;
- formal job id \`107112751294\`;
- clean \`lake build\`: PASS;
- axiom-audit: 58 declarations, all within \`propext\`, \`Classical.choice\`, \`Quot.sound\`;
- \`sorry|admit\` placeholder audit: PASS / none found;
- Lean \`v4.35.0-rc2\`;
- mathlib \`b1007d8abfd0c776eb8a75e8f6bf26db5eae4a69\`.

Formalized: proof-critical algebraic identities and signs listed in \`theorem_certificates/FORMAL_VERIFICATION_CERTIFICATE.md\`.

Not formalized: economic primitives, branch exhaustiveness, full-game equilibrium correspondence, unrestricted mixed uniqueness, Stage-I/II game logic, portability, source identity.

## 12. Frozen novelty / closest-literature distinction

Known / not claimed as novel:
- mixed pricing with discrete heterogeneity;
- mixed pricing with switching/captive consumers;
- generic pure-nonexistence-to-mixed transitions in related price games.

Surviving contribution:
- source-specific global-equilibrium correction of the inspected model;
- exact pure validity threshold and pure correspondence;
- constructive selected mixed continuation;
- complete downstream reassessment showing which investment/sharing/profit/CS/welfare conclusions change or survive.

No generic common-control theorem is claimed.

## 13. Institutional interpretation freeze

FTC, CMA, and EU DMA materials support the real-world plausibility of customer-level data acquisition/profiling, competitive importance of data access, information sharing/access, and switching frictions/data portability.

They do not validate the exact four-type distribution, uniform switching costs, simultaneous price structure, or the welfare signs.

No policy-causal claim is authorized.

## 14. Benchmark-definition register

Permitted:
- total welfare;
- outcome-welfare ranking;
- privately selected investment;
- excessive investment relative to the compared no-information outcome where exact.

Prohibited without a new planner problem:
- first best;
- unrestricted social optimum;
- socially optimal information policy in general.

## 15. Counterexample / regression register

Permanent regression objects:
- exact \(23/225\) counterexample;
- threshold root/sign;
- active-set pure-candidate exhaustion;
- primitive Stage-4A best-response attack;
- two-by-two mixed falsification search;
- Stage-II/Stage-I equilibrium-correspondence audit;
- primitive consumer-surplus/welfare integration;
- portability falsification attacks;
- Lean proof-critical core.

## 16. Explicit claims not made

- unrestricted mixed-equilibrium uniqueness;
- complete mixed-equilibrium correspondence;
- selection-free high-\`z\` SPE/welfare conclusions;
- cross-model portability of pure nonexistence;
- generic theorem for arbitrary common-price heterogeneous demand;
- VOR-specific equation error before equation-level VOR inspection;
- empirical estimation or causal policy effect;
- first-best planner result.

## 17. Change control

Any post-freeze change to primitives, strategy sets, equilibrium quantifiers, threshold formulas, welfare definitions, portability classification, or formal theorem hypotheses reopens the earliest affected research stage and all dependent downstream gates.

Pure exposition edits that stay within this freeze do not reopen theory.

## Stage-8 verdict

**GO — CANONICAL THEORY FROZEN.**

Next stage: **Stage 9 — Repository / Reproducibility Setup.**
