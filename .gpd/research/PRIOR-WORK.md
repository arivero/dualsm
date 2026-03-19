# Prior Work

**Project:** The Dualised Standard Model -- Part III Lecture Notes
**Physics Domain:** Non-perturbative gauge dynamics, Seiberg duality, gauge-fermion dualities, BSM physics
**Researched:** 2026-03-19

---

## Theoretical Framework

### Governing Theory

| Framework | Scope | Key Equations | Regime of Validity |
| --------- | ----- | ------------- | ------------------ |
| N=1 SQCD Seiberg duality | Electric-magnetic duality relating SU(N_c) with N_f flavours to SU(N_f - N_c) | W_mag = (1/Lambda) M q tilde{q}; anomaly matching | Conformal window: 3N_c/2 < N_f < 3N_c |
| Non-SUSY gauge-fermion duality | Extension of Seiberg duality to non-supersymmetric gauge theories with adjoint fermions | 't Hooft anomaly matching conditions; RG flow matching | Conjectured; supported by perturbative fixed-point analysis |
| Dualised Standard Model | SM as magnetic dual of a purely fermionic electric theory | Electric SU(N) with fermions only -> magnetic SM with composite scalars | IR regime; UV electric theory confines |
| Tumbling / complementarity | Dynamical symmetry breaking via condensation in most attractive channel | MAC criterion: condensation in channel maximising alpha * C_2 | Strongly coupled chiral gauge theories |

### Mathematical Prerequisites

| Topic | Why Needed | Key Results | References |
| ----- | ---------- | ----------- | --------- |
| Representation theory of SU(N) | Classify matter content of electric and magnetic theories; decompose under subgroups for Pati-Salam embedding | Young tableaux, branching rules, Dynkin indices | Georgi, "Lie Algebras in Particle Physics" |
| 't Hooft anomaly matching | Constrains IR spectrum from UV symmetries; central tool for conjecturing dualities | Triangle anomaly coefficients must match between UV and IR descriptions | 't Hooft (1980), NATO ASI Series B 59 |
| NSVZ exact beta function | Determines conformal window boundaries in SUSY theories; guides non-SUSY generalisation | beta(g) = -(g^3/16pi^2)[3N_c - N_f(1 - gamma(g))] / [1 - N_c g^2/(8pi^2)] | Novikov, Shifman, Vainshtein, Zakharov (1983); Seiberg (1994) |
| Holomorphy and non-renormalisation theorems | Exact results constraining the superpotential in SUSY theories | W_eff determined by symmetries, holomorphy, and weak-coupling limits | Seiberg (1993), hep-ph/9309335 |
| Renormalisation group flows and fixed points | UV/IR structure of gauge theories; conformal windows, Banks-Zaks fixed points | Perturbative beta functions, scheme independence at fixed points | Banks & Zaks (1982); Caswell (1974) |
| Chiral symmetry breaking patterns | Determines how global symmetry is broken by dynamics; constrains composite spectrum | Vafa-Witten theorem, persistent mass condition | Peskin (1980); Vafa & Witten (1984) |

### Symmetries and Conservation Laws

| Symmetry | Conserved Quantity | Implications for Methods |
| -------- | ------------------ | ------------------------ |
| SU(3)_c x SU(2)_L x U(1)_Y gauge symmetry | Colour charge, weak isospin, hypercharge | Must be preserved by duality map; magnetic theory gauge group must contain SM |
| SU(N_f)_L x SU(N_f)_R global (chiral) | Axial and vector currents | Anomaly matching constrains dual matter content |
| U(1)_B baryon number | Baryon number | Maps non-trivially between electric and magnetic descriptions |
| U(1)_R (in SUSY theories) | R-charge | Constrains superpotential; determines anomalous dimensions at fixed points via a-maximisation |
| Discrete Z_{2N_f} anomaly-free subgroup | Discrete chiral symmetry | Survives instanton effects; constrains vacuum structure |

### Unit System and Conventions

- **Unit system:** Natural units (hbar = c = k_B = 1)
- **Metric signature:** (+,-,-,-) (Peskin-Schroeder / "mostly minus" convention)
- **Coupling convention:** g for gauge couplings; alpha_s = g_s^2/(4 pi) for QCD
- **Renormalisation scheme:** MS-bar for perturbative running; holomorphic scheme for SUSY exact results
- **Spinor convention:** Two-component Weyl spinors for SUSY content; four-component Dirac for SM quarks/leptons
- **Group theory normalisation:** Fundamental representation has T(fund) = 1/2; adjoint has T(adj) = N_c

**Convention warning:** Seiberg's original papers use the convention where the dual gauge group is SU(N_f - N_c). Sannino 2407.17281 applies this with specific N_c and N_f values for each SM gauge factor. The meson field M^i_j in the magnetic theory is related to the electric quarks by M ~ Q tilde{Q} / Lambda, where Lambda is the dynamical scale. The normalisation of Lambda differs between papers and must be tracked carefully.

### Known Limiting Cases

| Limit | Parameter Regime | Expected Behavior | Reference |
| ----- | ---------------- | ----------------- | --------- |
| N_f -> 3N_c (upper edge of conformal window) | Weak coupling in electric theory | Banks-Zaks fixed point; both descriptions weakly coupled; duality is trivial | Banks & Zaks (1982) |
| N_f -> 3N_c/2 (lower edge, SUSY) | Magnetic theory loses asymptotic freedom | Free magnetic phase; magnetic description is IR free | Seiberg (1994), hep-th/9411149 |
| N_f = N_c + 1 | s-confining theory | No dual gauge group; confined spectrum of mesons and baryons | Seiberg (1995), hep-th/9411149 |
| N_f < N_c + 1 | ADS superpotential generated | Runaway vacuum or SUSY breaking; no stable vacuum | Affleck, Dine, Seiberg (1984) |
| SUSY breaking -> infinity | Decouple all sparticles | Must recover ordinary QCD dynamics | Sannino & Schechter (1997), hep-th/9708113 |
| Lambda_QCD << v_EW | SM hierarchy | Electroweak and QCD sectors decouple | Standard Model |

