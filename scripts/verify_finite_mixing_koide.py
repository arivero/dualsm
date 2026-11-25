#!/usr/bin/env python3
"""
Finite-mixing Koide shift and common-mediator reconstruction (issue 3).

Recomputes every statement and number of the subsection "Finite mixing:
the exact Koide shift and the reconstructed mediator mass" in
papers/COMPOSITE-FLAVOUR-MATCHING.md for the aligned common-mediator block

    M_i = [[0, u x_i], [v x_i, M]],   u, v, x_i, M > 0,

with light and heavy singular values m_i < H_i, b = u v and
kappa = (u^2 + v^2) / (u v) >= 2:

  1. Closed forms. The rationalized light value
     F(t) = 2 u v t / (sqrt(M^2 + (u+v)^2 t) + sqrt(M^2 + (u-v)^2 t)),
     t = x^2, and H = u v t / F(t) reproduce the two block invariants
     (H m = u v t, H^2 + m^2 = M^2 + (u^2+v^2) t) and the eigenvalues of
     M_i M_i^dagger obtained by direct diagonalization.
  2. Forward chain Q(m^2) < Q(x^2) < Q(m) < Q(x) at every finite M,
     strict for masses that are not all equal (two equal seeds included),
     equality for equal seeds, and the limits M -> 0, M -> infinity.
  3. Heavy-branch lemma H_- < m < H_+ for every M > 0, on samples that
     include m > M.
  4. Inverse: T_i = m_i H_i(M, kappa); G_kappa(M) = Q(T) is strictly
     increasing with endpoints Q(m^2) and Q(m); bisection on
     G_kappa(M') = Q(x^2) returns the true M; the converse construction
     (rho, u, v, x_i) returns the light masses; kappa = 2 gives H = M + m.
  5. The 1/M expansion of G_kappa with remainder O((kappa m_max / M)^2).
  6. Charged leptons with q_star = 3/2: pole-mass numbers, the tau-mass
     threshold, and the one-loop QED common-scale values.
  7. The quoted numbers are present in the note.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA

Conventions:
    Q(z) = (sum_i sqrt(z_i))^2 / sum_i z_i, so Q(x^2) = (sum x)^2 / sum x^2
    Lepton masses: PDG 2024 pole masses [MeV]

Arithmetic in decimal at 50 digits. In double precision the light singular
value written as (tr - sqrt(tr^2 - 4 det))/2 cancels catastrophically for
m << H; every light value here uses the rationalized form.

Pure Python (decimal, math, random); no third-party packages.
"""

import os
import random
import sys
from decimal import Decimal as D, getcontext

getcontext().prec = 50

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
NOTE = os.path.join(ROOT, "papers", "COMPOSITE-FLAVOUR-MATCHING.md")

M_E, M_MU, M_TAU = D("0.51099895"), D("105.6583755"), D("1776.93")  # PDG 2024, MeV
DM_TAU = D("0.09")
M_Z = D("91187.6")
ALPHA = 1 / D("137.035999")
PI = D("3.14159265358979323846264338327950288419716939937511")

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


def Q(z):
    """Q(z) = (sum sqrt z_i)^2 / sum z_i."""
    return sum(t.sqrt() for t in z) ** 2 / sum(z)


def light(u, v, M, x):
    """Rationalized light singular value F(x^2)."""
    t = x * x
    return 2 * u * v * t / ((M * M + (u + v) ** 2 * t).sqrt() + (M * M + (u - v) ** 2 * t).sqrt())


def heavy(u, v, M, x):
    """Heavy singular value from H m = u v x^2."""
    return u * v * x * x / light(u, v, M, x)


def heavy_branch(m, M, kappa):
    """Both roots H_-, H_+ of H^2 - kappa m H + m^2 - M^2 = 0."""
    s = (4 * M * M + (kappa * kappa - 4) * m * m).sqrt()
    return (kappa * m - s) / 2, (kappa * m + s) / 2


def G(masses, M, kappa):
    """G_kappa(M) = Q(T), T_i = m_i H_+(m_i, M, kappa)."""
    return Q([m * heavy_branch(m, M, kappa)[1] for m in masses])


def solve_M(masses, kappa, q_star, lo=D("1e-30"), hi=D("1e30"), steps=400):
    """Bisection in log M for G_kappa(M) = q_star (G increasing)."""
    if not (G(masses, lo, kappa) < q_star < G(masses, hi, kappa)):
        return None
    for _ in range(steps):
        mid = (lo * hi).sqrt()
        if G(masses, mid, kappa) < q_star:
            lo = mid
        else:
            hi = mid
    return (lo * hi).sqrt()


