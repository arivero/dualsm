#!/usr/bin/env python3
"""
Koide / VEV-condition verification for Lecture 11 and Exercise Set 9.

Recomputes every number that lectures/lecture-11.tex and
exercises/exercise-09.tex quote about the Koide relation, and checks that
the quoted strings are still present in the two sources (so that an edit
to either file that changes a number without updating this script fails):

  1. Koide VEV condition for nonnegative x: Q(m_0 x_k^2) = (sum x)^2 /
     sum x^2, the trace condition z_0^2 = (1/3) sum z_k^2, scale invariance.
  2. Q(e, mu, tau) = 1.500005 (PDG 2024) and 1.500004 (rounded inputs).
  3. Q(1/m_d, 1/m_s, 1/m_b) = 1.5045 +/- 0.010 and Q(m_d, m_s, m_b) = 1.3675.
  4. Z_3 parametrisation: the signed ratio equals 3/2 for every delta.
     The mass ratio equals 3/2 on the nonnegative arc. Delta = 2/9 gives
     m_e/m_mu = 0.004836 and m_mu/m_tau = 0.05946 (relative differences
     1.0e-5 and 2.1e-5); m_0 z_0^2 = sum m / 6 = 313.85 MeV.
  5. SU(N) Casimirs: C_2(wedge^2 N)/C_2(N) = 2(N-2)/(N-1) = 3/2 only at
     N = 5; integer only at N = 2, 3; Dynkin ratios 7, 10, 3 for SU(5).
  6. Chain angle 3 x 2/9 rad = 38.2 deg (2.7% above 37.2 deg); seesaw
     pairings; Z-ladder examples.
  7. sBootstrap closure conditions: unique solution (k_u, k_d, N) = (2, 3, 3);
     ISS agreement only at (N_c, N_f) = (3, 5), outside the ISS range.
  8. S_3-symmetric potential of Exercise Set 9, Problem 5: the ten quartic
     structures are invariant and independent (character count 10), the
     leading-order minimum x_k^2 = s/mu_S^2 + d_k/mu_D^2, Q = 3/(1 + r^2),
     and the Koide-surface vector for delta = 2/9.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA

Conventions:
    Q = (sum_k sqrt(m_k))^2 / sum_k m_k, Koide point Q = 3/2
    C_2(R) = T(R) d(adj) / d(R), T(fund) = 1/2
    Lepton masses: PDG 2024 pole masses [MeV]
    Quark masses: MS-bar m_d(2 GeV), m_s(2 GeV), m_b(m_b) [MeV]

Pure Python (math, cmath, fractions, itertools, random); no third-party
packages.
"""

import cmath
import itertools
import math
import os
import random
import sys
from fractions import Fraction

# ============================================================
# Inputs (MeV)
# ============================================================
M_E, M_MU, M_TAU = 0.51099895, 105.6583755, 1776.93   # PDG 2024
DM_TAU = 0.09
M_E_R, M_MU_R = 0.511, 105.658                         # rounded (Exercise 2)
M_D, DM_D = 4.70, 0.20
M_S, DM_S = 93.5, 0.8
M_B, DM_B = 4183.0, 7.0
M_C = 1273.0                                           # m_c(m_c)
M_Z = 91188.0
DELTA = 2.0 / 9.0

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LECTURE = os.path.join(ROOT, "lectures", "lecture-11.tex")
EXERCISE = os.path.join(ROOT, "exercises", "exercise-09.tex")

passed = 0
failed = 0


def check(description, condition, detail=""):
    """Register a pass/fail check."""
    global passed, failed
    status = "PASS" if condition else "FAIL"
    if condition:
        passed += 1
    else:
        failed += 1
    detail_str = f"  [{detail}]" if detail else ""
    print(f"  [{status}] {description}{detail_str}")
    return condition


def koide_q(a, b, c):
    """Koide parameter Q = (sqrt a + sqrt b + sqrt c)^2 / (a + b + c)."""
    return (math.sqrt(a) + math.sqrt(b) + math.sqrt(c)) ** 2 / (a + b + c)


def z3_x(delta, r=1.0):
    """x_k / z_0 = 1 + sqrt(2) r cos(2 pi k/3 + delta), k = 1, 2, 3."""
    return [1.0 + math.sqrt(2.0) * r * math.cos(2.0 * math.pi * k / 3.0 + delta)
            for k in (1, 2, 3)]


