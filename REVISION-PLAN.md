# Revision Plan

Based on the 4-round assessment (initial → audit → adjudication → reassessment).

## Priority Tiers

### Tier 1: CRITICAL — Physics errors and prompt-solution contradictions (fix first)

These are wrong or self-contradictory. They undermine trust.

#### Exercises (most error-prone category)

| File | Issue | Type | Fix |
|------|-------|------|-----|
| exercise-01 | P2: Asks for SU(2)_L^3 anomaly + hint says nonzero, but SU(2) has no cubic d^{abc}. Solution changes target mid-answer. | physics error | Rewrite P2: either use SU(2)^2 U(1)_B + Witten anomaly, or frame cubic computation as intentional diagnostic trap |
| exercise-02 | P4: Labels SUSY conformal window on a non-SUSY diagram. Category error. | physics error | Split diagram into separate SUSY/non-SUSY panels with explicit labels |
| exercise-03 | P4: Hint says [M]=[mass], solution gets [mass]^2, corrects itself mid-derivation | physics error | Fix hint to state [M]=[mass]^2 from the start |
| exercise-03 | P3: Background says Delta=3|R|/2, solution uses Delta=3R/2 | physics error | Standardise to Delta=3R/2 throughout |
| exercise-04 | P1: Says N=2 and N=1 R-symmetries "coincide" at N_f=2N_c, then computes R=1/2 not 1 | physics error | Replace "coincide" with "related by mixing" |
| exercise-05 | P1(b): Mechanism drift — generic Planck suppression fails, solution switches to H-mixing without warning | physics error | Either introduce mixing mechanism in prompt, or let naive suppression fail and ask what it means |
| exercise-05 | P1(c): Prompt says p is integer, solution gets p=0.2 and says p need not be integer | physics error | Remove integer-tier language or fix mechanism to support it |
| exercise-06 | P1(b)(i): Prompt says "argue NOT asymptotically free" but b_0^e=4>0, so it IS AF | physics error | Correct prompt to "argue that the electric theory IS asymptotically free" |
| exercise-06 | P1(b)(ii): Prompt says use alpha_s=0.3, solution silently replaces with 0.032 | prompt-solution contradiction | Use one consistent input throughout; either fix prompt to alpha_s(M_Z)=0.118 or let alpha_s=0.3 give absurd result and ask why |
| exercise-07 | P3(b)(i): Prompt says composites are dimensionless, solution assigns [M]=2 | physics error | Choose one normalisation convention throughout |

#### Lectures

| File | Issue | Type | Fix |
|------|-------|------|-----|
| lecture-01 | SU(2)_L^3 anomaly: conventions section says SU(2) has no cubic anomaly, warmup computes nonzero one | physics error | Either switch warmup to SU(3)_c flavour anomalies or label SU(2) example as schematic |
| lecture-02 | Moduli-space dimension derivation mixes real/complex dimensions, N_f=N_c=2 check contradicts itself | physics error | Rewrite with one consistent counting scheme, stating complex vs real at each step |
| lecture-02 | Baryon number: L1 uses B[Q]=1/N_c, L2 uses B=+/-1 without announcement | prompt-solution contradiction | Add explicit announcement of convention change |

#### Papers

| File | Issue | Type | Fix |
|------|-------|------|-----|
| paper-1 | Abstract says mesons give Higgs doublets; body shows they're SU(2)_L singlets (no-go). Central contradiction. | physics error | Rewrite abstract/intro to match body's actual result (no-go + generation bound) |
| paper-1 | Meson sector: "66 real scalars" vs "66 complex scalar DOF" | physics error | Fix to one consistent counting |
| paper-2 | Sum Rule VI: abstract says DSM-specific, body says standard HQET. Central novelty claim. | prompt-solution contradiction | Reframe: only Sum Rule V is DSM-specific from the start |
| paper-3 | Observable 2 (gluinoball-meson degeneracy): relies on adjoint structure absent from fundamental-fermion target | physics error | Demote to "exploratory/conditional" tier |

### Tier 2: HIGH — Missing caveats on epistemic status

These are correct but overstated. Fix after Tier 1.

