# Exercise 03 XHigh Assessment

Source: `exercises/exercise-03.tex`

## Scope
This sheet is a practical Seiberg-duality workshop. It moves from explicit electric/magnetic anomaly matching in the benchmark `SU(3), N_f=6` case, to a mass deformation down to `N_f=5`, then to non-anomalous `R`-charges, and finally to `s`-confinement at `N_f=N_c+1`. The overall progression is excellent: each problem reuses machinery from the previous one and builds toward more structural statements about dual descriptions. The file is dense, but its ambition is appropriate for an advanced exercise set.

## Strengths
Problem 1 is very strong. The complete quantum-number tables for both electric and magnetic theories force students to organize the data before doing anomaly arithmetic, and the six explicit checks are concrete rather than merely symbolic. That makes the problem genuinely diagnostic. Problem 2 is also well chosen. Mapping a mass term on the electric side to a meson deformation on the magnetic side is exactly the kind of operational duality check students should practice.

Problem 3 is compact but valuable because it isolates a reusable method: derive the anomaly-free `R`-charge, map it through the magnetic superpotential, and relate the meson dimension to the conformal-window boundary. Problem 4 has a strong conceptual target as well. Asking for the most general symmetry-allowed superpotential before quoting the exact confining form is good pedagogy, and the anomaly check for `SU(4)_L^3` closes the loop cleanly.

## Concerns
The main reliability problem is in Problem 4's dimensional analysis, because the prompt and solution visibly disagree with themselves. The hint states that mesons have dimension `[mass]`, the solution initially repeats that assignment, and the first pass through the calculation produces `[mass]^2` instead of `[mass]^3`. The source then stops and corrects the meson dimension to `[mass]^2`. That is a genuine prompt-solution mismatch and the sharpest issue in the file. Earlier reviews that focused only on density or scaffolding missed the concrete source-level error.

Problem 3 has a smaller but real inconsistency: the background states the chiral-primary relation as `Delta = 3|R|/2`, while the solution uses the standard `Delta = 3R/2` formula. The downstream computation is fine, but the sheet should not force students to infer which formula it really intends.

Problem 2 is conceptually right but under-explained. The `F`-term condition producing `<q_6 \tilde q^6> != 0` is clear, yet the step from that vev to the statement that `SU(3)` Higgses to `SU(2)` is too compressed. The source gives the outcome without showing the gauge orientation, the rank-lowering mechanism, or what becomes massive.

## Suggestions
Fix Problem 4 at the source level. The hint should assign the meson the same dimension the solution ultimately uses, or the false start should be reframed explicitly as a diagnostic checkpoint rather than left as an accidental correction. Problem 3 should standardize the conformal-dimension formula between background and solution. Problem 2 would benefit from one short paragraph explaining how a fundamental vev selects an `SU(2)` subgroup and which fields are integrated out after Higgsing.

The file does not need a conceptual rewrite; it needs sharper alignment between what it asks, what it hints, and what the worked solution actually demonstrates.
