---
phase: 05-extensions
plan: 03
depth: full
one-liner: "Exercise Sets 7-8 complete: SO(10) anomaly matching (A_el = A_mag = -40/13), KS duality with k=1 recovery, s-confinement boundary, meson quantum numbers via Gell-Mann-Nishijima, GMOR verified m_pi = 140 MeV, mass hierarchy with geometric epsilon ~ 0.01"
subsystem: [derivation, paper-writing]
tags: [anomaly-matching, SO-duality, KS-duality, s-confinement, meson-quantum-numbers, GMOR, mass-hierarchy, exercises]

requires:
  - phase: 05-extensions/05-01
    provides: [Lecture 9 content on SO/Sp dualities, KS duality, s-confinement]
  - phase: 05-extensions/05-02
    provides: [Lecture 10 content on meson matrix, scalar-pseudoscalar distinction, GMOR, mass hierarchy]
provides:
  - "Exercise Set 7: 3 problems (65 marks) with complete worked solutions on SUSY duality extensions"
  - "Exercise Set 8: 3 problems (65 marks) with complete worked solutions on physical meson identification"
affects: [final-compilation, exam-preparation]

methods:
  added: [anomaly coefficient computation for SO(N) duality, Gell-Mann-Nishijima formula verification, GMOR numerical evaluation]
  patterns: [exercise-with-worked-solution structure from Exercise Sets 1-6, epistemic qualifier discipline for non-SUSY claims]

key-files:
  created:
    - exercises/exercise-07.tex
    - exercises/exercise-08.tex
  modified: []

key-decisions:
  - "SO(10) with N_f=13 chosen for Exercise 7.1 (inside conformal window 12 < 13 < 24; magnetic SO(7) gives non-trivial anomaly matching)"
  - "SU(4) with k=2, N_f=5 chosen for KS example (inside window 4 < 5 < 6; gives magnetic SU(6))"
  - "GMOR computation uses f_pi=92.1 MeV physical convention (not F_pi=65 MeV Gasser-Leutwyler)"
  - "Mass hierarchy framed as parametric consistency check with O(1) coefficients throughout"

patterns-established:
  - "Convention box at start of each exercise set matching preamble.tex ASSERT_CONVENTION"
  - "Epistemic qualifiers on all duality-dependent claims in exercise solutions"
  - "Mark allocations: 65 marks per set, 90 minutes suggested"

conventions:
  - "hbar = c = 1 (natural)"
  - "metric = (+,-,-,-)"
  - "T(vector SO(N)) = 1 (Intriligator-Seiberg)"
  - "T(fund Sp(N)) = 1/2"
  - "T(fund SU(N)) = 1/2"
  - "Sp(N_c) = rank N_c (IS convention)"
  - "PDG 2024 meson naming"
  - "f_pi = 92.1 MeV (physical convention)"

