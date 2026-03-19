# Conventions: The Dualised Standard Model

**Established:** 2026-03-20
**Ground truth hierarchy:** Seiberg > Sannino > Terning

All conventions follow Seiberg (hep-th/9411149) unless otherwise noted.

## Unit System

Natural units: hbar = c = k_B = 1.
- [length] = [time] = [energy]^{-1}
- [mass] = [energy]
- Lagrangian density [L] = [mass]^4

## Metric Signature

Mostly minus (West Coast): eta = diag(+1, -1, -1, -1).
- On-shell: p^2 = E^2 - **p**^2 = m^2 > 0 for massive particles
- Feynman propagator: i/(k^2 - m^2 + i epsilon)

## Fourier Convention

Physics (asymmetric):
- f_tilde(k) = integral dx f(x) e^{-ikx}
- f(x) = integral dk/(2pi) f_tilde(k) e^{+ikx}

## Generator Normalisation and Dynkin Index

**CRITICAL — factor-of-2 errors propagate through all anomaly matching.**

Tr(T^a T^b) = (1/2) delta^{ab} in the fundamental representation.

Equivalently: T(fund) = 1/2 per Weyl fermion.

| Representation | T(R) | C_2(R) |
| -------------- | ---- | ------ |
| Fundamental N | 1/2 | (N^2-1)/(2N) |
| Antifundamental N-bar | 1/2 | (N^2-1)/(2N) |
| Adjoint | N | N |
| Antisymmetric_2 | (N-2)/2 | (N-1)(N+2)/(2N) |
| Symmetric_2 | (N+2)/2 | (N-1)(N+4)/(2N) |

Test: SU(3) fundamental: C_2(fund) = 4/3. Correct.

## Anomaly Coefficient Convention

A(R) = Tr_R(T^a {T^b, T^c}) normalised so that A(fund) = 1 for SU(N).

| Representation | A(R) |
| -------------- | ---- |
| Fundamental | 1 |
| Antifundamental | -1 |
| Adjoint | 2N |
| Antisymmetric_2 | N-4 |
| Symmetric_2 | N+4 |

**Important:** A(R) = 0 for real representations (adjoint of SU(2), adjoint of SU(N) for the cubic anomaly d_{abc}). Do not confuse the cubic anomaly coefficient A(R) with the Dynkin index T(R) — they are different quantities.

## Beta Function Convention

b_0 = (11N_c - 2N_f)/3 for SU(N_c) with N_f Dirac fundamental flavours.

Equivalently: b_0 = (11/3)T(adj) - (4/3) N_f T(fund) with T(fund) = 1/2.

- b_0 > 0: asymptotically free
- Loss of asymptotic freedom: N_f = 11N_c/2
- Beta function: mu d(alpha_s)/d(mu) = -b_0 alpha_s^2/(2pi) + ...

Test: SU(3), N_f = 6 Dirac: b_0 = (33 - 12)/3 = 7 > 0. Correct.

## Coupling Convention

alpha_s = g_s^2 / (4 pi).

At M_Z: alpha_s(M_Z) ~ 0.118; alpha_em ~ 1/137.

## Renormalisation Scheme

- MS-bar for perturbative running
- Holomorphic scheme for SUSY exact results (NSVZ beta function)

## Spinor Convention

- **Weyl (two-component) spinors** for SUSY content and anomaly matching
- **Dirac (four-component) spinors** for physical SM quarks/leptons

Test: N_f Dirac flavours = N_f pairs (Q_i, Q-tilde_i) of Weyl fermions.
SQCD has 2N_f Weyl fermions in the fundamental.

## Fermion Counting Convention — N_f

**PEDAGOGICAL NOTE: This convention requires explicit attention in lectures, especially when transitioning between N=2 and N=1 descriptions.**

N_f counts the number of **Dirac flavour pairs** (Q_i, Q-tilde_i) in SQCD, i = 1,...,N_f. Each pair contains 2 Weyl fermions.

When counting Weyl fermions explicitly, state "N_f Weyl".

### N=2 counting (Lecture 4 — special care required)

In N=2 language:
- Each **hypermultiplet** contains 2 N=1 chiral multiplets: (Q, Q-tilde)
- The **N=2 vector multiplet** contains 1 N=1 vector + 1 N=1 chiral (adjoint)
- The adjoint chiral from the vector multiplet is NOT counted in N_f

When breaking N=2 → N=1:
- N_f hypermultiplets → N_f pairs of N=1 chirals (Q_i, Q-tilde_i) PLUS 1 adjoint chiral Phi from the vector
- The N=1 superpotential includes W = sqrt(2) Q Phi Q-tilde from the N=2 structure
- The adjoint Phi contributes to the beta function but is NOT a "flavour"

