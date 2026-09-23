# Exercise 7 Assessment
Source: `exercises/exercise-07.tex`
Scope: content quality of the SUSY-duality tour, especially anomaly matching, Kutasov-Schwimmer, and s-confinement.

## Strengths
This set has strong thematic cohesion. It moves from a concrete anomaly-matching computation in $\SO(N_c)$, to the broader Kutasov-Schwimmer family, and then to the boundary case of s-confinement. That progression is pedagogically sensible: students first see a fully worked algebraic check, then they are asked to generalize, and finally they are shown where the duality picture degenerates. The $\SO(N_c)$ problem is especially good at forcing careful representation bookkeeping.

## Concerns
The Kutasov-Schwimmer material is under-scaffolded relative to its difficulty. The prompt asks students to derive the conformal window and reduce the $k=1$ theory to Seiberg duality, but the solution leans on advanced fixed-point logic, anomaly arguments, and references to $a$-maximization without giving the student enough intermediate structure. A student who has only the stated background will likely be asked to accept too much on faith.

There is also a mismatch between the algebraic level of the questions and the sophistication of some solution steps. In Problem 2, the derivation of the upper and lower bounds is not really derived from the prompt's own ingredients; instead it compresses several results from the literature into a short narrative. That makes the exercise feel like a result summary rather than a guided derivation.

Problem 3 is conceptually valuable, but the solution's degree-counting is shaky. The text mixes microscopic degrees of freedom, gauge redundancy, and composite constraints in a way that is not easy to audit. Even if the final qualitative point is right, the path to it is not rigorous enough for students to use as a model.

## Suggestions
For the Kutasov-Schwimmer section, either add a short derivational scaffold or reduce the ambition. A two-step structure would work better: first ask for the $k=1$ reduction, then separately ask for the conformal-window statement as a conceptual consequence rather than a derivation.

In the s-confinement problem, make the counting target explicit. If the goal is to identify the trivial dual group and list the composite degrees of freedom, say that directly and avoid a quasi-derivation of moduli counting unless the necessary constraints are also given. The overall sequence is good; it just needs tighter alignment between what the prompt asks and what the solution actually justifies.
