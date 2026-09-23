# Exercise 02 XHigh Assessment

Source: `exercises/exercise-02.tex`

## Scope
This sheet is structured as a progression from asymptotic-freedom bookkeeping to perturbative fixed points, then to the exact supersymmetric conformal window, and finally to a broad phase-diagram synthesis. That overall arc is sensible and mostly cumulative. Problems 1 and 2 are computational; Problem 3 shifts to exact supersymmetric statements; Problem 4 tries to connect those exact results to the looser non-supersymmetric phase-language that motivates later duality discussions. The file is strongest when it stays within a single regime of validity and weakest when it crosses regimes without marking the boundary clearly.

## Strengths
Problem 1 works well as a warm-up. The numerical survey for `SU(3)` makes the one-loop coefficient concrete and sets up the asymptotic-freedom boundary cleanly. Problem 2 is the best-contained exercise in the set: the prompt, derivation, and numerical examples for `N_f=16` and `N_f=15` line up well, and students can see directly why the Banks-Zaks fixed point becomes more trustworthy near `11N_c/2`.

Problem 3 is also pedagogically valuable because it explicitly distinguishes the supersymmetric case from the non-SUSY one and uses exact machinery: the NSVZ numerator for the upper boundary and the chiral-primary unitarity bound for the meson at the lower boundary. The table for `SU(2)`, `SU(3)`, and `SU(5)` is a useful synthesis checkpoint.

## Concerns
The most serious issue is Problem 4. The prompt says "For `SU(3)` with `N_f` Dirac fundamental flavours," which is non-supersymmetric language, but one of the plotted phase regions is literally labeled the "SUSY conformal window" for `N_f approx 5-8`. The source then alternates between exact SQCD statements and uncertain non-SUSY estimates on the same diagram. That is not just a soft comparison problem; it is a category error in the presentation. Any review that treats this as a minor final-section looseness misses the main structural defect of the file.

Problem 3 contains a second, more local overstatement. The derivation of the lower boundary from the meson unitarity bound is a standard exact SQCD argument, but the solution concludes that below `3N_c/2` "the theory confines." That compresses a more nuanced supersymmetric IR story into a single label. The prompt is reasonable; the solution oversimplifies the interpretation.

There are also smaller issues of exact versus heuristic language. Problem 1's explanation of the fermion `4/3` factor is heuristic rather than derivational, and Problem 2's "high" versus "marginal" reliability labels are sensible but not tied to an explicit criterion.

## Suggestions
Problem 4 should be rewritten so the reader never has to guess whether a statement is about SQCD or ordinary Dirac-flavor gauge theory. The cleanest repair is to split the synthesis into two parallel summaries: exact SQCD phases and non-SUSY conjectural phases. If the shared figure is kept, its axes and labels must say explicitly when a region is supersymmetric and when a boundary is only an estimate.

Problem 3 should replace "the theory confines" with a more careful statement that the electric conformal description fails below `3N_c/2` and that the IR is better described by the magnetic variables. Problem 1 and Problem 2 need only lighter edits: tighten the coefficient explanation and state an explicit perturbative-reliability yardstick.
