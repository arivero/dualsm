#!/usr/bin/env python3
"""
VALD-02: Symbolic verification of Seiberg duality anomaly matching.

Computes all 6+1 independent 't Hooft anomaly coefficients for both
the electric SU(N_c) theory and the magnetic SU(N_f - N_c) theory,
and verifies exact matching as polynomial identities in N_c and N_f.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA

Conventions:
    T(fund) = 1/2 per Weyl fermion
    A(fund) = 1, A(antifund) = -1 (cubic anomaly coefficient)
    R_fermion = R_superfield - 1 for chiral multiplet components
    R_gaugino = +1 (directly; gaugino is NOT a chiral superfield component)
    B[Q] = +1, B[Q-tilde] = -1
    B[q] = N_c / (N_f - N_c), B[q-tilde] = -N_c / (N_f - N_c)
    N_f counts Dirac flavour pairs

References:
    Seiberg, hep-th/9411149
    Intriligator-Seiberg, hep-th/9509066
"""

import sys
from sympy import symbols, simplify, Rational, expand, cancel

# ============================================================
# Symbols
# ============================================================
Nc, Nf = symbols('N_c N_f', positive=True, integer=True)

# ============================================================
# Convention constants
# ============================================================
T_fund = Rational(1, 2)   # Dynkin index T(fund) = 1/2
A_fund = 1                # Cubic anomaly coefficient A(fund) = 1
A_antifund = -1            # A(antifund) = -1

# ============================================================
# Electric theory: SU(N_c) with N_f x (Q, Q-tilde)
# ============================================================
# Superfield R-charges
R_sf_Q = (Nf - Nc) / Nf           # R[Q] = (N_f - N_c)/N_f
R_sf_Qtilde = (Nf - Nc) / Nf      # R[Q-tilde] = (N_f - N_c)/N_f
R_sf_gaugino = 1                    # R[gaugino] = +1

# FERMION R-charges: R_ferm = R_sf - 1 for chiral multiplet components
# Gaugino R_ferm = +1 directly (NOT shifted)
R_ferm_Q = R_sf_Q - 1              # = -N_c / N_f
R_ferm_Qtilde = R_sf_Qtilde - 1    # = -N_c / N_f
R_ferm_gaugino = 1                  # +1 directly

# Baryon charges
B_Q = 1
B_Qtilde = -1
B_gaugino = 0

# Gauge multiplicities
gauge_mult_Q = Nc          # N_c colours
gauge_mult_Qtilde = Nc     # N_c colours (antifund)
gauge_mult_gaugino = Nc**2 - 1   # adjoint = N_c^2 - 1

# ============================================================
# Magnetic theory: SU(N_f - N_c) with N_f x (q, q-tilde) + M
# ============================================================
Nc_mag = Nf - Nc   # magnetic gauge group rank

# Superfield R-charges
R_sf_q = Nc / Nf                   # R[q] = N_c / N_f
R_sf_qtilde = Nc / Nf              # R[q-tilde] = N_c / N_f
R_sf_M = 2 * (Nf - Nc) / Nf       # R[M] = 2(N_f - N_c)/N_f
R_sf_gaugino_mag = 1               # R[gaugino_mag] = +1

# FERMION R-charges: R_ferm = R_sf - 1 for chiral multiplet components
R_ferm_q = R_sf_q - 1              # = (N_c - N_f) / N_f
R_ferm_qtilde = R_sf_qtilde - 1    # = (N_c - N_f) / N_f
R_ferm_M = R_sf_M - 1              # = (N_f - 2N_c) / N_f
R_ferm_gaugino_mag = 1             # +1 directly

# Baryon charges
B_q = Nc / (Nf - Nc)          # Derived from baryon matching
B_qtilde = -Nc / (Nf - Nc)
B_M = 0
B_gaugino_mag = 0

# Gauge multiplicities
gauge_mult_q = Nf - Nc         # magnetic colours
gauge_mult_qtilde = Nf - Nc
gauge_mult_M = 1               # gauge singlet
gauge_mult_gaugino_mag = (Nf - Nc)**2 - 1


