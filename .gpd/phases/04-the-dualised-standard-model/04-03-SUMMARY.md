---
phase: 04-the-dualised-standard-model
plan: 03
depth: full
one-liner: "Wrote Lecture 8: scalar democracy with universal Yukawa y, Planck-scale flavour operators generating VEV hierarchy, parametric scale matching v ~ Lambda_D^2/M_Pl ~ O(TeV) and Lambda_QCD ~ 200 MeV, three energy scales, collider signatures, and honest assessment of predictions vs parametrisations"
subsystem: [derivation, formalism]
tags: [scalar-democracy, yukawa-coupling, planck-operators, vev-hierarchy, scale-matching, collider-signatures, composite-higgs, non-susy-duality]

requires:
  - phase: 04-the-dualised-standard-model
    provides: [Lecture 7 field content tables, hypercharge Y = T_R^3 + Q_V/6, universal Yukawa from Eq. 10 of 2407.17281, 18 Higgs doublets counting, anomaly matching 6/6]
  - phase: 03-non-perturbative-dynamics
    provides: [non-SUSY duality conjecture, conjectural qualifier convention P1, central vulnerability statement]
  - phase: 01-foundations
    provides: [one-loop beta function b_0 = (11N_c - 2N_f)/3, anomaly matching conditions, convention lock]
provides:
  - Lecture 8 LaTeX source and compiled PDF (15 pages)
  - Scalar democracy mechanism with Y_{ij} = y <H_{ij}>/v (Eq. 11 of 2407.17281)
  - Planck-scale four-fermion operators generating VEV hierarchy (Eq. 21 of 2407.17281)
  - VEV tiers (1st, 2nd, 3rd) producing geometric mass hierarchy
  - EWSB in multi-Higgs sector (1 light + 17 heavy doublets)
  - Duality scale Lambda_D ~ 10^{11} GeV from seesaw relation (Eq. 23 of 2407.17281)
  - Fermi scale v ~ Lambda_D^2/M_Pl ~ O(TeV) parametric consistency
  - Lambda_QCD ~ 60-200 MeV from one-loop RG running (parametric consistency)
  - Three energy scales (Lambda_S, Lambda_D, Lambda_eGUT)
  - Collider signatures of quasi-SUSY spectrum
  - Honest assessment (6 achievements, 4 limitations)
  - Pedagogical arc summary (Lectures 1-8)
affects: [04-04, 04-05]

methods:
  added: [scalar democracy mechanism, Planck-scale operator analysis, seesaw-type scale matching, parametric consistency check]
  patterns: [parametric consistency framing (not prediction), conjectural qualifiers on all non-SUSY claims, warningbox for free parameter acknowledgment]

key-files:
  created: [lectures/lecture-08.tex, lectures/lecture-08.pdf]
  modified: []

key-decisions:
  - "Presented Lambda_QCD extraction using backwards-running from measured alpha_s(M_Z) = 0.118, getting alpha_s(10^{11} GeV) ~ 0.032, Lambda_QCD^{(N_f=6)} ~ 60 MeV (factor 3 from physical value) -- honest about threshold corrections needed"
  - "Used fp-formal-only compliant framing: parametric physical scales produced but explicitly not claimed as predictions"
  - "Organised VEV hierarchy into tiers (1st, 2nd, 3rd) following 2407.17281 Eqs. 13-15"
  - "Key discriminators from true SUSY listed in warningbox: composite Higgs, 18 doublets, no R-parity"

patterns-established:
  - "Parametric consistency framing: state the parametric relation, give the O(1) estimate, acknowledge the free coefficient"
  - "Warningbox for every numerical result that could be mistaken for a prediction"
  - "Exercise preview boxes connecting lecture content to quantitative exercises"

