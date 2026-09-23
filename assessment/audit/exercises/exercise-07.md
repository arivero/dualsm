# Audit of Exercise 7 Assessment

## Source Pair
`exercises/exercise-07.tex` and `assessment/exercises/exercise-07.md`

## Verdict
Partly accurate but substantially incomplete. The assessment is directionally right about Problems 2 and 3, yet it leaves out several explicit convention and derivation mismatches that are present in the source.

## What The Assessment Gets Right
The assessment is correct that the overall sequence is pedagogically sensible. Problem 1 is a concrete anomaly-matching computation in `SO(N_c)`, Problem 2 broadens to the Kutasov-Schwimmer family, and Problem 3 treats s-confinement as a boundary case. That description matches the file closely.

It is also fair to say that Problem 2 is under-scaffolded relative to its ambition. The prompt asks students to "derive" the KS conformal window, but the solution leans on fixed-point language, NSVZ-style reasoning, anomaly matching, unitarity, and even `a`-maximization references without deriving the bounds from the stated ingredients. Likewise, the assessment is justified in saying the Problem 3 degree-counting discussion is shaky: the solution lists composite degrees of freedom, then compares them to a microscopic moduli count, then invokes constraints, but the numbers are not presented in a transparent or internally reconciled way.

## What It Misses Or Overstates
The biggest omission is Problem 3(b)(i). The prompt says "`M`, `B`, `\widetilde B` are dimensionless composites in canonical normalisation," then asks for the dimension carried by `Lambda^(2N_c-1)`. The solution answers a different question: it assigns `[Q]=1`, `[M]=2`, `[B]=N_c`, and derives the power from those dimensions. That is a direct prompt-solution convention mismatch, not merely "shaky" exposition.

The assessment also misses that Problem 2(a)(i) is not really a clean verification of the stated SUSY beta-function coefficient. The solution writes a non-SUSY-looking `11/3 - 2/3` Weyl-fermion counting formula and then simplifies to the SUSY result `2N_c - N_f`, which weakens the instructional clarity of the derivation.

## Recommended Revisions
The assessment should explicitly add the Problem 3 convention mismatch on operator dimensions and make the Problem 2 criticism more concrete: the source does not really derive the KS bounds from the prompt's own data. It would also be worth noting that Problem 1 is comparatively solid, so the weaknesses are concentrated in the later, more ambitious sections rather than spread uniformly across the whole set.
