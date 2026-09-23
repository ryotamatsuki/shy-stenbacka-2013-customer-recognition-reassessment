# Stage 4 — Clipped Stage-III Price-Game Construction

Date: 2026-09-23  
Canonical workflow: `research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7`

## Executive finding
The no-information price game has a complete **pure-strategy** correspondence that is sharper than the historical counterexample:

Let
[
z=\Delta/\sigma,qquad
z_c={-6+4\sqrt3\over3}.
]

Under Assumption 2, `0<z<1/3`:

1. for `0<z<=z_c`, the source profile
[
p_A=p_B=2\sigma/3,qquad q_A=q_B=\sigma/3
]
is the unique pure-strategy no-information price equilibrium;

2. for `z_c<z<1/3`, the no-information price subgame has **no pure-strategy equilibrium**;

3. on the high-`z` wedge there exists a symmetric semi-mixed equilibrium in which each incumbent control is pure and each uniform poaching control mixes over two prices. Existence/global best-response validity is certified below; uniqueness within the full mixed-strategy space is not yet claimed.

This replaces the incorrect inference that crossing the kink necessarily generates another pure branch.

## 1. Canonical segment decomposition
Normalize `sigma=1`. For one inherited customer base, write `p` for the incumbent price and `q` for the rival poaching price. Define `x=p-q` and
[
F_z(x)
=2[x]_0^1+[x+z]_0^1+[x-z]_0^1,
]
where `[y]_0^1=min(1,max(0,y))`.

The segment payoffs are
[
u_I(p,q)=p[4-F_z(p-q)],qquad
u_P(q,p)=qF_z(p-q).
]

The full no-information four-control game decomposes into two independent copies:
[
(p_A,q_B)quad\text{and}quad(p_B,q_A).
]

Hence the pure equilibrium correspondence of the four-control game is the Cartesian product of the two segment-game correspondences.

## 2. Complete piecewise demand
For `0<z<1/3`,
[
F_z(x)=
\begin{cases}
0,&x\le -z,\\
x+z,&-z\le x\le0,\\
3x+z,&0\le x\le z,\\
4x,&z\le x\le1-z,\\
3x+1-z,&1-z\le x\le1,\\
x+3-z,&1\le x\le1+z,\\
4,&x\ge1+z.
\end{cases}
]

Each interval produces a quadratic own-price problem. Every candidate is checked against its interval feasibility and against adjacent and non-adjacent kinks.

## 3. Pure-equilibrium theorem
On a smooth branch `F=ax+b`, simultaneous interior FOCs imply
[
p={8-b\over3a},qquad
q={4+b\over3a},qquad
x={2(2-b)\over3a}.
]

After imposing branch feasibility for every active-set region, the only smooth mutual candidate in `0<z<1/3` is the all-four-active branch
[
(p,q)=(2/3,1/3),quad x=1/3.
]

No kink is a local mutual optimum:
- at the slope-increase kinks `x=-z,0,z`, the poacher's one-sided derivative jumps in the wrong direction for a local maximum;
- at the slope-decrease kinks `x=1-z,1,1+z`, the incumbent's one-sided derivative jumps in the wrong direction for a local maximum;
- `p=0` and `q=0` cannot form a mutual best response.

At the source candidate, the incumbent control remains a global best response for every `z<1/3`. The poacher has a competing three-active-group candidate
[
q_H={2+z\over6}
]
with gain
[
G(z)={3z^2+12z-4\over36}.
]

Therefore
[
G(z)\le0
\iff
z\le z_c={-6+4\sqrt3\over3}.
]

This proves the pure-strategy correspondence stated in the executive finding. At `z=z_c`, the poacher has two best replies to `p=2/3`, but only `q=1/3` is part of a mutual pure best response; pure-equilibrium uniqueness therefore remains at the equality point.

## 4. Exact counterexample regression
For `sigma=25, Delta=8`, `z=8/25>z_c`.
The source control is `q_0=25/3`; the three-active-group best reply is `q_H=29/3`. The exact profit gain is
[
23/225>0.
]

This is stored as a permanent regression target.

## 5. High-z symmetric semi-mixed equilibrium
For `z_c<z<1/3`, define
[
p^*=z{3+2\sqrt3\over3},
]
[
q_L={p^*\over2}
=z{3+2\sqrt3\over6},
]
[
q_H=z{2+\sqrt3\over3},
]
and
[
\lambda(z)
={4-(5+3\sqrt3)z\over z(1+\sqrt3)}.
]

The incumbent sets `p=p^*` surely. The poacher sets `q_L` with probability `lambda` and `q_H` with probability `1-lambda`.

Properties:
- `0<lambda<1` on `z_c<z<1/3`;
- `lambda(z_c)=1`, so the mixed continuation joins the source pure branch continuously;
- `q_L` is the four-active-group poaching optimum at `p^*`;
- `q_H` is the three-active-group optimum at `p^*`;
- their poaching profits are exactly equal;
- the mixture weight makes the incumbent's expected first-order condition zero at `p^*`;
- direct comparison with every piecewise branch and kink establishes global best-response validity for both roles.

The normalized expected component profits are
[
E\pi_I
={z(5+3\sqrt3)(2-z)\over3},
]
[
E\pi_P
={z^2(7+4\sqrt3)\over3},
]
so a no-information firm receives
[
M(z)
={z[(2+\sqrt3)z+10+6\sqrt3]\over3}.
]
Dimensioned profit equals `sigma M(Delta/sigma)`.

### Current quantifier boundary
What is certified here is:
- complete pure-strategy correspondence;
- existence and global best-response validity of the displayed symmetric semi-mixed equilibrium.

