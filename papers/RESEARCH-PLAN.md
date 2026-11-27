# Four Research Papers from the Dualised SM Lectures

When an obstruction arises, record which observable it concerns, which assumptions the proof uses, and what happens in a model that changes one of them. Closing a calculation settles the stated case. The broader mechanism can be revisited when a new field, vacuum, operator map or independently fixed coefficient changes its premises.

The open-string endpoint labels, geometric flavour triplet and Koide mass matrix now have a common test. At a zero-electron-mass boundary, a Koide-preserving deformation must change the heavy mass ratio at first order in $\sqrt{m_e/m_\mu}$. A second independent endpoint amplitude with the first held fixed gives zero slope. On the elliptic triplet, squaring a smooth scalar Yukawa profile before projection gives three positive masses and still permits an arbitrarily light electron. The open question is which intermediate states and normalized amplitudes the magnetic theory or the geometry actually produces. [Composite flavour matching and the two issue results](COMPOSITE-FLAVOUR-MATCHING.md) The common-mediator realization of the square now has an exact finite-mixing result. Every finite mediator mass raises the Koide ratio above an unequal seed, and at fixed mixing asymmetry the light masses fix the mediator mass uniquely inside the window $\mathcal Q(m^2)<q_\star<\mathcal Q(m)$. For charged leptons an exact $3/2$ seed at a common scale overshoots, so the scale question of Lecture 11 moves to the sector that completes the model. [Finite-mixing shift and reconstruction](COMPOSITE-FLAVOUR-MATCHING.md#finite-mixing-the-exact-koide-shift-and-the-reconstructed-mediator-mass)

## Paper 1: Sp(1) Seiberg Duality as an Alternative UV Completion of the Electroweak Sector

**Theme:** From Lecture 9 (SUSY duality landscape)
**Question:** Can the SU(2)_L sector of the SM be dualised via Sp(1) ≅ SU(2) duality instead of Sannino's SU(N) route? Sp(N_c) with 2N_f fundamentals has magnetic gauge group Sp(N_f - N_c - 2). For SU(2)_L ≅ Sp(1), what is the electric theory and what new anomaly matching conditions arise?
**Decisive output:** Explicit electric theory field content, anomaly matching verification, comparison with the Sannino SU(N) route.
**Anchor:** Intriligator–Pouliot hep-th/9505006 (Sp duality) and Cacciapaglia–Sannino 2407.17281 (SM dualisation).

## Paper 2: Dual Meson Mass Sum Rules from the 6×6 Flavour Matrix

**Theme:** From Lecture 10 (mesons as dual mesons)
**Question:** The scalar democracy framework with 18 Higgs doublets (= 6×6 meson matrix) + hierarchical VEVs implies algebraic relations among meson masses. What sum rules arise from the structure of the meson matrix, and do they hold against PDG data?
**Decisive output:** Derived sum rules, numerical comparison with PDG masses, assessment of which sum rules are trivially satisfied vs genuinely constraining.
**Anchor:** PDG 2024 meson masses; Gell-Mann–Okubo mass formula as benchmark.

## Paper 3: Mass Exponents and Supercurrent Tests at the Conformal Window

**Theme:** From Lecture 6 (emergent SUSY)
**Question:** Can the magnetic fixed point studied by Antipin, Mojaza, Pica and Sannino (2013) motivate a lattice test at the lower boundary of the fundamental-only SU(3) conformal window? Propose specific measurement protocols for SU(3) N_f = 8-12 lattice simulations.
**Decisive output:** A mode-number test of the eight-flavour exponent benchmark $1/8$, which has no known mechanism in fundamental-only QCD, and an independent adjoint-current Ward identity.
**Anchor:** Existing SU(3) N_f=8,12 lattice data (LatKMI, LSD collaborations).

The eight-flavour test requires an independent assumption about the leading mass operator of a QCD fixed point. Its target is a Dirac mode-number slope of 32/9. [Derivation and scope of the matching](paper-3-emergent-susy-lattice/SUMMARY.md)

For a direct supersymmetry test, the six-flavour theory with an additional massless adjoint Weyl fermion admits a baryon-neutral supercurrent candidate and enough ultraviolet Euler anomaly for a same-rank SQCD endpoint. If a positive squark mass at that endpoint decouples into the same scalar-free basin, a return flow requires $\Delta_K\ge4$ for the Konishi scalar. Its dimension and the basin remain open. The current and its conjugate must generate translations on a flavour-nonsinglet bilinear. [Endpoint classification and lattice test](paper-3-emergent-susy-lattice/SUMMARY.md#which-theories-can-support-a-supercurrent)

Holomorphic scale matching illustrates the normalization issue. At $(N_c,N_f)=(3,8)$ it gives $\Lambda_e\Lambda_m^7=-\mu^8$ in the conventional choice of phases. The parameter $\mu$ specifies the normalization of the magnetic meson. Extracting a canonical mass also requires its kinetic term. The scaling dimension of the nonsupersymmetric mass operator remains independent input. The logarithmic mode-number slope removes an overall normalization and tests that dimension directly. [Intriligator and Seiberg, Eq. (5.6)](https://arxiv.org/pdf/hep-th/9509066#page=22) · [Alphaology on meson normalization](https://explaining-alphaology.al-rivero.chatgpt.site/geometry-duality/#duality)

**Standing Wilson fermion goal.** Determine whether one normalized supercurrent closes on the stress-tensor translation of a physical bilinear in the six-plus-adjoint theory. Search the release at the start of each visit, commit and push the partial calculation, then rotate. The finite contact survives the adjoint Pfaffian. The normalized free gauge–adjoint charge translates the gauge field and gives zero on a quark bilinear with a nonzero stress response. Next resolve the matter breaking insertion against a separate probe. [Finite-regulator derivation and next spectator](paper-3-emergent-susy-lattice/FERMION-WARD.md)

### A normalized traceless source for the eight-flavour test

Use eight dynamical Wilson Dirac fundamentals of $SU(3)$ with one common reference coupling and a mass-independent subtraction at a fixed $\mu_0$. At the symmetric point take $m_R>0$. Vary the mass matrix as $M_R=m_R{\bf1}+\lambda_R T$ with $T=\operatorname{diag}(1,-1,0,\ldots,0)/2$. Fix the critical Wilson mass, the coupling and the scalar renormalization prescription independently of the mode count. For example, use the massless Landau-gauge RI/SMOM nonsinglet scalar vertex with normalized quark legs and $p_1^2=p_2^2=(p_1-p_2)^2=\mu_0^2$. Use the inverse scalar factor for the nonsinglet mass, including the chosen improvement terms at finite cutoff. Flavour interchange then makes singlet retunings even in $\lambda_R$ at the symmetric point. [RI/SMOM bilinear prescription](https://arxiv.org/abs/0901.2599)

**First test — the source and current.** The action derivative in this direction inserts the spacetime integral of $S_T^R=(\bar\psi T\psi)_R$. With eight sea determinants and physical volume held fixed the finite-regulator identity is
$$
\partial_{\lambda_R}\langle Y\rangle=
\langle\partial_{\lambda_R}Y\rangle-
\langle Y\,\partial_{\lambda_R}S_{\rm lat}\rangle_c .
$$
Include the source dependence of the insertions, counterterms and bare parameters along the tuned trajectory. Use the conserved point-split vector current for the flavour generator $E_{12}$. In conventions $\delta\psi=\alpha E_{12}\psi$, $\delta\bar\psi=-\bar\psi\alpha E_{12}$ and the smeared divergence $D_{12}(\alpha)$ of §108.1, the continuum matching condition is
$$
\langle D^R_{12}(\alpha)Y\rangle+\langle\delta_{12,\alpha}Y\rangle
=\lambda_R\langle S^R_{12}(\alpha)Y\rangle .
$$
Take $Y=S_{21}^R(y)S_T^R(z)$ with $\alpha=1$ near $y$ and zero near $z$, using disjoint smooth supports. The contact term is $-2\langle S_T^R(y)S_T^R(z)\rangle$ because $[E_{21},E_{12}]=-2T$. This checks current normalization whenever the separated correlator survives. At $\lambda_R=0$ the predicted integrated divergence is the opposite of that contact. The scalar unit is fixed by the independent source prescription. The six-flavour fit rescales a scalar density by a vector coefficient divided by a fitted mass difference. At degeneracy that quotient needs a separate limiting prescription, which is why this test normalizes the scalar before varying the masses. Any use of a local axial or vector bilinear in place of the conserved vector current needs its own matching, including the subtracted Wilson breaking term for the axial current. [Submitted finite Ward identity](https://github.com/yang-mills-group/OpenAI-QCD-20261104/blob/53f81cafe5cb9cd18cd0d5b49b8364cce50a0fe7/proof/YM/Massive/PCAC/Bare.lean) · [Continuum contact obligation](https://github.com/yang-mills-group/QCD/blob/9b2971888b9d525431bdb398ae2cb3ac33bf28e5/docs/mass-current-normalization.md)

**Second test — the scaling operator.** Measure the separated scalar correlator and the mode count on the symmetric ensembles. Use a single fixed valence operator or a flavour-symmetric count. Exchanging flavours 1 and 2 sends $\lambda_R$ to $-\lambda_R$ and preserves this count. Its first derivative in the traceless sea source vanishes even at finite cutoff. The spectral observable is the slope in the **renormalized eigenvalue threshold**. For Wilson fermions use the spectral projector of $D_m^\dagger D_m$ with its renormalized cutoff $M_R$. In the continuum $\Lambda_R^2=M_R^2-m_R^2$. Report the density per physical four-volume with exact zero modes omitted, as in Paper 3. [Wilson mode-number renormalization](https://arxiv.org/abs/0812.3638)

At an infrared fixed point with restored chiral flavour symmetry, a leading mass multiplet of dimension $23/8$ and nonzero overlap with our scalar would give, for a fixed dilation $b>1$,
$$
 \frac{\langle S_T^R(br) S_T^R(0)\rangle_c}
      {\langle S_T^R(r) S_T^R(0)\rangle_c}\longrightarrow b^{-23/4},
 \qquad
 \frac{n(b\Lambda_R)}{n(\Lambda_R)}\longrightarrow b^{32/9}.
$$
Here $r$ is a separation along one fixed direction. The first exponent tests $2\Delta$ and the second tests $4/(4-\Delta)$. Take the cutoff limit at fixed physical box, mass, separations, and thresholds. Increase the box, then take $m_R\downarrow0$ before probing $r\to\infty$ and $\Lambda_R\downarrow0$. Compare freely fitted slopes in overlapping scale windows as these controls improve. Check fixed-point running independently. A different limiting exponent falsifies this matching at an established fixed point. A transient walking window leaves it unresolved. [Mode-number scaling](https://arxiv.org/abs/1204.4432)

The six-flavour release supplies the transfer of inserted densities and a mass fit on a selected massive trajectory. Its leading scheduling inequality admits eight flavours arithmetically, with $11-16/3=17/3>11/2$. The eight-flavour construction still needs a tuned neighbourhood of $\lambda_R=0$, contact and insertion bounds uniform towards the chiral limit, and infrared control on that same family. The SQCD exponent remains a benchmark. [Running and flavour budget](https://github.com/yang-mills-group/QCD/blob/9b2971888b9d525431bdb398ae2cb3ac33bf28e5/docs/flavor-running-tests.md)

## Paper 4: Why Three Generations — The n_g ≥ 3 Bound Across Duality Types

**Theme:** From Lecture 7 (generation bound)
**Question:** The Cacciapaglia-Sannino construction gives n_g ≥ 3 from requiring a non-abelian electric gauge group. How does this bound change for SO, Sp, and Kutasov-Schwimmer dualities? Is there a duality type that predicts exactly n_g = 3?
**Decisive output:** Table of generation bounds for all duality types (SU, SO, Sp, KS with various k), identification of which (if any) predict n_g = 3 exactly.
**Anchor:** Seiberg hep-th/9411149 (SU), Intriligator-Seiberg hep-th/9509066 (SO/Sp), Kutasov-Schwimmer hep-th/9505004 (KS).

## Can the dormant-doublet model tie the lepton masses to QCD?

The alphaology page compares three measured combinations. The isospin-averaged nucleon mass divided by three, $H_N=(m_p+m_n)/6$, is $312.97$ MeV. The lepton normalization $A_\ell=(m_e+m_\mu+m_\tau)/6$ is $313.85$ MeV. The tabulated electroweak combination $\alpha(0)\sqrt{M_Z^2-M_W^2}$ is $314.47$ MeV. Comparing the last quantity with $\alpha g'v/2$ uses a tree-level mass relation and requires radiative matching for precision work. [Alphaology, definitions and inputs](https://explaining-alphaology.al-rivero.chatgpt.site/)

In the diagonal dormant-doublet model of Lecture 11, $A_\ell=yv\sum_i x_i^2/(6\sqrt{2})$ at tree level, with $x_i=\mu_{0i}/M_i$. Comparison with the lepton pole masses requires running and finite matching. For a local variation of $v$, hold the six-flavour QCD scale $\Lambda_6$ and the heavy-quark threshold ratios $m_{c,b,t}/v$ fixed. Continuous one-loop QCD matching across those thresholds, with no other coloured states in the interval, gives $\Lambda_3=\Lambda_6^{7/9}(m_tm_bm_c)^{2/27}$. To leading order in heavy-quark decoupling, the three-light-flavour chiral limit of pure QCD gives $H_N^{(0)}\propto\Lambda_3$, so its logarithmic slope is $2/9$. For $A_\ell$ to track this benchmark along the same variation, differentiating the lepton mass formula requires

$$
\frac{d\ln y}{d\ln v}
  +2\sum_i w_i\frac{d\ln x_i}{d\ln v}
  =-\frac79,\qquad w_i=\frac{x_i^2}{\sum_j x_j^2}.
$$

Fixed $y,x_i$ give $H_N^{(0)}/A_\ell\propto v^{-7/9}$. At fixed $y$, a common $x_i\propto v^{-7/18}$ would give the required response while preserving the lepton mass ratios. A potential or threshold calculation must produce that response independently to explain tracking on this path. At physical light masses the hadronic slope also contains the light-quark sigma terms. Equality at one value of $v$ alone imposes no derivative condition. [Threshold derivation and light-quark correction](https://explaining-alphaology.al-rivero.chatgpt.site/strong-dynamics/#thresholds)

The sister repository supplies two checks on proposed mechanisms. In its Berger-sphere reduction, matching $e^2/g_s^2=3/8$ fixes the round shape and leaves a free radius $R$ with $\alpha_{\rm em},\alpha_s\propto R^{-7}$ at matching. The relative normalization alone leaves the low-energy scale undetermined. Its five-flavour adjoint reproduces the electromagnetic multiplicities of three lepton generations with right-handed neutrinos. Assigning the generations to a flavour triplet then requires a source of flavour breaking to split their masses. Lecture 11 derives the corresponding test for a symmetric potential in the mixing ratios. [Berger matching](https://github.com/arivero/conneskk/blob/fd698239cd54a4b8a25054cab7abb4c408f96883/results/47_berger_radius_at_matching.md) · [Five-flavour decomposition](https://github.com/arivero/conneskk/blob/fd698239cd54a4b8a25054cab7abb4c408f96883/lemmas/52_lepton_generation_three_views.md) · [Lecture 11, §4](../lectures/lecture-11.pdf)

The inverse down-quark route to the same scale has a recorded negative answer. Its normalization $\sqrt{C_\ell C_d}$ runs with the renormalization point and matches $f_\pi$ only at $\mu_\ast\simeq2$ GeV. A bridge to $f_\pi$ has to supply an RG-invariant relation, for example through $m_i\langle\bar q_iq_i\rangle$ or a matching scale fixed independently, a computed Kähler coefficient, and the shift from the Koide phase $0.190$ rad of the inverse down triple to the lepton value $0.2222$ rad. [Inverse-Koide scale note](INVERSE-KOIDE-SCALE.md)
