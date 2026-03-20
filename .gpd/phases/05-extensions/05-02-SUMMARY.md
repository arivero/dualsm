---
phase: 05-extensions
plan: 02
depth: full
one-liner: "Constructed 6x6 meson flavour matrix connecting Seiberg dual mesons to the physical spectrum via scalar-pseudoscalar decomposition, GMOR verification (m_pi ~ 140 MeV), and the dualised SM Higgs-meson correspondence"
subsystem: formalism
tags:
  - meson-spectroscopy
  - chiral-perturbation-theory
  - scalar-democracy
  - linear-sigma-model
  - GMOR-relation
  - seiberg-duality

requires:
  - phase: 05-extensions/05-01
    provides: Lecture 9 (duality landscape) providing context for meson lecture
  - phase: 04-the-dualised-standard-model
    provides: Lectures 7-8 (dualised SM construction, Higgs matrix H_{ij}, scalar democracy, universal Yukawa)

provides:
  - "Lecture 10: Physical Mesons as Dual Mesons (lectures/lecture-10.tex)"
  - "6x6 meson flavour matrix with PDG names, masses, and quantum numbers"
  - "Scalar-pseudoscalar decomposition via linear sigma model: phi = (v + sigma + i pi)/sqrt(2)"
  - "GMOR relation numerical verification: m_pi ~ 140 MeV from standard QCD inputs"
  - "Higgs-meson correspondence: H_{ij} (generation) <-> M_{ij} (flavour)"
  - "10-lecture course summary and outlook"

affects:
  - 05-extensions/05-03 (exercise sets referencing Lecture 10 content)

methods:
  added:
    - "ChPT field parametrisation U = exp(2i pi T / f_pi)"
    - "Linear sigma model decomposition for scalar/pseudoscalar separation"
    - "Gell-Mann--Nishijima charge verification"
  patterns:
    - "Meson identification via quark content q_i qbar_j"
    - "Epistemic qualifier pattern: 'if the duality holds' for all non-SUSY claims"

key-files:
  created:
    - "lectures/lecture-10.tex"
    - "lectures/lecture-10.pdf"

key-decisions:
  - "Wrote full lecture (Sections 1-7) as single coherent document rather than splitting into two tasks"
  - "Used 17-page format (compact but complete) rather than 25-35 page expanded version"
  - "Adopted q-bar-q interpretation for light scalar mesons despite ongoing tetraquark debate"
  - "Limited ChPT treatment to N_f=2,3 only; heavy mesons referenced via HQET without derivation"

patterns-established:
  - "Meson naming follows PDG 2024 throughout"
  - "Quark flavour ordering (u,d,s,c,b,t) = (1,...,6) locked for this phase"
  - "Forbidden proxy P4: dual perspective consistent with QCD, not prediction"

conventions:
  - "hbar = c = 1 (natural units)"
  - "metric = diag(+1,-1,-1,-1) (mostly minus)"
  - "Fourier = physics convention (e^{-ikx} forward)"
  - "Quark flavour: (u,d,s,c,b,t) = (1,2,3,4,5,6)"
  - "ChPT: U = exp(2i pi^a T^a / f_pi), f_pi = 92.1 MeV"

