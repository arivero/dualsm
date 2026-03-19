# Known Pitfalls Research

**Domain:** Gauge-fermion dualities, Seiberg duality, dualised Standard Model, anomaly matching, conformal window analysis
**Researched:** 2026-03-19
**Confidence:** MEDIUM-HIGH

---

## Critical Pitfalls

### Pitfall 1: Confusing the conjectural status of non-SUSY duality with established SUSY results

**What goes wrong:**
In N=1 SUSY SQCD, Seiberg duality is established through multiple independent checks: holomorphy, the NSVZ exact beta function, 't Hooft anomaly matching, superconformal index matching, and consistency with known limits (large-N, large-N_f). When extending to non-supersymmetric theories --- as the dualised SM program requires --- none of these non-perturbative guarantees survive intact. The NSVZ beta function has no non-SUSY analog; holomorphic control of the superpotential is absent; the superconformal index is undefined. Presenting non-SUSY duality with the same confidence as SUSY duality is a critical error that will mislead students about what is proven versus what is conjectured.

**Why it happens:**
The Seiberg duality in SUSY is so well-established and elegant that it is tempting to assume the same level of rigour carries over when SUSY is softly broken or when non-SUSY analogs are constructed. Cacciapaglia and Sannino (2407.17281) explicitly present the SM as being "interpreted as the magnetic dual" --- they investigate and pursue, but do not claim a proof. However, downstream presentations may lose this qualification.

**How to avoid:**
- State the epistemic status explicitly at every stage: "In SUSY, Seiberg duality is established by [list]. In the non-SUSY extension, the evidence is [anomaly matching, large-N planar equivalence, lattice indications] but not a proof."
- Separate lectures on SUSY duality (where everything works) from the non-SUSY extension (where it is a conjecture motivated by those results).
- When presenting 't Hooft anomaly matching as evidence for non-SUSY duality, emphasise that anomaly matching is a necessary but not sufficient condition --- it constrains the spectrum but does not prove the duality.

**Warning signs:**
- Students treating the dual description as "the UV completion of the SM" rather than as a conjectured dual description.
- Exercises producing "predictions" from the dual theory without any caveat about the conjectural status.
- Statements like "the duality shows that..." rather than "if the duality holds, then..."

**Phase to address:**
The foundational lectures on Seiberg duality (Lectures 2-3) must establish the SUSY case cleanly. The transition to non-SUSY (Lectures 5-6) must include an explicit "what we lose" discussion.

**References:**
- Seiberg, hep-th/9411149 (original SUSY duality, established)
- Intriligator and Seiberg, hep-th/9509066 (pedagogical review of the SUSY case)
- Cacciapaglia and Sannino, arXiv:2407.17281 (the dualised SM --- conjectural extension)
- Armoni, Shifman, Unsal, arXiv:0801.0762 (non-SUSY duality via orientifold planar equivalence --- finite-N validity unclear)

---

### Pitfall 2: Treating fermion mass predictions as quantitative when they are qualitative

**What goes wrong:**
The dualised SM (2407.17281) generates fermion masses through a mechanism involving 18 Higgs doublets with hierarchical VEVs, where the hierarchy descends from Planck-scale four-fermion operators. The mass ratios are expressed parametrically (e.g., m_b/m_t ~ v_2/v, m_light ~ mu^4/M^4 * v), but the numerical coefficients are unspecified. Presenting these as "quantitative predictions reproducing m_t ~ 173 GeV" goes beyond what the paper actually delivers.

**Why it happens:**
The PROJECT.md acceptance criterion states "exercises reproduce m_t ~ 173 GeV, v ~ 246 GeV, Lambda_QCD ~ 200 MeV with correct parametric dependences." The phrase "correct parametric dependences" is the operative one, but it is easy to slide from "parametric" to "quantitative" --- especially when writing exercises that produce numbers.

**How to avoid:**
- Distinguish sharply between (a) parametric scaling: the duality explains *why* there is a hierarchy, and (b) numerical values: these require inputting measured SM parameters, not deriving them from the duality alone.
- Exercises should demonstrate: "Given the observed top Yukawa coupling y_t ~ 1, and the duality relation Y = y <H>/v, show that the top mass of order v is natural in this framework." This is parametric consistency, not prediction.
- Do not claim the dualised SM "predicts" m_t = 173 GeV. It provides a framework in which m_t ~ O(v) is natural, and the hierarchy m_b << m_t follows from the VEV hierarchy.

**Warning signs:**
- Exercises that produce specific mass values without inputting any measured parameter.
- Language like "the dual theory predicts m_t = 173 GeV" rather than "the dual theory is consistent with m_t ~ v."
- Students believing the duality predicts more than it does.

**Phase to address:**
The exercises chapter (Lectures 7-8) and the chapter on the SM spectrum from the duality (Lecture 6-7). The scoping contract's acceptance criterion should be reinterpreted as: exercises demonstrate parametric matching with correct scaling, using measured inputs where needed.

**References:**
- Cacciapaglia and Sannino, arXiv:2407.17281, Eq. (11), (15), (23): parametric scaling of mass matrices
- PROJECT.md "Skeptical Review" section correctly flags this as the weakest anchor

---

### Pitfall 3: Conflating 't Hooft anomaly matching (global anomaly constraints) with gauge anomaly cancellation

