# Computational Approaches: Dualised Standard Model Lecture Notes

**Surveyed:** 2026-03-19
**Domain:** Gauge-fermion dualities, non-SUSY Seiberg duality, anomaly matching, dualised Standard Model
**Confidence:** HIGH (pedagogical/reference project -- tools and resources are well-established)

## Recommended Stack

This is a LaTeX lecture notes project, not a numerical computation project. The "computational" resources are: (1) existing lecture notes and reviews as pedagogical models, (2) group-theory and anomaly-matching tools for verifying exercises, (3) LaTeX packages for typesetting Feynman diagrams, Young tableaux, and representation theory notation, and (4) the primary paper corpus to download.

Use **LaTeX** (pdflatex or lualatex) for the notes, **Mathematica with GroupMath** (Fonseca, arXiv:2011.01764) for verifying anomaly coefficients and representation-theory calculations in exercises, and **tikz-feynman + ytableau** for diagrams. No heavy numerical computation is needed.

---

## Existing Lecture Notes and Reviews (Pedagogical Models)

These are ranked by relevance to this project, not by general quality.

### Tier 1: Direct Models (Structure Your Notes Around These)

| Resource | arXiv / Location | Coverage | Relevance |
|----------|-----------------|----------|-----------|
| Tong, *Supersymmetric Field Theory* (Part III) | damtp.cam.ac.uk/user/tong/susy.html | Full SUSY field theory including Seiberg duality for SQCD, Intriligator-Pouliot duality, chiral gauge theories, a-maximisation, dynamical SUSY breaking | **PRIMARY COMPETITOR.** Your notes are an alternative to this course. Study Tong's pedagogical style (building machinery incrementally, each chapter ending with applications) and match or exceed its clarity. Tong assumes SUSY from scratch but uses it throughout -- you must match the self-containedness without requiring SUSY. |
| Intriligator and Seiberg, *Lectures on SUSY gauge theories and electric-magnetic duality* | hep-th/9509066 | Holomorphy, NSVZ beta function, ADS superpotential, Seiberg duality for SQCD, conformal window, s-confinement | **FOUNDATIONAL PEDAGOGICAL MODEL** for presenting duality. Terse but rigorous. Use their anomaly-matching worked examples as templates for your exercises. |
| Terning, *TASI-2002: Non-perturbative Supersymmetry* | hep-th/0306119 | Anomalies, instantons, superconformal unitarity bounds, holomorphy, Seiberg duality, dynamical SUSY breaking, gauge mediation (113 pp.) | **BEST PEDAGOGICAL MODEL for anomaly/instanton background.** More detailed than Intriligator-Seiberg on the prerequisite material. Use Terning's anomaly chapter structure as a template for your anomaly lecture(s). |
| Peskin, *Duality in Supersymmetric Yang-Mills Theory* (1996 TASI) | hep-th/9702094 | Effective Lagrangians (non-SUSY and SUSY), SQCD for N_f < N_c, Seiberg-Witten for N=2, SQCD for large N_f | **BEST MODEL for "building from non-SUSY to SUSY duality."** Peskin explicitly starts from non-SUSY effective Lagrangians before introducing SUSY -- exactly the pedagogical path your notes should follow. 80 pp. with 12 figures. |

### Tier 2: Essential Reference Reviews

