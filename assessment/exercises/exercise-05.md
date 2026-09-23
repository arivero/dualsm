# Exercise 5 Assessment
Source: `exercises/exercise-05.tex`
Scope: content quality of the prompts and embedded solution, especially the scalar-democracy hierarchy argument.

## Strengths
This set has a clear narrative arc: a dominant top Yukawa, then induced VEVs for lighter fermions, then a discussion of what is actually being claimed. The exercise does a good job separating exact structural statements from the conjectural duality interpretation, and the final discussion prompt is pedagogically useful because it forces students to distinguish "prediction" from "parametric consistency check." The worked solution also models the kind of order-of-magnitude reasoning the course seems to want: it keeps the universal Yukawa idea central and repeatedly returns to the role of free coefficients and Planck-suppressed operators.

## Concerns
The main issue is internal consistency. Part (b)(iii) asks students to compare the generic suppression factor $\Lambda_D^2/M_{Pl}^2 \sim 10^{-16}$ with observed mass ratios of order $10^{-2}$ to $10^{-4}$, which is a deliberately huge mismatch. That mismatch is not really resolved later; the solution effectively abandons the generic estimate and introduces a different "direct mixing" mechanism for the bottom quark. As written, a student could reasonably conclude the exercise is asking for one mechanism and the solution is using another.

Part (c) is also problematic. The prompt asks for a power $p$ in
\[
m_b/m_t \sim c_b (\Lambda_D/M_{Pl})^p,
\]
but the solution first asserts $p=2$ from the operator structure and then computes $p\approx 0.2$ from the observed ratio. Those two answers are not compatible, and the solution's claim that $p$ "need not be an integer" contradicts the prompt's language about tiers and positive integer powers. This is the kind of inconsistency that will mislead students about what is being tested.

There is also a sequencing issue: the exercise asks for "tier" assignments before the hierarchy has been made quantitatively coherent. That makes the pedagogical message feel retrofitted rather than derived.

## Suggestions
Decide whether this exercise is about a strict parametric estimate or about a qualitative hierarchy story. If it is qualitative, remove the integer-$p$ language and ask students to rank the fermions by tier with explicit caveats. If it is quantitative, then the solution needs a consistent suppression model that actually reproduces the quoted ratios to the intended accuracy.

The bottom-quark discussion should be rewritten so the prompt and solution use the same mechanism. If a direct $H_{33}^u$--$H_{33}^d$ mixing term is intended, say so up front; if the generic Planck-suppression estimate is the intended lesson, then the target ratio needs to be adjusted or the $O(1)$ coefficients made explicit in the question.
