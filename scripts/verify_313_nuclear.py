#!/usr/bin/env python3
"""Recalculate the nuclear part of papers/313-MEV-SCALE.md from unflagged AME2020 data.

The numerical mass unit is MeV; phase h has units MeV². The earlier nuclear study
used G_F=1.1663788e-5 GeV^-2; the electroweak and 313 spectroscopy note also reports
what changes with the PDG 2026 value. Stdlib only.
ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA
"""

import csv
import gzip
import sys
from math import acos, asin, asinh, degrees, hypot, log, pi, sqrt
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_313_scale import DATA, VEV, show
from verify_inverse_koide_scale import ALPHA0, M_Z26

U, ELECTRON = 931.49410242, 0.51099895
V = 1000 / sqrt(sqrt(2) * 1.1663788e-5)
D = 1864.84
ZPOLE = M_Z26 / hypot(1, 2495.5 / M_Z26)
FE, NI, NI64 = (32, 26), (34, 28), (36, 28)
P, N, HE, T, S = (0, 1), (1, 0), (2, 2), (82, 50), (132, 100)


def masses():
    data = {}
    with gzip.open(DATA / "ame2020.tsv.gz", "rt") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            n, z = int(row["N"]), int(row["Z"])
            electron_binding = (14.4381 * z**2.39 + 1.55468e-6 * z**5.35) * 1e-6
            data[n, z] = (
                (n + z) * U
                + float(row["atomic_excess_keV"]) / 1000
                - z * ELECTRON
                + electron_binding
            )
    assert len(data) == 2550
    return data


def covariance():
    codes = {sum(q) * 10000 + 10 * q[1]: q for q in (P, FE, NI, NI64)}
    matrix = {}
    with (DATA / "ame2020-covariance.tsv").open() as f:
        for r in csv.DictReader(f, delimiter="\t"):
            i, j = codes[int(r["nuclide_1"])], codes[int(r["nuclide_2"])]
            matrix[i, j] = matrix[j, i] = float(r["covariance_nano_u_squared"]) * (1e-9 * U) ** 2
    return matrix


def error(gradient):
    cov = covariance()
    return sqrt(
        sum(di * dj * cov[i, j] for i, di in gradient.items() for j, dj in gradient.items())
    )


def real_periods(m, q1, q2):
    n, z = q1
    p, w = q2
    det = n * w - p * z
    return (m[q1] * w - m[q2] * z) / det, (n * m[q2] - p * m[q1]) / det


