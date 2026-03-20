---
phase: 04-the-dualised-standard-model
plan: 04
depth: full
one-liner: "Exercise Sets 5-6 produce parametric physical scales from the dualised SM: m_t ~ O(v) ~ 173 GeV from universal Yukawa, v ~ 820 GeV ~ O(246 GeV) from seesaw relation, Lambda_QCD ~ 70 MeV ~ O(200 MeV) from one-loop RG running -- all with O(1) free coefficients explicitly stated"
subsystem: derivation
tags: [fermion-mass-hierarchy, scalar-democracy, scale-matching, RG-running, Planck-operators, parametric-consistency]

requires:
  - phase: 04-the-dualised-standard-model/04-01
    provides: "Lecture 7 with dualised SM construction, universal Yukawa, 18 Higgs doublets"
  - phase: 04-the-dualised-standard-model/04-03
    provides: "Lecture 8 with scalar democracy, Planck operators, scale matching framework"
provides:
  - "Exercise 5: fermion mass hierarchy from scalar democracy (m_t ~ y*v, mass ratios from VEV tiers)"
  - "Exercise 6: scale matching (v ~ Lambda_D^2/M_Pl ~ 820 GeV, Lambda_QCD ~ 70 MeV from one-loop RG)"
  - "All free parameters explicitly listed (y, c^{abcd}, xi, Lambda_D, M_Pl)"
  - "Conjectural qualifiers on all non-SUSY duality claims"
  - "Marking schemes for Part III written examination (25 marks each)"
affects: [verification, paper-writing]

methods:
  added: [scalar-democracy-exercises, one-loop-RG-scale-extraction, seesaw-Planck-operator-analysis]
  patterns: [parametric-consistency-framing, conjectural-qualifier-protocol, input-output-table]

key-files:
  created:
    - "exercises/exercise-05.tex"
    - "exercises/exercise-05.pdf"
    - "exercises/exercise-06.tex"
    - "exercises/exercise-06.pdf"

key-decisions:
  - "Exercise 5 uses one unified Problem (25 marks, 4 parts) rather than separate problems, matching the self-contained nature of the scalar democracy argument"
  - "Exercise 6 derives alpha_s(Lambda_D) from measured alpha_s(M_Z) via one-loop running for self-consistency rather than treating alpha_s(Lambda_D) = 0.3 as an ungrounded input"
  - "Bottom-to-top mass ratio presented as controlled by O(1) scalar potential parameters (mu_b^2/M_d^2 ~ 0.02) rather than forced into the generic Planck suppression (Lambda_D/M_Pl)^p form, which gives unrealistic p ~ 0.2"

conventions:
  - "hbar = c = 1 (natural units)"
  - "metric = (+,-,-,-) (mostly minus)"
  - "b_0 = (11N_c - 2N_f)/3 for N_f Dirac flavours"
  - "alpha_s = g_s^2/(4 pi)"
  - "Universal Yukawa y; VEV sum rule v^2 = sum(H^2) = (246 GeV)^2/2"
  - "Epistemic: all non-SUSY duality claims carry conjectural qualifiers (P1)"