| Language | N_f meaning | Beta function contribution from matter |
| -------- | ----------- | -------------------------------------- |
| N=2 | Number of hypermultiplets | b_0 = 2N_c - 2N_f T(fund) = 2N_c - N_f |
| N=1 (from N=2) | Number of chiral pairs | b_0 = 3N_c - N_f - N_c = 2N_c - N_f (same, as it must be) |

Test: SU(2) with N_f = 4 hypers: b_0 = 4 - 4 = 0 (conformal). Correct.

**A table showing this decomposition explicitly is REQUIRED in Lecture 4.**

## Conformal Window

SUSY (exact, Seiberg): 3N_c/2 < N_f < 3N_c for SU(N_c) with N_f Dirac pairs.

Non-SUSY: lower bound debated (~8-12 for SU(3)); upper bound at 11N_c/2 (loss of AF).

Test: SU(3) SUSY window: 4.5 < N_f < 9.

## Covariant Derivative

D_mu = partial_mu - ig A_mu^a T^a.

Consequences:
- [D_mu, D_nu] = -ig F_{mu nu}
- F_{mu nu} = partial_mu A_nu - partial_nu A_mu - ig[A_mu, A_nu]
- QCD vertex rule: -ig gamma^mu T^a

Note: Peskin-Schroeder QED uses D = partial + ieA (e > 0). For QCD they match our convention.

## Levi-Civita

epsilon^{0123} = +1.

With mostly-minus metric: epsilon_{0123} = +1.

## Gamma Matrices

Weyl (chiral) basis. Clifford algebra: {gamma^mu, gamma^nu} = 2 eta^{mu nu}.

gamma^5 = i gamma^0 gamma^1 gamma^2 gamma^3.

Test: Tr(gamma^mu gamma^nu) = 4 eta^{mu nu}; Tr(gamma^5) = 0.

## Index Convention

- Greek mu, nu, rho, sigma = 0,1,2,3 (spacetime)
- Latin a,b,c = 1,...,N^2-1 (gauge group adjoint)
- Latin i,j = 1,...,N_f (flavour; context-disambiguated from spatial)
- Latin i,j,k = 1,2,3 (spatial, when no flavour indices present)

## R-Charge Convention

R[Q] = 1 - N_c/N_f = (N_f - N_c)/N_f (non-anomalous R-symmetry for massless SQCD).

Test: R[W_mag] = R[M] + R[q] + R[q-tilde] = 2(N_f-N_c)/N_f + 2N_c/N_f = 2. Correct.

## Meson Field Convention

Electric theory: M^i_j = Q^i Q-tilde_j / Lambda (composite, dimension [mass]).

Magnetic theory: M is elementary N_f x N_f matrix with [M] = [mass].

Magnetic superpotential: W_mag = (1/mu) M q q-tilde.

R[M] = 2(N_f - N_c)/N_f.

## Representation Labelling

Dimension notation with overbar for conjugates: N, N-bar, adj, antisym_2, sym_2.

Dynkin labels in parentheses for disambiguation: e.g., (1,0,...,0) for fundamental.

Young tableaux in exercises.

Test: SU(3): fund = 3 = (1,0); antifund = 3-bar = (0,1); adj = 8 = (1,1); antisym_2 = 3-bar = (0,1).

## Reference Convention Map

| Reference | Conventions | Match? |
| --------- | ----------- | ------ |
| Seiberg hep-th/9411149 | T(fund)=1/2, Weyl, mostly-minus, D=partial-igA | Yes |
| Intriligator-Seiberg hep-th/9509066 | Same as Seiberg | Yes |
| Peskin-Schroeder | T(fund)=1/2, mostly-minus | Yes (QCD) |
| Terning textbook | T(fund)=1/2, Weyl basis, mostly-minus | Yes |
| Sannino 2407.17281 | TBD — to be verified during Phase 4 | TBD |
| Csaki-Terning 1106.3074 | SUSY standard | Expected match |

## Cross-Convention Consistency (Verified)

All convention pairs checked compatible:
- Metric + propagator: i/(k^2 - m^2 + i epsilon) with k^2 = E^2 - **p**^2. OK.
- D = partial - igA + vertex rule -ig gamma^mu T^a. OK.
- T(fund)=1/2 + b_0 = (11N-2N_f)/3. OK.
- epsilon^{0123}=+1 + gamma^5 = i gamma^0...gamma^3. OK.
- R-charge + superpotential R[W]=2. OK.

---

_Established: 2026-03-20_
_Convention source: Seiberg hep-th/9411149_