---

## Key Parameters and Constants

| Parameter | Value | Source | Notes |
| --------- | ----- | ------ | ----- |
| v (Fermi/Higgs vev) | 246.22 GeV | PDG 2024 | Sets electroweak scale; must emerge from dual construction |
| Lambda_QCD (MS-bar, N_f=5) | ~213 MeV | PDG 2024 | QCD confinement scale |
| m_t (pole mass) | 172.57 +/- 0.29 GeV | PDG 2024 | Heaviest SM fermion; parametrically O(v) |
| alpha_s(M_Z) | 0.1180 +/- 0.0009 | PDG 2024 | Strong coupling at Z mass |
| sin^2(theta_W) | 0.23122 +/- 0.00003 | PDG 2024 | Electroweak mixing |
| N_c = 3 | Exact | -- | SU(3) colour; Seiberg dual has SU(N_f - 3) |
| N_f = 6 (quarks) | Exact | -- | Six quark flavours; for SU(3)_c duality: dual group is SU(3) |
| N_f = 3 (lepton doublets, SU(2)_L) | Exact | -- | Three lepton doublets for SU(2)_L sector |

---

## Chronological Chain of Established Results

The following traces the intellectual lineage from pre-Seiberg foundations through to Sannino's 2024 dualised SM, organized chronologically.

---

### Era 1: Pre-Seiberg Foundations (1974--1993)

#### Result 1: 't Hooft Anomaly Matching Conditions

**Statement:** In any confining gauge theory, the 't Hooft anomalies of the unbroken global symmetries computed using the fundamental (UV) fields must equal those computed using the composite (IR) fields. Specifically, if G_global has generators T^a, then Tr[T^a T^b T^c] evaluated over UV massless fermions equals the same trace over IR massless fermions.

**Proven/Conjectured:** Proven (follows from consistency of coupling background gauge fields to the global symmetry).

**Reference:** G. 't Hooft, "Naturalness, Chiral Symmetry, and Spontaneous Chiral Symmetry Breaking," in Recent Developments in Gauge Theories, NATO ASI Series B 59, pp. 135--157 (1980). Reprinted in "Under the Spell of the Gauge Principle," World Scientific, 1994.

**Relevance:** THE central tool for the entire dualised SM program. Every proposed duality must satisfy anomaly matching. Seiberg used it as the primary evidence for N=1 duality. Sannino uses it to constrain the non-SUSY dual SM spectrum. Students must master this before anything else.

**Pedagogical priority:** ESSENTIAL -- Lecture 1 or 2.

#### Result 2: Tumbling Gauge Theories and the MAC Criterion

**Statement:** In chiral gauge theories, dynamical symmetry breaking occurs preferentially in the "most attractive channel" (MAC) -- the fermion bilinear channel with the largest product alpha * C_2(R), where C_2(R) is the quadratic Casimir of the condensation channel. This can trigger a cascade ("tumbling") of successive symmetry breakings, each producing a hierarchy of mass scales.

**Proven/Conjectured:** Conjectured (motivated by one-gluon exchange, not rigorously proven; known counterexamples exist for gauge-mediated corrections).

**Reference:** S. Raby, S. Dimopoulos, and L. Susskind, "Tumbling Gauge Theories," Nucl. Phys. B 169, 373--383 (1980).

**Related:** S. Dimopoulos, S. Raby, and L. Susskind, "Light Composite Fermions," Nucl. Phys. B 173, 208--228 (1980); T. Appelquist, R. Shrock, various papers on walking technicolour.

**Relevance:** Provides the dynamical mechanism for how the UV electric theory confines and produces the IR magnetic spectrum. The MAC analysis is how one determines which condensate forms and what symmetry-breaking pattern results. Historical precursor to Seiberg's exact SUSY results.

**Pedagogical priority:** IMPORTANT -- provides physical intuition. Introduce in Lecture 2 as motivation before the exact SUSY machinery.

**Limitations:** The MAC criterion is a leading-order (one-gluon exchange) approximation. It is unreliable when multiple channels have comparable attraction, or when the gauge coupling runs slowly (near the conformal window). Seiberg's exact SUSY results supersede the MAC criterion within SUSY theories but the intuition remains valuable.

#### Result 3: Complementarity (Osterwalder-Seiler-Fradkin-Shenker)

**Statement:** In gauge-Higgs systems, the confined phase and the Higgs phase are smoothly connected -- there is no phase transition separating them when the Higgs field is in the fundamental representation. The spectrum of gauge-invariant operators can be described equivalently in either language.

**Proven/Conjectured:** Proven on the lattice (Fradkin & Shenker, 1979; Osterwalder & Seiler, 1978). Extended to chiral theories by Dimopoulos-Raby-Susskind.

**Reference:** E. Fradkin and S. Shenker, "Phase Diagrams of Lattice Gauge Theories with Higgs Fields," Phys. Rev. D 19, 3682 (1979); K. Osterwalder and E. Seiler, "Gauge Field Theories on a Lattice," Ann. Phys. 110, 440 (1978).

**Relevance:** Justifies the interpretation of the magnetic (dual) description's Higgs phase as the confinement phase of the electric theory. Critical for understanding why the dualised SM's Higgs sector is actually describing confinement of the electric quarks.

**Pedagogical priority:** USEFUL background -- mention in Lecture 2, details not required.

#### Result 4: Preskill-Weinberg Decoupling Constraints

**Statement:** Massless composite fermions in a confining theory must satisfy additional constraints beyond anomaly matching -- specifically, they must form representations consistent with the decoupling of heavy flavours. A set of 't Hooft anomaly solutions is physical only if it satisfies the "persistent mass condition": if a bare mass is added for any fermion, it must be possible to integrate it out while still satisfying anomaly matching with the reduced flavour symmetry.

**Proven/Conjectured:** Proven within the framework of effective field theory.