def logu(rng, lo, hi):
    """Log-uniform Decimal on [10^lo, 10^hi]."""
    return D(10) ** D(repr(rng.uniform(lo, hi)))


def rel(a, b):
    return abs(a / b - 1)


TOL = D("1e-40")


# ============================================================
# 1. Closed forms against invariants and direct diagonalization
# ============================================================
def check_closed_forms():
    print("\n=== 1. Closed forms: invariants and direct diagonalization ===")
    rng = random.Random(3)
    worst_inv = worst_diag = D(0)
    for _ in range(1500):
        u, v, x = logu(rng, -2, 2), logu(rng, -2, 2), logu(rng, -2, 2)
        M = logu(rng, -3, 3)
        t = x * x
        m = light(u, v, M, x)
        # H from its second closed form, independent of H = u v t / m
        H = ((M * M + (u + v) ** 2 * t).sqrt() + (M * M + (u - v) ** 2 * t).sqrt()) / 2
        worst_inv = max(worst_inv, rel(H * m, u * v * t),
                        rel(H * H + m * m, M * M + (u * u + v * v) * t))
        # M M^dagger = [[u^2 t, u x M], [u x M, v^2 t + M^2]]
        a, c, d = u * u * t, u * x * M, v * v * t + M * M
        tr, det = a + d, a * d - c * c
        lam_p = (tr + (tr * tr - 4 * det).sqrt()) / 2
        lam_m = det / lam_p
        worst_diag = max(worst_diag, rel(m * m, lam_m), rel(H * H, lam_p))
        worst_diag = max(worst_diag, rel(H, heavy(u, v, M, x)))
    check("m H = u v t and m^2 + H^2 = M^2 + (u^2+v^2) t on 1500 samples", worst_inv < TOL,
          f"max rel. dev. {float(worst_inv):.1e}")
    # det = a d - c^2 loses up to ~12 digits to cancellation at large M, small x
    check("m^2, H^2 equal the eigenvalues of M M^dagger; both forms of H agree", worst_diag < D("1e-30"),
          f"max rel. dev. {float(worst_diag):.1e}")


# ============================================================
# 2. Forward chain and limits
# ============================================================
def chain(u, v, M, xs):
    ms = [light(u, v, M, x) for x in xs]
    return (Q([m * m for m in ms]), Q([x * x for x in xs]), Q(ms), Q(xs))


def check_forward_chain():
    print("\n=== 2. Forward chain Q(m^2) < Q(x^2) < Q(m) < Q(x) ===")
    rng = random.Random(33)
    ok = True
    for _ in range(1500):
        u, v, M = logu(rng, -2, 2), logu(rng, -2, 2), logu(rng, -3, 3)
        xs = [logu(rng, -2, 2) for _ in range(3)]
        a, b, c, d = chain(u, v, M, xs)
        ok &= a < b < c < d
    check("strict chain on 1500 random nondegenerate seeds", ok)

    a, b, c, d = chain(D(1), D(2), D(5), [D(1), D(1), D(3)])
    check("two equal seeds x = (1,1,3), (u,v,M) = (1,2,5): strict chain",
          a < b < c < d, f"Q(x^2) = {b:.4f}, Q(m) = {c:.4f}")
    check("  Q(x^2) = 2.2727 and Q(m) = 2.4666",
          round(b, 4) == D("2.2727") and round(c, 4) == D("2.4666"))

    a, b, c, d = chain(D("0.7"), D("3.1"), D("2.3"), [D("1.9")] * 3)
    check("equal seeds: all four values equal 3", all(abs(q - 3) < TOL for q in (a, b, c, d)))

    xs = [D("0.3"), D("1.1"), D("2.9")]
    _, qx2, qm_big, _ = chain(D(1), D(2), D("1e12"), xs)
    qm2_small, _, qm_small, _ = chain(D(1), D(2), D("1e-12"), xs)
    qx = Q(xs)
    check("M -> infinity: Q(m) -> Q(x^2) (leading seesaw value)", abs(qm_big - qx2) < D("1e-20"))
    check("M -> 0: m_i -> min(u,v) x_i, so Q(m) -> Q(x) and Q(m^2) -> Q(x^2)",
          abs(qm_small - qx) < D("1e-20") and abs(qm2_small - qx2) < D("1e-20"))