# ============================================================
# Compute anomaly coefficients
# ============================================================

def compute_anomalies():
    """Compute all 7 anomaly coefficients on both sides."""
    results = {}
    all_pass = True

    # ----------------------------------------------------------
    # Coefficient 1: SU(N_f)_L^3
    # Uses cubic anomaly A(R) for fields charged under SU(N_f)_L
    # ----------------------------------------------------------
    # Electric: Q in fund of SU(N_f)_L, N_c gauge copies
    el_1 = gauge_mult_Q * A_fund

    # Magnetic: q in antifund of SU(N_f)_L, (N_f-N_c) gauge copies
    #           M in fund of SU(N_f)_L, N_f copies from SU(N_f)_R index
    mag_1 = gauge_mult_q * A_antifund + Nf * A_fund

    diff_1 = simplify(el_1 - mag_1)
    results['SU(N_f)_L^3'] = (el_1, mag_1, diff_1)
    if diff_1 != 0:
        all_pass = False

    # ----------------------------------------------------------
    # Coefficient 2: SU(N_f)_R^3
    # By L-R symmetry, same as coefficient 1
    # ----------------------------------------------------------
    # Electric: Q-tilde in antifund of SU(N_f)_R, N_c gauge copies
    el_2 = gauge_mult_Qtilde * A_antifund

    # Magnetic: q-tilde in fund of SU(N_f)_R, (N_f-N_c) gauge copies
    #           M in antifund of SU(N_f)_R, N_f copies from SU(N_f)_L index
    mag_2 = gauge_mult_qtilde * A_fund + Nf * A_antifund

    # Note: A(antifund) for Q-tilde, A(fund) for q-tilde.
    # Electric: N_c * A(antifund) = N_c * (-1) = -N_c
    # Magnetic: (N_f - N_c) * A(fund) + N_f * A(antifund) = (N_f - N_c) - N_f = -N_c
    # These match by L-R symmetry. Let's verify:
    diff_2 = simplify(el_2 - mag_2)
    results['SU(N_f)_R^3'] = (el_2, mag_2, diff_2)
    if diff_2 != 0:
        all_pass = False

    # ----------------------------------------------------------
    # Coefficient 3: SU(N_f)_L^2 U(1)_B
    # = sum_f (gauge_mult) * T(R_L) * B_f
    # ----------------------------------------------------------
    # Electric: Q in fund of SU(N_f)_L, N_c colours, B = +1
    el_3 = gauge_mult_Q * T_fund * B_Q

    # Magnetic: q in antifund of SU(N_f)_L, (N_f-N_c) colours, B = N_c/(N_f-N_c)
    #           M: B = 0, no contribution
    mag_3 = gauge_mult_q * T_fund * B_q + Nf * T_fund * B_M

    diff_3 = simplify(el_3 - mag_3)
    results['SU(N_f)_L^2 U(1)_B'] = (el_3, mag_3, diff_3)
    if diff_3 != 0:
        all_pass = False

    # ----------------------------------------------------------
    # Coefficient 4: SU(N_f)_L^2 U(1)_R
    # = sum_f (gauge_mult) * T(R_L) * R_ferm_f
    # ----------------------------------------------------------
    # Electric: Q in fund of SU(N_f)_L, N_c colours
    el_4 = gauge_mult_Q * T_fund * R_ferm_Q

    # Magnetic: q in antifund of SU(N_f)_L, (N_f-N_c) colours
    #           M in fund of SU(N_f)_L, N_f copies
    mag_4 = gauge_mult_q * T_fund * R_ferm_q + Nf * T_fund * R_ferm_M

    diff_4 = simplify(el_4 - mag_4)
    results['SU(N_f)_L^2 U(1)_R'] = (el_4, mag_4, diff_4)
    if diff_4 != 0:
        all_pass = False

    # ----------------------------------------------------------
    # Coefficient 5: U(1)_B^2 U(1)_R
    # = sum_f (total_mult) * B_f^2 * R_ferm_f
    # Total multiplicity = gauge_mult * flavour_mult
    # ----------------------------------------------------------
    # Electric:
    #   Q: N_c * N_f fermions, B=+1, R_ferm = -N_c/N_f
    #   Q-tilde: N_c * N_f fermions, B=-1, R_ferm = -N_c/N_f
    #   Gaugino: B=0, no contribution
    el_5 = (Nc * Nf * B_Q**2 * R_ferm_Q
            + Nc * Nf * B_Qtilde**2 * R_ferm_Qtilde
            + gauge_mult_gaugino * B_gaugino**2 * R_ferm_gaugino)

    # Magnetic:
    #   q: (N_f-N_c) * N_f fermions
    #   q-tilde: (N_f-N_c) * N_f fermions
    #   M: N_f^2 fermions, B=0
    #   Gaugino: B=0
    mag_5 = ((Nf - Nc) * Nf * B_q**2 * R_ferm_q
             + (Nf - Nc) * Nf * B_qtilde**2 * R_ferm_qtilde
             + Nf**2 * B_M**2 * R_ferm_M
             + gauge_mult_gaugino_mag * B_gaugino_mag**2 * R_ferm_gaugino_mag)

    diff_5 = simplify(el_5 - mag_5)
    results['U(1)_B^2 U(1)_R'] = (simplify(el_5), simplify(mag_5), diff_5)
    if diff_5 != 0:
        all_pass = False

    # ----------------------------------------------------------
    # Coefficient 6a: Tr[R] (gravitational anomaly)
    # = sum_f (total_mult) * R_ferm_f
    # ----------------------------------------------------------
    el_6a = (Nc * Nf * R_ferm_Q
             + Nc * Nf * R_ferm_Qtilde
             + gauge_mult_gaugino * R_ferm_gaugino)

    mag_6a = ((Nf - Nc) * Nf * R_ferm_q
              + (Nf - Nc) * Nf * R_ferm_qtilde
              + Nf**2 * R_ferm_M
              + gauge_mult_gaugino_mag * R_ferm_gaugino_mag)

    diff_6a = simplify(el_6a - mag_6a)
    results['Tr[R] (gravitational)'] = (simplify(el_6a), simplify(mag_6a), diff_6a)
    if diff_6a != 0:
        all_pass = False

    # ----------------------------------------------------------
    # Coefficient 6b: Tr[R^3]
    # = sum_f (total_mult) * R_ferm_f^3
    # ----------------------------------------------------------
    el_6b = (Nc * Nf * R_ferm_Q**3
             + Nc * Nf * R_ferm_Qtilde**3
             + gauge_mult_gaugino * R_ferm_gaugino**3)

    mag_6b = ((Nf - Nc) * Nf * R_ferm_q**3
              + (Nf - Nc) * Nf * R_ferm_qtilde**3
              + Nf**2 * R_ferm_M**3
              + gauge_mult_gaugino_mag * R_ferm_gaugino_mag**3)

    diff_6b = simplify(expand(el_6b) - expand(mag_6b))
    # If simplify does not reduce, try cancel as fallback
    if diff_6b != 0:
        diff_6b = cancel(expand(el_6b) - expand(mag_6b))
    results['Tr[R^3]'] = (simplify(el_6b), simplify(mag_6b), diff_6b)
    if diff_6b != 0:
        all_pass = False

    return results, all_pass


