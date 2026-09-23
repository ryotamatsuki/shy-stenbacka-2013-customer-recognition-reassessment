# Stage 0 — Evidence Freeze

## Objective
Convert the historical audit signal into a narrowly falsifiable, independently re-verifiable publication-development question without treating the upstream audit as proof.

## Frozen repository/workflow inputs
- Production input HEAD: `8c5994950b934dc8d6cf4c2a50be696488cb73af`.
- Production branch: `research/stage-00-evidence-freeze`.
- Canonical workflow: `ryotamatsuki/research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7` (v2.4; current main verified 2026-09-23).
- Historical audit branch: `ryotamatsuki/ozshypapers@final-cleanroom-theorem-audit-20260919`, branch HEAD `cbef3c56bf5b50e3db57a48671d3a9bef26a8f5b`.
- Historical target audit: `audits/investment_customer_recognition_information_exchange_2013_final.md`.
- Historical source record: `sources/investment_customer_recognition_information_exchange_2013_source_record.md`.
- Historical clean-room code: `code/investment_customer_recognition_information_exchange_2013_cleanroom.py`.

## Phenomenon versus proposed explanation
Phenomenon: the paper's Stage-III price formulas are obtained on interior demand branches, while the primitive consumer problem is clipped at switching thresholds 0 and 1.

Candidate explanation to test: a common poaching-price control across heterogeneous valuation groups can cross a clipping kink and make an interior FOC profile fail global best-response optimality.

This explanation is a hypothesis until independently reconstructed from primitives.

## Actors / decisions / frictions / outcomes
- Firms A and B.
- Stage I: share or not share customer information.
- Stage II: invest or not invest in recognition, cost c.
- Stage III: choose information-contingent incumbent/poaching prices.
- Consumers: valuation types HH, HL, LH, LL and switching-cost draw s in [0,1].
- Frictions: switching cost sigma*s and endogenous recognition/information sharing.
- Outcomes: price equilibria, investment, information sharing, switching, profits, consumer surplus, and total welfare.

## Research architecture candidates
A. Minimal correction: Eq. (8) counterexample plus equality/multiplicity corrections.
B. Continuation-game reassessment: solve the relevant clipped Stage-III price games, then rebuild Stage II and Stage I where pure continuation equilibria are available.
C. General common-control theorem: abstract the kinked uniform-pricing mechanism.

Initial choice: B. C is permitted only if it emerges naturally and survives theorem-absorption review; no journal-driven extension is authorized.

## Falsifiable research question
**When does the no-information price profile in Shy and Stenbacka (2013) solve the global clipped price game, and what do the resulting continuation-game qualifications imply for investment and information-sharing equilibria?**

This wording deliberately does not assume a corrected pure branch exists above the failure threshold and does not presuppose a welfare reversal.

## Source freeze status
See `sources/SOURCE_MANIFEST.md`.

- VOR bibliographic identity: VERIFIED.
- Complete mathematical body directly inspected: Boston Fed WP 12-4 (15 February 2012).
- VOR equation-by-equation identity: UNVERIFIED because the publisher formal body was not directly accessible.
- Claim policy: equation-level statements remain working-paper-qualified until the VOR body is verified.
- Historical upstream PDF SHA-256 is retained as provenance; it was not recomputed from raw bytes in this session.

## Independent discrepancy reproduction
`code/stage01_cleanroom_reproduction.py` was written without importing the upstream audit. It reconstructs the four clipped poaching demands and verifies:
- q0 = sigma/3;
- q* = (2 sigma + Delta)/6 on the three-active-group branch;
- gain = (3 Delta^2 + 12 Delta sigma - 4 sigma^2)/(36 sigma);
- threshold z_c = (-6 + 4 sqrt(3))/3;
- exact regression (sigma,Delta)=(25,8): q0=25/3, q*=29/3, gain=23/225.

The script also performs a separate exact rational direct-payoff calculation with clipping, not a second call to the symbolic expression.

## Prior-disclosure search
Fresh searches on 2026-09-23 covered:
- exact title + erratum/corrigendum/correction/comment/reply;
- DOI/PII + correction terms;
- Boston Fed, ScienceDirect, Hanken, RePEc/IDEAS;
- later customer-recognition / behavior-based price-discrimination literature.

No erratum, corrigendum, comment, reply, or author correction addressing Eq. (8), the equality correspondences, or Result 9 was located. This is a negative search result, not proof of nonexistence. Stage 2 must still perform broader forward/backward and structural-isomorphism review.

## Gate assessment
- Exact source identity: PASS, with explicit WP/VOR qualification.
- Independent central discrepancy: PASS.
- Exact regression: PASS.
- VOR publication attribution of the equation-level discrepancy: OPEN; claims remain source-version qualified.
- Fresh prior-disclosure screen: PASS for Stage 0; deeper novelty audit deferred to Stage 2.
- Research question: PASS.

## Canonical verdict
**GO TO AUDIT — SOURCE-VERSION QUALIFIED.**

The unresolved VOR body does not prevent analysis of the directly inspected working-paper model, because publication-facing wording is explicitly qualified. It remains a mandatory pre-submission blocker for any sentence asserting that the published VOR contains the same equation-level defect.

## Output state
Stage-0 artifacts were added after input HEAD `8c5994950b934dc8d6cf4c2a50be696488cb73af`. The last pre-report artifact commit is `139b106c23cba4a48832ec500cbe2772136a462c`; the Git commit containing this report is the Stage-0 closure record.

## Stage-1 contract
Reconstruct timing, information sets, thresholds, payoff functions, all relevant Stage-III displayed profiles, Tables 1–9/Results 1–10 dependencies, exact counterexample, and equality/SPE multiplicity from primitives. The historical audit may be used only as provenance/regression target.