**Reference:** J. Preskill and S. Weinberg, "Decoupling Constraints on Massless Composite Particles," Phys. Rev. D 24, 1059 (1981).

**Relevance:** Cited in Sannino 2407.17281 as a constraint on the dual spectrum. Not all solutions of the anomaly equations are physical; only those satisfying persistent mass/decoupling conditions qualify.

**Pedagogical priority:** IMPORTANT -- builds on anomaly matching as an exercise.

---

### Era 2: Seiberg Duality (1993--1997)

#### Result 5: Seiberg Exact Results for N=1 SQCD Vacua

**Statement:** The vacuum structure of N=1 SQCD with gauge group SU(N_c) and N_f flavours of quarks Q^i, tilde{Q}_j is exactly determined by holomorphy, symmetries, and weak-coupling limits. For N_f < N_c: runaway superpotential W_dyn ~ (Lambda^{3N_c-N_f} / det M)^{1/(N_c-N_f)}. For N_f = N_c: quantum-modified moduli space (det M - B tilde{B} = Lambda^{2N_c}). For N_f = N_c + 1: s-confinement with no dynamical superpotential.

**Proven/Conjectured:** Exact within N=1 SUSY (proven using holomorphy + symmetries + limiting cases).

**Reference:** N. Seiberg, "Exact Results on the Space of Vacua of Four-Dimensional SUSY Gauge Theories," Phys. Rev. D 49, 6857 (1994), hep-th/9402044.

**Relevance:** Establishes the theoretical machinery. The vacuum structure for N_f < N_c is the Affleck-Dine-Seiberg (ADS) superpotential; for N_f >= N_c the moduli space is modified. Understanding these regimes is prerequisite for the conformal window where duality lives.

**Pedagogical priority:** ESSENTIAL -- Lectures 2-3.

#### Result 6: Seiberg Electric-Magnetic Duality for N=1 SQCD

**Statement:** SU(N_c) N=1 SQCD with N_f flavours in the conformal window (3N_c/2 < N_f < 3N_c) has a dual magnetic description: SU(N_f - N_c) gauge theory with N_f magnetic quarks q_i, tilde{q}^j and gauge-singlet mesons M^i_j, coupled through a magnetic superpotential W_mag = (1/mu) M^i_j q_i tilde{q}^j. The two descriptions flow to the same IR conformal fixed point. Evidence:
1. 't Hooft anomaly matching for SU(N_f)_L x SU(N_f)_R x U(1)_B x U(1)_R
2. Correct mapping of chiral ring operators: M^i_j <-> Q^i tilde{Q}_j / Lambda
3. Consistent with all known limits (large mass deformations, Higgsing)
4. Duality is self-consistent under successive applications ("duality of duality returns to the original theory")

**Proven/Conjectured:** Conjectured with overwhelming evidence (anomaly matching, consistency checks, holomorphic constraints, RG flow analysis). Not proven from first principles.

**Reference:** N. Seiberg, "Electric-Magnetic Duality in Supersymmetric Non-Abelian Gauge Theories," Nucl. Phys. B 435, 129--146 (1995), hep-th/9411149.

**Relevance:** THE foundational result. The entire dualised SM program rests on extending this to non-SUSY. The dual gauge group formula N_f - N_c is precisely what gives the SM gauge groups when applied with appropriate N_c and N_f values. This paper is ground truth.

**Pedagogical priority:** ESSENTIAL -- core of Lectures 3-4. This is the centrepiece of the course.

**Key structural features for lectures:**
- The meson M^i_j transforms as a bifundamental of SU(N_f)_L x SU(N_f)_R -- it maps to the Higgs doublets in the SM application
- The magnetic superpotential is cubic: W ~ M q tilde{q}. This gives a universal Yukawa coupling in the magnetic theory
- Baryon operators map non-trivially: B ~ epsilon Q^{N_c} maps to b ~ epsilon q^{N_f-N_c}
- The conformal window has three sub-regimes:
  - 3N_c/2 < N_f < 3N_c: both theories in conformal window
  - N_c+2 <= N_f <= 3N_c/2: free magnetic phase (magnetic theory IR-free)
  - N_f > 3N_c: electric theory IR-free (no interesting duality)

#### Result 7: Intriligator-Seiberg Review and Extensions

**Statement:** Comprehensive development of N=1 SUSY gauge theory dynamics, including: theories with tensor matter (antisymmetric, symmetric representations), SO(N) and Sp(2N) gauge groups, product gauge groups, chiral theories, and the role of confinement vs. Higgs phase in duality.

**Proven/Conjectured:** Various; some conjectured duals for product groups, others established.

**Reference:** K. Intriligator and N. Seiberg, "Lectures on Supersymmetric Gauge Theories and Electric-Magnetic Duality," Nucl. Phys. B Proc. Suppl. 45BC, 1--28 (1996), hep-th/9509066. Also: K. Intriligator and N. Seiberg, "Duality, Monopoles, Dyons, Confinement, and Oblique Confinement in Supersymmetric SO(N_c) Gauge Theories," Nucl. Phys. B 444, 125 (1995), hep-th/9503179.

**Relevance:** The canonical review for teaching duality. Extends beyond SU(N_c) SQCD to the gauge groups and representations needed for realistic SM model building (product groups, antisymmetric tensors). Pedagogically the most accessible treatment of Seiberg duality.

**Pedagogical priority:** ESSENTIAL as a reference -- the review is pitched at exactly the right level for Part III students.

#### Result 8: NSVZ Exact Beta Function

**Statement:** The exact beta function for N=1 SUSY gauge theories with gauge group G and matter fields Phi_i in representations R_i is:

beta(g) = -(g^3 / 16 pi^2) * [3 T(adj) - sum_i T(R_i)(1 - gamma_i(g))] / [1 - T(adj) g^2 / (8 pi^2)]

where gamma_i is the anomalous dimension of field Phi_i and T(R) is the Dynkin index.

