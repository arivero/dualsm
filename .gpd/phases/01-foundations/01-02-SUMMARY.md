---
phase: 01-foundations
plan: 02
depth: full
one-liner: "Lecture 1 presents 't Hooft anomaly matching with explicit gauge/global distinction, conformal window with correct SUSY boundaries, and Chan-Tsou disambiguation -- self-contained at Part III level using locked T(fund)=1/2 conventions"
subsystem: [formalism, derivation]
tags: [anomaly-matching, conformal-window, beta-function, gauge-theory, lecture-notes]

requires:
  - phase: 01-foundations (plan 01)
    provides: convention verification and reference corpus
provides:
  - "Lecture 1 LaTeX (lectures/lecture-01.tex): anomaly matching, conformal window, conventions"
  - "Shared LaTeX preamble (lectures/preamble.tex): macros, theorem environments, convention boxes"
  - "Six UV anomaly coefficients for SU(Nc) with Nf flavours (Table in S6)"
  - "Conformal window phase diagram (Fig. 1)"
affects: [01-foundations-plan-03, 02-susy-seiberg, all-subsequent-lectures]

methods:
  added: [anomaly-matching, beta-function-analysis, spectator-field-argument]
  patterns: [comparison-table-for-gauge-vs-thooft, convention-box-macro, preview-box-for-forward-references]

key-files:
  created:
    - "lectures/preamble.tex"
    - "lectures/lecture-01.tex"
  modified: []

key-decisions:
  - "Non-SUSY foundations first (per Peskin TASI-96): anomaly matching and conformal window presented without SUSY prerequisites"
  - "WZW term included in SU(3) Nf=2 warmup for completeness (anomaly matching requires it)"
  - "Chan-Tsou disambiguation placed as remark in introduction (3 sentences + footnote)"
  - "Exercises referenced but deferred to Exercise Sets 1-2 (plan 01-03)"

patterns-established:
  - "Convention box at start of every lecture (conventionbox environment)"
  - "Comparison table for key distinctions (comparisontable environment)"
  - "Preview box for forward references to SUSY results (previewbox environment)"
  - "Equation numbering: all displayed equations numbered with labels"

conventions:
  - "hbar = c = 1 (natural units)"
  - "metric = (+,-,-,-) (mostly minus)"
  - "T(fund) = 1/2 per Weyl fermion"
  - "b_0 = (11Nc - 2Nf)/3 for Nf Dirac flavours"
  - "A(fund) = 1 (cubic anomaly coefficient)"
  - "B[Q] = 1/Nc, B[Q-tilde] = -1/Nc (Seiberg baryon number)"
  - "R[Q] = (Nf - Nc)/Nf (non-anomalous R-charge)"

