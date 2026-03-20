---
phase: 02-susy-and-seiberg-duality
plan: 04
depth: full
one-liner: "Wrote Exercise Set 4 with 3 N=2 deformation problems and full solutions: multiplet decomposition with 4+4 DOF verification, FI D-term mechanism with [xi]=[mass]^2 dimensional check, and APS deformation for SU(2) N_f=4 demonstrating self-duality"
subsystem: formalism
tags: [n2-multiplets, fayet-iliopoulos, aps-deformation, self-duality, seiberg-duality, conformal-window]

requires:
  - phase: 02-susy-and-seiberg-duality plan 03
    provides: "Lecture 4 (N=2 SUSY, Coulomb branch, APS deformation, FI mechanism), Exercise Set 3 (Seiberg duality problems)"
provides:
  - "Exercise Set 4: 3 problems with full solutions on N=2 to N=1 deformation"
  - "Explicit N=2 to N=1 multiplet decomposition with DOF counting (4+4 per hyper)"
  - "FI D-term mechanism worked example: SUSY breaking vs preservation, gauge boson mass"
  - "APS deformation for SU(2) N_f=4: self-duality demonstrated, meson dimension Delta=3/2 computed"
affects: [03-non-susy-duality, 04-sm-duality]

methods:
  added: [fi-d-term-potential-minimisation, aps-deformation-exercise, conformal-dimension-computation]
  patterns: [exercise-set-format-with-solutions, n2-n1-decomposition-table]

key-files:
  created:
    - exercises/exercise-04.tex
  modified: []

key-decisions:
  - "Used SU(2) N_f=4 (self-dual) for APS deformation exercise instead of SU(2) N_f=2 (quantum modified moduli space) -- cleaner pedagogically and illustrates self-duality"
  - "FI Problem 2(d) uses W=0 with two opposite-charge fields instead of plan's W=m*Phi*Phi-tilde -- the plan's suggestion was physically incorrect (F=0 forces phi=phi-tilde=0, then D=xi!=0, SUSY broken for all m!=0, xi!=0)"
  - "Distinguished N=2 R-charges (R[Q]=1, R[Phi]=0) from N=1 R-charges (R[Q]=(N_f-N_c)/N_f) with explicit remark explaining the difference"

patterns-established:
  - "Exercise format: convention box, problems with star ratings and time estimates, hints section, full worked solutions"
  - "Scope note pattern for exercises that accept prior results without derivation"

conventions:
  - "hbar = c = 1 (natural units)"
  - "metric = (+,-,-,-) (mostly minus)"
  - "T(fund) = 1/2 per Weyl fermion"
  - "N=2: N_f hypermultiplets = N_f pairs of N=1 chirals; adjoint Phi NOT counted in N_f"
  - "FI parameter [xi] = [mass]^2"
  - "APS deformation [mu] = [mass]"
  - "N=2 R-charges: R[Q] = R[Q-tilde] = 1, R[Phi] = 0"

