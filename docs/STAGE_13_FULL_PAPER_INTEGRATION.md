# Stage 13 — Full-Paper Integration

Date: 2026-09-23
Primary target: Information Economics and Policy
Input: Stage-8 frozen theory + Stage-11 surviving manuscript + Stage-12 journal positioning.

## Objective

Turn the independently certified manuscript sections and journal-specific submission materials into one coherent IEP submission package without enlarging the frozen contribution.

## Integration audit

### Introduction
PASS.
- question: global validity of the no-information common-price continuation;
- mechanism: common pricing over heterogeneous clipped switching segments;
- main result: exact pure-validity threshold and high-z pure nonexistence;
- downstream contribution: investment/sharing/profit/CS/welfare reassessment;
- contribution boundary: model-specific;
- mixed-selection qualifier: explicit;
- source-version qualifier: explicit.

No claim exceeds the Stage-7.5A contribution-robustness certificate.

### Related literature
PASS.
The literature is organized by conceptual relationship:
1. classic mixed-pricing / sales models;
2. customer recognition and behavior-based pricing;
3. recent IEP work on information sharing, algorithmic pricing, and imperfect recognition;
4. source-specific distinction from generic mechanism families.

Current IEP additions integrated:
- Colombo, Filippini & Pignataro (2024);
- Dubus (2024);
- Colombo, Graziano & Pignataro (2025).

### Model
PASS.
No new primitive, timing assumption, refinement, price restriction, or tie-breaking rule was introduced after Stage 8.

### Results
PASS.
The manuscript proves:
- complete baseline pure UU correspondence;
- exact counterexample;
- existence/global-best-response validity of the selected mixed continuation;
- corrected Stage-II/Stage-I correspondences;
- corrected profit/consumer-surplus rankings;
- surviving total-welfare ordering.

Unrestricted mixed uniqueness remains unclaimed.

### Discussion
PASS.
The discussion interprets:
- sequential propagation of a terminal-game correction;
- separation of private incentives, CS, and total welfare;
- failed portability;
- selected-continuation limitation;
- source-version evidence boundary.

It does not enlarge theory.

### Conclusion
PASS.
No new theorem, policy claim, generality claim, planner benchmark, or VOR-specific attribution is introduced.

### Terminology / notation
PASS.
Canonical notation remains:
- z = Delta/sigma;
- k = c/sigma;
- z_c = (-6+4sqrt(3))/3;
- K_S and K_NS;
- UU, TT, TU;
- selected mixed continuation p*, q_L, q_H, lambda.

“First best,” generic portability, unique mixed equilibrium, and complete mixed-equilibrium correspondence remain absent.

### Tables / figures
PASS.
No figures are retained.

Two manuscript tables are generated reproducibly from code/generate_tables.py:
- key thresholds/crossings;
- Results 1–10 disposition map.

No hand-entered quantitative figure/table is used as evidence.

### Formal verification language
PASS.
The manuscript states:
- proof-critical algebraic core only;
- clean Lean/mathlib build and allowed-axiom audit;
- economic primitives, branch exhaustiveness, full equilibrium correspondence, backward induction, and portability are not claimed as formalized.

This matches theorem_certificates/FORMAL_VERIFICATION_CERTIFICATE.md.

## Journal-specific integration

### Author metadata
Integrated:
- Ryota Matsuki;
- Independent Researcher;
- Matsuyama, Ehime 790-0853, Japan;
- corresponding email;
- ORCID.

### Keywords
Six keywords integrated after the abstract, within current Elsevier generic guidance.

### Highlights
submission/highlights.txt contains four bullets; each is <=85 characters.

### Cover letter
submission/cover_letter.md integrates:
- IEP fit;
- source-version qualification;
- exact equilibrium contribution;
- downstream importance;
- MODEL-SPECIFIC portability classification;
- mixed-existence/uniqueness boundary;
- formal-verification boundary;
- originality/funding/COI declarations.

### Declarations
Integrated in manuscript and submission package:
- acknowledgments: none;
- funding: no external funding;
- competing interests: none;
- no external dataset;
- reproducibility repository;
- ethics not applicable to pure theory.

### Generative-AI disclosure
Current Elsevier policy rechecked on 2026-09-23.

Integrated in two places:
1. research/code-use description in the scope/verification section;
2. separate declaration immediately before references.

The disclosure identifies OpenAI ChatGPT, states the purposes of use, records independent checking/editing, and assigns full responsibility to the author.

## Source and anonymity posture

Publicly available current IEP-specific peer-review/anonymization instructions were not sufficiently exposed to certify a current double-anonymization requirement. Historical official IEP guidance used single-anonymized review.

Stage 13 therefore:
- retains author metadata in the manuscript;
- separately prepares submission/title_page.md;
- does not fabricate a journal-specific anonymization rule.

If the authenticated Stage-14 portal requires an anonymized manuscript, removing the author block/declarations from the reviewer copy is an editorial-format transformation and does not reopen theory.

## Scientific consistency matrix

| Submission object | Source scope | Mixed scope | Portability | Formal scope |
|---|---|---|---|---|
| Abstract | WP/predecessor qualified | selected continuation downstream | model-specific | proof-critical algebra only |
| Introduction | same | same | same | same |
| Main results | direct baseline theorem | existence only for mixed | no transport | no whole-model claim |
| Discussion | same | limitation explicit | failed tests explicit | limitation explicit |
| Conclusion | same | limitation explicit | model-specific | limitation explicit |
| Cover letter | same | uniqueness not claimed | model-specific | proof-critical core |
| Highlights | no VOR-specific equation claim | no uniqueness claim | no generic claim | no formalization overclaim |

## CI / build gate

Stage 13 closure requires:
- mathematical regression suite: SUCCESS;
- continuous-BR portability regression: SUCCESS;
- Lean clean build / axiom / placeholder audit: SUCCESS;
- deterministic tables: SUCCESS;
- clean manuscript LaTeX/BibTeX build: SUCCESS;
- unresolved citation/cross-reference check: SUCCESS.

## Current verdict

**PENDING CI — INTEGRATION COMPLETE, CLOSURE AWAITS GREEN BUILD.**

No substantive inconsistency has been found.
