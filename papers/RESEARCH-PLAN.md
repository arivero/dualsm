# Four Research Papers from the Dualised SM Lectures

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

## Paper 3: Lattice Signatures of Emergent Supersymmetry at the Conformal Window Boundary

**Theme:** From Lecture 6 (emergent SUSY)
**Question:** Can the magnetic fixed point studied by Antipin, Mojaza, Pica and Sannino (2013) motivate a lattice test at the lower boundary of the fundamental-only SU(3) conformal window? Propose specific measurement protocols for SU(3) N_f = 8-12 lattice simulations.
**Decisive output:** List of discriminating observables with predicted values/scaling in the emergent-SUSY scenario vs the confining scenario.
**Anchor:** Existing SU(3) N_f=8,12 lattice data (LatKMI, LSD collaborations).

The eight-flavour test requires an independent assumption about the leading mass operator of a QCD fixed point. Its target is a Dirac mode-number slope of 32/9. [Derivation and scope of the matching](paper-3-emergent-susy-lattice/SUMMARY.md)

Holomorphic scale matching illustrates the normalization issue. At $(N_c,N_f)=(3,8)$ it gives $\Lambda_e\Lambda_m^7=-\mu^8$ in the conventional choice of phases. The parameter $\mu$ specifies the normalization of the magnetic meson. Extracting a canonical mass also requires its kinetic term. The scaling dimension of the nonsupersymmetric mass operator remains independent input. The logarithmic mode-number slope removes an overall normalization and tests that dimension directly. [Intriligator and Seiberg, Eq. (5.6)](https://arxiv.org/pdf/hep-th/9509066#page=22) · [Alphaology on meson normalization](https://explaining-alphaology.al-rivero.chatgpt.site/geometry-duality/#duality)

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
