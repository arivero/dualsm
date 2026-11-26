# Can five-flavour colour duality fix the electromagnetic lepton mass scale?

The target is $R_\ell=[(m_e+m_\mu+m_\tau)/6]/[\alpha(0)\sqrt{M_Z^2-M_W^2}]=0.9980(3)$. Use the PDG 2026 line-shape inputs recorded for this comparison, $M_W=80.3625(77)$ and $M_Z=91.1879(20)$ GeV, with $\alpha(0)^{-1}=137.035999$. The denominator is $314.4729$ MeV. The lepton pole masses $(0.51099895,105.6583755,1776.93)$ MeV give $313.8499$ MeV in the numerator, hence $R_\ell=0.998019$. Using $(m_p+m_n)/6=312.9729$ MeV gives $0.995230$. [Archived pdgLive inputs](https://github.com/arivero/pdghist/blob/60b4139972ee5a854d97f5cf2db997f2834a72ca/data/2026/electroweak.yaml#L36-L49) · [Lepton inputs](../../scripts/verify_koide_vev.py) · [Thomson coupling](https://physics.nist.gov/cgi-bin/cuu/Value?alphinv)

With independent weak-mass errors the fractional uncertainty is $\sqrt{(M_W\delta M_W)^2+(M_Z\delta M_Z)^2}/(M_Z^2-M_W^2)=0.000347$. Including the $0.09$ MeV tau uncertainty in quadrature gives $R_\ell=0.99802(35)$. Raising $M_W$ by $9$ MeV at fixed $M_Z$ raises $R_\ell$ by about $0.00039$. Comparing the model with this number requires charged-lepton pole masses, two weak poles in the same convention, and the Thomson charge. An independent gauge coupling survives even at fixed strong-sector inputs. [Issue 1](https://github.com/arivero/dualsm/issues/1) · [Electroweak and hadronic definitions](https://explaining-alphaology.al-rivero.chatgpt.site/)

## A current measurement on the one-mass branch

Take electric $\mathcal N=1$ $SU(3)$ SQCD with five pairs $(u,c,d,s,b)$. Its magnetic fields are $SU(2)_m$ quarks $q,\tilde q$ and the singlet $M^i{}_j=Q^i\widetilde Q_j$. This is a colour dual. The 66 mesons of the $Sp(3)\leftrightarrow Sp(1)$ weak dual in Paper 1 are singlets of its magnetic weak group. Use electric quark baryon number $+1$ and weakly gauge the vector charge $Y=t_f+B/15$, with $t_f=\operatorname{diag}(3,3,-2,-2,-2)/5$. Magnetic $q$ is a flavour antifundamental with baryon number $3/2$, so $Y(q_U)=-1/2$ and $Y(q_D)=+1/2$. Antifundamentals have the opposite charges. [Seiberg, §4](https://arxiv.org/pdf/hep-th/9411149) · [Five-flavour charge calculation](https://github.com/arivero/conneskk/issues/14#issuecomment-6674327248) · [Paper 1](../paper-1-sp-duality-sm/SUMMARY.md)

Turn on just $m_b$. The magnetic F-term gives $q_b\tilde q^b=-\mu m_b$. Choose the D-flat orientation where $q_b$ condenses in its $T^3=-1/2$ component and $\tilde q^b$ has the opposite weights. The surviving generator is $Q'=T^3+Y$, equal to $Y$ on magnetic singlets. To calculate a reference correlator, take canonical doublet kinetic terms and diagonal gauge kinetic terms at a matching scale. In charge-connection coordinates $(a_3,a_Y)$ the couplings to probes are $a_3J_3+a_YJ_Y$. With $t=p_E^2$ and transverse projectors suppressed, the inverse exchange kernel is

$$
\mathcal D_T^{-1}(t)=t\,\operatorname{diag}(g_m^{-2},g_Y^{-2})
       + f^2 d d^T,\qquad d=(1,-1)^T,\quad
 f^2=(|\langle q_b\rangle|^2+|\langle\tilde q^b\rangle|^2)/2 .
$$

With $a_Y$ an external source, integrating out $a_3$ gives the matter correlator $\langle J_Y^\mu J_Y^\nu\rangle=(t\delta^{\mu\nu}-p^\mu p^\nu)\Pi_Y(t)$, with $\Pi_Y(t)=f^2/(t+g_m^2 f^2)$ at this order, up to a local source counterterm. With $Y$ dynamical the Schur complement gives $\mathcal D_{YY}^{-1}=t[g_Y^{-2}+\Pi_Y(t)]$. Inverting the full matrix gives

$$
\mathcal D_T(t)=\frac{e^2 n n^T}{t}
       +\frac{h h^T}{(g_m^2+g_Y^2)(t+M_N^2)},\qquad
 n=(1,1)^T,\quad h=(g_m^2,-g_Y^2)^T ,
$$

$$
 e^{-2}=g_m^{-2}+g_Y^{-2},\qquad
 M_N^2=(g_m^2+g_Y^2)f^2,\qquad M_C^2=g_m^2 f^2 .
$$

The charge-one exchange residue is $e^2$. The charged vector comes from the two broken $SU(2)_m$ directions. For example the $SU(2)_m$-singlet source $q_b^T i\sigma_2 D_\mu q_b$ has $Y=+1$ and overlaps with that channel in the Higgs expansion. Gauging $Y$ requires the usual electromagnetic dressing for a charged probe. The pole difference gives $g_Y f$ for $\sqrt{M_N^2-M_C^2}$ in this approximation. The two-derivative canonical action is an assumption about kinetic data. At $(3,5)$ Seiberg duality gives no perturbative pole calculation at the undeformed fixed point. The physical correlator requires the renormalized polarization, including thresholds and cuts. Neither magnetic vector couples to observed coloured left-handed weak doublets in this field content. Identifying either pole with a measured weak boson would require such a current and matching its residue. [Komargodski on vector-current poles](https://arxiv.org/abs/1010.4105) · [Abbott and Farhi's confining weak model](https://columbia.edu/cu/neurotheory/Larry/AbbottPL81.pdf)

There is an infrared check independent of the canonical pole ansatz. At the origin of the remaining four-flavour moduli, the electric theory confines with massless mesons and baryons. The light flavours $(u,c,d,s)$ give eight charge-one meson chirals counting both signs. Of the four baryons obtained by omitting one flavour, two have charge $+1$ and two are neutral. Their conjugates supply two charges $-1$. On the magnetic side the surviving component of each $q_i$ has $Q'=\tfrac12+Y_i=(0,0,1,1)$, and the four conjugate components have opposite charges. With the eight charged mesons, both descriptions give $\sum_{\rm light}Q'^2=8+2+2=12$. In the weakly gauged infrared theory the leading screening is

$$
 e_{\rm eff}^{-2}(p)=e_{\rm eff}^{-2}(p_0)
       +\frac{12}{8\pi^2}\log\frac{p_0}{p}+\text{subleading terms} .
$$

The exactly massless branch therefore has a running photon exchange with vanishing limiting residue $\lim_{p\to0}p^2\mathcal D_{YY}(p^2)$. With massive charged thresholds a finite Thomson residue can be defined, and depends on those thresholds and the input $g_Y$. [Intriligator and Seiberg, §§4.3 and 5.5](https://arxiv.org/pdf/hep-th/9509066)

## Canonical masses on the full-rank branch

Now give all five electric flavours nonzero masses. The magnetic quarks become massive and the remaining pure magnetic $SU(2)$ confines. In holomorphic dimension-two coordinates, $\Lambda_e^4\widetilde\Lambda=\mu^5$. On a branch write $W=-2S+\operatorname{tr}(mM)$, $S=(\det M/\Lambda_e^4)^{1/2}$. At a diagonal supersymmetric vacuum $M_{ii}=h_i$ the F-equations give $m_i h_i=S$ and $S^3=\Lambda_e^4\det m$. For $i\ne j$ the determinant changes by $-\det M\,\delta M_{ij}\delta M_{ji}/(h_i h_j)$ to quadratic order in that pair. The holomorphic charged Hessian is consequently $H_{ij,ji}=S/(h_i h_j)=m_i m_j/S$. Its dimension is inverse mass in these coordinates. [Intriligator and Seiberg, Eqs. (5.6) and (5.18)](https://arxiv.org/pdf/hep-th/9509066)

Let $G_\pm$ be the positive Kähler metrics of the charge $\pm1$ fields in this vacuum. The quadratic two-derivative fermion masses are the singular values of $(G_+^{-1/2})^T H_{+-}G_-^{-1/2}$. For a diagonal metric $G_{ij,\overline{ij}}=\kappa_{ij}/|\mu|^2$ one obtains

$$
 m_{ij}^{\rm can}=
 \frac{|\mu|^2}{\sqrt{\kappa_{ij}\kappa_{ji}}}
       \left|\frac{m_i m_j}{S}\right|.
$$

Under $M'=cM$, the Hessian transforms as $H'=H/c^2$ and the metric as $G'=G/|c|^2$. All canonical masses are invariant. Changing the physical metric with holomorphic inputs held fixed does change the result. For example multiplying both metric entries of a pair by $k>0$ divides its mass by $k$. In a specified microscopic SQCD the metric is dynamical input to be computed. Momentum-dependent self-energies would also enter pole masses beyond a local low-energy approximation. The same free coefficient leaves the scale of an inverse-Koide image of the down quarks undetermined. [Inverse-Koide scale note](../INVERSE-KOIDE-SCALE.md)

### What six charged masses test

Keep the diagonal two-derivative metric and identify each charged pair by its flavour current. With $a=u,c$, $j=d,s,b$ and $Z_{aj}=\sqrt{\kappa_{aj}\kappa_{ja}}>0$, define the dimensionless cross-ratio of four canonical masses. The preceding formula gives
$$
 \frac{m_{uj}^{\rm can}m_{ck}^{\rm can}}
      {m_{uk}^{\rm can}m_{cj}^{\rm can}}
 =\frac{Z_{uk}Z_{cj}}{Z_{uj}Z_{ck}} .
$$
The five microscopic masses, the common holomorphic condensate and the choice of meson normalization cancel. Thus the two comparisons $(j,k)=(d,s),(d,b)$ both equal one exactly when the six positive normalization factors separate as $Z_{aj}=A_a B_j$. In the converse direction choose $A_a=Z_{ad}$ and $B_j=Z_{uj}/Z_{ud}$; the two equalities determine the remaining entries in the charm row. A change in just one channel can be detected even when the absolute normalization is unknown.

This is a test of multiplicative factorization of a two-by-three **array**. All six charged pairs have nonzero canonical masses under the hypotheses. A nondiagonal metric or momentum-dependent pole self-energy calls for current-resolved matching before applying the ratio. The conditions leave a common lepton or hadron mass scale free.

## A common low-energy counterexample

The two vacua above have different light fields. To test predictivity in a *single* EFT, keep the full-rank branch and weakly gauge its vector $Y$. Add a spectator $SU(2)_w$ and a vectorlike pair of Higgs doublets of $Y=\pm1/2$ with a fixed total VEV $v_w$ and massive charged excitations. The SQCD states are $SU(2)_w$ singlets. This explicit extension gives a gapped charged spectrum, a Thomson matching prescription and identifiable spectator charged and neutral poles. Use a common weak matching scale, canonically normalized kinetic terms and the tree approximation. Choose the three charged $(u,d),(u,s),(u,b)$ mesino pairs as mass probes, and denote the sum of their canonical masses by $\Sigma_u$. The result is

$$
 \frac{\Sigma_u/6}{\alpha_{\rm tree}\sqrt{M_Z^2-M_W^2}}
 =\frac{4\pi\Sigma_u(g_w^2+g_Y^2)}
        {3v_w g_w^2g_Y^3},\qquad
 \sqrt{M_Z^2-M_W^2}=g_Yv_w/2 .
$$

Holding the strong-sector inputs, $v_w$ and $g_w$ fixed and varying the independent weak $g_Y$ changes this ratio as $g_Y^{-3}$ at small $g_Y$. Finite threshold matching to $\alpha(0)$ does not remove that free boundary coupling. The mesino probes are vectorlike. The traceless meson contains $(12,6,6)$ left-Weyl components of charges $(0,+1,-1)$, twice the $(6,3,3)$ in three chiral lepton generations including $\nu_R$. An exact generation-triplet symmetry also makes its invariant mass matrix degenerate. A physical lepton interpretation requires mirror removal, a chiral weak current and a source of flavour breaking. The measured $0.9980$ can supply an input to an extension. The five-flavour duality by itself has neither a common weak/lepton identification nor a prediction for that number. [Lepton representation count](https://github.com/arivero/conneskk/blob/fd698239cd54a4b8a25054cab7abb4c408f96883/lemmas/52_lepton_generation_three_views.md) · [Six-flavour mass sum rules](SUMMARY.md)

In a geometric family with matched gauge couplings the independent spectator variation is unavailable. The projective-product construction gives a separate tree-level test by varying its interval length at fixed matched radii. [Geometric scale response](../COMPOSITE-FLAVOUR-MATCHING.md#how-far-the-two-issue-results-reach)
