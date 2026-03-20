# Roadmap: The Dualised Standard Model -- Part III Lecture Notes

## Overview

This project produces self-contained Part III lecture notes (~8 lectures) on the dualised Standard Model, building Seiberg duality machinery from scratch for students with standard non-SUSY QFT (gauge theory, anomalies, representation theory) from Michaelmas term. The roadmap proceeds from anomaly matching foundations through minimal SUSY and Seiberg duality to the Cacciapaglia-Sannino dualised SM construction, culminating in solved exercises that reproduce the SM spectrum parametrically (fermion mass hierarchies from operator dimensions with free O(1) coefficients, Fermi scale v ~ 246 GeV, QCD scale Lambda_QCD ~ 200 MeV) from the dual description. Exercises carry heavy pedagogical load -- they compensate for compressed lectures and serve as Part III written examination material.

## Contract Overview

| Contract Item | Type | Advanced By Phase(s) | Status |
| ------------- | ---- | -------------------- | ------ |
| claim-lecture-notes: Self-contained Part III notes producing SM spectrum from dual description | claim | 1, 2, 3, 4 | Planned |
| deliv-latex-notes: Complete LaTeX lecture notes (~8 lectures) | deliverable | 1, 2, 3, 4 | Planned |
| deliv-exercises: Solved exercises reproducing SM spectrum with physical scales | deliverable | 1, 2, 4 | Planned |
| test-spectrum-match: Exercises produce m_t ~ 173 GeV, v ~ 246 GeV, Lambda_QCD ~ 200 MeV | acceptance test | 4 | Planned |
| test-self-contained: Part III student with standard QFT can follow start to finish | acceptance test | 1, 2, 3, 4 | Planned |
| ref-sannino-2407: Sannino et al., arXiv:2407.17281 (backbone) | anchor | 2, 3, 4 | Planned |
| ref-csaki-terning: Csaki and Terning, arXiv:1106.3074 | anchor | 2, 3 | Planned |
| ref-seiberg-duality: Seiberg, hep-th/9411149 (ground truth) | anchor | 2 | Planned |
| fp-formal-only: Reject notes with formal duality but no quantitative IR spectrum | forbidden proxy | 4 | Planned |

## Phases

**Phase Numbering:**

- Integer phases (1, 2, 3, 4): Planned research work
- Decimal phases (e.g. 2.1): Urgent insertions if needed (marked INSERTED)

- [x] **Phase 1: Foundations** -- Anomaly matching review, conformal window, conventions, reference corpus download
- [x] **Phase 2: SUSY and Seiberg Duality** -- Minimal N=1 SUSY, Seiberg duality for N=1 SQCD, N=2 content including Fayet mechanisms, duality verification exercises
- [ ] **Phase 3: Non-perturbative Dynamics** -- Tumbling/MAC, complementarity, non-SUSY duality extensions (Sannino-Schechter, Maekawa, Pati-Salam embedding, emergent SUSY)
- [ ] **Phase 4: The Dualised Standard Model** -- Cacciapaglia-Sannino construction, duality map, anomaly matching for full SM, parametric spectrum exercises, scale matching, all validations

## Phase Details

### Phase 1: Foundations

**Goal:** The anomaly matching and conformal window machinery is established with fixed conventions, detailed calculations are moved to exercises, and the full reference corpus is assembled -- a Part III student can verify anomaly coefficients and conformal window boundaries independently

**Depends on:** Nothing (entry point)

**Requirements:** LECT-01, EXER-01, EXER-02, REFS-01, REFS-02, REFS-04

**Contract Coverage:**
- Advances: claim-lecture-notes (Lecture 1 content), deliv-latex-notes (first lecture), deliv-exercises (anomaly + conformal window exercises)
- Deliverables: Lecture 1 LaTeX; Exercise sets 1-2 with full solutions; reference corpus in ./sources/
- Anchor coverage: ref-seiberg-duality (anomaly matching conventions must be compatible); ref-csaki-terning and ref-sannino-2407 downloaded into ./sources/
- Forbidden proxies: None directly active in this phase (foundational material)

**Success Criteria** (what must be TRUE):