plan_contract_ref: ".gpd/phases/02-susy-and-seiberg-duality/02-04-PLAN.md#/contract"
contract_results:
  claims:
    claim-n2-exercises:
      status: passed
      summary: "Exercise Set 4 provides 3 problems covering N=2 multiplet decomposition with beta function verification, FI D-term analysis with dimensional checks, and APS deformation for SU(2) N_f=4 with self-duality identification. All problems have full worked solutions with explicit intermediate steps."
      linked_ids: [deliv-exercise-04, test-exercise-04-solutions, test-exercise-04-coverage, ref-seiberg-witten, ref-aps, ref-seiberg-duality]
  deliverables:
    deliv-exercise-04:
      status: passed
      path: "exercises/exercise-04.tex"
      summary: "10-page exercise set with 3 problems and full solutions. Compiles cleanly with preamble.tex (0 errors). ASSERT_CONVENTION line present."
      linked_ids: [claim-n2-exercises, test-exercise-04-solutions, test-exercise-04-coverage]
  acceptance_tests:
    test-exercise-04-solutions:
      status: passed
      summary: "All 3 exercise solutions verified: (1) N=2 decomposition gives correct N=1 content; b_0 = 3N_c - (N_c + N_f) = 2N_c - N_f matches N=2 result; SU(2) N_f=4 conformal (b_0=0); SU(3) N_f=5 AF (b_0=1); R[W]=2 verified with N=2 R-charges. (2) FI analysis: xi>0 SUSY broken, xi<0 SUSY preserved with U(1) broken; [xi]=[mass]^2 verified; m_A^2=2g|xi| with correct dimensions; two opposite-charge fields always achieve D-flatness. (3) APS for SU(2) N_f=4: deformation produces N=1 SU(2) N_f=4; Seiberg dual is SU(2) (self-dual); Delta[M]=3/2 inside conformal window 3<4<6; S-duality descent explained."
      linked_ids: [claim-n2-exercises, deliv-exercise-04, ref-seiberg-witten, ref-aps]
    test-exercise-04-coverage:
      status: passed
      summary: "3 problems covering: multiplet decomposition + beta function (algebraic, Problem 1, 20 min), FI D-term mechanism (potential minimisation, Problem 2, 25 min), APS deformation (conceptual flow + self-duality, Problem 3, 30 min). Each problem has hints and full worked solution with explicit intermediate steps."
      linked_ids: [claim-n2-exercises, deliv-exercise-04]
  references:
    ref-seiberg-witten:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "SW hep-th/9407087 cited in exercise-04.tex bibliography and referenced in Problem 3 scope note."
    ref-aps:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "APS hep-th/9603042 cited in exercise-04.tex bibliography and referenced in Problem 3 background."
    ref-seiberg-duality:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Seiberg hep-th/9411149 cited in exercise-04.tex bibliography. Seiberg duality rule SU(N_f-N_c) applied and verified for SU(2) N_f=4 self-duality case."
  forbidden_proxies:
    fp-exercises-without-solutions-04:
      status: rejected
      notes: "All 3 exercises have complete worked solutions with explicit intermediate steps."
    fp-sw-derivation-in-exercise:
      status: rejected
      notes: "No exercise asks students to derive the SW curve, compute monodromies, or perform instanton calculations. Problem 3 has explicit scope note: 'We accept the Seiberg-Witten solution as a stated result.' Exercises test the deformation logic and self-duality conclusion only."
  uncertainty_markers:
    weakest_anchors:
      - "APS deformation exercise for SU(2) N_f=4 requires accepting SW results and Seiberg duality rule; the exercise tests understanding of the deformation logic, not their derivation"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-n2-exercises
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-seiberg-duality
    comparison_kind: benchmark
    metric: exact_match
    threshold: "Seiberg dual of SU(2) N_f=4 is SU(2) N_f=4 (self-dual)"
    verdict: pass
    recommended_action: "None needed"
    notes: "Self-duality verified: SU(N_f - N_c) = SU(4-2) = SU(2). Conformal window check 3 < 4 < 6 passes. Meson dimension Delta=3/2 > 1 confirms healthy operator."

duration: 7min
completed: 2026-03-20
---

# Phase 02 Plan 04: N=2 Deformation Exercises Summary

**Wrote Exercise Set 4 with 3 N=2 deformation problems and full solutions: multiplet decomposition with 4+4 DOF verification, FI D-term mechanism with [xi]=[mass]^2 dimensional check, and APS deformation for SU(2) N_f=4 demonstrating self-duality**

## Performance

- **Duration:** ~7 min
- **Started:** 2026-03-20T01:39:11Z
- **Completed:** 2026-03-20T01:46:00Z
- **Tasks:** 1
- **Files created:** 1 (exercises/exercise-04.tex)

## Key Results

