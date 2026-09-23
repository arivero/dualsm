# Innovations for Opus

Proposed by a Fable subagent review of this repo.

## 1. Bring Lecture 11 (Koide Relation) through the full quality pipeline

`lectures/lecture-11.tex` ("The Koide Relation and the Dualised Standard Model") sits untracked in git, absent from `assessment/FINAL-SCORECARD.md` (which covers only Lectures 1-10), and lacks a companion exercise set — yet it is the bridge between this repo's 6x6 meson/VEV matrix framework and the Koide-relation work in the sibling `phys3`/`phys4` projects that fill `related-papers/`. Opus would run the lecture through the same assess → audit → adjudicate → revise workflow documented in `assessment/README.md`, write Exercise Set 9 with worked solutions in the established format, add a `scripts/verify_koide_vev.py` numerical check of the Koide VEV condition against PDG lepton masses, and commit the whole unit. This closes the one visibly unfinished piece of the corpus and formalizes the connection the symlinks and related-papers collection already gesture at.

**Size:** medium

## 2. A corpus-wide consistency linter built from the existing verify scripts

The 4-round assessment's central finding (`assessment/GENERAL-REPORT.md`) is that the dominant defect class was source-level contradiction — prompt-solution input drift, mid-file convention changes, abstract-vs-body mismatches — and `scripts/verify_vs_sannino2407.py` already prototypes the fix: regex-checking LaTeX sources against encoded expected statements. Opus would generalize this into a `scripts/lint_corpus.py` that parses the `ASSERT_CONVENTION` headers, verifies the shared conventions (T(fund)=1/2, Delta=3R/2, b_0 formulas, meson mass dimension, alpha_s inputs) hold identically across all 23 revised source files, and cross-checks numeric values quoted in multiple places (e.g., Lambda_D ~ 10^11 GeV, the n_g bounds table). Wired in as a pre-commit gate, it prevents the revised corpus (commit f6c0383) from regressing into exactly the error class the REVISION-PLAN spent four assessment rounds eliminating.

**Size:** medium

## 3. Paper 5: Escaping the Sp no-go — Kutasov-Schwimmer and product-group routes to composite Higgs doublets

Paper 1's headline result is a group-theoretic no-go: Sp(1)-dualising SU(2)_L yields only SU(2)_L-singlet mesons (diquarks, leptoquarks), never Higgs doublets — and its own `SUMMARY.md` lists the follow-ups: Kutasov-Schwimmer duality on SU(2)_L (whose k meson species may evade the antisymmetric obstruction), product SU x Sp dualities, and Sp electric baryons as Higgs candidates. Opus would work these three escape routes into a fifth paper following the established `papers/paper-N/` structure (paper.tex + SUMMARY.md + anomaly-matching verification script), recompute the generation bounds for any viable route, and feed the results back into Paper 4's duality-bounds table — either strengthening or breaking the "n_g = 3 uniquely selected" claim that is currently the programme's strongest output.

**Size:** large