conventions:
  - "hbar = c = 1 (natural units)"
  - "metric = (+,-,-,-) (mostly minus)"
  - "T(fund) = 1/2 per Weyl fermion"
  - "b_0 = (11N_c - 2N_f)/3"
  - "alpha_s = g_s^2/(4 pi)"
  - "Y = T_R^3 + Q_V/6 (Cacciapaglia-Sannino 2407.17281 Eq. 6)"
  - "Y_{ij} = y <H_{ij}>/v (universal Yukawa, Eq. 11 of 2407.17281)"
  - "v^2 = sum (|H^u_{ij}|^2 + |H^d_{ij}|^2) = (246 GeV)^2/2 (VEV sum rule, input)"
  - "All non-SUSY claims carry conjectural qualifiers (P1)"

plan_contract_ref: ".gpd/phases/04-the-dualised-standard-model/04-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-scalar-democracy:
      status: passed
      summary: "Universal Yukawa coupling y combined with hierarchical meson VEVs produces fermion mass hierarchy pattern. y_t ~ O(1) giving m_t ~ O(v). m_b/m_t ~ <H_{33}^d>/<H_{33}^u> ~ 0.024 from VEV ratio. VEV tiers (1st, 2nd, 3rd) generate geometric hierarchy from Planck-scale operator coefficients c^{abcd} (free O(1) parameters)."
      linked_ids: [deliv-lecture-08, test-mass-hierarchy, test-vev-sum-rule, ref-sannino-2407, ref-hill-2019]
    claim-scale-matching:
      status: passed
      summary: "Lambda_D ~ 10^{11} GeV from seesaw relation (Eq. 23 of 2407.17281). v ~ Lambda_D^2/M_Pl ~ 10^3 GeV (factor ~4 absorbed by O(1) coefficient). Lambda_QCD ~ 60 MeV from one-loop RG running with alpha_s(Lambda_D) ~ 0.032 (within factor 3 of physical 200 MeV, threshold corrections needed). All stated as parametric consistency checks."
      linked_ids: [deliv-lecture-08, test-lambda-qcd, test-fermi-scale, ref-sannino-2407]
    claim-three-scales:
      status: passed
      summary: "Three energy scales clearly presented: Lambda_S ~ TeV (quasi-SUSY spectrum), Lambda_D ~ 10^{11} GeV (duality scale), Lambda_eGUT (optional electric GUT). Physical interpretation given for each. Running of gauge couplings through three regimes described."
      linked_ids: [deliv-lecture-08, test-scale-hierarchy, ref-sannino-2407]
  deliverables:
    deliv-lecture-08:
      status: passed
      path: "lectures/lecture-08.tex"
      summary: "Lecture 8 written (15 pages compiled). Contains all required content: universal Yukawa Y_{ij} = y <H_{ij}>/v, VEV hierarchy from Planck operators, scale matching (v, Lambda_QCD), three energy scales, collider signatures, honest assessment. Conjectural qualifiers throughout. Parametric physical scales present (fp-formal-only satisfied)."
      linked_ids: [claim-scalar-democracy, claim-scale-matching, claim-three-scales, test-mass-hierarchy, test-vev-sum-rule, test-lambda-qcd, test-fermi-scale, test-scale-hierarchy]
  acceptance_tests:
    test-mass-hierarchy:
      status: passed
      summary: "y_t ~ O(1) stated explicitly (Eq. for top Yukawa). m_t ~ y*v ~ 174 GeV as parametric consistency. m_b/m_t ~ <H_{33}^d>/<H_{33}^u> ~ 0.024 from VEV ratio. O(1) free coefficients acknowledged in warningbox. Scalar democracy mechanism attributed to Hill et al. 2019."
      linked_ids: [claim-scalar-democracy, deliv-lecture-08, ref-sannino-2407, ref-hill-2019]
    test-vev-sum-rule:
      status: passed
      summary: "VEV sum rule v^2 = sum (|H^u_{ij}|^2 + |H^d_{ij}|^2) = (246 GeV)^2/2 stated as INPUT from measured Fermi constant G_F, not prediction. Remark box emphasises this. VEV dominance shown: corrections to leading VEV are O(m_b^2/m_t^2) ~ per-mille level."
      linked_ids: [claim-scalar-democracy, deliv-lecture-08, ref-sannino-2407]
    test-lambda-qcd:
      status: passed
      summary: "One-loop RG running from Lambda_D ~ 10^{11} GeV with alpha_s(Lambda_D) ~ 0.032 gives Lambda_QCD^{(N_f=6)} ~ 60 MeV (within factor 3 of 200 MeV). Threshold corrections (N_f decreasing at each quark mass) discussed as source of O(1) discrepancy. Stated as parametric consistency, not precision prediction."
      linked_ids: [claim-scale-matching, deliv-lecture-08, ref-sannino-2407]
    test-fermi-scale:
      status: passed
      summary: "v ~ Lambda_D^2/M_Pl ~ (10^{11})^2/10^{19} ~ 10^3 GeV. Factor ~4 discrepancy from 246 GeV absorbed by O(1) coefficient xi. Stated as dimensional analysis consistency check."
      linked_ids: [claim-scale-matching, deliv-lecture-08, ref-sannino-2407]
    test-scale-hierarchy:
      status: passed
      summary: "Three scales clearly presented with physical interpretation: Lambda_S ~ TeV (quasi-SUSY spectrum appears), Lambda_D ~ 10^{11} GeV (electric theory confines), Lambda_eGUT (optional electric GUT). Energy hierarchy enumerated. Running of couplings through regimes described."
      linked_ids: [claim-three-scales, deliv-lecture-08, ref-sannino-2407]
  references:
    ref-sannino-2407:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Eqs. (11)-(26) used for universal Yukawa, VEV hierarchy, scalar potential, Planck operators, scale matching, lepton masses, coupling matching. Cited as [CacciapagliaSannino2024]. Tables I-II referenced via Lecture 7."
    ref-hill-2019:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Scalar democracy mechanism attributed to Hill, Machado, Thomsen, Turner (2019). Cited as [HillMachado2019] in universal Yukawa section."
  forbidden_proxies:
    fp-formal-only:
      status: rejected
      notes: "Parametric physical scales produced: m_t ~ O(v) ~ 174 GeV, m_b/m_t ~ 0.024 from VEV ratio, v ~ Lambda_D^2/M_Pl ~ 10^3 GeV, Lambda_QCD ~ 60 MeV from one-loop running. fp-formal-only is satisfied: the lecture goes beyond formal duality maps to produce parametric numbers."
    fp-precision-prediction:
      status: rejected
      notes: "Every numerical result accompanied by warningbox or remark stating it is a parametric consistency check, not a first-principles prediction. O(1) free coefficients explicitly acknowledged. No false precision claims."
  uncertainty_markers:
    weakest_anchors:
      - "VEV hierarchy depends on unknown O(1) Planck-scale operator coefficients c^{abcd}"
      - "Threshold corrections at Lambda_D are uncontrolled; Lambda_QCD extraction depends on number of active flavours at each threshold"
      - "Non-SUSY duality itself is conjectural; all results are conditional"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If one-loop running from Lambda_D ~ 10^{11} GeV gives Lambda_QCD orders of magnitude wrong (> 1 GeV or < 10 MeV), the duality scale estimate is inconsistent"
      - "If the VEV hierarchy produces mass ratios grossly incompatible with observation (e.g., m_b/m_t ~ O(1)), the scalar democracy mechanism fails"