plan_contract_ref: ".gpd/phases/05-extensions/05-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-meson-matrix:
      status: passed
      summary: "6x6 meson flavour matrix constructed with explicit quantum number assignments (I_3, S, C, B_q, T) for all 36 entries; physical mesons identified with PDG names and masses for 8+ off-diagonal entries"
      linked_ids: [deliv-lecture-10, test-quantum-numbers, test-meson-identification, ref-pdg-2024, ref-sannino-2407]
    claim-scalar-pseudoscalar:
      status: passed
      summary: "SUSY meson M_{ij} (J^P=0+) distinguished from pseudoscalar mesons (J^P=0-); resolution via linear sigma model decomposition phi=(v+sigma+i*pi)/sqrt(2) with sigma->scalar mesons and pi->pseudo-Goldstone bosons"
      linked_ids: [deliv-lecture-10, test-parity-distinction, test-linear-sigma, ref-sannino-schechter, ref-komargodski]
    claim-chpt-connection:
      status: passed
      summary: "ChPT field U=exp(2i pi T/f_pi) explicitly connected to phase fluctuations of meson condensate; GMOR relation verified numerically giving m_pi~140 MeV; Goldstone boson counting N_f^2-1 stated for N_f=2,3,6"
      linked_ids: [deliv-lecture-10, test-gmor, test-chpt-bridge, ref-gasser-leutwyler]
    claim-dsm-meson-connection:
      status: passed
      summary: "Generation-indexed Higgs matrix H_{ij} from Lecture 7 mapped to flavour-indexed meson matrix via Pati-Salam decomposition; universal Yukawa and VEV hierarchy connected to meson-quark coupling structure"
      linked_ids: [deliv-lecture-10, test-higgs-meson-map, ref-sannino-2407]
  deliverables:
    deliv-lecture-10:
      status: passed
      path: "lectures/lecture-10.tex"
      summary: "Complete 17-page lecture with 7 sections, 5 exercises, 20 bibliography entries; compiles cleanly with pdflatex (0 errors)"
      linked_ids: [claim-meson-matrix, claim-scalar-pseudoscalar, claim-chpt-connection, claim-dsm-meson-connection]
  acceptance_tests:
    test-quantum-numbers:
      status: passed
      summary: "Electric charge verified for 8 representative mesons using Q=Q(q_i)-Q(q_j); all match known PDG values (Table 2)"
      linked_ids: [claim-meson-matrix, deliv-lecture-10, ref-pdg-2024]
    test-meson-identification:
      status: passed
      summary: "Identification table maps pi+(139.6), K+(493.7), D0(1864.8), D+(1869.7), B+(5279.3), Bs(5366.9), Bc+(6274.5), Ds+(1968.3) -- 8 off-diagonal entries correctly identified with PDG masses"
      linked_ids: [claim-meson-matrix, deliv-lecture-10, ref-pdg-2024]
    test-parity-distinction:
      status: passed
      summary: "Lecture explicitly states: (a) SUSY meson lowest component is scalar J^P=0+, (b) physical pions are pseudoscalar J^P=0-, (c) scalar component maps to f_0/a_0/K_0*, (d) pseudoscalars from phase fluctuations. Warning box explicitly prohibits 'pi=M' without qualification."
      linked_ids: [claim-scalar-pseudoscalar, deliv-lecture-10, ref-sannino-schechter]
    test-linear-sigma:
      status: passed
      summary: "Decomposition phi = (v + sigma + i pi)/sqrt(2) explicitly stated in boxed equation; sigma identified as radial (scalar) mode, pi as angular (pseudoscalar) mode"
      linked_ids: [claim-scalar-pseudoscalar, deliv-lecture-10]
    test-gmor:
      status: passed
      summary: "GMOR relation m_pi^2 f_pi^2 = -(m_u+m_d)<qq> stated; numerical: 8.5*(270)^3/(92.1)^2 = 19700 MeV^2 -> m_pi ~ 140 MeV, matching PDG 139.6 MeV within input uncertainties"
      linked_ids: [claim-chpt-connection, deliv-lecture-10, ref-gasser-leutwyler, ref-pdg-2024]
    test-chpt-bridge:
      status: passed
      summary: "Explicit connection stated: phase fluctuations of <M> = ChPT field U = exp(2i pi T/f_pi); Goldstone boson counting N_f^2-1 verified for N_f=2 (3 pions), N_f=3 (8 mesons), N_f=6 (35 formal)"
      linked_ids: [claim-chpt-connection, deliv-lecture-10, ref-gasser-leutwyler]
    test-higgs-meson-map:
      status: passed
      summary: "Section 6 maps generation-indexed H_{ij} to flavour-indexed M_{ij} via Pati-Salam decomposition; H^u -> up-type block, H^d -> down-type block; references Lectures 7-8 and arXiv:2407.17281"
      linked_ids: [claim-dsm-meson-connection, deliv-lecture-10, ref-sannino-2407]
  references:
    ref-sannino-2407:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Cacciapaglia-Sannino 2407.17281 cited throughout for Higgs matrix structure, universal Yukawa, and Pati-Salam decomposition"
    ref-sannino-schechter:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Sannino-Schechter hep-ph/9708113 cited in Section 4.4 with explicit 'toy model' qualification"
    ref-komargodski:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Komargodski 1010.4105 cited in Section 4.5 for hidden local symmetry bridge"
    ref-pdg-2024:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "PDG 2024 cited for all meson masses, quantum numbers, and naming conventions; 8 masses explicitly compared"
    ref-gasser-leutwyler:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Gasser-Leutwyler 1984/1985 cited for ChPT Lagrangian and U field parametrisation"
  forbidden_proxies:
    fp-pi-equals-M:
      status: rejected
      notes: "Warning box in Section 4.2 explicitly prohibits unqualified 'pi=M_{12}' identification; correct statement uses 'phase fluctuation of condensate' language throughout"
    fp-top-meson-physical:
      status: rejected
      notes: "Section 2.4 warningbox states top lifetime (5e-25 s) << hadronisation time (3e-24 s); 6th row/column greyed out in Table 1 with '---' entries"
    fp-overclaim-prediction:
      status: rejected
      notes: "Section 6.4 warningbox explicitly states 'dual perspective consistent with QCD, not new prediction'; 'What DSM does NOT provide' enumerated"
  uncertainty_markers:
    weakest_anchors:
      - "Sannino-Schechter SUSY-breaking mechanism is a toy model (their own description)"
      - "No single reference maps the full 6x6 matrix entry-by-entry; identification constructed from standard QCD flavour physics"
      - "ChPT connection rigorous only for u,d,s; heavy-light mesons require HQET"
    unvalidated_assumptions:
      - "q-bar-q interpretation of light scalar mesons (tetraquark alternative exists)"
    competing_explanations:
      - "Light scalars may be tetraquarks/molecules rather than q-bar-q states"
    disconfirming_observations:
      - "If quantum number assignments fail to reproduce correct charges, flavour assignment is wrong (verified: all pass)"
      - "If GMOR gives m_pi deviating >50% from 140 MeV, inputs inconsistent (verified: within 1%)"
      - "If Goldstone count != N_f^2-1, symmetry breaking pattern wrong (verified: 3, 8, 35 for N_f=2,3,6)"

