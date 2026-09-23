# Exercise 03 Adjudication

## Source Triple
- `exercises/exercise-03.tex`
- `assessment/exercises/exercise-03.md`
- `assessment/audit/exercises/exercise-03.md`

## Final Ruling
`REVISE`

## Confidence
High

## Why Keep/Revise/Replace
The first-pass assessment is mostly sound on the first three problems. It correctly describes this as the densest sheet so far and accurately identifies the main instructional moves: explicit electric/magnetic anomaly comparison in Problem 1, mass deformation and Higgsing logic in Problem 2, and `R`-charge bookkeeping in Problem 3. Its praise for the up-front quantum-number tables is source-grounded, and its concern that Problem 2 moves too quickly from the `F`-term condition to gauge-group reduction is also fair. The solution states `\langle q_6 \tilde q^6\rangle = -\mu m` and then immediately says this Higgses `SU(3)` to `SU(2)` without spelling out orientation or eaten modes (`437-460`).

This still needs revision because the first pass misses the most concrete reliability problem in the file: Problem 4's dimensional analysis visibly corrects itself mid-solution. The hint says the meson has dimension `[mass]` (`680-684`), the solution initially repeats that assignment (`763-766`), computes the superpotential term and gets `[mass]^2` instead of `[mass]^3` (`769-776`), then stops and changes the meson dimension to `[mass]^2` in order to recover the right answer (`781-818`). That is exactly the sort of source-level self-correction that should be called out explicitly in a final assessment.

There is also a smaller but real inconsistency in Problem 3: the background states the chiral-primary formula as `\Delta = 3|R|/2` (`496-500`), while the solution uses the standard `\Delta = 3R/2` relation without the absolute value (`589-617`). The first pass's current critique of under-scaffolding is fine, but it misses these sharper source-grounded issues.

## Minimum Changes Needed
Retain the existing comments on density, Problem 2 Higgsing, and Problem 3 scaffolding. Add an explicit concern that Problem 4 contains a wrong-start dimensional analysis that is then corrected in place, and note the smaller formula inconsistency in Problem 3's background.

## Notes For Final Summary
Exercise 3 is another `REVISE`: the first pass is broadly reliable, but it overlooks a worked-solution self-correction substantial enough to matter for final-use accuracy.
