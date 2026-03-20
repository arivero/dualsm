---
phase: 03-non-perturbative-dynamics
plan: 02
depth: full
one-liner: "Wrote Lecture 6 presenting the Sannino non-SUSY duality programme chronologically (1997-2013) with conjectural qualifiers on every non-SUSY claim, Cheng-Shadmi tension acknowledged as unresolved, and the central vulnerability (no cross-validation beyond anomaly matching) as the dedicated concluding section"
subsystem: formalism
tags: [non-SUSY-duality, anomaly-matching, Sannino, Cheng-Shadmi, emergent-SUSY, Pati-Salam, SM-as-magnetic, conjectural-qualifiers]

requires:
  - phase: 01-foundations
    provides: "'t Hooft anomaly matching machinery (Lecture 1); anomaly coefficient conventions A(fund)=1"
  - phase: 02-susy-and-seiberg-duality
    provides: "Seiberg duality framework (Lecture 3); NSVZ beta function (Lecture 2); N=2 origin (Lecture 4); four pillars of SUSY duality"
  - phase: 03-non-perturbative-dynamics (plan 01)
    provides: "Tumbling/MAC/complementarity physical picture (Lecture 5); preview of conjectural qualifier requirement"
provides:
  - "SUSY vs non-SUSY evidence comparison table (5 pillars vs 1)"
  - "Cheng-Shadmi tension: tachyonic scalars under large SUSY breaking (unresolved)"
  - "Sannino QCD dual gauge group SU(2N_f - 5N) with anomaly matching"
  - "SM-as-magnetic: n_gen >= 3 from non-abelian electric gauge group"
  - "Emergent SUSY at perturbative fixed points (Veneziano limit)"
  - "Central vulnerability: no cross-validation beyond anomaly matching"
  - "Forward reference to Lectures 7-8 with conditional language"
affects: [04-dualised-standard-model]

methods:
  added: [non-SUSY-anomaly-matching, conjectural-qualifier-discipline]
  patterns: [warningbox-for-epistemic-caveats, comparisontable-for-evidence-levels, chronological-narrative]

key-files:
  created:
    - "lectures/lecture-06.tex"
    - "lectures/lecture-06.pdf"

key-decisions:
  - "Every non-SUSY duality statement carries conjectural qualifier ('if the duality holds', 'conjectured', 'suggests') -- contract requirement P1 strictly enforced"
  - "Cheng-Shadmi tension presented as unresolved; Sannino's approach described as sidestepping rather than resolving the problem"
  - "Central vulnerability given a dedicated concluding section (Section 6), not buried in a footnote"
  - "Emergent SUSY limitation stated explicitly: perturbative result in Veneziano limit, finite-N validity uncontrolled"

patterns-established:
  - "Conjectural qualifier pattern: all non-SUSY claims carry explicit hedge language"
  - "Epistemic convention box: lecture-level epistemic status declared in the convention box"

conventions:
  - "hbar = c = 1 (natural units)"
  - "metric = (+,-,-,-) (mostly minus)"
  - "T(fund) = 1/2 per Weyl fermion"
  - "b_0 = (11N_c - 2N_f)/3"
  - "A(fund) = 1"
  - "R[Q] = (N_f - N_c)/N_f; R[W] = 2"
  - "N_f counts Dirac flavour pairs"