**Proven/Conjectured:** Proven to all orders in perturbation theory for N=1 SUSY Yang-Mills; relation to holomorphic scheme demonstrated.

**Reference:** V. Novikov, M. Shifman, A. Vainshtein, and V. Zakharov, "Exact Gell-Mann-Low Function of Supersymmetric Yang-Mills Theories from Instanton Calculus," Nucl. Phys. B 229, 381 (1983). Also: M. Shifman, "Exact Results in Gauge Theories: Putting Supersymmetry to Work," hep-th/9906049 (review).

**Relevance:** Determines the conformal window boundaries exactly: the numerator vanishes (fixed point) when 3N_c = N_f at the upper end and at a non-trivial value gamma* = 1 - N_c/N_f at the lower end (N_f = 3N_c/2 follows from gamma = -1 unitarity bound in the magnetic theory). Essential for justifying when duality is expected to hold.

**Pedagogical priority:** ESSENTIAL -- derive or state the beta function in Lecture 3.

---

### Era 3: Maekawa's Dual SM Constructions (1995--1996)

#### Result 9: Maekawa -- Duality of a Supersymmetric Standard Model

**Statement:** Constructed the first explicit Seiberg dual of a supersymmetric model containing the Standard Model gauge group and matter content. Key findings: (i) the top quark naturally has a mass of order the weak scale (O(v)), while other quarks are lighter; (ii) the supersymmetric mu parameter is naturally small in the magnetic (dual) description; (iii) the dual description provides dynamical explanations for features that are unexplained inputs in the standard MSSM.

**Proven/Conjectured:** Conjectured (applies Seiberg duality to a specific SUSY model containing the SM).

**Reference:** N. Maekawa, "Duality of a Supersymmetric Standard Model," Prog. Theor. Phys. 95, 943--948 (1996).

**Relevance:** First paper to apply Seiberg duality directly to the Standard Model matter content. Established the key insight that a heavy top quark and a small mu parameter follow naturally from the dual description. Direct precursor to Sannino's program.

**Pedagogical priority:** IMPORTANT -- cite and discuss in Lecture 5 as the first SM application.

#### Result 10: Maekawa-Sato -- Duality Without R-Parity

**Statement:** Extended the dual SM construction to include lepton Yukawa couplings by relaxing R-parity. In the R-parity-conserving version, the Yukawa couplings of the lepton sector could not be generated; dropping R-parity allows lepton mass generation through the dual description.

**Reference:** N. Maekawa and J. Sato, "Duality of a Supersymmetric Standard Model without R Parity," Prog. Theor. Phys. 96, 979--984 (1996).

**Relevance:** Shows the tension between R-parity conservation and generating the full SM flavour structure in dual descriptions. This tension persists in Sannino's work and must be addressed in the lecture notes.

**Pedagogical priority:** MENTION -- cite as historical development.

#### Result 11: Maekawa-Takahashi -- Duality with Pati-Salam Group

**Statement:** Extended the dual construction to embed the SM in a Pati-Salam SU(4)_C x SU(2)_L x SU(2)_R framework. This allows lepton Yukawa couplings without dropping R-parity. The Pati-Salam breaking scale is predicted to coincide with the SUSY breaking scale.

**Reference:** N. Maekawa and T. Takahashi, "Duality of a Supersymmetric Model with the Pati-Salam Group," Prog. Theor. Phys. 95, 1167 (1996), hep-ph/9510426.

**Relevance:** The Pati-Salam embedding is exactly what Sannino 2407.17281 uses (he extends it to the non-SUSY case). This paper establishes the Pati-Salam route as the natural framework for dualising the SM.

**Pedagogical priority:** IMPORTANT -- discuss in Lecture 5 as the precursor to Sannino's construction.

---

### Era 4: Sannino's Program -- From SUSY to Non-SUSY Duality (1997--2013)

#### Result 12: Sannino-Schechter -- Toy Model for Breaking Super Gauge Theories

**Statement:** Constructed an explicit effective Lagrangian model showing how super QCD can transition to ordinary QCD when SUSY is broken. The key insight: the standard QCD degrees of freedom (pions, sigma, etc.) emerge from the auxiliary fields of the supersymmetric effective Lagrangian after SUSY breaking. Gluinos and squarks decouple below the SUSY breaking scale.

**Proven/Conjectured:** Demonstrated at the effective Lagrangian level; not a UV-complete proof.

**Reference:** F. Sannino and J. Schechter, "Toy Model for Breaking Super Gauge Theories at the Effective Lagrangian Level," Phys. Rev. D 57, 170 (1998), hep-th/9708113.

**Related:** S. D. Hsu, F. Sannino, and J. Schechter, "Anomaly Induced QCD Potential and Quark Decoupling," Phys. Lett. B 427, 300 (1998), hep-th/9801097.

**Relevance:** THIS is the paper the user specifically flagged (hep-th/9708113). It is the embryo of Sannino's entire program: the idea that one can interpolate between SUSY and non-SUSY theories while retaining structural features of the duality. The "amusing feature" where QCD degrees of freedom emerge from auxiliary fields is the physical mechanism underlying the dualised SM.

**Pedagogical priority:** IMPORTANT -- discuss in Lecture 5 as motivation for non-SUSY extensions.

**Condition:** This is a "toy model" at the effective Lagrangian level. It does not prove that Seiberg duality survives SUSY breaking at the fundamental level. The tension identified by Cheng & Shadmi (hep-th/9801146) -- that large SUSY breaking in the dual theory leads to inconsistencies with QCD expectations -- remains an open problem.

#### Result 13: Sannino -- QCD Dual (2009)

**Statement:** Proposed non-supersymmetric gauge duals for QCD, exhibiting solutions to the 't Hooft anomaly matching conditions for SU(N_c) with N_f fundamental Dirac fermions. Provided a consistent picture of the phase diagram as a function of N_c and N_f, including the conformal window and confinement/chiral symmetry breaking regimes.