**What goes wrong:**
These are fundamentally different objects:
1. **Gauge anomaly cancellation** (ABJ anomaly for gauged symmetries): Required for consistency of the quantum theory. If gauge anomalies do not cancel, the theory is inconsistent. This is a constraint on the UV theory's field content.
2. **'t Hooft anomaly matching** (anomalies of global symmetries): The 't Hooft anomaly of a global symmetry must match between UV and IR descriptions. This is a constraint relating two descriptions of the same physics; it is a diagnostic tool, not a consistency requirement on either description alone.

Confusion between these leads to two errors: (a) treating anomaly matching as "anomaly cancellation in the dual theory" (wrong --- the anomalies do NOT cancel, they must MATCH), and (b) concluding that anomaly matching proves the duality (wrong --- it is necessary but not sufficient).

**Why it happens:**
Both involve computing Tr[T^a {T^b, T^c}] for various symmetry generators. The calculation looks identical; only the interpretation differs. Textbooks sometimes present both in the same chapter without sharply distinguishing them. Students who have learned anomaly cancellation in the SM course may assume anomaly matching is the same thing.

**How to avoid:**
- Dedicate a full subsection (or lecture segment) to the distinction. Use a table:

| | Gauge anomaly cancellation | 't Hooft anomaly matching |
|---|---|---|
| Symmetry type | Gauged | Global |
| Requirement | Must vanish (cancel) | Must be equal in UV and IR |
| Physical meaning | Consistency of gauge theory | Constraint on IR spectrum |
| What it tells you | Theory is well-defined | Which massless fermions can appear in IR |

- Present anomaly matching AFTER gauge anomaly cancellation, so students see the familiar object first.
- Use worked examples: show that anomaly cancellation in the SM (the familiar case) is conceptually distinct from anomaly matching between electric and magnetic theories (the new case in Seiberg duality).

**Warning signs:**
- Students writing "the anomalies cancel between electric and magnetic quarks" (wrong: the anomalies MATCH).
- Confusion about whether the anomaly coefficients should vanish or should be equal.
- Inability to state what anomaly matching tells you (it constrains the massless spectrum, it does not prove the duality).

**Phase to address:**
Lecture on anomaly matching (Lecture 3-4), which must follow the SM anomaly cancellation review.