- N=2 to N=1 multiplet decomposition: one hyper = 4+4 real on-shell DOF, adjoint Phi not counted in N_f [CONFIDENCE: HIGH -- standard textbook result]
- Beta function verification: b_0^{N=1} = 3N_c - (N_c + N_f) = 2N_c - N_f = b_0^{N=2} [CONFIDENCE: HIGH -- verified against Lecture 4 eq (2)-(3)]
- FI parameter dimension: [xi] = [mass]^2, verified from [V_D] = [mass]^4 and [D] = [mass]^2 [CONFIDENCE: HIGH]
- Gauge boson mass from FI mechanism: m_A^2 = 2g|xi|, [m_A] = [mass] [CONFIDENCE: HIGH]
- SU(2) N_f=4 self-duality: Seiberg dual is SU(4-2) = SU(2), theory maps to itself [CONFIDENCE: HIGH -- well-established result from Seiberg hep-th/9411149]
- Meson dimension at IR fixed point: Delta[M] = (3/2)(2(4-2)/4) = 3/2 > 1 (healthy interacting operator in conformal window 3 < 4 < 6) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Write Exercise Set 4** - `7554271` (docs: 3 N=2 deformation problems with full solutions)

## Files Created/Modified

- `exercises/exercise-04.tex` - Exercise Set 4: N=2 multiplet decomposition, FI D-term, APS deformation for SU(2) N_f=4 (10 pages compiled, 0 errors)

## Equations Derived

**Eq. (02-04.1):** N=1 beta function for N=2 SQCD

$$b_0 = 3T(\mathrm{adj}) - [T(\mathrm{adj}) + N_f T(\mathrm{fund}) + N_f T(\mathrm{antifund})] = 3N_c - N_c - N_f = 2N_c - N_f$$

**Eq. (02-04.2):** FI D-term potential

$$V_D = \frac{1}{2}(g|\phi|^2 + \xi)^2, \qquad [\xi] = [\mathrm{mass}]^2$$

**Eq. (02-04.3):** Gauge boson mass from FI Higgs mechanism

$$m_A^2 = 2g^2 \langle|\phi|^2\rangle = 2g|\xi|$$

**Eq. (02-04.4):** F-term equation for adjoint under APS deformation

$$\Phi = -\frac{1}{\sqrt{2}\,\mu}\, Q_i \widetilde{Q}^i \;\xrightarrow{\mu \to \infty}\; 0$$

**Eq. (02-04.5):** Meson conformal dimension for SU(2) N_f=4

$$\Delta[M] = \frac{3}{2} R[M] = \frac{3}{2} \cdot \frac{2(N_f - N_c)}{N_f} = \frac{3}{2}$$

## Validations Completed

- N=2 beta function consistency: b_0^{N=1} = 2N_c - N_f = b_0^{N=2} (Problem 1c)
- SU(2) N_f=4: b_0 = 0 (conformal boundary, Problem 1d(i))
- SU(3) N_f=5: b_0 = 1 > 0 (asymptotically free, Problem 1d(ii))
- [W_{N=2}] = [mass]^3 verified (Problem 1e(i))
- R[W_{N=2}] = 1 + 0 + 1 = 2 using N=2 R-charges (Problem 1e(ii))
- [xi] = [mass]^2 from dimensional analysis of V_D (Problem 2b(i))
- [m_A] = [mass] from m_A^2 = 2g|xi| (Problem 2c)
- [mu Tr Phi^2] = [mass]^3 = [W] (Problem 3c)
- Conformal window check: 3 < 4 < 6 for N_c = 2 (Problem 3e(ii))
- Unitarity bound: Delta[M] = 3/2 > 1 (Problem 3e(iii))
- LaTeX compilation: 10 pages, 0 errors
- Convention consistency: ASSERT_CONVENTION line matches convention_lock; all exercises use T(fund)=1/2, mostly-minus metric, N=2 counting conventions from Lecture 4

## Decisions & Deviations

**Key decisions:**
- Used SU(2) N_f=4 (self-dual, conformal) for the APS deformation exercise -- the cleanest illustration of how N=2 S-duality descends to N=1 Seiberg self-duality
- Distinguished N=2 R-charges (R[Q]=1, R[Phi]=0) from N=1 R-charges (R[Q]=(N_f-N_c)/N_f) with an explicit remark explaining that they are different symmetries
- Used SU(3) N_f=5 (rather than N_f=6) for the second case in Problem 1(d) to show a theory that IS asymptotically free (b_0=1>0), providing contrast with the conformal SU(2) N_f=4

