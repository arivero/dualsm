# Lattice signatures of emergent supersymmetry at the conformal window boundary

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

## Existing comparisons

| $N_f$ | SQCD mass exponent for $SU(3)$ | Two-loop QCD estimate | Selected lattice results |
|---|---|---|---|
| 8 | $1/8$ | No positive two-loop zero | Finite-mass hyperscaling gives effective $\gamma_m\simeq0.6$ for $m_\pi$ and $\simeq1$ in several other channels. [LatKMI eight-flavour study](https://arxiv.org/abs/1610.07011) |
| 10 | Outside the interacting window | $4.19$, beyond the unitarity bound and unreliable | Running-coupling measurements probe the location of the QCD conformal boundary. [Ten-flavour step scaling](https://arxiv.org/abs/2004.00754) |
| 12 | Outside the interacting window | $0.77$, with a large two-loop correction | LatKMI finite-size fits gave $\gamma_m\simeq0.4$–$0.5$. [LatKMI twelve-flavour study](https://arxiv.org/abs/1207.3060) |

The light singlet scalar and nonsinglet pion carry different vector flavour. Their mass ratio remains a probe of the spectrum, with no value fixed by the matched exponent. The gluonic spectrum and condensate potential likewise require their own dynamics. A SUSY Ward identity requires a local supercurrent.

[Paper source](paper.tex) · [Compiled paper](paper.pdf)
