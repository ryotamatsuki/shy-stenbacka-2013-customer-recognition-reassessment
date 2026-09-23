# Stage 6 — Novelty Re-Kill

Date: 2026-09-23  
Workflow: \`research-paper-workflow@63f11a50a13d9328213498a5a6576d00b9bceef7\` (v2.4)  
Input branch: \`research/stage-06-novelty-rekill\`

## Objective

Re-run the novelty and theorem-absorption gate **after** Stage 4/4A has fixed the actual theorem set. Stage 6 does not ask whether mixed pricing is known. It asks whether the final correction/reassessment can be reduced to, or directly imported from, prior work.

The theorem set tested is:

1. the exact validity threshold
\[
z_c=\frac{-6+4\sqrt3}{3};
\]
2. unique pure \`UU\` equilibrium for \`0<z\le z_c\`;
3. no pure \`UU\` equilibrium for \`z_c<z<1/3\`;
4. existence of the displayed symmetric two-point mixed continuation on the high-\`z\` wedge;
5. propagation of corrected Stage-III continuation payoffs into Stage-II investment incentives, Stage-I information-sharing incentives, switching, profit, consumer surplus, and total welfare;
6. explicit selected-continuation quantification for all high-\`z\` downstream claims unless a later gate proves selection invariance.

## 1. Exact correction / prior-disclosure re-search

Fresh searches on 2026-09-23 covered:

- exact title + \`erratum\`, \`corrigendum\`, \`correction\`, \`comment\`, \`reply\`, \`reassessment\`;
- DOI \`10.1016/j.infoecopol.2013.03.002\` + correction terms;
- PII \`S0167624513000115\`;
- exact title + \`pure strategy\`, \`mixed strategy\`, \`equilibrium failure\`;
- exact critical expression \`(-6+4 sqrt(3))/3\`;
- exact regression value \`23/225\`;
- citation routes around customer recognition, information sharing, switching costs, behavior-based pricing, and mixed pricing.

Sources/routes checked included ScienceDirect, RePEc/IDEAS, Federal Reserve Bank of Boston, Hanken, SciSpace, and general scholarly web indexing.

### Result
No erratum, corrigendum, author correction, comment/reply, or later article was located that identifies the present source-specific \`UU\` globality failure, derives the exact threshold \`z_c\`, or reconstructs the affected three-stage backward induction.

This remains a negative search result, not proof of nonexistence.

## 2. Closest prior theory families

### 2.1 Mixed pricing with discrete heterogeneity
Rosa-Branca Esteves (2010), “Pricing with customer recognition,” *International Journal of Industrial Organization* 28(6), 669–681, explicitly studies customer recognition with a discrete distribution of consumer preferences and mixed pricing. The paper itself places the mechanism in the Shilony (1977), Varian (1980), and Narasimhan (1988) mixed-pricing tradition.

**Absorption consequence:**  
The present paper must not claim that discrete consumer heterogeneity, customer recognition, brand loyalty, or captive/switcher demand generating mixed prices is new.

### 2.2 Switching-cost mixed pricing
The switching-cost literature includes “Mixed pricing in oligopoly with consumer switching costs” (1992, *International Journal of Industrial Organization* 10(3), 393–411).

**Absorption consequence:**  
The fact that switching costs can coexist with mixed pricing is established prior art.

### 2.3 Pure nonexistence plus mixed equilibrium in spatial/captive-buyer competition
Kawai and Nakagawa (2025), “Price Equilibria in a Spatial Competition with Captive Buyers,” characterizes parameter regions with no pure equilibrium and constructs mixed equilibria in a spatial competition model with captive buyers.

**Absorption consequence:**  
“Pure equilibria can disappear in a spatial/captive-buyer price game and mixed pricing can replace them” is not a novel generic theorem.

However, their model does not supply the Shy–Stenbacka four-type clipped-demand game, the threshold \`z_c\`, the \`UU/TT/TU\` information-control decomposition, or the three-stage investment/sharing/welfare reconstruction.

### 2.4 Customer-data sharing / recognition literature after 2013
Relevant later application work includes:
- de Nijs (2017), “Behavior-based price discrimination and customer information sharing,” *International Journal of Industrial Organization* 50, 319–334;
- Choe, Cong, and Wang (2024), “Softening Competition Through Unilateral Sharing of Customer Data,” *Management Science* 70(1), 526–543;
- Colombo, Graziano, and Pignataro (2024), “Imperfect history-based price discrimination with asymmetric market shares,” *Information Economics and Policy* 67;
- Colombo, Graziano, and Pignataro (2025), “Personalized pricing with imperfect customer recognition,” *Information Economics and Policy* 70, 101129.

These papers confirm that customer recognition, partial information, data sharing, and welfare remain active literatures. None located in the Stage-6 search states the present correction.

## 3. Structural-isomorphism test

The corrected \`UU\` segment is
\[
F_z(x)=2[x]_0^1+[x+z]_0^1+[x-z]_0^1,
\]
with incumbent and poacher controls entering through \`x=p-q\`.

The source-specific theorem depends on all of the following simultaneously:

- exactly four inherited valuation groups with offsets \`0,0,+z,-z\`;
- one common incumbent/poaching price over those groups in the \`UU\` information state;
- clipped switching masses;
- the maintained domain \`0<z<1/3\`;
- a source candidate at \`(p,q)=(2/3,1/3)\`;
- a competing three-active poaching vertex;
- the exact crossing
\[
3z^2+12z-4=0;
\]
- embedding of that continuation into the source paper's Stage-II and Stage-I games.

No searched prior theorem takes those primitives as an immediate special case and returns the exact Stage-4/4A theorem set without additional derivation.

## 4. Theorem-absorption matrix

| Candidate contribution | Stage-6 classification | Reason |
|---|---|---|
| Mixed pricing can arise with customer recognition/discrete tastes | **ABSORBED / KNOWN** | Esteves 2010 and older mixed-pricing literature |
| Mixed pricing can arise with switching costs | **ABSORBED / KNOWN** | established switching-cost pricing literature |
| Pure price equilibrium can fail and mixed equilibrium can emerge in spatial/captive-buyer competition | **ABSORBED AS A GENERIC MECHANISM** | e.g. Kawai–Nakagawa 2025 |
| A common price can optimally exclude one heterogeneous segment | **KNOWN MECHANISM FAMILY** | standard piecewise/captive-segment pricing logic |
| Exact Shy–Stenbacka \`UU\` threshold \`z_c=(-6+4sqrt(3))/3\` | **SURVIVES** | no direct prior correction/theorem located |
| Complete pure correspondence in the source \`UU\` game | **SURVIVES** | no source-specific prior characterization located |
| Source-specific symmetric two-point continuation | **SURVIVES AT EXISTENCE SCOPE** | no direct prior construction located; uniqueness not claimed |
| \`UU/TT/TU\` equation-impact decomposition for Eqs. (6)–(11),(17) | **SURVIVES** | source-specific reconstruction |
| Corrected Stage-II investment thresholds | **SURVIVES, CONDITIONAL ON HIGH-z CONTINUATION WHERE APPLICABLE** | downstream source-specific consequence |
| Corrected Stage-I sharing/SPE implications | **SURVIVES AT CERTIFIED QUANTIFIER** | downstream source-specific consequence |
| Corrected profit/consumer-surplus crossings | **SURVIVES AT SELECTED-CONTINUATION SCOPE** | not supplied by generic mixed-pricing literature |
| Total-welfare survival/reclassification | **SURVIVES AT CERTIFIED QUANTIFIER** | source-specific reassessment |
| General theorem for arbitrary common-control piecewise games | **NOT ESTABLISHED / NOT CLAIMED** | unnecessary extension |

## 5. Novelty kill tests

### Test A — Exact prior correction
**PASS.** No exact prior correction was located.

### Test B — Direct theorem specialization
**PASS.** No searched theorem mechanically specializes to the complete source-specific correction.

### Test C — Generic-mechanism overclaim
**PASS AFTER SCOPE REDUCTION.** Generic mixed pricing and generic pure-nonexistence mechanisms are treated as prior art, not contributions.

### Test D — Downstream value
**PASS.** The project does more than identify a deviation: it changes the admissible Stage-III equilibrium object and thereby requires a new Stage-II/Stage-I and welfare reconstruction.

### Test E — Need for generalization
**NO.** A broad common-control theorem is not needed to justify publication value and would increase proof/positioning burden.

### Test F — Selection-robust novelty
**PASS WITH QUALIFIER.** High-\`z\` downstream novelty is explicitly tied to the certified selected continuation unless later selection invariance is proved.

## 6. Maximum defensible contribution statement

The manuscript may claim, in substance:

> We identify a source-specific global-equilibrium defect in the no-information price subgame of the inspected Shy–Stenbacka model, characterize the exact parameter region in which the reported pure price profile remains valid, prove pure-strategy nonexistence on the remaining admissible region, construct a certified mixed continuation there, and reassess the model's investment, information-sharing, profit, consumer-surplus, and welfare conclusions under the corrected continuation.

The manuscript must **not** claim:
- discovery of mixed pricing as a phenomenon;
- discovery that heterogeneous/captive/switching consumers can eliminate pure price equilibrium;
- a new generic mixed-pricing theorem;
- uniqueness of the high-\`z\` mixed equilibrium;
- an unqualified correction to the 2013 VOR until equation-level VOR comparison is directly verified.

## 7. Positioning consequence

The paper is best positioned as a **correction/reassessment with substantive downstream consequences**, not as a general theory paper.

The strongest publication value comes from the combination:
1. exact source-model equilibrium correction;
2. complete pure correspondence;
3. nontrivial admissible pure-nonexistence wedge;
4. constructive mixed continuation;
5. changed investment/profit/consumer-surplus implications;
6. explicit demonstration of which welfare conclusions survive.

This is materially stronger than a one-equation corrigendum but narrower than a generic mixed-pricing contribution.

## 8. Stage-6 verdict

**GO — NOVELTY RE-KILL SURVIVED AT SOURCE-SPECIFIC REASSESSMENT SCOPE.**

The final theorem set is not absorbed by the searched literature. The project remains publishable in principle as a source-specific correction/reassessment, subject to mathematical and manuscript gates still to come.

## 9. Formal closure record

- Stage: 6 — Novelty Re-Kill
- Closure date: 2026-09-23
- Input: Stage 4 closed construction + Stage 4A closed adversarial certificate.
- Exact prior-correction re-search: **PASS — none located**.
- Structural-isomorphism re-search: **PASS**.
- Generic mixed-pricing novelty: **KILLED / absorbed**.
- Generic pure-nonexistence-to-mixing novelty: **KILLED / absorbed as mechanism family**.
- Exact source-model threshold/correspondence: **SURVIVES**.
- Source-specific downstream reassessment: **SURVIVES at certified quantifier**.
- General-theory extension: **NOT AUTHORIZED / NOT REQUIRED**.
- VOR attribution qualification: **carried forward**.
- Mixed-selection qualification: **carried forward**.
- Exact correctness blocker at Stage-6 scope: **NONE**.
- Canonical verdict: **STAGE 6 CLOSED — GO.**
- Next gate: **Stage 7 — Backward Induction and Welfare Reconstruction closure**.

## Search/reference anchors

- Shy & Stenbacka (2013), ScienceDirect: https://www.sciencedirect.com/science/article/pii/S0167624513000115
- Boston Fed WP 12-4: https://www.bostonfed.org/publications/research-department-working-paper/2012/investment-in-customer-recognition-and-information-exchange.aspx
- RePEc/IDEAS target record: https://ideas.repec.org/a/eee/iepoli/v25y2013i2p92-106.html
- Esteves (2010): https://www.sciencedirect.com/science/article/abs/pii/S0167718710000408
- de Nijs (2017): https://www.sciencedirect.com/science/article/pii/S0167718716304234
- Choe, Cong & Wang (2024): https://doi.org/10.1287/mnsc.2023.4689
- Colombo, Graziano & Pignataro (2025): https://doi.org/10.1016/j.infoecopol.2025.101129
- Kawai & Nakagawa (2025): https://arxiv.org/abs/2505.06961
