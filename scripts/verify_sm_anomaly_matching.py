#!/usr/bin/env python3
"""
VALD-01: Symbolic verification of anomaly matching for the dualised SM.

Computes all 6 independent anomaly coefficients for SU(3)_c x SU(2)_L x U(1)_Y
on both the electric and magnetic sides of the conjectured non-SUSY duality, and
verifies exact matching as polynomial identities in n_g (number of generations).

Electric theory:  SU(2n_g - 4) with N_f = 2n_g Dirac flavours + adjoint Weyl fermion,
                  plus elementary lepton fields L, L-tilde.

Magnetic theory:  SU(3)_c with magnetic quarks (q, q-tilde), leptons (l, l-tilde),
                  gaugino (lambda_m), mesino (M), and scalars (phi, phi-tilde, Phi_H).
                  Only fermions contribute to anomalies.

Duality map: X = N_f - N = 2n_g - (2n_g - 4) = 4, with SU(4)_PS => SU(3)_c x U(1)_{B-L}.
For n_g = 3 specifically: N = 2, N_f = 6, X = 4 (Pati-Salam group).

The key result is: all anomaly coefficients vanish on BOTH sides (0 = 0 matching),
because the magnetic theory has vector-like fermion content under the SM gauge group,
and the electric theory inherits this via factorisation through SU(2)_el multiplicities.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA

Conventions:
    T(fund) = 1/2 per Weyl fermion
    A(fund) = 1, A(antifund) = -1 (cubic anomaly coefficient)
    Hypercharge: Y = T_R^3 + Q_V/6  (Cacciapaglia-Sannino 2407.17281 Eq. 6)
    N_f = 2 * n_g (number of Dirac flavour pairs)
    Electric gauge group: SU(2n_g - 4)

References:
    Cacciapaglia and Sannino, arXiv:2407.17281 (Tables I-II: field content)
    Sannino, arXiv:1102.5100 (Tables III-IV: electric theory field content)
    Lecture 7 (this project): explicit anomaly computation
"""

import sys
from sympy import symbols, simplify, Rational, expand, Symbol

# ============================================================
# Symbols
# ============================================================
n_g = symbols('n_g', positive=True, integer=True)
N_f = 2 * n_g          # number of Dirac flavour pairs
N = 2 * n_g - 4        # electric gauge group rank SU(N)
X = N_f - N            # magnetic gauge group rank = 4 (always)

# ============================================================
# Convention constants
# ============================================================
T_fund = Rational(1, 2)    # Dynkin index T(fund) = 1/2
T_adj_su3 = 3              # T(adj) for SU(3) = N = 3
A_fund = 1                 # Cubic anomaly A(fund) = 1
A_antifund = -1            # A(antifund) = -1
A_adj = 0                  # A(adj) = 0 (adjoint is real for SU(N))


# ============================================================
# Magnetic theory field content
# ============================================================
# Under SU(3)_c x SU(2)_L x U(1)_Y, the magnetic FERMIONS are:
#
# From Table II bottom block of 2407.17281 and Lecture 7 Table 6:
#
# SM quarks (from q, q-tilde decomposition):
#   q_L^i :  (3, 2, +1/6)  x n_g generations
#   u_R^i :  (3, 1, +2/3)  x n_g generations
#   d_R^i :  (3, 1, -1/3)  x n_g generations
#
# Conjugate quarks:
#   q-tilde_L^i :  (3-bar, 2, -1/6) x n_g generations
#   u-tilde_R^i :  (3-bar, 1, -2/3) x n_g generations
#   d-tilde_R^i :  (3-bar, 1, +1/3) x n_g generations
#
# SM leptons (from l, l-tilde):
#   ell_L^i :  (1, 2, -1/2)  x n_g generations
#   nu_R^i  :  (1, 1,  0)    x n_g generations
#   e_R^i   :  (1, 1, -1)    x n_g generations
#
# Conjugate leptons:
#   ell-tilde_L^i : (1, 2, +1/2)  x n_g generations
#   nu-tilde_R^i  : (1, 1,  0)    x n_g generations
#   e-tilde_R^i   : (1, 1, +1)    x n_g generations
#
# Gaugino (from lambda_m):
#   lambda_m : (8, 1, 0)   x 1  (one Weyl fermion in adjoint of SU(3)_c)
#
# Mesino (from M): transforms as (F, F-bar) under SU(N_f)_L x SU(N_f)_R
#   with Q_V = 0, so Y = T_R^3 + Q_V/6 = T_R^3.
#   Under SU(N_f)_L => SU(n_g) x SU(2)_L and SU(N_f)_R => SU(n_g) x SU(2)_R:
#   M decomposes into components:
#     M(2_L, 2_R):  n_g^2 copies of (1, 2) with Y = +1/2 and (1, 2) with Y = -1/2
#     M(2_L, 1_R):  n_g^2 copies of (1, 2) with Y = 0
#     M(1_L, 2_R):  n_g^2 copies of (1, 1) with Y = +1/2 and (1, 1) with Y = -1/2
#     M(1_L, 1_R):  n_g^2 copies of (1, 1) with Y = 0
#   The key point: SU(2)_R pairs enforce cancellation in all anomaly coefficients.
#
# Scalars (phi, phi-tilde, Phi_H): DO NOT contribute to anomalies.

