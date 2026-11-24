# The simultaneous solution is unique up to scale and permutation

Section archived on 20 November 2026 from *Explaining alphaology*. [Original chapter](https://explaining-alphaology.al-rivero.chatgpt.site/shape/#both)

The chapter uses $K(m)=\sum_i m_i/(\sum_i\sqrt{m_i})^2$, the reciprocal of the $Q$ used in Lecture 11. For $q_i=\sqrt{m_i}>0$ let $s_1,s_2,s_3$ be the elementary symmetric polynomials in the $q_i$. Then $K(m)=1-2s_2/s_1^2$ and $K(1/m)=1-2s_1s_3/s_2^2$. At $K=2/3$ these give $s_2=s_1^2/6$ and $s_2^2=6s_1s_3$ respectively. [Definitions in the preceding section](https://explaining-alphaology.al-rivero.chatgpt.site/shape/#invariants)

Impose both equalities. Then $s_3=s_1^3/216$. With $t_i=6q_i/s_1$, the three normalized roots satisfy

$$
\sum t_i=6,\quad \sum_{i<j}t_it_j=6,\quad\prod t_i=1.
$$

Their polynomial therefore factorizes:

$$
t^3-6t^2+6t-1=(t-1)(t^2-5t+1).
$$

$$
\rho=\frac{5+\sqrt{21}}2,\qquad \{t_i\}=\{\rho^{-1},1,\rho\}.
$$

Thus, for positive masses, the necessary and sufficient condition is

$$
\boxed{\begin{gathered}K(m)=K(1/m)=\frac23\\\Longleftrightarrow\quad(m_1,m_2,m_3)\propto(\rho^{-2},1,\rho^2).\end{gathered}}
$$

Every positive simultaneous solution is a geometric progression. The converse follows by substitution, since $\rho+\rho^{-1}=5$. This becomes restrictive when a reciprocal seesaw is required to leave direct Koide on both physical sides.