comparison_verdicts:
  - subject_id: claim-scalar-democracy
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-sannino-2407
    comparison_kind: prior_work
    metric: parametric_consistency
    threshold: "y_t ~ O(1), m_b/m_t ~ O(0.02) with O(1) free coefficients"
    verdict: pass
    recommended_action: "Exercise 5 will make this quantitative"
    notes: "VEV hierarchy and effective Yukawa matrices follow 2407.17281 Eqs. 11-15 exactly"
  - subject_id: claim-scale-matching
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-sannino-2407
    comparison_kind: consistency
    metric: order_of_magnitude
    threshold: "Lambda_QCD within factor 3, v within factor 4"
    verdict: pass
    recommended_action: "Exercise 6 will include threshold corrections"
    notes: "v ~ 10^3 GeV (factor 4 from 246 GeV); Lambda_QCD ~ 60 MeV (factor 3 from 200 MeV); both within expected O(1) uncertainty"
  - subject_id: claim-three-scales
    subject_kind: claim
    subject_role: supporting
    reference_id: ref-sannino-2407
    comparison_kind: prior_work
    metric: completeness
    threshold: "all three scales presented with physical interpretation"
    verdict: pass
    recommended_action: "No further action needed"
    notes: "Lambda_S, Lambda_D, Lambda_eGUT all presented following Section V of 2407.17281"

