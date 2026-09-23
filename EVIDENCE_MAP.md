# Evidence Map

## Core mathematical correction

| Object | Evidence |
|---|---|
| Pure \`UU\` correspondence | \`docs/STAGE_04_PRICE_GAME_CONSTRUCTION.md\`; \`derivations/stage04_active_set_certificate.md\`; \`code/stage04_global_price_certification.py\` |
| Independent Stage-III attack | \`docs/STAGE_04A_ADVERSARIAL_CERTIFICATION.md\`; \`code/stage04a_primitive_evaluator.py\` |
| Exact \`23/225\` counterexample | \`code/stage01_cleanroom_reproduction.py\`; Lean theorem \`exact_counterexample_gain\` |
| Mixed continuation | Stage 4 construction + Stage 4A primitive global-BR audit |
| Alternative mixed falsification | \`code/stage04a_mixed_alternative_search.py\`; diagnostic only, not uniqueness proof |

## Backward induction and welfare

| Object | Evidence |
|---|---|
| Threshold identities | \`code/stage07_backward_induction.py\`; Lean \`corrected_threshold_gap\` |
| Stage-II / Stage-I correspondence | \`code/stage07_equilibrium_correspondence_audit.py\`; \`derivations/stage07_equilibrium_welfare_certificate.md\` |
| Consumer surplus | \`code/stage07_primitive_welfare.py\` direct utility integration |
| Welfare identities | Stage 7 symbolic + primitive audit; Lean proof-critical identities |
| Results 1–10 map | \`docs/STAGE_07_BACKWARD_INDUCTION_WELFARE.md\` |

## Novelty and scope

| Object | Evidence |
|---|---|
| Novelty re-kill | \`docs/STAGE_06_NOVELTY_REKILL.md\` |
| Full-paper decision | \`docs/STAGE_075_FULL_THEORY_DECISION.md\` |
| Portability falsification | \`code/stage075a_portability_attacks.py\`; \`derivations/stage075a_portability_falsification.md\` |
| Contribution robustness | \`theorem_certificates/STAGE_075A_CONTRIBUTION_ROBUSTNESS.md\` |
| Formal claim map | \`theorem_certificates/FORMAL_VERIFICATION_CERTIFICATE.md\` |
| Canonical theory freeze | \`docs/STAGE_08_CANONICAL_THEORY_FREEZE.md\` |

## Formal verification status

GitHub Actions run #71:
- mathematical regressions: PASS;
- Lean build: PASS;
- axiom audit: PASS;
- placeholder audit: PASS.

Formal coverage is restricted to the proof-critical algebraic core.

## Source evidence

Complete inspected source: Boston Fed WP 12-4.  
VOR lineage/metadata: verified.  
VOR equation-level body: **not directly verified**.

## Current maturity

Independent reproduction: COMPLETE.  
Mathematical certification: COMPLETE at frozen scope.  
Portability classification: COMPLETE.  
Theory freeze: COMPLETE.  
Manuscript/reproducibility stages: NEXT.