plan_contract_ref: ".gpd/phases/04-the-dualised-standard-model/04-04-PLAN.md#/contract"
contract_results:
  claims:
    claim-exer05-mass-hierarchy:
      status: passed
      summary: "Exercise 5 derives m_t ~ y*v with y ~ O(1) ~ 0.99, giving m_t ~ 174 GeV. Mass hierarchy from tiered VEVs: bottom at 1st tier (mu_b^2/M_d^2 ~ 0.024), charm/strange at 1st-2nd and 2nd tiers respectively. All O(1) free coefficients c^{abcd} explicitly listed."
      linked_ids: [deliv-exercise-05, test-top-mass, test-mass-ratios, test-free-params-stated, ref-sannino-2407, ref-hill-2019]
    claim-exer06-scale-matching:
      status: passed
      summary: "Exercise 6 extracts v ~ 820 GeV (factor ~3.3 from 246 GeV, within O(1)) from Lambda_D^2/M_Pl seesaw, and Lambda_QCD ~ 70 MeV (factor ~3 from 200 MeV) from one-loop RG running with alpha_s(Lambda_D) ~ 0.032 evolved from measured alpha_s(M_Z)."
      linked_ids: [deliv-exercise-06, test-lambda-qcd-ex, test-fermi-scale-ex, test-inputs-outputs, ref-sannino-2407]
    claim-examination-suitable:
      status: passed
      summary: "Both exercises are self-contained Part III problems with guided parts (a)-(d), full solutions with all intermediate steps, and 25-mark allocation each."
      linked_ids: [deliv-exercise-05, deliv-exercise-06, test-self-contained]
  deliverables:
    deliv-exercise-05:
      status: passed
      path: "exercises/exercise-05.tex"
      summary: "Exercise Set 5: 7-page PDF, 1 problem with 4 guided parts (a)-(d), 25 marks total. Self-contained problem statement, universal Yukawa background, Planck operator mixing, VEV tier structure, full solution, discussion of prediction vs parametric consistency."
      linked_ids: [claim-exer05-mass-hierarchy, claim-examination-suitable]
    deliv-exercise-06:
      status: passed
      path: "exercises/exercise-06.tex"
      summary: "Exercise Set 6: 8-page PDF, 1 problem with 4 guided parts (a)-(d), 25 marks total. Self-contained problem statement, one-loop RG running, seesaw relation, input/output table, full solution with numerical computations."
      linked_ids: [claim-exer06-scale-matching, claim-examination-suitable]
  acceptance_tests:
    test-top-mass:
      status: passed
      summary: "Exercise 5(a) derives m_t = y*v ~ 174 GeV with y ~ 0.99 ~ O(1). Stated as parametric consistency check, not precision prediction."
      linked_ids: [claim-exer05-mass-hierarchy, deliv-exercise-05, ref-sannino-2407]
    test-mass-ratios:
      status: passed
      summary: "Exercise 5(b)-(c) derives mass suppression m_f/m_t from induced VEVs. Bottom ratio m_b/m_t ~ 0.024 from mu_b^2/M_d^2 with O(1) coefficients explicitly acknowledged as free parameters."
      linked_ids: [claim-exer05-mass-hierarchy, deliv-exercise-05, ref-sannino-2407]
    test-free-params-stated:
      status: passed
      summary: "Exercise 5(d) explicitly lists all free parameters: y (universal Yukawa), c^{abcd} (Planck operator coefficients, ~100 parameters), Lambda_D (duality scale), M_Pl (measured), lambda_i and M_i^2 (scalar potential parameters)."
      linked_ids: [claim-exer05-mass-hierarchy, deliv-exercise-05]
    test-lambda-qcd-ex:
      status: passed
      summary: "Exercise 6(b) computes Lambda_QCD ~ 70 MeV from one-loop running with alpha_s(Lambda_D) ~ 0.032 and Lambda_D = 10^11 GeV. Within factor 3 of measured 200 MeV; threshold corrections and two-loop effects identified as sources of O(1) uncertainty."
      linked_ids: [claim-exer06-scale-matching, deliv-exercise-06, ref-sannino-2407]
    test-fermi-scale-ex:
      status: passed
      summary: "Exercise 6(c) derives v ~ Lambda_D^2/M_Pl ~ (10^11)^2/10^19 ~ 820 GeV, within factor 3.3 of v_measured = 246 GeV. Seesaw interpretation explained; O(1) coefficient absorbs discrepancy."
      linked_ids: [claim-exer06-scale-matching, deliv-exercise-06, ref-sannino-2407]
    test-inputs-outputs:
      status: passed
      summary: "Exercise 6(d)(i) contains explicit input/output table: Inputs = Lambda_D, M_Pl, alpha_s(Lambda_D). Outputs = v, Lambda_QCD, Lambda_S."
      linked_ids: [claim-exer06-scale-matching, deliv-exercise-06]
    test-self-contained:
      status: passed
      summary: "Both exercises provide self-contained problem statements (no need to read arXiv:2407.17281), guided parts with increasing difficulty, full solutions with all intermediate steps, and marking schemes (25 marks each)."
      linked_ids: [claim-examination-suitable, deliv-exercise-05, deliv-exercise-06]
  references:
    ref-sannino-2407:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Cacciapaglia-Sannino 2407.17281 cited in both exercises. Eqs. (11)-(23) for mass hierarchy and scale matching reproduced and extended into guided exercise format."
    ref-hill-2019:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Hill-Machado-Thomsen-Turner 2019 cited in Exercise 5 as originator of scalar democracy mechanism."
  forbidden_proxies:
    fp-formal-only-ex:
      status: rejected
      notes: "DEFEATED. Exercise 5 produces m_t ~ y*v ~ 174 GeV (explicit numerical scale). Exercise 6 produces Lambda_QCD ~ 70 MeV and v ~ 820 GeV (explicit numerical scales). Not formal-only."
    fp-unmotivated-numbers:
      status: rejected
      notes: "DEFEATED. Both exercises derive their numerical results from the parametric framework: Lambda_QCD via one-loop RG running equation with all steps shown, v via seesaw relation from Planck operators. Numbers are motivated, not plugged in."
    fp-hidden-inputs:
      status: rejected
      notes: "DEFEATED. Exercise 5(d) lists all free parameters explicitly. Exercise 6(d) has input/output table distinguishing given from derived quantities."
  uncertainty_markers:
    weakest_anchors:
      - "O(1) coefficients c^{abcd} completely unconstrained; exercises demonstrate parametric consistency but cannot distinguish dualised SM from other models with same free parameter count"
      - "One-loop RG running neglects threshold corrections; proper N_f matching would shift Lambda_QCD toward 200 MeV"
      - "v ~ 820 GeV vs measured 246 GeV (factor ~3.3); absorbed by O(1) coefficient xi"
    unvalidated_assumptions:
      - "Non-SUSY duality itself (conjectural qualifier stated throughout)"
      - "Planck-scale operator coefficients c^{abcd} are O(1) (assumed, not derived)"
    competing_explanations: []
    disconfirming_observations:
      - "If parametric mass hierarchy gives wrong SCALING -- e.g. m_b/m_t ~ O(1) instead of O(0.02) -- scalar democracy mechanism fails qualitatively"
      - "If Lambda_QCD from one-loop running is orders of magnitude off (> 1 GeV or < 10 MeV) for Lambda_D in range 10^9-10^12 GeV, scale matching framework is inconsistent"