| File | Issue | Fix |
|------|-------|-----|
| lecture-02 | Says duality can be "proved" — L3 treats it as conjecture with evidence | Replace "prove" with "derive evidence for" |
| lecture-05 | Bridge from tumbling/complementarity to duality is motivational, not deductive | Add explicit sentence: "This connection is motivational, not a derivation" |
| lecture-06 | Status changes (exact → heuristic → conjecture) compressed; reader loses track | Add status tag at start of each section: "toy model" / "obstruction" / "anomaly-based candidate" |
| lecture-07 | Some compositeness statements too bold — bare declarative instead of "within conjectured dual map" | Add "within the conjectured dual map" qualifiers |
| lecture-08 | H_0 direction choice not derived, only asserted | State explicitly that dominant Higgs direction is model assumption |
| lecture-10 | "Higgs matrix and meson matrix ARE the same object" — too strong | Soften to "correspondence" / "shared structural origin" |
| lecture-10 | Scalar nonet q-qbar interpretation is modelling choice, not settled | Add caveat |
| paper-2 | Title/abstract claim rules "derived from 6x6 matrix" but most work is imported ChPT/HQET | Reframe title: reorganises known relations in dual-meson language |
| paper-3 | "Sharp quantitative predictions" / "test decisively" — rhetorical overreach | Replace with "diagnostic proposals" / "distinguish between scenarios" |
| paper-4 | "Uniquely selects" n_g=3 in abstract — conditional on SUSY conformal window import | Add assumptions table; soften "uniquely selects" to "emerges within chosen framework" |
| exercise-02 | P3: "theory confines" below 3N_c/2 — compresses nuanced SQCD IR story | Replace with "electric conformal description fails; magnetic description preferred" |
| exercise-04 | P3: SL(2,Z) "simply descends" to Seiberg self-duality — unstated assumption | Mark as accepted from broader SW/APS framework |
| exercise-08 | P2: sigma_{12} identified with a_0(980)^+ — model-dependent | Add caveat on model dependence |

### Tier 3: MEDIUM — Structural/pedagogical improvements

Not wrong, but confusing or incomplete. Fix after Tiers 1-2.

| File | Issue | Fix |
|------|-------|-----|
| lecture-01 | Course-goal framing overshoots lecture scope | Trim to tools-and-payoffs |
| lecture-03 | Mass deformation step too compressed | Add one explanatory paragraph on Higgsing mechanism |
| lecture-03 | Moduli space treatment skeletal | Add explicit operator map electric↔magnetic |
| lecture-05 | SU(5) tumbling stops after first step | Add one more step or note it's illustrative |
| lecture-07 | Rapid group-switching overloads reader | Add compact map of which group is active where |
| lecture-07 | Mesino anomaly cancellation handled schematically | Add one representative decomposition |
| lecture-08 | Derivation chain too dense | Add one-page summary table: inputs → induced quantities → free parameters |
| lecture-09 | Non-SU relevance connection weak | Add one sentence per duality block: why this matters |
| lecture-10 | 6x6 matrix compresses different regimes into one visual | Add caveat before matrix: flavour-organisation device, not uniform dynamical description |
| exercise-01 | P4: Hint says use gauge-invariant operators, solution uses anomaly cancellation | Align hint with solution method |
| exercise-02 | P1: Heuristic explanation of fermion 4/3 factor | Add explicit derivation or mark as heuristic |
| exercise-03 | P2: Higgsing step too compressed | Add paragraph on gauge orientation + rank lowering |
| exercise-07 | P2: Asks "derive" but solution summarises from literature | Weaken "derive" to "state and justify" or provide actual machinery |
| exercise-07 | P2(a)(i): Non-SUSY formula in SUSY calculation | Use 3T(adj)-ΣT(r) SUSY form |
| preamble | Minimal — lacks comment about lecture-local convention extensions | Add short comment noting convention boxes extend shared base |

### Tier 4: LOW — Polish

| File | Issue |
|------|-------|
| lecture-04 | FI term needs qualification as effective low-energy statement |
| lecture-04 | Separate exact SW facts from APS interpretation with transition paragraph |
| exercise-08 | P1(d): D-meson solution drifts into isospin aside |
| exercise-08 | P3: Hierarchy question absorbs variations into O(1) coefficients without telling students |
| paper-1 | Complete cubic anomaly derivation or demote to cited background |
| paper-3 | Separate "boundary-only" observables from off-boundary predictions |

## Execution Plan

**Phase A — Tier 1 fixes (physics errors + contradictions): 17 files**
Priority: exercises first (most errors), then papers, then lectures.
Method: Read source file → apply targeted fix → verify no new inconsistencies → commit.

**Phase B — Tier 2 fixes (epistemic caveats): ~13 files**
Method: Add qualifiers, soften overstated claims, add status tags. Often 1-3 sentence additions.

**Phase C — Tier 3 fixes (structural): ~15 files**
Method: Add explanatory paragraphs, summary tables, signposting. Larger edits but not physics changes.

**Phase D — Tier 4 polish: ~6 files**
Method: Minor additions and refinements.

**Estimated scope:** ~50 targeted edits across 20 files. No full rewrites needed — the assessment confirms the corpus is "conceptually strong, structurally ambitious" with "locally uneven rigor."