def rel(a, b):
    return a / b - 1.0


# ============================================================
# 1. The Koide relation as a VEV condition (Lecture 11, section 2)
# ============================================================
def check_vev_condition():
    print("\n=== 1. Koide relation as a VEV condition (L11 section 2) ===")
    rng = random.Random(11)
    ok_qx = ok_scale = ok_trace = True
    for _ in range(200):
        x = [rng.uniform(0.01, 3.0) for _ in range(3)]
        m0 = rng.uniform(0.1, 500.0)
        q_mass = koide_q(*[m0 * t * t for t in x])
        q_x = sum(x) ** 2 / sum(t * t for t in x)
        ok_qx &= abs(q_mass - q_x) < 1e-12
        ok_scale &= abs(koide_q(*[7.3 * m0 * t * t for t in x]) - q_mass) < 1e-12
        z0 = sum(x) / 3.0
        z = [t - z0 for t in x]
        q_z = 9 * z0 ** 2 / (3 * z0 ** 2 + sum(t * t for t in z))
        ok_trace &= abs(q_z - q_x) < 1e-12
    check("Q(m_0 x_k^2) = (sum x)^2 / sum x^2 (eq. Qx)", ok_qx)
    check("Q is independent of the universal scale m_0", ok_scale)
    check("Q = 9 z_0^2 / (3 z_0^2 + sum z_k^2) (eq. Qz)", ok_trace)
    # Q = 3/2 <=> z_0^2 = (1/3) sum z_k^2
    x = z3_x(DELTA)
    z0 = sum(x) / 3.0
    zsq = sum((t - z0) ** 2 for t in x)
    check("Q = 3/2 <=> trace condition z_0^2 = (1/3) sum z_k^2",
          abs(z0 ** 2 - zsq / 3.0) < 1e-12 and abs(sum(x) ** 2 / sum(t * t for t in x) - 1.5) < 1e-12)


# ============================================================
# 2-3. Q values (Lecture 11 section 7; Exercise Set 9 Problem 2)
# ============================================================
def check_q_values():
    print("\n=== 2. Q for the charged leptons ===")
    q_pdg = koide_q(M_E, M_MU, M_TAU)
    q_rnd = koide_q(M_E_R, M_MU_R, M_TAU)
    dq = abs(koide_q(M_E, M_MU, M_TAU + DM_TAU) - koide_q(M_E, M_MU, M_TAU - DM_TAU)) / 2
    print(f"  Q(e,mu,tau) PDG = {q_pdg:.7f}, rounded inputs = {q_rnd:.7f}, dQ(m_tau) = {dq:.2e}")
    check("Q(e,mu,tau) = 1.500005 (PDG 2024)", abs(q_pdg - 1.500005) < 5e-7)
    check("Q(e,mu,tau) = 1.500004 (0.511, 105.658, 1776.93)", abs(q_rnd - 1.500004) < 5e-7)
    check("uncertainty from m_tau is 1.1e-5", abs(dq - 1.1e-5) < 0.05e-5)
    check("Q(e,mu,tau) within 0.4 sigma of 3/2", abs(q_rnd - 1.5) / dq < 0.4)

    print("\n=== 3. Q for the inverse down-type quark masses ===")
    q_inv = koide_q(1 / M_D, 1 / M_S, 1 / M_B)
    eps = 1e-7
    parts = []
    for i, dm in enumerate((DM_D, DM_S, DM_B)):
        m = [M_D, M_S, M_B]
        m2 = list(m)
        m2[i] *= 1 + eps
        dqdm = (koide_q(*[1 / t for t in m2]) - q_inv) / (m[i] * eps)
        parts.append(dqdm * dm)
    sig = math.sqrt(sum(p * p for p in parts))
    q_dir = koide_q(M_D, M_S, M_B)
    print(f"  Q(1/d,1/s,1/b) = {q_inv:.5f} +/- {sig:.4f}  (parts {', '.join(f'{p:+.4f}' for p in parts)})")
    check("Q(1/m_d,1/m_s,1/m_b) = 1.5045", abs(q_inv - 1.5045) < 5e-5)
    check("propagated uncertainty = 0.010, dominated by m_d",
          abs(sig - 0.010) < 5e-4 and abs(parts[0]) > 0.9 * sig)
    check("m_d uncertainty is 4.3%", abs(DM_D / M_D - 0.043) < 5e-4)
    check("deviation from 3/2 is 0.0045 (within 1 sigma)",
          abs((q_inv - 1.5) - 0.0045) < 1e-4 and abs(q_inv - 1.5) < sig)
    check("Q(m_d,m_s,m_b) = 1.3675 directly", abs(q_dir - 1.3675) < 5e-5)

    direct_only = (1, 1, (4 + 3 * math.sqrt(2)) ** 2)
    check("reciprocation can take a positive Koide triple off the cone",
          math.isclose(koide_q(*direct_only), 1.5)
          and not math.isclose(koide_q(*(1 / m for m in direct_only)), 1.5))
    r = (5 + math.sqrt(21)) / 2
    paired = (r ** -2, 1, r ** 2)
    check("the exceptional spectrum satisfies direct and reciprocal Koide",
          math.isclose(koide_q(*paired), 1.5)
          and math.isclose(koide_q(*(1 / m for m in paired)), 1.5))


