# Exercise 01 Audit

## Source Pair
`exercises/exercise-01.tex` and `assessment/exercises/exercise-01.md`

## Verdict
Mostly accurate, but incomplete.

## What The Assessment Gets Right
The assessment correctly identifies the sheet's broad arc. The source really does move from Standard Model gauge-anomaly cancellation, to general `SU(N_c)` flavor-anomaly bookkeeping, to a chiral `SU(5)`-type example with antisymmetric matter. It is also right that Problem 1 is carefully scaffolded: the TeX explicitly tells students to convert right-handed fields into left-handed conjugates, and the worked solution spells out multiplicities step by step. The assessment's biggest substantive point is also well founded: Problem 2's solution does contain a pedagogically awkward false start. The source first computes nonzero `SU(2)_L^3` and `SU(2)_R^3` anomalies for two-flavor QCD, then pauses, retracts that line of reasoning, and reframes the real matching conditions in terms of mixed anomalies and the special status of `SU(2)`. That is exactly the kind of self-correcting sequence the assessment warns could confuse students.

## What It Misses Or Overstates
The assessment understates how concrete the Problem 2 issue is. This is not just a matter of tone or pacing; the solution explicitly presents an initial anomaly table with `SU(2)^3` entries, finds a mismatch with a nucleon doublet, and only then corrects itself by noting that `SU(2)` has no cubic `d^{abc}` anomaly. That is a real mathematical correction inside the worked solution, not merely an interpretive wobble. The assessment also does not mention that the exercise prompt itself asks students in part (a) to compute `SU(2)_L^3` and `SU(2)_R^3`, so the ambiguity is already built into the question, not just the answer. On the other hand, the note about Problem 3 needing an added multiplicity prompt is somewhat softer than the file warrants: Problem 3 is already fairly explicit about color-copy counting and the six anomaly coefficients. The larger omission is that the sheet never clearly reconciles the Problem 2 prompt with the later correction.

## Recommended Revisions
Revise the assessment so it says plainly that Problem 2 contains an internal correction about `SU(2)^3` anomalies, rather than describing the issue only as a pedagogical false start. It should also note that the problem statement itself asks for those cubic anomalies, so the source text needs tightening at the prompt level, not only in the prose of the solution. A stronger revision would recommend replacing the initial `SU(2)^3` calculation with either `SU(2)^2 U(1)_B` and Witten-anomaly discussion from the outset, or an explicit warning that the cubic-anomaly computation is a deliberate trap to be resolved. The rest of the original assessment can stay largely intact.