# Each magnetic fermion is specified as:
#   (name, SU3_dim, SU2_dim, Y, A_colour, T_colour, multiplicity)
# where A_colour is the cubic anomaly coeff for SU(3), T_colour is Dynkin index.
# multiplicity is in units of Weyl fermions.

# For the mesino decomposition, we need to be more careful.
# M is in (F, F-bar) of SU(N_f)_L x SU(N_f)_R = SU(2n_g)_L x SU(2n_g)_R.
# Under SU(2n_g) => SU(n_g) x SU(2), the fundamental 2n_g => (n_g, 2).
# So F of SU(2n_g)_L = (n_g, 2) under SU(n_g)_gen x SU(2)_L.
# And F-bar of SU(2n_g)_R = (n_g-bar, 2-bar) = (n_g-bar, 2) under SU(n_g)_gen x SU(2)_R.
# (Since SU(2) fund = antifund.)
#
# Therefore M decomposes as:
#   M = (n_g, 2)_L x (n_g-bar, 2)_R
# The SU(2)_L x SU(2)_R content: 2_L x 2_R = (2_L, 2_R)
# with generation content: n_g x n_g-bar = n_g^2 copies (adjoint + singlet of SU(n_g)).
#
# Under SU(2)_R, the 2_R has T_R^3 = +1/2 and -1/2.
# Y = T_R^3 + Q_V/6, and Q_V = 0 for mesino, so Y = T_R^3.
#
# Mesino SU(2)_L doublet components (from 2_L piece):
#   For T_R^3 = +1/2: n_g^2 copies of (1, 2, +1/2)
#   For T_R^3 = -1/2: n_g^2 copies of (1, 2, -1/2)
# These are colour singlets.
#
# Total mesino: 2n_g x 2n_g = 4n_g^2 = (2n_g)^2 Weyl components.
# Check: n_g^2 copies of (2_L, 2_R) = n_g^2 * 2 * 2 = 4n_g^2. Correct.


