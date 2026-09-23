# Exercise 07 XHigh Assessment
Source: `exercises/exercise-07.tex`
Scope: Content assessment of the three-part SUSY-duality exercise set, with attention to representation conventions, derivational adequacy, and prompt-solution consistency across anomaly matching, Kutasov-Schwimmer duality, and s-confinement.

## Strengths
The strongest feature of this file is its front-loaded clarity on conventions. The exercise explicitly fixes the normalisations for
$T(\fund_{\SU{N}})$,
$T(\text{vector}_{\SO{N}})$,
$T(\fund_{\Sp{N}})$,
dual Coxeter numbers, and the meaning of $\Sp{N_c}$. That makes Problem 1 genuinely useful: the $\SO{N_c}$ anomaly-matching calculation is concrete, well scaffolded, and mostly self-contained. The prompt tells the student exactly what data to use, and the solution carries the electric and magnetic
$\SU{N_f}^2 U(1)_R$
anomaly calculation through in a way that can actually be checked line by line.

The later choice of topics is also well chosen. Moving from a concrete
$\SO{N_c}$
example to the Kutasov-Schwimmer family and then to s-confinement gives students a reasonable map of the duality landscape. Problem 2(c), where the
$k=1$
case reduces to ordinary Seiberg duality, is particularly effective as a bridge between the generalised theory and the standard case.

## Concerns
The main weakness is that Problems 2 and 3 ask for more derivation than the source actually provides. In Problem 2(a), the prompt asks the student to derive the Kutasov-Schwimmer conformal window. But the solution does not derive the bounds from the ingredients stated in the question. It starts with the one-loop coefficient
$b_0 = 2N_c - N_f$,
then imports fixed-point language, NSVZ-style reasoning, unitarity, anomaly matching, and even
$a$-maximisation
references before simply stating the result
$3N_c/(k+1) < N_f < 3N_c/k$.
That is mechanism drift from the prompt: the exercise advertises a guided derivation, while the solution really gives a literature-backed summary. Even part 2(a)(i) muddies the pedagogy by verifying a supersymmetric beta-function coefficient through a non-SUSY-looking
$11/3 - 2/3$
Weyl-fermion count instead of the cleaner
$3T(\text{adj}) - \sum T(r)$
SUSY formula.

Problem 3 contains a direct convention mismatch. In 3(b)(i), the prompt states that
$M$, $B$, and $\widetilde B$
are dimensionless composites in canonical normalisation and then asks what dimension must be carried by
$\Lambda^{2N_c-1}$.
The solution ignores that convention and instead assigns
$[Q]=1$,
$[M]=2$,
$[B]=[\,\widetilde B\,]=N_c$.
That produces the standard answer
$[\Lambda^{2N_c-1}] = 2N_c - 1$,
but it answers a different normalisation problem from the one posed. This is not just loose wording; it changes what "dimensional check" means.

The extra moduli-counting discussion in 3(a)(ii) is also unreliable. The prompt only asks for the number of composite degrees of freedom, but the added "check against the microscopic theory" introduces gauge fixing, constraints, and arithmetic that are not transparently reconciled.

## Suggestions
Keep Problem 1 largely as written. The repairs should focus on Problems 2 and 3. For Problem 2, either provide the actual fixed-point machinery needed to derive the conformal window or weaken the wording from "derive" to "state and justify." The
$k=1$
reduction can stay ambitious because that part is much better aligned with the prompt.

Problem 3 should choose one normalisation convention and keep it throughout. If the composites are treated as dimensionless in the prompt, the coefficient structure of
$W_{\text{conf}}$
must be written consistently with that choice. If the intended calculation is the standard canonical-dimension one, then the phrase "dimensionless composites" should be removed. The moduli-counting side comment should also be dropped or rewritten carefully. As written, the file is strongest where it is explicit and algebraic, and weakest where it substitutes imported lore or changed conventions for actual derivation.