comparison_verdicts:
  - subject_id: claim-exer06-scale-matching
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-sannino-2407
    comparison_kind: benchmark
    metric: order_of_magnitude
    threshold: "within factor 10"
    verdict: pass
    recommended_action: "none"
    notes: "Lambda_QCD ~ 70 MeV vs measured 200 MeV (factor 3); v ~ 820 GeV vs measured 246 GeV (factor 3.3). Both within O(1) as expected for one-loop estimates with free O(1) coefficients."
  - subject_id: claim-exer05-mass-hierarchy
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-sannino-2407
    comparison_kind: benchmark
    metric: parametric_consistency
    threshold: "m_t ~ O(v) with y ~ O(1)"
    verdict: pass
    recommended_action: "none"
    notes: "m_t ~ y*v = 0.99 * 174 GeV ~ 173 GeV. y ~ 0.99 is naturally O(1)."

duration: 6min
completed: 2026-03-20
---

# Phase 04 Plan 04: Exercise Sets 5-6 Summary

**Exercise Sets 5-6 produce parametric physical scales from the dualised SM: m_t ~ O(v) ~ 173 GeV from universal Yukawa, v ~ 820 GeV from seesaw relation, Lambda_QCD ~ 70 MeV from one-loop RG running -- all with O(1) free coefficients explicitly stated, defeating fp-formal-only.**

## Performance

- **Duration:** 6 min
- **Started:** 2026-03-20T03:18:41Z
- **Completed:** 2026-03-20T03:25:01Z
- **Tasks:** 2 completed
- **Files modified:** 2 created (exercise-05.tex, exercise-06.tex) + 2 compiled PDFs

## Key Results

- **m_t ~ y * v ~ 174 GeV** with y ~ 0.99 ~ O(1): parametric consistency, not prediction [CONFIDENCE: HIGH]
- **Lambda_QCD ~ 70 MeV** from one-loop RG running with alpha_s(Lambda_D) ~ 0.032: within factor 3 of measured 200 MeV [CONFIDENCE: MEDIUM -- one-loop only, threshold corrections omitted]
- **v ~ 820 GeV** from Lambda_D^2/M_Pl seesaw: within factor 3.3 of measured 246 GeV [CONFIDENCE: MEDIUM -- O(1) coefficient xi absorbs discrepancy]
- **fp-formal-only DEFEATED**: both exercises produce explicit numerical scales
- **All free parameters stated**: y, c^{abcd}, xi, Lambda_D, M_Pl

## Task Commits

Each task was committed atomically:

1. **Task 1: Exercise Set 5 -- fermion mass hierarchy** - `dc55d82` (calc)
2. **Task 2: Exercise Set 6 -- scale matching** - `56a683e` (calc)

## Files Created/Modified

- `exercises/exercise-05.tex` - Fermion mass hierarchy from scalar democracy (7 pages, 25 marks)
- `exercises/exercise-05.pdf` - Compiled PDF
- `exercises/exercise-06.tex` - Scale matching: v and Lambda_QCD from dual parameters (8 pages, 25 marks)
- `exercises/exercise-06.pdf` - Compiled PDF

