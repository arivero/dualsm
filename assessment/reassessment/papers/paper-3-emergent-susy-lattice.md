# Title
XHigh Assessment: Lattice Signatures of Emergent Supersymmetry at the Conformal Window Boundary

## Source
`papers/paper-3-emergent-susy-lattice/paper.tex`

**Correction to this historical review.** The formula endorsed below, `3N_c/N_f`, is the mass-source eigenvalue. The anomalous dimension is smaller by one because the mass couples to the meson's top component. For eight flavours it equals 1/8 in SQCD. The revised paper states the extra assumption needed to compare this number with QCD and the symmetry obstruction to a literal multiplet map. [Current Paper 3 summary](../../../papers/paper-3-emergent-susy-lattice/SUMMARY.md)

## Scope
This paper is best read as a conditional lattice-proposal paper rather than as evidence that emergent supersymmetry has already been observed. Its core move is to start from the Antipin-Mojaza-Pica-Sannino Veneziano-limit result on emergent SUSY in a magnetic dual, assume that some finite-`N_c` remnant survives for non-supersymmetric `SU(3)` near the lower conformal-window boundary, and then ask what lattice observables at `N_f = 8, 10, 12` should look like if that assumption is right. The load-bearing argument is therefore not the five-observable list by itself, but the transfer of superconformal operator relations into a non-SUSY finite-`N_c` setting.

## Strengths
The paper is unusually explicit about its own conditionality. The abstract, introduction, Section 3 opening, prediction-table caption, and conclusion all say in one form or another that the emergent-SUSY claims are conjectural and are meant to be tested rather than presumed. That matters, because the paper is strongest when treated as a structured measurement programme under a stated hypothesis.

Within that framing, the most solid derivation is the mass-anomalous-dimension prediction. The route from the SQCD R-charge relation to `dim(M)`, then to `gamma_m = 3N_c/N_f`, is internally coherent, numerically explicit for `N_f = 8, 10, 12`, and compared against Banks-Zaks, Schwinger-Dyson, and available lattice values. Observable 1, the scalar-to-pseudoscalar ratio, is also a plausible phenomenological target: the paper explains why `m_sigma / m_pi -> 1` would be distinctive if the scalar and pseudoscalar really sit in one supermultiplet, and it correctly notes the existing dilaton competitor. The scenario table and the prioritisation of `N_f = 10` are also useful, because the manuscript recognizes that the whole proposal is boundary-sensitive and that at most one of `8, 10, 12` can be the true candidate `N_f*`.

## Concerns
The main weakness is that the paper's downstream predictions are only as strong as its bridge from supersymmetric magnetic-dual logic to the actual non-supersymmetric `SU(3)` theories being discussed. That bridge is openly conjectural, but it still carries substantial argumentative weight. Once that is granted, Observable 3 is reasonably motivated; Observables 2, 4, and 5 are not.

Observable 2 depends on adjoint-fermion/gluinoball structure that the target fundamental-fermion lattice theories do not possess. The paper admits the observable is "not directly available," but the prediction table still promotes a concrete glueball-meson near-degeneracy that is not actually derived for the stated source theory. Observable 4 is even less secure: the proposed Ward-identity violation parameter is written down before the manuscript has established a workable supercurrent for the non-SUSY theory, and the crucial electric-theory implementation is left at the level of composite-operator aspiration. Observable 5 similarly imports SUSY moduli-space and pseudo-modulus language into a chiral-condensate effective potential without showing that the non-SUSY theory should inherit those flat directions rather than merely a light scalar from some other mechanism.

The paper also has intermittent rhetorical overreach. Phrases such as "sharp, quantitative predictions," "`N_f = 8` is strikingly close," "in tension with ordinary confinement," and "test decisively" run ahead of what the source has established. The manuscript often qualifies itself correctly, but the five-observable presentation can still flatten the hierarchy between two comparatively load-bearing diagnostics (`gamma_m` and `m_sigma / m_pi`) and three speculative extensions.

## Suggestions
Recast the paper explicitly as a tiered proposal. Observable 3 and, secondarily, Observable 1 should be the core case; Observables 2, 4, and 5 should be labeled exploratory and contingent on additional operator-mapping work. A short per-observable table stating the operator dictionary, what would count as a null result, and what non-SUSY dynamics could mimic the signal would materially improve the paper.

The boundary logic should also be made harder to miss. Since emergent SUSY is asserted to occur only at `N_f = N_f*`, the manuscript should separate "boundary-only" predictions from off-boundary comparisons more sharply and soften evidentiary language around current `N_f = 8` data and Ward-identity feasibility.