# ============================================================
# 4. Z_3 parametrisation (Lecture 11 sections 4-5; Exercise Set 9 Problem 3)
# ============================================================
def check_z3():
    print("\n=== 4. Z_3 parametrisation and the Koide angle ===")
    signed_ok = True
    for i in range(50):
        d = -3.0 + 0.123 * i
        x = z3_x(d)
        signed_ok &= abs(sum(x) ** 2 / sum(t * t for t in x) - 1.5) < 1e-12
    check("the signed-root identity holds around the circle", signed_ok)
    positive_ok = True
    for i in range(13):
        x = z3_x((i / 12) * math.pi / 12)
        positive_ok &= min(x) >= -1e-14 and math.isclose(koide_q(*(t * t for t in x)), 1.5)
    check("positive mass roots give Q = 3/2 on the ordered nonnegative arc", positive_ok)
    x = z3_x(math.pi / 3)
    check("positive mass roots give Q > 3/2 with one negative x at pi/3",
          min(x) < 0 and koide_q(*(t * t for t in x)) > 1.5)
    x = z3_x(DELTA)
    determinant = (math.sqrt(2) * math.cos(3 * DELTA) - 1) / 2
    check("the dimensionless determinant selects the fitted phase",
          math.isclose(math.prod(x), determinant))
    m = [t * t for t in x]
    print(f"  x_k/z_0 = {x[0]:.6f}, {x[1]:.6f}, {x[2]:.6f}; m_k/(m_0 z_0^2) = "
          f"{m[0]:.6f}, {m[1]:.6f}, {m[2]:.6f}")
    check("x_k/z_0 = 0.040350, 0.580212, 2.379438 at delta = 2/9",
          all(abs(a - b) < 5e-7 for a, b in zip(x, (0.040350, 0.580212, 2.379438))))
    check("m_k/(m_0 z_0^2) sum to 6", abs(sum(m) - 6.0) < 1e-12)
    r_emu, r_mutau = m[0] / m[1], m[1] / m[2]
    d_emu, d_mutau = rel(r_emu, M_E / M_MU), rel(r_mutau, M_MU / M_TAU)
    print(f"  m_e/m_mu = {r_emu:.6e} (PDG {M_E / M_MU:.6e}, {d_emu:+.2e}); "
          f"m_mu/m_tau = {r_mutau:.6e} (PDG {M_MU / M_TAU:.6e}, {d_mutau:+.2e})")
    check("m_e/m_mu = 0.004836 (4.83628e-3)", round(r_emu, 6) == 0.004836 and abs(r_emu - 4.83628e-3) < 5e-9)
    check("m_mu/m_tau = 0.05946 (5.94599e-2)", round(r_mutau, 5) == 0.05946 and abs(r_mutau - 5.94599e-2) < 5e-8)
    check("relative differences 1.0e-5 and 2.1e-5, both below 1e-4",
          abs(abs(d_emu) - 1.0e-5) < 0.05e-5 and abs(abs(d_mutau) - 2.1e-5) < 0.05e-5
          and max(abs(d_emu), abs(d_mutau)) < 1e-4)
    s = M_E_R + M_MU_R + M_TAU
    scale = s / 6.0
    pred = [scale * t for t in m]
    print(f"  m_0 z_0^2 = {scale:.3f} MeV; predicted masses {pred[0]:.4f}, {pred[1]:.3f}, {pred[2]:.2f}")
    check("m_0 z_0^2 = (m_e+m_mu+m_tau)/6 = 313.85 MeV", abs(scale - 313.85) < 5e-3)
    check("predicted masses 0.5110, 105.656, 1776.93 MeV",
          abs(pred[0] - 0.5110) < 5e-5 and abs(pred[1] - 105.656) < 5e-4 and abs(pred[2] - 1776.93) < 5e-3)