def bound_rows(m):
    print("AME masses and sharp bounds")
    tin100, tin116 = m[50, 50], m[66, 50]
    v_higgs = 125130 + M_Z26
    show("Sn100,116,132 nuclear", tin100, tin116, m[T])
    show(
        "R1, R2, R3 fractional excess",
        V / (2 * m[T]) - 1,
        v_higgs / (tin100 + m[T]) - 1,
        2 * D / 3727.3794118 - 1,
    )
    show(
        "midpoint, nickel witness, stable witness",
        tin100 + m[T] - 2 * tin116,
        tin100 + m[T] - (13 * m[NI64] + 12 * m[38, 28]) / 7,
        tin100 + m[T] - (31 * m[NI64] + 12 * m[50, 36]) / 13,
    )
    for name, q, target, contacts in [
        ("100Sn", (50, 50), tin100, ((28, 28), (30, 28))),
        ("132Sn", T, m[T], ((50, 30), (50, 32))),
        ("pair", S, m[T] + tin100, (NI64, (38, 28))),
        ("alpha", HE, m[HE], ((28, 28), (30, 28))),
    ]:
        cn, cp = real_periods(m, *contacts)
        assert all(abs(n * cn + z * cp) <= mass + 1e-7 for (n, z), mass in m.items())
        ceiling = q[0] * cn + q[1] * cp
        show(name + " norm, mass minus norm", ceiling, target - ceiling)
    at100, at132 = (
        m[q] + q[1] * ELECTRON - (14.4381 * q[1] ** 2.39 + 1.55468e-6 * q[1] ** 5.35) * 1e-6
        for q in [(50, 50), T]
    )
    neutral25 = 91188.0 + 125200.0
    w_abs = sqrt((125200.0 - 91188.0) ** 2 - (at132 - at100) ** 2) / 2
    show("2025 two-level shift and w [GeV]", (neutral25 - at100 - at132) / 2000, w_abs / 1000)
    show(
        "historical crossings [%]",
        -100 * log(V / (2 * at132)) / 0.70,
        -100 * log(neutral25 / (at100 + at132)) / 0.70,
        -100 * log(2 * D / 3727.3794118) / 0.55,
    )
    show(
        "fixed-charge and fixed-mass coordinates; Fm ratio",
        52.7 * 222 / 90,
        52.7 * 238 / 92,
        125200 / U,
        131 * 365.25 * 86400 / 0.00037,
    )
    cap = V / 2 + 50 * D
    shift = V - 132 * D
    show(
        "Higgs alternatives BW: unit, aligned, EW",
        *(v / 1000 for v in (116 * D - M_Z26, cap - M_Z26, 29 * V / 33 - M_Z26)),
    )
    show(
        "Higgs aligned pole; v - 132 D, spacings",
        (cap - ZPOLE) / 1000,
        shift,
        shift / 2,
        25 * shift / 66,
    )
    atomic = lambda q: (
        m[q] + q[1] * ELECTRON - (14.4381 * q[1] ** 2.39 + 1.55468e-6 * q[1] ** 5.35) * 1e-6
    )
    show(
        "Higgs Th completion (nuclear), additive A (atomic) [GeV]",
        (2 * m[142, 90] - m[T] - m[60, 40] - ZPOLE) / 1000,
        (V - M_Z26 + atomic((50, 50)) - atomic(T)) / 1000,
    )
    for d in (D - 0.04, D, D + 0.04):
        dn = (V / 2 - 50 * d) / 32
        dp = d - dn
        k, q = max((abs(n * dn + z * dp) / mass, (n, z)) for (n, z), mass in m.items())
        show("aligned scale, limiter N,Z", k, *q)


class IronNickel:
    """Two exactly saturated nuclear masses with an arbitrary relative complex phase."""

    def __init__(self, iron, nickel):
        self.iron, self.nickel = iron, nickel

    def terms(self, q):
        n, z = q
        a = (28 * n - 34 * z) / 12
        b = (32 * z - 26 * n) / 12
        return a * self.iron + b * self.nickel, -a * b

    def norm(self, q, h):
        base, slope = self.terms(q)
        return sqrt(base * base + slope * h)

    def scaled(self, q, h):
        return V * self.norm(q, h) / (2 * self.norm(T, h))

    def interval(self, m):
        limits = [(4 * self.iron * self.nickel, None)]
        for q, mass in m.items():
            base, slope = self.terms(q)
            assert abs(base) <= mass + 1e-7
            if slope > 0:
                limits.append(((mass - base) * (mass + base) / slope, q))
        return min(limits)