| Resource | arXiv / Location | Coverage | Relevance |
|----------|-----------------|----------|-----------|
| Strassler, *Unorthodox Introduction to SUSY Gauge Theory* | hep-th/0309149 | Scaling/RG as organising principle; 3d SUSY QED with solitons, dimensional antitransmutation, duality; 4d non-abelian extensions | **PEDAGOGICAL INNOVATION MODEL.** Strassler's approach of using RG flow as the organising principle (rather than the SUSY algebra) is close to what you need. 78 pp. |
| Csaki, Shirman, Terning, *A Seiberg Dual for the MSSM* | 1106.3074 | SU(2)_L as magnetic dual gauge group; composite/partially composite W, Z; composite Higgs and top | **DIRECTLY RELEVANT to the dualised SM.** This paper dualises the MSSM electroweak sector. Study its duality map as a template for the non-SUSY dualised SM construction. |
| Sannino, *Conformal Dynamics for TeV Physics and Cosmology* | 0911.0931 | Phase diagrams for SU, Sp, SO gauge theories; conformal windows; walking technicolor; chiral gauge theory dynamics | **SANNINO'S OWN REVIEW.** Establishes the conformal-window methodology that underlies the dualised SM. Use this for background on how Sannino thinks about gauge dynamics. |
| Bilal, *Lectures on Anomalies* | 0802.0634 | Abelian anomalies (triangle, index theorem); non-abelian gauge anomalies; anomaly cancellation in the SM; descent equations; Wess-Zumino consistency; gravitational anomalies | **BEST ANOMALY REFERENCE.** Self-contained, pedagogical, covers exactly the anomaly material your students need. Recommend as supplementary reading. |

### Tier 3: Textbooks for Background

| Textbook | Coverage | How to Use |
|----------|----------|------------|
| Terning, *Modern Supersymmetry: Dynamics and Duality* (Oxford, 2006) | Ch. 7-11: Nonperturbative results, holomorphy, ADS superpotential, Seiberg duality for SQCD, more Seiberg duality. Ch. 12: Dynamical SUSY breaking. Appendix B: Group theory. | **PRIMARY TEXTBOOK REFERENCE for Seiberg duality.** Chapters 9-11 are the most detailed textbook treatment of Seiberg duality available. Use for derivation details that Intriligator-Seiberg's lectures compress. |
| Weinberg, *Quantum Theory of Fields, Vol. 3* (Cambridge, 2000) | Ch. 27-29: SUSY gauge theories, non-perturbative results, electric-magnetic duality (Seiberg-Witten) | **RIGOROUS REFERENCE** for the formal structure. Weinberg's treatment is more mathematical; use for proofs but not as a pedagogical model. |
| Peskin and Schroeder, *QFT* | Ch. 19: Perturbative anomalies. Ch. 22: Anomalies and effective action. | **PREREQUISITE REFERENCE.** Your students should know P&S Ch. 19 anomaly material. Don't re-derive; cite and build on. |
| Schwartz, *Quantum Field Theory and the Standard Model* | Ch. 30: Anomalies. | **ALTERNATIVE PREREQUISITE.** More modern than P&S on anomalies. |

### Tier 4: No Existing Lecture Notes on the Dualised SM

**There are no existing lecture notes on the dualised Standard Model.** This is a gap your project fills. The closest resources are:
- Sannino's original research papers (2407.17281, 1102.5100, 0907.1364, 0909.4584)
- Maekawa's SUSY dualised SM papers (hep-ph/9509407, hep-ph/9511395, hep-ph/9510426)
- Csaki-Shirman-Terning (1106.3074) for the MSSM dualisation

You are writing the first pedagogical treatment. This is both the opportunity and the challenge.

---

## Paper Corpus from Sannino 2407.17281

### Complete Reference List with Classification

References extracted from arXiv:2407.17281 (Cacciapaglia and Sannino, 2024), classified by relevance to the lecture notes.

#### Class A: Must-Read (Core to the Dualised SM Construction)

