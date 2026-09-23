# Exercise 04 XHigh Assessment

Source: `exercises/exercise-04.tex`

## Scope
This source has three problems, not four, and that structural fact matters because earlier review language drifted away from the actual file. The sheet covers `N=2` to `N=1` multiplet decomposition and beta-function counting, Fayet-Iliopoulos `D`-term mechanics, and the APS deformation for the self-dual `SU(2), N_f=4` case. As a supersymmetric exercise set, it is internally focused and much more coherent than any review that treats it as a mixed SUSY/non-SUSY phase survey. The file itself even includes a scope note in Problem 3 stating that the Seiberg-Witten solution is accepted as input and that the exercise is about deformation logic rather than rederiving the curve.

## Strengths
Problem 1 is the strongest section. The `N=2` to `N=1` decomposition is explicit, the hypermultiplet degree-of-freedom count is straightforward, and the one-loop beta-function computation cleanly reproduces `b_0=2N_c-N_f`. The superpotential dimension and `R`-charge checks also fit naturally at the end of that problem.

Problem 2 is pedagogically solid. The one-field FI analysis is concrete, the dimensional analysis is explicit, the gauge-boson mass computation is easy to follow, and the two-field extension correctly shows why opposite charges restore `D`-flatness for either sign of `xi`. The final confinement analogy is appropriately placed as a conceptual bridge after the mechanics have been established.

Problem 3 is well scoped. The deformation `W_def = mu Tr Phi^2`, the `mu -> infinity` decoupling limit, and the identification of the surviving `N=1` theory are all clearly staged. The later checks on meson dimension and the `N=1` conformal window are also consistent with the source's supersymmetric setting.

## Concerns
The clearest local error is in the remark at the end of Problem 1. It says the `N=2` and `N=1` `R`-symmetries "coincide" at `N_f=2N_c`, then immediately evaluates the `N=1` value as `(N_f-N_c)/N_f = 1/2`, not `1`. The source is trying to express a relation between symmetry structures, but the wording says numerical coincidence and then disproves itself.

Problem 3 becomes more interpretive in its last steps than the earlier parts. The derivation that integrating out `Phi` leaves `N=1` `SU(2)` with four flavors is clear, but the claim that `N=2` `SL(2,Z)` duality simply descends to `N=1` Seiberg self-duality is presented as a guided narrative rather than a demonstrated result. That is acceptable if labeled as interpretation, but the current solution states it with more confidence than it earns.

Problem 2(e) has a similar status. The monopole-condensation analogy is physically standard, yet it is heuristic within this worksheet and should be marked as such. Earlier reviews that criticized a nonexistent "Problem 4" or imported non-SUSY conformal-window concerns were structurally mismatched to the actual source.

## Suggestions
Fix the Problem 1 `R`-symmetry remark so it distinguishes "related by mixing" from "numerically equal." In Problem 3, add one sentence separating what is explicitly shown in the exercise from what is being accepted from the broader Seiberg-Witten and APS framework. In Problem 2(e), label the confinement paragraph as an analogy or physical interpretation rather than a derived consequence of the toy `U(1)` model.

The main repair here is precision, not overhaul. The source already has a coherent three-problem supersymmetric structure; the assessment should stay anchored to that structure and the file itself should sharpen a few statements at the exact-versus-heuristic boundary.