plan_contract_ref: ".gpd/phases/05-extensions/05-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-exercise-07:
      status: passed
      summary: "Exercise Set 7 contains 3 problems (30+20+15 marks) on SO anomaly matching, KS duality, and s-confinement, all with complete step-by-step worked solutions"
      linked_ids: [deliv-exercise-07, test-so-anomaly-exercise, test-ks-exercise, test-solutions-07, ref-is-9506101, ref-ks-9505004]
    claim-exercise-08:
      status: passed
      summary: "Exercise Set 8 contains 3 problems (25+20+20 marks) on meson quantum numbers, scalar-pseudoscalar distinction, and mass hierarchy, all with complete worked solutions"
      linked_ids: [deliv-exercise-08, test-quantum-number-exercise, test-mass-hierarchy-exercise, test-solutions-08, ref-pdg-2024, ref-sannino-2407]
  deliverables:
    deliv-exercise-07:
      status: passed
      path: "exercises/exercise-07.tex"
      summary: "Exercise Set 7 with ASSERT_CONVENTION line, SO(10) anomaly matching (2 coefficients computed and matched), KS duality with k=1 limit, s-confinement boundary table"
      linked_ids: [claim-exercise-07, test-so-anomaly-exercise, test-ks-exercise, test-solutions-07]
    deliv-exercise-08:
      status: passed
      path: "exercises/exercise-08.tex"
      summary: "Exercise Set 8 with ASSERT_CONVENTION line, 3x3 meson quantum number table with GMN verification, GMOR numerical check, VEV hierarchy mass ratios"
      linked_ids: [claim-exercise-08, test-quantum-number-exercise, test-mass-hierarchy-exercise, test-solutions-08]
  acceptance_tests:
    test-so-anomaly-exercise:
      status: passed
      summary: "Problem 1 computes SU(13)^2 U(1)_R anomaly coefficient on both electric (A=-40/13) and magnetic sides (A_q=-35/26, A_M=-45/26, total=-40/13), with general proof for arbitrary N_c, N_f"
      linked_ids: [claim-exercise-07, deliv-exercise-07, ref-is-9506101]
    test-ks-exercise:
      status: passed
      summary: "Problem 2 derives conformal window 3N_c/(k+1) < N_f < 3N_c/k, shows k=1 limit gives 3N_c/2 < N_f < 3N_c (Seiberg), and demonstrates adjoint mass term + meson reduction at k=1"
      linked_ids: [claim-exercise-07, deliv-exercise-07, ref-ks-9505004]
    test-solutions-07:
      status: passed
      summary: "All 3 problems in Exercise Set 7 have complete worked solutions with step-by-step derivations, not just final answers"
      linked_ids: [claim-exercise-07, deliv-exercise-07]
    test-quantum-number-exercise:
      status: passed
      summary: "Problem 1 assigns I, I_3, S, Q to all 6 off-diagonal mesons in the 3x3 block, verifies charges via both GMN formula and direct computation; extends to N_f=4 with D meson family"
      linked_ids: [claim-exercise-08, deliv-exercise-08, ref-pdg-2024]
    test-mass-hierarchy-exercise:
      status: passed
      summary: "Problem 3 connects VEV hierarchy to quark mass ratios (m_t/m_c~136, m_c/m_u~577, m_b/m_s~44, m_s/m_d~20), shows geometric epsilon~0.01 with O(1) coefficients provides parametric consistency"
      linked_ids: [claim-exercise-08, deliv-exercise-08, ref-sannino-2407, ref-pdg-2024]
    test-solutions-08:
      status: passed
      summary: "All 3 problems in Exercise Set 8 have complete worked solutions with step-by-step derivations"
      linked_ids: [claim-exercise-08, deliv-exercise-08]
  references:
    ref-is-9506101:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as source of SO/Sp duality maps and anomaly coefficients in Exercise 7.1 problem statement, solution, and bibliography"
    ref-ks-9505004:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as source of KS duality in Exercise 7.2 problem statement and bibliography"
    ref-pdg-2024:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for meson masses, quark quantum numbers, quark masses in Exercises 8.1-8.3; meson naming conventions follow PDG 2024"
    ref-sannino-2407:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for VEV hierarchy from Planck operators in Exercise 8.3 background and solution"
  forbidden_proxies:
    fp-answers-only:
      status: rejected
      notes: "All 6 problems have complete worked solutions with step-by-step derivations, explicit intermediate calculations, and verification checks"
    fp-trivial-exercises:
      status: rejected
      notes: "All problems require physical reasoning: anomaly computation (not lookup), GMN verification (not table reading), GMOR derivation (not plugging numbers), parametric analysis (not data retrieval)"
  uncertainty_markers:
    weakest_anchors:
      - "SO/Sp anomaly conventions: T(vector SO(N))=1 used consistently per IS 9509066, but differs from some references that use T=1/2"
      - "Mass hierarchy epsilon values depend on PDG running masses at mu=2 GeV; pole masses vs running masses give different ratios"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 9min
completed: 2026-03-20
---

# Plan 05-03: Exercise Sets 7-8 Summary

**Exercise Sets 7-8 complete: SO(10) anomaly matching (A_el = A_mag = -40/13), KS duality with k=1 recovery, s-confinement boundary, meson quantum numbers via Gell-Mann-Nishijima, GMOR verified m_pi = 140 MeV, mass hierarchy with geometric epsilon ~ 0.01**

## Performance

- **Duration:** 9 min
- **Started:** 2026-03-20T15:23:18Z
- **Completed:** 2026-03-20T15:32:16Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- SO(10)/SO(7) anomaly matching: A[SU(13)^2 U(1)_R] = -40/13 on both sides (general proof: A = -N_c(N_c-2)/(2N_f))
- KS conformal window 3N_c/(k+1) < N_f < 3N_c/k reduces to Seiberg window at k=1
- GMOR relation: m_pi = sqrt(8.5 * (270)^3 / (92.1)^2) MeV = 140 MeV, matching observed 139.6 MeV
- Geometric VEV hierarchy with epsilon ~ 0.01 and O(1) coefficients accommodates all quark mass ratios