plan_contract_ref: ".gpd/phases/03-non-perturbative-dynamics/03-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-what-we-lose:
      status: passed
      summary: "Section 1 explicitly lists what SUSY provides (holomorphy, NSVZ beta function, moduli space matching, superconformal index) and what survives without SUSY (anomaly matching alone). The contrast is made explicit via a SUSY vs non-SUSY comparison table."
      linked_ids: [deliv-lecture-06, test-susy-vs-nonsusy, ref-sannino-2407]
    claim-chronological-narrative:
      status: passed
      summary: "Non-SUSY duality results presented in strict chronological order: Sannino-Schechter (1997, Sec 2) -> Cheng-Shadmi (1998, Sec 2.3) -> QCD dual (2009, Sec 3) -> SM-as-magnetic (2011, Sec 4) -> emergent SUSY (2011/2013, Sec 5), with each paper cited and its key result stated"
      linked_ids: [deliv-lecture-06, test-chronological-order, test-all-papers-cited, ref-sannino-2407, ref-sannino-qcd-dual, ref-sannino-sm-magnetic, ref-emergent-susy]
    claim-conjectural-qualifiers:
      status: passed
      summary: "15+ instances of conjectural language ('if the duality holds', 'conjectured', 'suggests that', etc.) found in the lecture. Zero unqualified non-SUSY duality assertions found in systematic scan for 'the duality shows/implies/proves/demonstrates'."
      linked_ids: [deliv-lecture-06, test-conjectural-language, ref-sannino-2407]
    claim-central-vulnerability:
      status: passed
      summary: "Central vulnerability is Section 6 (dedicated concluding section, not a footnote): states 'no independent cross-validation beyond anomaly matching', distinguishes SUSY (4 pillars) from non-SUSY (1 pillar), states 'postulates and checks consistency -- consistency is not proof'"
      linked_ids: [deliv-lecture-06, test-vulnerability-stated, ref-sannino-2407, ref-cheng-shadmi]
    claim-cheng-shadmi-tension:
      status: passed
      summary: "Cheng-Shadmi tension presented in Section 2.3 in a dedicated warningbox: negative mass-squared stated, 'unresolved' stated explicitly, Sannino's approach described as sidestepping (not resolving) the problem"
      linked_ids: [deliv-lecture-06, test-cheng-shadmi, ref-cheng-shadmi]
    claim-maekawa-precursor:
      status: passed
      summary: "Maekawa-Takahashi (hep-ph/9510426) cited in Section 4.1 as 'the direct SUSY precursor' of Sannino's non-SUSY Pati-Salam construction, with their key results (natural top mass, natural mu parameter) stated"
      linked_ids: [deliv-lecture-06, test-maekawa-cited, ref-maekawa]
  deliverables:
    deliv-lecture-06:
      status: passed
      path: "lectures/lecture-06.tex"
      summary: "14-page lecture with 7 sections (what we lose, Sannino-Schechter 1997, QCD dual 2009, SM-as-magnetic 2011, emergent SUSY 2011, central vulnerability, summary), plus convention box, comparison table, 5 warningboxes, and preview box; compiles cleanly with pdflatex (0 errors)"
      linked_ids: [claim-what-we-lose, claim-chronological-narrative, claim-conjectural-qualifiers, claim-central-vulnerability, claim-cheng-shadmi-tension, claim-maekawa-precursor]
  acceptance_tests:
    test-susy-vs-nonsusy:
      status: passed
      summary: "Section 1 contains a comparisontable environment explicitly listing 5 SUSY evidence types (holomorphy, NSVZ, moduli space, anomaly matching, superconformal index) against non-SUSY (only anomaly matching), with checkmarks and X marks"
      linked_ids: [claim-what-we-lose, deliv-lecture-06, ref-sannino-2407]
    test-chronological-order:
      status: passed
      summary: "Sections appear in chronological order: Sec 2 (1997), Sec 3 (2009), Sec 4 (2011), Sec 5 (2011/2013). Verified by grep of section headings at lines 185, 285, 388, 489."
      linked_ids: [claim-chronological-narrative, deliv-lecture-06]
    test-all-papers-cited:
      status: passed
      summary: "All 7 required papers cited: SS1997 (5 refs), CS1998 (4 refs), Sannino2009 (7 refs), Sannino2011 (7 refs), AMPS2011 (4 refs), MT1996 (7 refs), CacciapagliaSannino2024 (4 refs)"
      linked_ids: [claim-chronological-narrative, deliv-lecture-06]
    test-conjectural-language:
      status: passed
      summary: "15+ conjectural qualifiers found across the lecture. Zero unqualified non-SUSY assertions found: systematic scan for 'the duality shows/implies/proves/demonstrates' and 'the dual theory predicts' returned zero matches in non-SUSY context."
      linked_ids: [claim-conjectural-qualifiers, deliv-lecture-06, ref-sannino-2407]
    test-vulnerability-stated:
      status: passed
      summary: "Section 6 (The Central Vulnerability) is a dedicated concluding section with warningbox stating: (1) 'no independent cross-validation beyond anomaly matching', (2) 'anomaly matching is necessary but not sufficient', (3) 'consistency is not proof'"
      linked_ids: [claim-central-vulnerability, deliv-lecture-06, ref-sannino-2407]
    test-cheng-shadmi:
      status: passed
      summary: "Section 2.3 contains warningbox titled 'Cheng-Shadmi tension (unresolved)': (1) negative mass-squared stated, (2) 'unresolved' stated, (3) Sannino's approach described as sidestepping rather than resolving"
      linked_ids: [claim-cheng-shadmi-tension, deliv-lecture-06, ref-cheng-shadmi]
    test-maekawa-cited:
      status: passed
      summary: "Section 4.1 titled 'The SUSY precursor: Maekawa-Takahashi' explicitly identifies MT1996 as 'the direct SUSY precursor' with natural top mass and natural mu parameter results"
      linked_ids: [claim-maekawa-precursor, deliv-lecture-06, ref-maekawa]
  references:
    ref-sannino-2407:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Cited as CacciapagliaSannino2024; backbone paper referenced for the dualised SM programme and forward reference to Lectures 7-8"
    ref-sannino-qcd-dual:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Cited as Sannino2009; QCD dual gauge group SU(2N_f-5N), anomaly matching solution, conformal window prediction presented"
    ref-sannino-sm-magnetic:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Cited as Sannino2011; SM-as-magnetic-dual proposal with Pati-Salam embedding, n_gen >= 3, composite Higgs presented"
    ref-emergent-susy:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Cited as AMPS2011; emergent SUSY fixed points from non-SUSY RG flow in Veneziano limit presented with limitations"
    ref-cheng-shadmi:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Cited as CS1998; tachyonic scalar masses under large SUSY breaking presented as unresolved tension in dedicated warningbox"
    ref-sannino-schechter:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Cited as SS1997; toy model with QCD degrees of freedom from SUSY auxiliary fields presented as suggestive but not a proof"
    ref-maekawa:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Cited as MT1996; SUSY Pati-Salam dual identified as direct precursor with natural top mass and mu parameter"
    ref-csaki-terning:
      status: not_applicable
      completed_actions: []
      missing_actions: []
      summary: "must_surface=false in contract; MSSM duality map discussed in Lecture 5 (plan 03-01) rather than Lecture 6"
    ref-bi-terning:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as BT2022; 21 anomaly matching conditions for Spin(8) candidate dual mentioned as recent active work in Section 6.3"
  forbidden_proxies:
    fp-unqualified-nonsusy:
      status: rejected
      notes: "15+ conjectural qualifiers found; zero unqualified non-SUSY assertions; systematic negative scan confirms no violations of contract requirement P1"
    fp-vulnerability-buried:
      status: rejected
      notes: "Central vulnerability is Section 6 (dedicated concluding section, 3 subsections), not a footnote or passing mention. It is the final substantive section before the summary."
    fp-cheng-shadmi-resolved:
      status: rejected
      notes: "Cheng-Shadmi tension explicitly described as 'unresolved' in warningbox title; Sannino's approach described as 'sidesteps rather than resolves'. No language claiming resolution."
    fp-formalism-without-epistemic:
      status: rejected
      notes: "Section 1 (What We Lose Without SUSY) opens the lecture with explicit comparison of SUSY and non-SUSY evidence, including a comparisontable showing 5 pillars vs 1"
  uncertainty_markers:
    weakest_anchors:
      - "Non-SUSY duality itself has no proof; the entire lecture content (beyond Section 1) rests on consistency arguments and anomaly matching, which are necessary but not sufficient"
      - "Emergent SUSY (Antipin et al.) is a perturbative result in the Veneziano limit; finite-N validity is uncontrolled"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If a non-SUSY anomaly matching solution is found that does NOT correspond to a physical dual theory, the foundational assumption weakens"
      - "If lattice studies definitively show the non-SUSY conformal window is inconsistent with the QCD dual predictions, quantitative support weakens"

