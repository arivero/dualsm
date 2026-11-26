#!/usr/bin/env python3
"""
Charged-meson mass cross-ratios near flavour symmetry (issue 5).

Recomputes every statement and number of the subsection "What six charged
masses test" and its continuation "The first departure from factorization"
in papers/paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md.

On the full-rank branch m_i h_i = S, S^3 = Lambda^4 det m, the canonical
charged masses are m_ij = |mu|^2 |m_i m_j / S| / Z_ij with
Z_ij = sqrt(kappa_ij kappa_ji). With m_i = m0 exp(delta_i),

    F_jk = log R_jk,  R_jk = m_uj m_ck / (m_uk m_cj),  (j, k) = (d, s), (d, b).

  1. Reconstruction from six masses: the holomorphic factors, S and the
     overall normalization cancel, F_jk = z_uk + z_cj - z_uj - z_ck with
     z = log Z, for random masses and metrics.
  2. Symmetry: for a metric covariant under all flavour permutations
     (built from the vacuum values w_i = log h_i), F vanishes whenever
     delta_u = delta_c or delta_j = delta_k, for random spectators; it is odd
     under u <-> c and under j <-> k; s <-> b maps F_ds onto F_db.
  3. Quadratic order: the four-corner difference converges to
     C = -[(d_u - d_c)(d_j - d_k) z_uj]_0, the same for both ratios, with an
     error of order x^2 + y^2; the predicted C from the second derivatives
     of the model metric agrees.
  4. Effective kinetic term K_2 = tr(Phi^+ Phi + lambda Phi^+ D Phi D):
     kappa_ij = 1 + lambda delta_i delta_j, positive for |lambda| |delta|^2 < 1,
     and C = -lambda for both ratios with holomorphic inputs fixed.
  5. Controls: Z_aj = A_a B_j gives (R_ds, R_db) = (1, 1) exactly; rescaling
     only Z_us by q sends them to (q R_ds, R_db).
  6. One-loop magnetic estimate: for K = tr f(M^+ M) at a positive diagonal
     vacuum the off-diagonal metric is the divided difference of x f'(x)
     (checked against numerical second derivatives of the matrix function);
     for f = x - eps x log x this gives C = -2 eps / 3.
  7. The quoted numbers are present in the note.

Python 3 standard library (decimal, math, random, cmath). The matrix check in
part 6 uses a small Hermitian eigenvalue routine written here (Jacobi
rotations), so no third-party package is needed.
"""

import cmath
import math
import os
import random
import sys
from decimal import Decimal as D, getcontext

getcontext().prec = 60

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
NOTE = os.path.join(ROOT, "papers", "paper-2-meson-mass-sum-rules", "FIVE-FLAVOUR-MATCHING.md")

FLAV = ["u", "c", "d", "s", "b"]
UP, DOWN = ["u", "c"], ["d", "s", "b"]

passed = 0
failed = 0