# ============================================================
# 5. Casimir and Dynkin ratios (Lecture 11 section 3; Exercise Set 9 Problem 1)
# ============================================================
def check_casimirs():
    print("\n=== 5. SU(N) Casimir and Dynkin ratios ===")

    def c2_wedge(p, n):
        return Fraction(p * (n - p) * (n + 1), 2 * n)

    def t_wedge(p, n):
        return Fraction(math.comb(n - 2, p - 1), 2)

    ok_formula = ok_t = True
    for n in range(2, 30):
        for p in range(1, n):
            ok_t &= c2_wedge(p, n) == t_wedge(p, n) * (n * n - 1) / math.comb(n, p)
        ok_formula &= c2_wedge(2, n) / c2_wedge(1, n) == Fraction(2 * (n - 2), n - 1)
    check("C_2(wedge^p N) = p(N-p)(N+1)/(2N) equals T d(adj)/d for all p, N < 30", ok_t)
    check("C_2(wedge^2 N)/C_2(N) = 2(N-2)/(N-1)", ok_formula)
    table = {n: (c2_wedge(1, n), c2_wedge(2, n), c2_wedge(2, n) / c2_wedge(1, n)) for n in range(2, 7)}
    expected = {2: ("3/4", "0", "0"), 3: ("4/3", "4/3", "1"), 4: ("15/8", "5/2", "4/3"),
                5: ("12/5", "18/5", "3/2"), 6: ("35/12", "14/3", "8/5")}
    check("table of C_2(N), C_2(wedge^2 N), ratio for N = 2..6",
          all(tuple(str(v) for v in table[n]) == expected[n] for n in expected))
    ratios = {n: Fraction(2 * (n - 2), n - 1) for n in range(2, 1001)}
    check("ratio = 3/2 only at N = 5 (N <= 1000)", [n for n, r in ratios.items() if r == Fraction(3, 2)] == [5])
    check("ratio is an integer only at N = 2, 3", [n for n, r in ratios.items() if r.denominator == 1] == [2, 3])
    n = 5
    dadj = n * n - 1
    c2 = {"5": Fraction(n * n - 1, 2 * n), "10": Fraction((n - 2) * (n + 1), n),
          "15": Fraction((n + 2) * (n - 1), n), "24": Fraction(n)}
    dims = {"5": 5, "10": 10, "15": 15, "24": 24}
    t = {k: c2[k] * dims[k] / dadj for k in c2}
    check("SU(5): C_2(10)/C_2(5) = (18/5)/(12/5) = 3/2", c2["10"] / c2["5"] == Fraction(3, 2))
    check("SU(5): T(15)/T(5) = N+2 = 7", t["15"] / t["5"] == 7)
    check("SU(5): T(24)/T(5) = 2N = 10", t["24"] / t["5"] == 10)
    check("SU(5): T(10)/T(5) = N-2 = 3", t["10"] / t["5"] == 3)