| Ref | Authors | Title / Topic | arXiv | Why Essential |
|-----|---------|---------------|-------|---------------|
| [2] | Seiberg (1995) | Electric-magnetic duality in SUSY non-abelian gauge theories | hep-th/9411149 | **Ground truth.** The original Seiberg duality paper. |
| [1] | Seiberg (1994) | Exact results on vacua of 4d SUSY gauge theories | hep-th/9402044 | Establishes holomorphy/exact results framework |
| [6] | Sannino (2011) | The SM is natural as magnetic gauge theory | 1102.5100 | **Key precursor** -- first statement that the SM might be a magnetic dual |
| [4] | Sannino (2009) | QCD Dual | 0907.1364 | Non-SUSY dual of QCD -- the SU(3)_c dualisation |
| [3] | Sannino (2010) | Higher Representations Duals | 0909.4584 | Extends duality to higher representations (needed for SM matter content) |
| [12] | Maekawa (1996) | Duality of a SUSY SM | hep-ph/9509407 | **Earliest SUSY dualised SM** -- Maekawa's pioneering construction |
| [20] | Csaki, Shirman, Terning (2011) | Seiberg Dual for the MSSM | 1106.3074 | **Partially composite W/Z** -- key alternate dualisation approach |
| [9] | Preskill, Weinberg (1981) | Decoupling constraints on massless composites | Phys. Rev. D 24, 1059 | Theoretical foundation for anomaly matching with composites |

#### Class B: Important Supporting Material

| Ref | Authors | Title / Topic | arXiv | Relevance |
|-----|---------|---------------|-------|-----------|
| [5] | Mojaza, Nardecchia, Pica, Sannino (2011) | Dual of QCD with one adjoint fermion | 1101.1522 | Extends QCD dual to adjoint matter |
| [7] | Antipin, Mojaza, Pica, Sannino (2013) | Magnetic fixed points and emergent SUSY | 1105.1510 | Emergent SUSY in magnetic theories -- critical for understanding why dualised SM has quasi-SUSY spectrum |
| [8] | Sannino (2010) | Magnetic S-parameter | 1007.0254 | Precision electroweak constraints on magnetic duals |
| [13] | Maekawa, Sato (1996) | Duality of SUSY SM without R-parity | hep-ph/9511395 | Extension of Maekawa's construction |
| [14] | Maekawa, Takahashi (1996) | Duality of SUSY model with Pati-Salam | hep-ph/9510426 | Pati-Salam dualisation |
| [11] | Pati, Salam (1974) | Lepton number as fourth colour | Phys. Rev. D 10, 275 | Background: Pati-Salam model |
| [21] | Craig, Stolarski, Thaler (2011) | Fat Higgs with magnetic personality | 1106.2164 | Related approach: magnetic dual producing Higgs |
| [22] | Cui, Gherghetta, Wells (2009) | Emergent EWSB with composite W, Z | 0907.0906 | Related approach: composite gauge bosons from strong dynamics |

#### Class C: Phenomenological Context (Lower Priority for Lecture Notes)

| Ref | Authors | Title / Topic | arXiv | Relevance |
|-----|---------|---------------|-------|-----------|
| [15] | Hill, Machado, Thomsen, Turner (2019) | Scalar democracy | 1902.07214 | Phenomenological framework related to scalar spectrum |
| [16] | ATLAS (2024) | Quest to discover SUSY at ATLAS | 2403.02455 | Experimental context; mention in introduction only |
| [19] | Belyaev, Cacciapaglia, Locke, Pukhov (2022) | Minimal DM models | 2203.03660 | DM phenomenology of dualised SM -- out of scope for lectures |
| [23] | Abel, Gherghetta (2010) | AdS5 as large N limit of Seiberg duality | 1010.5655 | Holographic perspective -- interesting but out of scope |

### Additional Papers to Download (Not in 2407.17281 but Essential)