def check(description, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
    else:
        failed += 1
    detail_str = f"  [{detail}]" if detail else ""
    print(f"  [{'PASS' if condition else 'FAIL'}] {description}{detail_str}")
    return condition


# ------------------------------------------------------------ vacuum and masses
def vacuum_logs(delta):
    """w_i = log h_i up to a common constant: log S = sum(delta)/3, h_i = S/m_i."""
    s = sum(delta.values()) / 3
    return {f: s - delta[f] for f in FLAV}


def canonical_masses(delta, kappa, m0=D(1), lam4=D(1), mu2=D(1)):
    """m_ij = |mu|^2 m_i m_j / (S Z_ij) on the full-rank branch."""
    m = {f: m0 * delta[f].exp() for f in FLAV}
    det = m["u"] * m["c"] * m["d"] * m["s"] * m["b"]
    S = (lam4 * det).ln() / 3
    S = S.exp()
    out = {}
    for a in UP:
        for j in DOWN:
            Z = (kappa(a, j, delta) * kappa(j, a, delta)).sqrt()
            out[(a, j)] = mu2 * m[a] * m[j] / (S * Z)
    return out


def F(masses, j, k):
    return (masses[("u", j)] * masses[("c", k)] / (masses[("u", k)] * masses[("c", j)])).ln()


# ------------------------------------------------------------ a covariant model metric
COEF = dict(al=D("0.3"), be=D("-0.7"), ga=D("1.1"), rho=D("0.45"), tau=D("-0.25"),
            sig=D("0.6"), cub=D("0.9"), quart=D("0.5"), anti=D("0.8"))


def z_model(a, b, delta):
    """Symmetric, permutation-covariant log metric of the pair (a, b)."""
    w = vacuum_logs(delta)
    wa, wb = w[a], w[b]
    others = [w[o] for o in FLAV if o not in (a, b)]
    so = sum(others)
    c = COEF
    return (c["al"] * (wa + wb) + c["be"] * (wa * wa + wb * wb) + c["ga"] * wa * wb
            + c["rho"] * (wa + wb) * so + c["tau"] * so * so
            + c["sig"] * sum(o * o for o in others) + c["cub"] * wa * wb * (wa + wb + so)
            + c["quart"] * wa * wb * (wa * wa + wb * wb))


def kappa_model(a, b, delta):
    """kappa_ab = exp(z_ab + antisymmetric part); only the product kappa_ab kappa_ba enters."""
    w = vacuum_logs(delta)
    return (z_model(a, b, delta) + COEF["anti"] * (w[a] - w[b])).exp()


def predicted_C_model():
    """C = -[(d_u - d_c)(d_j - d_k) z_uj] at 0, using d w_i / d delta_p = 1/3 - [i = p].

    (d_u - d_c) and (d_j - d_k) change w by -e_u + e_c and -e_j + e_k. The second
    derivative of z_uj along v1 = -e_u + e_c, v2 = -e_j + e_k at w = 0:
    v1 has w_a-component -1 and an 'other' component +1 (c); v2 has w_b-component -1
    and an 'other' component +1 (k).
    """
    c = COEF
    # Hessian entries of z_ab at w = 0 (quadratic part only):
    #   d2/dwa dwb = ga ; d2/dwa do = rho ; d2/dwb do = rho ; d2/do do' (o != o') = 2 tau ;
    #   d2/do^2 = 2 tau + 2 sig.  The cubic and quartic terms have no second derivative at 0.
    # v1 . Hess . v2 with v1 = (-1 at a, +1 at c), v2 = (-1 at b, +1 at k), c != k:
    val = (-1) * (-1) * c["ga"] + (-1) * (+1) * c["rho"] + (+1) * (-1) * c["rho"] + (+1) * (+1) * 2 * c["tau"]
    return -val


def mixed_derivative(fun, h=D("1e-12")):
    """Second mixed derivative along (e_u - e_c) and (e_j - e_k) by central differences."""
    tot = D(0)
    for s1 in (1, -1):
        for s2 in (1, -1):
            tot += s1 * s2 * fun(s1 * h, s2 * h)
    return tot / (4 * h * h)


def corner(fun, x, y):
    """Four-corner difference sum_{eps,eta} eps eta F(eps x, eta y) / (4 x y)."""
    tot = D(0)
    for e in (1, -1):
        for n in (1, -1):
            tot += e * n * fun(e * x, n * y)
    return tot / (4 * x * y)


def split(x, y, j, k):
    delta = {f: D(0) for f in FLAV}
    delta["u"], delta["c"] = x / 2, -x / 2
    delta[j], delta[k] = y / 2, -y / 2
    return delta


# ============================================================
def part1():
    print("\n=== 1. Reconstruction from the six canonical masses ===")
    rng = random.Random(5)
    worst = D(0)
    for _ in range(200):
        delta = {f: D(repr(rng.uniform(-0.8, 0.8))) for f in FLAV}
        kv = {(a, b): D(repr(rng.uniform(0.2, 5))) for a in FLAV for b in FLAV if a != b}
        kap = lambda a, b, d: kv[(a, b)]
        m0, lam4, mu2 = (D(repr(rng.uniform(0.1, 10))) for _ in range(3))
        ms = canonical_masses(delta, kap, m0, lam4, mu2)
        for j, k in (("d", "s"), ("d", "b")):
            z = {(a, b): (kv[(a, b)] * kv[(b, a)]).ln() / 2 for (a, b) in kv}
            direct = z[("u", k)] + z[("c", j)] - z[("u", j)] - z[("c", k)]
            worst = max(worst, abs(F(ms, j, k) - direct))
    check("F_jk = z_uk + z_cj - z_uj - z_ck for random masses, metrics and normalizations",
          worst < D("1e-50"), f"max error {float(worst):.1e}")


def part2():
    print("\n=== 2. Permutation symmetry and the two vanishing tests ===")
    rng = random.Random(7)
    worst_uc = worst_jk = worst_odd = worst_map = D(0)
    for _ in range(200):
        delta = {f: D(repr(rng.uniform(-0.5, 0.5))) for f in FLAV}
        for j, k in (("d", "s"), ("d", "b")):
            d1 = dict(delta); d1["c"] = d1["u"]
            worst_uc = max(worst_uc, abs(F(canonical_masses(d1, kappa_model), j, k)))
            d2 = dict(delta); d2[k] = d2[j]
            worst_jk = max(worst_jk, abs(F(canonical_masses(d2, kappa_model), j, k)))
            d3 = dict(delta); d3["u"], d3["c"] = delta["c"], delta["u"]
            f0 = F(canonical_masses(delta, kappa_model), j, k)
            worst_odd = max(worst_odd, abs(F(canonical_masses(d3, kappa_model), j, k) + f0))
            d4 = dict(delta); d4[j], d4[k] = delta[k], delta[j]
            worst_odd = max(worst_odd, abs(F(canonical_masses(d4, kappa_model), j, k) + f0))
        d5 = dict(delta); d5["s"], d5["b"] = delta["b"], delta["s"]
        worst_map = max(worst_map, abs(F(canonical_masses(d5, kappa_model), "d", "b")
                                       - F(canonical_masses(delta, kappa_model), "d", "s")))
    check("F_jk = 0 when delta_u = delta_c, any spectators", worst_uc < D("1e-45"), f"{float(worst_uc):.1e}")
    check("F_jk = 0 when delta_j = delta_k, any spectators", worst_jk < D("1e-45"), f"{float(worst_jk):.1e}")
    check("F_jk odd under u <-> c and under j <-> k", worst_odd < D("1e-45"), f"{float(worst_odd):.1e}")
    check("s <-> b maps F_ds onto F_db", worst_map < D("1e-45"), f"{float(worst_map):.1e}")


def part3():
    print("\n=== 3. Quadratic order and the common coefficient ===")
    Cpred = predicted_C_model()
    for j, k in (("d", "s"), ("d", "b")):
        Cz = -mixed_derivative(lambda a, b: z_model("u", j, {**{f: D(0) for f in FLAV},
                                                            "u": a, "c": -a, j: b, k: -b}))
        # With delta_u = a, delta_c = -a, delta_j = b, delta_k = -b: d/da = d_u - d_c, d/db = d_j - d_k.
        check(f"C from -(d_u-d_c)(d_j-d_k) z_uj equals the model prediction ({j}{k})",
              abs(Cz - Cpred) < D("1e-15"), f"{float(Cz):.12f} vs {float(Cpred):.12f}")
        Ffun = lambda x, y: F(canonical_masses(split(x, y, j, k), kappa_model), j, k)
        errs = []
        for t in (D("0.2"), D("0.1"), D("0.05"), D("0.025")):
            est = corner(Ffun, t, t)
            errs.append(abs(est - Cpred))
        ratios = [float(errs[i] / errs[i + 1]) for i in range(3)]
        check(f"four-corner difference -> C for R_{j}{k}, error O(x^2 + y^2)",
              errs[-1] < D("2e-3") and all(3.5 < r < 4.5 for r in ratios),
              f"errors {[f'{float(e):.2e}' for e in errs]}, successive ratios {[round(r, 2) for r in ratios]}")
        aniso = abs(corner(Ffun, D("0.02"), D("0.001")) - Cpred)
        check(f"independent shrinking (x = 0.02, y = 0.001) for R_{j}{k}", aniso < D("1e-3"), f"{float(aniso):.1e}")
        # No linear term: F/(|delta|) -> 0 along a generic direction.
        lin = max(abs(F(canonical_masses({f: t * D(c) for f, c in zip(FLAV, ("0.3", "-0.7", "0.5", "0.2", "-0.4"))},
                                         kappa_model), j, k)) / t for t in (D("1e-6"),))
        check(f"no linear term in F_{j}{k}", lin < D("1e-5"), f"F/t at t = 1e-6: {float(lin):.1e}")
    print(f"  model coefficient C = {float(Cpred):.6f}")


def part4():
    print("\n=== 4. The effective kinetic term K_2 with coefficient lambda ===")
    for lam in (D("0.7"), D("-1.3")):
        kap = lambda a, b, d, lam=lam: 1 + lam * d[a] * d[b]
        rng = random.Random(11)
        ok = True
        for _ in range(300):
            delta = {f: D(repr(rng.uniform(-0.5, 0.5))) for f in FLAV}
            norm2 = sum(v * v for v in delta.values())
            if abs(lam) * norm2 < 1:
                ok &= all(kap(a, b, delta) > 0 for a in FLAV for b in FLAV if a != b)
        check(f"kappa_ij = 1 + lambda delta_i delta_j > 0 for |lambda||delta|^2 < 1 (lambda = {lam})", ok)
        for j, k in (("d", "s"), ("d", "b")):
            Ffun = lambda x, y, kap=kap: F(canonical_masses(split(x, y, j, k), kap), j, k)
            est = corner(Ffun, D("0.001"), D("0.001"))
            check(f"C = -lambda for R_{j}{k}", abs(est + lam) < D("1e-6"), f"{float(est):.9f}")


def part5():
    print("\n=== 5. Controls ===")
    rng = random.Random(13)
    worst1 = worst2 = D(0)
    for _ in range(100):
        A = {a: D(repr(rng.uniform(0.3, 3))) for a in UP}
        B = {j: D(repr(rng.uniform(0.3, 3))) for j in DOWN}
        delta = {f: D(repr(rng.uniform(-0.6, 0.6))) for f in FLAV}
        # Factorized Z_aj = A_a B_j realized as kappa_aj = kappa_ja = A_a B_j.
        kapf = lambda a, b, d: A[a] * B[b] if a in UP else A[b] * B[a]
        ms = canonical_masses(delta, kapf)
        worst1 = max(worst1, abs(F(ms, "d", "s")), abs(F(ms, "d", "b")))
        q = D(repr(rng.uniform(0.2, 5)))
        kapq = lambda a, b, d: kappa_model(a, b, d) * (q if {a, b} == {"u", "s"} else 1)
        m1, m2 = canonical_masses(delta, kappa_model), canonical_masses(delta, kapq)
        Rds1, Rdb1 = F(m1, "d", "s").exp(), F(m1, "d", "b").exp()
        Rds2, Rdb2 = F(m2, "d", "s").exp(), F(m2, "d", "b").exp()
        worst2 = max(worst2, abs(Rds2 / (q * Rds1) - 1), abs(Rdb2 / Rdb1 - 1))
    check("Z_aj = A_a B_j gives (R_ds, R_db) = (1, 1)", worst1 < D("1e-50"), f"{float(worst1):.1e}")
    check("rescaling only Z_us by q gives (q R_ds, R_db)", worst2 < D("1e-50"), f"{float(worst2):.1e}")


# ------------------------------------------------------------ part 6: matrix Kahler metric
def jacobi_eigvals(Hm, sweeps=60):
    """Eigenvalues of a Hermitian matrix (list of lists of complex) by complex Jacobi rotations."""
    n = len(Hm)
    A = [row[:] for row in Hm]
    for _ in range(sweeps):
        off = sum(abs(A[p][q]) ** 2 for p in range(n) for q in range(n) if p != q)
        if off < 1e-30:
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = A[p][q]
                if abs(apq) < 1e-300:
                    continue
                phase = apq / abs(apq)
                theta = 0.5 * math.atan2(2 * abs(apq), (A[q][q] - A[p][p]).real)
                c, s = math.cos(theta), math.sin(theta)
                # Rotation G with G[p][p] = c, G[p][q] = s*phase, G[q][p] = -s*conj(phase), G[q][q] = c.
                for r in range(n):
                    arp, arq = A[r][p], A[r][q]
                    A[r][p] = c * arp - s * phase.conjugate() * arq
                    A[r][q] = s * phase * arp + c * arq
                for r in range(n):
                    apr, aqr = A[p][r], A[q][r]
                    A[p][r] = c * apr - s * phase * aqr
                    A[q][r] = s * phase.conjugate() * apr + c * aqr
    return [A[i][i].real for i in range(n)]


def trace_f(M, f):
    n = len(M)
    X = [[sum(M[k][i].conjugate() * M[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return sum(f(x) for x in jacobi_eigvals(X))


def kahler_metric_numeric(h, i, j, f, step=1e-4):
    """g = d^2 K / dt dtbar at t = 0 for M = diag(h) + t E_ij, t = a + i b."""
    n = len(h)

    def K(a, b):
        M = [[complex(h[r]) if r == s else 0j for s in range(n)] for r in range(n)]
        M[i][j] += complex(a, b)
        return trace_f(M, f)
    k0 = K(0, 0)
    d2a = (K(step, 0) - 2 * k0 + K(-step, 0)) / step ** 2
    d2b = (K(0, step) - 2 * k0 + K(0, -step)) / step ** 2
    return (d2a + d2b) / 4


def divided(g, x, y):
    return (g(x) - g(y)) / (x - y) if abs(x - y) > 1e-12 else None


def part6():
    print("\n=== 6. Kahler metric of tr f(M^+ M) and the one-loop magnetic estimate ===")
    h = [0.7, 1.3, 1.9]
    for name, f, xfp in (("2 sqrt(x)", lambda x: 2 * math.sqrt(max(x, 0)), lambda x: math.sqrt(x)),
                         ("x log x", lambda x: x * math.log(x) if x > 0 else 0.0, lambda x: x * (math.log(x) + 1))):
        worst = 0.0
        for (i, j) in ((0, 1), (1, 2), (2, 0)):
            num = kahler_metric_numeric(h, i, j, f)
            ana = divided(xfp, h[i] ** 2, h[j] ** 2)
            worst = max(worst, abs(num / ana - 1))
        check(f"off-diagonal metric of tr f(M^+M) = divided difference of x f'(x), f = {name}",
              worst < 1e-4, f"max relative deviation {worst:.1e}")
    check("f = 2 sqrt(x) gives the classical metric 1/(h_i + h_j)",
          abs(divided(lambda x: math.sqrt(x), 0.49, 1.69) - 1 / (0.7 + 1.3)) < 1e-12)

    def kapcl(a, b, delta):
        w = vacuum_logs(delta)
        return 1 / (w[a].exp() + w[b].exp())
    est = corner(lambda x, y: F(canonical_masses(split(x, y, "d", "s"), kapcl), "d", "s"), D("0.001"), D("0.001"))
    check("pair-local metric 1/(h_i + h_j) gives C = -1/4", abs(est + D("0.25")) < D("1e-6"), f"{float(est):.9f}")

    # One loop: f = x - eps x log x  =>  k(x_i, x_j) = 1 - eps (1 + L(x_i, x_j)), L = (x log x)^[1].
    eps = D("0.01")

    def Lfun(x, y):
        if x == y:
            return x.ln() + 1
        return (x * x.ln() - y * y.ln()) / (x - y)

    def kap1(a, b, delta):
        w = vacuum_logs(delta)
        xa, xb = (2 * w[a]).exp(), (2 * w[b]).exp()
        return 1 - eps * (1 + Lfun(xa, xb))
    for j, k in (("d", "s"), ("d", "b")):
        Ffun = lambda x, y: F(canonical_masses(split(x, y, j, k), kap1), j, k)
        est = corner(Ffun, D("0.002"), D("0.002"))
        # k = 1 - eps (1 + L); at the symmetric point L = 1, d_w L = 1, d_wa d_wb L = -2/3, so
        # C = -d_a d_b log k = -(2 eps/3)/(1 - 2 eps) + eps^2/(1 - 2 eps)^2.
        exact = -(2 * eps / 3) / (1 - 2 * eps) + eps * eps / (1 - 2 * eps) ** 2
        check(f"one-loop magnetic estimate: C = -2 eps/3 to first order in eps (R_{j}{k})",
              abs(est - exact) < D("1e-7") and abs(est / (-2 * eps / 3) - 1) < D("0.05"),
              f"C = {float(est):.8f}, closed form {float(exact):.8f}, -2 eps/3 = {float(-2 * eps / 3):.8f}")
    print(f"  with eps = N_m y^2/(32 pi^2), N_m = 2: C = -y^2/(24 pi^2) = {float(-1 / (24 * D(math.pi) ** 2)):.6f} y^2")


def part7():
    print("\n=== 7. Quoted values present in the note ===")
    text = open(NOTE, encoding="utf-8").read()
    quoted = ["C=-\\lambda", "-2\\epsilon/3", "y^2/(24\\pi^2)", "x^2+y^2", "(qR_{ds},R_{db})",
              "1/(h_i+h_j)", "C=-1/4"]
    missing = [q for q in quoted if q not in text]
    check(f"{len(quoted) - len(missing)}/{len(quoted)} quoted expressions found", not missing, f"missing {missing}")


if __name__ == "__main__":
    for part in (part1, part2, part3, part4, part5, part6, part7):
        part()
    print("\n" + "=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 70)
    sys.exit(1 if failed else 0)
