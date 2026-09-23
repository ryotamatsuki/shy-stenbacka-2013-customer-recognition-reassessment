# Stage 4 Active-Set and Related-Subgame Certificate

Date: 2026-09-23  
Workflow: `research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7`

## Purpose
Close the construction-stage mathematical gaps that are not discharged by the single Eq. (8) counterexample. This certificate addresses:

1. exhaustive pure active-set analysis of the no-information `UU` component;
2. kink-local-optimum exclusion;
3. exact source-profile globality threshold;
4. the high-`z` selected semi-mixed continuation;
5. globality of the `TT` and `TU` components used by Eqs. (6)–(7), (9)–(11), and (17).

Stage 4A remains responsible for logically independent adversarial certification.

## 1. Canonical normalized demand
Let `z=Delta/sigma`, normalize `sigma=1`, and define
[
F_z(x)=2[x]_0^1+[x+z]_0^1+[x-z]_0^1,
qquad x=p-q.
]
The segment payoffs are
[
u_I(p,q)=p[4-F_z(p-q)],qquad
u_P(q,p)=qF_z(p-q).
]

For `0<z<1/3`,
[
F_z(x)=
egin{cases}
0,&xle-z,\\
x+z,&-zle xle0,\\
3x+z,&0le xle z,\\
4x,&zle xle1-z,\\
3x+1-z,&1-zle xle1,\\
x+3-z,&1le xle1+z,\\
4,&xge1+z.
end{cases}
]

## 2. Exhaustive smooth pure candidates
On a smooth branch `F=ax+b`, the simultaneous interior first-order conditions imply
[
p={8-bover3a},qquad
q={4+bover3a},qquad
x={2(2-b)over3a}.
]

Applying these formulas to every positive-slope branch gives:

| branch | candidate x | feasibility under 0<z<1/3 |
|---|---:|---|
| [-z,0] | 2(2-z)/3 | impossible: x>0 |
| [0,z] | 2(2-z)/9 | impossible: x-z=(4-11z)/9>0 |
| [z,1-z] | 1/3 | feasible; gives p=2/3, q=1/3 |
| [1-z,1] | 2(1+z)/9 | impossible: (1-z)-x=(7-11z)/9>0 |
| [1,1+z] | 2(z-1)/3 | impossible: x<0 |

The flat regions `F=0` and `F=4` cannot contain an interior mutual optimum because one role has zero demand while a finite move toward the adjacent active region yields positive revenue.

Hence the source point is the only smooth pure candidate.

## 3. Kink exclusion
A kink cannot supply a missing pure equilibrium.

For the poacher,
[
partial_q u_P=F-qF'.
]
At slope-increase kinks `x=-z,0,z`, increasing `q` moves `x` to the lower-slope side. The one-sided derivatives have the ordering opposite to that required for a local maximum, so no poacher best response can be located at these kinks.

For the incumbent,
[
partial_p u_I=4-F-pF'.
]
At slope-decrease kinks `x=1-z,1,1+z`, increasing `p` moves `x` to the lower-slope side. Again the one-sided derivative ordering is incompatible with a local maximum.

Thus neither smooth branches nor kink points produce any pure candidate other than the source profile.

## 4. Globality of the source profile
Fix the incumbent price at `p=2/3`. For nonnegative `q`, the only competing interior poaching maxima are:

- all-four-active:
[
q_0=1/3,qquad Pi_0=4/9;
]
- three-active:
[
q_H=(2+z)/6,qquad
Pi_H={(2+z)^2over12},
]
when that vertex is branch-feasible.

Their difference is
[
G(z)=Pi_H-Pi_0
={3z^2+12z-4over36}.
]
Let
[
z_c={-6+4sqrt3over3}.
]
Then `G(z)<=0` iff `z<=z_c`.

The lower-demand branches after further type exit are already decreasing when entered and cannot exceed the preceding branch maxima. The incumbent's source price is its global best response to `q=1/3` throughout `0<z<1/3`.