**Proven/Conjectured:** Conjectured. Anomaly matching is a necessary but not sufficient condition for duality.

**Reference:** F. Sannino, "QCD Dual," Phys. Rev. D 80, 065011 (2009), arXiv:0907.1364.

**Related:** F. Sannino, "Higher Representations Duals," Nucl. Phys. B 830, 179 (2010), arXiv:0909.4584.

**Relevance:** The foundational paper for non-SUSY duality. Demonstrates that anomaly matching has non-trivial solutions for real QCD (not just SUSY QCD). Opens the door to the dualised SM.

**Pedagogical priority:** ESSENTIAL -- Lecture 6, the non-SUSY extension.

**Limitations:** Anomaly matching alone does not prove duality. In SUSY, duality is supported by holomorphy, exact beta functions, and moduli space matching. In non-SUSY, these tools are absent. The evidence is circumstantial: anomaly matching + consistency with known phases. This is the central open question.

#### Result 14: Sannino -- The Standard Model is Natural as Magnetic Gauge Theory (2011)

**Statement:** The Standard Model can be viewed as the magnetic dual of a gauge theory featuring only fermionic matter content (no elementary scalars). The electric theory is based on a Pati-Salam-like extension. Key consequences:
1. The absence of scalars in the electric theory means the hierarchy problem is absent in the UV description
2. The number of fermion generations must be at least three (follows from requiring the electric gauge group to be non-abelian: N_f - N_c >= 2)
3. The Higgs doublets are composite mesons of the electric theory
4. This provides a novel solution to the naturalness problem

**Proven/Conjectured:** Conjectured. Relies on the non-SUSY gauge duality being valid.

**Reference:** F. Sannino, "The Standard Model is Natural as Magnetic Gauge Theory," Mod. Phys. Lett. A 26, 1763--1769 (2011), arXiv:1102.5100.

**Relevance:** THE proposal that the SM IS the magnetic dual. This is the conceptual backbone of the lecture notes. Everything before this is preparation; everything after is elaboration.

**Pedagogical priority:** ESSENTIAL -- Lecture 6-7, the central claim.

**Key structural point for lectures:** For QCD with N_c = 3 and N_f = 6 (six quark flavours), the dual gauge group is SU(N_f - N_c) = SU(3). The dual theory also has SU(3) gauge symmetry but with additional composite matter (mesons = Higgs fields). This is not a coincidence -- it IS the duality.

#### Result 15: Antipin-Mojaza-Pica-Sannino -- Magnetic Fixed Points and Emergent Supersymmetry (2013)

**Statement:** In perturbation theory, the magnetic dual of QCD with an adjoint Weyl fermion and scalar matter admits multiple non-trivial fixed points along the RG flow. Among these fixed points, supersymmetric ones emerge from a generic non-supersymmetric RG flow without fine-tuning of bare couplings. The existence of non-SUSY fixed points supports gauge duality beyond SUSY.

**Proven/Conjectured:** Proven at the perturbative level (in the Veneziano limit).

**Reference:** O. Antipin, M. Mojaza, C. Pica, and F. Sannino, "Magnetic Fixed Points and Emergent Supersymmetry," JHEP 06 (2013) 037, arXiv:1105.1510.

**Relevance:** Provides the strongest perturbative evidence for non-SUSY gauge duality. The emergence of SUSY as a fixed point of a non-SUSY theory is remarkable and supports the "quasi-supersymmetric" spectrum that appears in Sannino 2407.17281.

**Pedagogical priority:** MENTION -- cite as evidence in Lecture 6.

#### Result 16: Litim-Sannino -- Asymptotic Safety Guaranteed (2014)

**Statement:** Four-dimensional gauge-Yukawa theories in the Veneziano limit (large N_c, N_f with N_f/N_c fixed) can possess perturbatively controlled interacting UV fixed points, establishing asymptotic safety (not freedom) in non-gravitational QFT. The UV fixed point is induced by the interplay of gauge, fermion, and scalar fluctuations.

**Proven/Conjectured:** Proven perturbatively in the Veneziano limit.

**Reference:** D. Litim and F. Sannino, "Asymptotic Safety Guaranteed," JHEP 12 (2014) 178, arXiv:1406.2337.

**Relevance:** Establishes that gauge-Yukawa theories can be UV-complete without asymptotic freedom. This is the theoretical underpinning for the electric theory being UV-complete in the dualised SM. The "safety" (interacting UV fixed point) replaces asymptotic freedom as the UV completion mechanism.

**Pedagogical priority:** MENTION -- context for UV completion in Lecture 7.

---

### Era 5: The Dualised Standard Model (2011--2024)

#### Result 17: Csaki-Shirman-Terning -- Seiberg Dual for the MSSM (2011)

**Statement:** Proposed that the SU(2) gauge group of the SM arises as the dual magnetic gauge group of a SUSY confining theory. In this picture:
- The Higgs and top quark are composite
- W and Z are partially composite (dual magnetic gauge bosons)
- Light fermions (u, d, s, ...) are elementary
- The effective low-energy theory is an NMSSM-type model
- The Higgs mass can reach ~400 GeV (pre-LHC prediction)

**Proven/Conjectured:** Conjectured within the SUSY framework.

**Reference:** C. Csaki, Y. Shirman, and J. Terning, "A Seiberg Dual for the MSSM: Partially Composite W and Z," Phys. Rev. D 84, 095011 (2011), arXiv:1106.3074.

**Related:** N. Craig, D. Green, and A. Katz, "Fat Higgs with Magnetic Personality," JHEP 11 (2011) 145. Y. Cui, T. Gherghetta, and J. D. Wells, "Emergent Electroweak Symmetry Breaking with Composite W, Z Bosons," JHEP 11 (2009) 080.

**Relevance:** The SUSY analogue of Sannino's non-SUSY proposal, but for SU(2)_L only. Key reference in the project's ground truth hierarchy. Shows how composite W/Z and Higgs emerge from duality. More conservative than Sannino (works within SUSY, dualises only SU(2)_L).