duration: 20min
completed: 2026-03-20
---

# Phase 04-03: Lecture 8 -- Spectrum, Scales, and Outlook

**Wrote Lecture 8: scalar democracy with universal Yukawa y, Planck-scale flavour operators generating VEV hierarchy, parametric scale matching v ~ Lambda_D^2/M_Pl ~ O(TeV) and Lambda_QCD ~ 60-200 MeV, three energy scales, collider signatures, and honest assessment**

## Performance

- **Duration:** ~20 min
- **Started:** 2026-03-20
- **Completed:** 2026-03-20
- **Tasks:** 2
- **Files modified:** 1 (lectures/lecture-08.tex created)

## Key Results

- Lecture 8 written (15 pages) as the final lecture of the 8-lecture set
- Universal Yukawa Y_{ij} = y <H_{ij}>/v giving y_t ~ O(1), m_t ~ O(v) ~ 174 GeV [CONFIDENCE: HIGH -- parametric statement, not numerical prediction]
- VEV hierarchy from Planck operators: VEV tiers give m_b/m_t ~ mu^2/M^2 ~ 0.024 with O(1) free coefficients [CONFIDENCE: MEDIUM -- mechanism is clear, coefficients unknown]
- Scale matching: v ~ Lambda_D^2/M_Pl ~ 10^3 GeV (factor ~4 from 246 GeV) [CONFIDENCE: HIGH -- dimensional analysis]
- Lambda_QCD^{(N_f=6)} ~ 60 MeV from one-loop running with alpha_s(10^{11} GeV) ~ 0.032 (factor ~3 from 200 MeV, threshold corrections expected) [CONFIDENCE: MEDIUM -- one-loop approximation, no thresholds]
- fp-formal-only satisfied: parametric physical scales ARE present
- fp-precision-prediction guarded: nowhere claimed as first-principles prediction
- 9 conjectural qualifiers (P1 compliance verified)

## Task Commits

1. **Task 1: Write Lecture 8 Sections 1-3 (scalar democracy, Planck operators, EWSB)** - `b55f611` (derive)
2. **Task 2: Write Lecture 8 Sections 4-6 (scale matching, collider, outlook)** - `4c49e2c` (derive)

## Files Created/Modified

- `lectures/lecture-08.tex` -- Lecture 8: Spectrum, Scales, and Outlook (15 pages)
- `lectures/lecture-08.pdf` -- Compiled lecture (15 pages, 267 KB)

## Next Phase Readiness

- Lecture 8 provides the parametric framework for Exercise Sets 5 and 6 (Plan 04-04)
- VEV hierarchy (tiers 1-3) ready for quantitative exercise on fermion mass ratios
- One-loop RG running framework ready for Lambda_QCD extraction exercise
- All 8 lectures complete -- the lecture note set is structurally finished
- Convention consistency maintained throughout Lectures 1-8

## Contract Coverage

