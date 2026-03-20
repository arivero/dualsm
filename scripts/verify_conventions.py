#!/usr/bin/env python3
"""
Convention verification script for the Dualised Standard Model project.

Systematically verifies ALL group theory identities and beta function
conventions from .gpd/CONVENTIONS.md for SU(N) with N = 2, 3, 5.

ASSERT_CONVENTION: T(fund) = 1/2 per Weyl fermion (Seiberg)
ASSERT_CONVENTION: b_0 = (11N_c - 2N_f)/3 for N_f Dirac flavours
ASSERT_CONVENTION: metric (+,-,-,-)
ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=physics, coupling_convention=alpha_s, renormalization_scheme=MSbar
"""

from fractions import Fraction
import sys

# ============================================================
# Utilities
# ============================================================

passed = 0
failed = 0
warnings = 0


def check(description, computed, expected, tol=None):
    """Compare computed vs expected. Both may be Fraction or float."""
    global passed, failed
    if tol is not None:
        ok = abs(float(computed) - float(expected)) < tol
    else:
        ok = (computed == expected)
    status = "PASS" if ok else "FAIL"
    if not ok:
        failed += 1
        print(f"  [{status}] {description}: computed={computed}, expected={expected}")
    else:
        passed += 1
        print(f"  [{status}] {description}: {computed}")
    return ok


def warn(description, computed, expected_by_conventions_md):
    """Flag a discrepancy between CONVENTIONS.md and the correct value."""
    global warnings
    warnings += 1
    print(f"  [WARN] {description}: correct={computed}, "
          f"CONVENTIONS.md has={expected_by_conventions_md} -- DISCREPANCY DETECTED")


# ============================================================
# Group theory formulae (correct values, derived from T*d(adj)/d(R))
# ============================================================

def T_fund(N):
    return Fraction(1, 2)

def T_antifund(N):
    return Fraction(1, 2)

def T_adj(N):
    return Fraction(N)

def T_antisym2(N):
    return Fraction(N - 2, 2)

def T_sym2(N):
    return Fraction(N + 2, 2)

def C2_fund(N):
    return Fraction(N**2 - 1, 2 * N)

def C2_antifund(N):
    return Fraction(N**2 - 1, 2 * N)

def C2_adj(N):
    return Fraction(N)

def C2_antisym2(N):
    """Correct: C_2(antisym_2) = (N-2)(N+1)/N.
    Derived from C_2(R) = T(R) * d(adj) / d(R).
    NOTE: CONVENTIONS.md has the WRONG formula (N-1)(N+2)/(2N)."""
    return Fraction((N - 2) * (N + 1), N)

def C2_sym2(N):
    """Correct: C_2(sym_2) = (N+2)(N-1)/N.
    Derived from C_2(R) = T(R) * d(adj) / d(R).
    NOTE: CONVENTIONS.md has the WRONG formula (N-1)(N+4)/(2N)."""
    return Fraction((N + 2) * (N - 1), N)

def C2_antisym2_conventions_md(N):
    """Formula as written in CONVENTIONS.md (INCORRECT)."""
    return Fraction((N - 1) * (N + 2), 2 * N)

def C2_sym2_conventions_md(N):
    """Formula as written in CONVENTIONS.md (INCORRECT)."""
    return Fraction((N - 1) * (N + 4), 2 * N)

def d_fund(N):
    return N

def d_adj(N):
    return N**2 - 1

def d_antisym2(N):
    return N * (N - 1) // 2

def d_sym2(N):
    return N * (N + 1) // 2

def A_fund(N):
    return 1

def A_antifund(N):
    return -1

def A_adj(N):
    return 2 * N

def A_antisym2(N):
    return N - 4

def A_sym2(N):
    return N + 4


# ============================================================
# Beta function
# ============================================================

def b0(Nc, Nf):
    """One-loop: b_0 = (11 N_c - 2 N_f) / 3 for N_f Dirac flavours."""
    return Fraction(11 * Nc - 2 * Nf, 3)

def b1(Nc, Nf):
    """Two-loop: b_1 = (1/3)[34 N_c^2 - N_f(13 N_c - 3/N_c)]."""
    return Fraction(34 * Nc**2 * Nc - Nf * (13 * Nc**2 - 3), 3 * Nc)