def define_magnetic_fermions(ng):
    """
    Define all magnetic Weyl fermions with SM quantum numbers.

    Returns list of (name, su3_dim, su2_dim, Y, multiplicity) tuples,
    where multiplicity is the number of Weyl fermions of that type
    (as a sympy expression in n_g, or an integer).
    """
    fermions = []

    # --- SM quarks from q ---
    fermions.append(("q_L", 3, 2, Rational(1, 6), ng))
    fermions.append(("u_R", 3, 1, Rational(2, 3), ng))
    fermions.append(("d_R", 3, 1, Rational(-1, 3), ng))

    # --- Conjugate quarks from q-tilde ---
    # SU(3)_c antifundamental = 3-bar (dim 3 but conjugate)
    fermions.append(("qtilde_L", -3, 2, Rational(-1, 6), ng))
    fermions.append(("utilde_R", -3, 1, Rational(-2, 3), ng))
    fermions.append(("dtilde_R", -3, 1, Rational(1, 3), ng))

    # --- SM leptons from l ---
    fermions.append(("ell_L", 1, 2, Rational(-1, 2), ng))
    fermions.append(("nu_R", 1, 1, 0, ng))
    fermions.append(("e_R", 1, 1, -1, ng))

    # --- Conjugate leptons from l-tilde ---
    fermions.append(("elltilde_L", 1, 2, Rational(1, 2), ng))
    fermions.append(("nutilde_R", 1, 1, 0, ng))
    fermions.append(("etilde_R", 1, 1, 1, ng))

    # --- Gaugino lambda_m ---
    # Adjoint of SU(3)_c = 8, SU(2)_L singlet, Y = 0
    fermions.append(("lambda_m", 8, 1, 0, 1))

    # --- Mesino M ---
    # Colour singlet. Decomposes into SU(2)_L doublets with Y = T_R^3.
    # n_g^2 copies of (1, 2, +1/2) and n_g^2 copies of (1, 2, -1/2).
    fermions.append(("M_doublet_Yp", 1, 2, Rational(1, 2), ng**2))
    fermions.append(("M_doublet_Ym", 1, 2, Rational(-1, 2), ng**2))

    return fermions


def define_electric_fermions(ng):
    """
    Define all electric Weyl fermions decomposed under SU(3)_c x SU(2)_L x U(1)_Y.

    The electric theory has gauge group SU(N) = SU(2n_g - 4).  Its fermions
    carry SU(N)_el quantum numbers AND global SU(N_f)_L x SU(N_f)_R x U(1)_V
    quantum numbers.  SU(3)_c x SU(2)_L x U(1)_Y is a subgroup of the global
    symmetry (gauged only in the magnetic/IR description).

    From Lecture 7, Eq. (7.48) and Section 5.7: the SM quantum numbers of the
    electric fermions are IDENTICAL to those of the corresponding magnetic
    fermions, but multiplied by dim(R_SU(N)_el):

      p  (fund of SU(N)_el, dim = N):
        Same SM content as magnetic quarks q, with N-fold multiplicity.
      p-tilde  (antifund of SU(N)_el, dim = N):
        Same SM content as magnetic quarks q-tilde, with N-fold multiplicity.
      lambda  (adjoint of SU(N)_el, dim = N^2 - 1):
        Complete singlet under SU(3)_c x SU(2)_L x U(1)_Y.
        (It is in the adjoint of SU(N)_el, but singlet of SU(N_f)_L x SU(N_f)_R
        with Q_V = 0, so Y = T_R^3 + Q_V/6 = 0.)
      L  (singlet of SU(N)_el):
        Same SM content as magnetic leptons l, multiplicity 1.
      L-tilde  (singlet of SU(N)_el):
        Same SM content as magnetic l-tilde, multiplicity 1.

    The factorisation result is:
      A_el = dim(R_SU(N)_el) x A_SM = dim(R) x 0 = 0
    for all 6 anomaly conditions, because the SM-decomposed content is
    vector-like on both the quark and lepton sectors.
    """
    Nval = 2 * ng - 4   # electric gauge group SU(N)

    fermions = []

    # p: fund of SU(N)_el, decomposes under SM like the magnetic quarks
    # but with N-fold SU(N)_el multiplicity
    # Same SM quantum numbers as q from the magnetic side
    fermions.append(("p->q_L", 3, 2, Rational(1, 6), ng * Nval))
    fermions.append(("p->u_R", 3, 1, Rational(2, 3), ng * Nval))
    fermions.append(("p->d_R", 3, 1, Rational(-1, 3), ng * Nval))

    # p-tilde: antifund of SU(N)_el (dim = N), same SM as q-tilde
    fermions.append(("ptilde->qtilde_L", -3, 2, Rational(-1, 6), ng * Nval))
    fermions.append(("ptilde->utilde_R", -3, 1, Rational(-2, 3), ng * Nval))
    fermions.append(("ptilde->dtilde_R", -3, 1, Rational(1, 3), ng * Nval))

    # lambda: adjoint of SU(N)_el, complete singlet under SM
    # (N^2 - 1) Weyl fermions, all with (1, 1, 0)
    fermions.append(("lambda", 1, 1, 0, Nval**2 - 1))

    # L: singlet of SU(N)_el, same SM as magnetic leptons l
    fermions.append(("L->ell_L", 1, 2, Rational(-1, 2), ng))
    fermions.append(("L->nu_R", 1, 1, 0, ng))
    fermions.append(("L->e_R", 1, 1, -1, ng))

    # L-tilde: singlet of SU(N)_el, same SM as l-tilde
    fermions.append(("Ltilde->elltilde_L", 1, 2, Rational(1, 2), ng))
    fermions.append(("Ltilde->nutilde_R", 1, 1, 0, ng))
    fermions.append(("Ltilde->etilde_R", 1, 1, 1, ng))

    return fermions


