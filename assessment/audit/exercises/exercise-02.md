# Exercise 02 Audit

## Source Pair
`exercises/exercise-02.tex` and `assessment/exercises/exercise-02.md`

## Verdict
Partly accurate, but incomplete and too gentle about the source's larger conceptual mixing.

## What The Assessment Gets Right
The assessment correctly describes the sheet's overall progression. The source does move from one-loop asymptotic freedom, to the two-loop Banks-Zaks fixed point, to the exact supersymmetric conformal window, and then to a synthesis problem. It is also right that Problem 2 is one of the strongest units: the TeX has students derive the fixed point, compute it numerically for `N_f=16` and `N_f=15`, and compare reliability as the coupling grows. The critique of Problem 1's "factor of 4" explanation is fair as well. The source really does explain the fermion contribution in a hand-wavy way, using a mix of Dirac-degree-of-freedom counting and loop-factor language rather than a clean field-theory derivation.

## What It Misses Or Overstates
The assessment misses the most serious issue in the file: Problem 4 mixes SUSY and non-SUSY phase structure in a way that is stronger than "the final comparison section" suggests. In the source, the `SU(3)` phase diagram is presented for ordinary Dirac-flavor gauge theory, but one of its labeled regions is literally the "SUSY conformal window" at `N_f≈5–8`. The corresponding prose then describes that regime by switching back and forth between exact SUSY statements and uncertain non-SUSY estimates. That is a deeper structural problem than the assessment notes. The assessment also slightly misdescribes the lower-bound discussion in Problem 3: the source is explicitly about SQCD, not a general non-SUSY argument. Its real overstatement is different. It says below `3N_c/2` "the theory confines," whereas later Seiberg phases are more nuanced, including a free magnetic regime. So the file overstates the IR interpretation within SUSY, not merely by blurring rigorous and non-rigorous boundaries across SUSY versus non-SUSY.

## Recommended Revisions
Revise the assessment to call out the Problem 4 synthesis section directly. It should say that the source overlays exact SUSY window data onto a non-SUSY `SU(3)` phase diagram, which risks students reading a supersymmetric result as if it were a phase region of ordinary QCD-like theory. It should also sharpen the Problem 3 critique: the issue is not that the sheet treats a standard SUSY argument as a non-SUSY proof, but that it compresses the rich IR structure below `3N_c/2` into the single word "confines." The comments on Problem 1 and Problem 2 can remain, but they should be demoted behind those more substantive conceptual problems.