def check_r_charge_consistency():
    """Verify R[W_mag] = 2."""
    R_Wmag = R_sf_M + R_sf_q + R_sf_qtilde
    result = simplify(R_Wmag - 2)
    return result == 0, simplify(R_Wmag)


def check_scale_matching():
    """Verify scale matching exponents sum to N_f."""
    exp_el = 3 * Nc - Nf
    exp_mag = 3 * (Nf - Nc) - Nf   # = 2*N_f - 3*N_c
    total = simplify(exp_el + exp_mag - Nf)
    return total == 0, exp_el, exp_mag


def numerical_spot_check(nc_val, nf_val, results):
    """
    Spot-check anomaly matching at specific (N_c, N_f) values.
    Returns True if all coefficients match numerically.
    """
    subs = {Nc: nc_val, Nf: nf_val}
    all_ok = True
    for name, (el, mag, diff) in results.items():
        el_num = float(el.subs(subs))
        mag_num = float(mag.subs(subs))
        diff_num = float(diff.subs(subs)) if diff != 0 else 0.0
        if abs(diff_num) > 1e-12:
            print(f"  FAIL  {name}: el={el_num:.6f}, mag={mag_num:.6f}, diff={diff_num:.6f}")
            all_ok = False
        else:
            print(f"  OK    {name}: el={el_num:.6f}, mag={mag_num:.6f}")
    return all_ok


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 70)
    print("VALD-02: Seiberg Duality Anomaly Matching Verification")
    print("=" * 70)
    print()

    # ----- Symbolic verification -----
    print("--- Symbolic anomaly matching (as polynomial identities in N_c, N_f) ---")
    print()
    results, all_pass = compute_anomalies()

    for name, (el, mag, diff) in results.items():
        status = "PASS" if diff == 0 else "FAIL"
        print(f"  [{status}]  {name}")
        print(f"         Electric: {el}")
        print(f"         Magnetic: {mag}")
        print(f"         Diff:     {diff}")
        print()

    # ----- R-charge consistency -----
    print("--- R-charge consistency: R[W_mag] = 2 ---")
    r_ok, r_val = check_r_charge_consistency()
    print(f"  [{'PASS' if r_ok else 'FAIL'}]  R[W_mag] = {r_val}")
    print()

    # ----- Scale matching -----
    print("--- Scale matching dimensional check ---")
    s_ok, e_el, e_mag = check_scale_matching()
    print(f"  [{'PASS' if s_ok else 'FAIL'}]  exp_el = {e_el}, exp_mag = {e_mag}, sum = N_f")
    print()

    # ----- Numerical spot-checks -----
    print("--- Numerical spot-checks ---")
    print()

    test_cases = [
        (3, 6, "SU(3), N_f=6 (standard textbook)"),
        (2, 3, "SU(2), N_f=3"),
        (5, 8, "SU(5), N_f=8"),
        (3, 4, "SU(3), N_f=4 (N_f = N_c + 1 boundary)"),
        (3, 9, "SU(3), N_f=9 (N_f = 3N_c boundary)"),
        (4, 6, "SU(4), N_f=6 (N_f = 3N_c/2 boundary)"),
    ]

    numerical_ok = True
    for nc_val, nf_val, label in test_cases:
        print(f"  Case: {label}  [N_c={nc_val}, N_f={nf_val}]")
        if not numerical_spot_check(nc_val, nf_val, results):
            numerical_ok = False
        print()

    # ----- Final summary -----
    print("=" * 70)
    overall = all_pass and r_ok and s_ok and numerical_ok
    if overall:
        print("ALL CHECKS PASSED")
        print()
        print("Summary:")
        print(f"  Symbolic anomaly matching:  {len(results)}/7 coefficients match")
        print(f"  R[W_mag] = 2:              PASS")
        print(f"  Scale matching:            PASS")
        print(f"  Numerical spot-checks:     {len(test_cases)}/{len(test_cases)} cases pass")
    else:
        print("SOME CHECKS FAILED")
        if not all_pass:
            print("  FAILED: Symbolic anomaly matching")
        if not r_ok:
            print("  FAILED: R-charge consistency")
        if not s_ok:
            print("  FAILED: Scale matching")
        if not numerical_ok:
            print("  FAILED: Numerical spot-checks")

    print("=" * 70)

    return 0 if overall else 1


if __name__ == '__main__':
    sys.exit(main())