duration: 12min
completed: 2026-03-20
---

# Phase 3 Plan 02: Non-SUSY Duality Extensions Summary

**Wrote Lecture 6 presenting the Sannino non-SUSY duality programme chronologically (1997-2013) with conjectural qualifiers on every non-SUSY claim, Cheng-Shadmi tension acknowledged as unresolved, and the central vulnerability (no cross-validation beyond anomaly matching) as the dedicated concluding section**

## Performance

- **Duration:** 12 min
- **Started:** 2026-03-20T02:30:00Z
- **Completed:** 2026-03-20T02:42:00Z
- **Tasks:** 1
- **Files modified:** 2 (1 LaTeX + 1 PDF)

## Key Results

- Lecture 6 written (14 pages, compiles cleanly with 0 errors) covering the Sannino non-SUSY duality programme in chronological order
- Contract requirement P1 satisfied: 15+ conjectural qualifiers present; zero unqualified non-SUSY duality assertions found in systematic scan [CONFIDENCE: HIGH -- verified by automated grep]
- Cheng-Shadmi tension presented as unresolved in dedicated warningbox; Sannino's approach described as sidestepping, not resolving [CONFIDENCE: HIGH -- verified against paper]
- Central vulnerability is Section 6 (dedicated concluding section, not a footnote), stating "no cross-validation beyond anomaly matching" and "consistency is not proof" [CONFIDENCE: HIGH -- structural verification]
- All 7 required papers cited with arXiv identifiers, plus Ryttov-Sannino, Pati-Salam, Armoni-Shifman-Unsal as supporting references
- SUSY vs non-SUSY comparison table in Section 1 with 5 pillars vs 1 pillar