def iron_nickel(m):
    print("\nIron and nickel")
    f, k = m[FE], m[NI]
    cal = IronNickel(f, k)
    hmax, limit = cal.interval(m)
    assert limit == P
    n, p = real_periods(m, FE, NI)
    binding = lambda q: (q[0] * 939.56542194 + q[1] * 938.27208943 - m[q]) / sum(q)
    assert sorted(m, key=binding, reverse=True)[:2] == [NI, FE]
    show("B/A Ni, Fe; c_n, c_p; mu_e", binding(NI), binding(FE), n, p, n - p)
    for q1, q2 in [((30, 26), NI), (NI, FE), (FE, NI64)]:
        nn, pp = real_periods(m, q1, q2)
        assert all(abs(i * nn + j * pp) <= mass + 1e-7 for (i, j), mass in m.items())
        show("contact slope, aligned charm", nn - pp, V * (nn + pp) / (2 * (82 * nn + 50 * pp)))
    show("h limit, theta max [degrees]", hmax, degrees(2 * asin(sqrt(hmax / (4 * f * k)))))
    for h in (0, hmax):
        show(
            "D, H_BW, H_pole [last two GeV]",
            cal.scaled(HE, h) / 2,
            (cal.scaled(S, h) - M_Z26) / 1000,
            (cal.scaled(S, h) - ZPOLE) / 1000,
        )
    a, ba = cal.terms(HE)
    t, bt = cal.terms(T)
    s, bs = cal.terms(S)
    g = (bs - (s / t) ** 2 * bt) / (ba - (a / t) ** 2 * bt)
    assert ba - (a / t) ** 2 * bt < 0 and bs - (s / t) ** 2 * bt < 0
    show("squared-ratio slope, aligned dH/dD", g, 2 * g * a / s)
    upper = cal.scaled(HE, 0) / 2
    r = k / f
    sensitivity = r / (r - 1) + 133 * r / (149 - 133 * r)
    sigma_n = error({FE: -upper * sensitivity / f, NI: upper * sensitivity / k})
    sigma_g = upper * 6e-12 / (2 * 1.1663788e-5)
    show(
        "D ceiling with 2026 GF; sensitivity; errors [keV]",
        upper * VEV / V,
        sensitivity,
        1000 * sigma_n,
        1000 * sigma_g,
        1000 * hypot(sigma_n, sigma_g),
    )
    r_needed = (596 * D + 3 * V) / (532 * D + 3 * V)
    softened = IronNickel(k / r_needed, k)
    assert abs(softened.scaled(HE, 0) / 2 - D) < 1e-7
    softened.interval(m)
    show(
        "Fe slack and excess [keV], sigma for 3 s.d.",
        1000 * (f - k / r_needed),
        1000 * (D - upper),
        1000 * sqrt(((D - upper) / 3) ** 2 - sigma_n**2 - sigma_g**2),
    )
    return cal, hmax


def physical_controls(cal, hmax):
    print("\nPhysical p, n and helium controls")
    with (DATA / "codata2022-rest-masses.tsv").open() as f:
        reference = {
            row["particle"]: float(row["mass_MeV"]) for row in csv.DictReader(f, delimiter="\t")
        }
    p, n, alpha, d, t, he3 = (
        reference[key]
        for key in ("proton", "neutron", "alpha_particle", "deuteron", "triton", "helion")
    )
    bd = p + n - d
    show("pair thresholds p, n, alpha, D", 2 * p, 2 * n, 2 * alpha, 2 * D)
    show("per valence slot free, helium, charm", 2 * (p + n) / 12, alpha / 12, D / 6)
    show(
        "free quartet, B_alpha, charm excess, B_d",
        2 * (p + n),
        2 * (p + n) - alpha,
        2 * D - alpha,
        bd,
    )
    sep = alpha + cal.iron - cal.nickel
    show(
        "separation, scale shift, net charm excess",
        sep,
        cal.scaled(HE, 0) - cal.norm(HE, 0),
        cal.scaled(HE, 0) - alpha,
    )
    for h in (0, hmax):
        k = V / (2 * cal.norm(T, h))
        show(
            "kappa, scaled proton, neutron, alpha",
            k,
            cal.scaled(P, h),
            cal.scaled(N, h),
            cal.scaled(HE, h),
        )
        area_sq = h * (cal.iron * cal.nickel - h / 4) / 144
        show("symmetry curvature [MeV]", area_sq / (8 * (cal.norm(HE, h) / 4) ** 3))
    n0, bn = cal.terms(N)
    p0, bp = cal.terms(P)
    ratio = (n / p) ** 2
    h = (ratio * p0 * p0 - n0 * n0) / (bn - ratio * bp)
    k = p / cal.norm(P, h)
    assert 0 < h < hmax and abs(k * cal.norm(N, h) - n) < 1e-7
    show(
        "free nucleon calibration: h, kappa, v [GeV], D",
        h,
        k,
        2 * k * cal.norm(T, h) / 1000,
        k * cal.norm(HE, h) / 2,
    )
    inner = ((alpha / 2) ** 2 - n * n - p * p) / 2

    def length(q):
        i, j = q
        return sqrt((i * n) ** 2 + (j * p) ** 2 + 2 * i * j * inner)

    mstar = 2 * length(T) / 132
    x = 8 / 33
    u = alpha / 2
    show(
        "light Gram: angle, m*, linear, quadratic",
        degrees(acos(inner / (n * p))),
        mstar,
        2 * x * (n * n - p * p) / (mstar + u),
        x * x * (2 * (n * n + p * p) - u * u) / (mstar + u),
    )
    free_v_charm = sqrt(((V / 2) ** 2 - 32 * (82 * n * n - 50 * p * p)) / (82 * 50))
    show(
        "light Gram: v [GeV], deficit; free-v charm",
        2 * length(T) / 1000,
        V - 2 * length(T),
        free_v_charm,
    )
    show(
        "mirror splitting: proxy, actual, correction",
        length((2, 1)) - length((1, 2)),
        t - he3,
        t - he3 - length((2, 1)) + length((1, 2)),
    )
    dtarget = (alpha + bd) / 2
    ratio = (4 * dtarget / V) ** 2
    a, ba = cal.terms(HE)
    tin, bt = cal.terms(T)
    h = (ratio * tin * tin - a * a) / (ba - ratio * bt)
    assert 0 < h < hmax
    show(
        "B_d completion: D, h, H_BW and pole [GeV]",
        dtarget,
        h,
        (cal.scaled(S, h) - M_Z26) / 1000,
        (cal.scaled(S, h) - ZPOLE) / 1000,
    )