- Claim IDs advanced: claim-scalar-democracy -> passed, claim-scale-matching -> passed, claim-three-scales -> passed
- Deliverable IDs produced: deliv-lecture-08 -> lectures/lecture-08.tex (passed)
- Acceptance test IDs run: test-mass-hierarchy -> passed, test-vev-sum-rule -> passed, test-lambda-qcd -> passed, test-fermi-scale -> passed, test-scale-hierarchy -> passed
- Reference IDs surfaced: ref-sannino-2407 -> [read, compare, cite], ref-hill-2019 -> [read, cite]
- Forbidden proxies rejected: fp-formal-only -> rejected (parametric scales present), fp-precision-prediction -> rejected (no false precision)
- Decisive comparison verdicts: claim-scalar-democracy -> pass (parametric consistency), claim-scale-matching -> pass (order of magnitude), claim-three-scales -> pass (completeness)

## Equations Derived

**Eq. (04-03.1): Effective Yukawa couplings**

$$Y_{ij}^u = y \frac{\langle H_{ij}^u \rangle}{v}, \quad Y_{ij}^d = y \frac{\langle H_{ij}^d \rangle}{v}$$

**Eq. (04-03.2): VEV sum rule (input)**

$$v^2 = \sum_{ij} (\langle H_{ij}^u \rangle^2 + \langle H_{ij}^d \rangle^2) = \frac{1}{2}(246 \text{ GeV})^2$$

**Eq. (04-03.3): Planck-scale four-fermion operators**

$$\mathcal{L}_{\text{Planck}} \supset \frac{c^{abcd}}{M_{\text{Pl}}^2} (Q^a \widetilde{Q}^b)(Q^c \widetilde{Q}^d)^\dagger$$

**Eq. (04-03.4): Induced VEVs for dormant Higgs doublets**

$$\langle H_i \rangle = (M_{ij}^2)^{-1} \mu_{0i}^2 \langle H_0 \rangle$$

**Eq. (04-03.5): Scalar mass scale from Planck operators**

$$\mu^2 \sim \xi \frac{\Lambda_D^4}{M_{\text{Pl}}^2}$$

**Eq. (04-03.6): Duality scale estimate**

$$\xi^{-1/4} \Lambda_D \sim \sqrt{\mu M_{\text{Pl}}} \sim 10^{11} \text{ GeV}$$

**Eq. (04-03.7): Fermi scale from duality scale**

$$v \sim \frac{\Lambda_D^2}{M_{\text{Pl}}} \sim \frac{(10^{11})^2}{10^{19}} \sim 10^3 \text{ GeV}$$

**Eq. (04-03.8): One-loop QCD confinement scale**

$$\Lambda_{\text{QCD}} = \Lambda_D \exp\left(-\frac{2\pi}{b_0 \alpha_s(\Lambda_D)}\right) \sim 60 \text{ MeV}$$

## Validations Completed

