# Exercise 06 XHigh Assessment
Source: `exercises/exercise-06.tex`
Scope: Content assessment of the scale-matching exercise and its worked solution, focusing on whether the prompt, numerical inputs, and physical interpretation remain aligned.

## Strengths
This is a well-organised exercise set. The source separates standard textbook ingredients from conjectural duality input more clearly than most of the surrounding material: one-loop QCD running is presented as ordinary field theory, while the interpretation of $\alpha_s(\Lambda_D)$ and the meaning of the duality scale are explicitly marked as contingent on the duality picture. Parts 1(a) and 1(c)(i),(iv) are especially solid. The derivation of
$\Lambda_{\text{QCD}} = \mu_0 \exp[-2\pi/(b_0\alpha_s(\mu_0))]$
from the one-loop running formula is exact within the stated approximation, and the dimensional checks are appropriate and correctly placed. The seesaw-style scaling
$v \sim \Lambda_D^2/M_{\text{Pl}}$
is also presented honestly as an order-of-magnitude relation once the $\mathcal{O}(1)$ factors $\xi$ and $\lambda$ are acknowledged.

Pedagogically, the file has a useful ambition: a single exercise ties together running couplings, threshold intuition, and the input/output logic of the dualised SM. The final discussion question about prediction versus parametric consistency check is the right question for this material.

## Concerns
The most serious defect is a direct prompt-solution contradiction in 1(b)(i). The question tells the student to compute the electric one-loop coefficient and "argue that the electric theory is not asymptotically free (or marginally so)." But inserting the stated field content gives $b_0^e = 4 > 0$, and the solution correctly concludes the opposite: the electric theory is asymptotically free and therefore grows strong in the infrared. This is not a small wording issue. It reverses the conceptual claim being tested.

Part 1(b)(ii) then changes the numerical input midstream. The prompt explicitly says to use
$\alpha_s(\Lambda_D) = 0.3$,
$\Lambda_D = 10^{11}\,\text{GeV}$,
and
$b_0 = 7$.
That exact input gives
$\Lambda_{\text{QCD}} \approx 5\times 10^9\,\text{GeV}$,
which the solution computes. Instead of treating that as the answer to the stated problem, the solution replaces the input by an RG-evolved value
$\alpha_s(\Lambda_D)\approx 0.032$
derived from $\alpha_s(M_Z)$. That produces a more plausible
$\Lambda_{\text{QCD}} \approx 70\,\text{MeV}$,
but it is no longer the problem the student was asked to solve. The summary table makes the same substitution permanent by silently rewriting the input from $\sim 0.3$ to $\sim 0.03$.

The electroweak-scale part has a milder version of the same issue. With the stated
$\Lambda_D = 10^{11}\,\text{GeV}$,
the relation
$v \sim \Lambda_D^2/M_{\text{Pl}}$
gives about $820\,\text{GeV}$, not $246\,\text{GeV}$. The solution correctly says this is acceptable only at the level of an $\mathcal{O}(1)$ parametric check, but the problem statement and end summary sometimes speak as if the observed Fermi scale has been derived more sharply than that.

## Suggestions
Repair the file by choosing one numerical route and keeping it fixed. If the intent is to test the stated input $\alpha_s(\Lambda_D)=0.3$, then the exercise should let the absurd result stand and ask students what it means. If the intent is to obtain a realistic $\Lambda_{\text{QCD}}$, then the prompt should start from $\alpha_s(M_Z)$ or directly from $\alpha_s(\Lambda_D)\approx 0.03$ and say so explicitly.

Problem 1(b)(i) should also be corrected so the wording matches the actual sign of $b_0^e$. More broadly, the source should label exact one-loop formulas as exact within approximation, and label the numerical matches for $v$, $\Lambda_{\text{QCD}}$, and $\Lambda_S$ as heuristic or parametric outcomes. The material works well as a consistency-check exercise; it becomes misleading only when it changes inputs or overstates precision.
