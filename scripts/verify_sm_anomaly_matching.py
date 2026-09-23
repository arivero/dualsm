#!/usr/bin/env python3
"""
VALD-01: Anomaly matching for the dualised SM under SU(3)_c x SU(2)_L x U(1)_Y.

The script follows the QCD-sector route of Lecture 7, Sec. 5, which
transcribes Tables I-II of Cacciapaglia and Sannino (arXiv:2407.17281):

Electric theory:  SU(3)_el with N_f = 2 n_g = 6 Dirac flavours (Q, Q-tilde),
                  one adjoint Weyl fermion lambda and elementary leptons
                  (L, L-tilde).  It has no colour: SU(2)_L x U(1)_Y is a
                  subgroup of its flavour symmetry SU(6)_L x SU(6)_R x U(1)_V.
Magnetic theory:  SU(3)_c (X = N_f - N = 3) with magnetic quarks (q, q-tilde),
                  leptons (l, l-tilde), gaugino lambda_m, mesino M and the
                  scalars phi, phi-tilde, Phi_H, which carry no anomaly.

Parts:
  1. Magnetic theory: the six SM gauge anomaly conditions vanish as
     polynomials in n_g.  The fermions are the chiral SM content of each
     generation (q-tilde and l-tilde hold the left-handed conjugates of
     u_R, d_R, e_R, nu_R), the gaugino (8, 1, 0) and the mesino, whose
     n_g^2 doublets with Y = +1/2 pair with n_g^2 doublets with Y = -1/2.
     The SM part cancels generation by generation, the textbook
     non-trivial cancellation.
  2. Witten's global SU(2)_L anomaly: the number of doublets is even.
  3. Electric theory at n_g = 3: the flavour conditions SU(2)_L^2 U(1)_Y,
     U(1)_Y^3 and U(1)_Y-gravity equal the magnetic values.  SU(3)_c^3 and
     SU(3)_c^2 U(1)_Y have no electric counterpart, because colour is the
     magnetic gauge group.  Lecture 7's tables have N = X = 3, so Parts 3
     and 4 are evaluated at n_g = 3.
  4. The 't Hooft anomalies of the whole flavour symmetry
     SU(6)_L x SU(6)_R x U(1)_V x U(1)_AF, computed from Lecture 7's
     electric and magnetic tables, match (twelve coefficients).
  5. The SM content alone (no gaugino, no mesino) cancels all six conditions.
  6. Spot checks of Part 1 at n_g = 1, ..., 6.

Until 2026-09-23 the field list paired every SM field with a conjugate copy
of the same chirality (q_L with a (3bar, 2, -1/6), u_R with a (3bar, 1, -2/3),
...).  That vector-like content cancels every anomaly identically, so the
matching it reported was empty; the electric group was also taken from the
Pati-Salam route, SU(2 n_g - 4), while the magnetic content came from the
QCD-sector route.

Chirality: fermions are listed as (name, SU(3) rep, SU(2) dim, Y,
multiplicity, chirality).  A right-handed Weyl fermion (chirality -1) is
the conjugate of a left-handed one in the conjugate representation with
opposite charges, so every anomaly coefficient it contributes flips sign.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA

Conventions:
    T(fund) = 1/2 per Weyl fermion
    A(fund) = 1, A(antifund) = -1, A(adj) = 0 (cubic anomaly coefficient)
    Hypercharge: Y = T_R^3 + Q_V/6  (Cacciapaglia-Sannino 2407.17281 Eq. 6)
    N_f = 2 n_g (number of Dirac flavour pairs)

References:
    Cacciapaglia and Sannino, arXiv:2407.17281 (Tables I-II: field content)
    Lecture 7 (this project), Tables electric-SM, magnetic-SM and Sec. 5
"""

import sys
from sympy import symbols, simplify, Rational, expand

# ============================================================
# Symbols and constants
# ============================================================
n_g = symbols('n_g', positive=True, integer=True)