**References:**
- 't Hooft, in "Recent Developments in Gauge Theories," Cargese 1979 (original anomaly matching argument)
- Tong, "Gauge Theory" lectures, Ch. 3 (https://www.damtp.cam.ac.uk/user/tong/gaugetheory/3anom.pdf) -- clear pedagogical distinction
- Preskill, "Gauge Anomalies in an Effective Field Theory," Ann. Phys. 210, 323 (1991) -- rigorous treatment

---

### Pitfall 4: Applying Seiberg duality outside the conformal window

**What goes wrong:**
Seiberg duality for N=1 SU(N_c) SQCD with N_f flavours is established in the conformal window 3N_c/2 < N_f < 3N_c. Outside this range:
- For N_f < N_c + 1: the theory has a runaway superpotential (Affleck-Dine-Seiberg). No stable vacuum exists.
- For N_c + 1 <= N_f <= 3N_c/2: the magnetic theory is strongly coupled. The duality still relates the two theories, but the magnetic description is not weakly coupled and not directly useful.
- For N_f >= 3N_c: both theories are IR free (trivial in the IR).

The SM has SU(3) with N_f = 6 quarks. Since 3*3/2 = 4.5 and 3*3 = 9, we have 4.5 < 6 < 9, so ordinary QCD is formally inside the SUSY conformal window. However, the SM is NOT supersymmetric, and the non-SUSY conformal window is different (the lower boundary is debated: estimates range from N_f ~ 8 to N_f ~ 12 for SU(3), with lattice evidence suggesting N_f = 8 is below the conformal window and N_f = 12 is at or near the lower boundary). The dualised SM sidesteps this by working with larger gauge groups in the UV electric theory.

**Why it happens:**
The conformal window analysis is one of the most technically demanding parts of the subject. The SUSY conformal window has clean boundaries (set by the NSVZ beta function and unitarity bounds on R-charges). The non-SUSY conformal window is determined by the two-loop beta function at best, with lattice input needed for precision.

**How to avoid:**
- Present the SUSY conformal window with exact boundaries first.
- Then present the non-SUSY estimates (Caswell-Banks-Zaks fixed point, Ryttov-Sannino all-orders beta function ansatz, ladder/Schwinger-Dyson approximation).
- Make clear that the non-SUSY boundaries are approximate and model-dependent.
- When applying to the SM, specify exactly which gauge group and which matter content is being dualised, and verify that the claimed UV theory is inside or near the conformal window.

**Warning signs:**
- Citing the SUSY conformal window bounds 3N_c/2 < N_f < 3N_c for a non-SUSY theory.
- Not checking whether the electric theory is in the regime where duality is expected to apply.
- Ignoring the lattice controversy about N_f = 8 vs N_f = 12 for SU(3).

**Phase to address:**
Lecture on the conformal window (Lecture 4-5). The non-SUSY extension lecture must address this.

**References:**
- Seiberg, hep-th/9411149, Sec. 5 (conformal window for SQCD)
- Ryttov and Sannino, arXiv:0711.3745 (SUSY-inspired all-orders beta function for non-SUSY theories)
- LatKMI Collaboration, arXiv:2401.00267 (lattice evidence for SU(3) N_f=8 near conformal window, 2024)
- Appelquist et al., Phys. Rev. Lett. 100, 171607 (2008) (early lattice study of conformal window)
- Sannino, arXiv:2111.09690 (broken conformal window analysis)

---

### Pitfall 5: Confusing tumbling/complementarity with Seiberg duality

**What goes wrong:**
Three distinct phenomena are often muddled:
1. **Seiberg duality:** An IR equivalence between an "electric" SU(N_c) theory and a "magnetic" SU(N_f - N_c) theory with specific matter content and a mapped superpotential. The two theories have different UV descriptions but the same IR physics.
2. **Tumbling/most attractive channel (MAC):** A dynamical scenario where the most strongly interacting channel of a chiral gauge theory forms a condensate, breaking the gauge symmetry to a subgroup, and the process repeats ("tumbles") until confinement. This is a dynamical mechanism, not a duality.
3. **Complementarity (Osterwalder-Seiler, Fradkin-Shenker):** The statement that in certain gauge-Higgs systems, the confining phase and the Higgs phase are continuously connected (no phase transition separating them). This is a statement about phases, not about equivalent descriptions.

Confusing these leads to wrong claims: "tumbling produces the dual description" (it does not --- tumbling is a dynamical mechanism within a single description) or "complementarity means electric = magnetic" (it does not --- complementarity relates different phases of the same theory, while duality relates different theories).

**Why it happens:**
All three involve strongly coupled gauge dynamics and non-perturbative phenomena. The dualised SM program uses all three ideas: Seiberg duality to construct the magnetic theory, tumbling (condensation) to drive symmetry breaking in the electric theory, and complementarity to argue that the confining and Higgs phases describe the same physics. A naive reader may conflate them.

**How to avoid:**
- Introduce each concept in a separate lecture or section with a clear definition.
- Provide a comparison table:

| Concept | What it relates | Key claim | Status |
|---|---|---|---|
| Seiberg duality | Electric theory <-> Magnetic theory | Same IR physics, different UV | Proven (SUSY) / Conjectured (non-SUSY) |
| Tumbling/MAC | Condensate channel within one theory | Most attractive channel condenses | Conjecture; known to fail in some cases |
| Complementarity | Confining phase <-> Higgs phase | Same physical phase | Proven in certain gauge-Higgs systems |

- When applying to the dualised SM, clearly label which concept is being invoked at each step.

**Warning signs:**
- Students saying "the SM is the tumbled version of the electric theory" when they mean "the SM is the Seiberg dual."
- Using "complementarity" and "duality" interchangeably.
- Not recognizing that the MAC hypothesis can fail (it is not a theorem).

**Phase to address:**
Lecture introducing non-perturbative dynamics (Lecture 2), and the lecture applying these to the SM (Lecture 6).

**References:**
- Raby, Dimopoulos, Susskind, Nucl. Phys. B169, 373 (1980) (tumbling)
- Osterwalder and Seiler, Ann. Phys. 110, 440 (1978) (complementarity)
- Fradkin and Shenker, Phys. Rev. D19, 3682 (1979) (complementarity)
- Terning, "Modern Supersymmetry," Ch. 9 (Seiberg duality), Ch. 12 (tumbling and chiral theories)

---

## Moderate Pitfalls

### Pitfall 6: Assuming SUSY background when the audience has none

**What goes wrong:**
The standard pedagogy for Seiberg duality (Intriligator-Seiberg lectures, Terning textbook, Csaki TASI lectures) assumes the reader knows: superfields (chiral, vector), the superpotential, holomorphy, the NSVZ beta function, R-symmetry, and moduli spaces of SUSY vacua. None of this is available to Part III students taking this as their first beyond-SM course.

**Prevention:**
- Build the duality argument in two stages: first as a purely group-theoretic statement about gauge invariant operators and anomaly matching (no SUSY needed), then show how SUSY provides additional evidence (holomorphy, the exact beta function) as a "bonus" structure.
- Introduce only the minimum SUSY concepts needed: the superpotential as a holomorphic function constraining the dynamics, and the NSVZ beta function as the reason we trust the SUSY conformal window boundaries. These can be presented as black boxes for the purposes of the course.
- Test the exposition: can a student who knows only canonical QFT (Peskin-Schroeder level) follow each derivation?

**Warning signs:**
- References to "F-terms" or "D-terms" without definition.
- Using the language of "the moduli space" without explaining that it means the space of vacuum expectation values.
- Citing the non-renormalization theorem without explaining what it says.

**Phase to address:**
Lecture 1-2 (foundations), and throughout --- every SUSY concept used must be defined where first used.

---

### Pitfall 7: Naive analogy between EM duality (Maxwell) and non-abelian Seiberg duality

**What goes wrong:**
Students naturally extrapolate from the familiar statement "Maxwell's equations are symmetric under E -> B, B -> -E" to non-abelian gauge theories. This analogy breaks down in multiple ways:
1. **No magnetic gauge potential in Maxwell theory:** EM duality in vacuum exchanges field strengths, not gauge potentials. There is no "dual gauge field" in the abelian theory (unless you introduce magnetic monopoles).
2. **Strong-weak coupling exchange:** Seiberg duality exchanges strong and weak coupling. EM duality in vacuum is an exact symmetry at all coupling strengths (it acts on the free theory).
3. **Different gauge groups:** In Seiberg duality, the dual theory has a different gauge group SU(N_f - N_c) from the original SU(N_c). EM duality maps U(1) to U(1).
4. **Matter content changes:** The dual theory has different matter content (dual quarks + meson singlets) compared to the original (quarks only). In EM duality, there is no matter to map.
5. **Non-abelian monopoles:** The "magnetic" degrees of freedom in Seiberg duality are loosely analogous to non-abelian magnetic monopoles, but these are not point particles --- they are the elementary fields of the dual gauge theory.

**Prevention:**
- Present EM duality in Lecture 1 as motivation only, then immediately list the ways the non-abelian case differs.
- A good exercise: "List three ways in which Seiberg duality differs from classical EM duality."
- Emphasise that "electric" and "magnetic" in Seiberg duality are names for the two descriptions, not literal E and B fields.

**Warning signs:**
- Students drawing Dirac monopole diagrams when discussing Seiberg duality.
- Questions like "what is the magnetic charge of a dual quark?"
- Attempts to derive Seiberg duality from Maxwell's equations.

**Phase to address:**
Lecture 1 (motivating duality from EM) and Lecture 2 (Seiberg duality proper).

---

### Pitfall 8: The Chan-Tsou "Dualized Standard Model" is a different program

**What goes wrong:**
There are (at least) two distinct programs that go by the name "dualised/dualized standard model":
1. **Chan and Tsou (late 1990s-2000s):** Based on a non-abelian generalisation of EM duality applied to the SM gauge group itself. The dual colour SU(3) plays the role of a generation symmetry. Fermion generations arise from the dual gauge group. References: hep-ph/9904406, hep-ph/0303010, hep-th/0010261.
2. **Sannino and Cacciapaglia (2024):** The SM is recast as the magnetic (IR) description of a UV electric theory with larger gauge groups. The SM fields are composite magnetic degrees of freedom. Reference: arXiv:2407.17281.

These are completely different proposals. Confusing them (or citing Chan-Tsou papers in a discussion of Sannino's dualised SM) will cause serious errors.

**Prevention:**
- State explicitly in the lecture notes which program is being followed: "We follow the dualised Standard Model program of Cacciapaglia and Sannino (2024), in which the SM arises as the magnetic dual of a UV electric theory. This should not be confused with the earlier 'Dualized Standard Model' of Chan and Tsou, which uses EM duality within the SM gauge group to explain fermion generations."
- Check reference lists carefully: hep-ph/9904406 and hep-ph/0303010 are Chan-Tsou, not Sannino.

**Warning signs:**
- References to "dual colour SU(3)" as a generation symmetry in the context of Sannino's program (wrong framework).
- Citing Bordes, Chan, and Tsou papers as supporting the Cacciapaglia-Sannino construction.

**Phase to address:**
Introduction (Lecture 1) and reference list curation.

---

### Pitfall 9: Presenting the flavour structure as complete when it is an open problem

**What goes wrong:**
In 2407.17281, the flavour structure (fermion mass hierarchy, CKM mixing) arises from Planck-scale four-fermion operators that generate scalar mass hierarchies upon dualisation. However, the paper explicitly acknowledges that the precise duality scale, specific model details of the flavour sector, and numerical coefficients are "left for future studies." The construction is a framework, not a completed model.

**Prevention:**
- Present the flavour mechanism as: "The dualised SM provides a *framework* for explaining the fermion mass hierarchy, in which Planck-scale operators generate hierarchical Higgs VEVs. The detailed flavour structure (CKM matrix elements, CP violation) requires further model-building within this framework."
- Exercises should demonstrate the mechanism (hierarchy from operator dimensions) without claiming to predict specific CKM entries.

**Warning signs:**
- Claims that the dualised SM "explains" the CKM matrix.
- Exercises producing specific CKM matrix elements from the dual theory alone.
- Conflating the parametric hierarchy explanation with a complete flavour model.

**Phase to address:**
Lectures on the SM spectrum from duality (Lectures 6-7) and exercises (Lecture 8).

**References:**
- Cacciapaglia and Sannino, arXiv:2407.17281, Eqs. (11), (15), (21)

---

### Pitfall 10: Motivating the duality without SUSY non-renormalization theorems

**What goes wrong:**
In the SUSY context, the non-renormalization theorem (Seiberg, 1993) ensures that the superpotential is not renormalized in perturbation theory, which is crucial for establishing the exact results that underpin the duality. Without SUSY, there is no such theorem, and one must explain why we trust the duality despite losing this control.

If the lectures simply omit this issue, students will either (a) not understand why the SUSY case is special, or (b) assume the non-SUSY case has similar protection (it does not).

**Prevention:**
- State the non-renormalization theorem as a key reason for the SUSY duality's power, in a self-contained way: "In SUSY theories, the superpotential --- a function that controls masses and interactions --- cannot receive perturbative corrections. This means certain quantities computed at tree level are exact. This is why Seiberg could derive exact results."
- Then explain what replaces this in non-SUSY: "Without SUSY, we lose this protection. The evidence for non-SUSY duality comes from (1) anomaly matching, (2) large-N equivalences, (3) lattice evidence, and (4) consistency with the SUSY limit."

**Warning signs:**
- Students asking "why can't we just compute the beta function exactly in the non-SUSY case?"
- No mention of what changes when SUSY is removed.

**Phase to address:**
Lecture 3-4 (SUSY duality evidence) and Lecture 5 (transition to non-SUSY).

---

## Minor Pitfalls

### Pitfall 11: Factor-of-two errors in anomaly coefficients from Dynkin index conventions

**What goes wrong:**
Different references use different normalisations for the Dynkin index T(R) (also called the index of the representation). The two common conventions:
- **Convention A (Seiberg, Intriligator-Seiberg):** T(fund) = 1/2 for the fundamental of SU(N).
- **Convention B (some group theory references, Terning's appendix for Dirac fermions):** T(fund) = 1 for a Dirac fermion in the fundamental (= 1/2 per Weyl fermion).

The anomaly coefficient for SU(N)^3 with N_f Weyl fermions in the fundamental is proportional to N_f * T(fund). A factor-of-2 error from using the wrong convention propagates to incorrect conformal window boundaries, wrong anomaly matching checks, and wrong dual rank calculations.

**Prevention:**
- Fix a convention at the start and state it: "Throughout these notes, T(fund) = 1/2 for one Weyl fermion in the fundamental of SU(N), following Seiberg (1994) and Intriligator-Seiberg (1995)."
- When quoting results from any reference, check the convention used in that reference.
- A useful consistency check: for SU(N) with N_f flavours (Dirac), the one-loop beta function coefficient is b_0 = (11/3)C_2(adj) - (2/3)N_f T(fund) (Weyl) or equivalently (11/3)N - (2/3)N_f * 1/2 for T(fund)=1/2 convention. Verify this reproduces b_0 = (11N - 2N_f)/3 for SU(N) with N_f Dirac flavours.

**Phase to address:**
Lecture on anomaly matching and group theory review (Lecture 2-3). A conventions appendix should be provided.

---

### Pitfall 12: Not distinguishing perturbative from non-perturbative anomalies

**What goes wrong:**
The perturbative (ABJ-type) anomaly is computed from one-loop triangle diagrams and yields anomaly coefficients proportional to Tr[T^a {T^b, T^c}]. The non-perturbative (global) anomaly (Witten, 1982) is a Z_2-valued obstruction that exists for SU(2) with an odd number of Weyl doublets and cannot be seen in perturbation theory.

In the context of the SM, the Witten anomaly constrains the number of SU(2)_L doublets. In the dualised SM, one must check that the Witten anomaly is absent in both the electric and magnetic theories separately. This is a separate check from perturbative anomaly matching.

**Prevention:**
- Mention the Witten anomaly when discussing the SM gauge group and verify it is absent.
- When performing anomaly matching between electric and magnetic theories, note that the Witten anomaly is checked separately.

**Phase to address:**
Lecture on anomaly matching (Lecture 3-4). Can be a brief remark or an exercise.

**References:**
- Witten, Phys. Lett. B117, 324 (1982) (SU(2) global anomaly)

---

### Pitfall 13: Not tracking which SM gauge factors are being dualised

**What goes wrong:**
The SM gauge group is SU(3)_c x SU(2)_L x U(1)_Y. The dualised SM program (2407.17281) does not dualise all three factors simultaneously in the same way. Different factors may be dualised independently, with different electric gauge groups and different matter content for each. Losing track of which factor is being dualised at which step leads to inconsistent field content tables and wrong anomaly matching.

**Prevention:**
- Label every field with all its quantum numbers under every gauge group factor, at every step.
- When dualising SU(3)_c, the SU(2)_L x U(1)_Y quantum numbers of the dual quarks must be tracked through the dualisation.
- Use a master table of field content for each stage of the construction.

**Phase to address:**
Lectures 5-6 (constructing the dualised SM). The master field content table should be a central exhibit.

---

### Pitfall 14: Presenting 't Hooft anomaly matching without losing students

**What goes wrong:**
Anomaly matching involves computing Tr[T^a {T^b, T^c}] for many combinations of global symmetry generators in both the UV and IR descriptions. This is technically straightforward but can feel like an unmotivated "matching game" unless students understand *why* it constrains the IR spectrum.

**Prevention:**
- Before the computation, present 't Hooft's original argument: "Imagine gauging the global symmetry with very weak gauge fields. The UV anomaly computes the triangle diagram with these weakly-gauged external legs. Since anomalies are exact (Adler-Bardeen theorem), they cannot change under RG flow. Therefore the IR theory must reproduce the same anomaly."
- Then present a simple example: SU(N_c) with N_f flavours, matching SU(N_f)_L x SU(N_f)_R x U(1)_B anomalies. Show that the matching constrains the number and representations of massless baryons.
- Only after the example, proceed to the full anomaly matching for the duality.

**Phase to address:**
Lecture 3-4 (anomaly matching). The pedagogical ordering is: motivation -> simple example -> general statement -> application to duality.

---

## Convention Traps

| Convention Issue | Common Mistake | Correct Approach |
|---|---|---|
| **Dynkin index normalisation:** T(fund) = 1/2 (Seiberg, Intriligator-Seiberg) vs T(fund) = 1 (some refs for Dirac fermions) | Using T(fund) = 1 in formulas derived with T(fund) = 1/2, doubling all anomaly coefficients | Fix T(fund) = 1/2 per Weyl fermion throughout. State explicitly in conventions section. Verify with b_0 = (11N - 2N_f)/3 for SU(N) with N_f Dirac flavours. |
| **Quadratic Casimir normalisation:** C_2(fund) = (N^2-1)/(2N) vs C_2(fund) in different normalisation | Factor-of-N errors in beta function coefficients | Use C_2(fund) = (N^2-1)/(2N) consistently (standard in Peskin-Schroeder). |
| **Anomaly coefficient definition:** A(R) = 1 for fundamental (Seiberg) vs d(R)/d(fund) normalisation | Misidentifying which representation has anomaly coefficient 1 | Fix A(fund) = 1 following Seiberg. Compute A(adj) = N for SU(N) as a consistency check. |
| **Metric signature:** (+,-,-,-) in particle physics vs (-,+,+,+) in some GR-influenced texts | Sign errors in propagators when using formulas from mixed sources | Fix (+,-,-,-) throughout (standard for particle physics/gauge theory). State in conventions. |
| **Weyl fermion counting:** Counting Weyl fermions vs Dirac fermions in N_f | Factor of 2 in conformal window boundaries: the window 3N_c/2 < N_f < 3N_c assumes N_f Dirac flavours (= 2N_f Weyl) | State "N_f counts the number of Dirac flavour pairs (Q, Q-tilde)" in the SUSY context. Verify: SQCD has N_f chiral superfield pairs (Q_i, Q-tilde_i), each containing one Weyl fermion, so N_f Dirac flavours correspond to 2N_f Weyl fermions in the fundamental. |
| **R-charge assignments:** Different papers use different R-charge conventions (e.g., R[Q] = (N_f - N_c)/N_f vs R[Q] = 1 - N_c/N_f) | These are the same formula written differently, but mixing conventions can lead to sign errors in superpotential terms | Fix R[Q] = 1 - N_c/N_f = (N_f - N_c)/N_f following Seiberg. Verify R[W] = 2 for the superpotential (SUSY constraint). |
| **Four-fermion operator normalisation:** Sannino (2407.17281) uses operators suppressed by M_Pl vs other papers using generic cutoff Lambda | Factor-of-(M_Pl/Lambda)^n errors when comparing with other compositeness literature | Use the same cutoff scale throughout; when comparing, convert explicitly. |

---

## Approximation Shortcuts

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|---|---|---|---|
| Using SUSY conformal window bounds for non-SUSY theories | Avoids the model-dependence of non-SUSY beta function estimates | Wrong conformal window boundaries; may place the SM in the wrong phase | Never for quantitative claims. Acceptable as a rough first estimate to motivate the construction, clearly labeled. |
| One-loop anomaly matching only | Avoids two-loop and scheme-dependent corrections | Misses scheme-dependent effects at two loops. However, anomaly matching is exact (Adler-Bardeen), so one-loop is actually exact for perturbative anomalies | Always acceptable for ABJ-type anomalies (they are one-loop exact). Not applicable to Witten anomaly (non-perturbative). |
| Treating the MAC hypothesis as a theorem | Simplifies the analysis of chiral symmetry breaking patterns | The MAC hypothesis is known to fail in some cases; the most attractive channel does not always condense | Never present as proven. Acceptable as a guiding principle with caveats: "The MAC hypothesis suggests... but it is not a theorem." |
| Large-N planar equivalence as proof of non-SUSY duality | Provides theoretical support from string theory / orbifold constructions | Only holds at N -> infinity; finite-N corrections are unknown and potentially large | Acceptable as motivation. State "at large N... but finite-N corrections are uncontrolled." |
| Neglecting the sigma (dilaton) in conformal window analysis | Simplifies the spectrum | Near the conformal window, there may be a light scalar (approximate dilaton) that affects the dynamics. Lattice evidence (N_f=8 SU(3)) suggests such a state exists. | Acceptable far from the conformal window. Problematic near the lower boundary. |

---

## Numerical Traps

These are relevant for exercises that involve computing anomaly coefficients, beta functions, or mass ratios.

| Trap | Symptoms | Prevention | When It Breaks |
|---|---|---|---|
| Integer overflow in group theory factors for large representations | Anomaly coefficients that are unexpectedly large or have wrong signs | Use the dimension formula d(R) and index T(R) from tables, not from general formulas that involve large factorials | Large N or high-rank representations |
| Caswell-Banks-Zaks fixed point at negative coupling | Two-loop beta function yields a fixed point at alpha* < 0, which is unphysical | Check that the fixed point coupling is positive. If negative, the theory is not in the conformal window at this loop order. | N_f near the lower boundary of the conformal window, where the two-loop estimate is unreliable |
| Double-counting when composites overlap with elementary fields | In the magnetic theory, mesonic operators M^{ij} are elementary fields, but they correspond to composite operators Q^i Q-tilde^j of the electric theory. If exercises ask students to enumerate degrees of freedom, double-counting is easy. | Clearly distinguish between electric and magnetic field content. Count degrees of freedom in one description at a time. | When building the full dual SM spectrum with multiple gauge group factors |

---

## Interpretation Mistakes

| Mistake | Risk | Prevention |
|---|---|---|
| Treating the magnetic theory as "more fundamental" than the electric theory | Misunderstanding duality as a derivation (electric -> magnetic) rather than an equivalence | Emphasise: both descriptions are equally valid. "Electric" and "magnetic" are conventional labels. The duality is symmetric. |
| Interpreting composites of the electric theory as observable bound states | Confusion about what is physical vs what is a mathematical mapping | The composite operators map to elementary fields of the magnetic theory. They are not separately observable objects in the magnetic description. |
| Claiming the dualised SM "explains" electroweak symmetry breaking | The dualised SM recasts EWSB in dual variables but does not derive it from a new principle | Present as: "EWSB is reinterpreted in the dual description as the condensation of [specific composite operators]." It is a rewriting, not a derivation of the mechanism. |
| Confusing the duality scale with the compositeness scale | The duality scale (Lambda_D ~ 10^11 GeV in 2407.17281) is where the two descriptions cross over, not where new composite resonances appear at colliders | Clearly separate: (1) Lambda_D = duality scale, (2) compositeness scale relevant for collider bounds (typically related to masses of magnetic theory particles), (3) M_Pl = Planck scale (where flavour operators are generated). |
| Assuming the dualised SM is ruled out by compositeness bounds | LHC bounds on compositeness (Lambda > few TeV) apply to four-fermion operators generated by contact interactions, not directly to the duality scale | The duality maps composites to elementary-looking fields at low energies. Compositeness bounds constrain the magnetic theory spectrum, not the duality scale directly. |

---

## "Looks Correct But Is Not" Checklist

- [ ] **Anomaly matching:** Verify that *all* independent global symmetries are matched (SU(N_f)_L, SU(N_f)_R, U(1)_B, and all mixed anomalies), not just the simplest ones. Missing even one anomaly matching condition can invalidate the claim.
- [ ] **Conformal window check:** Verify that N_f and N_c satisfy 3N_c/2 < N_f < 3N_c for the SUSY case, and that the non-SUSY analog is checked separately with the appropriate beta function.
- [ ] **Dual gauge group rank:** For SU(N_c) with N_f flavours, the dual gauge group is SU(N_f - N_c). Verify this gives a non-trivial (positive-rank) gauge group. If N_f - N_c <= 0, the duality breaks down.
- [ ] **Meson matrix dimensions:** The meson matrix M^{ij} has dimensions N_f x N_f. If the lecture notes present it as N_c x N_c, there is a transposition error in the construction.
- [ ] **Superpotential mapping:** In SUSY duality, W_mag = M q q-tilde. If the magnetic superpotential is missing or has wrong field content, the moduli space matching fails.
- [ ] **R-charge consistency:** Check R[W] = 2 (SUSY constraint). If R[Q] + R[Q-tilde] = 2(N_f-N_c)/N_f, then R[Mq q-tilde] = 2(N_f-N_c)/N_f + 2N_c/N_f = 2. Verify this.
- [ ] **Weyl fermion vs Dirac fermion counting:** Every time N_f appears, verify whether it counts Weyl pairs or Dirac fermions. A factor-of-2 error here invalidates the entire conformal window analysis.
- [ ] **Global symmetry of the magnetic theory:** The magnetic theory must have the same global symmetry group as the electric theory. If additional accidental symmetries appear, they must be understood (they may be anomalous or broken by the superpotential).

---

## Open Problems in the Dualised SM

These are genuinely unresolved issues that the lecture notes should flag as open, not attempt to resolve.

| Open Problem | Status | Impact on Lecture Notes | Reference |
|---|---|---|---|
| Is the fermion mass spectrum quantitative? | The current framework provides parametric scaling (mass hierarchies), not numerical predictions. Specific mass values require inputting measured parameters. | Exercises must be honest about what is predicted vs input. | 2407.17281, Eqs. 11, 15 |
| Flavour structure completeness | The flavour sector (CKM, PMNS, CP violation) is outlined as arising from Planck-scale operators but not computed in detail. "Left for future studies." | Present as open. Do not claim CKM matrix is derived. | 2407.17281, Sec. 3-4 |
| Full anomaly matching for the complete SM gauge group | Anomaly matching for individual gauge factors is addressed, but the full interplay of SU(3) x SU(2) x U(1) anomaly matching in the dualised construction is intricate and not fully displayed. | Present the anomaly matching factor by factor; note that the complete cross-check is needed. | 2407.17281 |
| Robustness under radiative corrections | Without SUSY non-renormalization, the dual description may receive radiative corrections that shift the spectrum. Whether the qualitative features are stable is not established. | Flag as an open question. Do not assume radiative stability without proof. | General concern; no specific reference addresses this for the dualised SM |
| Compositeness constraints from colliders | The magnetic theory fields are composites of the electric theory. LHC bounds on compositeness scales must be satisfied. The relationship between the duality scale and compositeness bounds is model-dependent. | Present the general argument for why compositeness bounds are not immediately fatal (composites look elementary at low energies). Do not claim they are satisfied without checking. | 2407.17281, Sec. 5 |
| Lattice verification | Direct lattice simulation of the electric theory could test the duality, but this has not been done for the specific field content of the dualised SM. | Mention as a future direction. Do not cite lattice results for related theories as verification of this specific construction. | General |
| Grand unification in the dual description | 2407.17281 suggests the duality opens "novel avenues for grand unification" but this is not developed. | Mention as motivation for future work, not as a result. | 2407.17281 |

---

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
|---|---|---|
| P1: Conjectural status of non-SUSY duality | Lectures 2-3 (SUSY duality) and 5-6 (non-SUSY) | Check: does every statement about non-SUSY duality carry an appropriate caveat? |
| P2: Qualitative vs quantitative mass predictions | Lectures 6-8 (spectrum and exercises) | Check: do exercises distinguish input parameters from predictions? |
| P3: Global vs gauge anomaly confusion | Lecture 3-4 (anomaly matching) | Check: is the comparison table present? Can students state the difference? |
| P4: Outside the conformal window | Lecture 4-5 (conformal window) | Check: are non-SUSY conformal window boundaries stated with uncertainties? |
| P5: Tumbling vs duality confusion | Lectures 2 and 6 | Check: is each concept introduced with a clear definition? |
| P6: SUSY background assumption | Throughout | Check: is every SUSY concept defined where first used? |
| P7: Naive EM duality analogy | Lecture 1-2 | Check: does the transition from EM to non-abelian duality list explicit differences? |
| P8: Chan-Tsou vs Sannino confusion | Lecture 1 and reference list | Check: is the distinction stated? Are references correctly attributed? |
| P9: Incomplete flavour structure | Lectures 6-7 | Check: is the flavour mechanism presented as a framework with open questions? |
| P10: Missing motivation without SUSY | Lectures 3-5 | Check: is the non-renormalization theorem explained and its absence in non-SUSY acknowledged? |
| P11: Dynkin index factor-of-2 | Lecture 2-3 and conventions appendix | Check: is T(fund) = 1/2 stated and the one-loop beta function verified? |
| P12: Perturbative vs non-perturbative anomaly | Lecture 3-4 | Check: is the Witten anomaly mentioned? |
| P13: Tracking which SM gauge factors are dualised | Lectures 5-6 | Check: is there a master field content table for each stage? |
| P14: Anomaly matching pedagogy | Lecture 3-4 | Check: is the motivation (gauging with weak fields) presented before the calculation? |

---

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
|---|---|---|
| P1: Non-SUSY treated as proven | LOW | Add caveats and qualifiers to relevant passages. No structural change needed. |
| P2: Exercises claim quantitative prediction | MEDIUM | Redesign exercise statements to distinguish inputs from outputs. May require rewriting solutions. |
| P3: Anomaly confusion | MEDIUM | Add the comparison table and a worked example showing the distinction. Insert before the duality lecture. |
| P4: Wrong conformal window | HIGH | If the conformal window analysis is wrong, the entire duality application may be in the wrong regime. Must re-derive with correct bounds and verify the construction still works. |
| P5: Tumbling/duality conflation | LOW | Add definitions and comparison table. No structural change. |
| P8: Wrong reference program | LOW | Correct references. No physics change. |
| P11: Factor-of-2 | HIGH | If the anomaly matching was done with wrong conventions, ALL anomaly checks must be redone. Requires a complete pass through all equations. |

---

## Sources

### Primary References
- Seiberg, "Electric-magnetic duality in supersymmetric non-Abelian gauge theories," hep-th/9411149
- Intriligator and Seiberg, "Lectures on supersymmetric gauge theories and electric-magnetic duality," hep-th/9509066
- Cacciapaglia and Sannino, "Charting Standard Model Duality and its Signatures," arXiv:2407.17281
- Terning, "Modern Supersymmetry: Dynamics and Duality," Oxford University Press (2006)
- Csaki and Terning, arXiv:1106.3074

### Anomaly Matching
- 't Hooft, "Naturalness, chiral symmetry, and spontaneous chiral symmetry breaking," in "Recent Developments in Gauge Theories," Cargese 1979
- Tong, "Gauge Theory" lectures, Ch. 3, https://www.damtp.cam.ac.uk/user/tong/gaugetheory/3anom.pdf
- Preskill, "Gauge Anomalies in an Effective Field Theory," Ann. Phys. 210, 323 (1991)
- Witten, "An SU(2) anomaly," Phys. Lett. B117, 324 (1982)

### Conformal Window
- Ryttov and Sannino, "Supersymmetry Inspired QCD Beta Function," arXiv:0711.3745
- Appelquist, Fleming, Neil, Phys. Rev. Lett. 100, 171607 (2008) (early lattice conformal window)
- LatKMI Collaboration, arXiv:2401.00267 (SU(3) N_f=8 lattice, 2024)
- Sannino, "Broken Conformal Window," arXiv:2111.09690

### Non-SUSY Duality
- Armoni, Shifman, Unsal, "Non-Supersymmetric Seiberg Duality, Orientifold QCD and Non-Critical Strings," arXiv:0801.0762

### Chan-Tsou (distinct program)
- Chan and Tsou, "The Dualized Standard Model and its Applications --- an Interim Report," hep-ph/9904406
- Bordes, Chan, Tsou, "Fermion Generations and Mixing from Dualized Standard Model," hep-ph/0303010

### Tumbling/Complementarity
- Raby, Dimopoulos, Susskind, Nucl. Phys. B169, 373 (1980)
- Osterwalder and Seiler, Ann. Phys. 110, 440 (1978)
- Fradkin and Shenker, Phys. Rev. D19, 3682 (1979)

---

_Known pitfalls research for: Gauge-fermion dualities and the dualised Standard Model_
_Researched: 2026-03-19_
