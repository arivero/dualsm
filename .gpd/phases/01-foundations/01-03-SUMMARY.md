---
phase: 01-foundations
plan: 03
depth: full
one-liner: "Wrote Exercise Sets 1 and 2 (8 problems with full worked solutions) covering anomaly matching and the conformal window, all numerical results exact, Banks-Zaks formula correctly derived from two-loop beta function"
subsystem: formalism
tags: [anomaly-matching, conformal-window, banks-zaks, SQCD, exercises, pedagogy]

requires:
  - phase: 01-foundations, plan 01
    provides: verified conventions (T(fund)=1/2, A(fund)=1, b_0=(11N_c-2N_f)/3)
  - phase: 01-foundations, plan 02
    provides: Lecture 1 content (preamble.tex, lecture-01.tex)
provides:
  - "Exercise Set 1: 4 problems on anomaly matching with full solutions (exercise-01.tex)"
  - "Exercise Set 2: 4 problems on conformal window with full solutions (exercise-02.tex)"
  - "UV anomaly coefficients for SU(N_c) with N_f fundamentals (6 independent coefficients)"
  - "Banks-Zaks fixed point alpha_* = -2pi*b_0/b_1 for SU(3) N_f=15,16"
  - "SUSY conformal window tabulated for SU(2,3,5)"
  - "Phase diagram of SU(3) as function of N_f (TikZ figure)"
affects: [01-foundations plan 04, 02-susy-foundations, 03-duality]

methods:
  added: [anomaly-coefficient-computation, beta-function-analysis, R-charge-unitarity-bound]
  patterns: [convention-check-within-exercises, all-left-handed-Weyl-convention]

key-files:
  created:
    - exercises/exercise-01.tex
    - exercises/exercise-02.tex

key-decisions:
  - "Used correct Banks-Zaks formula alpha_* = -2pi*b_0/b_1 from Lecture 1 beta function convention, NOT the plan's formula alpha_* = -b_0/(2b_1)*16pi^2 which gives the wrong value"
  - "Problem 2 of Exercise 1: noted that SU(2)^3 cubic anomaly vanishes (d^abc=0 for SU(2)); used mixed anomalies SU(2)^2 U(1)_B for non-trivial matching"

patterns-established:
  - "All-left-handed Weyl convention for anomaly computations"
  - "Convention check problems embedded within exercise sets"

conventions:
  - "T(fund) = 1/2 per Weyl fermion"
  - "A(fund) = 1 (cubic anomaly coefficient)"
  - "b_0 = (11N_c - 2N_f)/3 for N_f Dirac flavours"
  - "B[Q] = 1/N_c, B[Q-tilde] = -1/N_c (Seiberg)"
  - "R[Q] = (N_f - N_c)/N_f"
  - "beta(alpha) = -(b_0/2pi)*alpha^2 - (b_1/4pi^2)*alpha^3"