T_fund = Rational(1, 2)    # Dynkin index T(fund) = 1/2
T_adj_su3 = 3              # T(adj) for SU(3) = N = 3
A_fund = 1                 # Cubic anomaly A(fund) = 1
A_antifund = -1            # A(antifund) = -1
A_adj = 0                  # A(adj) = 0 (adjoint is real for SU(N))

L_HAND, R_HAND = 1, -1     # chirality factors
N_EL = 3                   # electric SU(3)_el of the QCD-sector route
NG_PHYS = 3                # Lecture 7's tables: N = X = 3, N_f = 6

CONDITIONS = ['SU(3)^3', 'SU(2)^3', 'SU(3)^2 U(1)_Y',
              'SU(2)^2 U(1)_Y', 'U(1)_Y^3', 'U(1)_Y-grav']
FLAVOUR_CONDITIONS = ['SU(2)^2 U(1)_Y', 'U(1)_Y^3', 'U(1)_Y-grav']


# ============================================================
# Field content under SU(3)_c x SU(2)_L x U(1)_Y
# ============================================================

def define_sm_fermions(ng):
    """Chiral SM content, n_g generations, textbook notation.

    In the magnetic theory q supplies q_L, q-tilde the left-handed
    conjugates of u_R and d_R, l supplies ell_L and l-tilde the
    conjugates of e_R and nu_R.
    """
    return [
        ("q_L",   3, 2, Rational(1, 6),  ng, L_HAND),
        ("u_R",   3, 1, Rational(2, 3),  ng, R_HAND),
        ("d_R",   3, 1, Rational(-1, 3), ng, R_HAND),
        ("ell_L", 1, 2, Rational(-1, 2), ng, L_HAND),
        ("e_R",   1, 1, -1,              ng, R_HAND),
        ("nu_R",  1, 1, 0,               ng, R_HAND),
    ]


def define_magnetic_fermions(ng):
    """Magnetic Weyl fermions: SM content, gaugino and mesino.

    Mesino M: (F, Fbar) of SU(2n_g)_L x SU(2n_g)_R with Q_V = 0, so
    Y = T_R^3.  Under SU(2n_g) -> SU(n_g)_gen x SU(2), F -> (n_g, 2), hence
    M = n_g^2 copies of (2_L, 2_R): n_g^2 doublets with Y = +1/2 and n_g^2
    with Y = -1/2 (4 n_g^2 Weyl components).
    """
    fermions = define_sm_fermions(ng)
    fermions.append(("lambda_m", 8, 1, 0, 1, L_HAND))
    fermions.append(("M_doublet_Yp", 1, 2, Rational(1, 2), ng**2, L_HAND))
    fermions.append(("M_doublet_Ym", 1, 2, Rational(-1, 2), ng**2, L_HAND))
    return fermions


def define_electric_fermions(ng, n_el=N_EL):
    """Electric Weyl fermions under the flavour subgroup SU(2)_L x U(1)_Y.

    The electric theory has no SU(3)_c; its SU(3)_el multiplicity n_el enters
    the multiplicities, and every field is an SM colour singlet.  All fields
    are left-handed, as in the tables:
      Q       (F of SU(3)_el, F of SU(6)_L, Q_V = +1): doublets, Y = +1/6
      Q-tilde (Fbar of SU(3)_el, Fbar of SU(6)_R, Q_V = -1): SU(2)_R
              doublets, i.e. SU(2)_L singlets with Y = +1/2 - 1/6 = +1/3 and
              -1/2 - 1/6 = -2/3
      lambda  (adjoint of SU(3)_el): SM singlet
      L       (F of SU(6)_L, Q_V = -3): doublets, Y = -1/2
      L-tilde (Fbar of SU(6)_R, Q_V = +3): singlets with Y = +1 and 0
    """
    return [
        ("Q",            1, 2, Rational(1, 6),  n_el * ng, L_HAND),
        ("Qtilde(+1/3)", 1, 1, Rational(1, 3),  n_el * ng, L_HAND),
        ("Qtilde(-2/3)", 1, 1, Rational(-2, 3), n_el * ng, L_HAND),
        ("lambda",       1, 1, 0,               n_el**2 - 1, L_HAND),
        ("L",            1, 2, Rational(-1, 2), ng, L_HAND),
        ("Ltilde(+1)",   1, 1, 1,               ng, L_HAND),
        ("Ltilde(0)",    1, 1, 0,               ng, L_HAND),
    ]


