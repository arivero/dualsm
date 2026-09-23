# Exercise 01 Adjudication

## Source Triple
- `exercises/exercise-01.tex`
- `assessment/exercises/exercise-01.md`
- `assessment/audit/exercises/exercise-01.md`

## Final Ruling
`REVISE`

## Confidence
High

## Why Keep/Revise/Replace
The first-pass assessment is directionally useful, but it is not precise enough about the central defect in the sheet. It correctly identifies the broad arc of the exercise set: Standard Model anomaly cancellation in Problem 1, general `SU(N_c)` anomaly bookkeeping in Problem 3, and the chiral `SU(5)`-type example in Problem 4 are all described fairly. Its praise for Problem 1 is also well grounded: the source explicitly tells students to convert right-handed fermions to left-handed conjugates and then models the multiplicity counting carefully in the worked solution.

The reason this cannot be kept as-is is Problem 2. The first pass frames the issue as a pedagogical false start about nucleons, but the source problem is more concrete and more serious. The prompt itself asks students to compute `SU(2)_L^3` and `SU(2)_R^3` anomalies and even hints that the `SU(2)_L^3` anomaly is nonzero (`tex` lines 217-232). The worked solution then computes those cubic anomalies as `3` in the UV (`251-260`), later stops, admits the `SU(2)^3` anomaly vanishes for `SU(2)` because there is no cubic `d^{abc}` tensor, and redoes the real matching in terms of mixed anomalies (`344-458`). That is not merely a slightly confusing presentation choice; it is an internal correction of the mathematical target of the problem.

The first pass also overstates the need for extra multiplicity scaffolding in Problem 3. The source already gives a fairly explicit multiplicity hint and a transparent six-entry anomaly table, so that is secondary compared with the unresolved Problem 2 prompt/solution mismatch.

## Minimum Changes Needed
Revise the assessment so it says plainly that Problem 2 contains an explicit correction about `SU(2)^3` anomalies, and that the prompt itself needs tightening, not just the prose of the solution. Keep the positive comments on structure and on Problem 1. Demote the Problem 3 multiplicity suggestion to a minor note.

## Notes For Final Summary
Exercise 1 is a `REVISE`, not a `REPLACE`, because the first pass gets the overall pedagogical arc right. The decisive issue is a source-level prompt/solution inconsistency, not a total misread of the file.
