---
phase: 02-susy-and-seiberg-duality
plan: 03
depth: full
one-liner: "Wrote Lecture 4 (N=2 SUSY executive summary: Coulomb branch, SW singularities, FI mechanism, APS deformation identifying magnetic quarks as monopoles) and Exercise Set 3 (4 Seiberg duality problems with full solutions cross-checked against verify_anomaly_matching.py)"
subsystem: formalism
tags: [seiberg-witten, coulomb-branch, monopole, fayet-iliopoulos, seiberg-duality, anomaly-matching, s-confinement]

requires:
  - phase: 02-susy-and-seiberg-duality plan 02
    provides: "Lecture 3 (Seiberg duality statement, anomaly matching for general N_c/N_f), anomaly verification script"
provides:
  - "Lecture 4: N=2 SUSY origin of magnetic quarks via APS deformation"
  - "N=2 to N=1 decomposition table (vector = V + Phi_adj, hyper = Q + Q-tilde)"
  - "N=2 beta function b_0^{N=2} = 2N_c - N_f verified via N=1 decomposition"
  - "Exercise Set 3: 4 problems with full solutions (anomaly matching SU(3) N_f=6, mass deformation, R-charges, s-confinement)"
affects: [03-non-susy-duality, 04-sm-duality]

methods:
  added: [N=2-to-N=1-decomposition, coulomb-branch-analysis, APS-deformation, s-confinement]
  patterns: [executive-summary-of-exact-results, monopole-identification-argument]

key-files:
  created:
    - lectures/lecture-04.tex
    - exercises/exercise-03.tex
  modified: []

key-decisions:
  - "Presented N=2 SW solution as executive summary only (no curve derivation, no monodromy computation, no instanton expansion) per scope control"
  - "Used [M] = [mass]^2 (UV dimension of composite Q*Q-tilde) in s-confinement dimensional analysis, not [M]=[mass] (which would be the elementary meson convention)"

patterns-established:
  - "N=2/N=1 decomposition table format: vector=V+Phi_adj, hyper=Q+Q-tilde, Phi NOT counted in N_f"
  - "APS 4-step argument structure: N=2 setup -> turn on W=mu*Tr(Phi^2) -> identify vacua at singularities -> take mu->infinity"

conventions:
  - "hbar = c = 1 (natural units)"
  - "metric = (+,-,-,-) (mostly minus)"
  - "T(fund) = 1/2 per Weyl fermion"
  - "R[Q] = (N_f - N_c)/N_f, R[W] = 2"
  - "N=2: N_f hypermultiplets = N_f pairs of N=1 chirals; adjoint Phi NOT counted in N_f"
  - "FI parameter [xi] = [mass]^2"
  - "APS deformation [mu] = [mass]"

