# Exercise 05 Adjudication

## Source Triple
- `exercises/exercise-05.tex`
- `assessment/exercises/exercise-05.md`
- `assessment/audit/exercises/exercise-05.md`

## Final Ruling
REVISE

## Confidence
High

## Why Keep/Revise/Replace
The first-pass assessment is directionally right and identifies the core failure mode of the exercise: the prompt and worked solution stop using a single suppression logic once the numbers become inconvenient. It correctly flags the clash between the generic estimate in Problem 1(b), where the solution derives
`m_f/m_t ~ xi_i Lambda_D^2 / M_Pl^2` and evaluates it at about `6.7 x 10^-17`, and the observed quark-mass ratios quoted in the prompt, which are many orders of magnitude larger. It also correctly notices that the solution later pivots to a different bottom-quark story based on direct `H^u_33-H^d_33` mixing without clearly aligning that move with the question.

That said, the first pass is not precise enough to stand unchanged. The most serious contradiction is in Problem 1(c): the prompt explicitly asks for a positive integer power `p` and ties `p = 2, 4, ...` to the tier interpretation, but the solution first says the operator structure gives `p = 2`, then computes `p ~= 0.2`, and finally says `p` need not be an integer. That is not just a soft pedagogical mismatch. It is a direct contradiction between what the student is asked to determine and what the solution permits. The first-pass assessment mentions the inconsistency, but it understates how explicit and disqualifying it is.

## Minimum Changes Needed
- Elevate the Problem 1(c) contradiction to the lead concern, not a secondary one.
- State explicitly that the solution gives two incompatible suppression mechanisms: generic Planck suppression in 1(b) and ad hoc direct mixing in 1(c).
- Tighten the conclusion from “sequencing issue” to “prompt-solution inconsistency that would mislead students about the intended mechanism.”

## Notes For Final Summary
This is a useful first assessment with the right overall diagnosis, so replacement is unnecessary. The needed fix is sharper specificity: name the integer-`p` contradiction and the mechanism swap as the two decisive defects.