| Authors | Title / Topic | arXiv | Why Needed |
|---------|---------------|-------|------------|
| 't Hooft (1980) | Naturalness, chiral symmetry breaking, and anomaly matching | (Cargese lectures, NATO Sci. Ser. B 59) | **Original 't Hooft anomaly matching.** Not on arXiv but essential. |
| Intriligator, Seiberg (1995) | Lectures on SUSY gauge theories and EM duality | hep-th/9509066 | Best pedagogical presentation of Seiberg duality |
| Peskin (1997) | Duality in SUSY Yang-Mills theory | hep-th/9702094 | Pedagogical model for your notes |
| Strassler (2003) | Unorthodox introduction to SUSY gauge theory | hep-th/0309149 | Pedagogical model (RG-based approach) |
| Terning (2003) | TASI-2002: Non-perturbative SUSY | hep-th/0306119 | Anomaly/instanton background |
| Bilal (2008) | Lectures on Anomalies | 0802.0634 | Self-contained anomaly reference |
| Sannino (2009) | Conformal Dynamics for TeV Physics and Cosmology | 0911.0931 | Sannino's own review of conformal windows |
| Ryttov, Sannino (2008) | Higher representations: conformal windows | 0711.3745 | Conformal window for higher-rep matter |
| Sannino (2008) | Conformal chiral dynamics | 0811.0616 | Chiral dynamics at IR fixed points |
| Fonseca (2020) | GroupMath: Mathematica package for group theory | 2011.01764 | Tool paper for anomaly computation verification |

---

## Tools for Anomaly Matching Calculations

### Primary Recommendation: GroupMath (Mathematica)

**Use GroupMath** (Fonseca, arXiv:2011.01764) for all representation-theory computations needed to verify anomaly matching exercises.

| Feature | Capability | Relevance to This Project |
|---------|------------|--------------------------|
| Anomaly coefficients | Computes Tr({T^a,T^b}T^c) for any representation | Verify 't Hooft anomaly matching between electric and magnetic theories |
| Tensor product decomposition | Decomposes R_1 x R_2 into irreps | Identify meson/baryon operators in dual theory |
| Branching rules | Decomposes reps under subgroup embeddings | Track SM quantum numbers under gauge group breaking |
| Casimir invariants | C_2(R), T(R), d(R) for any rep | Needed for beta function coefficients and anomaly formulae |
| Dimension of representations | d(R) for any Dynkin label | Quick cross-checks |

**Installation:** Download from https://renatofonseca.net/groupmath. Free. Requires Mathematica.

**Key commands for this project:**

```mathematica
(* Load *)
<< GroupMath`

(* Anomaly coefficient A(R) for SU(N) *)
Anomaly[SU3, {1,0}]  (* fundamental: should give 1 *)
Anomaly[SU3, {0,1}]  (* antifundamental: should give -1 *)

(* Dynkin index T(R) *)
DynkinIndex[SU3, {1,0}]  (* fundamental: should give 1/2 *)

(* Dimension *)
DimR[SU5, {1,0,0,0}]  (* fundamental of SU(5): should give 5 *)

(* Tensor product decomposition *)
ReduceRepProduct[SU3, {{1,0},{0,1}}]  (* 3 x 3-bar = 8 + 1 *)
```

### Fallback: LieART (Mathematica)

**LieART 2.0** (arXiv:1912.10969) is an alternative if GroupMath proves insufficient. It has broader coverage of exceptional Lie algebras and subalgebra branching rules. However, GroupMath has more direct anomaly-coefficient computation.

| Tool | Strengths | Weaknesses | Recommendation |
|------|-----------|------------|----------------|
| GroupMath | Direct anomaly coefficients, modern API, active development | Requires Mathematica | **Primary choice** |
| LieART 2.0 | Extensive branching rules, Dynkin diagram support | Less direct anomaly interface | Fallback |
| By hand | Full pedagogical control, no software dependency | Error-prone for large representations | Use for exercises, verify with GroupMath |

### Manual Anomaly Computation (For Exercises)

For the anomaly matching exercises in the lecture notes, students should compute by hand. The key formulae are:

For SU(N) with fermions in representation R_i:
- **SU(N)^3 anomaly:** Sum_i A(R_i) where A(fundamental) = 1
- **SU(N)^2 U(1) anomaly:** Sum_i T(R_i) q_i where T(fundamental) = 1/2
- **U(1)^3 anomaly:** Sum_i q_i^3
- **U(1)-gravity^2 anomaly:** Sum_i q_i
- **SU(N)^2 gravity anomaly:** Sum_i T(R_i)

The anomaly coefficients A(R) and Dynkin indices T(R) for SU(N) representations commonly needed:

| Representation | Dimension | Dynkin Index T(R) | Anomaly A(R) |
|---------------|-----------|-------------------|--------------|
| Fundamental | N | 1/2 | 1 |
| Antifundamental | N | 1/2 | -1 |
| Adjoint | N^2-1 | N | 0 |
| Symmetric | N(N+1)/2 | (N+2)/2 | N+4 |
| Antisymmetric | N(N-1)/2 | (N-2)/2 | N-4 |

These are standard results from any group theory textbook (Slansky, Phys. Rep. 79 (1981) 1; Yamatsu, arXiv:1511.08771).

---

## LaTeX Resources

### Recommended Package Set

```latex
% ---- Core document class ----
\documentclass[11pt,a4paper]{article}  % or amsart for heavier math

