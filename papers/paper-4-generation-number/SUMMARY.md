# SUMMARY: Paper 4 -- Why Three Generations: The n_g >= 3 Bound Across Duality Types

**Status:** Complete
**Date:** 2026-03-20

## One-Liner

The intersection of SU and Sp Seiberg-type duality bounds uniquely selects n_g = 3 fermion generations; SO duality self-consistently excludes itself, and Kutasov-Schwimmer with k >= 2 admits no integer generation number.

## Conventions

| Convention | Value | Source |
|---|---|---|
| Units | natural (hbar = c = 1) | Seiberg hep-th/9411149 |
| Metric | (+,-,-,-) mostly minus | Seiberg |
| Sp(N) convention | rank N, fund dim 2N | Intriligator-Seiberg hep-th/9509066 |
| T(fund SU/Sp) | 1/2 | Seiberg / IS |
| T(vector SO) | 1 | IS |
| Dual Coxeter | h(SU(N))=N, h(SO(N))=N-2, h(Sp(N))=N+1 | IS |
| N_f counting | Dirac pairs (SU), vectors (SO), 2N_f total funds (Sp) | Standard |
| Epistemic | All non-SUSY claims conjectural | Project convention |

## Key Results

### Master Generation Bound Table

| Duality | Magnetic = SM | Electric | Group bound | CW range | Combined |
|---|---|---|---|---|---|
| SU Seiberg | SU(3)_c | SU(2n_g - 3) | n_g >= 3 | {3,4} | {3,4} |
| SU Pati-Salam | SU(3)_c via SU(4) | SU(2n_g - 4) | n_g >= 3 | {3,...,6} | {3,...,6} |
| Sp (IS) | Sp(1) = SU(2)_L | Sp(2n_g - 3) | n_g >= 2 | {2,3} | {2,3} |
| SO (IS) | SO(6) ~ SU(4) | SO(2n_g - 2) | n_g >= 3 | {4,5} | {4,5} |
| KS k=1 | SU(3)_c | SU(2n_g - 3) + adj | n_g >= 3 | {3,4} | {3,4} |
| KS k >= 2 | SU(3)_c | SU(2kn_g - 3) + adj | various | empty | ruled out |

### Central Result
[CONFIDENCE: HIGH]

**Intersection of SU and Sp bounds:**
- SU route: n_g >= 3 (electric SU group must be non-abelian)
- Sp route: 2 <= n_g <= 3 (group theory + conformal window)
- Intersection: **n_g = 3 uniquely**

This confirms and extends the result of Paper 1 (which showed SU intersection Sp gives n_g = 3).

### SO Exclusion
[CONFIDENCE: HIGH]

The SO route requires n_g >= 4 for conformal window compatibility (b_0 = 0 for n_g = 3). This self-consistently excludes SO as a duality frame for the SM with three generations. The physical origin is the +4 shift in the SO duality map: SO(N_f - N_c + 4).

### KS Exclusion for k >= 2
[CONFIDENCE: HIGH]

For Kutasov-Schwimmer duality with k >= 2, the conformal window width in n_g is 9/[k(4k-2)], which is less than 1 for k >= 2. No integer generation number fits. Only k = 1 (= Seiberg duality) is viable.

## Verification Checks

1. **SU Seiberg n_g=3:** N_c=3, N_f=6, CW 4.5<6<9. Matches standard Seiberg result.
2. **Sp n_g=3:** N_c=3, N_f=6, CW lower = 6 = N_f (boundary). Matches Paper 1.
3. **SO n_g=3:** N_c=4, N_f=6, b_0 = 3(2) - 6 = 0. Not asymptotically free. Confirmed.
4. **KS k=2 CW:** 9/8 < n_g < 3/2, width 0.375. No integers. Confirmed.
5. **Limiting case k=1:** KS reduces to Seiberg duality. Gauge group SU(N_f - N_c), CW 3N_c/2 < N_f < 3N_c. Consistent.

## Deviations

None. All derivations proceeded as planned.

## Artifacts

- **Paper:** `/home/codexssh/dualsm/papers/paper-4-generation-number/paper.tex` (15 pages, compiles cleanly)
- **PDF:** `/home/codexssh/dualsm/papers/paper-4-generation-number/paper.pdf`
- **Summary:** `/home/codexssh/dualsm/papers/paper-4-generation-number/SUMMARY.md`

## Open Questions

1. How does the non-SUSY conformal window (which is not exactly known) affect the Sp upper bound?
2. Could exceptional group dualities (G_2, F_4, E_6) provide additional constraints?
3. The SO exclusion relies on the SO(6) ~ SU(4) embedding; are there other SO embeddings of SM matter?
4. What happens if one allows the SM to sit at the boundary of (rather than inside) the conformal window for the SO case?

## Confidence Assessment

The generation bounds from group theory (non-abelian condition) are exact and do not depend on dynamical assumptions. [CONFIDENCE: HIGH]

The conformal window bounds depend on the exact SUSY result, which is rigorous in the SUSY context but whose extrapolation to non-SUSY is uncertain. The qualitative picture (SU provides lower bound, Sp provides upper bound) is robust. [CONFIDENCE: MEDIUM for non-SUSY extrapolation]

The uniqueness of n_g = 3 from the SU-Sp intersection is a purely algebraic result given the duality maps and the conformal window formulas. [CONFIDENCE: HIGH within the SUSY framework]