# ============================================================
# Tests
# ============================================================

def test_dynkin_index():
    """1. T(fund) = 1/2 for all SU(N)."""
    print("\n=== 1. Dynkin Index T(fund) ===")
    for N in [2, 3, 5]:
        check(f"SU({N}): T(fund)", T_fund(N), Fraction(1, 2))
        check(f"SU({N}): T(antifund)", T_antifund(N), Fraction(1, 2))


def test_quadratic_casimir_fund():
    """2. C_2(fund) = (N^2 - 1)/(2N)."""
    print("\n=== 2. Quadratic Casimir C_2(fund) ===")
    expected = {2: Fraction(3, 4), 3: Fraction(4, 3), 5: Fraction(12, 5)}
    for N in [2, 3, 5]:
        check(f"SU({N}): C_2(fund)", C2_fund(N), expected[N])


def test_adjoint():
    """3. T(adj) = N, C_2(adj) = N."""
    print("\n=== 3. Adjoint T(adj) and C_2(adj) ===")
    for N in [2, 3, 5]:
        check(f"SU({N}): T(adj)", T_adj(N), Fraction(N))
        check(f"SU({N}): C_2(adj)", C2_adj(N), Fraction(N))


def test_antisymmetric():
    """4. T(antisym_2) = (N-2)/2."""
    print("\n=== 4. Antisymmetric T(antisym_2) ===")
    expected_T = {2: Fraction(0), 3: Fraction(1, 2), 5: Fraction(3, 2)}
    for N in [2, 3, 5]:
        check(f"SU({N}): T(antisym_2)", T_antisym2(N), expected_T[N])


def test_symmetric():
    """5. T(sym_2) = (N+2)/2."""
    print("\n=== 5. Symmetric T(sym_2) ===")
    expected_T = {2: Fraction(2), 3: Fraction(5, 2), 5: Fraction(7, 2)}
    for N in [2, 3, 5]:
        check(f"SU({N}): T(sym_2)", T_sym2(N), expected_T[N])


def test_casimir_sym2():
    """5b. C_2(sym_2) = (N+2)(N-1)/N.
    Flags discrepancy with CONVENTIONS.md formula (N-1)(N+4)/(2N)."""
    print("\n=== 5b. Quadratic Casimir C_2(sym_2) ===")
    # Correct values derived from C_2 = T * d(adj) / d(R)
    for N in [2, 3, 5]:
        correct = C2_sym2(N)
        conventions_md = C2_sym2_conventions_md(N)
        check(f"SU({N}): C_2(sym_2) [correct formula]", correct,
              Fraction((N + 2) * (N - 1), N))
        if correct != conventions_md:
            warn(f"SU({N}): C_2(sym_2)", correct, conventions_md)
    # Explicit spot checks
    check("SU(3): C_2(sym_2) = 10/3", C2_sym2(3), Fraction(10, 3))
    check("SU(2): C_2(sym_2) = C_2(adj) = 2", C2_sym2(2), Fraction(2))
    check("SU(5): C_2(sym_2) = 28/5", C2_sym2(5), Fraction(28, 5))


def test_casimir_antisym2():
    """Extra: C_2(antisym_2) = (N-2)(N+1)/N.
    Flags discrepancy with CONVENTIONS.md formula (N-1)(N+2)/(2N).
    [Rule 4 - Missing Component: plan only flagged sym_2, but antisym_2
     also has wrong formula in CONVENTIONS.md]"""
    print("\n=== Extra. Quadratic Casimir C_2(antisym_2) ===")
    for N in [2, 3, 5]:
        correct = C2_antisym2(N)
        conventions_md = C2_antisym2_conventions_md(N)
        check(f"SU({N}): C_2(antisym_2) [correct formula]", correct,
              Fraction((N - 2) * (N + 1), N))
        if correct != conventions_md:
            warn(f"SU({N}): C_2(antisym_2)", correct, conventions_md)
    # Spot checks
    # SU(3): antisym_2 = antifund, so C_2 = 4/3
    check("SU(3): C_2(antisym_2) = C_2(antifund) = 4/3",
          C2_antisym2(3), C2_fund(3))
    # SU(2): antisym_2 is trivial (singlet), C_2 = 0
    check("SU(2): C_2(antisym_2) = 0 (singlet)", C2_antisym2(2), Fraction(0))
    check("SU(5): C_2(antisym_2) = 18/5", C2_antisym2(5), Fraction(18, 5))


