# The Dualised Standard Model — Part III Lecture Notes

## What This Is

Self-contained Part III (Cambridge) half-course lecture notes (~8 lectures) on the dualised Standard Model, following Sannino et al. (2407.17281), Csaki-Terning (1106.3074), Maekawa, and Seiberg's foundational duality work. The notes build duality machinery from scratch — no SUSY prerequisite assumed — and culminate in solved exercises that reproduce the physical SM spectrum (fermion masses, Fermi scale, QCD scale) from the dual description. Intended as an alternative to Tong's SUSY lectures for a shorter visit.

## Core Research Question

Can the dualised Standard Model program be presented as a self-contained Part III half-course that builds duality machinery from scratch and produces quantitative IR matching of the SM spectrum?

## Scoping Contract Summary

### Contract Coverage

- **Lecture notes + exercises**: Self-contained notes producing the physical SM spectrum from the dual description
- **Acceptance signal**: Exercises reproduce m_t ~ 173 GeV, v ~ 246 GeV, Lambda_QCD ~ 200 MeV with correct parametric dependences; a Part III student with standard QFT can follow start to finish
- **False progress to reject**: Formal duality map without quantitative IR spectrum matching

### User Guidance To Preserve

- **User-stated observables:** Full SM fermion mass spectrum with physical scales from dual description
- **User-stated deliverables:** LaTeX lecture notes (~8 lectures) with solved exercises suitable for Part III written examination
- **Must-have references / prior outputs:** Sannino 2407.17281 (backbone), Csaki-Terning 1106.3074, Maekawa's works, Seiberg hep-th/9411149; full reference list from 2407.17281 to be downloaded
- **Stop / rethink conditions:** If the dualised SM does not actually produce quantitative fermion mass predictions; if 8 lectures cannot cover the material

### Scope Boundaries

**In scope**

- Self-contained ~8 lecture notes on the dualised SM for Part III students
- Building duality machinery from scratch without SUSY prerequisites
- Quantitative exercises reproducing SM fermion masses, Fermi scale, QCD scale from dual description
- Complete LaTeX lecture notes with solved exercises suitable for written examination
- Systematic coverage of Seiberg duality, anomaly matching, tumbling, and the dualised SM construction
- Full reference corpus from Sannino 2407.17281, Csaki-Terning 1106.3074, Maekawa, and foundational papers

**Out of scope**

- Full SUSY lecture course — only duality-relevant content if needed
- BSM phenomenology beyond the dualised SM program
- Lattice calculations or numerical simulations
- Cosmological implications of the dualised SM

### Active Anchor Registry

- **ref-sannino-2407**: Sannino et al., arXiv:2407.17281
  - Why it matters: Primary reference for the dualised SM construction — defines the duality map, spectrum, and IR matching
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-csaki-terning**: Csaki and Terning, arXiv:1106.3074
  - Why it matters: Key reference for non-SUSY duality methods and techniques
  - Carry forward: planning | execution | writing
  - Required action: read | cite

- **ref-seiberg-duality**: Seiberg, hep-th/9411149
  - Why it matters: Foundational ground truth for the formal duality structure
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

### Carry-Forward Inputs

- Full reference list from 2407.17281 (to be downloaded into ./sources/)
- Maekawa's specific papers (to be identified during literature survey)

### Skeptical Review

- **Weakest anchor:** Whether the dualised SM program actually produces quantitative fermion mass predictions vs. only qualitative/structural matching
- **Unvalidated assumptions:** 8 lectures suffice for self-contained coverage; non-SUSY duality machinery can be made pedagogically accessible at Part III level
- **Competing explanation:** None identified — this is a pedagogical project, not a competing theory
- **Disconfirming observation:** If the dualised SM literature shows the fermion mass spectrum is only qualitatively matched, not quantitatively derived, the exercise framework needs fundamental revision
- **False progress to reject:** Notes that present the formal duality map without quantitative IR spectrum matching

### Open Contract Questions

- Whether 8 lectures suffice to go from no SUSY background to quantitative spectrum — may need 10-12
- Exact chapter decomposition to be determined after literature review

## Research Questions

### Answered

(None yet — investigate to answer)

### Active

