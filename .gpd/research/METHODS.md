# Methods Research: Dualised Standard Model Lecture Notes

**Domain:** Non-perturbative QFT / gauge-fermion dualities / Standard Model duality
**Researched:** 2026-03-19
**Confidence:** HIGH (core duality methods); MEDIUM (non-SUSY extensions and scale matching)

### Scope Boundary

METHODS.md covers the analytical and pedagogical PHYSICS methods needed to build and present gauge-fermion dualities, anomaly matching, and the dualised Standard Model construction. It does NOT cover software tools (LaTeX, symbolic algebra) -- those belong in COMPUTATIONAL.md. The focus is on what techniques to teach, in what order, and how each method connects to producing the SM spectrum.

---

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended | SUSY Required? |
| ------ | ------- | --------------- | -------------- |
| 't Hooft anomaly matching | Constrain IR spectrum from UV symmetries | Non-negotiable consistency check for any duality; purely group-theoretic, no SUSY needed | No |
| Seiberg duality map (N=1 SQCD) | Establish electric-magnetic duality for SU(N) with N_f flavours | Ground truth: the formal structure that all SM dualisation rests on | Yes (N=1) |
| Banks-Zaks fixed point analysis | Determine conformal window boundaries | Required to identify which SU(N) theories flow to IR fixed points vs. confine | No |
| Most attractive channel (MAC) criterion | Identify which fermion bilinear condenses first | Standard tool for tumbling dynamics; purely non-SUSY, based on one-gluon exchange | No |
| Tumbling / sequential condensation | Derive hierarchical symmetry breaking patterns | Raby-Dimopoulos-Susskind (1980): explains how chiral gauge theories break symmetry in stages | No |
| Complementarity principle | Relate confined-phase composites to Higgs-phase elementary fields | Connects tumbling results to the particle spectrum one observes | No |
| N=2 to N=1 mass deformation (Argyres-Plesser-Seiberg) | Derive Seiberg duality from semiclassical N=2 physics | Provides the most rigorous derivation of N=1 duality; essential for conceptual grounding | Yes (starting N=2) |
| Holomorphy and non-renormalisation | Constrain superpotentials exactly | Foundation for all exact results in SUSY gauge theories | Yes (N=1) |
| Planck-scale four-fermion operators (Sannino) | Generate flavour hierarchy and fermion masses | Specific to the dualised SM programme; produces the observed mass spectrum | No (applied in magnetic theory) |
| RG matching of scales | Extract physical scales (v, Lambda_QCD, m_f) from dual description | Required for quantitative exercises reproducing SM parameters | No |

### Pedagogical Classification

**Essential -- must be in the notes:**
1. 't Hooft anomaly matching (non-SUSY, prerequisite for everything)
2. Seiberg duality for N=1 SQCD (the core machinery)
3. Conformal window / Banks-Zaks analysis (non-SUSY, determines when duality applies)
4. Tumbling and MAC criterion (non-SUSY, produces spectrum)
5. Complementarity (non-SUSY, interprets spectrum)
6. Duality map construction (maps UV to IR)
7. Scale matching (produces quantitative SM parameters)

**Conceptually important -- present as motivation/derivation:**
8. N=2 to N=1 deformation (explains WHERE Seiberg duality comes from)
9. Holomorphy (explains WHY exact results are possible)

