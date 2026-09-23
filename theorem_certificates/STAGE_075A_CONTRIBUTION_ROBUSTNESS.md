# Contribution Robustness Certificate — Stage 7.5A

Date: 2026-09-23  
Workflow: research-paper-workflow v2.4

## Headline claim register

| ID | Canonical claim | Mechanism invariant | Diagnostic alternatives | Result | Classification | Maximum wording |
|---|---|---|---|---|---|---|
| H1 | In the inspected baseline \`UU\` price game, the source pure profile is unique iff \`z<=z_c\`, and no pure equilibrium exists for \`z_c<z<1/3\`. | Global price optimization must account for segment exit. | Beta(2,2) switching costs; unequal type masses | Both alternatives retain pure profiles at attacked high-\`z\` points. | **MODEL-SPECIFIC** | Exact theorem for the inspected baseline model only. |
| H2 | A symmetric two-point mixed continuation exists on the baseline high-\`z\` wedge. | Mixed continuation repairs the baseline nonexistence region. | Same two alternatives | Baseline nonexistence itself disappears in attacked alternatives. | **MODEL-SPECIFIC** | Existence in the baseline model; no uniqueness or portability claim. |
| H3 | Corrected acquisition thresholds \`K_S,K_NS\` alter Stage-II and Stage-I behavior. | Price-continuation payoffs determine the value of recognition. | Alternatives change the Stage-III object and therefore do not inherit the formulas. | No transport of formulas permitted. | **MODEL-SPECIFIC** | Exact backward-induction result conditional on certified baseline continuation. |
| H4 | Profit and consumer-surplus rankings cross in the high-\`z\` baseline region. | Corrected price continuation changes transfers and switching patterns. | Not transported after H1/H2 fail portability. | Stop rule applied. | **MODEL-SPECIFIC** | Baseline selected-continuation result only. |
| H5 | Total welfare remains ordered \`W(NI)>W(NS,I)>W(S,I)\` in the maintained baseline model. | Switching/allocation losses dominate price-transfer changes. | Not generalized after two portability failures. | Baseline identity survives. | **MODEL-SPECIFIC** | Outcome-welfare ordering in the maintained model and certified continuation. |

## Essential assumptions identified

Material result-driving assumptions include:
- uniform switching-cost distribution;
- equal four-type masses;
- exact four-offset structure \`0,0,+z,-z\`;
- common price in the \`UU\` information state;
- source timing/control architecture;
- maintained domain \`0<z<1/3\`.

## Negative portability evidence

Attack A changes the switching-cost CDF to Beta(2,2). Pure profiles remain at \`z=0.31,0.32,0.33\`.

Attack B changes type masses to \`(1,1.25,0.75,1)\`. Pure profiles again remain at the attacked high-\`z\` points.

These are pre-specified, economically meaningful, non-cosmetic perturbations. Both overturn the cross-model pure-nonexistence claim.

## Stop rule

**TRIGGERED.**

No further result-driven redesign is authorized to rescue a general mechanism claim. The paper must present the contribution as a source-specific/model-specific reassessment.

## Strongest contribution wording licensed

> In the inspected Shy–Stenbacka model, the no-information common-price continuation is globally valid only below an exact mismatch threshold. Above that threshold the baseline game has no pure equilibrium; a certified mixed continuation changes the model's investment, information-sharing, profit, and consumer-surplus implications while the broad total-welfare ordering survives.

## Prohibited stronger wording

- generic failure of pure pricing under customer recognition;
- robust mixed pricing under arbitrary switching-cost distributions;
- portability to unequal type masses;
- unique mixed equilibrium;
- complete mixed-equilibrium correspondence;
- selection-free high-\`z\` welfare/SPE results;
- first-best terminology for the compared outcome set;
- policy effects inferred from institutional examples.

## Stage 12 consumption rule

Journal positioning must treat the paper as a **model-specific correction/reassessment with substantive downstream consequences**, not as a general theory contribution.


## Stage-11 recertification

The original portability artifact used grid regret only. Stage 11 correctly treated that evidence level as insufficient and reopened the Stage-7.5A diagnostic certificate.

The repaired artifact `code/stage075a_portability_attacks.py` now:
1. initializes from a dense grid;
2. alternates continuous incumbent and poacher best responses;
3. recomputes continuous unilateral regret;
4. fails unless residual is below `1e-8`.

Both pre-specified failures survive. The classification **MODEL-SPECIFIC** is recertified; no theory-freeze claim changes.