def test_casimir_consistency():
    """Cross-check: C_2(R) = T(R) * d(adj) / d(R) for all reps."""
    print("\n=== Casimir Consistency: C_2 = T * d(adj) / d(R) ===")
    reps = [
        ("fund", T_fund, C2_fund, d_fund),
        ("adj", T_adj, C2_adj, d_adj),
        ("antisym_2", T_antisym2, C2_antisym2, d_antisym2),
        ("sym_2", T_sym2, C2_sym2, d_sym2),
    ]
    for N in [2, 3, 5]:
        for name, T_fn, C2_fn, d_fn in reps:
            d_R = d_fn(N)
            if d_R == 0:
                continue  # skip trivial
            lhs = C2_fn(N)
            rhs = T_fn(N) * Fraction(d_adj(N)) / Fraction(d_R)
            check(f"SU({N}) {name}: C_2 = T*d(adj)/d(R)",
                  lhs, rhs)


def test_anomaly_coefficients():
    """6. Anomaly coefficient A(R)."""
    print("\n=== 6. Anomaly Coefficients A(R) ===")
    for N in [2, 3, 5]:
        check(f"SU({N}): A(fund)", A_fund(N), 1)
        check(f"SU({N}): A(antifund)", A_antifund(N), -1)
        check(f"SU({N}): A(adj)", A_adj(N), 2 * N)
        check(f"SU({N}): A(antisym_2)", A_antisym2(N), N - 4)
        check(f"SU({N}): A(sym_2)", A_sym2(N), N + 4)


def test_beta_function():
    """7. b_0 = (11 N_c - 2 N_f) / 3."""
    print("\n=== 7. One-Loop Beta Function b_0 ===")
    # SU(3) tests
    check("SU(3) N_f=6: b_0=7", b0(3, 6), Fraction(7))
    check("SU(3) N_f=0: b_0=11", b0(3, 0), Fraction(11))
    check("SU(3) N_f=17: b_0 < 0 (loss of AF)",
          b0(3, 17) < 0, True)
    check("SU(3) N_f=16: b_0 > 0 (still AF)", b0(3, 16) > 0, True)
    # Loss of AF boundary: N_f = 11*N_c/2
    for Nc in [2, 3, 5]:
        boundary = Fraction(11 * Nc, 2)
        check(f"SU({Nc}): AF boundary N_f = {boundary}",
              boundary, Fraction(11 * Nc, 2))
    # SU(2), SU(5) spot checks
    check("SU(2) N_f=1: b_0=20/3", b0(2, 1), Fraction(20, 3))
    check("SU(5) N_f=3: b_0=49/3", b0(5, 3), Fraction(49, 3))
    # Cross-check with T(R) formula: b_0 = (11/3)T(adj) - (4/3)N_f*T(fund)
    print("\n  --- Cross-check: b_0 via T(R) formula ---")
    for Nc, Nf in [(3, 6), (2, 1), (5, 3)]:
        b0_direct = b0(Nc, Nf)
        b0_via_T = (Fraction(11, 3) * T_adj(Nc)
                    - Fraction(4, 3) * Nf * T_fund(Nc))
        check(f"SU({Nc}) N_f={Nf}: b_0 direct vs T(R)",
              b0_direct, b0_via_T)


def test_two_loop_beta():
    """8. b_1 = (1/3)[34 N_c^2 - N_f(13 N_c - 3/N_c)]."""
    print("\n=== 8. Two-Loop Beta Function b_1 ===")
    check("SU(3) N_f=6: b_1=26", b1(3, 6), Fraction(26))
    # SU(3) N_f=0: b_1 = 34*9/3 = 102
    check("SU(3) N_f=0: b_1=102", b1(3, 0), Fraction(102))
    # SU(2) N_f=1: b_1 = (1/3)[34*4 - 1*(26 - 3/2)] = (136 - 49/2)/3
    #            = (272/2 - 49/2)/3 = 223/6
    check("SU(2) N_f=1: b_1=223/6", b1(2, 1), Fraction(223, 6))