plan_contract_ref: ".gpd/phases/02-susy-and-seiberg-duality/02-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-n2-origin:
      status: passed
      summary: "Lecture 4 presents the complete N=2 to N=1 deformation argument: N=2 multiplet decomposition, Coulomb branch with singular loci, massless monopoles/dyons at singularities (SW solution stated), FI mechanism for monopole condensation, W=mu*Tr(Phi^2) deformation, and explicit identification of monopoles with magnetic quarks. All at executive-summary depth (no SW curve derivation)."
      linked_ids: [deliv-lecture-04, test-n2-executive, test-fi-mechanism, test-n2-conventions, ref-seiberg-witten, ref-aps]
    claim-seiberg-exercises:
      status: passed
      summary: "Exercise Set 3 provides 4 problems spanning computational anomaly matching (SU(3) N_f=6), conceptual mass deformation (N_f=6->5), algebraic R-charge analysis, and limiting-case s-confinement (N_f=N_c+1). All problems have complete worked solutions with intermediate steps."
      linked_ids: [deliv-exercise-03, test-exercise-solutions, test-exercise-coverage, ref-seiberg-duality]
  deliverables:
    deliv-lecture-04:
      status: passed
      path: "lectures/lecture-04.tex"
      summary: "10-page lecture covering N=2 multiplets, Coulomb branch, SW solution (stated), FI mechanism, APS deformation, monopole-to-magnetic-quark identification. Compiles cleanly with preamble.tex."
      linked_ids: [claim-n2-origin, test-n2-executive, test-fi-mechanism, test-n2-conventions]
    deliv-exercise-03:
      status: passed
      path: "exercises/exercise-03.tex"
      summary: "12-page exercise set with 4 problems and full solutions. Solutions numerically cross-checked against verify_anomaly_matching.py."
      linked_ids: [claim-seiberg-exercises, test-exercise-solutions, test-exercise-coverage]
  acceptance_tests:
    test-n2-executive:
      status: passed
      summary: "All 5 elements verified present in Lecture 4: (1) N=2 multiplet decomposition table in Section 1.3, (2) Coulomb branch with singular loci in Section 2, (3) massless monopoles/dyons at singularities in Section 3.2, (4) W=mu*Tr(Phi^2) deformation in Section 5, (5) identification of monopoles with magnetic quarks in Section 5.3. N=2 physics content is ~5 pages (executive summary). No full SW curve derivation attempted."
      linked_ids: [claim-n2-origin, deliv-lecture-04, ref-aps]
    test-fi-mechanism:
      status: passed
      summary: "FI D-term V_FI = xi*D defined in Section 4.1 (eq 13). [xi] = [mass]^2 stated in eq 14 with dimensional analysis. Role in U(1) D-term breaking explained in Section 4.2. Connection to monopole condensation on the Coulomb branch in Section 4.3."
      linked_ids: [claim-n2-origin, deliv-lecture-04]
    test-n2-conventions:
      status: passed
      summary: "N=2 to N=1 decomposition table present (Section 1.3 tcolorbox). N=2 beta function b_0^{N=2} = 2N_c - N_f derived in eq 2 and verified via N=1 decomposition in eq 3: 3N_c - N_f - N_c = 2N_c - N_f. N_f counting consistent: adjoint Phi explicitly stated as NOT counted in N_f."
      linked_ids: [claim-n2-origin, deliv-lecture-04]
    test-exercise-solutions:
      status: passed
      summary: "All 4 exercise solutions verified: (1) SU(3) N_f=6 anomaly matching -- all 6 coefficients computed (3, -3, 3/2, -3/4, -18, -10), matching verify_anomaly_matching.py output. (2) Mass deformation SU(3) N_f=6->N_f=5 -- dual SU(2) with 5 flavours, Higgsing mechanism shown, SU(5)_L^3 check passes. (3) R[Q]=(N_f-N_c)/N_f derived, R[W_mag]=2 verified, Delta[M]=1 at N_f=3N_c/2 identified as lower conformal window boundary. (4) s-confinement for N_f=N_c+1: SU(1) trivial gauge group, confining superpotential with dimensional check, SU(4)_L^3 anomaly matching for Nc=3 Nf=4 passes."
      linked_ids: [claim-seiberg-exercises, deliv-exercise-03, ref-seiberg-duality]
    test-exercise-coverage:
      status: passed
      summary: "4 problems covering: anomaly matching (computational, Problem 1), mass deformation (conceptual, Problem 2), R-charges (algebraic, Problem 3), s-confinement (limiting case, Problem 4). Each problem has hints and full worked solution with explicit intermediate steps."
      linked_ids: [claim-seiberg-exercises, deliv-exercise-03]
  references:
    ref-seiberg-duality:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Seiberg hep-th/9411149 cited in exercise-03.tex; anomaly coefficients for SU(3) N_f=6 computed and match Seiberg exactly (verified by script)."
    ref-seiberg-witten:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "SW hep-th/9407087 cited in lecture-04.tex as SW1994; key results stated (two singular points for SU(2), monopole/dyon identification)."
    ref-aps:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "APS hep-th/9603042 cited in lecture-04.tex as APS1996; 4-step deformation argument presented in Section 5."
    ref-sannino-2407:
      status: completed
      completed_actions: []
      missing_actions: []
      summary: "Sannino 2407.17281 cited in both lecture-04.tex and exercise-03.tex for project backbone notation compatibility."
  forbidden_proxies:
    fp-full-sw-derivation:
      status: rejected
      notes: "No SW curve derivation, no monodromy computation, no instanton expansion in Lecture 4. Explicit warning box in Section 3 states scope. N=2 physics content is executive summary only (~5 pages)."
    fp-exercises-without-solutions:
      status: rejected
      notes: "All 4 exercises have complete worked solutions with explicit intermediate steps."
  uncertainty_markers:
    weakest_anchors:
      - "N=2 executive summary requires students to accept SW results on faith -- the conceptual leap from 'monopoles become massless' to 'these ARE the magnetic quarks' is not rigorously established without the full SW derivation"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-seiberg-exercises
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-seiberg-duality
    comparison_kind: benchmark
    metric: exact_match
    threshold: "all 6 anomaly coefficients match"
    verdict: pass
    recommended_action: "None needed"
    notes: "SU(3) N_f=6 anomaly coefficients (3, -3, 3/2, -3/4, -18, -10) match verify_anomaly_matching.py output exactly"

