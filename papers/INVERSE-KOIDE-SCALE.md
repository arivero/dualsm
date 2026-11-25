# What fixes the inverse-Koide scale?

Issue 4 asks whether Seiberg duality and chiral QCD can select the scale $M=\sqrt{C_\ell C_d}$ that maps an inverse down-quark Koide triple onto the charged leptons, and whether that scale is the pion decay constant. For every construction examined below the answer is negative and the scale stays free. The numerical agreement $M\simeq f_\pi$ is a choice of renormalization point near 2 GeV. One narrower bridge problem survives, and the research plan records it. Every number here is recomputed by [`scripts/verify_inverse_koide_scale.py`](../scripts/verify_inverse_koide_scale.py). [Issue 4](https://github.com/arivero/dualsm/issues/4)

## Definitions and the renormalization-group orbit

With $\mathcal Q(z)=(\sum_i\sqrt{z_i})^2/\sum_iz_i$ define

$$
C_\ell=\frac{(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau})^2}{9}=313.8509\ \mathrm{MeV},\qquad
C_d(\mu)=\frac{9}{\big(m_d(\mu)^{-1/2}+m_s(\mu)^{-1/2}+m_b(\mu)^{-1/2}\big)^2}.
$$

$C_\ell$ uses the PDG 2024 pole masses. For the image triple $\widetilde m_i=M^2/m_i$ one has $\mathcal Q(\widetilde m)=\mathcal Q(1/m)$ and $(\sum_i\sqrt{\widetilde m_i})^2/9=M^2/C_d$ for every $M>0$. The inverse relation therefore leaves $M$ free, as `lectures/lecture-11.tex` already states: a mass-scale prediction requires an independent matching condition. Equal normalizations $M^2/C_d=C_\ell$ give $M=M_{\rm match}=\sqrt{C_\ell C_d}$, which is a further hypothesis. The issue's inputs $(4.67,93.4,4180)$ MeV give $C_d=26.5991$ MeV and $M_{\rm match}=91.368$ MeV, $0.76\%$ below $f_\pi=92.07(57)$ MeV. The Lecture 11 inputs $m_d(2\,{\rm GeV})=4.70\pm0.20$, $m_s(2\,{\rm GeV})=93.5\pm0.8$ and $\bar m_b(\bar m_b)=4183\pm7$ MeV give $26.7405$ and $91.611$ MeV. Both mix reference scales.

**Proposition (orbit).** Assume a mass-independent scheme ($\overline{\rm MS}$), a flavour-universal mass anomalous dimension, and all three masses at one common scale $\mu$. Continue $m_b$ below $\bar m_b$ with the four-flavour universal factor, which is a convention because the $b$ quark is no dynamical flavour there. Then $(m_d,m_s,m_b)(\mu)=c(\mu)\,(m_d,m_s,m_b)(\mu_0)$ moves along a ray. The shape invariants $\mathcal Q(1/m)$, the Koide phase of $1/m$ and the weights $w_i=m_i^{-1/2}/\sum_jm_j^{-1/2}$ are the same at every common scale, and $C_d(\mu)=c(\mu)\,C_d(\mu_0)$ is the coordinate along the ray. The one exception is the two-loop decoupling step at $\bar m_b$, which shifts the light masses relative to $m_b$ by $0.1\%$ and moves $\mathcal Q(1/m)$ in its fifth digit. Any relation equating $C_d$ to an RG-invariant combination such as $f_\pi^2/C_\ell$ or $3f_\pi^2/m_N$ therefore holds at exactly one scale $\mu_\ast$, and imposing it is equivalent to choosing $\mu_\ast$.

## The common-scale table

