# Mass Exponents and Supercurrent Tests at the Conformal Window

## What gives $1/8$

In massless $\mathcal N=1$ electric SQCD at the origin of moduli space, the chiral meson is $M^i{}_j=Q^i\widetilde Q_j$. Its lowest component is a squark bilinear. A constant superpotential mass couples through $\int d^2\theta\,m^j{}_i M^i{}_j+\mathrm{h.c.}$, so the local operator sourced by the mass is the top component $F_M$. At zero mass the electric auxiliary fields vanish on shell and $F_M=-\psi_Q\psi_{\widetilde Q}$ up to conventions. A real common mass selects its scalar trace plus its conjugate. [Seiberg, §§2 and 4](https://arxiv.org/pdf/hep-th/9411149)

Inside the interacting SQCD window $3N_c/2<N_f<3N_c$, the superconformal charge gives $\Delta_M=3R(M)/2=3(1-N_c/N_f)$. Acting with two supercharges adds one unit of dimension. For $N_c=3$ and $N_f=8$,

$$
R(Q)=\frac58,\quad R(M)=\frac54,\quad
\Delta_M=\frac{15}{8},\quad \Delta_{F_M}=\frac{23}{8},\quad
y_m=4-\Delta_{F_M}=\frac98,\quad \gamma_m^*=y_m-1=\frac18.
$$

In general $\gamma_m^*=(3N_c-N_f)/N_f=-\gamma_Q^*$, approaching zero at the upper edge and one at the lower edge from inside. The old summary used $3-\Delta_M$ for the anomalous dimension. That expression gives the mass-source eigenvalue $y_m$.

## Assumption needed in the lattice theory

The lattice target has eight Dirac fundamentals and no squarks or adjoint Weyl fermion. Its mass matrix sources $B^i{}_j=\bar\psi_{Rj}\psi_L^{\,i}$ and its conjugate. **The proposed matching assumes an infrared fixed point at the candidate boundary and a leading mass operator of dimension $23/8$.** The mass insertion must overlap with that scaling operator, with no more relevant contribution in the same channel. Matching the flavour quantum numbers alone leaves the dimension undetermined. AMPS studied a perturbative magnetic theory whose proposed electric dual includes an adjoint Weyl fermion. [Antipin, Mojaza, Pica and Sannino](https://arxiv.org/abs/1105.1510)

There are two checks on a literal SQCD interpretation. The central element $-\mathbf 1_8$ of unbroken vector $SU(8)$ acts as fermion parity on local operators built from these quarks and gluons. A local $\mathcal N=1$ supercurrent would have to be both fermionic and a vector-flavour singlet, giving opposite signs under the same element. Independently, the full SQCD fixed point has Euler anomaly $2535/1024$, larger than the fundamental-only UV value $19/9$, contrary to the four-dimensional $a$-theorem for such a flow. Equality of the mass exponents alone is compatible with these checks. [Paper 3, mass-deformation matching](paper.pdf)

## Lattice measurement

On eight-flavour gauge ensembles, count both signs of the nonzero massless Dirac eigenvalues with renormalised magnitude below $\Lambda_R$ and divide the ensemble average by four-volume. This gives $n(\Lambda_R)=2\int_0^{\Lambda_R}\rho_R(\lambda)\,d\lambda$ with $\rho_R$ the positive-branch density. The count is RG invariant and the cutoff scales like the quark mass. Thus $n(\Lambda_R)=b^{-4}n(b^{y_m}\Lambda_R)$ at a four-dimensional fixed point. [Patella](https://arxiv.org/abs/1204.4432) and [Cheng et al.](https://arxiv.org/abs/1301.1355)

| Measurement | Eight-flavour target if the mass exponent matches |
|---|---|
| Logarithmic slope of $n(\Lambda_R)$ | $4/y_m=32/9$, equivalently $\rho_R(\lambda)\propto\lambda^{23/9}$ |
| Local two-point function of an off-diagonal $B$ and its conjugate | $\langle B(x)B^\dagger(0)\rangle\propto\lvert x\rvert^{-23/4}$ |
| Hadron masses or $f_\pi$ under a common small mass | $m_R^{8/9}$ under single-mass hyperscaling |

Fit the slope freely above finite-volume and sea-mass distortions and below the UV crossover and cutoff. Check stability under varying the interval, increasing volumes, reducing sea masses and taking the continuum limit. A different limiting slope at an established fixed point rules out exponent matching. A nonzero chiral-limit $\rho_R(0)$ after the thermodynamic limit gives $n\propto\Lambda_R$ and signals chiral symmetry breaking. A power law confined to a finite interval can occur during walking.

## Which theories can support a supercurrent?

Normalize baryon number $B=1$ for a colour baryon. In fundamental-only $SU(N_c)$, colour singlets obey $(-1)^F=(-1)^{N_cB}$. At even $N_c$ this excludes every local fermionic current. At odd $N_c$ such a current has odd baryon number. In a baryon- and charge-conjugation-preserving vacuum, unitary $C$ reverses $B$ and preserves the chirality of a unique Weyl supercharge. Consequently that charge must have $B=0$. This excludes a single local supersymmetry under those hypotheses. For even $N_f$ the vector-flavour centre gives an independent exclusion. For a same-rank SQCD endpoint with its standard chiral embedding, the two mixed baryon–flavour anomalies also force the baryon–$R$ mixing coefficient to vanish. The proof specifies the role of the faithful symmetry, unbroken $C$ and the single-supercharge hypothesis. [Paper 3, endpoint classification](paper.tex) · [Faithful QCD symmetry](https://arxiv.org/abs/1807.07666)

| Proposed same-colour SQCD endpoint | Fundamental-only $SU(3)$ | With one adjoint Weyl and no squarks |
|---|---|---|
| 5 | The Euler inequality passes. Unbroken $B,C$ exclude a single Weyl supercharge. Two same-chirality charges exchanged by $C$ evade that step. | The current channel exists and the continuous anomalies and Euler inequality pass. The endpoint is open. |
| 6 | The Euler inequality passes. The vector centre excludes a single local supercharge. | The current channel exists and the anomalies pass. If a positive squark mass leads back into this scalar-free basin, the endpoint requires $\Delta_K\ge4$. |
| 7 | Two same-chirality charges exchanged by $C$ evade the single-charge argument. The Euler inequality independently excludes ordinary same-rank SQCD. | The endpoint violates the Euler inequality. |
| 8 | Both the vector centre and the Euler inequality exclude ordinary same-rank SQCD. | The endpoint violates the Euler inequality. |

At six flavours the Euler margins $a_{\rm UV}-a_{\rm SQCD}$ are $17/2880$ and $41/320$ respectively. If the symmetry-singlet Konishi scalar is relevant and a positive mass decouples the squarks into the proposed basin, a return to SQCD would contradict strict decrease of $a$. The exact slope relation is $\Delta_K=2+\beta'(\alpha_*)$. Using one-loop matter running in the NSVZ beta function gives $23/7$. This estimate and the decoupling step are uncontrolled. At $\Delta_K=4$ the marginal flow still needs a sign. Softly broken SQCD has squarks as well as the adjoint in the ultraviolet and requires its own deformation analysis. [Konishi exponent, Eq. (1.1)](https://arxiv.org/pdf/hep-th/9601023) · [Exact SQCD anomalies](https://arxiv.org/abs/hep-th/9708042) · [Anomaly-mediated deformation](https://doi.org/10.1103/PhysRevLett.126.251601)

At eight flavours the vector-centre obstruction extends to $1\leq\mathcal N<8$ local Weyl supercharges with the same microscopic field content and unbroken vector flavour symmetry. A bosonic constituent with the quark's colour, flavour and baryon charges changes that argument. A Koide law for composite masses can also be tested independently of spacetime supersymmetry. [Proof and composite examples](../COMPOSITE-FLAVOUR-MATCHING.md#how-far-the-two-issue-results-reach)

**Six-flavour adjoint Ward test.** Use six fundamental Dirac fermions and one adjoint Weyl $\lambda$. Form a renormalized spin-$3/2$, baryon-neutral flavour singlet starting with $\operatorname{tr}(F_{\rho\sigma}\sigma^{\rho\sigma}\sigma_\mu\bar\lambda)$. Integrate this current and its conjugate on two nested surfaces around an off-diagonal $O=\bar\psi_R\psi_L$. The sum of the two ordered fluxes in $\langle S\bar S O O^\dagger\rangle$ must equal the translation derivative $2\sigma^\mu\partial_\mu\langle O O^\dagger\rangle$ with a common current normalization. The off-diagonal bottom- and top-component candidates also give distinct power laws, $|x|^{-3}$ and $|x|^{-5}$, if they overlap with the six-flavour SQCD meson. This tests a fermionic symmetry beyond light-scalar spectroscopy. [Supercurrent construction and Ward identity](paper.pdf)

## Existing comparisons

| $N_f$ | SQCD mass exponent for $SU(3)$ | Two-loop QCD estimate | Selected lattice results |
|---|---|---|---|
| 8 | $1/8$ | No positive two-loop zero | LSD conformal fits give $\gamma_*=1.073(28)$ at LO and $1.207(41),1.200(44)$ at NLO. LatKMI finds effective $\gamma_m\simeq0.6$ for $m_\pi$ and $\simeq1$ in several other channels. [LSD Table II](https://arxiv.org/pdf/2305.03665#page=4) · [LatKMI eight-flavour study](https://arxiv.org/abs/1610.07011) |
| 10 | Outside the interacting window | $4.19$, beyond the unitarity bound and unreliable | Running-coupling measurements probe the location of the QCD conformal boundary. [Ten-flavour step scaling](https://arxiv.org/abs/2004.00754) |
| 12 | Outside the interacting window | $0.77$, with a large two-loop correction | LatKMI finite-size fits gave $\gamma_m\simeq0.4$–$0.5$. [LatKMI twelve-flavour study](https://arxiv.org/abs/1207.3060) |

The light singlet scalar and nonsinglet pion carry different vector flavour. Their mass ratio remains a probe of the spectrum, with no value fixed by the matched exponent. The gluonic spectrum and condensate potential likewise require their own dynamics. A SUSY Ward identity requires a local supercurrent.

On the same eight-flavour data LSD found leading-order Akaike criteria of 33.3 for dilaton EFT and 60.1 for mass-deformed conformal scaling. At NLO the dilaton fit gives 24.3. The two conformal fits give 34.9 and 24.9. The LO conformal mass power is $1/(1+1.073)=0.482$, compared with $8/9$. In the second NLO fit, the correction to $F_S$ reaches 46% of its LO term at the heaviest simulated mass. Existing fits disfavour $1/8$ unless the simulated masses are far from its scaling regime. The adjoint-supercurrent test requires different ensembles. [LSD comparison, Tables I and II](https://arxiv.org/pdf/2305.03665)

[Paper source](paper.tex) · [Compiled paper](paper.pdf)
