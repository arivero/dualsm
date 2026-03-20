---
phase: 05-extensions
plan: 01
depth: full
one-liner: "Wrote Lecture 9 surveying the SUSY duality landscape: KS (k=1 limit recovers Seiberg), SO/Sp with anomaly matching verified, s-confinement classification, cascade mechanism, and master comparison table"
subsystem: formalism
tags: [susy-duality, kutasov-schwimmer, so-sp-duality, s-confinement, anomaly-matching, quiver-gauge-theory]

requires:
  - phase: 02-susy-and-seiberg-duality
    provides: Seiberg duality for SU(N_c) SQCD (Lecture 3)
  - phase: 04-the-dualised-standard-model
    provides: Dualised SM framework (Lectures 7-8)
provides:
  - Lecture 9 lecture notes covering KS, SO, Sp, s-confining, product group, and cascade dualities
  - Master comparison table of all N=1 SUSY dualities (Table 2)
  - SO(N_c) SU(N_f)^2 U(1)_R anomaly matching verification
  - Sp(N_c) SU(2N_f)^2 U(1)_R anomaly matching verification
  - KS k=1 limit reducing to Seiberg duality (5-step explicit verification)
  - s-confining theories classification table (Csaki-Schmaltz-Skiba)
  - Connection to dualised SM programme identifying KS duality as most relevant
affects: [05-02, 05-03]

methods:
  added: [anomaly-matching-SO-Sp, kutasov-schwimmer-duality, quiver-mutation]
  patterns: [anomaly-SU(N_f)^2-U(1)_R-for-real-gauge-groups, dual-coxeter-number-in-conformal-window]

key-files:
  created:
    - lectures/lecture-09.tex

key-decisions:
  - "Checked SU(N_f)^2 U(1)_R mixed anomaly (not pure SU(N_f)^3 cubic) for SO/Sp -- cleaner for real/pseudo-real representations"
  - "Used Intriligator-Seiberg Sp convention (rank N_c, fund dim 2N_c) throughout"
  - "Kept cascade section at executive-summary level (~1.5 pages) as planned"

patterns-established:
  - "SO/Sp anomaly matching: use SU(N_f)^2 U(1)_R with T(sym) = (N_f+2)/2 for SO meson, T(antisym) = (2N_f-2)/2 for Sp meson"
  - "Conformal window formula: 3h/2 < N_f < 3h with h = dual Coxeter number"

conventions:
  - "hbar = 1, c = 1"
  - "metric = (+,-,-,-)"
  - "T(fund SU(N)) = 1/2"
  - "T(vector SO(N)) = 1"
  - "T(fund Sp(N)) = 1/2"
  - "Sp(N_c) = rank N_c, fund dim 2N_c"
  - "R[Q] = 1 - h/N_f (general formula using dual Coxeter number)"