1. 't Hooft anomaly matching conditions for SU(N_c) with N_f fundamental flavours are derived and presented with explicit distinction from gauge anomaly cancellation (comparison table included per pitfall P3)
2. Conformal window boundaries for SU(N_c) with fundamental matter are computed: loss of asymptotic freedom at N_f = 11N_c/2, Banks-Zaks fixed point identified, SUSY conformal window 3N_c/2 < N_f < 3N_c reproduced
3. Convention T(fund) = 1/2 per Weyl fermion is fixed and verified against b_0 = (11N_c - 2N_f)/3 with N_f Dirac flavours -- all anomaly coefficients carry correct dimensions/indices throughout
4. Chan-Tsou "Dualized Standard Model" (loop-space Hodge duality) is explicitly disambiguated from Sannino's gauge-fermion duality program
5. All must-read references (ref-sannino-2407, ref-csaki-terning, ref-seiberg-duality, Maekawa papers, Sannino-Schechter) are downloaded and organized in ./sources/

**Backtracking:** If convention verification fails (b_0 formula inconsistent with T(fund) = 1/2), halt and fix conventions before any downstream work.

**Plans:** 3 plans

Plans:
- [ ] 01-01-PLAN.md -- Convention verification and reference corpus assembly
- [ ] 01-02-PLAN.md -- Lecture 1: Anomaly matching review and conformal window
- [ ] 01-03-PLAN.md -- Exercise Sets 1-2: Anomaly matching and conformal window exercises

### Phase 2: SUSY and Seiberg Duality

**Goal:** The minimal N=1 SUSY machinery is introduced and Seiberg duality for N=1 SQCD is derived with full anomaly matching verification -- including N=2 content with Fayet-Iliopoulos breaking and Argyres-Plesser-Seiberg deformations that ground the origin of magnetic degrees of freedom

**Depends on:** Phase 1 (anomaly matching machinery, conventions, reference corpus)

**Requirements:** LECT-02, LECT-03, LECT-04, EXER-03, EXER-04, VALD-02, REFS-03

**Contract Coverage:**
- Advances: claim-lecture-notes (Lectures 2-4), deliv-latex-notes (three lectures), deliv-exercises (Seiberg duality + N=2 deformation exercises)
- Deliverables: Lectures 2-4 LaTeX; Exercise sets 3-4 with full solutions; Sannino-Schechter and Fayet papers downloaded
- Anchor coverage: ref-seiberg-duality (ground truth -- all 6 anomaly coefficients must match exactly between SU(N_c) and SU(N_f - N_c) per Seiberg hep-th/9411149); ref-csaki-terning (duality methods reference)
- Forbidden proxies: None directly active (SUSY duality is well-established; formal-only risk does not apply here)

**Success Criteria** (what must be TRUE):

1. Superfields, superpotential, F/D-terms, and holomorphic non-renormalisation theorem are introduced with every SUSY concept defined at first use (no unexplained SUSY prerequisites)
2. All 6 independent 't Hooft anomaly coefficients for SU(N_f)_L x SU(N_f)_R x U(1)_B x U(1)_R match exactly between electric SU(N_c) and magnetic SU(N_f - N_c) theories -- verified against Seiberg hep-th/9411149 with zero free parameters
3. Moduli space matching (mesons M, baryons B/B-tilde) is demonstrated; mass deformation produces correct flow between dual theories
4. Fayet-Iliopoulos mechanism and Argyres-Plesser-Seiberg N=2 to N=1 deformation are presented showing how magnetic quarks arise as monopoles/dyons on the N=2 Coulomb branch
5. R-charge assignment R[Q] = (N_f - N_c)/N_f verified to give R[W] = 2 (Seiberg convention)

**Backtracking:** If anomaly coefficients do not match between electric and magnetic theories, there is a convention or calculation error -- do not proceed to Phase 3 until resolved. If N=2 content proves too heavy for one lecture, condense to executive summary and flag scope question (may need lecture 4.5).

**Plans:** 4 plans

Plans:
- [ ] 02-01-PLAN.md -- Reference downloads (REFS-03) + Lecture 2: Minimal N=1 SUSY introduction
- [ ] 02-02-PLAN.md -- Lecture 3: Seiberg duality with full anomaly matching + VALD-02 verification script
- [ ] 02-03-PLAN.md -- Lecture 4: N=2 SUSY, FI mechanism, APS deformation + Exercise Set 3: Seiberg duality exercises
- [ ] 02-04-PLAN.md -- Exercise Set 4: N=2 deformation exercises

### Phase 3: Non-perturbative Dynamics

**Goal:** Tumbling/MAC and complementarity are developed as physical mechanisms connecting strongly coupled electric theories to weakly coupled magnetic descriptions, and non-SUSY extensions of duality (Sannino-Schechter, Maekawa, emergent SUSY) are presented with appropriate conjectural qualifiers