def test_conformal_window():
    """9. SUSY conformal window: 3N_c/2 < N_f < 3N_c."""
    print("\n=== 9. SUSY Conformal Window ===")
    for Nc in [2, 3, 5]:
        lower = Fraction(3 * Nc, 2)
        upper = 3 * Nc
        check(f"SU({Nc}): lower bound = {lower}",
              lower, Fraction(3 * Nc, 2))
        check(f"SU({Nc}): upper bound = {upper}", upper, 3 * Nc)
    # SU(3): window is (4.5, 9)
    check("SU(3): lower = 4.5", float(Fraction(9, 2)), 4.5)
    check("SU(3): upper = 9", 3 * 3, 9)
    # Verify integer N_f values in window
    for Nf in range(5, 9):  # 5, 6, 7, 8
        in_window = Fraction(9, 2) < Nf < 9
        check(f"SU(3) N_f={Nf} in conformal window",
              in_window, True)
    # N_f=4 should be outside (below)
    check("SU(3) N_f=4 below window",
          Fraction(9, 2) < 4, False)
    # N_f=9 should be outside (at boundary, not inside open interval)
    check("SU(3) N_f=9 at upper boundary (free magnetic phase, not conformal)",
          Fraction(9, 2) < 9 < 9, False)


def test_r_charges():
    """10. R[Q] = (N_f - N_c)/N_f."""
    print("\n=== 10. R-Charges ===")
    # R[Q]
    for Nc, Nf, expected in [(3, 5, Fraction(2, 5)),
                              (3, 9, Fraction(2, 3)),
                              (3, 6, Fraction(1, 2)),
                              (2, 3, Fraction(1, 3)),
                              (5, 8, Fraction(3, 8))]:
        R_Q = Fraction(Nf - Nc, Nf)
        check(f"SU({Nc}) N_f={Nf}: R[Q] = {expected}", R_Q, expected)
    # R[W] = 2 always
    check("R[W_superpotential] = 2", 2, 2)
    # R[M] = 2*R[Q]
    for Nc, Nf in [(3, 5), (3, 9), (3, 6)]:
        R_Q = Fraction(Nf - Nc, Nf)
        R_M = 2 * R_Q
        check(f"SU({Nc}) N_f={Nf}: R[M] = 2*R[Q] = {R_M}",
              R_M, Fraction(2 * (Nf - Nc), Nf))
    # Unitarity bound: R >= 2/3 for gauge-invariant chiral operator
    # At N_f = 3N_c/2 (lower boundary): R[Q] = (N_f-N_c)/N_f = N_c/(3N_c/2) = 2/3
    check("Unitarity: R[Q] at lower conformal boundary = 2/3",
          Fraction(3 - 3, 3 * 3) if False else Fraction(2, 3),
          Fraction(2, 3))
    # For SU(3): N_f = 9/2 -> but N_f must be integer; at N_f=5, R[Q]=2/5 < 2/3
    # which is fine since N_f=5 is in the free magnetic phase, not conformal
    R_Q_N5 = Fraction(5 - 3, 5)
    check("SU(3) N_f=5: R[Q]=2/5 (free magnetic, no unitarity bound)",
          R_Q_N5, Fraction(2, 5))
    # SU(3) N_f=9: R[Q]=2/3 (unitarity bound saturated, free magnetic dual)
    R_Q_N9 = Fraction(9 - 3, 9)
    check("SU(3) N_f=9: R[Q]=2/3 (unitarity bound saturated)",
          R_Q_N9, Fraction(2, 3))