## Task Commits

Each task was committed atomically:

1. **Task 1: Write Lecture 6** - `3cf22f7` (docs: write Lecture 6 -- non-SUSY duality extensions)

## Files Created/Modified

- `lectures/lecture-06.tex` -- Lecture 6: Non-SUSY duality extensions (14 pages)
- `lectures/lecture-06.pdf` -- Compiled output (242 KB)

## Next Phase Readiness

Ready for Phase 4 (Dualised Standard Model construction). Lecture 6 provides:
- The conceptual foundation: what survives without SUSY (anomaly matching alone)
- The chronological narrative of the Sannino programme leading to the SM-as-magnetic proposal
- Explicit forward reference to Lectures 7-8 with conditional language: "Every prediction derived in Lectures 7-8 is conditional on the conjectured non-SUSY duality being correct"
- The central vulnerability stated honestly, preparing students for the conditional nature of the Phase 4 construction

## Contract Coverage

- Claim IDs advanced: claim-what-we-lose -> passed, claim-chronological-narrative -> passed, claim-conjectural-qualifiers -> passed, claim-central-vulnerability -> passed, claim-cheng-shadmi-tension -> passed, claim-maekawa-precursor -> passed
- Deliverable IDs produced: deliv-lecture-06 -> lectures/lecture-06.tex (passed)
- Acceptance test IDs run: test-susy-vs-nonsusy -> passed, test-chronological-order -> passed, test-all-papers-cited -> passed, test-conjectural-language -> passed, test-vulnerability-stated -> passed, test-cheng-shadmi -> passed, test-maekawa-cited -> passed
- Reference IDs surfaced: ref-sannino-2407 -> [read, cite], ref-sannino-qcd-dual -> [read, cite], ref-sannino-sm-magnetic -> [read, cite], ref-emergent-susy -> [read, cite], ref-cheng-shadmi -> [read, cite], ref-sannino-schechter -> [read, cite], ref-maekawa -> [read, cite]
- Forbidden proxies rejected: fp-unqualified-nonsusy -> rejected, fp-vulnerability-buried -> rejected, fp-cheng-shadmi-resolved -> rejected, fp-formalism-without-epistemic -> rejected