plan_contract_ref: ".gpd/phases/01-foundations/01-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-exercises-anomaly:
      status: passed
      summary: "Exercise Set 1 provides 4 problems with full worked solutions covering SM gauge anomaly cancellation, SU(3) N_f=2 't Hooft matching, general SU(N_c) anomaly coefficients, and antisymmetric matter. All anomaly coefficients are exact integers/rationals."
      linked_ids: [deliv-exercise-01, test-anomaly-coefficients, test-exercise-solvable, ref-seiberg-duality, ref-intriligator-seiberg]
    claim-exercises-conformal:
      status: passed
      summary: "Exercise Set 2 provides 4 problems with full worked solutions covering b_0 computation, Banks-Zaks fixed point, SUSY conformal window derivation, and phase diagram synthesis. SUSY window bounds reproduced exactly."
      linked_ids: [deliv-exercise-02, test-conformal-bounds, test-banks-zaks, ref-seiberg-duality, ref-banks-zaks]
  deliverables:
    deliv-exercise-01:
      status: passed
      path: "exercises/exercise-01.tex"
      summary: "12-page exercise set with 4 problems and full solutions on anomaly matching"
      linked_ids: [claim-exercises-anomaly, test-anomaly-coefficients]
    deliv-exercise-02:
      status: passed
      path: "exercises/exercise-02.tex"
      summary: "11-page exercise set with 4 problems and full solutions on conformal window"
      linked_ids: [claim-exercises-conformal, test-conformal-bounds, test-banks-zaks]
  acceptance_tests:
    test-anomaly-coefficients:
      status: passed
      summary: "SU(2)_L^3 = 3 for SU(3) N_f=2 UV (though SU(2)^3 cubic anomaly vanishes; non-trivial check is SU(2)^2 U(1)_B = 1/2). SU(5) antisymmetric: A(antisym_2) = 1. All coefficients exact."
      linked_ids: [claim-exercises-anomaly, deliv-exercise-01, ref-seiberg-duality]
    test-exercise-solvable:
      status: passed
      summary: "All exercises use only material from Lecture 1. Solutions include all intermediate steps. Difficulty ratings and time estimates provided."
      linked_ids: [claim-exercises-anomaly, deliv-exercise-01]
    test-conformal-bounds:
      status: passed
      summary: "b_0(SU(3),6) = 7. b_0(SU(3),17) = -1/3 < 0. SUSY window SU(3): N_f=5,6,7,8. R[Q] at N_f=3N_c gives 2/3."
      linked_ids: [claim-exercises-conformal, deliv-exercise-02, ref-seiberg-duality]
    test-banks-zaks:
      status: passed
      summary: "b_0(SU(3),16) = 1/3. b_1(SU(3),16) = -302/3. alpha_* = 2pi/302 ~ 0.021 > 0 and << 1. Perturbatively reliable."
      linked_ids: [claim-exercises-conformal, deliv-exercise-02, ref-banks-zaks]
  references:
    ref-seiberg-duality:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Seiberg conventions used throughout; anomaly coefficients and R-charge formula compatible with hep-th/9411149"
    ref-intriligator-seiberg:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Anomaly matching structure follows Intriligator-Seiberg systematic template"
    ref-banks-zaks:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Banks-Zaks fixed point calculation reproduced; alpha_* formula consistent with original paper's two-loop beta function"
  forbidden_proxies:
    fp-solutions-missing:
      status: rejected
      notes: "All 8 problems have full worked solutions with intermediate steps"
    fp-numerical-only:
      status: rejected
      notes: "All conformal window results derived analytically: b_0=0 boundary, b_1/b_0 ratio for Banks-Zaks, SUSY exact result from R-charge unitarity bound"

duration: 8min
completed: 2026-03-20
---

# Phase 01-foundations Plan 03: Exercise Sets 1 and 2 Summary

**Wrote Exercise Sets 1 and 2 (8 problems total with full worked solutions) covering 't Hooft anomaly matching and the conformal window. All anomaly coefficients are exact integers/rationals. Banks-Zaks formula correctly derived as alpha_* = -2pi*b_0/b_1 from the stated two-loop beta function, giving alpha_* ~ 0.021 for SU(3) N_f=16. SUSY conformal window 3N_c/2 < N_f < 3N_c tabulated for SU(2,3,5).**

## Performance

- **Duration:** 8 min
- **Started:** 2026-03-20T00:23:46Z
- **Completed:** 2026-03-20T00:32:31Z
- **Tasks:** 2
- **Files created:** 2

## Key Results

- Exercise Set 1 (exercise-01.tex, 12 pages): 4 problems on anomaly matching -- SM gauge anomaly cancellation, SU(3) N_f=2 't Hooft matching, general SU(N_c) anomaly coefficients, antisymmetric matter [CONFIDENCE: HIGH]
- Exercise Set 2 (exercise-02.tex, 11 pages): 4 problems on conformal window -- b_0 survey, Banks-Zaks fixed point, SUSY conformal window, phase diagram synthesis [CONFIDENCE: HIGH]
- Banks-Zaks fixed point: alpha_*(SU(3), N_f=16) = 2pi/302 ~ 0.021, perturbatively reliable [CONFIDENCE: HIGH]
- SUSY conformal window SU(3): N_f = 5, 6, 7, 8 (exact) [CONFIDENCE: HIGH]
- All 6 UV anomaly coefficients for SU(N_c) with N_f fundamentals computed and verified [CONFIDENCE: HIGH]

## Task Commits

Each task was committed atomically:

1. **Task 1: Exercise Set 1 -- Anomaly matching** - `54b5cd5` (docs)
2. **Task 2: Exercise Set 2 -- Conformal window** - `21e9c32` (docs)

## Files Created/Modified

- `exercises/exercise-01.tex` - Exercise Set 1: 4 problems on anomaly matching with full solutions
- `exercises/exercise-02.tex` - Exercise Set 2: 4 problems on conformal window with full solutions

## Equations Derived

**Eq. (01-03.1):** UV anomaly coefficients for SU(N_c) with N_f fundamentals (Exercise 1, Problem 3):

$$\mathcal{A}_{UV}[SU(N_f)_L^3] = N_c, \quad \mathcal{A}_{UV}[SU(N_f)_L^2 U(1)_B] = 1/2, \quad \mathcal{A}_{UV}[U(1)_B^3] = 0$$

