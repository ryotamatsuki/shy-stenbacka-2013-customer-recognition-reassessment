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

## Fresh Stage-14 CI evidence

Verification head:
`570be4152e006467f0582639e2fcfe99a96898d2`

Draft verification PR: #7 — verification only, never merge.

### Mathematical / metadata regression
verify-reassessment run #190, id `35851671051`, job `107150566378`: **SUCCESS**.

Passed:
- Stage 1 exact reproduction;
- Stage 4 symbolic construction;
- Stage 4 active-set certificate;
- Stage 4A primitive evaluator;
- Stage 7 backward-induction/welfare identities;
- Stage 7 equilibrium-correspondence audit;
- Stage 7 primitive welfare evaluator;
- Stage 7.5A continuous-best-response portability falsification;
- deterministic manuscript tables;
- Stage-14 submission consistency checks.

Submission-check output:
- abstract words: **202**;
- keyword count: **6**;
- highlight count: **4**;
- highlight lengths: **[77, 77, 79, 75]**;
- result: `stage14_submission_checks=PASS`.

### Formal verification
verify-reassessment run #190, formal job `107150566586`: **SUCCESS**.

- Lean build: **8940 jobs, SUCCESS**;
- axiom audit: **58 declarations** under `SS2013Reassessment`;
- allowed axioms only: `propext`, `Classical.choice`, `Quot.sound`;
- proof-placeholder rejection: **SUCCESS**.

Formal coverage remains the proof-critical algebraic core only.

### Manuscript / package build
manuscript-build run #13, id `35851670988`, job `107150566265`: **SUCCESS**.

Passed:
- deterministic table regeneration;
- Stage-14 submission consistency checks;
- LaTeX/BibTeX manuscript build;
- unresolved citation/reference rejection;
- submission bundle construction;
- manuscript PDF upload;
- submission bundle upload.

## Final artifacts

GitHub Actions manuscript artifact:
- artifact id: `10745293723`;
- artifact digest: `sha256:fb5c511fc773f9f9eda84742ff1d537e875a9acc587358fb75bddeeb7eddb1c0`.

Final PDF internal SHA-256:
`358c6c02032de120b3c1cbdb5203eb632bf973be4626b09838ceb1342cde8601`.

GitHub Actions IEP submission-bundle artifact:
- artifact id: `10746255279`;
- artifact digest: `sha256:c8c17526a8163c4e87fccd4a6c5e5797e7505bf9858912cc33af0a3954fa4ca7`.

Downloaded inner `iep_submission_bundle.tar.gz` SHA-256:
`90458447ae2be53cf4a6abe3e878d1f58f3291da7842215d513716b2928efac6`.

The PDF inside the fresh submission bundle has the **same SHA-256** as the standalone final PDF.

The clean bundle contains 23 intended files:
- final PDF;
- main LaTeX source;
- bibliography;
- all section sources;
- generated table sources;
- title page;
- cover letter;
- highlights;
- declarations.

No `.aux`, `.log`, `.out`, `.blg`, or other build debris is included.

A clean extraction was rebuilt from the bundled LaTeX/BibTeX source; it produced a 19-page manuscript with no unresolved citation/reference warnings.

## Final PDF inspection

Final PDF:
- pages: **19**;
- page size: US Letter;
- encrypted: no;
- forms/JavaScript: none;
- all 15 PDF fonts: **embedded and subset**;
- all 19 pages contain extractable text;
- no text block extends outside the page boundary;
- no Unicode replacement glyph was detected.

Visual QA:
- **all 19 pages inspected** using rendered page contact sheets;
- title/author/abstract/keywords on page 1: readable and unclipped;
- threshold table page: readable and within margins;
- Results 1–10 table page: readable and within margins;
- appendix/declarations page: readable;
- generative-AI declaration and references page: readable;
- no visible clipped equation, overlapping text, black square, broken glyph, or unreadable table was found.

No figures are present, so raster/vector-artwork DPI/color checks are not applicable.

## Submission-object consistency

PASS:
- manuscript title = title-page title = cover-letter title;
- source-version qualification consistent;
- mixed-equilibrium existence/uniqueness scope consistent;
- MODEL-SPECIFIC portability classification consistent;
- formal-verification scope consistent;
- declarations consistent;
- CRediT present;
- current AI disclosure split correctly between research methodology and manuscript-preparation declaration;
- funding/COI/data-code statements present;
- abstract/keywords/highlights satisfy current public Elsevier limits;
- no substantive theory drift from Stage 8.

## Authenticated portal boundary

Authenticated portal-only requirements cannot be certified from public access. If all non-portal QA passes, the maximum Stage-14 state is:

**CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**

This is a passing Stage-14 workflow state but is not authorization to click Submit and is not Stage 15 freeze.

## Formal closure record

- Stage: 14 — Submission QA.
- Closure date: 2026-09-23.
- Primary target: Information Economics and Policy.
- Submission-package QA head: `570be4152e006467f0582639e2fcfe99a96898d2`.
- Mathematical regressions: PASS.
- Continuous-BR portability regression: PASS.
- Formal verification: PASS — PROOF-CRITICAL CORE.
- Deterministic tables: PASS.
- Stage-14 metadata/scope checks: PASS.
- Clean manuscript build: PASS.
- Citations/cross-references: PASS.
- Editable source bundle: PASS.
- Final PDF page-by-page visual QA: PASS.
- Font embedding/legibility: PASS.
- Current public journal-policy recheck: PASS at public-evidence scope.
- Substantive correction pending: NONE.
- Fatal/major referee attack pending: NONE.
- Stage-15 submission freeze: **NOT PERFORMED / NOT AUTHORIZED**.
- Journal submission: **NOT PERFORMED**.

Only remaining item:
**authenticated Editorial Manager portal preflight**, including current article-type label, file designations, reviewer fields, review/anonymity handling, portal declaration fields, and inspection of the portal-generated merged PDF.

## Final Stage-14 verdict

**STAGE 14 CLOSED — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**

This is the maximum passing state permitted by the canonical workflow when the only unresolved items are authenticated-portal fields. It is **not** authorization to click Submit and is **not** Stage 15 Submission Freeze.