**Pedagogical priority:** IMPORTANT -- discuss in Lecture 5 as the SUSY version, contrast with Sannino's non-SUSY program.

#### Result 18: Cacciapaglia-Sannino -- Charting Standard Model Duality and its Signatures (2024)

**Statement:** Full construction of a gauge dual description of the Standard Model with both high-energy (electric) and low-energy (magnetic) descriptions explicitly specified. Key results:
1. **Electric theory:** Gauge dynamics with ONLY fermionic matter (no elementary scalars). Based on a Pati-Salam-like UV gauge group.
2. **Magnetic theory:** Features a "quasi-supersymmetric" spectrum -- gauge bosons, gauginos (composite fermion partners), quarks, squarks (composite scalar partners), mesinos, and composite Higgs doublets.
3. **Spectrum:** 18 Higgs doublets from the meson matrix M^i_j, whose hierarchical VEVs generate quark mass hierarchies and CKM mixing through a universal Yukawa coupling y.
4. **Flavour:** Flavour structure constructed via higher-dimensional operators generated at the Planck scale.
5. **Unification:** The duality opens new avenues for grand unification.
6. **Collider signatures:** The quasi-SUSY spectrum is testable at colliders, with characteristic mass relations differing from standard SUSY predictions.
7. **Three generations:** The requirement that the electric gauge group be non-abelian (N_f - N_c >= 2) naturally explains why N_gen >= 3.

**Proven/Conjectured:** Conjectured. Built on the assumption that non-SUSY gauge duality holds.

**Reference:** G. Cacciapaglia and F. Sannino, "Charting Standard Model Duality and its Signatures," arXiv:2407.17281 (2024).

**Relevance:** THE primary reference for these lecture notes. This paper IS the dualised SM that the course teaches. All previous results are preparation for understanding this construction.

**Pedagogical priority:** ESSENTIAL -- Lectures 7-8, the culmination.

**Key features for exercises:**
- The meson matrix Phi_H contains 9 complex bi-doublets, of which 18 real Higgs doublets contribute to EWSB
- Universal Yukawa coupling y in the magnetic theory means flavour hierarchy comes entirely from the VEV structure, not from different Yukawa couplings
- For QCD: electric SU(N) with N_f = 6 -> magnetic SU(3) = SU(3)_c with composite mesons
- The top mass m_t ~ y * v is naturally O(v) because y ~ O(1)
- Lighter quarks get masses from hierarchically suppressed VEVs of higher-generation meson components

---

### Additional Key Results

#### Result 19: Seiberg-Witten Exact Solution for N=2 SYM

**Statement:** Exact low-energy effective action for N=2 SU(2) SYM determined by a family of elliptic curves (the Seiberg-Witten curve). Demonstrates exact electric-magnetic duality with monopole and dyon condensation driving confinement.

**Reference:** N. Seiberg and E. Witten, "Electric-Magnetic Duality, Monopole Condensation, and Confinement in N=2 Supersymmetric Yang-Mills Theory," Nucl. Phys. B 426, 19 (1994), hep-th/9407087. Part II: Nucl. Phys. B 431, 484 (1994), hep-th/9408099.

**Relevance:** Historical precursor demonstrating exact duality in gauge theories. Provides the most rigorous example of electric-magnetic duality, but N=2 is too constrained for realistic SM model building (non-chiral matter). The N=1 Seiberg duality is more directly relevant.

**Pedagogical priority:** MENTION briefly -- cite as rigorous example but note it is N=2 (too much SUSY for SM).

#### Result 20: de Gouvea-Friedland-Murayama -- Seiberg Duality and e+e- Experiments

**Statement:** Cross sections for e+e- -> "hadrons" computed in both electric and magnetic descriptions agree in the IR, as guaranteed by anomaly matching. However, UV behaviour differs. This provides an in-principle experimental test of duality.

**Reference:** A. de Gouvea, A. Friedland, and H. Murayama, "Seiberg Duality and e+e- Experiments," hep-th/9810020 (1998).

**Relevance:** Demonstrates that duality has physical (measurable) consequences, not just formal mathematical interest. Suitable for an exercise.

**Pedagogical priority:** EXERCISE potential.

#### Result 21: Hill-Machado-Thomsen-Turner -- Scalar Democracy

**Statement:** If multiple Higgs doublets exist and share a common Yukawa coupling, the fermion mass hierarchy can be generated entirely from the hierarchy of Higgs VEVs, without Yukawa coupling hierarchy. Called "scalar democracy."

**Reference:** C. Hill, P. Machado, A. Thomsen, and J. Turner, "Scalar Democracy," Phys. Rev. D 100, 015015 (2019).

**Relevance:** Directly relevant to the mechanism in Sannino 2407.17281, where a universal Yukawa y couples all flavours to the meson matrix, and the mass hierarchy comes from hierarchical VEVs. This is the mathematical implementation of how 18 Higgs doublets generate the observed mass spectrum.

**Pedagogical priority:** IMPORTANT -- Lecture 8, the flavour structure.

---

## Open Problems Relevant to This Project

### Open Problem 1: Rigorous Foundation for Non-SUSY Gauge Duality

**Statement:** Does Seiberg duality (or any non-trivial IR equivalence) survive in the absence of supersymmetry? In SUSY, duality is established through holomorphy, exact beta functions, and moduli space analysis. No analogous tools exist in non-SUSY theories. The evidence is: (a) 't Hooft anomaly matching, (b) consistent phase diagrams, (c) perturbative fixed points in the magnetic theory. None of these individually or collectively constitute a proof.

**Why it matters:** The entire dualised SM program rests on this assumption. If non-SUSY duality fails, the SM-as-magnetic-dual interpretation collapses.

**Current status:** Conjectured. Supported by (i) anomaly matching solutions (Sannino 2009), (ii) perturbative fixed points (Antipin et al. 2013), (iii) emergent SUSY at fixed points, (iv) lattice studies of the conformal window in SU(3) with multiple flavours (ongoing, inconclusive for duality). No proof or disproof exists.