plan_contract_ref: ".gpd/phases/05-extensions/05-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-ks-duality:
      status: passed
      summary: "KS duality presented with correct dual gauge group SU(kN_f - N_c), k meson species M_j = Q Phi^j Q-tilde, and explicit 5-step verification that k=1 recovers Seiberg duality"
      linked_ids: [deliv-lecture-09, test-ks-reduces-to-seiberg, ref-ks-9505004, ref-seiberg-9411149]
    claim-so-sp-dualities:
      status: passed
      summary: "SO(N_c) duality SO(N_f-N_c+4) and Sp(N_c) duality Sp(N_f-N_c-2) presented with SU(N_f)^2 U(1)_R anomaly verified analytically and numerically for each"
      linked_ids: [deliv-lecture-09, test-so-anomaly, test-sp-anomaly, ref-is-9506101, ref-is-9509066]
    claim-landscape-completeness:
      status: passed
      summary: "Lecture covers all 6 duality types (Seiberg, KS, SO, Sp, s-confining, cascade) with master comparison table, product group/quiver section, and explicit connection to dualised SM programme"
      linked_ids: [deliv-lecture-09, test-comparison-table, test-dsm-connection, ref-css-9612207, ref-ks-0007191, ref-peskin-9702094]
  deliverables:
    deliv-lecture-09:
      status: passed
      path: "lectures/lecture-09.tex"
      summary: "18-page lecture with 8 sections, 11 bibliography entries, convention box, quiver diagram, two anomaly matching verifications, s-confinement table, and master comparison table"
      linked_ids: [claim-ks-duality, claim-so-sp-dualities, claim-landscape-completeness]
  acceptance_tests:
    test-ks-reduces-to-seiberg:
      status: passed
      summary: "Section 2.3 shows 5-step explicit verification: k=1 gives W=Tr(Phi^2)/2 mass term, dual group SU(N_f-N_c), single meson M_0=QQ-tilde, standard magnetic superpotential, and conformal window 3N_c/2 < N_f < 3N_c"
      linked_ids: [claim-ks-duality, deliv-lecture-09, ref-ks-9505004, ref-seiberg-9411149]
    test-so-anomaly:
      status: passed
      summary: "Section 3.4 computes SU(N_f)^2 U(1)_R anomaly: electric = -N_c(N_c-2)/(2N_f), magnetic = same after expanding (N_f-N_c+4)(N_f-N_c+2) and (N_f+2)(N_f-2N_c+4) terms. Numerical check: SO(10) with N_f=14 gives -20/7 on both sides."
      linked_ids: [claim-so-sp-dualities, deliv-lecture-09, ref-is-9506101]
    test-sp-anomaly:
      status: passed
      summary: "Section 4.4 computes SU(2N_f)^2 U(1)_R anomaly: electric = -N_c(N_c+1)/N_f, magnetic = same after algebra with a=N_f-N_c substitution. Numerical check: Sp(2) with N_f=5 gives -6/5 on both sides."
      linked_ids: [claim-so-sp-dualities, deliv-lecture-09, ref-is-9506101, ref-is-9509066]
    test-comparison-table:
      status: passed
      summary: "Table 2 (master comparison) has 6 rows: Seiberg SU, KS SU+adj, SO, Sp, s-confining, Cascade. Columns: Duality, Electric, Magnetic, Mesons, Conformal Window, Key Feature."
      linked_ids: [claim-landscape-completeness, deliv-lecture-09]
    test-dsm-connection:
      status: passed
      summary: "Section 8.3 explicitly connects landscape to dualised SM: identifies KS duality with adjoint as most relevant, discusses Pati-Salam embedding, product group structure, cites Lectures 7-8 and CacciapagliaSannino2024 (2407.17281)"
      linked_ids: [claim-landscape-completeness, deliv-lecture-09, ref-ks-9505004]
  references:
    ref-seiberg-9411149:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as ground truth for SU(N_c) duality in Sections 1, 2, bibliography"
    ref-ks-9505004:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Section 2 (KS duality definition) and Section 8 (DSM connection)"
    ref-is-9506101:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Sections 3 and 4 for SO and Sp duality definitions, anomaly matching source"
    ref-is-9509066:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in convention box and throughout for Dynkin index conventions and comprehensive review"
    ref-css-9612207:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Section 5 for s-confining classification, Table 1 adapted from this reference"
    ref-ks-0007191:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Section 7 for duality cascade mechanism"
    ref-peskin-9702094:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Section 1 as pedagogical model for lecture organisation"
  forbidden_proxies:
    fp-rederive-all:
      status: rejected
      notes: "Each duality is stated with its result and one anomaly coefficient verified, not re-derived from scratch. The pedagogical point is the landscape, not the derivation."
    fp-no-anomaly-check:
      status: rejected
      notes: "SO anomaly matching verified in Section 3.4 (SU(N_f)^2 U(1)_R). Sp anomaly matching verified in Section 4.4 (SU(2N_f)^2 U(1)_R). Both include analytical proof and numerical check."
  uncertainty_markers:
    weakest_anchors:
      - "Duality cascade section is at executive-summary level -- Klebanov-Strassler requires AdS/CFT context not developed in these notes"
      - "Product group dualities described schematically (quiver mutation) without full field content specification"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: test-ks-reduces-to-seiberg
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-seiberg-9411149
    comparison_kind: benchmark
    metric: exact_match
    threshold: "k=1 KS must reproduce Seiberg duality exactly"
    verdict: pass
    recommended_action: "None -- verification complete"
    notes: "All 5 steps of the k=1 limit match: gauge group, meson content, superpotential, conformal window"
  - subject_id: test-so-anomaly
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-is-9506101
    comparison_kind: benchmark
    metric: exact_match
    threshold: "Electric = magnetic SU(N_f)^2 U(1)_R anomaly as polynomial identity in N_c, N_f"
    verdict: pass
    recommended_action: "None -- anomaly matching verified analytically and numerically"
    notes: "Both sides give -N_c(N_c-2)/(2N_f). Numerical check: SO(10), N_f=14 gives -20/7."
  - subject_id: test-sp-anomaly
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-is-9506101
    comparison_kind: benchmark
    metric: exact_match
    threshold: "Electric = magnetic SU(2N_f)^2 U(1)_R anomaly as polynomial identity in N_c, N_f"
    verdict: pass
    recommended_action: "None -- anomaly matching verified analytically and numerically"
    notes: "Both sides give -N_c(N_c+1)/N_f. Numerical check: Sp(2), N_f=5 gives -6/5."