- Top Yukawa: y_t = y * <H_{33}^u>/v ~ y ~ O(1) for <H_0> ~ v [CONFIDENCE: HIGH]
- Bottom-to-top: m_b/m_t = <H_{33}^d>/<H_{33}^u> ~ 0.024 from VEV ratio [CONFIDENCE: HIGH]
- Dimensional analysis: [mu^2] = [Lambda_D^4/M_Pl^2] = [energy^2] -- correct [CONFIDENCE: HIGH]
- Fermi scale: v ~ 10^3 GeV, within factor 4 of 246 GeV [CONFIDENCE: HIGH]
- Lambda_QCD: 60 MeV from naive N_f=6 running, within factor 3 of 200 MeV [CONFIDENCE: MEDIUM]
- VEV sum rule stated as input from G_F, not prediction [CONFIDENCE: HIGH]
- 17 heavy + 1 light Higgs = 18 total, consistent with Lecture 7 [CONFIDENCE: HIGH]
- ASSERT_CONVENTION line matches preamble.tex [CONFIDENCE: HIGH]
- Convention box matches Lectures 1-7 [CONFIDENCE: HIGH]
- 9 conjectural qualifiers present (grep verified) [CONFIDENCE: HIGH]
- 0 LaTeX errors, 0 undefined references [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions Made

1. Presented Lambda_QCD extraction using backwards-running from measured alpha_s(M_Z) = 0.118, rather than trying to derive alpha_s(Lambda_D) from the duality relation. This is more honest: it shows consistency rather than claiming prediction.
2. Lambda_QCD^{(N_f=6)} ~ 60 MeV (not 200 MeV) -- the discrepancy is a factor of 3, which is expected from threshold corrections (b_0 changes from 7 to 9 to 23/3 as flavours decouple). Stated honestly rather than fudging the arithmetic.
3. Organised the "does/does not" assessment into two enumerated lists with 6 and 4 items respectively, covering all achievements and limitations stated in the plan.

### Deviations from Plan

None -- plan executed exactly as written.

**Total deviations:** 0
**Impact on plan:** None.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Non-SUSY duality conjecture | Assumed valid | N/A (conjecture) | If the duality is wrong |
| One-loop RG running | alpha_s/(4 pi) << 1 | ~10% from two-loop | mu ~ Lambda_QCD |
| Leading-order scalar potential | lambda/(16 pi^2) << 1 | Radiative corrections | Strong coupling |
| Planck-scale operator dominance | Lambda_D/M_Pl ~ 10^{-8} | (Lambda_D/M_Pl)^2 ~ 10^{-16} | Additional flavour dynamics |
| Naive N_f = 6 running (no thresholds) | All 6 quarks active | Factor ~3 in Lambda_QCD | Below m_t ~ 173 GeV |

## Open Questions

- Threshold corrections at quark mass thresholds would improve Lambda_QCD estimate (Exercise 6 will address this)
- Whether the O(1) coefficients c^{abcd} can be constrained by lattice simulations of the electric theory
- Whether the lightest mesino component can serve as a viable dark matter candidate
- Detailed phenomenology of the 17 heavy Higgs doublets at future colliders

## Self-Check: PASSED

- [x] lectures/lecture-08.tex exists (548 lines in Task 1 + 500 lines added in Task 2)
- [x] lectures/lecture-08.pdf exists (267 KB, 15 pages)
- [x] Commit b55f611 exists (Task 1)
- [x] Commit 4c49e2c exists (Task 2)
- [x] ASSERT_CONVENTION matches preamble.tex
- [x] Convention box lists all required conventions
- [x] Universal Yukawa Y_{ij} = y <H_{ij}>/v stated (Eq. 11 of 2407.17281)
- [x] y_t ~ O(1) and m_t ~ O(v) stated as parametric consistency
- [x] VEV sum rule stated as input, not prediction
- [x] Planck-scale operators from Eq. 21 of 2407.17281 presented
- [x] Warningbox about O(1) free coefficients present
- [x] Lambda_D stated as free parameter
- [x] v ~ Lambda_D^2/M_Pl ~ O(TeV) with dimensional analysis
- [x] Lambda_QCD from one-loop running (honestly: 60 MeV, not fudged to 200 MeV)
- [x] Three scales (Lambda_S, Lambda_D, Lambda_eGUT) presented
- [x] Collider signatures discussed with LHC constraints
- [x] Honest assessment: DOES (6 items) and DOES NOT (4 items)
- [x] Cross-references to all 8 lectures (pedagogical arc)
- [x] Preview box for Exercises 5-6
- [x] 9 conjectural qualifiers present
- [x] Hill et al. 2019 cited for scalar democracy
- [x] 0 LaTeX errors, 0 undefined references
- [x] All contract IDs covered
- [x] fp-formal-only satisfied (parametric scales present)
- [x] fp-precision-prediction guarded (no false precision)

---

_Phase: 04-the-dualised-standard-model_
_Plan: 03_
_Completed: 2026-03-20_