**Background -- state without full derivation:**
10. NSVZ exact beta function (state and use; derive only if lecture count permits)
11. Instanton effects in SQCD (mention; don't derive)

---

## Method Details

### Method 1: 't Hooft Anomaly Matching

**What:** Given a UV theory with global symmetry group G_f and massless fermions in representations R_UV, the triangle anomaly coefficients A(G_a, G_b, G_c) computed from the UV spectrum must equal those computed from whatever massless fermions survive in the IR. This is an exact non-perturbative statement.

**Mathematical basis:** For each triple of global (or global x gauge) symmetry generators T_a, T_b, T_c, compute:

```
A_UV(a,b,c) = sum over UV Weyl fermions: Tr[T_a {T_b, T_c}]
A_IR(a,b,c) = sum over IR Weyl fermions: Tr[T_a {T_b, T_c}]
```

The matching condition is A_UV = A_IR for every anomaly coefficient, including:
- SU(N_f)_L^3, SU(N_f)_R^3 (cubic flavour anomalies)
- SU(N_f)_L^2 U(1)_B, SU(N_f)_R^2 U(1)_B (mixed anomalies)
- U(1)_B^3 (cubic baryonic anomaly)
- U(1)_B (linear gravitational anomaly, i.e., Tr[T_a])
- Mixed anomalies with any other global symmetries

**SUSY requirement:** None. This is a purely group-theoretic tool.

**Why it works:** 't Hooft's argument (1980): promote G_f to a gauge symmetry by coupling to weakly-gauged spectator gauge fields. Anomaly cancellation of the full gauged theory is preserved under RG flow. The spectator fermions added to cancel UV anomalies are inert under RG. Therefore IR fermions must produce the same anomaly coefficients.

**Pedagogical note:** This is the FIRST method to teach because (a) it requires only group theory and fermion representations from standard QFT, (b) it is non-SUSY, (c) it constrains every subsequent construction. Start with QCD as a warm-up: SU(3) with N_f = 2 flavours, check SU(2)_L^3, SU(2)_R^3, U(1)_B^3 matching between quarks and baryons/pions.

**Known failure modes:** Anomaly matching is necessary but NOT sufficient. Multiple IR spectra can match the same UV anomalies ('t Hooft, 1980; Ryttov & Sannino, 2007). The method constrains but does not uniquely determine the IR physics.

**Validation:** For Seiberg duality, all six independent anomaly coefficients match between electric SU(N_c) and magnetic SU(N_f - N_c) theories. This is a quantitative check with no free parameters.

**Key references:**
- 't Hooft, 1980: "Naturalness, chiral symmetry, and spontaneous chiral symmetry breaking" (Cargese lectures). [HIGH confidence -- textbook result]
- Intriligator & Seiberg, hep-th/9509066, Section 5: systematic anomaly matching for SQCD [HIGH]
- Terning, "Modern Supersymmetry" (OUP, 2006), Chapter 9 [HIGH]
- Seiberg, hep-th/9411149, Section 4: explicit anomaly computation for the dual pair [HIGH]

---

### Method 2: Seiberg Duality for N=1 SQCD

**What:** SU(N_c) N=1 SQCD with N_f flavours of quarks Q_i, Q-tilde^i (i = 1,...,N_f) in the fundamental and anti-fundamental representations has a dual "magnetic" description as SU(N_f - N_c) with N_f flavours of dual quarks q^i, q-tilde_i plus N_f^2 gauge singlet mesons M^i_j, with a superpotential W = (1/mu) M q q-tilde.

**Mathematical basis:**
- Electric theory: SU(N_c) gauge, N_f flavours, W_elec = 0
- Magnetic theory: SU(N_f - N_c) gauge, N_f flavours + singlets M, W_mag = (1/mu) M_j^i q_i q-tilde^j
- Duality relation: N_c,mag = N_f - N_c
- Conformal window: (3/2)N_c < N_f < 3N_c (both theories flow to same IR fixed point)
- Free magnetic phase: N_c + 2 <= N_f <= (3/2)N_c (magnetic theory is IR free)
- Below N_c + 2: modified moduli space, confinement, or runaway

**Scale matching at the duality:**
```
Lambda_elec^(3N_c - N_f) * Lambda_mag^(3(N_f - N_c) - N_f) = (-1)^(N_f - N_c) * mu^N_f
```
This is the crucial scale-matching relation. It connects the strong-coupling scales of the two theories.

**SUSY requirement:** YES, N=1. The duality is established using holomorphy of the superpotential, the NSVZ exact beta function, and 't Hooft anomaly matching. Without SUSY, holomorphy is lost and the duality becomes conjectural.

**Pedagogical note:** Present Seiberg duality AFTER anomaly matching (Method 1) and AFTER introducing N=1 superfield formalism. The minimal SUSY content needed is: chiral superfields, vector superfields, F-term and D-term conditions, holomorphic superpotential, and the concept of the moduli space of vacua. This can be covered in approximately 2 lectures.

**Key insight for pedagogy:** The student should understand that Seiberg duality is NOT a derivation from first principles -- it is a conjecture supported by overwhelming evidence (anomaly matching, limiting cases, deformations). The N=2 to N=1 deformation (Method 7) provides the closest thing to a "derivation."

**Known failure modes:**
- Does not apply outside the specified N_f range
- Non-SUSY deformation to the SM is the central open question
- Duality cascade and strong-coupling effects complicate the picture for gauge theories with product gauge groups (as in the SM)

**Validation:**
- All 't Hooft anomaly coefficients match (6 independent checks for SU(N_f)_L x SU(N_f)_R x U(1)_B x U(1)_R)
- Deformation by mass terms: giving mass to one flavour in the electric theory flows to SU(N_c) with N_f - 1, and in the magnetic theory it Higgses SU(N_f - N_c) to SU(N_f - N_c - 1), producing the correct dual with one fewer flavour
- 't Hooft limit (large N_c, N_f/N_c fixed): both theories have the same meson spectrum
- Limiting cases (N_f = N_c + 1, N_f = N_c) produce confinement with/without chiral symmetry breaking, matching known results

**Key references:**
- Seiberg, hep-th/9411149 (1994) -- the foundational paper [HIGH]
- Intriligator & Seiberg, hep-th/9509066 (1995) -- pedagogical lectures [HIGH]
- Terning, "Modern Supersymmetry" (OUP, 2006), Chapters 10-12 [HIGH]
- Terning, hep-th/0306119 (TASI 2002) -- lecture-style presentation [HIGH]

---

### Method 3: Banks-Zaks Fixed Point and Conformal Window Analysis

**What:** For SU(N_c) gauge theory with N_f massless Dirac fermions in a representation R, the two-loop beta function has a perturbative zero (Banks-Zaks fixed point) when the one-loop coefficient b_0 > 0 (asymptotic freedom) and the two-loop coefficient b_1 < 0. The conformal window is the range of N_f where the theory flows to an interacting IR conformal fixed point.

**Mathematical basis:**
For fundamental representation fermions:
```
b_0 = (1/3)(11 N_c - 2 N_f)       [asymptotic freedom: b_0 > 0, i.e., N_f < 11N_c/2]
b_1 = (1/3)(34 N_c^2 - N_f(13 N_c - 3/N_c))  [b_1 < 0 gives BZ fixed point perturbatively]
```
The upper boundary of the conformal window is N_f^{AF} = 11N_c/2 (loss of asymptotic freedom).
The lower boundary N_f^* is non-perturbative and debated:
- Appelquist-Lane-Mahanta (1988): critical coupling condition gives N_f^* ~ 4N_c (ladder approximation)
- Sannino (SUSY-inspired beta function, 0711.3745): N_f^* determined by all-orders conjectured beta function
- Lattice evidence (Appelquist et al., 0712.0609): for SU(3), conformal window begins around N_f ~ 12

**SUSY requirement:** None. This is a standard perturbative and non-perturbative QFT analysis.

**Pedagogical note:** Present BEFORE Seiberg duality to motivate WHY duality exists: when N_f is in the conformal window, both electric and magnetic descriptions flow to the same fixed point. When N_f is below the window, one description confines while the other is weakly coupled. For the SM with SU(3) colour and N_f = 6 quarks, we are BELOW the conformal window -- the theory confines. This means we are in the "free magnetic" phase where the dual description is weakly coupled.

**For the SM application:** N_c = 3, N_f = 6. The conformal window for SU(3) fundamental fermions extends roughly from N_f ~ 8-12 (lower bound model-dependent) to N_f = 16.5 (loss of AF). With N_f = 6, we are below the conformal window, in the confined/chirally broken phase. The magnetic dual SU(N_f - N_c) = SU(3) with N_f = 6 dual quarks is in the same regime, but complementarity identifies the dual description with the observed SM spectrum.

**Key references:**
- Banks & Zaks, Nucl. Phys. B196 (1982) 189 [HIGH]
- Appelquist, Lane & Mahanta, Phys. Rev. Lett. 61 (1988) 1553 [HIGH]
- Ryttov & Sannino, arXiv:0711.3745 (2007) -- SUSY-inspired all-orders beta function [MEDIUM-HIGH]
- Appelquist, Fleming & Neil, arXiv:0712.0609 (2007) -- lattice study of conformal window [MEDIUM-HIGH]

---

### Method 4: Tumbling and the Most Attractive Channel (MAC) Criterion

**What:** In a chiral gauge theory where the fermion content does not form a real representation, dynamical symmetry breaking occurs. The MAC criterion identifies which fermion bilinear condensate forms first: the one in the channel with the largest one-gluon exchange attraction (largest quadratic Casimir in the attractive channel).

**Mathematical basis:**
For two fermions in representations R_1 and R_2 forming a condensate in channel R_c:
```
Delta C_2 = C_2(R_1) + C_2(R_2) - C_2(R_c)
```
The most attractive channel maximises Delta C_2. Once the condensate forms, it breaks the gauge symmetry, and the residual theory is analysed again for the next condensation -- this is "tumbling."

**SUSY requirement:** None. This is a non-SUSY strong dynamics argument based on one-gluon exchange, generalising the BCS mechanism.

**Regime of validity:** The MAC criterion is a leading-order estimate. It works well when the gauge coupling is strong enough to trigger condensation but not so strong that higher-order corrections dominate. It is most reliable for theories near the edge of the conformal window.

**Pedagogical note:** Tumbling is the mechanism that produces the hierarchical mass spectrum in the dualised SM. Present AFTER conformal window analysis (students understand when condensation occurs) and AFTER anomaly matching (students can check that tumbling preserves anomalies at each stage). The tumbling sequence is directly connected to the fermion mass hierarchy: each tumbling step produces a condensation scale, and the ratio of successive scales gives the mass ratios.

**Known failure modes:**
- MAC is a crude criterion: it uses one-gluon exchange, which is perturbative reasoning applied at strong coupling
- The actual condensation channel may differ from the MAC prediction in strongly coupled theories
- For theories with multiple attractive channels close in Delta C_2, the ordering may be wrong
- Walking dynamics (theories near the lower edge of the conformal window) can modify the condensation pattern

**Key references:**
- Raby, Dimopoulos & Susskind, Nucl. Phys. B169 (1980) 373 [HIGH -- original tumbling paper]
- Dimopoulos, Raby & Susskind, Nucl. Phys. B173 (1980) 208 [HIGH -- light composite fermions]
- Peskin, "Lectures on the theory of dynamical electroweak symmetry breaking" (1995) [HIGH -- pedagogical review]

---

### Method 5: Complementarity Principle

**What:** For a non-abelian gauge theory with scalars (or dynamically generated condensates playing the role of scalars), the Higgs phase and the confinement phase are smoothly connected -- there is no phase transition separating them. This means the confined-phase composite spectrum can be identified with the Higgs-phase elementary particle spectrum.

**Mathematical basis:** Consider SU(N) with a scalar in the fundamental. In the Higgs phase, the scalar VEV breaks SU(N) to SU(N-1) and there are massive W-bosons, a massive Higgs, and massless gauge bosons. In the confined phase, the gauge singlet composites (mesons, baryons) can be put in one-to-one correspondence with these Higgs-phase particles. The key is that the global quantum numbers (flavour, baryon number) match.

**SUSY requirement:** None. Complementarity is a statement about gauge theories with scalars, regardless of SUSY.

**Why it matters for the dualised SM:** The magnetic dual theory has scalar mesons M (or in the non-SUSY case, composite scalars from fermion bilinear condensation). Complementarity identifies these composites with the Higgs field and the SM scalars. The W, Z bosons of the SM are identified as confined-phase composites of the electric theory, equivalent to the elementary gauge bosons of the magnetic theory.

**Pedagogical note:** Present AFTER tumbling (students understand condensation) and AFTER Seiberg duality (students understand the magnetic theory has both fermions and scalars). The key exercise: map the confined-phase composites of the electric SU(N) theory to the Higgs-phase elementary particles of the magnetic SU(N_f - N_c) theory and verify quantum number matching.

**Known failure modes:**
- Complementarity is rigorous only when the Higgs VEV fully breaks the gauge group. For partial breaking (as in SU(3) x SU(2) x U(1) to SU(3) x U(1)), the argument requires more care.
- Topological obstructions can prevent smooth interpolation in some theories

**Key references:**
- Fradkin & Shenker, Phys. Rev. D19 (1979) 3682 [HIGH]
- 't Hooft, Cargese lectures (1980) [HIGH]
- Dimopoulos & Susskind, Nucl. Phys. B173 (1980) 208 [HIGH]

---

### Method 6: Holomorphy and Non-Renormalisation Theorems

**What:** In N=1 SUSY, the superpotential W is a holomorphic function of the chiral superfields. Combined with symmetry arguments, this constrains W to all orders in perturbation theory and often non-perturbatively. The Affleck-Dine-Seiberg (ADS) superpotential is the unique non-perturbative superpotential for SQCD with N_f < N_c.

**Mathematical basis:**
- Superpotential is holomorphic: W = W(Phi_i), not W(Phi_i, Phi_i^dagger)
- Symmetries + holomorphy fix W up to numerical coefficients
- NSVZ exact beta function: beta(g) = -(g^3 / 16 pi^2) * [3 T(Adj) - sum_i T(R_i)(1 - gamma_i(g))] / [1 - T(Adj) g^2 / (8 pi^2)]
- This gives the exact running of the gauge coupling in terms of anomalous dimensions

**SUSY requirement:** YES, N=1 minimum.

**Pedagogical note:** This is the engine that makes exact results possible. Present as part of the SUSY foundations lectures (Lectures 3-4 in the recommended ordering). The key pedagogical message: holomorphy + symmetry = exact answers. Without this, Seiberg duality is just a conjecture with some checks; with it, the conjecture is heavily constrained and has passed every test.

**Minimal SUSY content for the notes:**
1. Chiral and vector superfields (definitions, transformations)
2. F-term potential from superpotential
3. D-term potential from gauge invariance
4. Statement of non-renormalisation theorem (Seiberg, 1993)
5. Moduli space concept (flat directions of the potential)
6. ADS superpotential for N_f < N_c
7. NSVZ beta function (state; derive only from symmetry argument if time permits)

**Key references:**
- Seiberg, Phys. Lett. B318 (1993) 469, hep-ph/9309335 [HIGH]
- Affleck, Dine & Seiberg, Nucl. Phys. B241 (1984) 493 [HIGH]
- Intriligator & Seiberg, hep-th/9509066, Sections 3-4 [HIGH]

---

### Method 7: N=2 to N=1 Mass Deformation

**What:** Argyres, Plesser, and Seiberg (1996) showed that starting from N=2 SQCD (which is solved by Seiberg-Witten theory), one can derive N=1 Seiberg duality by adding a mass term mu Tr(Phi^2) for the adjoint chiral superfield Phi that breaks N=2 to N=1. In the limit mu -> infinity, the adjoint decouples and the theory flows to N=1 SQCD. The magnetic quarks and gluons of the N=1 theory are identified with specific massless states on the moduli space of the N=2 theory.

**Mathematical basis:**
- Start: N=2 SU(N_c) SQCD with N_f hypermultiplets (solved by SW curve)
- Deform: W = mu Tr(Phi^2) breaks N=2 to N=1
- As mu -> infinity: Phi decouples, leaving N=1 SU(N_c) SQCD
- At special points on the N=2 Coulomb branch, massless monopoles/dyons appear
- These become the magnetic quarks of the N=1 dual theory

**SUSY requirement:** YES (start with N=2, break to N=1). The N=2 structure provides the conceptual derivation of where the magnetic degrees of freedom come from.

**Pedagogical note:** This is the most intellectually satisfying explanation of WHY Seiberg duality works, but it requires N=2 SUSY background (SW theory, Coulomb branch, monopoles). For an 8-lecture course, present the LOGIC of this argument (20-30 minutes) without full derivation: "N=2 SQCD is exactly solved; deforming it to N=1 reveals the magnetic degrees of freedom as monopoles of the N=2 theory." This motivates the duality without requiring the students to do SW calculations.

**Key references:**
- Argyres, Plesser & Seiberg, hep-th/9603042 (1996) [HIGH]
- Seiberg & Witten, hep-th/9407087 (1994) [HIGH -- N=2 solution]
- Alvarez-Gaume & Hassan, Fortsch. Phys. 45 (1997) 159, hep-th/9701069 -- pedagogical SW review [HIGH]

---

### Method 8: Dualised SM Construction (Sannino Programme)

**What:** Apply Seiberg-type duality to the SM gauge groups. The UV "electric" theory contains only fermions (no elementary scalars) with a Pati-Salam-like gauge structure. The IR "magnetic" theory reproduces the SM spectrum, with the Higgs doublet emerging as a composite meson of the electric theory.

**Mathematical basis (following Sannino 1102.5100 and Cacciapaglia-Sannino 2407.17281):**

The construction proceeds in steps:
1. Start with SU(N) gauge theory with N_f Dirac fermions in the fundamental + one Weyl fermion in the adjoint (the "electric" theory)
2. The duality maps this to SU(X) with X = N_f - N, N_f dual quarks q, q-tilde, plus composite mesons M and a dual adjoint, plus mesino fields
3. For the SM application: identify SU(3)_c as a magnetic gauge group, with N_c = N_f - N for appropriate N, N_f
4. The "quasi-supersymmetric" spectrum emerges: field pairings (G_mu, lambda_m), (q, phi), (q-tilde, phi-tilde), (M, Phi_H) where the U(1)_AF charges match R-charges of would-be SUSY multiplets
5. Fermion masses are generated by Planck-scale four-fermion operators in the electric theory: (c_{abcd}/M_Pl^2)(Q_a Q-tilde_b)(Q_c Q-tilde_d)^dagger which flow to Yukawa couplings in the magnetic theory

**SUSY requirement:** The formal Seiberg duality requires N=1 SUSY. The Sannino programme conjectures that the duality persists (in modified form) after SUSY breaking, producing a "quasi-supersymmetric" spectrum. This is the central non-trivial assumption.

**Scale matching:**
- Duality scale Lambda_D: where the electric theory becomes strongly coupled
- The magnetic theory coupling: 1/alpha_elec(Lambda_D) ~ alpha_mag(Lambda_D)
- Electroweak scale: v^2 ~ xi * Lambda_D^4 / M_Pl^2 from Planck-scale operators
- QCD scale: Lambda_QCD determined by RG running of alpha_s from the duality scale
- Fermion masses: m_f ~ y_f * v, where Yukawa couplings y_f come from the flavour structure of Planck operators

**Pedagogical note:** This is the CLIMAX of the lecture notes. Present only after all machinery (Methods 1-7) is in place. The exercises should reproduce:
- m_t / v (top Yukawa ~ O(1) from leading Planck operator)
- m_b / m_t ratio (from flavour structure of higher-dimensional operators)
- v ~ 246 GeV (from Lambda_D and M_Pl through the seesaw-like formula)
- Lambda_QCD ~ 200 MeV (from RG running of alpha_s from the duality scale)

**Known failure modes:**
- The non-SUSY extension of Seiberg duality is conjectural -- it has anomaly matching support but no proof
- The quasi-supersymmetric spectrum is a prediction, not a derivation
- Precise fermion mass ratios depend on unknown O(1) coefficients in Planck-scale operators
- The flavour structure is not uniquely determined by the duality

**Key references:**
- Sannino, arXiv:1102.5100 (2011) -- SM as magnetic gauge theory [MEDIUM-HIGH]
- Cacciapaglia & Sannino, arXiv:2407.17281 (2024) -- most complete treatment [MEDIUM-HIGH]
- Maekawa, hep-ph/9509407 (1995) -- early dual SM [MEDIUM]
- Maekawa & Sato, hep-ph/9511395 (1996) -- dual SM without R-parity [MEDIUM]

---

### Method 9: RG Scale Matching and Physical Scale Extraction

**What:** Extract physical scales (v, Lambda_QCD, fermion masses) from the dual description by matching the running couplings at the duality scale and flowing down to the IR.

**Mathematical basis:**
```
Step 1: Fix Lambda_D (duality scale) from the electric theory's strong-coupling scale.
Step 2: At Lambda_D, the magnetic gauge couplings are determined by duality:
        alpha_mag(Lambda_D) = f(N_c, N_f) / alpha_elec(Lambda_D)
Step 3: Run magnetic couplings down to low energies using SM RG equations.
Step 4: The Higgs VEV v is determined by the scalar potential of the magnetic theory,
        with scalar masses generated by Planck operators:
        mu^2 ~ xi * Lambda_D^4 / M_Pl^2
Step 5: For Lambda_D ~ 10^8-10^10 GeV:
        v ~ sqrt(mu^2 / lambda) ~ sqrt(Lambda_D^4 / (M_Pl^2 * lambda))
        Choosing Lambda_D ~ 10^9 GeV, lambda ~ O(1):
        v ~ (10^9)^2 / (10^{19}) ~ 10^{-1} GeV...
        [The detailed numerics depend on precise operator coefficients]
Step 6: Lambda_QCD from running alpha_s(Lambda_D) down to the confinement scale.
```

**SUSY requirement:** No (this is IR physics, standard RG running).

**Pedagogical note:** This is the content of the quantitative exercises. The student should:
(a) Start from given values of alpha_elec at M_Pl
(b) Run down to Lambda_D using the electric beta function
(c) Apply the duality map to get magnetic couplings at Lambda_D
(d) Run SM beta functions from Lambda_D to low energies
(e) Extract v, Lambda_QCD, and fermion masses
(f) Compare with observed values

**Known failure modes:**
- Threshold corrections at the duality scale are unknown and O(1)
- The precise duality scale Lambda_D is a free parameter
- Fermion mass ratios depend on unknown Planck-scale operator coefficients

**Key references:**
- Cacciapaglia & Sannino, arXiv:2407.17281 (2024), Section on scale matching [MEDIUM]
- Standard SM RG equations: Machacek & Vaughn, Nucl. Phys. B222 (1983) 83 [HIGH]

---

## Pedagogical Ordering

The recommended ordering for an 8-lecture course, based on logical dependencies:

### Lecture 1-2: Non-Perturbative QFT Foundations (no SUSY)
**Methods used:** Anomaly matching (Method 1), Banks-Zaks / conformal window (Method 3)

**Content:**
- Review: SU(N) gauge theories, confinement, chiral symmetry breaking
- Anomalies: triangle diagrams, ABJ anomaly, gauge anomaly cancellation
- 't Hooft anomaly matching: statement, proof, QCD examples
- Exercise: verify anomaly matching for SU(3) QCD with 2 flavours
- Banks-Zaks fixed point: two-loop beta function zero
- Conformal window: definition, boundaries, physical meaning
- Phase diagram of SU(N_c) with N_f fundamentals

**Prerequisites from standard QFT:** Path integral, Feynman rules, gauge invariance, fermion representations, one-loop running of gauge couplings.

### Lecture 3-4: Minimal SUSY and Seiberg Duality
**Methods used:** Holomorphy (Method 6), Seiberg duality (Method 2)

**Content:**
- N=1 superfield formalism (chiral + vector superfields)
- Superpotential, F-terms, D-terms
- Non-renormalisation theorem (statement + symmetry argument)
- Moduli space of N=1 SQCD
- ADS superpotential for N_f < N_c
- Seiberg duality: statement, field content, superpotential
- Anomaly matching verification for Seiberg duality
- Exercise: verify all 6 anomaly coefficients match for SU(N_c) <-> SU(N_f - N_c)

**Minimal SUSY needed:** Superfields (30 min), superpotential (15 min), moduli space (15 min), non-renormalisation (15 min). Total: ~75 min of SUSY foundations, leaving ~75 min for duality.

### Lecture 5: Conceptual Derivation and Deformations
**Methods used:** N=2 to N=1 deformation (Method 7)

**Content:**
- Seiberg-Witten theory: 5-minute executive summary (state results, do not derive)
- N=2 to N=1 deformation: magnetic degrees of freedom as monopoles
- Mass deformation: adding quark masses, flowing between dual theories
- Limiting cases: N_f = N_c + 1 (confinement), N_f = N_c (quantum modified moduli space)
- Exercise: trace what happens to both electric and magnetic theories when one flavour gets a mass

### Lecture 6: Tumbling, MAC, and Complementarity
**Methods used:** MAC/Tumbling (Method 4), Complementarity (Method 5)

**Content:**
- Chiral gauge theories: why they are different from vector-like theories
- MAC criterion: one-gluon exchange, Delta C_2, condensation
- Tumbling: sequential symmetry breaking, hierarchy of scales
- Complementarity: Higgs-confinement continuity, composite = elementary
- Exercise: apply MAC to a simple SU(5) model (Georgi-Glashow type), determine condensation pattern
- Connection to the SM: why tumbling produces a mass hierarchy

### Lecture 7: The Dualised Standard Model
**Methods used:** Dualised SM construction (Method 8)

**Content:**
- Sannino's construction: electric theory with only fermions
- Pati-Salam extension as intermediate step
- Duality map: electric SU(N) -> magnetic SU(N_f - N_c)
- Identification of SM gauge groups in the magnetic theory
- Quasi-supersymmetric spectrum: field pairings and U(1)_AF charges
- Planck-scale operators and flavour structure
- Hierarchy problem: no scalars in UV -> no quadratic divergences
- Three generations: why N_f >= 3 N_c requires at least 3 families

### Lecture 8: Quantitative Spectrum and Physical Scales
**Methods used:** Scale matching (Method 9), all previous methods for validation

**Content:**
- Scale matching: Lambda_D, v, Lambda_QCD from the dual description
- Top mass: leading Planck operator gives y_t ~ O(1)
- Light fermion masses: suppressed by higher-dimensional operators
- Exercise: reproduce m_t ~ 173 GeV, v ~ 246 GeV, Lambda_QCD ~ 200 MeV (with parametric dependences)
- Collider signatures of the quasi-supersymmetric spectrum
- Open questions and future directions

---

## Pedagogical Dependencies (DAG)

```
Anomaly Matching (L1) -----> Seiberg Duality (L3-4) -----> Dualised SM (L7)
                    \                         |                     |
Banks-Zaks (L1-2) --+> Conformal Window ------+              Scale Matching (L8)
                                              |
N=1 SUSY basics (L3) > Holomorphy (L3-4) -----+
                                              |
N=2 -> N=1 (L5) -- conceptual derivation -----+
                                              |
MAC/Tumbling (L6) -----> Complementarity -----+------> Dualised SM (L7)
```

The critical path is: Anomaly matching -> SUSY basics -> Seiberg duality -> Dualised SM -> Scale matching.

Tumbling/MAC and complementarity are parallel to (and partially independent of) the SUSY track. They can be taught at any point after Lecture 2 but are best placed in Lecture 6 to provide physical intuition before the Sannino construction.

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
| -------- | ----------- | ----------- | ------- |
| Anomaly matching | 't Hooft spectator method | Index theory / descent equations | Spectator method is elementary, requires only group theory; index theory is more powerful but requires differential geometry not in Part III QFT prerequisites |
| Duality derivation | N=2 -> N=1 deformation (executive summary) | Direct derivation via string theory (brane constructions) | Brane constructions require string theory background; N=2 deformation is self-contained |
| Conformal window | Two-loop beta function + Sannino conjecture | Lattice determinations | Analytic method is more appropriate for a lecture course; lattice is computational, not analytical |
| Tumbling analysis | MAC criterion | Schwinger-Dyson gap equations | MAC is simpler, gives qualitatively correct results, and is the standard tool; SD equations are technically harder and don't improve precision enough for lecture notes |
| SM dualisation | Sannino Pati-Salam extension (2011-2024) | Chan-Tsou "Dualized SM" (dual colour) | Chan-Tsou is a different programme using loop-space dual colour, not Seiberg-type gauge-fermion duality; Sannino's is more directly connected to SQCD duality |
| SUSY presentation | Superfield formalism (minimal) | Component field formalism | Superfields are more compact and make holomorphy manifest; component formalism requires more equations for the same content |
| Pedagogical SUSY ref | Terning, "Modern Supersymmetry" | Weinberg vol 3, Wess & Bagger | Terning focuses on dynamics and duality (exactly what we need); Weinberg is encyclopedic, Wess & Bagger is too formal |

---

## What NOT to Use

| Avoid | Why | Use Instead |
| ----- | --- | ----------- |
| Full N=2 Seiberg-Witten derivation | Requires 3+ additional lectures on N=2 SUSY, elliptic curves, SW differential; completely infeasible in 8 lectures | Executive summary of SW results + mass deformation argument |
| Component SUSY formalism for foundations | More equations, obscures holomorphy which is the whole point | Superfield formalism (concise, holomorphy manifest) |
| String/brane duality constructions | Requires string theory prerequisites entirely absent from Part III QFT | Field-theory arguments for duality (anomaly matching, limiting cases, deformations) |
| Lattice Monte Carlo for conformal window | Computational technique not suited for analytical lecture notes | Perturbative beta function + analytic bounds |
| Full Schwinger-Dyson analysis for condensation | Technically demanding, not significantly more accurate than MAC for this application | MAC criterion + tumbling |
| DGLAP / parton evolution for scale matching | This is PDF evolution, not scale matching in the duality sense | Direct RG running of couplings from duality scale |

---

## Method Selection by Problem Type

**If presenting duality for a specific SU(N_c) with N_f flavours:**
- Use anomaly matching + Seiberg duality map
- Because these give the dual gauge group, matter content, and superpotential

**If determining whether duality applies to a given gauge theory:**
- Use conformal window analysis (Banks-Zaks + Sannino bounds)
- Because this determines whether the theory is in the conformal window, free magnetic phase, or confined phase

**If constructing the low-energy spectrum from the dual description:**
- Use complementarity + tumbling/MAC
- Because these map the dual theory's matter content onto observed particles

**If extracting quantitative mass scales:**
- Use RG scale matching (coupling matching at Lambda_D + SM running)
- Because this is the only method that produces numerical values for v, Lambda_QCD, m_f

**If checking whether a proposed dual theory is consistent:**
- Use 't Hooft anomaly matching (necessary condition) + limiting case analysis (deformations, mass terms)
- Because these are the strongest non-trivial tests

---

## Validation Strategy by Method

| Method | Validation Approach | Key Benchmarks |
| ------ | ------------------- | -------------- |
| 't Hooft anomaly matching | Compute all independent anomaly coefficients on both sides | 6 coefficients for SU(N_f)_L x SU(N_f)_R x U(1)_B x U(1)_R: all must match exactly |
| Seiberg duality | Mass deformation: give mass to one flavour, check both sides flow correctly | SU(N_c) with N_f -> SU(N_c) with N_f-1 on both sides |
| Banks-Zaks | Compare two-loop BZ fixed point with known exact results (SUSY) | For N=1 SQCD, exact NSVZ beta function gives gamma* = (N_f - 3N_c)/N_f at the fixed point |
| MAC/Tumbling | Check that condensation pattern is consistent with anomaly matching at each stage | Anomaly coefficients must match before and after each tumbling step |
| Scale matching | Compare extracted SM parameters with measured values | m_t ~ 173 GeV, v ~ 246 GeV, Lambda_QCD ~ 200 MeV (parametric dependences must be correct even if O(1) coefficients are free) |
| Complementarity | Global quantum numbers of confined composites match Higgs-phase elementary fields | One-to-one map with correct SU(N_f) x U(1)_B quantum numbers |

---

## Sources

### Primary References (ground truth hierarchy: Seiberg > Sannino > Csaki-Terning)

1. **Seiberg, hep-th/9411149** (1994) -- Electric-magnetic duality in N=1 SQCD. The foundational paper. [HIGH]
2. **Intriligator & Seiberg, hep-th/9509066** (1995) -- Lectures on SUSY gauge theories and duality. Best pedagogical treatment. [HIGH]
3. **Cacciapaglia & Sannino, arXiv:2407.17281** (2024) -- Charting SM duality and its signatures. Most complete treatment of the dualised SM programme. [MEDIUM-HIGH]
4. **Sannino, arXiv:1102.5100** (2011) -- SM is natural as magnetic gauge theory. Introduces the Pati-Salam dual construction. [MEDIUM-HIGH]
5. **Csaki et al., arXiv:1106.3074** (2011) -- Seiberg dual for the MSSM: partially composite W and Z. [MEDIUM-HIGH]

### Pedagogical References

6. **Terning, "Modern Supersymmetry: Dynamics and Duality"** (OUP, 2006) -- Best textbook for the dynamics and duality content. Chapters 9-12 cover anomaly matching, holomorphy, NSVZ, and Seiberg duality. [HIGH]
7. **Terning, hep-th/0306119** (TASI 2002) -- Non-perturbative SUSY lectures. 113 pages, lecture-style. [HIGH]
8. **Peskin, "Lectures on DEWSB"** (1995, SLAC-PUB-7479) -- Tumbling, MAC, technicolour. The best pedagogical review of dynamical symmetry breaking methods. [HIGH]

### Foundational Papers

9. **'t Hooft** (1980) -- Cargese lectures on naturalness and anomaly matching. [HIGH]
10. **Raby, Dimopoulos & Susskind**, Nucl. Phys. B169 (1980) 373 -- Tumbling gauge theories. [HIGH]
11. **Banks & Zaks**, Nucl. Phys. B196 (1982) 189 -- Banks-Zaks fixed point. [HIGH]
12. **Appelquist, Lane & Mahanta**, Phys. Rev. Lett. 61 (1988) 1553 -- Conformal window lower bound. [HIGH]
13. **Argyres, Plesser & Seiberg, hep-th/9603042** (1996) -- N=2 moduli space and N=1 duality derivation. [HIGH]
14. **Fradkin & Shenker**, Phys. Rev. D19 (1979) 3682 -- Higgs-confinement complementarity. [HIGH]

### Supporting References

15. **Ryttov & Sannino, arXiv:0711.3745** (2007) -- SUSY-inspired QCD beta function. [MEDIUM-HIGH]
16. **Appelquist, Fleming & Neil, arXiv:0712.0609** (2007) -- Lattice study of conformal window. [MEDIUM-HIGH]
17. **Seiberg, hep-ph/9309335** (1993) -- Naturalness vs. SUSY non-renormalisation. [HIGH]
18. **Maekawa, hep-ph/9509407** (1995) -- Duality of a SUSY SM. [MEDIUM]
19. **Maekawa & Sato, hep-ph/9511395** (1996) -- Dual SUSY SM without R-parity. [MEDIUM]

### Textbooks for Student Background

20. **Peskin & Schroeder**, "Introduction to QFT" (1995) -- QFT prerequisite. Chapters 15-19. [HIGH]
21. **Weinberg**, "Quantum Theory of Fields" vol 3 (2000) -- SUSY reference (encyclopedic). [HIGH]
22. **Tong**, "Lectures on Gauge Theory" (Cambridge) -- damtp.cam.ac.uk/user/tong/gaugetheory.html -- anomalies chapter. [HIGH]

---

_Methods research for: Dualised Standard Model lecture notes_
_Researched: 2026-03-19_
