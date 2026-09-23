# Exercise 07 Adjudication

## Source Triple
- `exercises/exercise-07.tex`
- `assessment/exercises/exercise-07.md`
- `assessment/audit/exercises/exercise-07.md`

## Final Ruling
REVISE

## Confidence
Medium-high

## Why Keep/Revise/Replace
The first-pass assessment gets the broad pedagogical shape right. Problem 1 is indeed the strongest part: it is a concrete `SO(N_c)` anomaly-matching calculation with clear bookkeeping, and the move from that example to Kutasov-Schwimmer duality and then s-confinement is a coherent tour of the duality landscape. The first pass is also right that Problem 2 is under-scaffolded relative to its ambition. The prompt asks students to derive the Kutasov-Schwimmer conformal window, but the solution imports NSVZ-style reasoning, fixed-point language, unitarity, and even `a`-maximization references rather than deriving the bounds from the prompt’s own ingredients. Its skepticism about the Problem 3 counting discussion is also justified.

Even so, the first pass is too general to stand unchanged. It misses a direct prompt-solution convention clash in Problem 3(b)(i). The prompt states that `M`, `B`, and `\widetilde B` are “dimensionless composites in canonical normalisation” and asks what dimension must be carried by `Lambda^(2N_c-1)`. The solution answers by reverting to canonical field dimensions `[Q]=1`, `[M]=2`, `[B]=N_c`, and then deriving the required power. That is not merely shaky exposition; it is a mismatch in the stated conventions of the exercise itself. The first pass also could be sharper about Problem 2(a)(i): the solution “verifies” the SUSY beta-function coefficient by writing a non-SUSY-looking `11/3 - 2/3` Weyl-fermion counting formula before simplifying to the stated result, which weakens clarity even if the final number is right.

## Minimum Changes Needed
- Add the explicit convention mismatch in Problem 3(b)(i) as a headline concern.
- Make the Problem 2 criticism concrete by stating that the bounds are asserted through imported fixed-point logic rather than actually derived from the prompt.
- Note that Problem 1 is comparatively solid so the weaknesses are concentrated in Problems 2 and 3.

## Notes For Final Summary
This first assessment is not unreliable, but it is too diffuse. Revision should make it less impressionistic and more source-anchored by naming the exact convention and derivation mismatches.
