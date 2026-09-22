# Shy–Stenbacka (2013) Customer Recognition Reassessment

## Target paper

Oz Shy and Rune Stenbacka (2013), “Investment in Customer Recognition and Information Exchange,” Information Economics and Policy 25(2), 92–106.

## Project purpose

Solve the kinked no-information price game globally, characterize the corrected price equilibrium across mismatch regimes, and propagate the correction through investment, sharing, switching, profit, consumer-surplus, and welfare results.

## Current status

**Stage 0 — Evidence Freeze / independent re-verification.**

No publication-facing correction theorem is frozen yet. The master audit findings are transferred only as hypotheses/evidence to be independently reconstructed in this repository.

## Starting evidence

- Master audit provenance: `ryotamatsuki/ozshypapers — audits/investment_customer_recognition_information_exchange_2013_final.md`
- Source status: Complete Boston Fed working-paper lineage inspected; VOR body still requires direct equation-level verification.
- Initial signal: The transferred audit found an open admissible parameter wedge in which Eq. (8) admits a profitable kink-crossing poaching-price deviation.

## Repository policy

1. Re-derive all publication-facing claims from the original model rather than copying the master-audit conclusion.
2. Separate source transcription, derivation, counterexample, corrected theorem, and downstream implications.
3. Treat local FOCs as insufficient when regime changes, clipping, entry/exit, or boundary actions are feasible.
4. Preserve exact equality and boundary cases in the equilibrium correspondence.
5. Numerical and symbolic checks support but do not replace analytical proof.
6. Do not draft a submission claim until the Version-of-Record lineage and prior-disclosure search are frozen.
7. Keep the master audit repository as provenance; this repository becomes canonical only for publication-facing development after Stage 0 passes.

## Planned structure

```text
README.md
PROJECT_STATUS.md
PROVENANCE.md
CLAIM_BOUNDARY.md
EVIDENCE_MAP.md
docs/
  STAGE_00_EVIDENCE_FREEZE.md
derivations/
code/
results/
sources/
manuscript/
submission/
```

## Immediate next step

Complete `docs/STAGE_00_EVIDENCE_FREEZE.md`: freeze the exact source/version, independently reproduce the transferred discrepancy, run a fresh prior-disclosure search, and decide whether the project passes into theorem/proposition development.