# ============================================================
# Anomaly coefficient computation
# ============================================================

def cubic_anomaly_su3(dim_su3):
    """Return A(R) for SU(3) representation given its dimension (signed: -3 for antifund)."""
    if dim_su3 == 3:
        return A_fund       # = 1
    elif dim_su3 == -3:
        return A_antifund   # = -1
    elif dim_su3 == 8:
        return 0            # adjoint is real
    elif dim_su3 == 1:
        return 0            # singlet
    else:
        raise ValueError(f"Unknown SU(3) representation dim = {dim_su3}")


def dynkin_index_su3(dim_su3):
    """Return T(R) for SU(3) representation."""
    if dim_su3 == 3:
        return T_fund       # = 1/2
    elif dim_su3 == -3:
        return T_fund       # = 1/2 (same for antifund)
    elif dim_su3 == 8:
        return T_adj_su3    # = 3
    elif dim_su3 == 1:
        return 0
    else:
        raise ValueError(f"Unknown SU(3) representation dim = {dim_su3}")


def abs_dim_su3(dim_su3):
    """Return absolute dimension of SU(3) representation."""
    if dim_su3 in (3, -3):
        return 3
    elif dim_su3 == 8:
        return 8
    elif dim_su3 == 1:
        return 1
    else:
        raise ValueError(f"Unknown SU(3) representation dim = {dim_su3}")


def dynkin_index_su2(dim_su2):
    """Return T(R) for SU(2) representation."""
    if dim_su2 == 2:
        return T_fund       # = 1/2
    elif dim_su2 == 1:
        return 0
    elif dim_su2 == 3:
        return 2            # T(adj) for SU(2) = N = 2
    else:
        raise ValueError(f"Unknown SU(2) representation dim = {dim_su2}")


def compute_anomaly_coefficients(fermions, label):
    """
    Compute all 6 anomaly coefficients for SU(3)_c x SU(2)_L x U(1)_Y.

    fermions: list of (name, su3_dim, su2_dim, Y, multiplicity) tuples.
    label: string label for printing.

    Returns dict: {condition_name: value}
    """
    results = {}

    # (i) SU(3)^3: sum A(R_colour) * dim(R_weak) * multiplicity
    su3_cubed = 0
    for name, su3, su2, Y, mult in fermions:
        su3_cubed += cubic_anomaly_su3(su3) * su2 * mult
    results['SU(3)^3'] = simplify(expand(su3_cubed))

    # (ii) SU(2)^3: trivially zero (d_abc = 0 for SU(2))
    results['SU(2)^3'] = 0

    # (iii) SU(3)^2 U(1)_Y: sum Y * T(R_colour) * dim(R_weak) * multiplicity
    su3sq_u1 = 0
    for name, su3, su2, Y, mult in fermions:
        su3sq_u1 += Y * dynkin_index_su3(su3) * su2 * mult
    results['SU(3)^2 U(1)_Y'] = simplify(expand(su3sq_u1))

    # (iv) SU(2)^2 U(1)_Y: sum Y * T(R_weak) * dim(R_colour) * multiplicity
    # Only SU(2)_L non-singlets contribute (T(1) = 0).
    su2sq_u1 = 0
    for name, su3, su2, Y, mult in fermions:
        su2sq_u1 += Y * dynkin_index_su2(su2) * abs_dim_su3(su3) * mult
    results['SU(2)^2 U(1)_Y'] = simplify(expand(su2sq_u1))

    # (v) U(1)_Y^3: sum Y^3 * dim(R_colour) * dim(R_weak) * multiplicity
    u1_cubed = 0
    for name, su3, su2, Y, mult in fermions:
        u1_cubed += Y**3 * abs_dim_su3(su3) * su2 * mult
    results['U(1)_Y^3'] = simplify(expand(u1_cubed))

    # (vi) U(1)_Y-gravitational: sum Y * dim(R_colour) * dim(R_weak) * multiplicity
    u1_grav = 0
    for name, su3, su2, Y, mult in fermions:
        u1_grav += Y * abs_dim_su3(su3) * su2 * mult
    results['U(1)_Y-grav'] = simplify(expand(u1_grav))

    return results


