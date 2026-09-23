# Audit of Exercise 6 Assessment

## Source Pair
`exercises/exercise-06.tex` and `assessment/exercises/exercise-06.md`

## Verdict
Mostly accurate, but materially incomplete. The assessment catches the most visible numerical bait-and-switches, but it misses a more basic prompt-solution contradiction in the electric beta-function discussion.

## What The Assessment Gets Right
The assessment accurately describes the source structure. The exercise is organized cleanly into one-loop QCD running, matching at the duality scale, the electroweak seesaw relation, and a final input/output synthesis. It also correctly identifies the two biggest numerical inconsistencies.

First, part 1(b)(ii) tells the student to use `alpha_s(Lambda_D) = 0.3` at `Lambda_D = 10^11 GeV`, and the solution does exactly that long enough to obtain the absurd result `Lambda_QCD ~ 5 x 10^9 GeV`. It then abandons the stated input and replaces it with an RG-evolved value `alpha_s(Lambda_D) ~= 0.032`, producing `Lambda_QCD ~= 70 MeV`. The assessment is right that this is a legitimate physics move but not the calculation the prompt asked for.

Second, the assessment correctly notes that `v ~ Lambda_D^2 / M_Pl` gives about `820 GeV`, not `246 GeV`, for the quoted `Lambda_D = 10^11 GeV`, and that the solution treats the mismatch as acceptable only after invoking unspecified `O(1)` factors.

## What It Misses Or Overstates
The largest omission is part 1(b)(i). The prompt tells students to "argue that the electric theory is not asymptotically free (or marginally so)," but the solution computes `b_0^e = 4 > 0` and explicitly concludes the opposite: the electric theory is asymptotically free and therefore grows strong in the IR. That is a direct contradiction between question and solution, and it is more fundamental than the later numerical inconsistencies.

The assessment also understates how much the summary table rewrites the setup. The prompt uses `alpha_s(Lambda_D) ~ 0.3`; the final table silently relabels it as an input `~ 0.03`.

## Recommended Revisions
Add the electric-theory beta-function contradiction to the assessment and elevate it near the top. Then distinguish two separate issues: one is a conceptual prompt-solution clash in 1(b)(i), and the other is the solution changing numerical inputs midstream in 1(b)(ii) and 1(d)(i). That would make the audit better aligned with the actual source content.
