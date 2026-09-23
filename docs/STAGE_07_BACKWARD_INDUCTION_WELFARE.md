# Stage 7 — Corrected Backward Induction, Switching, Profit, and Welfare

Date: 2026-09-23  
Scope: all high-`z` statements use the Stage-4A-certified symmetric mixed `UU` continuation unless explicitly stated otherwise.

## 1. Normalization
Let
[
z=\Delta/\sigma,qquad k=c/\sigma,qquad 0<z<1/3.
]
Let
[
z_c={-6+4\sqrt3\over3}\approx0.309401076758503.
]

For `z<=z_c`, the no-information continuation is the source pure equilibrium. For `z>z_c`, use the certified symmetric mixed continuation from Stage 4.

## 2. Corrected investment thresholds
Define `K_S(z)` for the gain from investing when information is shared and `K_{NS}(z)` for the gain when information is not shared.

For `0<z<=z_c`,
[
K_S(z)={2z^2\over9},qquad
K_{NS}(z)={z^2\over2}.
]

For `z_c<z<1/3`,
[
K_S(z)=
{(17+9\sqrt3)z^2-(30+18\sqrt3)z+16\over9},
]
[
K_{NS}(z)=
{(39+18\sqrt3)z^2-(60+36\sqrt3)z+32\over18}.
]

They join the source thresholds continuously at `z_c`, and
[
K_{NS}(z)-K_S(z)={5z^2\over18}>0.
]

Important roots:
[
K_S(z)=0
quad\text{at}quad
z\approx0.314086968713884,
]
[
K_{NS}(z)=0
quad\text{at}quad
z\approx0.320424885817143.
]

Hence sufficiently close to the Assumption-2 boundary, recognition investment is privately unprofitable even at zero acquisition cost under the corrected continuation.

## 3. Stage-II equilibrium correspondence

### (S,S)
- `k<K_S`: unique `(I,I)`;
- `k>K_S`: unique `(NI,NI)`;
- `k=K_S`: all four pure investment profiles are Nash equilibria.

If `K_S<0`, then for every feasible `k>=0`, `(NI,NI)` is unique except at the root `K_S=0,k=0`, where the equality correspondence applies.

### (NS,NS)
- `k<K_{NS}`: unique `(I,I)`;
- `k>K_{NS}`: unique `(NI,NI)`;
- `k=K_{NS}`: all four pure investment profiles are Nash equilibria.

If `K_{NS}<0`, no firm invests for any `k>=0`.

### (S,NS)
Let A be the sharer and B the non-sharer. Their investment incentives separate:
- A invests iff `k<K_S`;
- B invests iff `k<K_{NS}`.

Thus, when both thresholds are positive:
- `k<K_S`: `(I,I)`;
- `K_S<k<K_{NS}`: `(NI,I)`;
- `k>K_{NS}`: `(NI,NI)`.

Boundary correspondences:
- `k=K_S`: `(I,I)` and `(NI,I)`;
- `k=K_{NS}`: `(NI,I)` and `(NI,NI)`.

This is the corrected form of the source Result-8 structure.

## 4. Stage-I information-sharing correspondence
Under the certified symmetric mixed continuation:

### If `K_{NS}(z)>0`
- for `0<=k<K_{NS}(z)`, `(NS,NS)` is the unique Stage-I action profile compatible with SPE;
- for `k>=K_{NS}(z)`, all four Stage-I action profiles
[
(NS,NS),(NS,S),(S,NS),(S,S)
]
are SPE-compatible with valid Stage-II/III continuations.

At `k=K_{NS}`, the multiplicity follows from Stage-II indifference and is not removed by off-path continuation requirements.

### If `K_{NS}(z)<=0`
For every feasible `k>=0`, no customer-specific information is acquired in equilibrium and the Stage-I sharing labels are payoff irrelevant. All four Stage-I action profiles are SPE-compatible.

Therefore the source's unqualified “unique SPE” statement cannot survive globally. No-sharing remains uniquely selected only in the strict region `k<K_{NS}(z)`.

## 5. Switching reconstruction
For the three symmetric outcomes `S,I`, `NS,I`, and corrected no-information `NI`, the source switching-count ranking survives.

In the mixed wedge:
[
T^I(S,I)>T^I(NS,I)>T^I(NI),
]
[
T^E(S,I)<T^E(NS,I)<T^E(NI).
]

The independent primitive evaluator confirms this ordering over the high-`z` domain. Result 4 therefore survives under the certified mixed continuation.

## 6. Industry profit
Let normalized per-firm gross profits be
[
F(z)={4(z^2+5)\over9},qquad
N(z)={9z^2+40\over18},
]
and
[
M(z)={z[(2+\sqrt3)z+10+6\sqrt3]\over3}
]
for the corrected mixed no-information continuation.

Always,
[
N(z)-F(z)={z^2\over18}>0.
]

The corrected no-information gross profit crosses:
[
M=F
quad\text{at}quad z\approx0.315231824630597,
]
[
M=N
quad\text{at}quad z\approx0.315991499774449.
]

Hence the source's gross-profit ranking is not globally preserved in the mixed wedge.

Including investment cost:
- `NS,I` beats `S,I` for every `z>0`;
- `S,I` beats `NI` iff `F-M>k`;
- `NS,I` beats `NI` iff `N-M>k`.

When `M>=F` or `M>=N`, the corresponding investing outcome cannot overtake no information for any nonnegative `k`.