# ============================================================
# 6. Chain angle, seesaw pairings, Z-ladder (Lecture 11 sections 3, 6, 7)
# ============================================================
def check_misc_numbers():
    print("\n=== 6. Chain angle, seesaw pairings, Z-ladder ===")
    ang = math.degrees(3 * DELTA)
    check("delta_chain = 3 x 2/9 rad = 2/3 rad = 38.2 deg", round(ang, 1) == 38.2, f"{ang:.3f} deg")
    check("38.2 deg vs measured 37.2 deg: 2.7%", round(100 * (ang - 37.2) / 37.2, 1) == 2.7)
    r = M_S / M_D
    check("standard pairing: m_s/m_d = 19.9, a factor ~4000 from m_e/m_mu",
          round(r, 1) == 19.9 and 3500 < r / (M_E / M_MU) < 4500, f"factor {r / (M_E / M_MU):.0f}")
    c = M_TAU * M_D
    check("reversed pairing: m_mu 15% off, m_e a factor ~4 off",
          round(abs(c / M_S / M_MU - 1), 2) == 0.15 and round(c / M_B / M_E) == 4)
    zs = math.sqrt(M_D * M_Z) / 7
    zc = math.sqrt(M_TAU * M_Z) / 10
    check("Z-ladder: sqrt(m_d M_Z)/7 = 93.52 MeV vs m_s = 93.5 MeV",
          round(zs, 2) == 93.52 and abs(zs / M_S - 1) < 3e-4)
    check("Z-ladder: sqrt(m_tau M_Z)/10 = 1272.9 MeV vs m_c = 1273 MeV",
          round(zc, 1) == 1272.9 and abs(zc / M_C - 1) < 1e-4)


