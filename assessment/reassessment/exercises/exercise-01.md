# Exercise 01 XHigh Assessment

Source: `exercises/exercise-01.tex`

## Scope
This sheet covers four distinct layers of anomaly reasoning: Standard Model gauge-anomaly cancellation, a two-flavor QCD anomaly-matching example, the general `SU(N_c)` flavor-anomaly formulas, and a chiral antisymmetric-matter challenge with an `SU(5)` specialization. As a sequence, it is ambitious but coherent. Problem 1 is a warm-up on exact gauge consistency conditions; Problems 2 and 3 pivot to exact global-symmetry matching; Problem 4 broadens the representation theory and points toward later dualized-SM material. The broad architecture is strong, and the source is at its best when it states conventions explicitly and then turns them into transparent anomaly tables.

## Strengths
Problem 1 is the cleanest unit in the file. The prompt tells students to convert right-handed fields to left-handed conjugates, and the solution then carries that bookkeeping through carefully for `SU(3)^2 U(1)_Y`, `SU(2)^2 U(1)_Y`, and `U(1)_Y^3`. That is exact, source-grounded pedagogy rather than hand-waving. Problem 3 is also strong: it extracts the six standard UV coefficients for `SU(N_c)` with `N_f` fundamentals in a way that is reusable later, and it correctly distinguishes exact symmetries from the anomalous `U(1)_A`.

Problem 4 is a good challenge problem. The gauge-anomaly cancellation check is concise, the `SU(5)` specialization is well chosen, and the discussion of why chiral theories are more constrained than vector-like ones gives the sheet a useful forward link to GUT-style matter assignments.

## Concerns
The central weakness is Problem 2, and it is more concrete than a mere pedagogical wobble. The prompt explicitly asks for `SU(2)_L^3` and `SU(2)_R^3` anomalies, and the hint even says the `SU(2)_L^3` anomaly is nonzero. The worked solution initially computes those coefficients as `3`, then later stops, states that `SU(2)` has no cubic `d^{abc}` tensor, and redefines the real matching problem in terms of mixed anomalies and the special `SU(2)` global-anomaly story. That is a prompt-solution misalignment inside the source itself, not just an awkward exposition choice.

Problem 2 also slides from exact anomaly logic into a heuristic IR narrative. The move from pions to a "massless nucleon Dirac doublet" is presented as the matching agent, but the source itself has already had to change which anomalies matter. The result is that the exact claim, the stylized IR hypothesis, and the chiral-limit physical aside are not cleanly separated. Earlier reviews that described this only as a soft false start understated the problem: the mathematical target changes mid-solution.

Problem 4 has a smaller alignment issue. The hint for the non-anomalous `U(1)` suggests charge assignment by gauge-invariant operators, while the solution actually fixes charges by canceling the mixed `SU(N)^2 U(1)` anomaly. Both are relevant, but the route students are told to use is not the route the solution models.

## Suggestions
Rewrite Problem 2 from the prompt onward. Either remove the `SU(2)^3` request entirely and frame the exercise around `SU(2)^2 U(1)_B` plus the Witten anomaly, or label the cubic-anomaly computation as an intentional trap that is resolved explicitly. Also separate exact statements from heuristic ones: the mixed-anomaly equalities are exact, while the nucleon discussion is a model of the IR realization and should be labeled that way.

For Problem 4, align the hint with the actual solution method, or add one sentence showing how the gauge-invariant-operator perspective and the mixed-anomaly perspective fit together. That would make an already strong sheet feel consistently controlled from prompt to solution.
