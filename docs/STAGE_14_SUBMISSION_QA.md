# Stage 14 — Submission QA

Date: 2026-09-23  
Primary target: Information Economics and Policy  
Input: Stage-13 integrated IEP package.

## QA standard

This gate applies:
- workflow Submission Checklist;
- Figure/Table Checklist;
- frozen Formal Verification Certificate;
- current IEP/Elsevier public requirements ledger;
- fresh clean CI;
- page-by-page inspection of the final manuscript PDF.

A substantive mismatch reopens the earliest affected stage.

## Public journal-rule recheck

Rechecked on 2026-09-23:
- current IEP scope/article-type page;
- current IEP Editorial Manager portal landing page;
- current Elsevier keyword guidance;
- current Elsevier highlights guidance;
- current Elsevier CRediT guidance;
- current Elsevier data-statement guidance;
- current Elsevier generative-AI policy;
- legacy official IEP author pack for journal-specific single-file and review-mode evidence where current public IEP fields are not exposed.

Current public IEP pages do not expose all authenticated submission-record fields. These are classified explicitly as portal-only rather than inferred.

## Manuscript metadata preflight

- final title: synchronized across manuscript, title page, and cover letter;
- author: Ryota Matsuki;
- affiliation: Independent Researcher;
- corresponding email: present;
- postal address: present;
- ORCID: present;
- abstract: deterministic check <=250 words;
- keywords: deterministic check <=6;
- highlights: deterministic check 3–5 items, each <=85 characters;
- identified manuscript: prepared;
- separate title page: prepared;
- anonymous manuscript: not prepared because current public evidence does not establish a double-anonymized IEP requirement; authenticated portal preflight must confirm.

## Claim-scope preflight

The deterministic Stage-14 check rejects:
- stale TODO/FIXME/pending scaffold text;
- “the unique mixed equilibrium”;
- “the complete mixed-equilibrium correspondence”;
- VOR-specific “published Eq. (8) is wrong” language;
- whole-model formal-verification language.

Required scope anchors:
- model-specific contribution;
- unrestricted mixed-equilibrium uniqueness not claimed;
- working-paper/source-version qualification;
- proof-critical formal-verification scope.

## Declarations preflight

Integrated:
- CRediT;
- acknowledgments;
- funding;
- competing interests;
- data/code availability;
- generative-AI manuscript-preparation declaration;
- research-methodology disclosure of AI-assisted source/code/proof support;
- ethics N/A statement in submission declarations.

Acknowledgments/funding/COI are not duplicated on the separate title page.

## Figure/table/artwork preflight

Figures: none.

Tables:
1. key thresholds/crossings;
2. Results 1–10 disposition.

Both are generated from code/generate_tables.py in the pinned Python environment and embedded/cited in the manuscript.

Artwork-specific DPI/color checks: NOT APPLICABLE.

Stage 14 must still inspect table pages visually for overflow, clipping, broken glyphs, and readable font size.

## Formal-verification preflight

Required artifacts present:
- formal/SS2013Reassessment.lean;
- lean-toolchain;
- lakefile.lean;
- lake-manifest.json;
- theorem_certificates/FORMAL_VERIFICATION_CERTIFICATE.md.

Fresh Stage-14 CI must pass:
- Lean build;
- axiom audit;
- placeholder rejection.

Manuscript wording remains “proof-critical algebraic core,” not whole-model verification.

## Reproducibility/source-package preflight

Fresh CI is configured to:
- run all mathematical regressions;
- run continuous-BR portability regression;
- regenerate tables;
- run Stage-14 metadata/scope consistency script;
- rebuild the manuscript;
- reject unresolved citations/references;
- package editable LaTeX/BibTeX/section/table sources;
- upload manuscript PDF and an auditable IEP submission bundle.

## Pending exit checks

- fresh Stage-14 mathematical CI;
- fresh Stage-14 formal CI;
- fresh clean manuscript build;
- fresh source-bundle artifact;
- final PDF materialization and page-by-page inspection;
- final PDF metadata/page count/font/render inspection;
- final PROJECT_STATUS synchronization.

## Authenticated portal boundary

Authenticated portal-only requirements cannot be certified from public access. If all non-portal QA passes, the maximum Stage-14 state is:

**CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**

This is a passing Stage-14 workflow state but is not authorization to click Submit and is not Stage 15 freeze.

## Current verdict

**PENDING FRESH CI AND PDF INSPECTION.**