duration: 25min
completed: 2026-03-20
---

# Phase 05 Plan 01: Lecture 9 -- The Landscape of SUSY Dualities Summary

**Wrote Lecture 9 surveying the SUSY duality landscape: KS duality with k=1 limit recovering Seiberg duality, SO/Sp dualities with anomaly matching verified analytically and numerically, s-confinement classification, duality cascade, and master comparison table connecting the landscape to the dualised SM.**

## Performance

- **Duration:** 25 min
- **Started:** 2026-03-20
- **Completed:** 2026-03-20
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- KS duality at k=1 reduces exactly to Seiberg duality: SU(1*N_f - N_c) = SU(N_f - N_c), single meson M_0 = Q Q-tilde, standard superpotential [CONFIDENCE: HIGH]
- SO(N_c) SU(N_f)^2 U(1)_R anomaly: electric = magnetic = -N_c(N_c-2)/(2N_f) [CONFIDENCE: HIGH]
- Sp(N_c) SU(2N_f)^2 U(1)_R anomaly: electric = magnetic = -N_c(N_c+1)/N_f [CONFIDENCE: HIGH]
- Master comparison table with 6 duality types covering the full N=1 SUSY landscape [CONFIDENCE: HIGH]

## Task Commits

Each task was committed atomically:

1. **Task 1: Write Lecture 9 Sections 1-8** - `154bfc7` (docs: all 8 sections including KS, SO, Sp dualities, s-confinement, product groups, cascade, synthesis)
2. **Task 2: Verification and compilation** - `10e122a` (docs: add Peskin citation, verify compilation and content)

## Files Created/Modified

- `lectures/lecture-09.tex` - Lecture 9: The Landscape of SUSY Dualities (18 pages, 1316 lines, 11 bibliography entries)

## Next Phase Readiness

- Lecture 9 complete and ready for Lecture 10 (physical mesons as dual mesons, Plan 05-02)
- KS duality with adjoint matter identified as most relevant for dualised SM, providing the bridge to Lecture 10
- Convention box establishes SO/Sp conventions that may be referenced in future work

## Contract Coverage

- Claim IDs advanced: claim-ks-duality -> passed, claim-so-sp-dualities -> passed, claim-landscape-completeness -> passed
- Deliverable IDs produced: deliv-lecture-09 -> lectures/lecture-09.tex (passed)
- Acceptance test IDs run: test-ks-reduces-to-seiberg -> passed, test-so-anomaly -> passed, test-sp-anomaly -> passed, test-comparison-table -> passed, test-dsm-connection -> passed
- Reference IDs surfaced: all 7 must-surface references cited (ref-seiberg-9411149, ref-ks-9505004, ref-is-9506101, ref-is-9509066, ref-css-9612207, ref-ks-0007191, ref-peskin-9702094)
- Forbidden proxies rejected: fp-rederive-all (stated results with one anomaly check each), fp-no-anomaly-check (SO and Sp both verified)
- Decisive comparison verdicts: test-ks-reduces-to-seiberg -> pass, test-so-anomaly -> pass, test-sp-anomaly -> pass