% ---- Mathematics ----
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}          % \coloneqq, \DeclarePairedDelimiter, etc.
\usepackage{slashed}            % Feynman slash notation \slashed{D}
\usepackage{braket}             % Dirac notation (optional, not much used here)

% ---- Physics notation ----
\usepackage{physics}            % \tr, \comm, \acomm, \dd, \pdv, etc.
                                % WARNING: 'physics' package redefines \tr;
                                % if conflicts arise, define macros manually

% ---- Feynman diagrams ----
\usepackage[compat=1.1.0]{tikz-feynman}
                                % TikZ-based Feynman diagrams
                                % Requires LuaLaTeX for automatic layout;
                                % manual layout works with pdflatex

% ---- Young tableaux ----
\usepackage{ytableau}           % Young diagrams and tableaux
                                % \ydiagram{3,2,1} for a diagram
                                % \ytableau{a & b \\ c} for filled tableaux

% ---- Tables and formatting ----
\usepackage{booktabs}           % Professional tables with \toprule, \midrule
\usepackage{array}              % Extended column types
\usepackage{multirow}           % Multi-row cells

% ---- Cross-referencing ----
\usepackage[colorlinks]{hyperref}
\usepackage{cleveref}           % \cref{eq:anomaly} -> "Eq. (3.1)"

% ---- Bibliography ----
\usepackage[
  style=phys,                   % APS-style citations
  articletitle=true,
  biblabel=brackets,
  chaptertitle=true,
  pageranges=true
]{biblatex}
\addbibresource{references.bib}
```

### Feynman Diagrams with tikz-feynman

Use **tikz-feynman** (CTAN: tikz-feynman, jpellis.me/projects/tikz-feynman) because it integrates natively with TikZ, requires no external programs (unlike feynMF/feynMP), and produces publication-quality output.

Key diagram types needed for these notes:
- Triangle diagrams (anomaly illustration)
- Quark/gluon interactions (SM side)
- Meson/baryon vertices (dual magnetic side)
- RG flow diagrams (schematic, not Feynman -- use plain TikZ)

```latex
% Example: triangle anomaly diagram
\feynmandiagram [horizontal=a to b] {
  i1 [particle=\(A_\mu^a\)] -- [boson] a,
  i2 [particle=\(A_\nu^b\)] -- [boson] b,
  i3 [particle=\(A_\rho^c\)] -- [boson] c,
  a -- [fermion, half left] b -- [fermion, half left] c -- [fermion, half left] a,
};
```

**Compilation note:** For automatic vertex placement, use LuaLaTeX. For manual placement (sufficient for lecture notes), pdflatex works fine.

### Young Tableaux with ytableau

Use **ytableau** (CTAN: ytableau) for representation-theory diagrams. Needed for:
- Illustrating SU(N) representations (fundamental, antisymmetric, symmetric)
- Tensor product decompositions visually
- Meson/baryon operator construction

```latex
% SU(3) fundamental
\ydiagram{1}

% SU(3) antisymmetric (= antifundamental)
\ydiagram{1,1}