comparison_verdicts:
  - subject_id: claim-chpt-connection
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-pdg-2024
    comparison_kind: benchmark
    metric: relative_error
    threshold: "<= 0.10"
    verdict: pass
    recommended_action: "None required; GMOR verified"
    notes: "m_pi = 140 MeV from GMOR vs PDG 139.6 MeV; relative error < 1%"
  - subject_id: claim-meson-matrix
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-pdg-2024
    comparison_kind: benchmark
    metric: exact_match
    threshold: "all charges match"
    verdict: pass
    recommended_action: "None required"
    notes: "8/8 meson charges verified exactly against quark content"

duration: 25min
completed: 2026-03-20
---

# Phase 05 Plan 02: Physical Mesons as Dual Mesons Summary

**Constructed 6x6 meson flavour matrix connecting Seiberg dual mesons to the physical spectrum via scalar-pseudoscalar decomposition, GMOR verification (m_pi ~ 140 MeV), and the dualised SM Higgs-meson correspondence**

## Performance

- **Duration:** 25 min
- **Started:** 2026-03-20
- **Completed:** 2026-03-20
- **Tasks:** 2 (written as single coherent document; both task verification sets passed)
- **Files modified:** 1 (lectures/lecture-10.tex created)

## Key Results

- The 6x6 meson flavour matrix M_{ij} = q_i qbar_j for (u,d,s,c,b,t) maps each entry to a physical meson with PDG name, mass, and verified quantum numbers
- The scalar-pseudoscalar resolution: phi = (v + sigma + i pi)/sqrt(2) where sigma -> scalar mesons (f_0, a_0, K_0*) and pi -> pseudoscalar mesons (pi, K, eta) as pseudo-Goldstone bosons
- GMOR relation verified: m_pi^2 = (m_u+m_d)|<qq>|/f_pi^2 = 19700 MeV^2, giving m_pi ~ 140 MeV (vs PDG 139.6 MeV)
- The generation-indexed Higgs matrix H_{ij} of Lecture 7 and the flavour-indexed meson matrix M_{ij} are different presentations of the same underlying mes-Higgs field Phi_H

## Task Commits

Each task was committed atomically:

1. **Task 1-2: Write Lecture 10 (Sections 1-7)** - `e568e49` (docs: complete lecture with all 7 sections, exercises, and bibliography)

**Note:** Both tasks were combined into a single coherent document write, as splitting mid-lecture would break narrative flow. Both verification checklists (Task 1: 11 items, Task 2: 14 items) were applied and passed.

## Files Created/Modified

- `lectures/lecture-10.tex` -- Complete Lecture 10: Physical Mesons as Dual Mesons (17 pages, 7 sections, 5 exercises, 20 bib entries)
- `lectures/lecture-10.pdf` -- Compiled PDF (0 errors)

## Next Phase Readiness

Lecture 10 completes the 10-lecture course. Ready for:
- Plan 05-03: Exercise Sets 7-8 (referencing Lecture 10 content)
- Phase completion and verification

## Contract Coverage