# ============================================================
# SM-only subset check
# ============================================================


def define_sm_only_magnetic_fermions(ng):
    """
    Define the SM-ONLY subset of the magnetic theory.

    The full magnetic theory has vector-like pairs:
        (q_L, qtilde_L), (u_R, utilde_R), (d_R, dtilde_R),
        (ell_L, elltilde_L), (e_R, etilde_R), (nu_R, nutilde_R)
    plus the gaugino and mesino.

    The PHYSICAL SM content, expressed as left-handed Weyl fermions in
    the standard textbook convention (all-left-handed), consists of:

        q_L:     (3, 2, +1/6)    -- left-handed quark doublet
        u_R^c:   (3-bar, 1, -2/3) -- left-handed conjugate of right-handed u
        d_R^c:   (3-bar, 1, +1/3) -- left-handed conjugate of right-handed d
        ell_L:   (1, 2, -1/2)     -- left-handed lepton doublet
        e_R^c:   (1, 1, +1)       -- left-handed conjugate of right-handed e
        nu_R^c:  (1, 1, 0)        -- left-handed conjugate of right-handed nu

    In the magnetic theory table, these correspond to:
        q_L from the q sector (left-handed doublets)
        utilde_R from the qtilde sector = (3-bar, 1, -2/3) = SM u_R^c
        dtilde_R from the qtilde sector = (3-bar, 1, +1/3) = SM d_R^c
        ell_L from the l sector
        etilde_R from the ltilde sector = (1, 1, +1)       = SM e_R^c
        nutilde_R from the ltilde sector = (1, 1, 0)       = SM nu_R^c

    The "extra" vector-like partners (u_R, d_R, qtilde_L, etc.), the
    gaugino, and the mesino are all removed.

    Standard SM anomaly cancellation requires this all-left-handed content.
    """
    fermions = []

    # SM quarks (all left-handed Weyl, per the textbook convention)
    fermions.append(("q_L",      3,  2, Rational(1, 6),   ng))   # from q
    fermions.append(("utilde_R", -3, 1, Rational(-2, 3),  ng))   # from qtilde (= SM u_R^c)
    fermions.append(("dtilde_R", -3, 1, Rational(1, 3),   ng))   # from qtilde (= SM d_R^c)

    # SM leptons (all left-handed Weyl)
    fermions.append(("ell_L",      1,  2, Rational(-1, 2),  ng))   # from l
    fermions.append(("etilde_R",   1,  1, 1,                ng))   # from ltilde (= SM e_R^c)
    fermions.append(("nutilde_R",  1,  1, 0,                ng))   # from ltilde (= SM nu_R^c)

    return fermions


# ============================================================
# Main verification
# ============================================================

def _subs_ng(expr, ng_val):
    """Substitute n_g into expr, handling plain ints that lack .subs()."""
    from sympy import Integer
    if isinstance(expr, (int, float)):
        return int(expr)
    return int(expr.subs(n_g, ng_val))


