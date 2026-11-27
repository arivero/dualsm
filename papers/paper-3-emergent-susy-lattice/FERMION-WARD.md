# Fermion contacts and the supercurrent test

The target is a local supercurrent whose charge and conjugate translate a physical flavour-changing bilinear on the same continuum state as the stress tensor. Use the six-fundamental Wilson construction as a normalization control. Add one adjoint Weyl fermion, realized with a Wilson Majorana regulator. A positive result needs its own massless continuum limit. The eight-flavour scalar and mode-number tests remain separate.

## A contact that survives adding the adjoint

In lattice units add $\tfrac12\chi^{\mathsf T}\mathcal M(U)\chi$ to the six-flavour Wilson action, with $\mathcal M=C D_{\rm adj}$ antisymmetric in the combined spin, colour and site indices. Its Grassmann integral gives the Pfaffian with the chosen orientation. Tune the adjoint critical mass separately. The fundamental off-diagonal variation $\delta q=\alpha E_{12}q$, $\delta\bar q=-\bar q\alpha E_{12}$ has unit Berezin Jacobian and leaves the links and $\chi$ fixed. Let $B^L_A=\bar q A P_L q$, $T=(E_{11}-E_{22})/2$, and $Y=B^L_{21}(y)(B^L_T)^\dagger(z)$, where $21$ denotes $E_{21}$. Take $\alpha=1$ near $y$ and zero near $z$. Then
$$
 \delta Y=-2 B^L_T(y)(B^L_T)^\dagger(z),\qquad
 \langle D^V_{12}(\alpha)Y\rangle
 =(u_1-u_2)\langle S_{12}(\alpha)Y\rangle-\langle\delta Y\rangle .
