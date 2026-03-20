---
phase: 04-the-dualised-standard-model
plan: 02
depth: full
one-liner: "VALD-01: all 6 SU(3)_c x SU(2)_L x U(1)_Y anomaly coefficients verified symbolically to match between electric and magnetic dualised SM (0 = 0 as polynomial identities in n_g), with SM anomaly cancellation recovered as subset"
subsystem: [validation]
tags: [anomaly-matching, seiberg-duality, non-susy-duality, gauge-anomaly, sympy]

requires:
  - phase: 04-the-dualised-standard-model
    provides: [Lecture 7 field content tables, hypercharge formula Y = T_R^3 + Q_V/6, anomaly matching derivation]
  - phase: 02-susy-and-seiberg-duality
    provides: [VALD-02 anomaly matching script pattern, convention lock]
provides:
  - VALD-01 script: symbolic + numerical verification of all 6 SM anomaly conditions for dualised SM
  - Confirmation that magnetic theory anomaly cancellation is vector-like (0 for all conditions)
  - Confirmation that electric theory anomaly cancellation follows by factorisation through SU(N)_el
  - SM anomaly cancellation recovered as subset when extra magnetic states removed
affects: [04-03, 04-04, 04-05]

methods:
  added: [vector-like anomaly cancellation, factorisation through electric gauge group, SU(2)_R pairing argument for mesino]
  patterns: [VALD-XX script pattern with symbolic + numerical + subset checks]

key-files:
  created: [scripts/verify_sm_anomaly_matching.py]

key-decisions:
  - "Electric theory anomaly computed via factorisation: each electric fermion has SM quantum numbers identical to corresponding magnetic fermion, multiplied by dim(R_SU(N)_el)"
  - "Mesino decomposition: M in (F, F-bar) of SU(N_f)_L x SU(N_f)_R with Q_V = 0 gives SU(2)_L doublets with Y = +/-1/2 (from T_R^3), which cancel pairwise in all anomaly coefficients"
  - "SM subset check uses all-left-handed Weyl convention: u_R^c = (3-bar, 1, -2/3) etc., identifying SM right-handed fields with q-tilde/l-tilde components from the magnetic theory"

patterns-established:
  - "VALD script pattern: 6-part structure (magnetic, electric, matching, numerical, SM subset, extra spot-checks)"

conventions:
  - "hbar = c = 1 (natural units)"
  - "metric = (+,-,-,-) (mostly minus)"
  - "T(fund) = 1/2 per Weyl fermion"
  - "A(fund) = 1, A(antifund) = -1"
  - "Y = T_R^3 + Q_V/6 (Cacciapaglia-Sannino 2407.17281 Eq. 6)"

plan_contract_ref: ".gpd/phases/04-the-dualised-standard-model/04-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-vald01-anomaly:
      status: passed
      summary: "All 6 independent anomaly coefficients for SU(3)_c x SU(2)_L x U(1)_Y verified to match between electric and magnetic theories as polynomial identities in n_g (all give 0 = 0). Confirmed by symbolic SymPy computation and numerical spot-checks at n_g = 3, 4, 5, 6."
      linked_ids: [deliv-anomaly-script, test-symbolic-match, test-numerical-match, test-sm-subset, ref-sannino-2407, ref-sannino-1102]
      evidence:
        - verifier: gpd-executor
          method: symbolic computation + numerical spot-check
          confidence: high
          claim_id: claim-vald01-anomaly
          deliverable_id: deliv-anomaly-script
          acceptance_test_id: test-symbolic-match
          reference_id: ref-sannino-2407
  deliverables:
    deliv-anomaly-script:
      status: passed
      path: "scripts/verify_sm_anomaly_matching.py"
      summary: "625-line SymPy script computing all 6 anomaly conditions on both electric and magnetic sides, with numerical spot-checks and SM subset recovery. Exits with code 0."
      linked_ids: [claim-vald01-anomaly, test-symbolic-match, test-numerical-match, test-sm-subset]
  acceptance_tests:
    test-symbolic-match:
      status: passed
      summary: "All 6 anomaly conditions computed symbolically as functions of n_g; electric - magnetic = 0 verified by sympy.simplify for each condition as a polynomial identity."
      linked_ids: [claim-vald01-anomaly, deliv-anomaly-script, ref-sannino-2407]
    test-numerical-match:
      status: passed
      summary: "All 6 conditions evaluated numerically at n_g = 3 (physical SM): all give exact integer 0. Additional spot-checks at n_g = 4, 5, 6 also pass."
      linked_ids: [claim-vald01-anomaly, deliv-anomaly-script]
    test-sm-subset:
      status: passed
      summary: "After removing vector-like partners, gaugino, and mesino from magnetic theory, the remaining SM content (q_L, utilde_R = u_R^c, dtilde_R = d_R^c, ell_L, etilde_R = e_R^c, nutilde_R = nu_R^c) satisfies standard SM anomaly cancellation (all 6 conditions vanish) in the all-left-handed Weyl convention."
      linked_ids: [claim-vald01-anomaly, deliv-anomaly-script]
  references:
    ref-sannino-2407:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Field content from Tables I-II of Cacciapaglia-Sannino 2407.17281 used as ground truth for magnetic and electric quantum numbers. Hypercharge formula Y = T_R^3 + Q_V/6 from their Eq. 6."
    ref-sannino-1102:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Electric theory field content from Sannino 1102.5100 consistent with 2407.17281 Tables. Generation bound n_g >= 3 from 2n_g - 4 >= 2."
  forbidden_proxies:
    fp-numerical-only:
      status: rejected
      notes: "Symbolic verification performed as polynomial identities in n_g, not just numerical checks. The symbolic computation establishes the result for ALL n_g >= 3, not just specific values."
  uncertainty_markers:
    weakest_anchors:
      - "The field content is taken from 2407.17281 Tables I-II as transcribed in Lecture 7. Any transcription error would propagate."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-vald01-anomaly
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-sannino-2407
    comparison_kind: benchmark
    metric: exact_match
    threshold: "all 6 conditions give 0 = 0"
    verdict: pass
    recommended_action: "No further action needed. Result is exact."
    notes: "Both electric and magnetic anomaly coefficients vanish individually as polynomial identities in n_g, confirming the vector-like structure argument of Lecture 7."