def root(f, lo, hi):
    assert f(lo) < 0 < f(hi)
    for _ in range(70):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def plasma_case(m, lattice, exchange, screen):
    yf, yn, y64 = 26 / 58, 28 / 62, 28 / 64
    eta = (m[NI64] / 64 - m[NI] / 62) / (yn - y64)
    X = 1 + exchange * ALPHA0 / (2 * pi)

    def coeff(z):
        polar = (
            ALPHA0
            * 12 ** (4 / 3)
            / (35 * pi ** (1 / 3))
            * (1 - 1.1866 * z ** (-0.267) + 0.27 / z)
            * z ** (2 / 3)
        )
        return (
            -lattice
            * 1.4442307515
            * ALPHA0
            * (3 * pi * pi) ** (-1 / 3)
            * z ** (2 / 3)
            * (1 + screen * polar)
        )

    def pressure(z, x):
        return (
            ELECTRON**4
            / pi**2
            * (X / 8 * (x * (2 * x * x / 3 - 1) * hypot(1, x) + asinh(x)) + coeff(z) * x**4 / 9)
        )

    def term(z, x):
        return ELECTRON * (X * hypot(1, x) + 4 / 3 * coeff(z) * x)

    xni = root(lambda x: term(28, x) - eta, 0.2, 12)
    pres = pressure(28, xni)
    xfe = root(lambda x: pressure(26, x) - pres, 0.2, 12)
    gap = m[FE] / 58 - m[NI] / 62 + yf * term(26, xfe) - yn * eta
    slope = (yf * (xni / xfe) ** 3 - yn) / (yn - y64)
    sigma = error({FE: 1 / 58, NI: -(1 + slope) / 62, NI64: slope / 64})
    show(
        f"lattice/exchange/screen {lattice}/{exchange}/{screen}",
        pres / 197.3269804**3,
        1e6 * gap,
        1e6 * sigma,
    )


if __name__ == "__main__":
    table = masses()
    bound_rows(table)
    calibration, phase_max = iron_nickel(table)
    physical_controls(calibration, phase_max)
    print("\nCold pure-phase control: pressure [MeV/fm^3], gap and nuclear sigma [eV/baryon]")
    for settings in ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)):
        plasma_case(table, *settings)
