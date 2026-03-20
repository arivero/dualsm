# SUMMARY: Dual Meson Mass Sum Rules from the 6x6 Flavour Matrix

**Paper:** `paper-2-meson-mass-sum-rules/paper.tex`
**Status:** Complete
**Date:** 2026-03-20

## One-Liner

Six classes of meson mass sum rules derived from the 6x6 flavour matrix; only the scalar democracy geometric hierarchy (m_s/m_t ~ (m_b/m_t)^2, verified at 8%) is genuinely new -- all others reproduce standard QCD results from ChPT, HQET, and the additive quark model.

## Conventions

| Convention | Value |
|---|---|
| Units | Natural (hbar = c = 1) |
| Metric | Mostly minus (+,-,-,-) |
| f_pi | 92.1 MeV (Gasser-Leutwyler) |
| ChPT field | U = exp(2i pi^a T^a / f_pi) |
| Quark masses | MS-bar at 2 GeV (light); pole masses (heavy) |

## Key Results

### Sum Rule I: GMOR and Kaon Mass Ratio (Standard QCD)
- GMOR: m_pi^2 f_pi^2 = -(m_u + m_d)<qqbar> -- verified at ~10%
- Weinberg ratio: m_K^2/m_pi^2 = (m_u+m_s)/(m_u+m_d) -- 12.5 vs 14.0 (12% NLO corrections)
- [CONFIDENCE: HIGH] -- standard ChPT, well-verified

### Sum Rule II: Gell-Mann--Okubo (Standard QCD)
- 4m_K^2 = 3m_eta^2 + m_pi^2 at 5.7% (discrepancy from eta-eta' mixing)
- Anomaly mass m_0 = 854 MeV, consistent with Witten-Veneziano prediction (862 MeV)
- [CONFIDENCE: HIGH] -- standard SU(3) flavour

### Sum Rule III: Heavy Quark Symmetry Flavour Splittings (Standard QCD)
- Delta_s^(c) = m_Ds - m_D0 = 103.5 MeV
- Delta_s^(b) = m_Bs - m_B0 = 87.2 MeV
- Difference = 16.3 MeV ~ O(Lambda_QCD^2/m_c), consistent with 1/m_Q expansion
- m_B - m_D independent of light quark to < 17 MeV
- [CONFIDENCE: HIGH] -- standard HQET

### Sum Rule IV: B_c Mass Sum Rule (Standard QCD)
- m_Bc = (m_Jpsi + m_Upsilon)/2 to 4 MeV (0.06%) -- remarkably precise
- Structural interpretation: rectangular identity of the meson matrix
- Nussinov-Wetzel inequality satisfied: m_Bc^2 < (m_Jpsi^2 + m_Upsilon^2)/2
- [CONFIDENCE: HIGH] -- additive quark model, confirmed experimentally

### Sum Rule V: Scalar Democracy Geometric Hierarchy (NEW -- DSM specific)
- m_s/m_t = 5.41e-4 vs (m_b/m_t)^2 = 5.86e-4: ratio = 0.92 (8% accuracy)
- m_s/m_b = 0.0223 vs m_b/m_t = 0.0242: ratio = 0.92 (8% accuracy)
- Tier structure with epsilon ~ 0.024 describes 5 orders of magnitude in quark masses
- [CONFIDENCE: MEDIUM] -- framework-dependent, O(1) free parameters limit precision

### Sum Rule VI: Heavy-Light Column Sum Rule (Standard QCD)
- (m_Ds - m_D0) - (m_Bs - m_B0) = 16.3 MeV ~ O(Lambda_QCD^2/m_c)
- Rectangular identity: exact in heavy-heavy sector (7 MeV), fails at 7% in mixed sectors
- [CONFIDENCE: HIGH] -- standard HQET

## Honest Assessment

**What is new:** Only Sum Rule V (scalar democracy hierarchy) is genuinely new content from the dualised SM framework. The relation m_s/m_t ~ (m_b/m_t)^2 is not derivable from any QCD symmetry and represents a non-trivial consistency check. It holds at 8% with a single parameter epsilon ~ 0.024.

**What is not new:** Sum Rules I-IV and VI are well-established consequences of chiral symmetry, heavy quark symmetry, and the additive quark model. The meson matrix structure makes these relations manifest (especially the rectangular identity for Bc), but does not produce sharper predictions than standard QCD effective theories.

**Limitations:** The ~100 free O(1) coefficients (Planck-scale operators c^{abcd}) limit the predictive power. The framework explains the hierarchy but cannot predict individual mass values.

## Deviations

None. All sum rules derive cleanly from the effective theories.

## Artifacts

- `paper.tex` -- Complete LaTeX paper (15 pages)
- `paper.pdf` -- Compiled PDF
- `SUMMARY.md` -- This file

## Self-Check: PASSED

- [x] paper.tex exists and compiles without errors
- [x] paper.pdf generated (15 pages, 329 kB)
- [x] GMOR and GMO reproduced as consistency check
- [x] Heavy-light sum rules derived from meson matrix
- [x] Numerical comparison with PDG data (Table 1)
- [x] Assessment of which sum rules are new vs known
- [x] All numerical values cross-checked against PDG 2024
- [x] Convention consistency verified (natural units, mostly-minus throughout)