# ============================================================
# Anomaly coefficients under the SM group
# ============================================================

def cubic_anomaly_su3(dim_su3):
    """A(R) for an SU(3) representation given its dimension (-3 = antifund)."""
    return {3: A_fund, -3: A_antifund, 8: A_adj, 1: 0}[dim_su3]


def dynkin_index_su3(dim_su3):
    """T(R) for an SU(3) representation."""
    return {3: T_fund, -3: T_fund, 8: T_adj_su3, 1: 0}[dim_su3]


def abs_dim_su3(dim_su3):
    return abs(dim_su3)


def dynkin_index_su2(dim_su2):
    """T(R) for an SU(2) representation."""
    return {2: T_fund, 1: 0, 3: 2}[dim_su2]


def compute_anomaly_coefficients(fermions):
    """The six anomaly coefficients of SU(3)_c x SU(2)_L x U(1)_Y."""
    s = {c: 0 for c in CONDITIONS}
    for name, su3, su2, Y, mult, chi in fermions:
        s['SU(3)^3'] += chi * cubic_anomaly_su3(su3) * su2 * mult
        s['SU(3)^2 U(1)_Y'] += chi * Y * dynkin_index_su3(su3) * su2 * mult
        s['SU(2)^2 U(1)_Y'] += chi * Y * dynkin_index_su2(su2) * abs_dim_su3(su3) * mult
        s['U(1)_Y^3'] += chi * Y**3 * abs_dim_su3(su3) * su2 * mult
        s['U(1)_Y-grav'] += chi * Y * abs_dim_su3(su3) * su2 * mult
    s['SU(2)^3'] = 0      # d_abc = 0 for SU(2): no cubic anomaly
    return {c: simplify(expand(v)) for c, v in s.items()}


def count_doublets(fermions):
    """Number of SU(2)_L doublet Weyl fermions (colour components included)."""
    return simplify(expand(sum(abs_dim_su3(su3) * mult
                               for _, su3, su2, _, mult, _ in fermions if su2 == 2)))


def _at(expr, ng_val):
    return int(expr.subs(n_g, ng_val)) if hasattr(expr, 'subs') else int(expr)


# ============================================================
# Flavour-group 't Hooft anomalies (Lecture 7 tables, n_g = 3)
# ============================================================
# Each field: (name, gauge multiplicity, SU(6)_L rep, SU(6)_R rep, Q_V, Q_AF)
# with reps '1', 'F', 'Fb'.  Gauge multiplicity is the dimension of its
# SU(3)_el or SU(3)_c representation.

ELECTRIC_TABLE = [
    ("lambda",  8, '1', '1',  0, 1),
    ("Q",       3, 'F', '1',  1, Rational(-1, 2)),
    ("Qtilde",  3, '1', 'Fb', -1, Rational(-1, 2)),
    ("L",       1, 'F', '1', -3, 0),
    ("Ltilde",  1, '1', 'Fb', 3, 0),
]

MAGNETIC_TABLE = [
    ("lambda_m", 8, '1', '1',  0, 1),
    ("q",        3, 'Fb', '1', 1, Rational(-1, 2)),
    ("qtilde",   3, '1', 'F', -1, Rational(-1, 2)),
    ("l",        1, 'F', '1', -3, 0),
    ("ltilde",   1, '1', 'Fb', 3, 0),
    ("M",        1, 'F', 'Fb', 0, 0),
]

DIM6 = {'1': 1, 'F': 6, 'Fb': 6}
A6 = {'1': 0, 'F': 1, 'Fb': -1}
T6 = {'1': 0, 'F': Rational(1, 2), 'Fb': Rational(1, 2)}