# ============================================================
# 3. Heavy-branch lemma
# ============================================================
def check_heavy_branch():
    print("\n=== 3. Heavy-branch lemma H_- < m < H_+ ===")
    m = light(D(1), D(1), D(1), D(5))
    check("u = v = M = 1, x = 5 gives m = 4.52 > M", round(m, 2) == D("4.52"), f"m = {m:.4f}")
    rng = random.Random(333)
    ok = True
    n_big = 0
    for _ in range(1500):
        u, v, x = logu(rng, -2, 2), logu(rng, -2, 2), logu(rng, -2, 2)
        M = logu(rng, -3, 3)
        kappa = (u * u + v * v) / (u * v)
        m, H = light(u, v, M, x), heavy(u, v, M, x)
        hm, hp = heavy_branch(m, M, kappa)
        n_big += m > M
        ok &= hm < m < hp and rel(H, hp) < TOL
    check(f"H_- < m < H_+ = H on 1500 samples ({n_big} with m > M)", ok and n_big > 100)


# ============================================================
# 4. Inverse map
# ============================================================
def check_inverse():
    print("\n=== 4. Inverse: monotone G_kappa, window, round trip, converse ===")
    rng = random.Random(3333)
    ok_mono = ok_end = ok_trip = ok_conv = True
    for _ in range(300):
        u, v = logu(rng, -1, 1), logu(rng, -1, 1)
        M = logu(rng, -2, 2)
        xs = [logu(rng, -1, 1) for _ in range(3)]
        kappa = (u * u + v * v) / (u * v)
        ms = [light(u, v, M, x) for x in xs]
        # monotonicity on a sorted random grid
        grid = sorted(logu(rng, -4, 4) for _ in range(12))
        vals = [G(ms, g, kappa) for g in grid]
        ok_mono &= all(p < q for p, q in zip(vals, vals[1:]))
        ok_end &= abs(G(ms, D("1e-25"), kappa) - Q([m * m for m in ms])) < D("1e-30")
        ok_end &= abs(G(ms, D("1e25"), kappa) - Q(ms)) < D("1e-20")
        # round trip
        M_rec = solve_M(ms, kappa, Q([x * x for x in xs]))
        ok_trip &= M_rec is not None and rel(M_rec, M) < D("1e-30")
        # converse construction with an arbitrary b
        b = logu(rng, -1, 1)
        rho = (kappa + (kappa * kappa - 4).sqrt()) / 2
        uu, vv = (b * rho).sqrt(), (b / rho).sqrt()
        T = [m * heavy_branch(m, M, kappa)[1] for m in ms]
        xx = [(t / b).sqrt() for t in T]
        ok_conv &= all(rel(light(uu, vv, M, x), m) < D("1e-35") for x, m in zip(xx, ms))
        ok_conv &= rel((uu * uu + vv * vv) / (uu * vv), kappa) < TOL
    check("G_kappa strictly increasing on 300 random 12-point grids", ok_mono)
    check("G_kappa(0+) = Q(m^2) and G_kappa(infinity) = Q(m)", ok_end)
    check("bisection on G_kappa(M') = Q(x^2) returns the true M (300 cases)", ok_trip)
    check("converse (rho, u, v, x_i) reproduces m_i and kappa for arbitrary b", ok_conv)

    ms = [D(1), D(2), D(5)]
    lo, hi = Q([m * m for m in ms]), Q(ms)
    check("no root outside the window", solve_M(ms, D(3), lo - D("1e-6")) is None
          and solve_M(ms, D(3), hi + D("1e-6")) is None)
    check("unique root inside the window", solve_M(ms, D(3), (lo + hi) / 2) is not None)
    ok = all(abs(heavy_branch(m, M, D(2))[1] - (M + m)) < TOL
             for m in (D("0.1"), D(1), D(30)) for M in (D("0.01"), D(1), D(100)))
    check("kappa = 2: H_+ = M + m exactly", ok)


# ============================================================
# 5. 1/M expansion
# ============================================================
def coefficient(ms):
    S = lambda p: sum(m ** p for m in ms)
    return S(D(2)) / S(D(1)) - S(D("1.5")) / S(D("0.5"))


def check_expansion():
    print("\n=== 5. 1/M expansion of G_kappa ===")
    ms, kappa = [D(1), D(2), D(5)], D(3)
    C = coefficient(ms)
    ratios = []
    for k in (3, 4, 5):
        M = D(10) ** k * kappa * max(ms)
        approx = Q(ms) * (1 - kappa / (2 * M) * C)
        ratios.append(abs(G(ms, M, kappa) - approx) / Q(ms) / (kappa * max(ms) / M) ** 2)
    check("remainder / (kappa m_max / M)^2 bounded and converging at three M",
          max(ratios) < 1 and abs(ratios[2] / ratios[1] - 1) < D("0.01"),
          ", ".join(f"{float(r):.4f}" for r in ratios))
    check("coefficient S2/S1 - S_{3/2}/S_{1/2} > 0", C > 0, f"{float(C):.5f}")