Therefore:
- `0<z<=z_c`: the source point is the unique pure equilibrium;
- `z_c<z<1/3`: no pure equilibrium exists.

At `z=z_c`, the poacher is indifferent between `q_0` and `q_H`, but only `q_0` is part of a mutual pure best response.

## 5. Selected high-z semi-mixed continuation
For `z_c<z<1/3`, define
[
p^*=z{3+2sqrt3over3},qquad
q_L={p^*over2},qquad
q_H=z{2+sqrt3over3},
]
and
[
lambda(z)
={4-(5+3sqrt3)zover z(1+sqrt3)}.
]

The poacher is indifferent between `q_L` and `q_H`. The mixture with probability `lambda` on `q_L` makes `p^*` an incumbent best response. The Stage-4 construction compares all branch extrema and kinks; the separate Stage-4A primitive evaluator independently attacks globality.

Component expected profits are
[
Epi_I={z(5+3sqrt3)(2-z)over3},qquad
Epi_P={z^2(7+4sqrt3)over3}.
]

Stage 4 claims existence and validity of this selected symmetric continuation, **not uniqueness in the unrestricted mixed-strategy space**.

## 6. TT component globality
For one type with valuation difference `d`, `|d|<1/3`,
[
s=[p-q-d]_0^1.
]
The source type-specific candidate is
[
p={2+dover3},qquad q={1-dover3}.
]
Against the candidate `q`, the incumbent revenue is increasing in the full-retention region, strictly concave in the interior region, and zero after complete loss. Its unique global interior vertex is the displayed `p`.

Against the candidate `p`, the poacher has no nonnegative full-capture plateau because `p-d-1<0`; its interior revenue is strictly concave with unique global vertex at the displayed `q`.

Therefore every `TT` component used in full information is globally certified at Stage 4.

## 7. TU component globality
For a type-specific incumbent and common poacher,
[
p_t={2over3}+{d_tover2},qquad q={1over3}.
]
Every incumbent control is individually the unique global best response to `q=1/3`.

At these incumbent prices, the common-poaching demands are
[
s_t=left[{2over3}-q-{d_tover2}ight]_0^1.
]
No upper clipping occurs for any nonnegative `q` because `z<1/3`.

Before any type drops, aggregate demand is `8/3-4q`, whose unique revenue maximizer is `q=1/3`.

When the `d=+z` group drops at
[
q={2over3}-{zover2},
]
the three-active branch vertex is
[
q={1over3}+{zover12},
]
which lies strictly to the left of that branch boundary for all `z<1/3`. Hence revenue is already decreasing on entry. After the two `d=0` groups drop, the one-active vertex `1/3+z/4` also lies strictly to the left of its region. No later branch can recover the source payoff.

Thus `q=1/3` is the unique global common-poaching best response, and the `TU` component is globally certified.

## 8. Equation map
- Eqs. (6)–(7): `TT+TT` — globally certified.
- Eq. (8): `UU+UU` — source profile valid only for `z<=z_c`; no pure equilibrium above; selected semi-mixed continuation constructed.
- Eq. (9): `TT+UU` — `TT` survives; `UU` inherits the same high-`z` correction.
- Eq. (10): `TU+TU` — globally certified source branch.
- Eq. (11): `TU+UU` — `TU` survives; `UU` inherits the correction.
- Eq. (17): `TT+TU` — globally certified source branch.

## 9. Evidence
- `code/stage04_global_price_certification.py` — symbolic branch/identity regression.
- `code/stage04_no_information.py` — construction formulas and corrected continuation payoffs.
- `code/stage01_cleanroom_reproduction.py` — exact `23/225` regression.
- Stage 4A owns independent consumer-level adversarial certification and alternative-equilibrium search.

## 10. Construction-stage conclusion
The Stage-III construction is complete at the paper's selected-continuation scope. The only unresolved mixed-strategy issue is unrestricted mixed-equilibrium uniqueness/completeness, which is **not** asserted by Stage 4 and is explicitly routed to Stage 4A/7.5A quantifier certification.