duration: 25min
completed: 2026-03-20
---

# Phase 02 Plan 03: N=2 SUSY and Seiberg Duality Exercises Summary

**Wrote Lecture 4 (N=2 SUSY executive summary: Coulomb branch, SW singularities, FI mechanism, APS deformation identifying magnetic quarks as monopoles) and Exercise Set 3 (4 Seiberg duality problems with full solutions cross-checked against verify_anomaly_matching.py)**

## Performance

- **Duration:** ~25 min
- **Started:** 2026-03-20
- **Completed:** 2026-03-20
- **Tasks:** 2
- **Files created:** 2 (lectures/lecture-04.tex, exercises/exercise-03.tex)

## Key Results

- N=2 beta function b_0^{N=2} = 2N_c - N_f verified via N=1 decomposition: 3N_c - N_f - N_c = 2N_c - N_f [CONFIDENCE: HIGH]
- APS deformation argument: monopoles on N=2 Coulomb branch become magnetic quarks of N=1 Seiberg duality as W = mu Tr(Phi^2) is turned on and mu -> infinity [CONFIDENCE: HIGH -- well-established result from APS hep-th/9603042]
- FI mechanism: [xi] = [mass]^2 dimensional check confirmed [CONFIDENCE: HIGH]
- All 6 anomaly coefficients for SU(3) N_f=6: (3, -3, 3/2, -3/4, -18, -10) match verify_anomaly_matching.py [CONFIDENCE: HIGH -- cross-checked against independent script]
- s-confinement superpotential W = (B_i M^i_j B-tilde^j - det M) / Lambda^{2N_c-1} dimensionally verified [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Write Lecture 4** - `8048e61` (docs: N=2 SUSY executive summary with Coulomb branch, SW singularities, FI mechanism, APS deformation)
2. **Task 2: Write Exercise Set 3** - `5badd6f` (docs: 4 Seiberg duality problems with full solutions)

## Files Created/Modified

- `lectures/lecture-04.tex` - Lecture 4: N=2 SUSY, Coulomb branch, SW solution (stated), FI mechanism, APS deformation, monopole identification (10 pages compiled)
- `exercises/exercise-03.tex` - Exercise Set 3: anomaly matching SU(3) N_f=6, mass deformation, R-charges, s-confinement (12 pages compiled)

## Equations Derived

**Eq. (02-03.1):** N=2 beta function

$$b_0^{N=2} = 2N_c - N_f$$

Verified via N=1 decomposition: $3N_c - N_f - N_c = 2N_c - N_f$.

**Eq. (02-03.2):** N=2 superpotential (required by extended SUSY)

$$W_{N=2} = \sqrt{2}\, Q_i \Phi \widetilde{Q}^i$$

**Eq. (02-03.3):** APS deformation

$$W_{\mathrm{def}} = \mu\, \mathrm{Tr}\, \Phi^2$$

with $[\mu] = [\mathrm{mass}]$, breaking $N=2 \to N=1$.

**Eq. (02-03.4):** FI D-term

$$\mathcal{L}_{\mathrm{FI}} = \xi D, \qquad [\xi] = [\mathrm{mass}]^2$$

**Eq. (02-03.5):** s-confinement superpotential ($N_f = N_c + 1$)

$$W = \frac{1}{\Lambda^{2N_c - 1}} (B_i M^i{}_j \widetilde{B}^j - \det M)$$

## Validations Completed

- N=2 beta function consistency: b_0^{N=2} = 2N_c - N_f matches N=1 decomposition
- FI parameter dimension: [xi] = [mass]^2 from [L] = [mass]^4 and [D] = [mass]^2
- APS deformation dimension: [mu Tr Phi^2] = [mass]^3 = [W]
- SU(3) N_f=6 anomaly matching: all 6 coefficients match verify_anomaly_matching.py
- Mass deformation SU(3) N_f=6 -> N_f=5: dual SU(2) with 5 flavours, SU(5)_L^3 anomaly check passes
- R[W_mag] = 2 verified for general (N_c, N_f)
- Delta[M] = 1 at N_f = 3N_c/2: confirmed for N_c = 2, 3, 5
- s-confinement dimensional analysis: [B M B-tilde / Lambda^{2N_c-1}] = [mass]^3, [det M / Lambda^{2N_c-1}] = [mass]^3
- s-confinement anomaly matching: SU(4)_L^3 for N_c=3, N_f=4 passes (el=3, conf=3)
- LaTeX compilation: both files compile with 0 errors

## Decisions & Deviations

**Key decisions:**
- Presented N=2 SW solution as executive summary only (scope control per plan)
- Used [M] = [mass]^2 (composite dimension) for s-confinement dimensional analysis rather than [M] = [mass] (elementary meson convention from CONVENTIONS.md). This is correct because in the confined description the meson inherits the UV dimension of Q*Q-tilde. A corrective note in the exercise solution explains this subtlety.

**Deviations:** None -- plan executed as written.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Executive summary of SW theory | Always (stated results are exact) | N/A (presentational choice) | Students requiring quantitative SW curve derivation |
| Semiclassical monopole identification | Near singular loci of N=2 moduli space | Exact at the singularities | Far from singular loci on the Coulomb branch |

## Figures Produced

| Figure | File | Description | Key Feature |
| --- | --- | --- | --- |
| Fig. (02-03.1) | lecture-04.tex, Fig. 1 | SU(2) quantum Coulomb branch | Two singular points at u = +/-Lambda^2 with monopole/dyon labels; classical singularity at u=0 shown as split |

## Open Questions

- Whether the executive-summary presentation of N=2 is sufficient for students to accept the monopole-to-magnetic-quark identification on conceptual grounds (weakest anchor)
- Whether additional exercises on N=2 multiplet counting would strengthen student understanding

## Next Phase Readiness

Lecture 4 and Exercise Set 3 complete Phase 2 (SUSY and Seiberg duality). The N=2 origin of magnetic quarks, combined with the anomaly matching from Lecture 3 and the hands-on exercises, provides the foundation for extending duality ideas to non-SUSY theories in Phase 3.

## Contract Coverage

- Claim IDs advanced: claim-n2-origin -> passed, claim-seiberg-exercises -> passed
- Deliverable IDs produced: deliv-lecture-04 -> lectures/lecture-04.tex, deliv-exercise-03 -> exercises/exercise-03.tex
- Acceptance test IDs run: test-n2-executive -> passed, test-fi-mechanism -> passed, test-n2-conventions -> passed, test-exercise-solutions -> passed, test-exercise-coverage -> passed
- Reference IDs surfaced: ref-seiberg-duality -> [compare, cite], ref-seiberg-witten -> [cite], ref-aps -> [cite], ref-sannino-2407 -> [cited]
- Forbidden proxies rejected: fp-full-sw-derivation -> rejected (executive summary only), fp-exercises-without-solutions -> rejected (all solutions complete)
- Decisive comparison verdicts: claim-seiberg-exercises -> pass (all 6 anomaly coefficients match script)

## Self-Check: PASSED

- [x] lectures/lecture-04.tex exists and compiles (10 pages, 0 errors)
- [x] exercises/exercise-03.tex exists and compiles (12 pages, 0 errors)
- [x] Commit 8048e61 exists (Task 1)
- [x] Commit 5badd6f exists (Task 2)
- [x] All exercise solutions verified numerically against verify_anomaly_matching.py
- [x] Convention consistency: all files use mostly-minus metric, T(fund)=1/2, R[Q]=(N_f-N_c)/N_f
- [x] N=2 beta function verified via N=1 decomposition
- [x] FI mechanism [xi]=[mass]^2 dimensional check passed
- [x] No SW curve derivation in Lecture 4 (scope control)

---

_Phase: 02-susy-and-seiberg-duality_
_Completed: 2026-03-20_