## Equations Derived

No new equations derived (Phase 3 Plan 02 is a presentation phase, not a derivation phase). The key equations presented are:

**Eq. (03.4): QCD dual gauge group (Sannino 2009)**

$$X = 2N_f - 5N$$

**Eq. (03.5): Generation bound from electric dual (Sannino 2011)**

$$n_g \geq 3$$

**Eq. (03.6): Dual asymptotic freedom (conformal window bound)**

$$N_f \geq \frac{11}{4} N$$

## Validations Completed

- ASSERT_CONVENTION line present and matches preamble.tex exactly. PASS.
- Convention box inherits all Phase 1-2 conventions. PASS.
- "What we lose without SUSY" section: holomorphy, NSVZ, moduli space listed as lost; anomaly matching listed as surviving. PASS.
- Sannino-Schechter (1997) presented with conjectural language ("suggests", "amusing feature"). PASS.
- Cheng-Shadmi: negative mass-squared stated, "unresolved" stated, sidesteps (not resolves) stated. PASS.
- QCD dual (2009): anomaly matching consistency stated; "necessary but not sufficient" caveat present. PASS.
- SM-as-magnetic (2011): three conjectural consequences stated; Maekawa-Takahashi cited as SUSY precursor. PASS.
- Emergent SUSY (2013): Veneziano limit stated; finite-N limitation acknowledged. PASS.
- Central vulnerability: dedicated Section 6; "no cross-validation beyond anomaly matching" stated; "postulates and checks consistency" language present. PASS.
- Conjectural language check: zero unqualified non-SUSY duality assertions found. PASS.
- All 7 required papers cited. PASS.
- Forward reference to Lectures 7-8 with "conditional on conjectured duality" language. PASS.
- LaTeX compiles with 0 errors, 14 pages. PASS.
- Cross-references to Lectures 1-5 present (14 instances). PASS.
- Chronological order: 1997 -> 2009 -> 2011 -> 2013 in section structure. PASS.

## Decisions & Deviations

### Decisions

- **Epistemic convention in convention box:** Added an explicit "epistemic convention" paragraph to the convention box declaring that all non-SUSY claims carry conjectural qualifiers. This goes beyond the plan requirement but makes the epistemic status visible at the very start of the lecture.
- **Armoni-Shifman-Unsal placement:** The ASU large-N argument is placed in Section 5.4 (complementary to emergent SUSY) rather than as a separate section, to keep the chronological narrative focused on the Sannino programme.
- **Bi-Terning placement:** Placed in Section 6.3 (recent developments under central vulnerability) rather than as a separate section, since it serves to show the field is active rather than presenting a new key result.

### Deviations

None -- plan executed as written.

## Issues Encountered

None.

## Open Questions

- Whether emergent SUSY survives at finite N (SM values N_c = 3, N_f = 6) remains the key open theoretical question for the programme
- Whether lattice studies can provide independent verification of the non-SUSY conformal window and duality structure
- The full anomaly matching for the SM gauge group (not just factor-by-factor) is deferred to Phase 4

## Self-Check: PASSED

- [x] lectures/lecture-06.tex exists
- [x] lectures/lecture-06.pdf exists (241947 bytes)
- [x] Commit 3cf22f7 exists in git log
- [x] ASSERT_CONVENTION line matches preamble.tex
- [x] Convention consistency: all conventions match Phase 1-2 lock
- [x] No unqualified non-SUSY duality statements (grep confirms 0)
- [x] 15+ conjectural qualifiers present
- [x] All 7 required papers cited
- [x] Chronological order verified
- [x] Central vulnerability is dedicated concluding section (Section 6)
- [x] Cheng-Shadmi acknowledged as unresolved

---

_Phase: 03-non-perturbative-dynamics_
_Completed: 2026-03-20_