The running uses four-loop $\beta$ and $\gamma_m$ in $a=\alpha_s/\pi$ from $\alpha_s(M_Z)=0.1180$, with two-loop decoupling at $\mu=\bar m_h$: $a^{(n_f-1)}=a^{(n_f)}(1+\tfrac{11}{72}a^2)$ and $m^{(n_f-1)}=m^{(n_f)}(1+\tfrac{89}{432}a^2)$. The light masses at 2 GeV are four-flavour values. This gives $\alpha_s(2\,{\rm GeV})=0.3014$ and $\alpha_s(\bar m_b)=0.2247$. The universal factor $c(\mu)=m(\mu)/m(2\,{\rm GeV})$ is $0.9040$, $0.8446$, $0.5780$ and $0.5512$ at $3$ GeV, $\bar m_b$, $M_Z$ and $\bar m_t=162.9$ GeV. At one, two, three and four loops $c(\bar m_t)=0.632,\ 0.563,\ 0.553,\ 0.551$, so the truncation error at four loops is below $0.4\%$. From the Paper 2 inputs the code gives $(2.574,\ 51.48,\ 2730)$ MeV at $\bar m_t$, matching the printed $(2.58,\ 51.5,\ 2730)$ within their three-figure rounding. The rounded entries give $M_{\rm match}=68.05$ MeV, as in the 24 November comment, and the unrounded ones $67.98$ MeV. [Four-loop $\beta$: van Ritbergen, Vermaseren and Larin](https://arxiv.org/abs/hep-ph/9701390) · [Four-loop $\gamma_m$: Chetyrkin](https://arxiv.org/abs/hep-ph/9703278) · [Vermaseren, Larin and van Ritbergen](https://arxiv.org/abs/hep-ph/9703284) · [Decoupling: Chetyrkin, Kniehl and Steinhauser](https://arxiv.org/abs/hep-ph/9706430) · [Paper 2 running convention](paper-2-meson-mass-sum-rules/paper.tex)

With the Lecture 11 inputs at a common scale:

| $\mu$ | $2$ GeV | $3$ GeV | $\bar m_b$ | $M_Z$ | $\bar m_t$ |
|---|---|---|---|---|---|
| $C_d$ (MeV) | $26.86$ | $24.28$ | $22.68$ | $15.52$ | $14.80$ |
| $M_{\rm match}$ (MeV) | $91.81$ | $87.29$ | $84.37$ | $69.80$ | $68.16$ |

At every scale $\mathcal Q(1/m)=1.4983$, the Koide phase of $1/m$ is $0.190$ rad and $w=(0.797,\ 0.179,\ 0.025)$ for $(d,s,b)$. The slope at 2 GeV is $d\ln M_{\rm match}/d\ln\mu=-0.141$, so $M_{\rm match}$ changes by $14\%$ per e-fold in $\mu$. The crossing with $f_\pi$ is at

$$
\mu_\ast=1.96\pm0.25\ \mathrm{GeV}.
$$

To first order $\delta\ln M_{\rm match}=\tfrac12\sqrt{\sum_iw_i^2(\delta m_i/m_i)^2}=1.7\%$, with the three input masses taken as uncorrelated. Shared running and threshold uncertainties would enter the off-diagonal covariance. Adding the $0.62\%$ error of $f_\pi$ and dividing by the slope gives the quoted error. Varying $\alpha_s(M_Z)$ to $0.1171$ and $0.1189$ moves $\mu_\ast$ to $1.958$ and $1.962$ GeV, because the light inputs are fixed at 2 GeV. The crossing lies at the reference scale where $m_d$ and $m_s$ are quoted. The $b$ quark carries $2.5\%$ of the weight, which is why the mixed-scale value $91.61$ MeV sits close to the common-scale $91.81$ MeV. [Weights and covariance, 24 November comment](https://github.com/arivero/dualsm/issues/4)

## A literal seesaw with quark-mass mediators

Pair each lepton with a quark and let the quark mass be the mediator of a $2\times2$ block. For the symmetric block with off-diagonal $\mu_i$ and mediator $m_{q,i}$, the light singular value equals $m_{\ell,i}$ exactly when $\mu_i^2=m_{\ell,i}(m_{\ell,i}+m_{q,i})$. This is the $\kappa=2$ case $T_i=m_i(M+m_i)$ of the issue 3 block, applied family by family. For general $\kappa\ge2$ the two off-diagonal entries are $u x_i$ and $v x_i$ with $u/v$ fixed, $uv\,x_i^2=T_i=m_{\ell,i}H_+(m_{\ell,i},m_{q,i},\kappa)$, and their spread across families is $\sqrt{T_{\max}/T_{\min}}$. A mechanism with one chirally fixed mixing entry needs a spread of one. The best of the six pairings, $(e,\mu,\tau)\leftrightarrow(b,s,d)$, needs $\mu_i=(46.24,\ 145.06,\ 1779.28)$ MeV with the mixed-scale inputs, a spread of $38.5$. For all six pairings the spread is nondecreasing in $\kappa$. With common-scale masses the minimum spread is $35.4$ at 2 GeV and $47.6$ at $\bar m_t$. In the other direction, a common entry $f_\pi$ with mediators $(m_d,m_s,m_b)$ gives light values $(89.75,\ 56.51,\ 2.03)$ MeV. The approximation $\mu^2/m_q$ needs $m_q\gg\mu$, which holds for the $b$ quark alone. A literal seesaw with quark-mass mediators and a common chiral mixing is therefore excluded. [Issue 3 block formula](COMPOSITE-FLAVOUR-MATCHING.md#finite-mixing-the-exact-koide-shift-and-the-reconstructed-mediator-mass)

## The SQCD inverse law and its normalization

In five-flavour $SU(3)$ SQCD on the full-rank branch the F-equations give $m_ih_i=S$ for every flavour, so the meson VEVs follow the inverse law $h_i=S/m_i$. Canonical masses carry the Kähler coefficients,

$$
m_{ij}^{\rm can}=\frac{|\mu|^2}{\sqrt{\kappa_{ij}\kappa_{ji}}}\left|\frac{m_im_j}{S}\right|,
$$

and those coefficients are dynamical input that the holomorphic data leave undetermined. A lepton-type mass linear in the VEV, $\widetilde m_i=\lambda\,h_i=\lambda S/m_i$, therefore has $M^2=\lambda S$ with one free positive coefficient $\lambda$ that absorbs the Kähler normalization. The inverse hierarchy survives and the scale does not. [Canonical masses on the full-rank branch](paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md#canonical-masses-on-the-full-rank-branch)

Chiral QCD departs from the SQCD law exactly where $C_d$ has its weight. For the light flavours the condensate is mass-independent at leading chiral order (Gell-Mann–Oakes–Renner), and lattice QCD gives $\langle\bar ss\rangle/\langle\bar ll\rangle=1.08(16)$, where the inverse law would give $m_l/m_s\approx1/27$. For a heavy quark the condensate obeys $m_Q\langle\bar QQ\rangle=-\tfrac1{12}\langle\alpha_sG^2/\pi\rangle$, which does reproduce the inverse law. The $d$ and $s$ quarks carry $97.5\%$ of the weight in $C_d$. A QCD realization of the inverse triple through quark condensates fails on those two flavours. [McNeile et al., strange and light condensates](https://arxiv.org/abs/1211.6577) · [Shifman, Vainshtein and Zakharov](https://doi.org/10.1016/0550-3213(79)90022-1)

## The direct image and its invariant tests

For $\widetilde m_i=M^2/m_i$ the equal normalization holds by construction once $M=M_{\rm match}$, so the map has one fitted parameter. Its RG-invariant predictions are the ratios and the phase. They give $m_d/m_s=0.0503$ for $m_\mu/m_\tau=0.0595$, a quotient of $0.845$, and $m_s/m_b=0.01888$ at a common scale for $m_e/m_\mu=0.004836$, a factor $3.90$. The Koide phase of $1/m$ is $0.190$ rad against $0.2222$ rad for the leptons. At 2 GeV the image spectrum is $(1.70,\ 90.1,\ 1793)$ MeV. Lecture 11 records the mixed-scale version: $m_\tau$ by construction, $m_\mu$ $15\%$ off and $m_e$ a factor $4$ wrong. [Lecture 11, the hierarchy problem of the seesaw](../lectures/lecture-11.pdf)

## Chiral limit and reference scales

At a common scale $C_d=9\,m_d\,w_d^2$, with $w_d^2=0.635$. As $m_u,m_d\to0$ the weight $w_d\to1$ and $C_d\to9m_d\to0$, while $f_\pi$ tends to its chiral-limit value $F$ with $f_\pi/F=1.064(7)$ for $N_f=2+1$. The relation $C_\ell C_d=f_\pi^2$ is therefore a point condition on $m_d(\mu)$ at physical quark masses. The $6.4\%$ gap between $f_\pi$ and $F$ and the $14\%$ change of $M_{\rm match}$ per e-fold in $\mu$ both exceed the $0.76\%$ agreement. [FLAG 2016, $F_\pi/F$](https://arxiv.org/abs/1607.00299)

Three reference scales near $313$ MeV are separate observables. $C_\ell=313.8509$ MeV is the Koide normalization of the lepton pole masses. $m_N/3=312.973$ MeV is one third of the isospin-averaged nucleon pole mass. $\alpha(0)\sqrt{M_Z^2-M_W^2}=314.473$ MeV uses the Thomson coupling and the 2026 PDG line-shape masses $91.1879$ and $80.3625$ GeV. Rewriting $C_\ell C_d\simeq f_\pi^2$ as $C_d\simeq3f_\pi^2/m_N=27.085$ MeV adds the hypothesis $C_\ell\simeq m_N/3$. In the quark-level linear sigma model of Delbourgo and Scadron, $M_q=2\pi f_\pi^\chi/\sqrt{N_c}=325.8$ MeV for $f_\pi^\chi=89.8$ MeV, $3.8\%$ above $C_\ell$. That model fixes a constituent scale from an explicit chiral Lagrangian and supplies no inverse triple. [Scheme caveats for the three scales](https://github.com/arivero/conneskk/blob/master/results/issues/19.md) · [Delbourgo and Scadron](https://arxiv.org/abs/hep-ph/9910242)

## Verdicts on the completion criteria

| Criterion of issue 4 | Verdict |
|---|---|
| 1. A chirally and gauge-consistent bridge from the axial order parameter to a canonically normalized mixing operator, with $f_\pi$ and $F$ distinguished | **Open.** The constructions examined are excluded: the literal seesaw by its spread, the SQCD law by its free Kähler coefficient, and a condensate realization by the light-flavour condensates. $f_\pi$ and $F$ differ by $6.4\%$. |
| 2. All three masses at one common $\overline{\rm MS}$ scale with thresholds and uncertainties | **Settled.** Table above, $\mu_\ast=1.96\pm0.25$ GeV with uncorrelated inputs, truncation below $0.4\%$. |
| 3. SQCD inverse hierarchy against physical ratios; does a free normalization survive? | **Settled: a free coefficient survives, so there is no scale prediction.** |
| 4. A scheme-independent falsifiable ratio, and the reference scales kept apart | **Settled, negative.** The phase $0.190$ against $0.2222$ rad and the ratios $0.845$ and $3.90$ fail for the direct image. The three reference scales are distinct observables. |

## Status

Known: the scale freedom of inverse Koide (Lecture 11), the free Kähler normalization (five-flavour note), four-loop running and decoupling, the Gell-Mann–Oakes–Renner relation, the heavy-quark condensate, the lattice condensate ratio, $F_\pi/F$, and the Delbourgo–Scadron model. New bookkeeping, elementary and AI-checked: the orbit statement with the crossing scale $\mu_\ast$, the literal-seesaw exclusion over all pairings and $\kappa\ge2$, and the comparison of the weights $w_i$ with the light-flavour condensates. No search for a prior statement of the crossing scale was made. Conditional: the numbers depend on the quoted inputs and on uncorrelated input errors. The $f_\pi$ relations of the related drafts remain empirical observations without derivations from first principles, the wording of `related-papers/phys4_draft.tex`. AI reviewers checked this note in issue 4; independent review is pending. [Chaudhary, August 2026](https://doi.org/10.55041/IJSREM66507) · [Chaudhary, September 2026](https://ijqf.org/archives/8567) · [Rivero, inverse Koide](https://arxiv.org/abs/2606.10060)
