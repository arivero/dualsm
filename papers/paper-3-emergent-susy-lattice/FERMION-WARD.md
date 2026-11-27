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
