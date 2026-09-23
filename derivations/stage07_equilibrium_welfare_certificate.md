# Stage 7 — Equilibrium Correspondence and Welfare Closure Certificate

Date: 2026-09-23

## Independent closure purpose

This certificate checks the backward-induction logic independently of the prose result map. It treats Stage 4A continuation payoffs as inputs and re-derives the investment and sharing games from payoff differences.

Artifact: \`code/stage07_equilibrium_correspondence_audit.py\`.

## Stage-II dominance structure

For \`(S,S)\`, the gain from investing is the same whether the opponent invests or not:
\[
F-B_S=A_S-M=K_S.
\]
Therefore investment is strictly dominant if \`k<K_S\`, no investment is strictly dominant if \`k>K_S\`, and at equality every pure investment profile is a Nash equilibrium.

For \`(NS,NS)\`,
\[
N-B_{NS}=A_{NS}-M=K_{NS},
\]
giving the analogous complete correspondence.

For \`(S,NS)\`, the sharer's investment threshold is \`K_S\` and the non-sharer's is \`K_{NS}\`:
\[
C_A-B_{NS}=K_S,\qquad C_B-B_S=K_{NS}.
\]

## Stage-I no-sharing logic

When \`k<K_S\`, all Stage-II histories relevant to a Stage-I deviation invest. The gain from choosing \`NS\` rather than \`S\` is
\[
C_B-F=N-C_A={5z^2\over18}>0,
\]
regardless of the opponent's Stage-I action.

When \`K_S<k<K_{NS}\`, a non-sharer invests while a sharer does not. Again the gain from choosing \`NS\` is
\[
K_{NS}-k>0
\]
against either opponent action.

The lower-threshold equality \`k=K_S<K_{NS}\` does **not** create a Stage-I sharing equilibrium. The Stage-II indifference can alter continuation payoffs, so it must be checked explicitly rather than inferred from strict-region logic.

- On the source-pure branch, the least favorable payoff after deviating to \`NS\` exceeds the most favorable payoff from staying in \`(S,S)\` by \`z^2/18>0\`.
- On the high-\`z\` selected branch while \`K_S>=0\`, the analogous deviation gain is positive; the sole positive zero of that gain is approximately \`0.30756636<z_c\`, outside that branch.

Thus \`NS\` remains the unique Stage-I best response structure for all \`k<K_{NS}\`, including \`k=K_S\`.

At \`k=K_{NS}\`, Stage-II indifference permits no-investment continuations at every Stage-I history, making sharing labels payoff irrelevant and allowing all four Stage-I action profiles to be supported. For \`k>K_{NS}\`, no investment is uniquely selected and the same payoff irrelevance is immediate.

## Threshold topology

Under the selected high-\`z\` continuation:
- \`K_S=0\` at \`z≈0.314086968713884\`;
- \`K_{NS}=0\` at \`z≈0.320424885817143\`;
- \`K_{NS}-K_S=5z^2/18>0\`.

Hence the parameter domain contains four economically distinct zones:
1. \`0<z<z_S^0\`: both acquisition thresholds positive;
2. \`z=z_S^0\`: sharing-side acquisition is weakly profitable only at zero cost;
3. \`z_S^0<z<z_{NS}^0\`: sharing-side acquisition is never privately profitable at nonnegative cost, while no-sharing acquisition can remain profitable;
4. \`z>=z_{NS}^0\`: acquisition is never privately profitable at nonnegative cost under either Stage-I regime.

## Profit, consumer-surplus, and welfare boundaries

Selected high-\`z\` gross-profit crossings:
- \`M=F\` at \`z≈0.315231824630597\`;
- \`M=N\` at \`z≈0.315991499774449\`.

Thus:
- below the first crossing: \`N>F>M\`;
- between the crossings: \`N>M>F\`;
- above the second: \`M>N>F\`.

Consumer-surplus crossings:
- \`CS_M=CS_{NS}\` at \`z≈0.318731295698269\`;
- \`CS_M=CS_S\` at \`z≈0.320586070246451\`.

Thus:
- below the first: \`CS_M>CS_{NS}>CS_S\`;
- between: \`CS_{NS}>CS_M>CS_S\`;
- above the second: \`CS_{NS}>CS_S>CS_M\`.

Total welfare remains ordered
\[
W_M>W_{NS}>W_S
\]
through the selected high-\`z\` continuation. The direct expression
\[
W_M-W_{NS}
={36k+(3+12\sqrt3)z^2+(-72+24\sqrt3)z+8\over18}
\]
is decreasing in \`z\` throughout the maintained high-\`z\` wedge, increasing in \`k\`, and remains strictly positive at \`z=1/3,k=0\`. Also
\[
W_{NS}-W_S={7z^2\over18}>0.
\]

## Selection boundary

Nothing in this certificate upgrades the Stage-4A existence result to unrestricted mixed uniqueness. Accordingly:
- the pure correspondence and pure nonexistence results are selection-free;
- all high-\`z\` backward-induction, profit, consumer-surplus, and welfare formulas that use \`M\` are conditional on the certified symmetric two-point continuation;
- the manuscript must distinguish algebraic outcome comparisons from equilibrium welfare.

## Closure conclusion

No Stage-II equality case, Stage-I deviation, threshold disappearance, profit crossing, consumer-surplus crossing, or welfare sign required by the selected-continuation Stage-7 claims remains unresolved.
