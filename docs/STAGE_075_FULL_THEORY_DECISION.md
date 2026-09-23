# Stage 7.5 — Full-Theory Freeze Decision

Date: 2026-09-23  
Workflow: \`research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7\` (v2.4)

## Objective
Decide whether the certified project merits full-paper investment rather than a short equation correction or research note.

## 1. Core result without model-specific notation

The economic mechanism can be stated without the source paper's equation numbers:

> When a firm must use one common poaching price across customer segments with different willingness to switch, the aggregate demand schedule is kinked. An interior first-order-condition candidate can remain locally optimal while becoming globally dominated by a deviation that deliberately gives up one segment. Once that common-price continuation changes, the private value of customer recognition and information sharing changes, and downstream profit and consumer-surplus rankings can reverse even when the broad total-welfare ordering survives.

This statement identifies the strategic chain without claiming that the exact theorem is portable to arbitrary demand systems.

## 2. Minimal causal / strategic chain

1. customer heterogeneity creates segment-specific switching thresholds;
2. limited information forces a common price across heterogeneous segments;
3. aggregation produces kinks when a segment enters or exits demand;
4. a global deviation can cross a kink and sacrifice a segment;
5. the original local price profile therefore has a restricted validity domain;
6. corrected continuation payoffs alter the private return to acquiring customer information;
7. Stage-II investment changes Stage-I information-sharing incentives;
8. profit and consumer-surplus rankings can change independently of total welfare.

The mechanism is therefore not merely “a polynomial threshold changes sign.”

## 3. Essential assumptions versus tractability assumptions

### Essential for the certified baseline result
- heterogeneous customer segments;
- switching frictions;
- an information state in which at least one strategic price is constrained to be common across segments;
- sufficiently large heterogeneity relative to switching friction to make a type-exit deviation relevant;
- strategic price competition embedded in the acquisition/sharing game.

### Baseline-model / tractability structure
- exactly four valuation types with offsets \`0,0,+Delta,-Delta\`;
- uniform switching-cost distribution on the normalized interval;
- equal masses of the four types;
- the source timing and price-control architecture;
- the maintained source restriction \`0<Delta/sigma<1/3\`;
- the particular closed-form two-point mixed continuation.

No manuscript sentence may describe those baseline-specific objects as generic.

## 4. Is the welfare / organizational implication substantive?

Yes.

The corrected price game changes more than the disputed price itself:
- both private information-acquisition thresholds change on a nonempty admissible region;
- the sharing-side threshold reaches zero before the no-sharing threshold;
- the Stage-I SPE correspondence changes at the corrected upper threshold;
- gross-profit rankings cross twice;
- the source consumer-surplus ranking is false globally under the certified continuation;
- the total-welfare ranking survives, creating a useful distinction between corrected equilibrium/private incentives and the social ordering.

This combination is economically more substantive than a local corrigendum.

## 5. Is it more than a parameter exercise?

Yes, at the source-specific reassessment level.

The central result is a global-equilibrium failure caused by a common-control kink, followed by a backward-induction correction. The paper is not valuable because \`z_c\` has an unusual closed form; the value is that the source equilibrium ceases to exist in pure strategies over an admissible interval and the corrected continuation changes several downstream conclusions.

However, the project is **not** certified as a general theorem about all customer-recognition or switching-cost models.

## 6. Alternative-formulation status

Stage 7 did not claim cross-model portability. Stage 7.5 therefore does not use unperformed robustness tests as evidence.

The most economically meaningful portability attacks are reserved and pre-specified for Stage 7.5A:

1. replace the uniform switching-cost distribution by a smooth non-uniform distribution and re-solve the \`UU\` price game from primitives;
2. perturb the equal four-type mass structure while keeping the common-price information constraint and re-solve rather than substitute into baseline formulas.

Success criterion for portability of the **mechanism**, not the exact formula:
- an interior/common-price candidate can lose global optimality through segment exit, generating a regime change/non-pure region or a closely analogous global-equilibrium correction.

Failure of these tests will narrow the mechanism to \`MODEL-SPECIFIC\`; it will not invalidate the exact correction of the inspected baseline model.

## 7. Full-paper versus note decision

### Short-note route rejected
A short Eq. (8) note would omit:
- the complete pure correspondence;
- the selected high-\`z\` mixed continuation;
- the affected/unaffected \`UU/TT/TU\` map;
- corrected Stage-II thresholds;
- corrected Stage-I multiplicity;
- profit and consumer-surplus reversals;
- welfare-survival result.

That would leave the main economic consequences of the correction unresolved.

### General-theory expansion rejected
No generic common-control theorem is required. Stage 6 already established that mixed pricing and pure-nonexistence mechanisms are known families. Expanding the model for prestige would violate scope discipline.

### Selected route
**Full source-specific correction/reassessment paper.**

## 8. Stage-7.5 verdict

**GO — FULL REASSESSMENT ROUTE JUSTIFIED.**

The project contains a coherent strategic mechanism and substantive downstream consequences sufficient to justify a full paper at a source-specific reassessment scope.

This GO does **not** freeze theory. It routes to Stage 7.5A for quantifier, portability, benchmark, and formal-verification certification.

## 9. Next-stage contract

Stage 7.5A must:
- preserve the exact baseline theorem;
- pre-specify and execute the two diagnostic portability attacks above without result-driven redesign;
- classify each headline claim as PORTABLE / CONDITIONALLY PORTABLE / MODEL-SPECIFIC / INSTITUTION-SPECIFIC / FALSIFIED;
- freeze maximum defensible wording;
- audit equilibrium-selection and welfare quantifiers;
- close the Lean formal-verification gate with actual build/placeholder/axiom evidence;
- route back if a diagnostic test exposes a false baseline claim rather than merely limited portability.

## Formal closure record
- Stage: 7.5 — Full-Theory Freeze Decision
- Canonical verdict: **STAGE 7.5 CLOSED — GO.**
- Full-paper route: **AUTHORIZED**.
- Generic-theory expansion: **NOT AUTHORIZED**.
- Theory frozen: **NO — Stage 7.5A remains mandatory**.