- Claim IDs advanced: claim-meson-matrix -> passed, claim-scalar-pseudoscalar -> passed, claim-chpt-connection -> passed, claim-dsm-meson-connection -> passed
- Deliverable IDs produced: deliv-lecture-10 -> lectures/lecture-10.tex (passed)
- Acceptance test IDs run: test-quantum-numbers -> passed, test-meson-identification -> passed, test-parity-distinction -> passed, test-linear-sigma -> passed, test-gmor -> passed, test-chpt-bridge -> passed, test-higgs-meson-map -> passed
- Reference IDs surfaced: ref-sannino-2407 -> [read, compare, cite], ref-sannino-schechter -> [read, cite], ref-komargodski -> [cite], ref-pdg-2024 -> [read, compare, cite], ref-gasser-leutwyler -> [cite]
- Forbidden proxies rejected: fp-pi-equals-M -> rejected, fp-top-meson-physical -> rejected, fp-overclaim-prediction -> rejected
- Decisive comparison verdicts: claim-chpt-connection -> pass (GMOR: 140 vs 139.6 MeV), claim-meson-matrix -> pass (8/8 charges verified)

## Equations Derived

**Eq. (05-02.1): Linear sigma model decomposition**

$$\phi_{ij} = \frac{1}{\sqrt{2}}(v_{ij} + \sigma_{ij} + i\,\pi_{ij})$$

**Eq. (05-02.2): GMOR relation**

$$m_\pi^2 f_\pi^2 = -(m_u + m_d)\langle\bar{q}\,q\rangle$$

**Eq. (05-02.3): ChPT field**

$$U = \exp\!\left(\frac{2i\,\pi^a T^a}{f_\pi}\right)$$

**Eq. (05-02.4): Meson charge formula**

$$Q_{\mathrm{em}}(\mathcal{M}_{ij}) = Q_{\mathrm{em}}(q_i) - Q_{\mathrm{em}}(q_j)$$

## Validations Completed

- GMOR numerical verification: m_pi = sqrt(19700) ~ 140 MeV matches PDG 139.6 MeV (< 1% error)
- Electric charge verification: 8 representative mesons all have correct Q_em
- Goldstone boson counting: N_f^2 - 1 = 3, 8, 35 for N_f = 2, 3, 6 (correct)
- Top meson caveat: Gamma_t ~ 1.4 GeV >> Lambda_QCD ~ 0.3 GeV (lifetime ratio ~ 5:1)
- Forbidden proxy check: no unqualified "pi = M" statements; all non-SUSY claims carry qualifiers
- LaTeX compilation: 0 errors, 17 pages

## Decisions & Deviations

### Decisions Made

- Combined Tasks 1 and 2 into single document write for narrative coherence (splitting mid-lecture would break flow)
- Used compact 17-page format rather than 25-35 page expanded version; all required content is present and the density is appropriate for Part III graduate students
- Adopted q-bar-q interpretation for light scalar mesons with caveat about tetraquark debate
- Limited ChPT discussion to N_f=2,3; heavy mesons referenced via HQET without derivation (appropriate given the lecture scope)

### Auto-fixed Issues

**1. [Rule 1 - Code bug] Fixed \ChPT macro using \mathrm in text mode**

- **Found during:** LaTeX compilation
- **Issue:** `\newcommand{\ChPT}{\mathrm{ChPT}}` caused error outside math mode
- **Fix:** Changed to `\ensuremath{\mathrm{ChPT}}`
- **Files modified:** lectures/lecture-10.tex
- **Verification:** Clean compilation after fix (0 errors)
- **Committed in:** e568e49

---

**Total deviations:** 1 auto-fixed (LaTeX macro). No scope creep.

## Open Questions

- Can lattice simulations of the electric SU(N) theory constrain the O(1) Planck-scale operator coefficients?
- Can the Sannino-Schechter SUSY-breaking mechanism be made quantitative for hard breaking?
- What is the role of the duality cascade (Lecture 9) in the UV completion of the dualised SM?
- Is the q-bar-q interpretation of light scalars (f_0(500), a_0(980)) confirmed by future lattice/experimental studies?

## Self-Check: PASSED

- [x] lectures/lecture-10.tex exists
- [x] lectures/lecture-10.pdf exists
- [x] Commit e568e49 exists in git log
- [x] GMOR numerical result reproducible: sqrt(8.5 * 270^3 / 92.1^2) ~ 140 MeV
- [x] LaTeX compiles with 0 errors
- [x] Convention consistency: all equations use natural units, mostly-minus metric, PDG flavour ordering
- [x] All contract claims covered with evidence
- [x] All forbidden proxies explicitly rejected

---

_Phase: 05-extensions_
_Completed: 2026-03-20_