**Key references:** Sannino (2009), arXiv:0907.1364; Antipin et al. (2013), arXiv:1105.1510; Cheng & Shadmi (1998), hep-th/9801146.

**Pedagogical approach:** Present honestly as a conjecture. Emphasise that anomaly matching is necessary but not sufficient. Compare with SUSY case where much stronger evidence exists.

### Open Problem 2: Quantitative Fermion Mass Predictions

**Statement:** Does the dualised SM produce the observed fermion mass spectrum quantitatively, or only qualitatively? The universal Yukawa + hierarchical VEV mechanism (scalar democracy) can reproduce the hierarchy parametrically, but the specific VEV ratios must be inputs (generated by Planck-scale operators). The question is whether these inputs are determined by the theory or remain free parameters.

**Why it matters:** The user's acceptance criterion requires exercises that "reproduce physical SM spectrum." If the mass spectrum is only qualitatively correct, the exercise framework needs revision.

**Current status:** In Sannino 2407.17281, the flavour structure is constructed via higher-dimensional operators at the Planck scale. The VEV hierarchy is parameterised, not derived. The top mass m_t ~ y * v is a robust prediction (O(1) Yukawa with a single dominant VEV). Lighter masses depend on the VEV ratios, which are inputs from the Planck-scale flavour theory.

**Key references:** Cacciapaglia & Sannino (2024), arXiv:2407.17281; Hill et al. (2019).

**Pedagogical approach:** Frame exercises as: "Given the VEV structure, derive the mass spectrum." The VEV hierarchy is the input; the mass predictions are the output. This is honest and produces quantitative results.

### Open Problem 3: Fate of Duality Under Large SUSY Breaking

**Statement:** When soft SUSY-breaking terms are added to Seiberg-dual theories, the mapping between electric and magnetic soft terms is poorly understood. Cheng & Shadmi (1998) showed that in the limit of large SUSY breaking, the magnetic theory's scalar spectrum becomes inconsistent with QCD expectations.

**Why it matters:** The non-SUSY dualised SM implicitly takes the limit of infinite SUSY breaking. If duality fails in this limit, the entire construction is questionable.

**Current status:** Unresolved. Sannino's approach sidesteps this by postulating non-SUSY duality directly (not as a limit of broken SUSY). But the tension identified by Cheng & Shadmi remains a theoretical concern.

**Key references:** Cheng & Shadmi (1998), hep-th/9801146; Sannino & Schechter (1998), hep-th/9708113.

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
| -------- | ----------- | ----------- | ------- |
| Duality framework | Non-SUSY gauge-fermion duality (Sannino) | Chan-Tsou loop-space "Dualized Standard Model" (hep-th/9712171) | Different program entirely: Chan-Tsou's duality is a loop-space generalisation of Hodge duality, not Seiberg-type electric-magnetic duality. Not connected to conformal windows or anomaly matching. The name collision is unfortunate. |
| UV completion | Pati-Salam embedding of the electric theory | Direct SU(5) or SO(10) GUT embedding | Sannino 2407.17281 shows Pati-Salam is the natural framework; SU(5)/SO(10) would require different matter content in the electric theory |
| Duality basis | N=1 Seiberg duality (SU(N_c) SQCD) | N=2 Seiberg-Witten | N=2 gives non-chiral matter; cannot accommodate SM chiral fermions without additional breaking; too constrained for SM model building |
| Non-SUSY approach | Direct non-SUSY duality conjecture | Take SUSY duality + break SUSY softly | Cheng-Shadmi tension at large breaking; direct non-SUSY approach is cleaner for the SM application |
| Flavour mechanism | Scalar democracy (universal Yukawa + hierarchical VEVs) | Froggatt-Nielsen horizontal symmetry | Scalar democracy is the mechanism that naturally arises from the duality (meson matrix has universal coupling); Froggatt-Nielsen is an alternative but does not follow from the duality structure |
| Hierarchy solution | Absence of UV scalars in electric theory | Technicolour / composite Higgs | The dualised SM IS a form of compositeness (Higgs = meson), but the dual description provides more structure than generic technicolour |

---

## Key References

### Foundational -- Ground Truth Hierarchy

| Reference | arXiv/DOI | Type | Relevance |
| --------- | --------- | ---- | --------- |
| Seiberg (1995) | hep-th/9411149 | Seminal paper | THE duality. Electric-magnetic duality in N=1 SQCD. Ground truth tier 1. |
| Cacciapaglia & Sannino (2024) | 2407.17281 | Research paper | THE dualised SM construction. Primary backbone. Ground truth tier 2. |
| Csaki, Shirman & Terning (2011) | 1106.3074 | Research paper | Seiberg dual for the MSSM. SUSY version. Ground truth tier 3. |

### Foundational -- Pre-Seiberg

| Reference | arXiv/DOI | Type | Relevance |
| --------- | --------- | ---- | --------- |
| 't Hooft (1980) | NATO ASI B 59, p.135 | Lecture notes | Anomaly matching conditions and naturalness |
| Raby, Dimopoulos & Susskind (1980) | Nucl. Phys. B 169, 373 | Research paper | Tumbling gauge theories and MAC criterion |
| Preskill & Weinberg (1981) | Phys. Rev. D 24, 1059 | Research paper | Decoupling constraints on massless composites |
| Fradkin & Shenker (1979) | Phys. Rev. D 19, 3682 | Research paper | Complementarity / Higgs-confinement continuity |

### Foundational -- Seiberg Era

| Reference | arXiv/DOI | Type | Relevance |
| --------- | --------- | ---- | --------- |
| Seiberg (1994a) | hep-th/9402044 | Research paper | Exact results on vacua of N=1 SUSY gauge theories |
| Seiberg (1995) | hep-th/9411149 | Research paper | Electric-magnetic duality in N=1 SQCD |
| Intriligator & Seiberg (1996) | hep-th/9509066 | Review | Lectures on SUSY gauge theories and duality |
| Novikov, Shifman, Vainshtein & Zakharov (1983) | Nucl. Phys. B 229, 381 | Research paper | NSVZ exact beta function |
| Seiberg & Witten (1994a) | hep-th/9407087 | Research paper | Exact solution for N=2 SU(2) SYM |