% SU(5) antisymmetric tensor (10-dim)
\ydiagram{1,1}  % two-box column for \overline{5}
\ydiagram{2}    % two-box row for 10
```

### Custom Macros for These Notes

```latex
% ---- Gauge groups ----
\newcommand{\SU}[1]{\mathrm{SU}(#1)}
\newcommand{\SO}[1]{\mathrm{SO}(#1)}
\newcommand{\Sp}[1]{\mathrm{Sp}(#1)}
\newcommand{\U}[1]{\mathrm{U}(#1)}

% ---- Standard Model groups ----
\newcommand{\GSM}{\SU{3}_c \times \SU{2}_L \times \U{1}_Y}

% ---- Representations (boldface) ----
\newcommand{\fund}{\mathbf{N}}        % fundamental
\newcommand{\afund}{\overline{\mathbf{N}}}  % antifundamental
\newcommand{\adj}{\mathbf{Adj}}       % adjoint
\newcommand{\sym}{\mathbf{S}}         % symmetric
\newcommand{\asym}{\mathbf{A}}        % antisymmetric

% ---- Duality notation ----
\newcommand{\Nf}{N_f}
\newcommand{\Nc}{N_c}
\newcommand{\Nfc}{\widetilde{N}_c}    % dual colours
\newcommand{\Lam}{\Lambda}            % dynamical scale
\newcommand{\Lame}{\Lambda_{\mathrm{el}}}   % electric scale
\newcommand{\Lamm}{\Lambda_{\mathrm{mag}}}  % magnetic scale

% ---- Anomaly shorthand ----
\newcommand{\anomaly}[1]{\mathcal{A}\left[#1\right]}

% ---- Scales ----
\newcommand{\vev}[1]{\langle #1 \rangle}
\newcommand{\LambdaQCD}{\Lambda_{\mathrm{QCD}}}
\newcommand{\vEW}{v_{\mathrm{EW}}}
```

---

## Data Flow

```
Prior literature (papers downloaded to ./sources/)
-> Read and synthesise duality constructions
-> Draft LaTeX lecture notes with derivations
  -> Verify anomaly matching with GroupMath
  -> Draw diagrams with tikz-feynman
  -> Typeset representations with ytableau
-> Compile with pdflatex/lualatex
-> Cross-check limiting cases against known results
-> Final lecture notes PDF
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelise? |
|------|-----------|----------|-----------------|
| Download paper corpus | Network access | ./sources/*.pdf | Yes (all papers independent) |
| Survey Tong's notes structure | Tong notes PDF | Pedagogical structure template | Yes |
| Draft lecture structure | Paper corpus + structure template | Lecture outline | No (needs both inputs) |
| Write anomaly matching lecture | Lecture outline + Bilal reference | Anomaly chapter LaTeX | No |
| Verify anomaly exercises | Anomaly chapter + GroupMath | Verified exercises | No |
| Write duality lectures | Anomaly chapter + Seiberg papers | Duality chapters LaTeX | No |
| Write dualised SM lectures | Duality chapters + 2407.17281 | Final chapters LaTeX | No |
| Compile and cross-check | All chapters | PDF lecture notes | No |

## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| Paper download (~30 PDFs) | 10-30 min | Negligible | ~200 MB | Any with network |
| GroupMath anomaly checks | < 1 min each | < 1 GB | Negligible | Any with Mathematica |
| LaTeX compilation | < 1 min per pass | < 500 MB | < 50 MB | Any with TeX |
| Full project (writing) | ~40-80 hours human effort | N/A | N/A | N/A |

---

## Open Questions

Questions without consensus answers that affect the lecture notes.

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| Does the non-SUSY dualised SM produce *quantitative* fermion masses or only parametric dependences? | Sannino 2407.17281 claims IR matching but the level of quantitative prediction vs. parametric scaling is unclear from the abstract | If only parametric: exercises must be framed differently (scaling relations, not numbers) | Read the full paper carefully; compare with Maekawa's SUSY version |
| Is the quasi-SUSY spectrum of the magnetic theory testable independently of the dualised SM? | The "quasi-SUSY spectrum" claim in 2407.17281 could be a strong or weak prediction | Affects whether the phenomenology section is meaningful or speculative | Read 2407.17281 in detail |
| Can anomaly matching for the full SM (SU(3) x SU(2) x U(1) with 3 generations) be presented as a tractable exercise? | The number of anomaly conditions for the full SM is large but finite | If too complex: split into sub-exercises (SU(3) sector alone, then SU(2) sector, then combined) | Follow Terning's lecture structure for breaking up anomaly computations |

## Anti-Approaches

Approaches to explicitly NOT pursue.

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Lattice verification of duality claims | Out of scope; no lattice infrastructure; non-perturbative duality is not lattice-checkable in practice | Trust anomaly matching + holomorphy arguments; note limitations honestly |
| Full SUSY formalism (superspace, superfields) as prerequisite | Adds 3-4 lectures of overhead; students choosing this course specifically do not want full SUSY | Build duality from gauge theory + anomaly matching; introduce only the minimal SUSY concepts needed to state Seiberg's result |
| Numerical RG running for coupling constant matching | Adds computational complexity without pedagogical value for duality | Use known analytic results for beta functions and conformal windows; cite lattice results where available |
| Writing a review paper instead of lecture notes | Different genre; reviews are comprehensive, notes are pedagogical | Focus on building intuition through exercises, not on completeness |

## Logical Dependencies

```
Gauge theory prerequisites (Ch. 1-2)
  -> Anomaly computation machinery (Ch. 3)
    -> 't Hooft anomaly matching (Ch. 4)
      -> Seiberg duality for SQCD (Ch. 5)
        -> Non-SUSY extensions and conformal window (Ch. 6)
          -> Dualising the SM gauge sectors (Ch. 7)
            -> Physical spectrum and exercises (Ch. 8)

Anomaly matching (Ch. 3-4) -> INDEPENDENT of Seiberg duality details
Seiberg duality (Ch. 5) -> REQUIRES anomaly matching as a tool
Dualised SM (Ch. 7-8) -> REQUIRES both anomaly matching AND duality
```

## Recommended Investigation Scope

Prioritise:
1. **Anomaly matching machinery** -- this is the core tool students must master; build exercises around it
2. **Seiberg duality for SU(N_c) with N_f flavours** -- the canonical example; derive the conformal window, the dual gauge group, the mapping of operators
3. **Dualisation of SU(3)_c** -- the simplest SM sector to dualise; do this in detail as the central worked example

Defer:
- **Full electroweak sector dualisation** -- more complex, depends on SU(3)_c being understood first
- **Phenomenological predictions** -- only after the formal structure is established
- **Comparison with other BSM approaches** -- out of scope for these notes

---

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| Anomaly coefficients for SM representations | Compute by hand, verify with GroupMath | SM anomaly cancellation is exact | Peskin & Schroeder Ch. 19; PDG Review |
| Seiberg duality for SU(N_c) with N_f flavours | Reproduce Intriligator-Seiberg anomaly matching table | Electric and magnetic anomalies match exactly | hep-th/9509066, Table 1 |
| Conformal window bounds | Check N_f/N_c ratios against known results | 3N_c/2 < N_f < 3N_c for fundamental matter | Seiberg (hep-th/9411149); Ryttov-Sannino (0711.3745) |
| Dual gauge group dimension | N_f - N_c for SU(N_c) SQCD | Matches Seiberg's result | hep-th/9411149 |
| Beta function coefficients | Compare one-loop and two-loop with Terning Ch. 7 | Exact match | Terning, *Modern Supersymmetry* |
| Dualised SM spectrum | Compare with Sannino 2407.17281 Table(s) | Must reproduce their matter content | 2407.17281 |

---

## Textbook Presentations of Prerequisites

For a Part III student who has taken standard QFT (Peskin & Schroeder level), the following textbook chapters provide the exact prerequisite material.

### Gauge Theory and Anomalies

| Topic | Best Source | Chapter/Section | Level |
|-------|-----------|-----------------|-------|
| Perturbative anomalies (ABJ) | Peskin & Schroeder | Ch. 19 | Part III prerequisite (assumed known) |
| Non-perturbative anomalies | Weinberg Vol. 2 | Ch. 22 | Reference for deeper treatment |
| Anomaly cancellation in the SM | Bilal (0802.0634) | Sec. 4 | **Recommend as reading** |
| Instantons and theta vacua | Shifman, *Advanced Topics in QFT* | Ch. 3-4 | Reference only; not needed in detail |
| Anomalies (modern treatment) | Schwartz, *QFT and the SM* | Ch. 30 | Alternative to P&S Ch. 19 |
| Anomalies (Cambridge style) | Tong, *Gauge Theory* (damtp.cam.ac.uk/user/tong/gaugetheory/3anom.pdf) | Ch. 3 | **BEST for Part III students** -- same department, same conventions |

### Non-Abelian Gauge Theory

| Topic | Best Source | Chapter/Section | Level |
|-------|-----------|-----------------|-------|
| Non-abelian gauge fields | Peskin & Schroeder | Ch. 15-16 | Prerequisite |
| Asymptotic freedom | Peskin & Schroeder | Ch. 16.7 | Prerequisite |
| Confinement (qualitative) | Tong, *Gauge Theory* | Ch. 2 | Recommended background |
| Chiral symmetry breaking | Peskin & Schroeder | Ch. 19.3 | Prerequisite |
| Large N_c | 't Hooft (1974); Coleman, *Aspects of Symmetry* | Ch. 8 | Helpful but not essential |

### Representation Theory

| Topic | Best Source | Reference |
|-------|-----------|-----------|
| SU(N) representations for physicists | Georgi, *Lie Algebras in Particle Physics* | Standard reference |
| Young tableaux for SU(N) | Georgi Ch. 12-13 | Use for exercise construction |
| Dynkin indices and Casimirs | Slansky, Phys. Rep. 79 (1981) 1 | Comprehensive tables |
| Modern summary | Yamatsu, arXiv:1511.08771 | Updated Slansky-style tables |

---

## Sources

- Cacciapaglia and Sannino, arXiv:2407.17281 -- primary backbone paper
- Seiberg, arXiv:hep-th/9411149 -- foundational Seiberg duality
- Seiberg, arXiv:hep-th/9402044 -- exact results on SUSY vacua
- Intriligator and Seiberg, arXiv:hep-th/9509066 -- pedagogical duality lectures
- Peskin, arXiv:hep-th/9702094 -- TASI lectures on duality
- Strassler, arXiv:hep-th/0309149 -- unorthodox SUSY gauge theory introduction
- Terning, arXiv:hep-th/0306119 -- TASI 2002 non-perturbative SUSY
- Terning, *Modern Supersymmetry* (Oxford, 2006) -- textbook
- Bilal, arXiv:0802.0634 -- lectures on anomalies
- Sannino, arXiv:1102.5100 -- SM as magnetic gauge theory
- Sannino, arXiv:0907.1364 -- QCD dual
- Sannino, arXiv:0909.4584 -- higher representations duals
- Sannino, arXiv:0911.0931 -- conformal dynamics review
- Csaki, Shirman, Terning, arXiv:1106.3074 -- Seiberg dual for MSSM
- Maekawa, arXiv:hep-ph/9509407 -- duality of SUSY SM
- Fonseca, arXiv:2011.01764 -- GroupMath package
- Feger and Kephart, arXiv:1912.10969 -- LieART 2.0
- tikz-feynman documentation: jpellis.me/projects/tikz-feynman
- ytableau documentation: ctan.org/pkg/ytableau
- Tong, SUSY lectures: damtp.cam.ac.uk/user/tong/susy.html
- Tong, Gauge Theory Ch. 3 (Anomalies): damtp.cam.ac.uk/user/tong/gaugetheory/3anom.pdf
