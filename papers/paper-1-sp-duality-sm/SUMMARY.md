# SUMMARY: Sp(1) Seiberg Duality as an Alternative UV Completion of the Electroweak Sector

**Paper:** `paper-1-sp-duality-sm/paper.tex`
**Status:** Complete
**Date:** 2026-03-20

## One-liner

The Sp(1) Seiberg duality UV-completes SU(2)_L via an electric Sp(3) theory with 12 fundamentals, but the antisymmetric meson structure produces SU(2)_L singlets (diquarks, leptoquarks) rather than Higgs doublets -- a structural no-go for minimal EWSB.

## Conventions

| Convention | Value | Source |
|---|---|---|
| Sp naming | Sp(N_c) = rank N_c, fund dim 2N_c | Intriligator-Seiberg hep-th/9509066 |
| Sp duality | Sp(N_c) -> Sp(N_f - N_c - 2) | Intriligator-Seiberg hep-th/9506101 |
| T(fund Sp) | 1/2 | Project CONVENTIONS.md |
| h(Sp(N)) | N + 1 | Intriligator-Seiberg |
| Metric | (+,-,-,-) mostly minus | Project CONVENTIONS.md |
| Units | Natural (hbar = c = 1) | Project CONVENTIONS.md |
| Meson | M_{ij} = -M_{ji} antisymmetric | Sp structure |
| Non-SUSY | ALL claims conjectural | Epistemic convention |

## Key Results

### 1. Electric Theory Identified [CONFIDENCE: HIGH]
- **Result:** For n_g = 3 SM generations, SU(2)_L = Sp(1) has 2N_f = 12 Weyl doublets (9 quark + 3 lepton), so N_f = 6 and N_c = N_f - 3 = 3.
- **Electric theory:** Sp(3) with 12 fundamentals, dim(adj) = 21.
- **General:** Sp(2n_g - 3) with 4n_g fundamentals.
- **Verification:** Group-theoretic counting. Cross-checked with SM quantum numbers.

### 2. Anomaly Matching Verified [CONFIDENCE: HIGH]
- **Result:** SU(2N_f)^2 U(1)_R mixed anomaly matches:
  - Electric: A = -N_c(N_c+1)/N_f
  - Magnetic: A = -N_c(N_c+1)/N_f (after algebraic simplification of (a-2)(a-1) and (N_f-1)(N_f-2N_c-2) terms)
- **Numerical check:** Sp(3), N_f = 6: A^el = -12/6 = -2; A^mag = -1/3 - 5/3 = -2. Match.
- **Verification:** Symbolic derivation + numerical spot-check. Reproduces lecture 9 result.

### 3. Meson Content -> NO Higgs Doublets [CONFIDENCE: HIGH]
- **Result:** 66 complex meson components are all SU(2)_L SINGLETS (antisymmetric product: 2 x_A 2 = 1).
- **Meson types:** Diquarks (Y=+1/3), leptoquarks (Y=-1/3), charged singlets (Y=-1).
- **No-go:** None has Y = +/- 1/2 required for SM Higgs doublet.
- **Verification:** Group theory (SU(2) antisymmetric product is singlet) -- exact result.

### 4. Conformal Window Check [CONFIDENCE: HIGH]
- **Result:** Sp(3) with N_f = 6 has b_0 = 6 > 0 (AF). Sits at LOWER BOUNDARY of conformal window: N_f = 3(N_c+1)/2 = 6.
- **Magnetic:** b_0^mag = 0 (marginal coupling at one loop).
- **Physical:** Free magnetic phase -- magnetic description weakly coupled at low energies.
- **Verification:** Standard formula b_0 = 3(N_c+1) - N_f. Matches lecture 9 eq. (Sp-beta).

### 5. Generation Bounds [CONFIDENCE: HIGH]
- **Sp group-theory bound:** n_g >= 2 (from N_c = 2n_g - 3 >= 1).
- **Sp conformal window bound:** n_g <= 3 (from N_f >= 3(N_c+1)/2).
- **Combined Sp:** 2 <= n_g <= 3.
- **SU route:** n_g >= 3.
- **Intersection:** n_g = 3 UNIQUELY SELECTED.
- **Verification:** Enumerated all n_g = 2,3,4,5 cases explicitly.

### 6. Comparison with SU Route [CONFIDENCE: HIGH]
- **Main difference:** SU meson is bifundamental -> Higgs doublets. Sp meson is antisymmetric -> SU(2)_L singlets.
- **Root cause:** Pseudo-reality of SU(2) fundamental; antisymmetric SU(2) product is singlet.
- **Complementarity:** SU dualises QCD (produces Higgs), Sp dualises EW (produces diquarks/leptoquarks).

## Deviations

None. All tasks completed as planned.

## Issues

1. The SU(2N_f)^3 cubic anomaly matching requires careful treatment of the meson representation (Remark 4.3 in paper). We verified SU(2N_f)^2 U(1)_R explicitly and deferred the full cubic check to Intriligator-Seiberg.
2. The non-SUSY extrapolation is the weakest link in all results -- the SUSY duality structure is exact, but its applicability to the real SM is conjectural.

## Artifacts

- `paper.tex` -- Complete LaTeX paper (13 pages, compiles cleanly)
- `paper.pdf` -- Compiled PDF
- `SUMMARY.md` -- This file

## Physics Assessment

The central finding is a **no-go result**: the minimal Sp(1) Seiberg duality cannot produce Higgs doublets because the antisymmetric meson structure gives SU(2)_L singlets. This is a robust group-theoretic conclusion independent of dynamical assumptions. The construction does produce phenomenologically interesting composite scalars (leptoquarks, diquarks) and provides a complementary generation constraint that, combined with the SU route, uniquely selects n_g = 3.

## Recommended Follow-ups

1. Investigate product gauge group dualities that combine SU (for QCD) and Sp (for EW) simultaneously.
2. Explore whether higher-order Sp composites (baryons of the electric theory) could furnish Higgs doublets.
3. Study Kutasov-Schwimmer (SU + adjoint) duality applied to SU(2)_L -- this has k meson species and may evade the antisymmetric obstruction.
4. Compare the Sp-route leptoquark predictions with B-physics anomaly data.
