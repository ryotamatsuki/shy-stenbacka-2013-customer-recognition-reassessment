# Stage 2 — Literature Frontier / Novelty Kill Gate

Date: 2026-09-23  
Workflow: `research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7` (v2.4)

## Research object tested
The candidate contribution is not “mixed pricing exists.” It is the source-specific reassessment:

1. identify the exact globality domain of the Shy–Stenbacka no-information price profile;
2. prove pure-equilibrium nonexistence on the remaining admissible wedge;
3. construct a valid mixed continuation for the affected uniform/uniform component;
4. propagate corrected continuation payoffs through investment, information sharing, switching, profit, consumer surplus, and total welfare.

## Exact prior-correction search
Fresh searches were run for:
- exact title + erratum / corrigendum / correction / comment / reply;
- DOI `10.1016/j.infoecopol.2013.03.002` + correction/comment;
- PII `S0167624513000115`;
- author names + customer recognition correction;
- RePEc/IDEAS, ScienceDirect, Boston Fed, Hanken, SciSpace, and citing-paper routes.

No erratum, corrigendum, author note, comment/reply, or later paper explicitly identifying the Eq. (8) kink failure or correcting the downstream backward induction was located.

This is a negative search result, not a proof of nonexistence.

## Closest application literature
### Source and directly adjacent work
- Shy & Stenbacka (2013), *Information Economics and Policy* 25(2), 92–106.
- Shy & Stenbacka, Boston Fed WP 12-4 (2012), complete inspected mathematical predecessor.
- Shy & Stenbacka, “Customer Recognition and Competition” (Boston Fed WP 11-7), an adjacent recognition/pricing model.
- de Nijs (2017), “Behavior-based price discrimination and customer information sharing,” *International Journal of Industrial Organization*.
- later personalized-pricing/customer-information papers, including work on imperfect recognition, customer-data sharing, and privacy.

None located in the fresh search states the present source-specific correction.

## Closest mixed-pricing literature
The following literature prevents any novelty claim that discrete customer heterogeneity or captive/switching demand can generate mixed prices:

- Yuval Shilony (1977), “Mixed Pricing in Oligopoly,” *Journal of Economic Theory* 14(2), 373–388.
- Hal R. Varian (1980), “A Model of Sales,” *American Economic Review* 70(4), 651–659.
- Chakravarthi Narasimhan (1988), “Competitive Promotional Strategies,” *Journal of Business* 61(4), 427–449.
- Rosa-Branca Esteves (2010), “Pricing with customer recognition,” *International Journal of Industrial Organization* 28(6), 669–681. The paper explicitly emphasizes mixed pricing with a discrete distribution of consumer preferences.
- later work on price dispersion with heterogeneous/captive consumers, including the support-characterization literature and Armstrong–Vickers on captive-customer competition.

Thus the mixed-strategy *phenomenon* is established prior art.

## Structural-isomorphism audit
Application-neutral canonical form of the affected Stage-III component:

- one incumbent control `p`;
- one common poaching control `q`;
- four consumer groups with valuation offsets `0,0,+z,-z`;
- within each group, a continuum of switching costs;
- aggregate poaching demand
[
F_z(p-q)=2[p-q]_0^1+[p-q+z]_0^1+[p-q-z]_0^1;
]
- piecewise-quadratic revenues;
- a common price crosses a kink and can optimally exclude one mismatch group.

This has family resemblance to:
- mixed-pricing oligopoly;
- captive/switcher models;
- multi-segment uniform pricing;
- spatial competition with finite brand loyalty.

However, no searched general theorem was found that mechanically yields the exact source-specific threshold
[
z_c=(-6+4\sqrt3)/3,
]
the particular two-point continuation, and the three-stage downstream investment/sharing/welfare reconstruction as a direct corollary.

## Theorem-absorption classification
- “mixed pricing can arise”: **ABSORBED / known**.
- “a common price across heterogeneous segments can exclude a segment”: **known mechanism family / not claimed as new**.
- exact Eq. (8) globality threshold for this model: **source-specific new correction candidate**.
- complete pure-equilibrium nonexistence wedge for this source game: **source-specific new correction candidate**.
- downstream corrected investment/sharing/welfare implications: **source-specific reassessment contribution candidate**.
- generic theorem for all common-control piecewise games: **not established and not required**.

## Citing-literature check
Recent citing literature continues to use the Shy–Stenbacka paper as part of the customer-recognition/information-sharing literature. The fresh search did not locate a citing paper flagging the present price-game defect. No evidence was found that the correction has already entered the literature through a differently titled comment.

## Novelty kill tests
1. **Exact prior correction found?** No.
2. **Headline mechanism already a named theorem whose direct specialization gives the correction?** Not located.
3. **Would the paper be only “mixed strategies exist”?** No; that framing is prohibited.
4. **Is the downstream reconstruction independent value?** Yes, conditional on closing the mixed-continuation scope and VOR-version qualification.
5. **Does the project require a prestige-driven general model extension?** No.

## Stage-2 verdict
**GO — SOURCE-SPECIFIC CORRECTION/REASSESSMENT SURVIVES NOVELTY KILL.**

Maximum defensible novelty wording:
> The contribution is a source-specific global-equilibrium correction and backward-induction reassessment. It does not claim novelty for mixed pricing with discrete customer heterogeneity as a general phenomenon.

## Stage-3 contract
Compare:
A. short correction limited to Eq. (8) + boundary multiplicity;
B. corrected continuation-game reassessment through Stage I and welfare;
C. general common-control pricing theorem.

The default should be B unless downstream effects collapse to a trivial qualification. C is permitted only if a natural general theorem emerges without changing the target model.