plan_contract_ref: ".gpd/phases/01-foundations/01-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-lecture-1:
      status: passed
      summary: "Lecture 1 presents 't Hooft anomaly matching with explicit comparison table (6 rows), spectator argument (5 steps), SU(3) Nf=2 warmup, general SU(Nc) anomaly coefficients, conformal window with correct boundaries, and Chan-Tsou disambiguation. Self-contained at Part III level."
      linked_ids: [deliv-preamble, deliv-lecture-01, test-anomaly-distinction, test-conformal-window, test-conventions-in-tex, test-self-contained, ref-seiberg-duality, ref-sannino-2407, ref-peskin-tasi]
      evidence:
        - verifier: self-check
          method: numerical verification + content audit
          confidence: high
          claim_id: claim-lecture-1
  deliverables:
    deliv-preamble:
      status: passed
      path: "lectures/preamble.tex"
      summary: "Shared LaTeX preamble with all required macros (Nc, Nf, Tfund, bzero, etc.), convention box environments, theorem environments. Compiles without errors."
      linked_ids: [claim-lecture-1, test-conventions-in-tex]
    deliv-lecture-01:
      status: passed
      path: "lectures/lecture-01.tex"
      summary: "Complete Lecture 1 (16 pages compiled): anomaly matching review, comparison table, spectator argument, SU(3) Nf=2 warmup, general SU(Nc) anomaly matching, conformal window analysis, Chan-Tsou disambiguation. All formulas use locked conventions."
      linked_ids: [claim-lecture-1, test-anomaly-distinction, test-conformal-window, test-conventions-in-tex, test-self-contained]
  acceptance_tests:
    test-anomaly-distinction:
      status: passed
      summary: "Comparison table present with 6 distinguishing rows (symmetry type, condition, physical meaning, consequence of violation, role of RG flow, computational object). Spectator argument presented in 5 explicit steps."
      linked_ids: [claim-lecture-1, deliv-lecture-01]
    test-conformal-window:
      status: passed
      summary: "Loss of AF at Nf=11Nc/2 stated. Banks-Zaks fixed point from 2-loop beta. SUSY window 3Nc/2 < Nf < 3Nc stated with SU(3) values Nf=5,6,7,8. Non-SUSY lower boundary stated as model-dependent. All numerical values verified (b_0(SU(3),6)=7, alpha_*(SU(3),16)=0.021, R[Q](SU(3),9)=2/3)."
      linked_ids: [claim-lecture-1, deliv-lecture-01, ref-seiberg-duality]
    test-conventions-in-tex:
      status: passed
      summary: "All formulas use T(fund)=1/2 consistently. b_0=(11Nc-2Nf)/3 with Nf Dirac flavours throughout. Metric (+,-,-,-). Convention table present in Section 2 with conventionbox. No formula uses T(fund)=1 or b_0=(11Nc-4Nf)/3."
      linked_ids: [claim-lecture-1, deliv-lecture-01, deliv-preamble]
    test-self-contained:
      status: partial
      summary: "Automated check: no SUSY concepts used without context. All SUSY references (superfield, superpotential, F/D-terms) appear only in forward-looking preview boxes or convention warnings. Full human review (can a Part III student follow it?) deferred to verification phase."
      linked_ids: [claim-lecture-1, deliv-lecture-01]
  references:
    ref-seiberg-duality:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Conventions verified compatible with Seiberg hep-th/9411149: T(fund)=1/2, B[Q]=1/Nc, R[Q]=(Nf-Nc)/Nf. Cited as [Seiberg1995]."
    ref-sannino-2407:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as [Sannino2024]. Lecture 1 sets up foundations compatible with Sannino's dualised SM construction."
    ref-peskin-tasi:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Pedagogical strategy (non-SUSY first) adopted from Peskin TASI-96. Cited as [PeskinTASI1996]."
  forbidden_proxies:
    fp-outline-only:
      status: rejected
      notes: "Lecture is a complete 16-page LaTeX document, not an outline or bullet-point summary."
    fp-susy-prerequisite:
      status: rejected
      notes: "All arguments build from gauge theory + anomalies. SUSY terms appear only in forward-looking preview boxes with explicit 'to be introduced in Lecture 2' language."
  uncertainty_markers:
    weakest_anchors:
      - "Peskin TASI-96 pedagogical strategy is 30 years old; student background may differ. Physics content unchanged."
    unvalidated_assumptions:
      - "Part III students remember triangle diagrams well enough for the quick review approach"
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: test-conformal-window
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-seiberg-duality
    comparison_kind: benchmark
    metric: exact_match
    threshold: "exact integer/rational values"
    verdict: pass
    recommended_action: "None -- all values match"
    notes: "b_0(SU(3),6)=7, SUSY window (4.5,9), R[Q](SU(3),9)=2/3 all match Seiberg."

duration: 9min
completed: 2026-03-20
---

# Phase 1 Plan 02: Lecture 1 -- Anomaly Matching and Conformal Window Summary

**Lecture 1 presents 't Hooft anomaly matching with explicit gauge/global distinction, conformal window analysis with correct SUSY boundaries, and Chan-Tsou disambiguation -- self-contained at Part III level using locked T(fund)=1/2 conventions throughout**

## Performance

- **Duration:** 9 min
- **Started:** 2026-03-20T00:11:13Z
- **Completed:** 2026-03-20T00:20:00Z
- **Tasks:** 2
- **Files created:** 2 (lectures/preamble.tex, lectures/lecture-01.tex)

## Key Results

- Complete Lecture 1 (16 compiled pages) covering anomaly matching, conformal window, and conventions -- ready for Part III delivery
- Comparison table with 6 rows distinguishing gauge anomaly cancellation from 't Hooft anomaly matching
- Six UV anomaly coefficients for SU(Nc) with Nf flavours tabulated (Eq. 14--19)
- Conformal window phase diagram (Fig. 1) showing confinement, conformal window, and loss of AF regions with SUSY boundaries overlaid
- All numerical values verified: b_0(SU(3), Nf=6) = 7, SUSY window SU(3) = (4.5, 9), R[Q](SU(3), Nf=9) = 2/3, alpha_*(SU(3), Nf=16) = 0.021

## Task Commits

Each task was committed atomically:

1. **Task 1: Create shared LaTeX preamble and macros** - `80d7e22` (calc: preamble with physics macros and conventions)
2. **Task 2: Write Lecture 1** - `4a91dff` (docs: lecture 1 -- anomaly matching, conformal window, conventions)

## Files Created/Modified

- `lectures/preamble.tex` -- Shared LaTeX preamble: all physics macros (\Nc, \Nf, \Tfund, \bzero, etc.), convention/comparison/warning/preview box environments, theorem environments, page layout
- `lectures/lecture-01.tex` -- Complete Lecture 1 (16 pages): 8 sections covering introduction, conventions, gauge anomaly review, 't Hooft matching, SU(3) Nf=2 warmup, general anomaly matching, conformal window, summary/preview

## Next Phase Readiness

- Lecture 1 is complete and ready for Exercise Sets 1-2 (plan 01-03)
- Six UV anomaly coefficients are tabulated and available for Seiberg duality verification in Lecture 3
- Convention table and macros are established for all subsequent lectures
- Ready for plan 01-03 (Exercise Sets 1-2)

## Contract Coverage