# ============================================================
# 7. Closure conditions and ISS counting (Exercise Set 9 Problem 4)
# ============================================================
def check_closure_iss():
    print("\n=== 7. sBootstrap closure conditions and ISS counting ===")
    sols = [(ku, kd, n) for ku in range(1, 60) for kd in range(1, 60) for n in range(1, 400)
            if 2 * n == ku * kd and 4 * n == kd * (kd + 1) and 4 * n == ku * ku + kd * kd - 1]
    check("closure conditions: unique positive solution (k_u, k_d, N) = (2, 3, 3)", sols == [(2, 3, 3)], str(sols))
    pairs = [(nc, nf) for nc in range(1, 40) for nf in range(1, 80) if (nf - nc, nc) == (2, 3)]
    check("ISS split (N_f - N_c, N_c) = (2, 3) only at (N_c, N_f) = (3, 5)", pairs == [(3, 5)])
    ku, kd = 3, 2
    check("swapped split (3, 2) fails the second closure condition", kd * (kd + 1) // 2 != ku * kd)
    iss_range = [nf for nf in range(1, 20) if 3 < nf < 1.5 * 3]
    check("ISS range N_c < N_f < 3N_c/2 for N_c = 3 is {4}", iss_range == [4])
    b0mag = 3 * (5 - 3) - 5
    check("(3, 5): magnetic SU(2) has b_0 = 1 > 0 (inside the conformal window)",
          b0mag == 1 and 4.5 < 5 < 9)


# ============================================================
# 8. S_3-symmetric potential (Exercise Set 9 Problem 5)
# ============================================================
def _dot(a, b):
    """a^dagger b for doublets given as lists of two complex numbers."""
    return a[0].conjugate() * b[0] + a[1].conjugate() * b[1]


def _basis(h):
    """(H1, H2, H3) -> (h_S, h_1, h_2)."""
    s3, s2, s6 = math.sqrt(3), math.sqrt(2), math.sqrt(6)
    hs = [(h[0][i] + h[1][i] + h[2][i]) / s3 for i in range(2)]
    h1 = [(h[0][i] - h[1][i]) / s2 for i in range(2)]
    h2 = [(h[0][i] + h[1][i] - 2 * h[2][i]) / s6 for i in range(2)]
    return hs, h1, h2


def _structures(h):
    hs, h1, h2 = _basis(h)
    dd = _dot(h1, h1) + _dot(h2, h2)
    x4 = _dot(hs, h1) * (_dot(h1, h2) + _dot(h2, h1)) + _dot(hs, h2) * (_dot(h1, h1) - _dot(h2, h2))
    x7 = _dot(hs, h1) ** 2 + _dot(hs, h2) ** 2
    return [
        dd ** 2,                                                         # lambda_1
        (_dot(h1, h2) - _dot(h2, h1)) ** 2,                              # lambda_2
        (_dot(h1, h1) - _dot(h2, h2)) ** 2 + (_dot(h1, h2) + _dot(h2, h1)) ** 2,  # lambda_3
        _dot(hs, hs) * dd,                                               # lambda_5
        _dot(hs, h1) * _dot(h1, hs) + _dot(hs, h2) * _dot(h2, hs),       # lambda_6
        _dot(hs, hs) ** 2,                                               # lambda_8
        x4 + x4.conjugate(), 1j * (x4 - x4.conjugate()),                 # Re, Im lambda_4
        x7 + x7.conjugate(), 1j * (x7 - x7.conjugate()),                 # Re, Im lambda_7
    ]


def _rank(rows, tol=1e-9):
    """Rank of a real matrix by Gaussian elimination with partial pivoting."""
    a = [list(r) for r in rows]
    rank, ncol = 0, len(a[0])
    for col in range(ncol):
        piv = max(range(rank, len(a)), key=lambda i: abs(a[i][col]), default=None)
        if piv is None or abs(a[piv][col]) < tol:
            continue
        a[rank], a[piv] = a[piv], a[rank]
        for i in range(len(a)):
            if i != rank:
                f = a[i][col] / a[rank][col]
                a[i] = [x - f * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def _solve(m, v):
    """Solve m x = v for a small dense real system."""
    n = len(v)
    a = [list(m[i]) + [v[i]] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda i: abs(a[i][c]))
        a[c], a[p] = a[p], a[c]
        for i in range(n):
            if i != c:
                f = a[i][c] / a[c][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[c])]
    return [a[i][n] / a[i][i] for i in range(n)]


def check_s3_potential():
    print("\n=== 8. S_3-symmetric potential (Exercise Set 9, Problem 5) ===")
    rng = random.Random(3)

    def rnd_config():
        return [[complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(2)] for _ in range(3)]

    ok_inv = ok_real = True
    for _ in range(10):
        h = rnd_config()
        base = _structures(h)
        ok_real &= all(abs(v.imag) < 1e-10 for v in base)
        for perm in itertools.permutations(range(3)):
            sp = _structures([h[i] for i in perm])
            ok_inv &= all(abs(a - b) < 1e-9 * max(1.0, abs(b)) for a, b in zip(sp, base))
    check("the ten quartic structures are real and S_3-invariant", ok_inv and ok_real)
    rows = [[v.real for v in _structures(rnd_config())] for _ in range(40)]
    check("the ten structures are linearly independent (rank 10)", _rank(rows) == 10)
    # character count: bilinears K_ij carry chi = (Tr P)^2 = 9, 1, 0
    chi = {"e": 9, "t": 1, "c": 0}
    chi_sq = {"e": 9, "t": 9, "c": 0}              # chi(g^2)
    sym2 = {g: (chi[g] ** 2 + chi_sq[g]) // 2 for g in chi}
    n_quartic = Fraction(sym2["e"] + 3 * sym2["t"] + 2 * sym2["c"], 6)
    n_quadratic = Fraction(chi["e"] + 3 * chi["t"] + 2 * chi["c"], 6)
    check("character count: 10 invariant quartics, 2 invariant mass terms",
          n_quartic == 10 and n_quadratic == 2)
    # leading-order minimum
    mu_s2, mu_d2 = 2.3, 1.1
    mu0 = [0.3, 0.7, 1.9]
    s = sum(mu0) / 3
    # mass matrix in the H_k basis: M^2 1 + m'^2 (J - 1), mu_S^2 = M^2 + 2m'^2, mu_D^2 = M^2 - m'^2
    mprime2 = (mu_s2 - mu_d2) / 3
    mdiag2 = mu_d2 + mprime2
    mass = [[mdiag2 if i == j else mprime2 for j in range(3)] for i in range(3)]
    direct = _solve(mass, mu0)
    formula = [s / mu_s2 + (m - s) / mu_d2 for m in mu0]
    check("leading-order minimum x_k^2 = s/mu_S^2 + d_k/mu_D^2",
          all(abs(a - b) < 1e-12 for a, b in zip(direct, formula)))
    # Q = 3/(1 + r^2)
    ok = True
    for r in (0.0, 0.3, 0.5, 0.9, 1.0, 1.2):
        x = z3_x(0.1, r)
        ok &= min(x) >= 0 and abs(koide_q(*(t * t for t in x)) - 3 / (1 + r * r)) < 1e-12
    check("Q = 3/(1 + r^2) for x_k = z_0 [1 + sqrt2 r cos(2 pi k/3 + delta)]", ok)
    check("S_3-symmetric soft terms (r = 0) give Q = 3; one direction gives Q = 1",
          abs(koide_q(1, 1, 1) - 3) < 1e-12 and abs(koide_q(1e-30, 1e-30, 1) - 1) < 1e-12)
    # Koide surface vector for delta = 2/9
    x2 = [t * t for t in z3_x(DELTA)]
    a = sum(x2) / 3
    b = [t / a - 1 for t in x2]
    amp = cmath.sqrt(2) * cmath.exp(1j * DELTA) + 0.5 * cmath.exp(-2j * DELTA)
    big_b, beta = abs(amp), cmath.phase(amp)
    print(f"  a = {a:.4f} (= 2 z_0^2), b_k/a = {b[0]:.4f}, {b[1]:.4f}, {b[2]:.4f}; B = {big_b:.4f}, beta = {beta:.4f}")
    check("a = 2 z_0^2 and b_k/a = (-0.9992, -0.8317, 1.8309)",
          abs(a - 2) < 1e-12 and all(abs(p - q) < 5e-5 for p, q in zip(b, (-0.9992, -0.8317, 1.8309))))
    check("B = (9/4 + sqrt2 cos 3 delta)^(1/2) = 1.833, beta = 0.053",
          abs(big_b ** 2 - (2.25 + math.sqrt(2) * math.cos(3 * DELTA))) < 1e-12
          and round(big_b, 3) == 1.833 and round(beta, 3) == 0.053
          and all(abs(b[k - 1] - big_b * math.cos(2 * math.pi * k / 3 + beta)) < 1e-12 for k in (1, 2, 3)))
    check("electron needs 1 + b_1/a = 8e-4", round(1 + b[0], 4) == 0.0008)


# ============================================================
# 9. Quoted values still present in the sources (drift guard)
# ============================================================
QUOTED = {
    LECTURE: [
        "1.500005", "1.5045 \\pm 0.010", "0.0045 \\pm 0.010", "0.004836", "0.05946",
        "1.0\\times10^{-5}", "2.1\\times10^{-5}", "38.2^\\circ", "2.7\\%", "37.2^\\circ",
        "N+2 = 7", "2N = 10", "N-2 = 3", "93.52", "1272.9", "m_b(m_b) = 4183",
        "m_s/m_d = 19.9", "factor of $4000$", "$15\\%$ off", "\\Lambda_S \\sim$ few~TeV",
        "\\Lambda_D \\sim 10^{11}", "Numerical match", "Exercise Set~9",
    ],
    EXERCISE: [
        "1.500004", "1.500005", "1.1\\times 10^{-5}", "1.5045", "0.010", "1.3675",
        "0.040350", "0.580212", "2.379438", "4.83628\\times10^{-3}", "5.94599\\times10^{-2}",
        "313.85", "(k_u,k_d,N) = (2,3,3)", "(\\Nc,\\Nf) = (3,5)", "b_0^{\\text{mag}} = 3(\\Nf-\\Nc) - \\Nf = 1",
        "-0.9992", "-0.8317", "1.8309", "= 1.833", "\\beta = 0.053", "8\\times10^{-4}",
        "Q = \\frac{3}{1+r^2}", "3\\cdot 5",
    ],
}


def check_quoted_strings():
    print("\n=== 9. Quoted values present in lecture-11.tex and exercise-09.tex ===")
    for path, needles in QUOTED.items():
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            check(f"read {os.path.relpath(path, ROOT)}", False, str(exc))
            continue
        missing = [n for n in needles if n not in text]
        check(f"{os.path.relpath(path, ROOT)}: {len(needles) - len(missing)}/{len(needles)} quoted values found",
              not missing, "missing: " + ", ".join(missing) if missing else "")


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 70)
    print("Koide / VEV-condition verification: Lecture 11 and Exercise Set 9")
    print("=" * 70)
    check_vev_condition()
    check_q_values()
    check_z3()
    check_casimirs()
    check_misc_numbers()
    check_closure_iss()
    check_s3_potential()
    check_quoted_strings()
    print()
    print("=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 70)
    if failed:
        print(f"\nFAILED: {failed} checks did not pass.")
        return 1
    print("\nALL CHECKS PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