## Equations Derived

**Eq. (05.1): KS conformal window**

$$\frac{3N_c}{k+1} < N_f < \frac{3N_c}{k}$$

**Eq. (05.2): SO(N_c) dual gauge group**

$$\text{SO}(N_f - N_c + 4)$$

**Eq. (05.3): Sp(N_c) dual gauge group**

$$\text{Sp}(N_f - N_c - 2)$$

**Eq. (05.4): SO(N_c) SU(N_f)^2 U(1)_R anomaly**

$$\mathcal{A}^{\text{el}} = -\frac{N_c(N_c-2)}{2N_f} = \mathcal{A}^{\text{mag}}$$

**Eq. (05.5): Sp(N_c) SU(2N_f)^2 U(1)_R anomaly**

$$\mathcal{A}^{\text{el}} = -\frac{N_c(N_c+1)}{N_f} = \mathcal{A}^{\text{mag}}$$

## Validations Completed

- KS k=1 limit: 5-step explicit verification (gauge group, meson content, superpotential, conformal window) all match Seiberg duality from Lecture 3
- SO(N_c) anomaly matching: analytical proof as polynomial identity in N_c, N_f; numerical check SO(10), N_f=14: both sides = -20/7
- Sp(N_c) anomaly matching: analytical proof as polynomial identity in N_c, N_f; numerical check Sp(2), N_f=5: both sides = -6/5
- Convention consistency: ASSERT_CONVENTION line matches preamble.tex exactly
- Sp(1) = SU(2) consistency check stated in convention warning box
- SO conformal window: SO(10) gives 12 < N_f < 24 (consistent with IS)
- Sp conformal window: Sp(2) gives 4.5 < N_f < 9 (consistent with IS)
- LaTeX compilation: 0 errors, 0 undefined references
- All 11 bibliography entries resolve; all 10 citation keys have matching bibitems (Peskin1997 now cited)

## Decisions & Deviations

**Decisions:**
- Used SU(N_f)^2 U(1)_R mixed anomaly (not pure SU(N_f)^3 cubic) for SO and Sp anomaly matching. Rationale: the mixed anomaly gives a cleaner calculation for real/pseudo-real representations. The pure cubic anomaly SU(N_f)^3 also matches but requires more careful bookkeeping of the meson representation.
- Wrote all 8 sections in a single pass rather than splitting Task 1 (Sections 1-5) and Task 2 (Sections 6-8). Rationale: writing coherently ensures consistent cross-referencing and avoids artificial breaks in the narrative.
- Kept the cascade section at ~1.5 pages (executive summary level) as planned, explicitly stating that the geometric AdS/CFT picture is beyond the scope.

**Deviations:** None -- plan executed as specified.

## Open Questions

- Which specific Kutasov-Schwimmer theory (values of k, N_c, N_f) is most relevant for the dualised SM Pati-Salam embedding? (To be addressed in Lecture 10)
- Product group dualities could be expanded with explicit field content tables for the SU(3)xSU(2)xU(1) quiver -- deferred to keep Lecture 9 at survey level

## Self-Check: PASSED

- [x] lectures/lecture-09.tex exists (1316 lines)
- [x] Commit 154bfc7 found in git log
- [x] Commit 10e122a found in git log
- [x] ASSERT_CONVENTION matches preamble.tex
- [x] All 7 must-surface references cited
- [x] Master comparison table has 6 rows
- [x] KS k=1 limit explicit in Section 2.3
- [x] SO anomaly matching in Section 3.4
- [x] Sp anomaly matching in Section 4.4
- [x] Convention box with Sp naming warning present
- [x] LaTeX compilation clean

---

_Phase: 05-extensions_
_Completed: 2026-03-20_