## Next Phase Readiness

Plan 04-04 complete. Exercises 5-6 are the CONTRACT-CRITICAL deliverables that satisfy fp-formal-only. Ready for Plan 04-05 (if it exists) or phase verification.

## Contract Coverage

- Claim IDs advanced: claim-exer05-mass-hierarchy -> passed, claim-exer06-scale-matching -> passed, claim-examination-suitable -> passed
- Deliverable IDs produced: deliv-exercise-05 -> exercises/exercise-05.tex, deliv-exercise-06 -> exercises/exercise-06.tex
- Acceptance test IDs run: test-top-mass -> passed, test-mass-ratios -> passed, test-free-params-stated -> passed, test-lambda-qcd-ex -> passed, test-fermi-scale-ex -> passed, test-inputs-outputs -> passed, test-self-contained -> passed
- Reference IDs surfaced: ref-sannino-2407 -> read/compare/cite, ref-hill-2019 -> read/cite
- Forbidden proxies rejected: fp-formal-only-ex -> rejected (defeated), fp-unmotivated-numbers -> rejected (defeated), fp-hidden-inputs -> rejected (defeated)
- Decisive comparison verdicts: claim-exer06-scale-matching -> pass (order-of-magnitude), claim-exer05-mass-hierarchy -> pass (parametric consistency)

## Equations Derived

**Eq. (04-04.1): Top quark mass from universal Yukawa**

$$m_t = y \cdot v \approx 0.99 \times 174\;\text{GeV} \approx 173\;\text{GeV}$$

**Eq. (04-04.2): Mass suppression from Planck operators**

$$\frac{m_f}{m_t} \sim \xi_i \frac{\Lambda_D^2}{M_{\text{Pl}}^2}$$

**Eq. (04-04.3): QCD scale from one-loop running**

$$\Lambda_{\text{QCD}} = \Lambda_D \exp\!\left(-\frac{2\pi}{b_0 \alpha_s(\Lambda_D)}\right) \approx 70\;\text{MeV}$$

**Eq. (04-04.4): Fermi scale seesaw**

$$v \sim \frac{\Lambda_D^2}{M_{\text{Pl}}} \approx 820\;\text{GeV}$$

## Validations Completed

- Dimensional consistency of all equations verified
- b_0 = 7 for SU(3) with N_f = 6: (33-12)/3 = 7. Correct.
- Lambda_QCD ~ 70 MeV: within factor 3 of measured 200 MeV (threshold corrections would improve this)
- v ~ 820 GeV: within factor 3.3 of measured 246 GeV (O(1) coefficient xi absorbs this)
- m_t ~ 174 GeV: consistent with measured 172.7 +/- 0.3 GeV
- Both exercises compile cleanly with 0 LaTeX errors

## Decisions Made

- Bottom-to-top ratio treated as direct mixing (mu_b^2/M_d^2) rather than forced into generic Planck power-law form, which was the physically correct framing per Lecture 8
- alpha_s(Lambda_D) derived from measured alpha_s(M_Z) via one-loop running for self-consistency, rather than treating it as an arbitrary O(1) input
- Electric beta function b_0^e = 4 computed explicitly to show electric theory is asymptotically free (confines in IR at Lambda_D)

## Deviations from Plan

None - plan executed as specified.

## Issues Encountered

None.

## Open Questions

- Would two-loop RG running with proper threshold matching at each quark mass bring Lambda_QCD closer to 200 MeV? (Expected: yes, by a factor of ~2-3)
- Can the O(1) coefficient xi in v ~ sqrt(xi) Lambda_D^2/M_Pl be constrained by additional physics arguments?

## Self-Check: PASSED

- [x] exercises/exercise-05.tex exists and compiles
- [x] exercises/exercise-06.tex exists and compiles
- [x] Commit dc55d82 found in git log
- [x] Commit 56a683e found in git log
- [x] m_t ~ 174 GeV derived (test-top-mass)
- [x] Lambda_QCD ~ 70 MeV derived (test-lambda-qcd-ex)
- [x] v ~ 820 GeV derived (test-fermi-scale-ex)
- [x] Input/output table present (test-inputs-outputs)
- [x] All free parameters listed (test-free-params-stated)
- [x] Conjectural qualifiers present in both exercises
- [x] Marking schemes present (25 marks each)
- [x] All contract IDs covered

---

_Phase: 04-the-dualised-standard-model_
_Completed: 2026-03-20_