$$
Here $u_i$ are the dimensionless bare masses, $D^V$ uses the point-split divergence from $-[D_W,\alpha]$, and $S_{12}=\bar q E_{12}q$. The first equality follows from $[E_{21},E_{12}]=-2T$. The second is Berezin integration by parts at fixed links, followed by the same normalized joint integral on both sides. At equality of the masses the integrated divergence reads twice the separated $B_T^L$ correlator. The identity holds with the full Pfaffian whenever the joint partition function is nonzero. An axial flavour variation retains the Wilson breaking insertion and spectator variation. [Finite Ward algebra](https://github.com/yang-mills-group/OpenAI-QCD-20261104/blob/53f81cafe5cb9cd18cd0d5b49b8364cce50a0fe7/proof/YM/Massive/PCAC/Bare.lean) · [November manuscript, §108.1](https://github.com/yang-mills-group/OpenAI-informal-20261115/blob/6ca21d98b4022263fd7f2a3de5b5913b8495ee02/continuum-yang-mills-theory.pdf)

## What changes for a spinor variation

For an infinitesimal even variation $\delta$ built with an odd spinor parameter, set $W_\delta=\delta S-\operatorname{sdiv}\delta$, using the Haar and Berezin measures. The exact identity is $\langle W_\delta Y\rangle=\langle\delta Y\rangle$. As a definite trial, vary a link by a left tangent proportional to $\alpha_x(\bar\zeta\gamma_\mu\chi^a(x))T^a U_{x\mu}$ and vary the adjoint spinor by a clover field strength times $\alpha_x\sigma^{\rho\sigma}\zeta$ with the matching colour index. Set $\delta q=\delta\bar q=0$. Choose the relative coefficients by the continuum pure supersymmetric Yang–Mills current convention. For this one-sided link prescription the coefficient is independent of its own link and the spinor shift is independent of $\chi$, hence the infinitesimal superdivergence vanishes. The clover and Wilson hopping terms still vary.

In particular the fundamental action gives the additional insertion
$$
 W_\delta^{q}=\sum_{x,\mu,a}\alpha_x(\bar\zeta\gamma_\mu\chi^a(x))
             \sum_{f=1}^6\bar q_f(\nabla^a_{x\mu}D_W)q_f ,
$$
with the coefficient of the link tangent set to one in lattice units. Here $\nabla^a$ differentiates under $U\mapsto e^{tT^a}U$. In canonical continuum normalization $D=\partial+gA$ the leading operator is the colour current times $g\gamma_\mu\chi^a$. It has dimension $9/2$ before multiplication by the spinor parameter. This term survives mass tuning at nonzero gauge coupling and is a fundamental-flavour singlet.

Keep the adjoint variables until after the variation. For a link-only variation independent of $\chi$ one may equivalently use $\delta\log\operatorname{Pf}\mathcal M=\tfrac12\operatorname{Tr}(\mathcal M^{-1}\delta\mathcal M)$ on invertible configurations. A spinor-dependent link variation requires inserted adjoint contractions. The joint Grassmann identity handles both. Continuum matching requires the mixing of vector-spinors, including $F_{\rho\sigma}\sigma^{\rho\sigma}\gamma_\mu\chi$ and $F_{\mu\nu}\gamma^\nu\chi$ with colour traced, a subtracted adjoint mass times the gluino–glue operator in the divergence, and control of the fundamental insertion and contacts. The pure-SYM calculation supplies an adjoint-sector reference. The six-flavour release supplies the spectator normalization method and the stress translation test. [Pure-SYM Wilson Ward analysis](https://arxiv.org/abs/hep-lat/0111008) · [Six-flavour current-normalization audit](https://github.com/yang-mills-group/QCD/blob/9b2971888b9d525431bdb398ae2cb3ac33bf28e5/docs/mass-current-normalization.md)

The next calculation normalizes the two ordered supercurrent fluxes on a gauge operator and tests the translation of $B^L_{12}$ with the same coefficients.

## Two ordered insertions and a second spectator

Use two odd parameters and the corresponding even changes of variables $\delta_1,\delta_2$. Strip the parameters in the same order at the end. Their test functions equal one near the field at $x$, with nested supports avoiding the spectator at $y$. Twice applying finite Haar–Berezin integration by parts gives
$$
 \big\langle Y(W_1W_2-\delta_1 W_2)\big\rangle
  =\langle (\delta_1Y) W_2\rangle
  =\langle\delta_2\delta_1Y\rangle .
$$
The other ordering interchanges 1 and 2. Taking the commutator of the even variations and extracting the ordered odd parameters gives the anticommutator of the odd generators with the chosen spinor convention. The contact $\delta_1 W_2$ is essential. The two terms in the left side use the full action, including the variation of the fundamental hopping and adjoint Pfaffian sector. At finite Wilson spacing this is an identity for the **complete variations**. Expressing it as two surface fluxes involves separating the mass and Wilson breaking terms, renormalizing the currents, and controlling collisions with the inner insertion. The release's stress-shell identity supplies a translation with independently fixed unit coefficient. [Translation on the same field system](https://github.com/yang-mills-group/OpenAI-QCD-20261104/blob/53f81cafe5cb9cd18cd0d5b49b8364cce50a0fe7/proof/YM/Massive/Target/Physics.lean) · [Current contact audit](https://github.com/yang-mills-group/QCD/blob/9b2971888b9d525431bdb398ae2cb3ac33bf28e5/docs/mass-current-normalization.md)

**An explicit normalization test.** Take the massless, free continuum limit of the trial on the product of a gauge–adjoint vector multiplet and six Dirac fundamentals. Normalize the supercharge on $O_g=\operatorname{tr}F_{\mu\nu}F_{\mu\nu}$. The linear vector-multiplet transformations close on $A_\mu$ as a translation plus a gauge transformation, so on the gauge-invariant $O_g$ the summed nested insertion gives $2\sigma^\mu\partial_{x^\mu}C_g(x-y)$ in the conventions of Paper 3, where $C_g=c_g/|x-y|^8$, $c_g>0$. Choose the two-point normalization once, including the conjugate charge, and use a spinor component with a nonzero translated correlator.

For $B=\bar q_1 P_L q_2$, put $r=x-y$. Both variations of $B$ vanish for this charge. The connected, vacuum-subtracted gauge–adjoint surface product also factorizes from the separated fundamental pair at zero coupling. The stress translation on the same bilinear is nonzero. With $S(r)=\gamma\cdot r/(2\pi^2|r|^4)$ and the conjugate insertion $\bar q_2 P_R q_1$,
$$
 C_B(r)=-N_c\,{\rm tr}[P_L S(r)P_R S(-r)]
       =\frac{N_c}{2\pi^4 |r|^6},\qquad
 2\sigma\cdot\partial C_B(r)=-\frac{6N_c}{\pi^4}
                         \frac{\sigma\cdot r}{|r|^8}.
$$
The ratios of the normalized nested response to the stress response are one on the gauge insertion and zero on the bilinear. A second external probe $\partial_{y^\nu}B^\dagger(y)$ gives the derivative of this mismatch, at separated points. Every current built solely out of the free vector multiplet acts in that factor. A common finite change of its two mixing coefficients cannot supply the missing translation of the quark factor. In algebraic terms this charge squares to the gauge–adjoint momentum in the decoupled model, while the total momentum also contains the Dirac stress.

At nonzero coupling the bare action still gives zero for the **compensated** nested variation of $B$ since the trial leaves $q,\bar q$ fixed. A surface-current product alone now has contributions from the breaking insertions; its value cannot be inferred by setting the right side of the compensated identity to zero. The dimension-$9/2$ term displayed above is the first explicit matter contribution to follow. The test for an emergent current remains its infrared projection, measured on both operators with a common normalization. The next calculation is to project this breaking insertion on an independent quark–adjoint probe, fixing its free short-distance normalization before using it in the interacting Ward system. No interacting eight-flavour exponent has been determined by this test.

## A nonzero projection of the fundamental breaking insertion

Take the coefficient of the spinor parameter in the fundamental term alone. Use Hermitian colour generators with $\mathrm{tr}(T^aT^b)=T_F\delta^{ab}$, $T_F=1/2$, and absorb the phase from the link tangent into this definition. For flavour weights $v$ define the gauge-invariant spinor
$$
 \mathcal O_v=\sum_f v_f\,(\gamma_\mu\chi^a)\,\bar q_f\gamma_\mu T^a q_f .
$$
The leading continuum term of the bare variation is $g\mathcal O_{\bf1}$ in canonical gauge normalization. Use separated points and four-component Majorana notation, pairing $\chi$ with $\bar\chi$. The conjugate ordering is $\bar\chi^a\gamma_\nu j_\nu^a$ with the same Euclidean current convention. A Weyl component follows by chiral projection.

**Short-distance control.** Put $n=x/|x|$. At tree level a single Dirac flavour gives
$$
 -{\rm tr}[\gamma_\mu S(x)\gamma_\nu S(-x)]\,{\rm tr}(T^aT^b)
 =\frac{T_F\delta^{ab}}{\pi^4 |x|^6}(2n_\mu n_\nu-\delta_{\mu\nu}).
$$
The fermion loop and $S(-x)=-S(x)$ fix the signs. Contract the remaining adjoint field with $S(x)=\not n/(2\pi^2|x|^3)$. The term $2n_\mu n_\nu$ gives $2\not n$ between the two gamma matrices, and $-\sum_\mu\gamma_\mu\not n\gamma_\mu$ gives another $2\not n$. Thus
$$
 \langle\mathcal O_v(x)\overline{\mathcal O}_w(0)\rangle_0
 =\frac{2T_F(N_c^2-1)}{\pi^6 |x|^9}
       \left(\sum_f v_f\overline w_f\right)\not n.
$$
There is one open gluino propagator. Its contraction carries no closed Majorana-loop factor. At six flavours and three colours the singlet coefficient is **48**. This fixes a nonvanishing denominator for a separated projection in the free reference. The method follows the release's use of free Wick labels and an independent detector in the same symmetry channel. The adjoint contraction belongs to the six-plus-adjoint trial. [Release Wick interface](https://github.com/yang-mills-group/OpenAI-QCD-20261104/blob/53f81cafe5cb9cd18cd0d5b49b8364cce50a0fe7/proof/YM/Massive/Target/Wick.lean) · [Part VI, §§106 and 109](https://github.com/yang-mills-group/OpenAI-informal-20261115/blob/6ca21d98b4022263fd7f2a3de5b5913b8495ee02/continuum-yang-mills-theory.pdf)

At fixed physical separation divide $\mathrm{tr}[\not n\langle X(x)\overline{\mathcal O}_{\bf1}(0)\rangle]$ by the same expression with $X=\mathcal O_{\bf1}$. At leading order this returns $g$ for the isolated fundamental variation. For traceless $w$ the mixed singlet–$\mathcal O_w$ projection vanishes on a flavour-symmetric ensemble. Permutation invariance makes the matrix of diagonal-flavour correlations $A(r)\delta_{fg}+B(r)$, so singlet and traceless weights are orthogonal even with a disconnected term. One traceless self-correlation and one singlet self-correlation resolve the two functions.

At nonzero coupling use independent source normalization for $\mathcal O$, the full current divergence, and the gluino mass insertion. A gauge-equation insertion can acquire the same matter projection, so one singlet matrix element alone cannot determine all mixing coefficients. The next input is the continuum-extrapolated mixed correlation matrix and the two nested contacts on the **same** mass-tuned six-plus-adjoint ensemble. The local release supplies no such adjoint-ensemble readings. This ultraviolet coefficient and the nonsinglet null test leave the infrared supercharge open.