**Depends on:** Phase 1 (anomaly matching), Phase 2 (Seiberg duality framework)

**Requirements:** LECT-05, LECT-06

**Contract Coverage:**
- Advances: claim-lecture-notes (Lectures 5-6), deliv-latex-notes (two lectures)
- Deliverables: Lectures 5-6 LaTeX
- Anchor coverage: ref-sannino-2407 (non-SUSY duality extensions follow Sannino's program); ref-csaki-terning (tumbling/complementarity methods)
- Forbidden proxies: Indirect -- Phase 3 must maintain "if the duality holds" language for all non-SUSY duality claims (pitfall P1) to prevent the formal-only forbidden proxy from activating downstream

**Success Criteria** (what must be TRUE):

1. MAC criterion is stated with its limitations (leading-order one-gluon exchange approximation; known counterexamples acknowledged) and applied to identify condensation channels in a simple chiral gauge theory
2. Complementarity principle (Fradkin-Shenker) is presented: magnetic Higgs phase identified with electric confining phase for fundamental-representation Higgs; limitations for partial gauge breaking noted
3. Non-SUSY duality extensions (Sannino QCD dual 2009, SM-as-magnetic 2011, emergent SUSY at fixed points 2013) are presented chronologically with every non-SUSY statement carrying explicit "conjectural" qualification
4. The central theoretical vulnerability is stated: non-SUSY duality has no independent cross-validation beyond anomaly matching; the construction postulates the duality and checks consistency, but does not prove it

**Backtracking:** If tumbling analysis is inconsistent with anomaly matching from Phase 1, revisit the condensation channel assignment. If Maekawa's Pati-Salam construction proves incompatible with Sannino's later work, document the tension and present both.

**Plans:** 2 plans

Plans:
- [ ] 03-01-PLAN.md -- Lecture 5: Tumbling dynamics, MAC criterion, complementarity
- [ ] 03-02-PLAN.md -- Lecture 6: Non-SUSY duality extensions (chronological narrative with conjectural qualifiers)

### Phase 4: The Dualised Standard Model

**Goal:** The Cacciapaglia-Sannino dualised SM is constructed with full anomaly matching for the SM gauge group, and solved exercises produce parametric fermion mass hierarchies, Fermi scale v ~ 246 GeV, and Lambda_QCD ~ 200 MeV from the dual description -- with all conventions, anomaly coefficients, and parametric predictions validated against primary references

**Depends on:** Phase 1 (anomaly matching, conventions), Phase 2 (Seiberg duality), Phase 3 (tumbling/complementarity, non-SUSY extensions)

**Requirements:** LECT-07, LECT-08, EXER-05, EXER-06, VALD-01, VALD-03, VALD-04, VALD-05

**Contract Coverage:**
- Advances: claim-lecture-notes (Lectures 7-8, final lectures), deliv-latex-notes (complete notes), deliv-exercises (decisive spectrum exercises)
- Deliverables: Lectures 7-8 LaTeX; Exercise 5 (fermion mass hierarchy) and Exercise 6 (scale matching) with full solutions; completed and validated lecture note set
- Anchor coverage: ref-sannino-2407 (line-by-line comparison of dualised SM construction, duality map, spectrum -- VALD-05); ref-seiberg-duality (formal structure must remain consistent); ref-csaki-terning (methods cross-check)
- Forbidden proxies: **fp-formal-only** -- This phase must NOT produce notes that present the formal duality map without quantitative IR spectrum matching. The exercises MUST produce parametric scales (m_t ~ O(v), Lambda_QCD ~ O(200 MeV)) with physical numbers, not just abstract duality maps.

**Success Criteria** (what must be TRUE):

1. The dualised SM electric theory (Pati-Salam-like UV gauge structure with only fermions, no elementary scalars) is constructed and the duality map to the magnetic SM (SU(3)_c x SU(2)_L x U(1)_Y with composite Higgs doublets as mesons) is explicit
2. All anomaly coefficients match between electric and magnetic descriptions for the full SM gauge group SU(3)_c x SU(2)_L x U(1)_Y -- independently computed (VALD-01) and cross-checked against Sannino 2407.17281 (VALD-05)
3. Exercise 5 derives parametric fermion mass hierarchy: m_t ~ y*v with y ~ O(1) from universal Yukawa coupling + leading Higgs VEV, lighter masses suppressed by hierarchical VEVs from Planck-scale four-fermion operators with O(1) coefficients as free parameters -- framed as "parametric consistency" not "first-principles prediction" (pitfall P2)
4. Exercise 6 extracts Fermi scale v ~ 246 GeV and Lambda_QCD ~ 200 MeV from dual theory parameters via RG running below the duality scale Lambda_D (treated as input, not prediction) -- parametric consistency with physical values demonstrated
5. All conventions are verified internally consistent throughout the complete 8-lecture note set (T(fund) = 1/2, Weyl fermion counting, metric signature (+,-,-,-)) and the dualised SM construction is consistent with Sannino 2407.17281 (VALD-04, VALD-05)

**Backtracking:** If anomaly matching fails for the full SM gauge group, this is a fundamental problem -- revisit the electric theory field content and duality map before writing exercises. If the parametric spectrum is only qualitatively consistent (wrong scaling, not just O(1) coefficients), trigger stop-and-rethink: the acceptance criterion may need revision. If 8 lectures prove insufficient, flag for scope extension to 10-12 lectures per open contract question.

**Plans:** TBD

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
|-------|-----------|---------|:-:|
| 1 - Foundations | -- | 2, 3 | Yes |
| 2 - SUSY and Seiberg Duality | 1 | 3, 4 | Yes |
| 3 - Non-perturbative Dynamics | 1, 2 | 4 | Yes |
| 4 - The Dualised Standard Model | 1, 2, 3 | -- | Yes |

**Critical path:** 1 -> 2 -> 3 -> 4 (4 phases, strictly sequential)

**Parallelization note:** No parallel phases. Each phase builds on the conceptual machinery of the prior phase. Phase 3 could in principle begin its non-SUSY content (tumbling, MAC) concurrently with Phase 2's SUSY content, since tumbling is non-SUSY and only requires Phase 1. However, complementarity and the non-SUSY duality extensions require the Seiberg duality framework from Phase 2. The sequential ordering reflects the pedagogical dependency: students must see the established SUSY case before the conjectural non-SUSY extension.

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
|-------|---------|:-:|:-:|-----------|
| 1 | Factor-of-2 Dynkin index convention error propagating to all anomaly coefficients (P11) | MEDIUM | HIGH | Fix T(fund) = 1/2 and verify b_0 = (11N_c - 2N_f)/3 before any downstream calculation |
| 2 | N=2 content (Fayet, Argyres-Plesser-Seiberg) too heavy for one lecture | MEDIUM | MEDIUM | Condense to executive summary; detailed derivations in exercises; flag scope extension if needed |
| 3 | Conflating conjectural non-SUSY duality with established SUSY results (P1) | MEDIUM | HIGH | Maintain strict "if the duality holds" language; separate SUSY (established) from non-SUSY (conjectured) lectures |
| 4 | Fermion mass predictions are only qualitative, not parametric (P2) | LOW | CRITICAL | Frame exercises as "parametric consistency" with O(1) free coefficients; if even parametric consistency fails, trigger stop-and-rethink |

## Backtracking Triggers

- **Phase 1 -> Phase 1:** If b_0 formula is inconsistent with T(fund) = 1/2 convention, halt and fix before proceeding
- **Phase 2 -> Phase 1:** If anomaly matching fails for Seiberg duality, check whether Phase 1 conventions introduced an error
- **Phase 3 -> Phase 2:** If tumbling/complementarity results are inconsistent with Seiberg duality framework, revisit Phase 2 assumptions
- **Phase 4 -> Phase 3/2/1:** If full SM anomaly matching fails, systematically trace the error: first check Phase 4 duality map, then Phase 3 non-SUSY extensions, then Phase 2 Seiberg duality conventions, then Phase 1 anomaly matching conventions
- **Phase 4 -> STOP:** If the dualised SM program does not produce even parametric fermion mass predictions (stop-and-rethink condition from contract)
- **Phase 4 -> SCOPE:** If 8 lectures cannot cover the material (stop-and-rethink condition from contract), flag for extension to 10-12 lectures

## Progress

**Execution Order:** 1 -> 2 -> 3 -> 4

| Phase | Plans Complete | Status | Completed |
| ----- | -------------- | ------ | --------- |
| 1. Foundations | 3/3 | Complete | 2026-03-20 |
| 2. SUSY and Seiberg Duality | 4/4 | Complete | 2026-03-20 |
| 3. Non-perturbative Dynamics | 0/TBD | Not started | - |
| 4. The Dualised Standard Model | 0/TBD | Not started | - |