duration: 15min
completed: 2026-03-20
---

# Plan 04-02: VALD-01 SM Anomaly Matching Verification Summary

**All 6 SU(3)_c x SU(2)_L x U(1)_Y anomaly coefficients verified symbolically to match between electric and magnetic dualised SM (0 = 0 as polynomial identities in n_g), with SM anomaly cancellation recovered as subset check**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-03-20
- **Completed:** 2026-03-20
- **Tasks:** 1
- **Files created:** 1

## Key Results

- All 6 anomaly conditions (SU(3)^3, SU(2)^3, SU(3)^2 U(1)_Y, SU(2)^2 U(1)_Y, U(1)_Y^3, U(1)_Y-grav) vanish on BOTH electric and magnetic sides as polynomial identities in n_g [CONFIDENCE: HIGH]
- Anomaly matching is 0 = 0 for all conditions -- the vector-like structure of the magnetic theory ensures every coefficient vanishes independently [CONFIDENCE: HIGH]
- SM anomaly cancellation recovered when extracting SM-only content (q_L, u_R^c, d_R^c, ell_L, e_R^c, nu_R^c) from the magnetic spectrum [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Write VALD-01 SM anomaly matching verification script** - `1d16be5` (validate)

## Files Created/Modified

- `scripts/verify_sm_anomaly_matching.py` - VALD-01: symbolic + numerical verification of all 6 SM anomaly conditions for the dualised SM

## Next Phase Readiness

- VALD-01 complete: anomaly matching for SU(3)_c x SU(2)_L x U(1)_Y verified computationally
- Script available as reference for any future anomaly checks in the dualised SM framework
- Ready for plans 04-03 through 04-05

## Contract Coverage

- Claim IDs advanced: claim-vald01-anomaly -> passed
- Deliverable IDs produced: deliv-anomaly-script -> scripts/verify_sm_anomaly_matching.py (passed)
- Acceptance test IDs run: test-symbolic-match (passed), test-numerical-match (passed), test-sm-subset (passed)
- Reference IDs surfaced: ref-sannino-2407 (read, compare), ref-sannino-1102 (read, compare)
- Forbidden proxies rejected: fp-numerical-only (rejected -- symbolic verification performed)
- Decisive comparison verdicts: claim-vald01-anomaly -> pass (exact match, all 6 conditions)

## Validations Completed

- **Symbolic verification:** All 6 anomaly conditions computed as functions of n_g using SymPy; electric - magnetic = 0 verified by simplify() for each condition
- **Numerical spot-checks:** n_g = 3 (physical SM), 4, 5, 6 all give exact integer 0 for all conditions
- **SM subset check:** Standard SM anomaly cancellation recovered in all-left-handed Weyl convention when extra magnetic states removed
- **Convention consistency:** ASSERT_CONVENTION line in script matches project convention lock; hypercharge formula Y = T_R^3 + Q_V/6 verified against all 6 SM field hypercharges

## Decisions & Deviations

### Decisions Made

- **SM subset convention:** Used all-left-handed Weyl convention for SM subset check, identifying SM right-handed fields (u_R, d_R, e_R) with the charge conjugates of q-tilde/l-tilde components (utilde_R, dtilde_R, etilde_R). This is the standard textbook convention for SM anomaly cancellation.
- **Mesino decomposition:** Decomposed M as (F, F-bar) under SU(N_f)_L x SU(N_f)_R into n_g^2 copies of SU(2)_L doublets with Y = +/-1/2 (from T_R^3). The SU(2)_R pairing ensures all anomaly contributions cancel.
- **Electric theory factorisation:** Rather than performing an independent Pati-Salam decomposition of electric fermions, used the Lecture 7 factorisation argument: A_el = dim(R_SU(N)_el) * A_SM. This gives the same result but is more transparent.

### Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

- **SM subset chirality:** Initial implementation listed SM-only quarks u_R, d_R with the quantum numbers from the magnetic theory table (3, 1, +2/3) and (3, 1, -1/3), which does not give standard SM anomaly cancellation. Corrected by using the all-left-handed convention with utilde_R = (3-bar, 1, -2/3) = SM u_R^c and dtilde_R = (3-bar, 1, +1/3) = SM d_R^c. This matches the physical identification that the SM right-handed quarks correspond to q-tilde components, not q components, when expressed as left-handed Weyl fermions.

## Open Questions

- None. The anomaly matching is an exact group-theoretic result that is insensitive to dynamics.

---

_Phase: 04-the-dualised-standard-model_
_Completed: 2026-03-20_
