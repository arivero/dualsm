# Exercise 6 Assessment
Source: `exercises/exercise-06.tex`
Scope: content quality of the scale-matching exercise and its worked solution.

## Strengths
This is the cleanest "mechanism to scale" exercise in the set. The structure is easy to follow: one part on one-loop QCD running, one part on the duality-scale matching, one part on the electroweak seesaw relation, and a final synthesis table. The exercise does a good job giving students multiple entry points into the same idea, which is pedagogically sound for a topic that mixes RG flow, thresholds, and order-of-magnitude reasoning.

## Concerns
The biggest issue is that the stated numerical inputs and the worked solution do not agree. Part (b)(ii) explicitly tells the student to use $\alpha_s(\Lambda_D)=0.3$ at $\Lambda_D=10^{11}$ GeV, but the solution computes that this would give an absurdly large confinement scale, then silently replaces the input by an evolved value $\alpha_s(\Lambda_D)\approx 0.032$ obtained from $\alpha_s(M_Z)$. That is a legitimate physics move, but it is not what the prompt asked for. The result is that the student is taught to trust the narrative over the stated data.

The electroweak-scale estimate has a similar issue. Using the quoted $\Lambda_D=10^{11}$ GeV in $v\sim \Lambda_D^2/M_{Pl}$ gives roughly 820 GeV, not 246 GeV. The solution acknowledges this only after the fact and treats it as acceptable because of unspecified $O(1)$ factors. That is fine as a parametric check, but the exercise should say so more explicitly or choose an input scale that lands closer to the measured value.

The summary table at the end also blurs "input" and "derived" in a way that will confuse students. In one place $\alpha_s(\Lambda_D)$ is treated as an input from duality or running, while elsewhere the exercise frames it as something to be computed. Likewise, the relation between $\Lambda_S$ and the rest of the scales is asserted rather than derived.

## Suggestions
Make the exercise internally self-consistent by choosing one numerical route: either start from $\alpha_s(M_Z)$ and derive everything, or state that the numerical inputs are only approximate parametric anchors. If the point is parametric consistency, the text should say that clearly before the calculation begins.

The worked solution should not change the problem's input without flagging it. A short note such as "the stated $\alpha_s(\Lambda_D)=0.3$ is deliberately too large; we now recompute using RG evolution from $M_Z$" would make the logic transparent. Similarly, the electroweak-scale comparison should be framed as an $O(1)$ check, not as a near-fit.