def main():
    print("=" * 72)
    print("VALD-01: Dualised SM Anomaly Matching Verification")
    print("        SU(3)_c x SU(2)_L x U(1)_Y")
    print("=" * 72)
    print()
    print("Conventions:")
    print("  T(fund) = 1/2, A(fund) = 1, A(antifund) = -1")
    print("  Hypercharge: Y = T_R^3 + Q_V/6")
    print(f"  N_f = 2*n_g, N = 2*n_g - 4, X = N_f - N = 4")
    print()

    all_pass = True

    # ================================================================
    # PART 1: Symbolic anomaly matching (magnetic side)
    # ================================================================
    print("--- Part 1: Magnetic theory anomaly coefficients (symbolic in n_g) ---")
    print()

    mag_fermions = define_magnetic_fermions(n_g)
    mag_results = compute_anomaly_coefficients(mag_fermions, "magnetic")

    mag_pass = True
    for cond, val in mag_results.items():
        status = "PASS" if val == 0 else "FAIL"
        if val != 0:
            mag_pass = False
            all_pass = False
        print(f"  [{status}]  {cond:25s}  =  {val}")
    print()

    if mag_pass:
        print("  All magnetic anomaly coefficients vanish (vector-like structure).")
    else:
        print("  WARNING: Some magnetic anomaly coefficients are non-zero!")
    print()

    # ================================================================
    # PART 2: Symbolic anomaly matching (electric side)
    # ================================================================
    print("--- Part 2: Electric theory anomaly coefficients (symbolic in n_g) ---")
    print()

    el_fermions = define_electric_fermions(n_g)
    el_results = compute_anomaly_coefficients(el_fermions, "electric")

    el_pass = True
    for cond, val in el_results.items():
        status = "PASS" if val == 0 else "FAIL"
        if val != 0:
            el_pass = False
            all_pass = False
        print(f"  [{status}]  {cond:25s}  =  {val}")
    print()

    if el_pass:
        print("  All electric anomaly coefficients vanish (factorisation through SU(N)_el).")
    else:
        print("  WARNING: Some electric anomaly coefficients are non-zero!")
    print()

    # ================================================================
    # PART 3: Anomaly matching (electric - magnetic = 0)
    # ================================================================
    print("--- Part 3: Anomaly matching (electric - magnetic = 0) ---")
    print()

    match_pass = True
    conditions = ['SU(3)^3', 'SU(2)^3', 'SU(3)^2 U(1)_Y',
                  'SU(2)^2 U(1)_Y', 'U(1)_Y^3', 'U(1)_Y-grav']
    for cond in conditions:
        diff = simplify(expand(el_results[cond] - mag_results[cond]))
        status = "PASS" if diff == 0 else "FAIL"
        if diff != 0:
            match_pass = False
            all_pass = False
        print(f"  [{status}]  {cond:25s}  diff = {diff}")
    print()

    if match_pass:
        print("  Anomaly matching verified: electric = magnetic = 0 for all 6 conditions.")
    else:
        print("  WARNING: Anomaly matching failed for some conditions!")
    print()

    # ================================================================
    # PART 4: Numerical spot-check at n_g = 3
    # ================================================================
    print("--- Part 4: Numerical spot-check at n_g = 3 (physical SM) ---")
    print()

    ng_val = 3
    Nf_val = 2 * ng_val
    N_val = 2 * ng_val - 4
    print(f"  n_g = {ng_val}, N_f = {Nf_val}, N = {N_val} (SU({N_val})_el), X = {Nf_val - N_val}")
    print()

    num_pass = True
    for cond in conditions:
        mag_num = _subs_ng(mag_results[cond], ng_val)
        el_num = _subs_ng(el_results[cond], ng_val)
        diff_num = el_num - mag_num
        status = "PASS" if diff_num == 0 else "FAIL"
        if diff_num != 0:
            num_pass = False
            all_pass = False
        print(f"  [{status}]  {cond:25s}  mag = {mag_num:3d}  el = {el_num:3d}  diff = {diff_num}")
    print()

    if num_pass:
        print("  All anomaly coefficients are exactly zero at n_g = 3.")
    else:
        print("  WARNING: Numerical spot-check failed!")
    print()

    # ================================================================
    # PART 5: SM anomaly cancellation as subset check
    # ================================================================
    print("--- Part 5: SM anomaly cancellation (subset check) ---")
    print()
    print("  Extracting the physical SM content from the magnetic theory:")
    print("    q_L from q, utilde_R and dtilde_R from qtilde (= SM u_R^c, d_R^c),")
    print("    ell_L from l, etilde_R and nutilde_R from ltilde (= SM e_R^c, nu_R^c).")
    print("  Removing all extra states (vector-like partners, gaugino, mesino).")
    print("  Verifying standard SM anomaly cancellation in the all-left-handed convention.")
    print()

    sm_fermions = define_sm_only_magnetic_fermions(n_g)
    sm_results = compute_anomaly_coefficients(sm_fermions, "SM-only")

    sm_pass = True
    for cond in conditions:
        val = sm_results[cond]
        status = "PASS" if val == 0 else "FAIL"
        if val != 0:
            sm_pass = False
            all_pass = False
        print(f"  [{status}]  {cond:25s}  =  {val}")
    print()

    if sm_pass:
        print("  SM anomaly cancellation recovered: all conditions vanish for SM-only content.")
    else:
        print("  WARNING: SM anomaly cancellation failed -- check field content!")
    print()

    # Also check SM at n_g = 3 numerically
    print("  Numerical check at n_g = 3:")
    sm_num_pass = True
    for cond in conditions:
        val_num = _subs_ng(sm_results[cond], 3)
        status = "PASS" if val_num == 0 else "FAIL"
        if val_num != 0:
            sm_num_pass = False
            all_pass = False
        print(f"  [{status}]  {cond:25s}  =  {val_num}")
    print()

    # ================================================================
    # PART 6: Additional spot-checks at other n_g values
    # ================================================================
    print("--- Part 6: Additional numerical spot-checks ---")
    print()

    extra_ng_values = [4, 5, 6]
    for ng_val in extra_ng_values:
        Nf_val = 2 * ng_val
        N_val = 2 * ng_val - 4
        print(f"  n_g = {ng_val}: SU({N_val})_el, N_f = {Nf_val}, X = {Nf_val - N_val}")
        extra_pass = True
        for cond in conditions:
            mag_num = _subs_ng(mag_results[cond], ng_val)
            el_num = _subs_ng(el_results[cond], ng_val)
            diff_num = el_num - mag_num
            if diff_num != 0:
                extra_pass = False
                all_pass = False
                print(f"    FAIL  {cond}: diff = {diff_num}")
        if extra_pass:
            print(f"    All conditions: PASS (0 = 0)")
        print()

    # ================================================================
    # FINAL SUMMARY
    # ================================================================
    print("=" * 72)
    if all_pass:
        print("ALL CHECKS PASSED")
        print()
        print("Summary:")
        print("  Magnetic anomaly coefficients:   6/6 vanish symbolically (vector-like)")
        print("  Electric anomaly coefficients:   6/6 vanish symbolically (factorisation)")
        print("  Anomaly matching (el - mag):     6/6 conditions give 0 = 0")
        print("  Numerical at n_g = 3:            6/6 match (all zero)")
        print(f"  Extra spot-checks (n_g = {extra_ng_values}):  all pass")
        print("  SM subset check:                 6/6 SM-only conditions vanish")
        print()
        print("VALD-01 COMPLETE: anomaly matching verified for dualised SM.")
    else:
        print("SOME CHECKS FAILED")
        if not mag_pass:
            print("  FAILED: Magnetic anomaly coefficients")
        if not el_pass:
            print("  FAILED: Electric anomaly coefficients")
        if not match_pass:
            print("  FAILED: Anomaly matching (el - mag)")
        if not num_pass:
            print("  FAILED: Numerical spot-check at n_g = 3")
        if not sm_pass:
            print("  FAILED: SM anomaly cancellation")
    print("=" * 72)

    return 0 if all_pass else 1


if __name__ == '__main__':
    sys.exit(main())