- [ ] What is the minimal duality machinery needed to dualise the SM gauge sectors?
- [ ] How does the dual description produce the observed fermion mass hierarchy?
- [ ] What are the anomaly matching conditions that constrain the dualised SM spectrum?
- [ ] Can the Fermi scale (v ~ 246 GeV) and QCD scale (Lambda_QCD ~ 200 MeV) be derived from the dual theory?
- [ ] What is the optimal pedagogical path from no SUSY to quantitative spectrum in ~8 lectures?

### Out of Scope

- Dynamical SUSY breaking mechanisms — different program
- Composite Higgs models beyond the dualised SM — separate lecture course
- Precision electroweak constraints on the dualised SM — phenomenology paper, not textbook

## Research Context

### Physical System

The Standard Model of particle physics, recast through electric-magnetic (Seiberg-type) dualities applied to the SM gauge sectors SU(3)_c x SU(2)_L x U(1)_Y. The dual description provides an alternative UV completion where strongly coupled dynamics in the UV maps to the weakly coupled SM in the IR.

### Theoretical Framework

Non-supersymmetric gauge-fermion dualities (Seiberg duality and its non-SUSY extensions), 't Hooft anomaly matching, tumbling/complementarity, conformal window analysis. The framework connects to Sannino's program of extending Seiberg duality beyond SUSY to describe the SM as a dual magnetic theory.

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
| --------- | ------ | ------ | ----- |
| Fermi scale | v | 246 GeV | Electroweak symmetry breaking scale |
| QCD scale | Lambda_QCD | ~200 MeV | Confinement scale |
| Top mass | m_t | ~173 GeV | Heaviest SM fermion |
| Number of colours | N_c | 3 | SU(3) colour |
| Number of flavours | N_f | 6 | Quark flavours |
| Weak coupling | g_2 | ~0.65 | SU(2)_L gauge coupling |

### Known Results

- Seiberg duality for N=1 SQCD — Seiberg (1994)
- Non-supersymmetric extensions and tumbling — various authors
- Dualised SM construction — Sannino et al. (2024)
- Anomaly matching in dual theories — 't Hooft (1980)
- Csaki-Terning review of SUSY breaking and duality — Csaki, Terning (2011)
- Maekawa's early work on dual SM descriptions

### What Is New

A self-contained pedagogical presentation of the dualised SM program accessible to Part III students without SUSY background, with solved exercises that produce the actual SM spectrum with physical scales.

### Target Venue

Cambridge Part III Mathematics/Theoretical Physics lecture course (half-course, ~8 lectures)

### Computational Environment

Local workstation. LaTeX compilation. Paper downloads via university (unizar) access with sci-hub fallback. No heavy computation required — this is an analytical/pedagogical project.

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

Natural units (hbar = c = k_B = 1)

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

Key requirement categories: LECT (lecture content), EXER (exercises), VALD (validation against known results)

## Key References

- **Sannino et al., arXiv:2407.17281** — Primary backbone: dualised SM construction, duality map, spectrum, IR matching
- **Csaki and Terning, arXiv:1106.3074** — Duality methods and SUSY breaking review
- **Seiberg, hep-th/9411149** — Foundational: electric-magnetic duality in N=1 SQCD (ground truth for formal structure)
- **Maekawa** — Early dual SM descriptions (specific papers to be identified)
- Full reference list from 2407.17281 to be downloaded

## Constraints

- **Lecture count**: ~8 lectures (half Part III course) — constrains depth of foundational material
- **No SUSY prerequisite**: Must build all duality machinery within the notes themselves
- **Examination suitability**: Solved exercises must work as Part III written exam problems
- **Paper access**: University (unizar) access with sci-hub fallback for downloads

## Key Decisions

| Decision | Rationale | Outcome |
| -------- | --------- | ------- |
| Build duality from scratch, no SUSY prerequisite | Target audience: Part III students choosing this over Tong's SUSY | — Pending |
| ~8 lectures (half-course) with solved exercises for written work | Shorter visit format; exercises compensate for fewer lectures | — Pending |
| Seiberg > Sannino > Terning as ground truth hierarchy | Formal structure from Seiberg; SM application from Sannino; methods from Terning | — Pending |

Full log: `.gpd/DECISIONS.md`

---

_Last updated: 2026-03-19 after initialization_
