# Assessment: Lattice Signatures of Emergent Supersymmetry at the Conformal Window Boundary

## Source
`papers/paper-3-emergent-susy-lattice/paper.tex`

## Scope
This paper argues that emergent supersymmetry near the lower boundary of the SU(3) conformal window would produce lattice-visible signatures for `Nf = 8, 10, 12`, and it proposes a measurement program to test that hypothesis.

## Strengths
The manuscript has a clear central question and a useful organizing principle: it tries to turn a broad conjecture into a finite set of lattice observables. The best parts are the explicit conditional framing, the numerical predictions for `gamma_m`, and the attempt to separate confining, conformal, and emergent-SUSY expectations side by side. That structure makes the paper easy to navigate and gives it some practical value as a proposal document.

The paper is also strongest when it stays close to quantities lattice groups can actually measure: the mass anomalous dimension, the scalar-to-pseudoscalar ratio, and volume dependence. Those sections are comparatively coherent and connect the conjecture to concrete data streams rather than to generic aesthetic parallels.

## Concerns
The main weakness is that the paper repeatedly crosses from “motivated analogy” to “derived prediction” without enough justification. The NSVZ-based `gamma_m` estimate is one thing; the extension of superconformal multiplet logic to a non-supersymmetric SU(3) theory at finite `Nc` is much less secure. Several observables rest on that jump rather than on a controlled argument.

Observables 2, 4, and 5 are especially fragile. The glueball-gluinoball discussion depends on adjoint matter that is not present in the target theories, so the proposed proxy is not clearly equivalent to the claimed signal. The SUSY Ward-identity section is even more problematic: the paper never establishes a concrete lattice supercurrent for the actual theory under study, so the proposed violation parameter reads more like a formal wish than a defined observable. The effective-potential/flat-direction argument similarly imports SUSY moduli-space intuition into a theory where no such structure has been justified.

The paper also overstates novelty and discriminating power. The five observables are not independent tests; several are variants of the same scalar-sector question, so the paper implies more coverage than it actually has. The comparisons with existing lattice data are suggestive but not decisive, and some phrasing makes them sound stronger than they are. In particular, light-scalar data at `Nf = 8` support “interesting compatibility,” not evidence of emergent SUSY.

## Suggestions
Narrow the paper’s claims to the observables with the clearest operator mapping and the strongest chance of being falsifiable. `gamma_m` and `m_sigma / m_pi` should likely be the core, with the remaining proposals explicitly labeled as speculative extensions rather than equal-status diagnostics.

Add a short section that states, for each proposed observable, what would count as a successful test, what would count as a null result, and what alternative dynamics would mimic the same signal. That would improve scope discipline and make the proposal more scientifically usable.

Finally, soften the language around existing lattice results. The paper should say they are “compatible with” or “suggestive of” the conjecture, not that they materially support emergent SUSY over walking or dilaton-based explanations.