def flavour_anomalies(table):
    a = {}
    rows = [(g, l, r, V, AF) for _, g, l, r, V, AF in table]
    a['SU(6)_L^3'] = sum(g * A6[l] * DIM6[r] for g, l, r, V, AF in rows)
    a['SU(6)_R^3'] = sum(g * A6[r] * DIM6[l] for g, l, r, V, AF in rows)
    a['SU(6)_L^2 U(1)_V'] = sum(g * T6[l] * DIM6[r] * V for g, l, r, V, AF in rows)
    a['SU(6)_R^2 U(1)_V'] = sum(g * T6[r] * DIM6[l] * V for g, l, r, V, AF in rows)
    a['SU(6)_L^2 U(1)_AF'] = sum(g * T6[l] * DIM6[r] * AF for g, l, r, V, AF in rows)
    a['SU(6)_R^2 U(1)_AF'] = sum(g * T6[r] * DIM6[l] * AF for g, l, r, V, AF in rows)
    n = {id(row): row[0] * DIM6[row[1]] * DIM6[row[2]] for row in rows}
    a['U(1)_V^3'] = sum(n[id(x)] * x[3]**3 for x in rows)
    a['U(1)_AF^3'] = sum(n[id(x)] * x[4]**3 for x in rows)
    a['U(1)_V^2 U(1)_AF'] = sum(n[id(x)] * x[3]**2 * x[4] for x in rows)
    a['U(1)_V U(1)_AF^2'] = sum(n[id(x)] * x[3] * x[4]**2 for x in rows)
    a['U(1)_V-grav'] = sum(n[id(x)] * x[3] for x in rows)
    a['U(1)_AF-grav'] = sum(n[id(x)] * x[4] for x in rows)
    return a


def gauge_anomaly_free_af(table, gauge_T_adj=3):
    """SU(3)^2 U(1)_AF of the gauge group itself must vanish."""
    total = 0
    for _, g, l, r, V, AF in table:
        flav = DIM6[l] * DIM6[r]
        if g == 8:
            total += gauge_T_adj * flav * AF
        elif g == 3:
            total += T_fund * flav * AF
    return total


# ============================================================
# Main verification
# ============================================================

def report(results, header):
    ok = True
    print(header)
    for cond in CONDITIONS:
        val = results[cond]
        status = "PASS" if val == 0 else "FAIL"
        ok &= (val == 0)
        print(f"  [{status}]  {cond:25s}  =  {val}")
    print()
    return ok