### Auto-fixed Issues

**1. [Rule 4 - Missing/Incorrect Component] Corrected FI Problem 2 part (d)**

- **Found during:** Task 1 (physics content planning)
- **Issue:** Plan specified W = m Phi Phi-tilde with two opposite-charge fields and claimed "both F=0 and D=0 can be satisfied when xi < 0". This is incorrect: for m != 0, F-flatness requires phi = phi-tilde = 0, then D = xi != 0, so SUSY is always broken when m != 0 and xi != 0.
- **Fix:** Replaced with W = 0 and two opposite-charge fields, where D-flatness |phi|^2 - |phi-tilde|^2 = -xi/g always has solutions. This correctly demonstrates the key physics: having fields of both charges allows D-flatness for either sign of xi.
- **Verification:** D-flatness equation with xi > 0: set phi=0, |phi-tilde|^2 = xi/g. With xi < 0: set phi-tilde=0, |phi|^2 = |xi|/g. Both valid.
- **Committed in:** 7554271

---

**Total deviations:** 1 auto-fixed (1 incorrect physics in plan)
**Impact on plan:** Essential physics correction. The exercise is now physically correct while covering the same conceptual material (FI D-term with multiple charged fields).

## Open Questions

- Whether the self-duality of SU(2) N_f=4 should be connected more explicitly to the N=2 Montonen-Olive duality in lecture material
- Whether an additional exercise on the quantum modified moduli space (N_f = N_c case) would strengthen the coverage of N=2 deformation physics

## Next Phase Readiness

Exercise Set 4 completes Phase 2 (SUSY and Seiberg Duality). All four plans are now complete:
- Plan 01: Convention verification and reference setup
- Plan 02: Lectures 2-3 (SUSY foundations and Seiberg duality) with anomaly matching verification script
- Plan 03: Lecture 4 (N=2 executive summary) and Exercise Set 3 (Seiberg duality problems)
- Plan 04: Exercise Set 4 (N=2 deformation exercises)

Phase 2 provides the complete SUSY duality foundation needed for Phase 3 (non-SUSY duality extension to the Standard Model).

## Contract Coverage

- Claim IDs advanced: claim-n2-exercises -> passed
- Deliverable IDs produced: deliv-exercise-04 -> exercises/exercise-04.tex (passed)
- Acceptance test IDs run: test-exercise-04-solutions -> passed, test-exercise-04-coverage -> passed
- Reference IDs surfaced: ref-seiberg-witten -> [cite], ref-aps -> [cite], ref-seiberg-duality -> [compare]
- Forbidden proxies rejected: fp-exercises-without-solutions-04 -> rejected (all solutions complete), fp-sw-derivation-in-exercise -> rejected (explicit scope note, no SW derivation requested)
- Decisive comparison verdicts: claim-n2-exercises -> pass (SU(2) N_f=4 self-duality verified, conformal window and meson dimension checks pass)

## Self-Check: PASSED

- [x] exercises/exercise-04.tex exists and compiles (10 pages, 0 errors)
- [x] Commit 7554271 exists (Task 1)
- [x] ASSERT_CONVENTION line present and matches convention_lock
- [x] 3 problems present with hints and full solutions
- [x] Problem 1: N=1 decomposition correct, b_0 = 2N_c - N_f verified, 4+4 DOF per hyper
- [x] Problem 2: FI D-term analysis correct, [xi]=[mass]^2 verified, SUSY breaking/preservation correctly identified
- [x] Problem 3: APS deformation for SU(2) N_f=4, self-duality identified, Delta[M]=3/2 computed
- [x] N=2 conventions consistent with Lecture 4 and CONVENTIONS.md
- [x] No SW curve derivation requested in any exercise (scope control)
- [x] All references cited: SW hep-th/9407087, APS hep-th/9603042, Seiberg hep-th/9411149

---

_Phase: 02-susy-and-seiberg-duality_
_Completed: 2026-03-20_
