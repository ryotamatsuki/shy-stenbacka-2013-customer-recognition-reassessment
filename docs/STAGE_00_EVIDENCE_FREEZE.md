# Stage 0 — Evidence Freeze

## Objective
Establish a self-contained evidentiary base before any publication-facing corrected proposition is frozen.

## Input
- Production base: `8c5994950b934dc8d6cf4c2a50be696488cb73af`
- Canonical workflow: `ryotamatsuki/research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7` (v2.4)
- Historical audit only as provenance/regression target:
  - `ryotamatsuki/ozshypapers@final-cleanroom-theorem-audit-20260919`
  - `audits/investment_customer_recognition_information_exchange_2013_final.md`
  - `sources/investment_customer_recognition_information_exchange_2013_source_record.md`
  - `code/investment_customer_recognition_information_exchange_2013_cleanroom.py`

## Bibliographic freeze
Target:
Oz Shy and Rune Stenbacka (2013), “Investment in Customer Recognition and Information Exchange,” *Information Economics and Policy* 25(2), 92–106.

- DOI: `10.1016/j.infoecopol.2013.03.002`
- PII: `S0167624513000115`
- ScienceDirect VOR record: https://www.sciencedirect.com/science/article/pii/S0167624513000115
- Hanken institutional record: https://research.hanken.fi/en/publications/investment-in-customer-recognition-and-information-exchange/
- Boston Fed predecessor page: https://www.bostonfed.org/publications/research-department-working-paper/2012/investment-in-customer-recognition-and-information-exchange.aspx
- Boston Fed complete WP PDF: https://www.bostonfed.org/-/media/Documents/Workingpapers/PDF/economic/wp/wp2012/wp1204.pdf

The Boston Fed page explicitly states that a revised version was published in *Information Economics and Policy* 25(2), 92–106 (2013).

## VOR gate
On 2026-09-23 the ScienceDirect record and substantial introduction/metadata were reachable through public indexing, but direct access to the formal body still returned HTTP 403 when re-opened. No lawful equation-level VOR copy was located in the public routes checked so far. Hanken confirms the final bibliographic record but does not expose the mathematical body.

Therefore:
- the complete 15 February 2012 Boston Fed WP is the mathematical source currently used for derivation;
- no equation-level claim is yet attributed unqualifiedly to the VOR;
- VOR/WP identity remains an explicit Stage-1 open item and blocks final publication-facing wording if unresolved.

Historical upstream SHA-256 for the WP is `d2ca6b4959fd0b4436e8f35702f81086f564e064e1c962d05a6b987054ba7f16`. This hash is preserved as provenance; it has not yet been independently rehashed in this production environment.

## Independent discrepancy reproduction
The production analysis restarted from the primitive clipped switching masses rather than importing the upstream branch result.

Normalize `sigma=1`, `z=Delta/sigma`, and define
[
F(x)=2\operatorname{clip}(x)+\operatorname{clip}(x+z)+\operatorname{clip}(x-z).
]
For a no-information incumbent/poacher price pair `(p,q)`, the segment payoffs are
[
u_I(p,q)=p[4-F(p-q)],\qquad u_P(q,p)=qF(p-q).
]

At the source profile `p=2/3, q=1/3`, the poacher has a competing three-active-group maximizer
[
q_H=(2+z)/6,
]
with gain
[
G(z)=\frac{3z^2+12z-4}{36}.
]
Hence the source profile ceases to be a global best response when
[
z>z_c=\frac{-6+4\sqrt3}{3}.
]

At `sigma=25, Delta=8` (`z=8/25`), the dimensioned gain is reproduced exactly as
[
25G(8/25)=23/225>0.
]

This was checked by a separate primitive clipped-demand evaluator as well as symbolic algebra.

## Fresh prior-disclosure search
Searches run on 2026-09-23 included:
- exact title + erratum/corrigendum/correction/comment/reply;
- DOI/PII + correction;
- ScienceDirect, Boston Fed, Hanken, RePEc/IDEAS;
- citing/customer-recognition/behavior-based-pricing routes;
- application-neutral searches for mixed pricing with discrete customer types and uniform controls.

No erratum, corrigendum, author correction, or paper explicitly identifying the present Eq. (8) kink failure was located. This is a negative search result, not proof of nonexistence.

## Research question selected
**When is the no-information price profile in Shy and Stenbacka globally optimal, what replaces it when the clipped price game loses a pure equilibrium, and how do the resulting continuation payoffs alter investment, information sharing, and welfare?**

This is narrower and more falsifiable than presupposing a welfare reversal.

## Verdict
**CONDITIONAL GO — STAGE 0 CLOSED FOR INTERNAL RESEARCH.**

Conditions carried forward:
1. VOR equation-level comparison remains open.
2. Publication-facing attribution must remain WP/VOR-qualified until that gate closes.
3. The central task is the complete clipped Stage-III equilibrium, not the counterexample alone.

## Next-stage contract
Stage 1 must complete source/result mapping and continue lawful VOR retrieval. Stage 4 mathematics may proceed in parallel, but Stage 8 freeze and any unqualified VOR correction claim remain blocked until the source-version issue is resolved or the final manuscript is explicitly scoped to the verified version.


## Formal closure record

- Stage: 0 — Evidence Freeze
- Input SHA: `8c5994950b934dc8d6cf4c2a50be696488cb73af`
- Canonical workflow: `research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7`
- Files/evidence frozen: `README.md`, `PROVENANCE.md`, `CLAIM_BOUNDARY.md`, `EVIDENCE_MAP.md`, this report, and upstream audit/source references.
- Independent tests: primitive clipped-demand reconstruction; exact `(sigma,Delta)=(25,8)` regression; fresh prior-disclosure search.
- Rejected shortcut: treating the historical upstream audit as publication proof.
- Unresolved issue carried forward: equation-level VOR/WP comparison.
- Canonical verdict: **STAGE 0 CLOSED — CONDITIONAL GO (VOR attribution qualification carried forward).**
- Next-stage contract: Stage 1 must complete the source/result ledger, timing/strategy map, mathematical dependency graph, and explicit WP/VOR claim boundary.