**Eq. (01-03.2):** Banks-Zaks fixed point (Exercise 2, Problem 2):

$$\alpha_s^* = -\frac{2\pi b_0}{b_1}$$

derived from $\beta(\alpha_s) = -(b_0/2\pi)\alpha_s^2 - (b_1/4\pi^2)\alpha_s^3$.

**Eq. (01-03.3):** SUSY conformal window (Exercise 2, Problem 3):

$$\frac{3N_c}{2} < N_f < 3N_c$$

with lower bound from unitarity: $R[M] = 2(N_f - N_c)/N_f \geq 2/3$.

## Validations Completed

- SM gauge anomaly cancellation: SU(3)^2 U(1)_Y, SU(2)^2 U(1)_Y, U(1)_Y^3 all vanish (Problem 1)
- SU(3) N_f=2 anomaly matching: UV = IR for SU(2)_L^2 U(1)_B (= 1/2), U(1)_B^3 (= 0), U(1)_B-grav (= 0)
- b_0 values: b_0(3,0)=11, b_0(3,2)=29/3, b_0(3,6)=7, b_0(3,16)=1/3, b_0(3,17)=-1/3
- Convention check: (11/3)T(adj) - (4/3)N_f T(fund) = (11N_c - 2N_f)/3 with T(fund)=1/2 verified
- Banks-Zaks: alpha_*(SU(3),16) = 2pi/302 ~ 0.021, alpha_*(SU(3),15) = pi/44 ~ 0.071
- SUSY window: SU(2): N_f=4,5; SU(3): N_f=5,6,7,8; SU(5): N_f=8,...,14
- R-charge at boundary: R[M] = 2/3 at N_f = 3N_c/2 (unitarity bound saturated)
- Gauge anomaly cancellation for antisymmetric: A(antisym_2) + (N-4)*A(antifund) = 0
- LaTeX compilation: both exercise files compile successfully with no errors

## Decisions & Deviations

### Key Decision: Banks-Zaks Formula

The plan stated `alpha_* = -(b_0/b_1) * 8pi^2` (approximations frontmatter) and `alpha_* = -b_0/(2b_1) * 16pi^2` (Problem 2 description), giving alpha_* ~ 0.26 for SU(3) N_f=16.

However, deriving directly from the stated beta function $\beta(\alpha) = -(b_0/2\pi)\alpha^2 - (b_1/4\pi^2)\alpha^3$ yields:

$$\alpha_* = -\frac{2\pi b_0}{b_1}$$

For SU(3) N_f=16: alpha_* = 2pi/302 ~ 0.021.

This matches Lecture 1 equation (eq:bz-fixedpoint) exactly. The plan's formula corresponds to a different beta function convention where the two-loop term has coefficient $b_1/(8\pi^2)$ instead of $b_1/(4\pi^2)$. Since our convention is locked by Lecture 1, I used the correct formula. [Deviation Rule 1 - auto-fix: corrected formula to match established beta function convention.]

### SU(2) Cubic Anomaly

Problem 2 of Exercise Set 1 identified that SU(2)^3 cubic anomaly vanishes (d^{abc} = 0 for SU(2)), so the non-trivial anomaly matching involves the mixed anomalies SU(2)^2 U(1)_B. This is physically correct and pedagogically important. [Deviation Rule 4 - added clarification for correctness.]

## Open Questions

- The non-SUSY conformal window lower boundary for SU(3) remains debated (N_f ~ 8-12); Exercise 2 Problem 4(d) discusses the lattice evidence
- Exercise Set 3 (Seiberg duality verification) will need the anomaly coefficients from Exercise Set 1 Problem 3

## Next Phase Readiness

- Exercise Sets 1 and 2 complete and ready for student use
- UV anomaly coefficients available for Seiberg duality verification in Exercise Set 3
- Convention T(fund) = 1/2 verified within exercises (Problem 1(c) of Exercise Set 2)
- Phase 01-foundations Plan 03 complete; ready for next plan

## Self-Check: PASSED

- [x] exercises/exercise-01.tex exists and compiles (12 pages)
- [x] exercises/exercise-02.tex exists and compiles (11 pages)
- [x] Commit 54b5cd5 exists (Task 1)
- [x] Commit 21e9c32 exists (Task 2)
- [x] All numerical values verified by Python script
- [x] Convention A(fund)=1 used consistently (not T(fund))
- [x] Convention b_0 = (11N_c - 2N_f)/3 with N_f = Dirac throughout
- [x] Banks-Zaks formula matches Lecture 1 convention

---

_Phase: 01-foundations_
_Plan: 03_
_Completed: 2026-03-20_
