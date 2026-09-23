# Audit of Exercise 5 Assessment

## Source Pair
`exercises/exercise-05.tex` and `assessment/exercises/exercise-05.md`

## Verdict
Accurate on the central inconsistency, but incomplete. The assessment correctly identifies the file's main prompt-solution mismatch, yet it understates how explicit and repeated that mismatch becomes in the worked solution.

## What The Assessment Gets Right
The assessment is right that the exercise has a coherent pedagogical arc: Problem 1(a) establishes the universal Yukawa/top-mass story, 1(b) introduces dormant-Higgs suppression, and 1(d) asks students to distinguish mechanism from prediction. It also correctly notes that the source text itself is careful about epistemic status. The convention box, opening background, and closing discussion all distinguish exact algebraic statements from the conjectural non-SUSY duality interpretation.

Its main criticism is also well founded. In 1(b)(ii)-(iii), the prompt and solution derive the generic suppression
`m_f/m_t ~ xi_i Lambda_D^2 / M_Pl^2`, and for `Lambda_D = 10^11 GeV` the solution evaluates this as `6.7 x 10^-17`. That is many orders of magnitude below the quoted bottom, charm, and strange mass ratios. The assessment is correct that the solution then pivots to a different explanation for the bottom quark, namely a "direct" `H^u_33-H^d_33` mixing, without that mechanism being cleanly set up in the question.

## What It Misses Or Overstates
What the assessment misses is the severity of the contradiction in part 1(c). The prompt explicitly asks for a positive integer power `p` and ties `p = 2, 4, ...` to tier structure. The solution first says the operator structure gives `p = 2`, then computes `p ~= 0.2`, and then states that `p` "need not be an integer." That is not just a soft pedagogical mismatch; it directly contradicts the wording of the question.

The assessment also does not spell out that part 1(b)(iii) and part 1(c) are using incompatible suppression logics. In 1(b), one insertion gives `10^-16`; in 1(c), the bottom ratio is effectively replaced by an unexplained `mu_b^2 / M_{d,33}^2 ~ 10^-2`.

## Recommended Revisions
Revise the assessment so it explicitly names the two concrete contradictions: integer `p` versus `p ~= 0.2`, and generic Planck suppression versus ad hoc direct mixing for the bottom quark. It would also help to note that the source is strongest where it frames the whole construction as a parametric consistency check, and weakest where it tries to convert that qualitative hierarchy story into a quantitative tier-counting exercise.
