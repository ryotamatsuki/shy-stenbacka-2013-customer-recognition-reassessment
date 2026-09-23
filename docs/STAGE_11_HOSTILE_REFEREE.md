# Stage 11 — Full-Paper Hostile Referee / Robustness Gate

Date: 2026-09-23  
Input: Stage-10 complete manuscript; Stage-8 frozen theory; Stage-7.5A contribution-robustness and formal certificates.

## Objective

Try to reject the full manuscript after construction, including a fresh known-model-in-disguise attack, global-deviation reconstruction, claim-scope audit, computational failure-mode audit, and source/journal-risk audit.

## Attack ledger

| Attack | Classification | Stage-11 finding | Resolution |
|---|---|---|---|
| Classic-result / relabeling | MINOR | Mixed pricing and pure-nonexistence mechanisms are known families. | Manuscript already claims only source-specific correction/reassessment. |
| Known-model-in-disguise / theorem absorption | MINOR | Varian/Shilony/Esteves/captive-buyer mechanisms are close, but no searched theorem directly yields the exact baseline threshold, complete pure correspondence, and three-stage downstream map. | Stage-6 positioning retained; no general-theory claim. |
| Whole-game novelty | PASS | Value lies in global-equilibrium correction plus backward-induction consequences, not in introducing mixed pricing. | No change. |
| Ad hoc assumptions | PASS WITH BOUNDARY | Uniform switching costs and equal type masses materially drive the strong high-z result. | Explicitly classified MODEL-SPECIFIC; negative portability evidence retained. |
| Alternative demand/information structures | MAJOR BUT FIXABLE — REPAIRED | Original Stage-7.5A portability implementation used grid regret only and therefore did not exclude off-grid deviations. | Stage 7.5A reopened; continuous best-response refinement and continuous unilateral-regret checks added. Both negative portability results survive below 1e-8 residual. |
| Participation/corner/boundary/regime switch | PASS | Pure-price active-set, kinks, zero/flat boundaries, z=zc, k=K_S, and k=K_NS are explicitly handled. | No change. |
| Finite deviation outside regular branch | PASS | Exact (sigma,Delta)=(25,8), q:25/3 -> 29/3 deviation yields 23/225 and leaves the all-active branch. | Permanent regression retained. |
| Welfare mechanicality | PASS | Profit/CS rankings change while total-welfare ordering survives; manuscript explains transfer versus allocation logic. | No change. |
| Institutional specificity/external validity | PASS WITH BOUNDARY | FTC/CMA/EU examples support plausibility only. | No causal policy claim. |
| Numerical-not-proof | PASS AFTER REPAIR | Baseline pure theorem is analytic; primitive numerics are adversarial checks; portability remains numerical diagnostic evidence only. | Manuscript wording tightened. |
| Proof/notation inconsistency | PASS | Manuscript formulas match frozen Stage-8 identities and generated tables. | No change. |
| Quantifier inflation | PASS | Pure uniqueness/nonexistence, mixed existence, and selected-continuation downstream statements remain distinct. | No change. |
| Portability inflation | PASS AFTER REPAIR | Two pre-specified alternatives continue to defeat broad portability under continuous BR checks. | MODEL-SPECIFIC classification recertified. |
| Benchmark terminology drift | PASS | First-best / unrestricted planner language is absent. | No change. |
| Global/SPNE inflation | PASS | Stage-I statements are compatibility/SPE statements conditional on certified continuations; high-z selection qualifier retained. | No change. |
| Formal-verification scope inflation | PASS | Manuscript says proof-critical core only and lists unformalized economic objects. | No change. |
| Invalid/NaN/nonconvergent solver outcomes | PASS AFTER HARDENING | Critical primitive and portability optimizers now fail closed on non-success or non-finite outputs. The alternative-mixed two-atom search remains explicitly diagnostic and is not theorem evidence. | Code hardened; CI regression required. |
| Source-version attribution | MAJOR JOURNAL-RISK, NOT THEORY DEFECT | 2013 VOR bibliographic lineage verified but equation-level VOR body not directly compared. | Manuscript consistently attaches equation-specific claims to the directly inspected 2012 predecessor model. Stage 12 must consider this risk in venue choice. |

## Independent known-model-in-disguise repetition

The strongest reduction remains the one-base common-control price game
\[
u_I=p[4-F_z(p-q)],\qquad u_P=qF_z(p-q),
\]
with
\[
F_z(x)=2[x]_0^1+[x+z]_0^1+[x-z]_0^1.
\]

This clearly belongs to the broad family of piecewise/captive-segment price games in which mixed pricing and pure nonexistence are known possibilities. The exact source-specific object nevertheless retains:
- the fixed four-offset aggregation 0,0,+z,-z;
- the exact critical equation 3z^2+12z-4=0;
- the source control-map UU/TT/TU;
- the Stage-II acquisition and Stage-I sharing embedding.

No direct theorem specialization located at Stage 6 or Stage 11 eliminates the need for the source-specific derivation. Generic-mechanism novelty remains killed; source-specific reassessment novelty survives.

## Certification regression and rollback record

Stage 11 found one defect that Stage 7.5A should have caught: grid regret was being used as the portability falsification metric.

Workflow response:
1. reopen affected Stage-7.5A diagnostic evidence;
2. replace grid-only certification with continuous best-response refinement;
3. require continuous unilateral regret below 1e-8;
4. update the portability derivation and Contribution Robustness Certificate;
5. strengthen manuscript wording;
6. recertify Stage 8 and Stage 10 because no theorem/quantifier changed.

Outcome:
- Beta(2,2) attack: portability failure survives;
- unequal-mass attack: portability failure survives;
- contribution remains MODEL-SPECIFIC;
- no baseline theorem or formal theorem is altered.

## Computational failure-mode audit

Critical optimizers now fail closed if SciPy reports non-success or non-finite objective/action values.

No project theorem depends on:
- a null/None return;
- NaN/Inf values;
- an unreported solver failure;
- the diagnostic alternative-mixed search.

The unrestricted mixed-uniqueness question remains explicitly unresolved rather than converted from a failed search into a theorem.

## Manuscript claim audit

No manuscript claim exceeds the frozen boundaries:
- no unique-mixed claim;
- no complete mixed correspondence claim;
- no selection-free high-z welfare/SPE claim;
- no generic portability claim;
- no first-best language;
- no VOR-specific equation-error claim;
- no whole-model formal-verification claim.

## Stage-11 verdict

Subject to the repaired regression suite passing on the current branch:

**GO — NO UNRESOLVED FATAL OR MAJOR THEORY/MANUSCRIPT DEFECT.**

The only major certification regression discovered at this gate has been repaired without changing theory.

## Formal closure record

- Stage: 11 — Full-Paper Hostile Referee / Robustness Gate.
- Certification regressions found: 1.
- Certification regressions repaired: 1.
- Theory rollback required: NO.
- Stage-7.5A diagnostic recertification required/performed: YES.
- Stage-8 freeze recertified: YES.
- Stage-10 manuscript recertified: YES.
- Remaining issue for Stage 12: journal positioning under MODEL-SPECIFIC contribution and WP/VOR equation-level source qualification.
- Next gate after CI pass: **Stage 12 — Journal Positioning**.