## Task Commits

Each task was committed atomically:

1. **Task 1: Exercise Set 7 -- SUSY Duality Extensions** - `1f27193` (document)
2. **Task 2: Exercise Set 8 -- Physical Meson Identification** - `cff07b2` (document)

## Files Created/Modified

- `exercises/exercise-07.tex` - Exercise Set 7: SO anomaly matching, KS duality, s-confinement (3 problems, 65 marks, complete solutions)
- `exercises/exercise-08.tex` - Exercise Set 8: Meson quantum numbers, scalar-pseudoscalar distinction, mass hierarchy (3 problems, 65 marks, complete solutions)

## Next Phase Readiness

- Exercise Sets 1-8 now provide complete examination-style problem coverage for Lectures 1-10
- All exercises have complete worked solutions suitable for Part III exam preparation
- Convention consistency maintained across all 8 exercise sets and 10 lectures

## Contract Coverage

- Claim IDs advanced: claim-exercise-07 -> passed, claim-exercise-08 -> passed
- Deliverable IDs produced: deliv-exercise-07 -> exercises/exercise-07.tex, deliv-exercise-08 -> exercises/exercise-08.tex
- Acceptance test IDs run: test-so-anomaly-exercise -> passed, test-ks-exercise -> passed, test-solutions-07 -> passed, test-quantum-number-exercise -> passed, test-mass-hierarchy-exercise -> passed, test-solutions-08 -> passed
- Reference IDs surfaced: ref-is-9506101 -> cited, ref-ks-9505004 -> cited, ref-pdg-2024 -> cited, ref-sannino-2407 -> cited
- Forbidden proxies rejected: fp-answers-only -> rejected (all solutions complete), fp-trivial-exercises -> rejected (all require reasoning)

## Equations Derived

**Eq. (05-03.1):** SO(N_c) electric-side anomaly coefficient

$$\mathcal{A}^{\text{el}}[\text{SU}(N_f)^2 \text{U}(1)_R] = -\frac{N_c(N_c - 2)}{2N_f}$$

**Eq. (05-03.2):** KS conformal window

$$\frac{3N_c}{k+1} < N_f < \frac{3N_c}{k}$$

**Eq. (05-03.3):** GMOR relation (numerical)

$$m_\pi = \sqrt{\frac{(m_u + m_d)|\langle\bar{q}q\rangle|}{f_\pi^2}} \approx 140\;\text{MeV}$$

## Validations Completed

- SO(10) anomaly matching: A_el = -40/13 = A_mag (numerical verification)
- General anomaly matching proof: algebraic cancellation yields A_mag = -N_c(N_c-2)/(2N_f) for all N_c, N_f
- KS at k=1: conformal window, gauge group, meson content, superpotential all reduce to Seiberg duality
- Meson charges: all 6 off-diagonal mesons verified via both GMN formula and direct Q(q)-Q(qbar)
- GMOR: m_pi = 140 MeV vs observed 139.6 MeV (< 1% agreement)
- LaTeX compilation: 0 errors for both exercise files

## Decisions & Deviations

None - plan executed exactly as written. The SO(10)/N_f=13 example and SU(4)/k=2/N_f=5 example were pre-specified in the plan (after the plan's own corrections).

## Open Questions

- The light scalar meson spectrum (f_0(500), a_0(980)) interpretation as qqbar vs tetraquark vs molecular states remains debated (noted in Exercise 8.2 solution)
- The geometric VEV hierarchy parameter epsilon varies by a factor ~30 across sectors (0.002 to 0.05); the framework accommodates this via O(1) coefficients but does not explain why the ratios differ

## Self-Check: PASSED

- [x] exercises/exercise-07.tex exists (29656 bytes)
- [x] exercises/exercise-08.tex exists (32463 bytes)
- [x] Commit 1f27193 exists (Task 1)
- [x] Commit cff07b2 exists (Task 2)
- [x] GMOR numerical result: m_pi = 140 MeV (matches 139.6 observed)
- [x] Both files compile with 0 LaTeX errors
- [x] ASSERT_CONVENTION lines match preamble.tex in both files
- [x] All 6 problems have complete worked solutions
- [x] Convention consistency across all outputs verified

---

_Phase: 05-extensions_
_Plan: 03_
_Completed: 2026-03-20_