## 7. Consumer surplus
For one inherited customer base, with normalized low valuation `L=v_L/sigma`, the corrected mixed no-information consumer surplus is
[
CS_M=
{24L+z^2-20z-8\sqrt3 z\over6}.
]

The source-safe comparison outcomes are
[
CS_{NS}=
{9z^2+72(2L+z)-88\over36},
]
[
CS_S=
{z^2+18(2L+z)-22\over9}.
]

Always
[
CS_{NS}-CS_S={5z^2\over36}>0.
]

But the corrected no-information consumer surplus crosses:
[
CS_M=CS_{NS}
quad\text{at}quad
z\approx0.318731295698269,
]
[
CS_M=CS_S
quad\text{at}quad
z\approx0.320586070246451.
]

Therefore:
- below the first crossing: `CS_M>CS_{NS}>CS_S`;
- between the crossings: `CS_{NS}>CS_M>CS_S`;
- above the second crossing: `CS_{NS}>CS_S>CS_M`.

This is a genuine correction to Result 6 in the high-mismatch region under the certified mixed continuation. It is not produced by changing primitives or searching outside Assumption 2.

## 8. Total welfare
Prices cancel as transfers. Primitive integration of valuations and switching costs plus investment costs yields, in normalized units,
[
W_{NS}-W_S={7z^2\over18}>0.
]

For the corrected mixed no-information outcome,
[
W_M-W_{NS}
=
{36k+(3+12\sqrt3)z^2+(-72+24\sqrt3)z+8\over18}.
]

This expression is strictly positive for `z_c<z<1/3` and `k>=0`. Combined with the source branch below `z_c`,
[
W(NI)>W(NS,I)>W(S,I)
]
survives across the full model domain under the certified continuation.

Thus the paper's broad total-welfare ranking survives even though the price equilibrium, investment thresholds, profit ranking, and consumer-surplus ranking require correction.

## 9. Equilibrium welfare versus algebraic welfare
The investing-outcome welfare expressions remain algebraically valid even in regions where those outcomes cease to be equilibrium continuations. The manuscript must distinguish:
- **outcome comparison** `W(NI),W(NS,I),W(S,I)`;
- **equilibrium welfare**, which uses the corrected Stage-II/Stage-I correspondence.

For information acquisition:
- if `K_{NS}>0` and `k<K_{NS}`, the unique no-sharing SPE continuation invests even though `NI` has higher total welfare: excessive investment survives, with a corrected private threshold;
- if `k>K_{NS}`, no investment is privately selected and is welfare efficient;
- at equality, both investing and no-investment Stage-II equilibria exist, but only no investment attains the higher total welfare;
- if `K_{NS}<=0`, no investment is selected for all nonnegative costs and the excessive-investment region disappears.

## 10. Results 1–10 impact map
| Result | Corrected disposition |
|---|---|
| Result 1 | **CORRECTED THRESHOLD + CORRECTED CORRESPONDENCE.** Source threshold survives only for `z<=z_c`; high-`z` threshold is `K_S`. Equality supports all four investment profiles. |
| Result 2 | **CORRECTED THRESHOLD + CORRECTED CORRESPONDENCE.** Replace source threshold by `K_{NS}` for `z>z_c`; equality supports all four profiles. |
| Result 3 | **CORRECTED COST CLASSIFICATION.** Low/intermediate/high regions use `K_S,K_{NS}`; low and/or intermediate regions can disappear when thresholds become nonpositive. |
| Result 4 | **SURVIVES** under the certified symmetric mixed continuation; switching ranking retains its direction. |
| Result 5 | **CORRECTED PROFIT RANKING.** `NS>I` relative to sharing remains, but corrected no-information profit crosses both investing outcomes in the high-`z` wedge. |
| Result 6 | **FALSE GLOBALLY / CORRECTED RANKING.** Consumer-surplus ordering reverses in two subregions above the exact/numerically certified crossing points. |
| Result 7 | **SURVIVES** under the certified continuation as an outcome welfare ordering. |
| Result 8 | **CORRECTED THRESHOLDS + CORRESPONDENCE.** Asymmetric investment regions use `K_S,K_{NS}`; endpoint multiplicity retained explicitly. |
| Result 9 | **CORRECTED SPE CORRESPONDENCE.** `NS,NS` is unique only for strict `k<K_{NS}`; all four sharing profiles are SPE-compatible at/above the upper threshold, and for all `k>=0` once `K_{NS}<=0`. |
| Result 10 | **SURVIVES IN WELFARE LOGIC WITH CORRECTED PRIVATE THRESHOLD; TYPO LEDGER SEPARATE.** No-information has highest total welfare; excessive investment occurs only where the corrected private equilibrium still invests. Printed inequality/denominator defects remain TYPO ONLY. |

## 11. Independent evidence
- `code/stage07_backward_induction.py`: symbolic payoff/threshold/welfare identities.
- `code/stage07_primitive_welfare.py`: independent direct utility integration over four valuation types and the switching-cost continuum, plus switching-count and total-welfare regression.
- CI mathematical-regression job: PASS on Stage 1, Stage 4, Stage 4A, and Stage 7 symbolic programs; the new primitive-welfare regression is included in the next CI run.

## 12. Stage-7 verdict
**GO — DOWNSTREAM REASSESSMENT IS SUBSTANTIVE.**

The project should remain a full reassessment rather than shrink to an Eq. (8) note.

Quantifier retained:
high-`z` downstream statements are conditional on the certified symmetric mixed Stage-III continuation until unrestricted mixed-equilibrium uniqueness or payoff-selection robustness is established.