def main():
    print("=" * 72)
    print("VALD-01: Dualised SM Anomaly Matching Verification")
    print("        SU(3)_c x SU(2)_L x U(1)_Y, QCD-sector route (Lecture 7, Sec. 5)")
    print("=" * 72)
    print()
    print("Conventions:")
    print("  T(fund) = 1/2, A(fund) = 1, A(antifund) = -1, A(adj) = 0")
    print("  Hypercharge: Y = T_R^3 + Q_V/6")
    print(f"  N_f = 2*n_g; electric SU({N_EL})_el, magnetic SU(3)_c, X = N_f - N = 3 at n_g = 3")
    print()

    all_pass = True

    # PART 1: magnetic SM gauge anomalies, symbolic in n_g
    mag_results = compute_anomaly_coefficients(define_magnetic_fermions(n_g))
    mag_pass = report(mag_results,
                      "--- Part 1: Magnetic theory, SM gauge anomalies (symbolic in n_g) ---")
    all_pass &= mag_pass
    if mag_pass:
        print("  All six vanish: the chiral SM content cancels per generation, the")
        print("  gaugino is a real colour octet, the mesino doublets pair up in Y.")
        print()

    # PART 2: Witten global anomaly
    print("--- Part 2: Witten SU(2)_L anomaly (even number of doublets) ---")
    doublets = count_doublets(define_magnetic_fermions(n_g))
    witten_pass = all(_at(doublets, k) % 2 == 0 for k in range(1, 11))
    all_pass &= witten_pass
    print(f"  [{'PASS' if witten_pass else 'FAIL'}]  magnetic doublets = {doublets} "
          f"(even for n_g = 1..10)")
    el_doublets = count_doublets(define_electric_fermions(NG_PHYS))
    el_witten = _at(el_doublets, NG_PHYS) % 2 == 0
    all_pass &= el_witten
    print(f"  [{'PASS' if el_witten else 'FAIL'}]  electric doublets at n_g = 3 = "
          f"{_at(el_doublets, NG_PHYS)} (even)")
    print()

    # PART 3: electric vs magnetic flavour conditions at n_g = 3
    print("--- Part 3: Flavour conditions, electric vs magnetic at n_g = 3 ---")
    print("  (SU(3)_c^3 and SU(3)_c^2 U(1)_Y are magnetic-only: colour is magnetic.)")
    el_results = compute_anomaly_coefficients(define_electric_fermions(NG_PHYS))
    match_pass = True
    for cond in ['SU(2)^3'] + FLAVOUR_CONDITIONS:
        el_num = _at(el_results[cond], NG_PHYS) if el_results[cond] != 0 else 0
        mag_num = _at(mag_results[cond], NG_PHYS)
        ok = el_num == mag_num
        match_pass &= ok
        print(f"  [{'PASS' if ok else 'FAIL'}]  {cond:25s}  el = {el_num}  mag = {mag_num}")
    all_pass &= match_pass
    print()

    # PART 4: flavour-group 't Hooft anomalies from the Lecture 7 tables
    print("--- Part 4: 't Hooft anomalies of SU(6)_L x SU(6)_R x U(1)_V x U(1)_AF (n_g = 3) ---")
    el_flav = flavour_anomalies(ELECTRIC_TABLE)
    mag_flav = flavour_anomalies(MAGNETIC_TABLE)
    flav_pass = True
    for cond in el_flav:
        ok = el_flav[cond] == mag_flav[cond]
        flav_pass &= ok
        print(f"  [{'PASS' if ok else 'FAIL'}]  {cond:22s}  el = {str(el_flav[cond]):>6s}"
              f"  mag = {str(mag_flav[cond]):>6s}")
    for label, table in (("SU(3)_el", ELECTRIC_TABLE), ("SU(3)_c", MAGNETIC_TABLE)):
        val = gauge_anomaly_free_af(table)
        ok = val == 0
        flav_pass &= ok
        print(f"  [{'PASS' if ok else 'FAIL'}]  {label}^2 U(1)_AF = {val} (U(1)_AF anomaly-free)")
    all_pass &= flav_pass
    print()

    # PART 5: SM-only subset
    sm_results = compute_anomaly_coefficients(define_sm_fermions(n_g))
    sm_pass = report(sm_results,
                     "--- Part 5: SM content alone (no gaugino, no mesino) ---")
    all_pass &= sm_pass

    # PART 6: spot checks of Part 1
    print("--- Part 6: Magnetic spot checks at n_g = 1..6 ---")
    spot_pass = True
    for k in range(1, 7):
        vals = [_at(mag_results[c], k) for c in CONDITIONS]
        ok = all(v == 0 for v in vals)
        spot_pass &= ok
        print(f"  [{'PASS' if ok else 'FAIL'}]  n_g = {k}: {vals}")
    all_pass &= spot_pass
    print()

    print("=" * 72)
    if all_pass:
        print("ALL CHECKS PASSED")
        print()
        print("Summary:")
        print("  Magnetic SM gauge anomalies:      6/6 vanish symbolically (chiral content)")
        print("  Witten SU(2)_L anomaly:           doublet counts even")
        print("  Flavour conditions at n_g = 3:    electric = magnetic")
        print(f"  Flavour-group 't Hooft anomalies: {len(el_flav)}/{len(el_flav)} match")
        print("  SM subset check:                  6/6 SM-only conditions vanish")
        print()
        print("VALD-01 COMPLETE: anomaly matching verified for dualised SM.")
    else:
        print("SOME CHECKS FAILED")
        for name, ok in (("magnetic SM anomalies", mag_pass), ("Witten", witten_pass and el_witten),
                         ("electric vs magnetic", match_pass), ("flavour group", flav_pass),
                         ("SM subset", sm_pass), ("spot checks", spot_pass)):
            if not ok:
                print(f"  FAILED: {name}")
    print("=" * 72)
    return 0 if all_pass else 1


if __name__ == '__main__':
    sys.exit(main())
