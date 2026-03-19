# Requirements: The Dualised Standard Model — Part III Lecture Notes

**Defined:** 2026-03-20
**Core Research Question:** Can the dualised Standard Model program be presented as a self-contained Part III half-course that builds duality machinery and produces parametric IR matching of the SM spectrum?

## Primary Requirements

### Lecture Content

- [ ] **LECT-01**: Write Lecture 1 — Anomaly matching review and conformal window (quick review building on Michaelmas QFT; fix conventions T(fund)=1/2, Weyl counting; detailed calculations moved to exercises)
- [ ] **LECT-02**: Write Lecture 2 — Minimal N=1 SUSY introduction (superfields, superpotential, F/D-terms, non-renormalisation theorem, holomorphy)
- [ ] **LECT-03**: Write Lecture 3 — Seiberg duality for N=1 SQCD (electric-magnetic duality, conformal window, evidence, moduli space matching)
- [ ] **LECT-04**: Write Lecture 4 — N=2 SUSY and breaking mechanisms (Fayet-Iliopoulos mechanism, Seiberg-Witten theory essentials, Argyres-Plesser-Seiberg N=2→N=1 deformations, origin of magnetic degrees of freedom)
- [ ] **LECT-05**: Write Lecture 5 — Tumbling and complementarity (Raby-Dimopoulos-Susskind, MAC criterion, complementarity principle, condensation patterns)
- [ ] **LECT-06**: Write Lecture 6 — Non-SUSY extensions of duality (Sannino-Schechter 1997, Maekawa's dual SUSY SM, Pati-Salam embedding, emergent SUSY)
- [ ] **LECT-07**: Write Lecture 7 — The dualised Standard Model (Cacciapaglia-Sannino 2024 construction, electric theory, magnetic dual, duality map, anomaly matching for full SM gauge group)
- [ ] **LECT-08**: Write Lecture 8 — Spectrum, scales, and outlook (parametric fermion mass hierarchy from operator dimensions, Fermi scale and QCD scale matching, flavour structure, open problems, comparison with other BSM approaches)

### Exercises

- [ ] **EXER-01**: Anomaly matching exercises — 't Hooft anomaly matching for SU(N) with fundamental and antisymmetric representations; verify anomaly coefficients match between electric and magnetic descriptions (moved from Lecture 1)
- [ ] **EXER-02**: Conformal window exercises — compute conformal window boundaries for SU(3) with N_f flavours; Banks-Zaks fixed point; loss of asymptotic freedom (moved from Lecture 1)
- [ ] **EXER-03**: Seiberg duality verification exercises — moduli space matching, 't Hooft anomaly verification for SQCD, deformation by mass terms
- [ ] **EXER-04**: N=2 → N=1 deformation exercise — worked example of mass deformation breaking N=2 to N=1, emergence of magnetic quarks
- [ ] **EXER-05**: Full SM spectrum exercise — derive parametric fermion mass hierarchies from Planck-scale four-fermion operators in the dualised SM; show consistency with m_t >> m_b >> m_e hierarchy
- [ ] **EXER-06**: Scale matching exercise — extract Fermi scale v ~ 246 GeV and QCD scale Lambda_QCD ~ 200 MeV from dual theory parameters; show parametric consistency with physical values

### Validation

- [ ] **VALD-01**: Verify all anomaly coefficients match between electric and magnetic descriptions for the full SM gauge group SU(3)_c x SU(2)_L x U(1)_Y
- [ ] **VALD-02**: Verify Seiberg duality results in lectures reproduce known results from Seiberg hep-th/9411149
- [ ] **VALD-03**: Verify parametric spectrum is consistent with physical fermion mass hierarchy (m_t : m_b : m_tau : m_c : ... ratios)
- [ ] **VALD-04**: Verify all conventions are internally consistent throughout notes (T(fund)=1/2, Weyl fermion counting, metric signature)
- [ ] **VALD-05**: Cross-check dualised SM construction against Sannino 2407.17281

### Reference Corpus

- [ ] **REFS-01**: Download and organize all must-read papers from 2407.17281 reference list into ./sources/
- [ ] **REFS-02**: Include Maekawa's 3 foundational papers (hep-ph/9510426, Prog. Theor. Phys. 95 943, Prog. Theor. Phys. 96 979)
- [ ] **REFS-03**: Include Sannino-Schechter hep-th/9708113 and Fayet's N=2 breaking papers
- [ ] **REFS-04**: Include Csaki-Terning 1106.3074 and Seiberg hep-th/9411149

## Follow-up Requirements

### Extended Analysis

- **EXTD-01**: Add optional Lecture 9-10 on collider signatures and GUT extensions if course extends
- **EXTD-02**: Include lattice evidence for near-conformal dynamics (SU(3) with N_f=8)
- **EXTD-03**: Connect to composite Higgs models and partial compositeness

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Full SUSY lecture course | Only minimal N=1 and N=2 essentials needed for duality |
| BSM phenomenology beyond dualised SM | Different lecture course |
| Lattice calculations | Computational project, not textbook |
| Cosmological implications | Beyond half-course scope |
| Chan-Tsou "Dualized Standard Model" | Completely different program; disambiguate in introduction only |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| LECT-01–08 | Internally consistent, no sign errors | Convention check + cross-reference with source papers |
| EXER-01–02 | Exact anomaly coefficients and conformal window bounds | Compare with Seiberg, Intriligator-Seiberg |
| EXER-03 | Exact moduli space and anomaly matching | Compare with Seiberg hep-th/9411149 |
| EXER-05 | Parametric mass hierarchy correct | Compare with Sannino 2407.17281 Table/Section on spectrum |
| EXER-06 | Parametric scale matching correct | Compare with Sannino 2407.17281 |
| VALD-01 | Exact anomaly matching | Independent calculation |
| VALD-05 | Full consistency with primary reference | Line-by-line comparison |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| LECT-01–08 | Complete LaTeX lecture notes | Sannino 2407.17281, Seiberg hep-th/9411149 | None | Notes without exercises |
| EXER-05–06 | Solved exercises with SM spectrum | Sannino 2407.17281 spectrum section | None | Formal duality without scales |
| VALD-01–05 | Consistency verification | Seiberg, Sannino, Csaki-Terning | None | Unchecked anomaly matching |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| LECT-01 | Phase 1: Foundations | Planned |
| EXER-01 | Phase 1: Foundations | Planned |
| EXER-02 | Phase 1: Foundations | Planned |
| LECT-02 | Phase 2: SUSY and Seiberg Duality | Planned |
| LECT-03 | Phase 2: SUSY and Seiberg Duality | Planned |
| LECT-04 | Phase 2: SUSY and Seiberg Duality | Planned |
| EXER-03 | Phase 2: SUSY and Seiberg Duality | Planned |
| EXER-04 | Phase 2: SUSY and Seiberg Duality | Planned |
| LECT-05 | Phase 3: Non-perturbative dynamics | Planned |
| LECT-06 | Phase 3: Non-perturbative dynamics | Planned |
| LECT-07 | Phase 4: The Dualised SM | Planned |
| LECT-08 | Phase 4: The Dualised SM | Planned |
| EXER-05 | Phase 4: The Dualised SM | Planned |
| EXER-06 | Phase 4: The Dualised SM | Planned |
| VALD-01 | Phase 4: The Dualised SM | Planned |
| VALD-02 | Phase 2: SUSY and Seiberg Duality | Planned |
| VALD-03 | Phase 4: The Dualised SM | Planned |
| VALD-04 | Phase 4: The Dualised SM | Planned |
| VALD-05 | Phase 4: The Dualised SM | Planned |
| REFS-01 | Phase 1: Foundations | Planned |
| REFS-02 | Phase 1: Foundations | Planned |
| REFS-03 | Phase 2: SUSY and Seiberg Duality | Planned |
| REFS-04 | Phase 1: Foundations | Planned |

**Coverage:**

- Primary requirements: 22 total
- Mapped to phases: 22
- Unmapped: 0

---

_Requirements defined: 2026-03-20_
_Last updated: 2026-03-20 after literature survey_
