# Which parts of a composite lepton spectrum need a colour dual?

Fix the electric charges. At a common matching scale compare the three singular values of the charged-lepton mass matrix, the residue with which a candidate operator creates a state, and the normalization of the photon current. A quark bilinear, an open string with labelled ends, and a map between finite Dirac modules can have the same charges. Each construction still needs an operator and kinetic terms to calculate those quantities.

## What the two ends determine

For an oriented Chan–Paton state $E_{ij}:V_j\to V_i$, a diagonal charge acts by $[Q,E_{ij}]=(q_i-q_j)E_{ij}$. The colour-singlet meson $Q^i\widetilde Q_j$ has this same vector charge. The degree-three lepton multiplicity in the finite geometry can be assigned to the down-flavour index of the charge $-1$ block. Its conjugate is $\operatorname{Hom}(\mathbb C^3_d,\mathbb C^2_u)$ of charge $+1$. The assignments match electric charges. Spin, chirality and the action of weak isospin require separate checks. In particular, a complex meson Weyl field for each entry of the traceless adjoint contains twice the left-Weyl content of three chiral lepton generations with right-handed neutrinos. [Five-flavour decomposition in conneskk](https://github.com/arivero/conneskk/blob/a465d42f2cf8c9b74244f135b759a2e5957c2a2a/results/52_three_lepton_generations_and_flavour_adjoint.md) · [Rivero's composite and string-end proposal, §§III–V](https://arxiv.org/abs/2407.05397)

For a straight string between parallel branes, the mode mass obeys $M^2=(L/2\pi\alpha')^2+(N-a)/\alpha'$, with separation $L$, oscillator level $N$ and intercept $a$. At $N=a$ its **mass** is linear in $L$. Koide's composite ansatz puts the square in the **fermion mass**, $m_i=m_\star(z_0+z_i)^2$. Lecture 11 obtains the same square with $x_i=\mu_{0i}/M_i$ and $m_\star=yv/\sqrt2$ in the diagonal dormant-doublet model. Identifying the string separation, a preon amplitude and this Higgs mixing ratio requires an interaction or a matching rule. In the parallel QCD-string study of an Abelian Higgs vortex, two worldsheet poles can have the same frequency while their polarizations and residues distinguish the excitations. [Open-string spectrum, Eq. (2.17)](https://arxiv.org/pdf/hep-th/9602052#page=14) · [Koide's fermion–boson composite model](https://doi.org/10.1016/0370-2693(83)90644-5) · [Charged-lepton mass relation](https://doi.org/10.1103/PhysRevD.28.252) · [QCD-string pole and polarization calculation](https://github.com/arivero/qcdstring/blob/766b845505f8c181ee09a77a12794732584a9984/outputs/1991-vortex-pseudoscalar/README.md)

## A rank obstruction and a deformation that bypasses it

Identify the left and right charged-lepton family spaces and assume the positive mass matrix in this basis is $M_\ell=m_\star A^\dagger A$, with $m_\star>0$ and a single dimensionless transition matrix $A:\mathbb C^3_d\to\mathbb C^2_u$. This is a factorization hypothesis. Rank at most two then gives a massless lepton, even after invertible wave-function normalizations. With several independent intermediate amplitudes the hypothesis becomes $M_\ell=m_\star\sum_s A_s^\dagger A_s$. Its kernel is exactly $\bigcap_s\ker A_s$, since its quadratic form is a sum of squared norms. Two maps already suffice for a positive spectrum. The contractions carry zero charge and are compatible with unbroken electromagnetism.

The massive five-flavour dual gives a concrete check on which matrix is involved. With generic diagonal, nonzero electric masses the charged meson Hessian has coefficients $h_{\alpha j}=m_\alpha m_j/S$, where $S^3=\Lambda^4\det m$. This $2\times3$ array has rank one. Each entry pairs a positive-charge meson $M^\alpha{}_j$ with an independent opposite-charge meson $M^j{}_\alpha$, so the mass map between the two six-dimensional charged spaces has rank six. For diagonal kinetic terms put $w_{\alpha j}=\sqrt{Z_{\alpha j}Z_{j\alpha}}>0$. The canonically normalized quadratic masses $p_{\alpha j}=|h_{\alpha j}|/w_{\alpha j}$ obey

$$
\frac{p_{uj}p_{ck}}{p_{uk}p_{cj}}=
\frac{w_{uk}w_{cj}}{w_{uj}w_{ck}},\qquad j,k\in\{d,s,b\}.
$$

Two independent double ratios equal one precisely when the six kinetic weights factorize into an up weight times a down weight. The holomorphic superpotential permits other weights. Flavour-resolved pole masses would test this factorization where the quadratic effective action describes the poles. Identifying a three-family lepton operator inside these six pairs still requires a map. [Charged-meson Hessian and its kinetic terms in conneskk](https://github.com/arivero/conneskk/blob/951671a1601215e1e9b93b9647907c77ed79ba98/results/issues/14.md) · [Intriligator and Seiberg, §§5.4–5.5](https://arxiv.org/pdf/hep-th/9509066)

There is also a test using operator residues. Take the charge-one scalar source $O_{\alpha i}=\bar d_i u_\alpha$, project to zero spatial momentum and treat electromagnetism as a global charge. Its Euclidean matrix $C_{ij}(\tau)=\sum_\alpha\langle O_{\alpha i}^\dagger(\tau)O_{\alpha j}(0)\rangle$ has spectral terms $e^{-E_n\tau}A_n^\dagger A_n$ with $(A_n)_{\alpha i}=\langle n|O_{\alpha i}|0\rangle$ in unit-normalized finite-volume states. Each independent state counts, including degeneracies. A sum over states may have rank three even with only two up labels. The residues can be compared across a proposed duality once the operator normalizations are matched. Identifying a weighted sum of those residues with $M_\ell$ is an additional physical prediction. The masses extracted from the decay of $C$ are those of the scalar states.

The nonzero electron mass supplies a more selective test. For ordered positive masses set $a=\sqrt{m_e/m_\mu}$, $b=\sqrt{m_\tau/m_\mu}$. In the convention of Lecture 11, $Q=(1+a+b)^2/(1+a^2+b^2)$. Solving $Q=3/2$ on the ordered branch gives

$$
b(a)=2(1+a)+\sqrt{3(1+4a+a^2)},\qquad
b(0)=2+\sqrt3,\qquad b'(0^+)=2+2\sqrt3 .
$$

Start at this rank-two point with distinct heavy masses. Keep $A_1$ fixed and turn on $A_2=\epsilon B$, with $Bn\ne0$ for a unit null vector $n$ of $A_1$. Perturbation of the simple zero eigenvalue gives $m_e/m_\star=\epsilon^2\|Bn\|^2+O(\epsilon^4)$ for real $\epsilon$. The two heavy masses change only at $O(\epsilon^2)$. Thus $a=O(|\epsilon|)$ and $db/da=0$ at onset. This particular way of lifting the electron leaves the Koide relation at first order in $a$. A mechanism that keeps the relation must also change the heavy ratio at first order.

A smooth one-sided counterexample is explicit. For $\epsilon\geq0$ take $A_1$ to have rows $(0,1,0)$ and $(0,0,b(\epsilon))$, and take $A_2$ to have rows $(\epsilon,0,0)$ and zero. Then $M_\ell/m_\star=\operatorname{diag}(\epsilon^2,1,b(\epsilon)^2)$, which obeys Koide throughout the ordered branch near zero. The construction puts in the heavy response. An independently computed response is what would distinguish a composite model from a fit.

## Realizing the square on a geometric family space

On the degree-three elliptic zero-mode space of conneskk, a magnetic translation $U$ has eigenvalues $1,\omega,\omega^2$ with $\omega^3=1$, $\omega\ne1$. Define a dimensionless Hermitian family matrix $X=sI+cU+\bar c U^\dagger$, with $s>0$. Its eigenvalues are $x_g=s+2|c|\cos(\arg c+2\pi g/3)$. Choose the positive-root arc. For $M_\ell=m_\star X^2$ one gets

$$
Q=\frac{(\operatorname{tr}X)^2}{\operatorname{tr}X^2}
=\frac{9s^2}{3s^2+6|c|^2},\qquad
Q=\frac32\ \Longleftrightarrow\ 2|c|^2=s^2 .
$$

In the preon notation, $z_0=s$, $z_g=x_g-s$, and $\sum_g z_g=0$. The condition $\sum_g z_g^2=3z_0^2$ is exactly the norm relation above. At fixed norm ratio take $\arg c=\pi/12-\epsilon$ with $\epsilon>0$ small. The light amplitude is $s(1-\cos\epsilon+\sin\epsilon)=s\epsilon+O(\epsilon^2)$. The heavy amplitudes start at $s(3\mp\sqrt3)/2$ and change linearly, giving the correlated response above.

Flux supplies the three modes. The Fourier coefficient and its phase are independent inputs in the geometric construction. Preserving both magnetic translations on an irreducible triplet would force a scalar mass matrix by Schur's lemma. The second translation must be broken for distinct masses. A geometric calculation could start from an independently specified Hermitian Yukawa profile $\mathcal Y$ on the elliptic curve and evaluate $X_{gh}=\langle\psi_g,\mathcal Y\psi_h\rangle$ on its orthonormal zero modes. For a profile preserving $U$, the resulting matrix commutes with $U$ and its three eigenvalues determine $s$ and $c$. The norm and phase can then be checked before fitting lepton masses. The parallel Koide literature supplies specific potentials that impose a norm relation. Selecting the potential and matching its masses to lepton poles are further steps. [Degree-three zero modes and their operators](https://github.com/arivero/conneskk/blob/a465d42f2cf8c9b74244f135b759a2e5957c2a2a/results/issues/08.md) · [Koide's charged-lepton superpotential](https://arxiv.org/abs/0811.3470) · [Lecture 11, §§2–5](../lectures/lecture-11.pdf)

**Does the order of projection and squaring matter?** Let $P$ project onto the three elliptic zero modes. If the higher-dimensional mass law squares a smooth real scalar profile $\mathcal Y$ before projection, the reduced mass is proportional to $P\mathcal Y^2P$. The difference from the proposed $X^2$ is itself a sum over intermediate modes,

$$
P\mathcal Y^2P-(P\mathcal YP)^2
=\big[(1-P)\mathcal YP\big]^\dagger\big[(1-P)\mathcal YP\big].
$$

In this scalar model every nonzero smooth profile gives a positive definite $P\mathcal Y^2P$ on the triplet. For any nonzero holomorphic zero mode $\psi$, its quadratic form is $\int_E|\mathcal Y|^2|\psi|^2>0$. A nonzero profile is nonzero on an open set, and a holomorphic section that vanishes there vanishes identically. Thus a zero of the projected first moment $P\mathcal YP$ can coexist with three positive masses when the full profile is squared. [Alphaology on the projection identity](https://explaining-alphaology.al-rivero.chatgpt.site/geometry-duality/#compression) · [Elliptic zero modes](https://github.com/arivero/conneskk/blob/a465d42f2cf8c9b74244f135b759a2e5957c2a2a/results/issues/08.md)

There is no profile-independent lower bound on the light-to-heavy mass ratio in this smooth scalar class. Allow profiles that break the translation symmetry. Concentrate $|\mathcal Y|^2$ in shrinking neighbourhoods of two distinct points $p,q$, keeping a fixed positive integral near each. The limiting quadratic form is a positive weighted sum of $|\psi(p)|^2$ and $|\psi(q)|^2$. Its kernel is $H^0(E,L(-p-q))$, which has dimension one by Riemann–Roch since $L(-p-q)$ has degree one. Two masses stay positive while the lightest tends to zero. Exact masslessness at a smooth profile and a parametrically small mass are different predictions in this example.

An interaction with only three intermediate states realizes the other order. Add three heavy vectorlike charged-lepton singlets with common mass $M$ and canonical kinetic terms. Let a Higgs Yukawa mixing after symmetry breaking be $h_L X$ and a singlet mass mixing be $h_R X^\dagger$, where $h_L,h_R$ have mass dimension one. Assume a vanishing direct light Yukawa. The Schur complement of the heavy block gives $-h_Lh_R XX^\dagger/M$. Its singular values are proportional to $x_g^2$ to leading order in $|h_{L,R}x_g|/M$. This example uses only electroweak interactions and the assigned mixings. The alignment of the two mixings is a physical assumption. The exact tree-level light and heavy singular values $m_{g,-},m_{g,+}$ of each $2\times2$ block give a further test. Its determinant and squared norm imply

$$
m_{g,+}^2+m_{g,-}^2
=M^2+\frac{|h_L|^2+|h_R|^2}{|h_Lh_R|}\,m_{g,+}m_{g,-}.
$$

All three pairs must lie on one line with slope at least two. This relation tests the common mediator mass and aligned mixing strengths if the heavy states are accessible. The magnetic theory would add predictive content if its normalized amplitudes fixed the alignments, residues or phase independently. [Koide and Fusaoka on universal seesaw mass matrices](https://arxiv.org/abs/hep-ph/0209148) · [Alphaology on finite-mixing corrections](https://explaining-alphaology.al-rivero.chatgpt.site/seesaw/)

### Finite mixing: the exact Koide shift and the reconstructed mediator mass

The line test above uses the exact singular values. The same block also fixes the sign of the finite-mixing correction to a seed relation, and at fixed mixing asymmetry it inverts. The hypotheses are those of the preceding paragraph: one common matching scale, canonical kinetic terms, a vanishing direct light Yukawa, a common vectorlike mass $M>0$ and aligned mixings $h_LX$, $h_RX^\dagger$. After a singular-value decomposition of $X$ and phase redefinitions each family carries the block

$$
\mathcal M_i=\begin{pmatrix}0&u\,x_i\\ v\,x_i&M\end{pmatrix},\qquad
u=|h_L|,\quad v=|h_R|,\quad x_i>0,\qquad
b=uv,\quad \kappa=\frac{u^2+v^2}{uv}\ge2 .
$$

Its light and heavy singular values $m_i<H_i$ are tree-level masses at the common matching scale. Comparison with pole masses needs the finite and radiative corrections of the completed model, and the lepton paragraph below makes that step explicitly. Throughout, $\mathcal Q(z)=(\sum_i\sqrt{z_i})^2/\sum_iz_i$, so $\mathcal Q(x^2)=(\sum x_i)^2/\sum x_i^2$ is the seed value and $\mathcal Q(m)$ the Koide ratio of the light masses.

**Singular values.** With $t=x_i^2$ the invariants of $\mathcal M_i$ are $|\det\mathcal M_i|=H_im_i=uvt$ and $\|\mathcal M_i\|_F^2=H_i^2+m_i^2=M^2+(u^2+v^2)t$. Hence $(H_i\pm m_i)^2=M^2+(u\pm v)^2t$, and

$$
m_i=F(t)=\frac{\sqrt{M^2+(u+v)^2t}-\sqrt{M^2+(u-v)^2t}}2
=\frac{2uv\,t}{\sqrt{M^2+(u+v)^2t}+\sqrt{M^2+(u-v)^2t}},\qquad
H_i=\frac{uv\,t}{m_i}.
$$

Direct diagonalization gives the same values:

$$
\mathcal M_i\mathcal M_i^\dagger=\begin{pmatrix}u^2t&uMx_i\\ uMx_i&v^2t+M^2\end{pmatrix}
$$

has trace $M^2+(u^2+v^2)t$ and determinant $u^2v^2t^2$, and its eigenvalues are $m_i^2$ and $H_i^2$. The rationalized form is the one to evaluate numerically, since the difference of square roots cancels for $m_i\ll H_i$. $F$ is strictly increasing, $F(t)/t$ is strictly decreasing, and $F(t)/\sqrt t=2uv/\big(\sqrt{M^2/t+(u+v)^2}+\sqrt{M^2/t+(u-v)^2}\big)$ is strictly increasing.

**Lemma.** Let $t_1\ge t_2\ge t_3>0$, not all equal, and let $\phi$ be positive and increasing on these values with $\phi(t)/t$ strictly decreasing on them. Then the normalized vector $\phi(t)/\sum\phi(t)$ is majorized by $t/\sum t$, with strict inequality in at least one partial sum. Indeed, the ratios $r_i=\phi(t_i)/t_i$ are nondecreasing in $i$ and not all equal, so for $k=1,2$ the weighted average of $r_i$ with weights $t_i$ over the $k$ largest entries is at most its weighted average over all three, which is the partial-sum inequality $\sum_{i\le k}\phi(t_i)/\sum_i\phi(t_i)\le\sum_{i\le k}t_i/\sum_it_i$. Since $\sqrt p$ and $-p^2$ are strictly concave, $\sum_i\sqrt{p_i}$ and $-\sum_ip_i^2$ are strictly Schur-concave on the probability simplex, so $\mathcal Q(\phi(t))>\mathcal Q(t)$ and $\mathcal Q(\phi(t)^2)>\mathcal Q(t^2)$.

**Proposition 1 (forward shift).** For every finite $M,u,v>0$ and seeds $x_i>0$ that are not all equal,

$$
\boxed{\ \mathcal Q(m^2)<\mathcal Q(x^2)<\mathcal Q(m)<\mathcal Q(x)\ }
$$

The middle inequality is the lemma with $\phi=F$ on $t_i=x_i^2$. The outer two are the lemma applied to $x$ as a function of $m$, since $x_i/m_i=\sqrt{t_i}/F(t_i)$ decreases as $m_i$ grows. Strictness requires only that the seeds are not all equal: two equal seeds still shift, and $x=(1,1,3)$ with $(u,v,M)=(1,2,5)$ gives $\mathcal Q(x^2)=2.2727$ and $\mathcal Q(m)=2.4666$. Equal seeds give the value $3$ throughout. As $M\to\infty$ at fixed mixings, $m_i\to uvx_i^2/M$ and $\mathcal Q(m)\to\mathcal Q(x^2)$, the leading seesaw value. As $M\to0$, $m_i\to\min(u,v)\,x_i$, so $\mathcal Q(m)\to\mathcal Q(x)$ and $\mathcal Q(m^2)\to\mathcal Q(x^2)$. The result holds to all orders in $ux_i/M$ and $vx_i/M$ for this finite mass matrix: a seed with $\mathcal Q(x^2)=3/2$ and unequal entries produces $\mathcal Q(m)>3/2$ at every finite mediator mass.

**Heavy branch.** The line relation $H_i^2-\kappa m_iH_i+m_i^2-M^2=0$ has the roots $H_\pm=\big(\kappa m_i\pm\sqrt{4M^2+(\kappa^2-4)m_i^2}\big)/2$. Both are positive when $m_i>M$, which occurs in this model: $u=v=M=1$ and $x=5$ give $m=4.52$. The selection rule is $H_-<m_i<H_+$ for every $M>0$. The left inequality reduces to $-4(\kappa-2)m_i^2<4M^2$, the right one to $(2-\kappa)m_i<\sqrt{4M^2+(\kappa^2-4)m_i^2}$, and both hold for $\kappa\ge2$. Moreover $H_i>m_i$ because $(H_i^2-m_i^2)^2=(M^2+(u^2+v^2)t)^2-4u^2v^2t^2>0$. The heavy mass is therefore $H_i=H_+(m_i,M,\kappa)$.

**Proposition 2 (reconstruction at fixed $\kappa$).** Let the light masses $m_i>0$ be not all equal and fix $\kappa\ge2$. Put $T_i(M)=m_iH_+(m_i,M,\kappa)$, which equals $b\,x_i^2$, and $G_\kappa(M)=\mathcal Q(T_1,T_2,T_3)$. A seed value $q_\star$ is realized by exactly one finite $M>0$ if and only if

$$
\boxed{\ \mathcal Q(m^2)<q_\star<\mathcal Q(m)\ }
$$

The window depends on the light masses alone and is the same for every $\kappa$. The proof has three steps. (i) With $S_i=\sqrt{4M^2+(\kappa^2-4)m_i^2}$, $M\,\partial_M\log T_i=4M^2/[S_i(\kappa m_i+S_i)]=g_\kappa(m_i/M)$, where

$$
g_\kappa(z)=\frac4{\sqrt{4+(\kappa^2-4)z^2}\,\big[\kappa z+\sqrt{4+(\kappa^2-4)z^2}\big]}
$$

has a denominator strictly increasing in $z>0$, including $\kappa=2$. For $M_1<M_2$ the ratio $T_i(M_2)/T_i(M_1)=\exp\int_{M_1}^{M_2}g_\kappa(m_i/M)\,dM/M$ therefore decreases strictly as $m_i$ grows, while $T_i$ itself increases with $m_i$. The lemma gives $G_\kappa(M_2)>G_\kappa(M_1)$, so $G_\kappa$ is continuous and strictly increasing. (ii) As $M\to0^+$, $H_+\to\rho m_i$ with $\rho=(\kappa+\sqrt{\kappa^2-4})/2$, so $G_\kappa\to\mathcal Q(m^2)$. As $M\to\infty$, $H_+/M\to1$ and $G_\kappa\to\mathcal Q(m)$. Both limits are approached and never attained, which with (i) and the intermediate-value theorem gives existence and uniqueness inside the open window and no solution outside it. (iii) Conversely, a solution $M$ and any $b>0$ give an explicit aligned matrix: $u=\sqrt{b\rho}$, $v=\sqrt{b/\rho}$ and $x_i=\sqrt{T_i/b}$ satisfy $uv=b$, $(u^2+v^2)/(uv)=\kappa$, $|\det\mathcal M_i|=m_iH_i$ and $\|\mathcal M_i\|_F^2=M^2+\kappa m_iH_i=m_i^2+H_i^2$. The two invariants fix the two singular values, so the block reproduces $m_i$. The rescaling $b\mapsto cb$, $x_i^2\mapsto x_i^2/c$ leaves every mass unchanged. At $\kappa=2$ the heavy root simplifies to $H_i=M+m_i$ and $T_i=m_i(M+m_i)$. Proposition 1 is the forward reading of the same statement: its first two inequalities say that every finite $M$ lands inside the window.

**Near the seesaw limit.** For $M\gg\kappa\,m_{\max}$, $H_+=M+\kappa m_i/2+O(m_i^2/M)$, and with $S_p=\sum_im_i^p$

$$
G_\kappa(M)=\mathcal Q(m)\Big[1-\frac{\kappa}{2M}\Big(\frac{S_2}{S_1}-\frac{S_{3/2}}{S_{1/2}}\Big)+O\Big(\frac{\kappa^2m_{\max}^2}{M^2}\Big)\Big].
$$

The bracketed difference is positive for masses that are not all equal, by the ordering of the means $S_{p+1}/S_p$ in $p$. Inverting, $M\simeq\kappa\,\mathcal Q(m)\,(S_2/S_1-S_{3/2}/S_{1/2})/\big(2[\mathcal Q(m)-q_\star]\big)$ when $\mathcal Q(m)-q_\star$ is small and positive. This is the alphaology coefficient read in the light masses. In the forward direction $m_i=(uvx_i^2/M)(1-dx_i^2+\dots)$ with $d=(u^2+v^2)/(2M^2)$, and the source gives $\delta\ln K=-d\,(p_4/p_2-p_3/p_1)$, $p_n=\sum_ix_i^n$, for its $K=1/\mathcal Q$. Substituting $x_i^2\simeq Mm_i/b$ turns $d\,p_4/p_2$ into $(\kappa/2M)S_2/S_1$ and $d\,p_3/p_1$ into $(\kappa/2M)S_{3/2}/S_{1/2}$. The exact equation $G_\kappa(M)=q_\star$ defines $M$ outside this limit. [Alphaology, finite-mixing expansion](https://explaining-alphaology.al-rivero.chatgpt.site/seesaw/#quadratic)

**What stays free.** The light masses determine $M$ only once $\kappa$ is given, so they select a one-parameter family of completions labelled by $\kappa$, with $b$ unobservable. The seed value $q_\star$, the alignment of the two mixings and $\kappa$ are inputs. Deriving any of them, or a Koide-generating potential for the seed, is a separate problem. A direct light Yukawa, nonuniversal mediator masses, flavour-dependent kinetic terms or misaligned mixings change the block and need their own calculation.

**Charged leptons with $q_\star=3/2$.** The PDG 2024 pole masses $0.51099895$, $105.6583755$ and $1776.93\pm0.09$ MeV serve as placeholders. They give $\mathcal Q(m)=1.5000050$, $\mathcal Q(m^2)=1.119111$ and $S_2/S_1-S_{3/2}/S_{1/2}=252.87$ MeV. The exact root of $G_\kappa(M)=3/2$ is $M/\kappa=38.26$ TeV at the central $\tau$ mass, the same to four figures for $\kappa$ from 2 to 100, so $M=76.51$ TeV at $\kappa=2$. At $m_\tau-1\sigma$ it is $M/\kappa=11.57$ TeV. A root exists only for $m_\tau<1776.969$ MeV, and the central value lies $0.43\sigma$ below that threshold. With pole masses the model therefore gives a lower bound, $M/\kappa\gtrsim11.6$ TeV at one sigma, and no upper bound. The model's masses are running masses at the matching scale, however. The one-loop QED relation $m_i(\mu)=m_i^{\rm pole}\big[1-\tfrac{\alpha}{\pi}\big(1+\tfrac34\ln(\mu^2/m_i^2)\big)\big]$ gives $\mathcal Q=1.49740$ at $\mu=m_\tau$ and $1.49736$ at $\mu=M_Z$. That is $0.0026$ below $3/2$, about 240 times the pole-mass uncertainty of $\mathcal Q$, and the upper-endpoint test fails for $q_\star=3/2$ at a common scale. Finite mixing and the running-to-pole conversion both raise $\mathcal Q$. With Standard Model running below $M$ and flavour-universal thresholds, an exact $3/2$ seed in this aligned completion overshoots the pole value, and admissible common-scale seeds satisfy $q_\star\lesssim1.4974$. A cancelling correction of Sumino's type would have to come from another sector of the completed model. [Xing and Zhang on running lepton masses](https://arxiv.org/abs/hep-ph/0602134) · [Li and Ma on the scale dependence of Koide's relation](https://arxiv.org/abs/hep-ph/0601031) · [Sumino's family gauge cancellation](https://arxiv.org/abs/0812.2103) · [Lecture 11, scale convention](../lectures/lecture-11.pdf)

**Status.** The block algebra and the leading seesaw law are textbook universal-seesaw results, and the leading shift is already in the alphaology source. The all-orders sign, the heavy-branch rule and the inverse at fixed $\kappa$ with its $\kappa$-independent window are elementary consequences of the stated hypotheses. They are new as stated here, and their priority is open. The lepton application is conditional on the aligned completion and on the matching step. AI reviewers checked the derivation by hand and with `scripts/verify_finite_mixing_koide.py` in issue 3; independent review is pending. [Issue 3](https://github.com/arivero/dualsm/issues/3) · [Verification script](../scripts/verify_finite_mixing_koide.py)

### A correction to the parallel O'Raifeartaigh example

The sBootstrap manuscript obtains the rank-two Koide seed for $gv/m=\sqrt3$ in a rigid model. Its March version attributed a physical Goldstino mass to the superpotential deformation $\epsilon X B$. For $W=fX+mAB+gXA^2+\epsilon XB$ with canonical Kähler metric, stationarity requires $W_{ij}\overline{W_j}=0$. At the old seed $(X,A,B)=(v,0,0)$ this vector is $(\epsilon^2v,m\epsilon v,\epsilon f)$ for real parameters. For $\epsilon f\ne0$ the old background is no longer stationary. At any stationary vacuum with a nonzero $F$, the same equation protects a zero fermion mass eigenvalue. Breaking $R$ in the superpotential preserves rigid supersymmetry. For nonzero $f,m,g,\epsilon$ the three $F$ equations also admit the solutions

$$
A^2=-\frac{f}{3g},\qquad X=-\frac{mA}{\epsilon},\qquad
B=-\frac{2f}{3\epsilon}.
$$

These are supersymmetric vacua at large field values as $\epsilon\to0$. The rank construction above lifts a flavour zero through a second transition, and the explicitly correlated deformation follows the Koide branch. Identifying a flavour state with the Goldstino would also require the supersymmetry Ward identity at a stationary breaking vacuum. [March argument](https://github.com/arivero/physres2/blob/f2e137f/sbootstrap_v4d.tex) · [Corrected model and deformation](../related-papers/phys3_sbootstrap_v4d.tex) · [Intriligator and Seiberg on the Goldstino](https://arxiv.org/pdf/hep-ph/0702069#page=6) · [Nelson and Seiberg on R symmetry and supersymmetry breaking](https://arxiv.org/abs/hep-ph/9309299)

## How far the two issue results reach

- **Electromagnetic normalization.** The inverse-cube dependence in issue 1 varies an independent spectator hypercharge coupling at fixed strong masses and weak VEV. The projective-product model in conneskk correlates those inputs. At fixed matched radii, parent couplings and Higgs amplitude, its interval length $\ell$ gives $g_i^2\propto\ell^{-1}$ and $v^2\propto\ell$. The leading charged and neutral weak masses stay fixed. The compressed lepton mass $|y_{11}|\nu_{11}/\sqrt2$ also stays fixed. With three copies and fixed Yukawas this gives $A_\ell/[\alpha_{\rm match}\sqrt{M_Z^2-M_W^2}]\propto\ell$, with $A_\ell=\sum m_i/6$. This is a different response with a remaining continuous parameter. A length selected by the action and a threshold calculation down to the Thomson charge could turn that comparison into a prediction. The calculation applies in the tree-level window below the compactification gaps. [Five-flavour coupling variation](paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md) · [Projective-product normalization, §8](https://github.com/arivero/conneskk/blob/a465d42f2cf8c9b74244f135b759a2e5957c2a2a/results/issues/01.md#colour-the-finite-real-module-and-matching-on-one-product)
- **Local supersymmetry.** In eight-flavour quark-and-gluon QCD the Euler anomaly excludes the full same-colour SQCD endpoint. A change of interpolating operator cannot alter either endpoint anomaly. The current obstruction has other precise hypotheses. Even allowing $\mathcal N$ same-chirality supercharges, unbroken $SU(8)_V$ must act on their multiplicity space. For $1\leq\mathcal N<8$ every homomorphism $\mathfrak{su}(8)\to\mathfrak u(\mathcal N)$ is zero by simplicity and dimension. The connected group then acts trivially, in conflict with $-\mathbf1_8=(-1)^F$ on local currents. The argument works for every even $N_f$ with unbroken vector flavour and $1\leq\mathcal N<N_f$. Doubling the supercharges alone cannot evade the eight-flavour test. Adding colour-fundamental scalars $\phi_i$ with the same vector flavour action and baryon charge as the quarks permits the local neutral flavour-singlet fermion $\sum_i\phi_i^\dagger\psi_i$. The centre then acts trivially on a fermion, removing this obstruction. Establishing a conserved spin-$3/2$ current still needs a Ward identity. A composite lepton mass law by itself makes no supercurrent claim. [Paper 3, endpoint and current tests](paper-3-emergent-susy-lattice/SUMMARY.md#which-theories-can-support-a-supercurrent) · [Parallel study of the finite cubic operator identity](../related-papers/phys4_emergent_n2.tex)