### Maekawa's SM Applications

| Reference | arXiv/DOI | Type | Relevance |
| --------- | --------- | ---- | --------- |
| Maekawa (1996) | Prog. Theor. Phys. 95, 943 | Research paper | First Seiberg dual of the SUSY SM |
| Maekawa & Sato (1996) | Prog. Theor. Phys. 96, 979 | Research paper | Dual SUSY SM without R-parity |
| Maekawa & Takahashi (1996) | hep-ph/9510426 | Research paper | Dual with Pati-Salam group |

### Sannino's Program

| Reference | arXiv/DOI | Type | Relevance |
| --------- | --------- | ---- | --------- |
| Sannino & Schechter (1998) | hep-th/9708113 | Research paper | Breaking super gauge theories at effective Lagrangian level |
| Sannino (2009) | 0907.1364 | Research paper | QCD dual -- non-SUSY anomaly matching solutions |
| Sannino (2010) | 0909.4584 | Research paper | Higher representations duals |
| Sannino (2011) | 1102.5100 | Research paper | SM is natural as magnetic gauge theory |
| Antipin, Mojaza, Pica & Sannino (2013) | 1105.1510 | Research paper | Magnetic fixed points and emergent SUSY |
| Litim & Sannino (2014) | 1406.2337 | Research paper | Asymptotic safety guaranteed in gauge-Yukawa |

### Additional Important References

| Reference | arXiv/DOI | Type | Relevance |
| --------- | --------- | ---- | --------- |
| Terning (2006) | ISBN 9780198567639 | Textbook | "Modern Supersymmetry: Dynamics and Duality" -- pedagogical treatment |
| de Gouvea, Friedland & Murayama (1998) | hep-th/9810020 | Research paper | Seiberg duality and e+e- experiments |
| Cheng & Shadmi (1998) | hep-th/9801146 | Research paper | Duality in presence of SUSY breaking |
| Hill, Machado, Thomsen & Turner (2019) | Phys. Rev. D 100, 015015 | Research paper | Scalar democracy mechanism |
| Pati & Salam (1974) | Phys. Rev. D 10, 275 | Research paper | Lepton number as the fourth colour |

### Review Articles

| Reference | arXiv/DOI | Type | Relevance |
| --------- | --------- | ---- | --------- |
| Intriligator & Seiberg (1996) | hep-th/9509066 | Review | Best pedagogical review of Seiberg duality |
| Peskin (1997) | hep-th/9702094 | Review | "Duality in Supersymmetric Yang-Mills Theory" |
| Shifman (1999) | hep-th/9906049 | Review | Exact results in gauge theories |
| Strassler (2003) | hep-th/0505153 | Review | The duality cascade |

---

## Confidence Assessment

| Area | Confidence | Notes |
| ---- | ---------- | ----- |
| Seiberg duality (N=1 SQCD) | HIGH | Established result with 30 years of consistency checks |
| 't Hooft anomaly matching | HIGH | Proven; standard tool |
| Non-SUSY duality conjecture | LOW-MEDIUM | Conjectured with suggestive evidence; no proof |
| Maekawa's SUSY SM dual | MEDIUM | Published in Prog. Theor. Phys.; specific construction |
| Sannino's dualised SM (2024) | MEDIUM | Recent preprint by established researcher; not yet widely verified |
| Quantitative fermion mass predictions | LOW | VEV hierarchy is input, not derived from the duality |
| Emergent SUSY at fixed points | MEDIUM | Perturbative result in Veneziano limit |
| Dvali's specific N=2 breaking contributions | LOW | Could not locate specific early 1990s papers on N=2 breaking to SM; Dvali's main contributions appear to be anomalous U(1) and hierarchy problem rather than dual SM descriptions |

---

## Note on Dvali

The user flagged "pre-Seiberg N=2 breaking tricks by Dvali (early-mid 1990s)." After extensive search, Dvali's primary contributions from this period appear to be:
- Anomalous U(1) as mediator of SUSY breaking (with Pomarol, 1996, hep-ph/9607383)
- Role of anomalous U(1) for doublet-triplet splitting (1996, hep-ph/9610431)
- Family symmetry and fermion mass matrices (with Pokorski, 1995)
- Much later: extra dimensions and hierarchy problem (with Dimopoulos, Dvali, 1998, hep-ph/9803315)

These are important contributions to BSM physics but are NOT directly in the Seiberg duality -> dualised SM chain. Dvali's work on anomalous U(1) and SUSY breaking is tangential: it addresses how SUSY breaking communicates to the visible sector, not how gauge duality describes the SM.

If the user has a specific Dvali paper in mind about N=2 breaking to produce SM-like spectra through duality, the arXiv ID would help. The paper hep-th/9708113 that was flagged is actually Sannino & Schechter, not Dvali.

---

## Note on Chan-Tsou "Dualized Standard Model"

The paper hep-th/9712171 ("Standard Model with Duality: Theoretical Basis") by H.M. Chan and S.T. Tsou is a DIFFERENT program from Sannino's dualised SM. Chan-Tsou construct a nonabelian generalisation of Hodge duality in loop space and apply it to the SM. This is a geometric/topological duality, not a Seiberg-type electric-magnetic duality operating in the conformal window. The name collision is confusing but the physics is entirely distinct. Chan-Tsou's program generates fermion mass hierarchy through a "rotating mass matrix" mechanism and has a separate literature (see also hep-ph/0303010 by Chan and Tsou on "Fermion Generations and Mixing from Dualized Standard Model").

For these lecture notes, Chan-Tsou's program is OUT OF SCOPE. Mention only to disambiguate.