# ============================================================
# 6. Charged leptons
# ============================================================
def one_loop(m, mu):
    """m(mu) = m_pole [1 - (alpha/pi)(1 + (3/4) ln(mu^2/m^2))]."""
    return m * (1 - ALPHA / PI * (1 + D(3) / 4 * (mu * mu / (m * m)).ln()))


def tau_threshold():
    lo, hi = D(1700), D(1800)
    for _ in range(200):
        mid = (lo + hi) / 2
        if Q([M_E, M_MU, mid]) > D("1.5"):
            lo = mid
        else:
            hi = mid
    return lo


NUMBERS = {}


def check_leptons():
    print("\n=== 6. Charged leptons, q_star = 3/2 ===")
    ms = [M_E, M_MU, M_TAU]
    q, q2, C = Q(ms), Q([m * m for m in ms]), coefficient(ms)
    check("Q(m) = 1.5000050", round(q, 7) == D("1.5000050"), f"{q:.9f}")
    check("Q(m^2) = 1.119111", round(q2, 6) == D("1.119111"), f"{q2:.8f}")
    check("S2/S1 - S_{3/2}/S_{1/2} = 252.87 MeV", round(C, 2) == D("252.87"), f"{C:.4f}")
    roots = {k: solve_M(ms, D(k), D("1.5")) for k in (2, 3, 10, 100)}
    per_k = {k: r / k / 1000000 for k, r in roots.items()}
    check("M/kappa = 38.26 TeV at central m_tau", round(per_k[2], 2) == D("38.26"),
          f"{per_k[2]:.4f} TeV")
    check("same to four figures for kappa = 2, 3, 10, 100",
          len({round(r, 2) for r in per_k.values()}) == 1,
          ", ".join(f"{float(r):.4f}" for r in per_k.values()))
    check("M = 76.51 TeV at kappa = 2", round(roots[2] / 1000000, 2) == D("76.51"))
    r1 = solve_M([M_E, M_MU, M_TAU - DM_TAU], D(2), D("1.5")) / 2 / 1000000
    check("M/kappa = 11.57 TeV at m_tau - 1 sigma", round(r1, 2) == D("11.57"), f"{r1:.4f} TeV")
    thr = tau_threshold()
    check("a root exists only for m_tau < 1776.969 MeV", round(thr, 3) == D("1776.969"), f"{thr:.5f}")
    pull = (thr - M_TAU) / DM_TAU
    check("PDG central m_tau lies 0.43 sigma below the threshold", round(pull, 2) == D("0.43"))
    check("no root above the threshold",
          solve_M([M_E, M_MU, thr + D("0.001")], D(2), D("1.5")) is None)
    q_tau = Q([one_loop(m, M_TAU) for m in ms])
    q_z = Q([one_loop(m, M_Z) for m in ms])
    check("one-loop QED: Q = 1.49740 at mu = m_tau", round(q_tau, 5) == D("1.49740"), f"{q_tau:.7f}")
    check("one-loop QED: Q = 1.49736 at mu = M_Z", round(q_z, 5) == D("1.49736"), f"{q_z:.7f}")
    gap = D("1.5") - q_tau
    check("gap 3/2 - Q(m_tau) = 0.0026, about 240 times the pole uncertainty 0.000011",
          round(gap, 4) == D("0.0026") and 220 < gap / D("0.000011") < 250,
          f"{gap:.6f}, ratio {float(gap / D('0.000011')):.0f}")
    NUMBERS.update(q=q, q2=q2)


# ============================================================
# 7. Quoted strings
# ============================================================
QUOTED = [
    "1.5000050", "1.119111", "252.87", "38.26", "76.51", "11.57", "1776.969",
    "0.43", "1.49740", "1.49736", "0.0026", "2.2727", "2.4666", "4.52",
]


def check_quoted_strings():
    print("\n=== 7. Quoted values present in COMPOSITE-FLAVOUR-MATCHING.md ===")
    try:
        with open(NOTE, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        check("read note", False, str(exc))
        return
    missing = [n for n in QUOTED if n not in text]
    check(f"{len(QUOTED) - len(missing)}/{len(QUOTED)} quoted values found", not missing,
          "missing: " + ", ".join(missing) if missing else "")


def main():
    print("=" * 70)
    print("Finite-mixing Koide shift and common-mediator reconstruction")
    print("=" * 70)
    check_closed_forms()
    check_forward_chain()
    check_heavy_branch()
    check_inverse()
    check_expansion()
    check_leptons()
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