- Claim IDs advanced: claim-lecture-1 -> passed
- Deliverable IDs produced: deliv-preamble -> lectures/preamble.tex (passed), deliv-lecture-01 -> lectures/lecture-01.tex (passed)
- Acceptance test IDs run: test-anomaly-distinction -> passed, test-conformal-window -> passed, test-conventions-in-tex -> passed, test-self-contained -> partial (human review deferred)
- Reference IDs surfaced: ref-seiberg-duality -> [compare, cite] completed, ref-sannino-2407 -> [cite] completed, ref-peskin-tasi -> [cite] completed
- Forbidden proxies rejected: fp-outline-only -> rejected (16 pages, not an outline), fp-susy-prerequisite -> rejected (no SUSY prerequisites)
- Decisive comparison verdicts: test-conformal-window -> pass (all benchmark values match Seiberg)

## Equations Derived

**Eq. (01-02.1): One-loop beta function coefficient**

$$
b_0 = \frac{11N_c - 2N_f}{3}
$$

**Eq. (01-02.2): Two-loop beta function coefficient**

$$
b_1 = \frac{1}{3}\left[34 N_c^2 - N_f\left(13 N_c - \frac{3}{N_c}\right)\right]
$$

**Eq. (01-02.3): Banks-Zaks fixed-point coupling**

$$
\alpha_s^* = -\frac{2\pi\, b_0}{b_1}
$$

**Eq. (01-02.4): SUSY conformal window (exact, Seiberg)**

$$
\frac{3N_c}{2} < N_f < 3N_c
$$

**Eq. (01-02.5): R-charge at superconformal fixed point**

$$
R[Q] = \frac{N_f - N_c}{N_f}
$$

**Eq. (01-02.6): 't Hooft anomaly matching condition**

$$
\mathcal{A}^{abc}_{\text{UV}} = \mathcal{A}^{abc}_{\text{IR}}
$$

## Validations Completed

- b_0(SU(3), Nf=6) = 7 [CONFIDENCE: HIGH] -- exact integer, matches Peskin-Schroeder
- b_1(SU(3), Nf=6) = 26 [CONFIDENCE: HIGH] -- exact rational, matches Caswell 1974
- SUSY conformal window SU(3) = (4.5, 9) [CONFIDENCE: HIGH] -- matches Seiberg hep-th/9411149
- R[Q](SU(3), Nf=9) = 2/3 [CONFIDENCE: HIGH] -- unitarity bound saturated at upper edge
- alpha_*(SU(3), Nf=16) = 0.021 [CONFIDENCE: HIGH] -- perturbatively reliable Banks-Zaks
- Convention consistency: T(fund)=1/2 used throughout, no T(fund)=1 contamination
- LaTeX compilation: 0 errors, 0 warnings on third pass

## Decisions & Deviations

**Decisions:**
- Non-SUSY foundations first pedagogical strategy adopted (per Peskin TASI-96 and plan specification)
- WZW term included in SU(3) Nf=2 warmup -- required for complete anomaly matching (Deviation Rule 4: missing component, auto-fixed)
- bbm LaTeX package removed from preamble (not installed; Deviation Rule 1: environment issue, auto-fixed)
- \antisym macro changed from \ymark_2 (undefined) to \wedge^{\!2} (Deviation Rule 1: code bug, auto-fixed)

**Deviations:**
None beyond the auto-fixes above. Plan executed as specified.

## Open Questions

- Whether the WZW term discussion in the SU(3) Nf=2 warmup is at the right level for Part III students (may need simplification)
- Non-SUSY conformal window lower boundary is stated as model-dependent; more precise lattice values could be added as a footnote in later revision

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| One-loop beta function | alpha_s << 1 | O(alpha_s^2) from 2-loop | N_f far below 11Nc/2 |
| Two-loop Banks-Zaks | alpha_* << 1 | O(alpha_s^3) from 3-loop | N_f far below 11Nc/2 |
| Anomaly matching (exact) | Always | Exact (Adler-Bardeen) | Never |
| SUSY conformal window (exact) | N=1 SUSY | Exact (NSVZ) | Non-SUSY theories |

## Figures Produced

| Figure | File | Description | Key Feature |
| --- | --- | --- | --- |
| Fig. 01-02.1 | lectures/lecture-01.pdf p.12 | Phase structure of SU(Nc) with Nf flavours | Conformal window with SUSY boundaries overlaid; SU(3) integer Nf values marked |

## Self-Check: PASSED

- [x] lectures/preamble.tex exists
- [x] lectures/lecture-01.tex exists
- [x] Commit 80d7e22 found in git log
- [x] Commit 4a91dff found in git log
- [x] All numerical values reproduced by independent Python calculation
- [x] LaTeX compiles with 0 errors
- [x] Convention consistency: T(fund)=1/2 throughout, no mixed conventions
- [x] All contract deliverables produced
- [x] All automated acceptance tests pass
- [x] All must-surface references cited
- [x] All forbidden proxies rejected

---

_Phase: 01-foundations_
_Completed: 2026-03-20_