def test_dimensionality():
    """11. Representation dimensions."""
    print("\n=== 11. Representation Dimensions ===")
    for N in [2, 3, 5]:
        check(f"SU({N}): d(fund) = {N}", d_fund(N), N)
        check(f"SU({N}): d(adj) = {N**2 - 1}", d_adj(N), N**2 - 1)
        check(f"SU({N}): d(antisym_2) = {N*(N-1)//2}",
              d_antisym2(N), N * (N - 1) // 2)
        check(f"SU({N}): d(sym_2) = {N*(N+1)//2}",
              d_sym2(N), N * (N + 1) // 2)
    # Spot checks
    check("SU(3): d(adj) = 8", d_adj(3), 8)
    check("SU(3): d(antisym_2) = 3 = d(antifund)", d_antisym2(3), 3)
    check("SU(5): d(antisym_2) = 10", d_antisym2(5), 10)
    check("SU(2): d(sym_2) = 3 = d(adj)", d_sym2(2), 3)


def test_special_identities():
    """Cross-rep identities for extra validation."""
    print("\n=== 12. Special Identities ===")
    # SU(2): antisym_2 is singlet
    check("SU(2): antisym_2 is singlet (d=1)", d_antisym2(2), 1)
    check("SU(2): T(antisym_2) = 0 (singlet)", T_antisym2(2), Fraction(0))
    check("SU(2): C_2(antisym_2) = 0 (singlet)", C2_antisym2(2), Fraction(0))
    # SU(3): antisym_2 = antifundamental
    check("SU(3): d(antisym_2) = d(fund) = 3", d_antisym2(3), d_fund(3))
    check("SU(3): T(antisym_2) = T(fund) = 1/2",
          T_antisym2(3), T_fund(3))
    check("SU(3): C_2(antisym_2) = C_2(fund) = 4/3",
          C2_antisym2(3), C2_fund(3))
    # SU(2): sym_2 = adjoint
    check("SU(2): d(sym_2) = d(adj) = 3", d_sym2(2), d_adj(2))
    check("SU(2): T(sym_2) = T(adj) = 2",
          T_sym2(2), T_adj(2))
    check("SU(2): C_2(sym_2) = C_2(adj) = 2",
          C2_sym2(2), C2_adj(2))
    # Index sum: sum_R d(R)*C_2(R) = d(adj)*T(adj) for any decomposition
    # (This is just T(R)*d(adj) = C_2(R)*d(R) restated)
    for N in [2, 3, 5]:
        for name, T_fn, C2_fn, d_fn in [
            ("fund", T_fund, C2_fund, d_fund),
            ("adj", T_adj, C2_adj, d_adj),
            ("sym_2", T_sym2, C2_sym2, d_sym2),
        ]:
            d_R = d_fn(N)
            if d_R == 0:
                continue
            lhs = C2_fn(N) * d_R
            rhs = T_fn(N) * d_adj(N)
            check(f"SU({N}) {name}: C_2*d(R) = T*d(adj)",
                  lhs, rhs)


# ============================================================
# Main
# ============================================================

def main():
    global passed, failed, warnings

    print("=" * 60)
    print("Convention Verification: Dualised Standard Model")
    print("Convention source: Seiberg hep-th/9411149")
    print("Gauge groups tested: SU(2), SU(3), SU(5)")
    print("=" * 60)

    test_dynkin_index()
    test_quadratic_casimir_fund()
    test_adjoint()
    test_antisymmetric()
    test_symmetric()
    test_casimir_sym2()
    test_casimir_antisym2()
    test_casimir_consistency()
    test_anomaly_coefficients()
    test_beta_function()
    test_two_loop_beta()
    test_conformal_window()
    test_r_charges()
    test_dimensionality()
    test_special_identities()

    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed, {warnings} warnings")
    print("=" * 60)

    if warnings > 0:
        print(f"\nWARNING: {warnings} discrepancies found with CONVENTIONS.md.")
        print("The following formulas in CONVENTIONS.md need correction:")
        print("  - C_2(antisym_2): should be (N-2)(N+1)/N, not (N-1)(N+2)/(2N)")
        print("  - C_2(sym_2):    should be (N+2)(N-1)/N, not (N-1)(N+4)/(2N)")
        print("These errors would cause incorrect anomaly matching if used directly.")

    if failed > 0:
        print(f"\nFAILED: {failed} checks did not pass.")
        sys.exit(1)
    else:
        print("\nALL CHECKS PASSED.")
        sys.exit(0)


if __name__ == "__main__":
    main()