A theorem that this is the **unique equilibrium over the entire mixed-strategy space** is not yet frozen. Until that further uniqueness attack closes, downstream high-`z` results must be described as implications under this certified symmetric mixed continuation, not as selection-free statements over all mixed equilibria.

## 6. Other Stage-III subgames
The information-set decomposition gives:

### Full information, source (6)–(7): `TT+TT`
Each relevant control is type specific. Primitive global-deviation checks certify the source branch throughout Assumption 2.

### One invests and shares, source (9): `TT+UU`
The `TT` component survives. The embedded `UU` component has exactly the same pure-equilibrium failure and symmetric mixed repair as above for `z>z_c`.

### Both invest, no sharing, source (10): `TU+TU`
The type-specific incumbent controls break the common-control kink responsible for Eq. (8). Full clipped-demand global-deviation checks certify the source profile over `0<z<1/3`.

### One invests, no sharing, source (11): `TU+UU`
The `TU` component survives. The embedded `UU` component requires the same mixed continuation for `z>z_c`.

### Asymmetric sharing, both invest, source (17): `TT+TU`
No `UU` component is present. Full clipped-demand global-deviation checks certify the displayed branch over Assumption 2.

## 7. Stage-II continuation payoff primitives
For `z>z_c`, under the certified symmetric mixed `UU` continuation, the normalized safe components are
[
I_F={16+2z^2\over9},quad
P_F={4+2z^2\over9},quad
I_D={16\over9}+{z^2\over2},quad
P_U={4\over9}.
]

Therefore:
- no information: `M=Epi_I+Epi_P`;
- both invest/share: `F=4(z^2+5)/9`;
- both invest/no-share: `N=(9z^2+40)/18`;
- one invest/share: investor `I_F+Epi_P`, noninvestor `P_F+Epi_I`;
- one invest/no-share: investor `I_D+Epi_P`, noninvestor `P_U+Epi_I`;
- asymmetric sharing/both invest: source continuation remains unchanged.

These are the only admissible inputs to the corrected Stage-II reconstruction in the high-`z` wedge.

## 8. Verification artifacts
- `code/stage04_no_information.py`: independent symbolic piecewise construction and identities.
- `code/stage04a_primitive_evaluator.py`: separate primitive clipped-demand evaluator and numerical global-deviation attack; it does not call the Stage-4 symbolic branch solver.
- `code/stage01_cleanroom_reproduction.py`: exact counterexample regression.

## 9. Stage-4 verdict
**GO — PRICE-GAME CONSTRUCTION CLOSED WITH EXPLICIT MIXED-SELECTION SCOPE.**

The pure-strategy question is closed. The selected symmetric semi-mixed continuation is fully constructed and is the only high-`z` continuation used by downstream construction-stage calculations. Stage 4 does not claim unrestricted mixed-equilibrium uniqueness. That distinct alternative-equilibrium/quantifier question is routed explicitly to Stage 4A and Stage 7.5A and therefore does not block Stage-4 construction closure.

## 10. Next-stage contract
Stage 4A must attack the displayed mixed continuation without importing the Stage-4 branch labels, separately search for alternative mixed equilibria, and certify the exact quantifier permitted downstream. Stage 7 may reconstruct investment/sharing/welfare only under the selected continuation until Stage 4A/7.5A establish stronger selection robustness.


## 11. Formal closure record

- Stage: 4 — Minimal Model / Stage-III Price-Game Construction
- Formal-closure input SHA: `2e8385f87d0b53bd7bee5fe4e5baea2512f61a70`
- Canonical representation: `F_z(x)=2[x]_0^1+[x+z]_0^1+[x-z]_0^1`.
- Active-set partition: COMPLETE.
- Smooth-branch mutual candidates: EXHAUSTED.
- Kink candidates: EXCLUDED analytically by one-sided derivative ordering.
- Nonnegative price boundaries: CHECKED.
- Source Eq. (8) pure equilibrium domain:
  - unique pure equilibrium for `0<z<=z_c`;
  - no pure equilibrium for `z_c<z<1/3`.
- Exact threshold: `z_c=(-6+4sqrt(3))/3`.
- Exact permanent regression: `(sigma,Delta)=(25,8)`, gain `23/225`.
- High-`z` selected continuation: symmetric semi-mixed equilibrium constructed in closed form.
- Mixed-equilibrium uniqueness: deliberately **not claimed**.
- Related component certification:
  - `TT`: globally constructed/certified;
  - `TU`: globally constructed/certified;
  - `UU`: corrected as above.
- Equation map:
  - (6)–(7): survives;
  - (8): corrected;
  - (9): inherits corrected `UU`;
  - (10): survives;
  - (11): inherits corrected `UU`;
  - (17): survives.
- Continuation payoff primitives required by Stage II: generated from the corrected Stage-III construction.
- Supporting artifacts:
  - `derivations/stage04_active_set_certificate.md`;
  - `code/stage04_global_price_certification.py`;
  - `code/stage04_no_information.py`;
  - `code/stage01_cleanroom_reproduction.py`.
- Independent recalculation on 2026-09-23 reconfirmed the branch identities, critical root, exact `23/225` gain, `TT/TU` vertices, and mixed-support indifference.
- Rejected branch: no alternative pure kink-corrected equilibrium exists above `z_c`.
- Canonical verdict: **STAGE 4 CLOSED — GO, PRICE-GAME CONSTRUCTION COMPLETE AT EXPLICIT SELECTED-CONTINUATION SCOPE.**
- Open item routed forward: unrestricted mixed-equilibrium multiplicity/uniqueness and welfare-selection robustness.
- Next-stage contract: Stage 4A must independently certify global best responses and separately attack alternative mixed equilibria; a failure there reopens Stage 4.
