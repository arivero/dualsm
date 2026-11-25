#!/usr/bin/env python3
"""
Inverse-Koide scale test (issue 4): what fixes M = sqrt(C_ell C_d)?

Recomputes every number of papers/INVERSE-KOIDE-SCALE.md:

  1. Definitions and the image identity. C_ell = (sum sqrt m_l)^2 / 9,
     C_d = 9 / (sum m_i^{-1/2})^2, and for m~_i = M^2/m_i the Koide
     normalization of m~ equals M^2/C_d for every M > 0. The mixed-scale
     values for the issue inputs and the Lecture 11 inputs.
  2. Four-loop MS-bar running with two-loop decoupling at m_b and m_t:
     alpha_s at 2 GeV and m_b, the universal factor c(mu), its loop-order
     sequence, and the Paper 2 table at mu = m_t to 0.2%.
  3. The RG orbit: Q(1/m), the Koide phase and the weights w_i are the same
     at every common scale; C_d and M_match at 2 GeV, 3 GeV, m_b, M_Z, m_t;
     the slope at 2 GeV; the crossing scale mu_* with f_pi and its error
     from the mass errors, f_pi and alpha_s(M_Z).
  4. Literal seesaw: off-diagonal entries for all six pairings, the spread
     as a function of kappa >= 2, common-scale spreads, and the light values
     from a common off-diagonal f_pi.
  5. Direct image M^2/m_i: ratio and phase tests.
  6. Reference scales and the chiral-limit numbers.
  7. Quoted values present in the note.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA

Conventions:
    Q(z) = (sum sqrt z_i)^2 / sum z_i; Koide phase delta from
    sqrt z_k = z_0 (1 + sqrt2 r cos(2 pi k/3 + delta)), k = 1, 2, 3 in
    increasing order of z_k.
    a = alpha_s / pi; da/dln mu^2 = -a^2 (b0 + b1 a + b2 a^2 + b3 a^3);
    dln m/dln mu^2 = -a (g0 + g1 a + g2 a^2 + g3 a^3).
    Decoupling at mu = m_h(m_h): a^(nf-1) = a^(nf) (1 + 11/72 a^2),
    m^(nf-1) = m^(nf) (1 + 89/432 a^2), used with three- and four-loop
    running.
    Light masses at 2 GeV are four-flavour values. Below m_b the b mass is
    continued with the four-flavour universal factor from m_b(m_b), a
    convention: the b quark is not a dynamical flavour there.
    Leptons: PDG 2024 pole masses [MeV]; quarks: Lecture 11 inputs.

Pure Python (math, itertools); no third-party packages.
"""

import itertools
import math
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
NOTE = os.path.join(ROOT, "papers", "INVERSE-KOIDE-SCALE.md")

# Inputs [MeV]
M_E, M_MU, M_TAU = 0.51099895, 105.6583755, 1776.93
LEPTONS = (M_E, M_MU, M_TAU)
L11 = (4.70, 93.5, 4183.0)            # m_d(2 GeV), m_s(2 GeV), m_b(m_b)
L11_ERR = (0.20, 0.8, 7.0)
ISSUE = (4.67, 93.4, 4180.0)          # PDG inputs used in the issue and Paper 2
F_PI, DF_PI = 92.07, 0.57
M_Z = 91187.6                         # running input
M_Z26, M_W26 = 91187.9, 80362.5      # 2026 PDG line-shape pair (conneskk issue 19)
M_T = 162900.0                        # m_t(m_t)
ALPHA_S_MZ, D_ALPHA_S = 0.1180, 0.0009
ALPHA0 = 1 / 137.035999177
M_P, M_N_ = 938.27208943, 939.56542194
F_PI_OVER_F = 1.064                   # FLAG 2016, N_f = 2+1
ZETA3, ZETA4, ZETA5 = 1.2020569031595942, math.pi ** 4 / 90, 1.0369277551433699

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


def close(x, target, tol):
    return abs(x / target - 1) < tol


def Q(z):
    return sum(math.sqrt(t) for t in z) ** 2 / sum(z)


def C_lep(z):
    return sum(math.sqrt(t) for t in z) ** 2 / 9


def C_inv(z):
    return 9 / sum(t ** -0.5 for t in z) ** 2


def phase(z):
    """Koide phase of the triple z (k = 1, 2, 3 in increasing order)."""
    s = sorted(math.sqrt(t) for t in z)
    c = sum(sk * complex(math.cos(2 * math.pi * k / 3), -math.sin(2 * math.pi * k / 3))
            for k, sk in zip((1, 2, 3), s))
    return math.atan2(c.imag, c.real)


# ============================================================
# QCD running
# ============================================================
def beta(nf):
    b0 = (11 - 2 * nf / 3) / 4
    b1 = (102 - 38 * nf / 3) / 16
    b2 = (2857 / 2 - 5033 * nf / 18 + 325 * nf ** 2 / 54) / 64
    b3 = ((149753 / 6 + 3564 * ZETA3) - (1078361 / 162 + 6508 * ZETA3 / 27) * nf
          + (50065 / 162 + 6472 * ZETA3 / 81) * nf ** 2 + 1093 * nf ** 3 / 729) / 256
    return (b0, b1, b2, b3)


def gamma(nf):
    g0 = 1.0
    g1 = (202 / 3 - 20 * nf / 9) / 16
    g2 = (1249 + (-2216 / 27 - 160 * ZETA3 / 3) * nf - 140 * nf ** 2 / 81) / 64
    g3 = (4603055 / 162 + 135680 * ZETA3 / 27 - 8800 * ZETA5
          + (-91723 / 27 - 34192 * ZETA3 / 9 + 880 * ZETA4 + 18400 * ZETA5 / 9) * nf
          + (5242 / 243 + 800 * ZETA3 / 9 - 160 * ZETA4 / 3) * nf ** 2
          + (-332 / 243 + 64 * ZETA3 / 27) * nf ** 3) / 256
    return (g0, g1, g2, g3)


def run(a, mu0, mu1, nf, loops, steps=4000):
    """RK4 in ln mu^2: returns (a(mu1), m(mu1)/m(mu0))."""
    b, g = beta(nf)[:loops], gamma(nf)[:loops]

    def f(y):
        aa = y[0]
        return (-aa * aa * sum(c * aa ** n for n, c in enumerate(b)),
                -aa * sum(c * aa ** n for n, c in enumerate(g)))

    h = (math.log(mu1 ** 2) - math.log(mu0 ** 2)) / steps
    y = (a, 0.0)
    for _ in range(steps):
        k1 = f(y)
        k2 = f((y[0] + h / 2 * k1[0], y[1] + h / 2 * k1[1]))
        k3 = f((y[0] + h / 2 * k2[0], y[1] + h / 2 * k2[1]))
        k4 = f((y[0] + h * k3[0], y[1] + h * k3[1]))
        y = (y[0] + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
             y[1] + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))
    return y[0], math.exp(y[1])


class Running:
    """Four-flavour light masses at 2 GeV, b mass at m_b(m_b), common scale mu."""

    def __init__(self, masses, alpha_s_mz=ALPHA_S_MZ, loops=4):
        self.md, self.ms, self.mb = masses
        self.loops = loops
        self.dec = loops >= 3
        a_mz = alpha_s_mz / math.pi
        self.a_mb5, _ = run(a_mz, M_Z, self.mb, 5, loops)
        self.a_mb4 = self.a_mb5 * (1 + 11 / 72 * self.a_mb5 ** 2) if self.dec else self.a_mb5
        self.a_2, self.r_mb_2 = run(self.a_mb4, self.mb, 2000.0, 4, loops)  # m(2 GeV)/m(m_b)
        self.a_mz = a_mz

    def alpha_s(self, mu):
        if mu <= self.mb:
            return math.pi * run(self.a_mb4, self.mb, mu, 4, self.loops)[0]
        return math.pi * run(self.a_mb5, self.mb, mu, 5, self.loops)[0]

    def c(self, mu):
        """Universal light-quark factor m(mu)/m(2 GeV)."""
        if mu <= self.mb:
            return run(self.a_2, 2000.0, mu, 4, self.loops)[1]
        dec = 1 / (1 + 89 / 432 * self.a_mb5 ** 2) if self.dec else 1.0
        return dec / self.r_mb_2 * run(self.a_mb5, self.mb, mu, 5, self.loops)[1]

    def masses(self, mu):
        """(m_d, m_s, m_b) at the common scale mu."""
        cl = self.c(mu)
        if mu <= self.mb:
            fb = run(self.a_mb4, self.mb, mu, 4, self.loops)[1]
        else:
            fb = run(self.a_mb5, self.mb, mu, 5, self.loops)[1]
        return (self.md * cl, self.ms * cl, self.mb * fb)


def m_match(quarks):
    return math.sqrt(C_lep(LEPTONS) * C_inv(quarks))


# ============================================================
# 1. Definitions and the image identity
# ============================================================
def check_definitions():
    print("\n=== 1. Definitions, image identity, mixed-scale values ===")
    cl = C_lep(LEPTONS)
    check("C_ell = 313.8509 MeV", round(cl, 4) == 313.8509, f"{cl:.5f}")
    ok = True
    for M in (0.3, 17.0, 91.4, 1.0e4):
        img = [M * M / m for m in L11]
        ok &= close(C_lep(img), M * M / C_inv(L11), 1e-12)
        ok &= abs(1 / Q(img) - sum(1 / m for m in L11) / sum(m ** -0.5 for m in L11) ** 2) < 1e-12
    check("C(M^2/m) = M^2/C_d and Q(M^2/m) = Q(1/m) for every M", ok)
    cd_i, mm_i = C_inv(ISSUE), m_match(ISSUE)
    check("issue inputs: C_d = 26.5991, M_match = 91.368 MeV",
          round(cd_i, 4) == 26.5991 and round(mm_i, 3) == 91.368, f"{cd_i:.5f}, {mm_i:.5f}")
    cd_l, mm_l = C_inv(L11), m_match(L11)
    check("Lecture 11 inputs: C_d = 26.7405, M_match = 91.611 MeV",
          round(cd_l, 4) == 26.7405 and round(mm_l, 3) == 91.611, f"{cd_l:.5f}, {mm_l:.5f}")
    check("issue: 0.76% below f_pi", round(100 * (1 - mm_i / F_PI), 2) == 0.76)


# ============================================================
# 2. Running
# ============================================================
RUN = None


def check_running():
    global RUN
    print("\n=== 2. Four-loop running with decoupling ===")
    RUN = Running(L11)
    a2, amb = RUN.alpha_s(2000.0), RUN.alpha_s(RUN.mb)
    check("alpha_s(2 GeV) = 0.3014, alpha_s(m_b) = 0.2247",
          round(a2, 4) == 0.3014 and round(amb, 4) == 0.2247, f"{a2:.5f}, {amb:.5f}")
    cs = [RUN.c(mu) for mu in (3000.0, RUN.mb, M_Z, M_T)]
    target = (0.9040, 0.8446, 0.5780, 0.5512)
    check("c(mu) = 0.9040, 0.8446, 0.5780, 0.5512 at 3 GeV, m_b, M_Z, m_t",
          all(abs(x - t) < 0.0006 for x, t in zip(cs, target)),
          ", ".join(f"{x:.4f}" for x in cs))
    seq = [Running(L11, loops=n).c(M_T) for n in (1, 2, 3, 4)]
    check("loop-order sequence of c(m_t): 0.632, 0.563, 0.553, 0.551",
          all(round(x, 3) == t for x, t in zip(seq, (0.632, 0.563, 0.553, 0.551))),
          ", ".join(f"{x:.4f}" for x in seq))
    check("three- to four-loop change of c(m_t) below 0.4%", abs(seq[3] / seq[2] - 1) < 0.004)
    p2 = Running(ISSUE).masses(M_T)
    # printed to three figures: allow half a unit of the last digit plus 0.1%
    check("Paper 2 table at m_t: (2.58, 51.5, 2730) MeV within rounding + 0.1%",
          all(abs(x - t) < h + 0.001 * t for x, t, h in zip(p2, (2.58, 51.5, 2730.0), (0.005, 0.05, 5.0))),
          ", ".join(f"{x:.4g}" for x in p2))
    cd_t = C_inv(p2)
    check("Paper 2 at m_t: 68.05 MeV from the rounded table, 67.98 MeV unrounded",
          abs(m_match((2.58, 51.5, 2730.0)) - 68.05) < 0.01 and round(m_match(p2), 2) == 67.98,
          f"{m_match(p2):.3f}")


# ============================================================
# 3. The RG orbit
# ============================================================
SCALES = (("2 GeV", 2000.0), ("3 GeV", 3000.0), ("m_b", None), ("M_Z", M_Z), ("m_t", M_T))
ORBIT = {}


def check_orbit():
    print("\n=== 3. RG orbit: invariants, table, slope, crossing ===")
    qs, ph, ws = [], [], []
    for name, mu in SCALES:
        mu = RUN.mb if mu is None else mu
        q = RUN.masses(mu)
        inv = [1 / m for m in q]
        ORBIT[name] = (q, C_inv(q), m_match(q))
        qs.append(Q(inv))
        ph.append(phase(inv))
        s = sum(m ** -0.5 for m in q)
        ws.append([m ** -0.5 / s for m in q])
    check("Q(1/m) = 1.4983 at every common scale", all(round(x, 4) == 1.4983 for x in qs)
          and max(qs) - min(qs) < 1e-4, f"{qs[0]:.5f}..{qs[-1]:.5f}")
    check("phase of the inverse triple 0.190 rad at every common scale",
          all(round(x, 3) == 0.190 for x in ph), f"{ph[0]:.4f}")
    check("weights w = (0.797, 0.179, 0.025) at every common scale",
          all(all(round(a, 3) == b for a, b in zip(w, (0.797, 0.179, 0.025))) for w in ws),
          ", ".join(f"{x:.4f}" for x in ws[0]))
    cds = [ORBIT[n][1] for n, _ in SCALES]
    mms = [ORBIT[n][2] for n, _ in SCALES]
    check("C_d = 26.86, 24.28, 22.68, 15.52, 14.80 MeV",
          all(round(x, 2) == t for x, t in zip(cds, (26.86, 24.28, 22.68, 15.52, 14.80))),
          ", ".join(f"{x:.3f}" for x in cds))
    check("M_match = 91.81, 87.29, 84.37, 69.80, 68.16 MeV",
          all(abs(x - t) < 0.015 for x, t in zip(mms, (91.81, 87.29, 84.37, 69.80, 68.16))),
          ", ".join(f"{x:.3f}" for x in mms))
    eps = 1e-3
    slope = (math.log(m_match(RUN.masses(2000.0 * math.exp(eps))))
             - math.log(m_match(RUN.masses(2000.0 * math.exp(-eps))))) / (2 * eps)
    check("slope dln M_match/dln mu at 2 GeV = -0.141", round(slope, 3) == -0.141, f"{slope:.4f}")

    def crossing(run_obj, target=F_PI):
        lo, hi = 1000.0, 4000.0
        for _ in range(60):
            mid = math.sqrt(lo * hi)
            if m_match(run_obj.masses(mid)) > target:
                lo = mid
            else:
                hi = mid
        return math.sqrt(lo * hi)

    mu_star = crossing(RUN)
    w = ws[0]
    dlnM = 0.5 * math.sqrt(sum((wi * e / m) ** 2 for wi, e, m in zip(w, L11_ERR, L11)))
    dlnmu = math.sqrt(dlnM ** 2 + (DF_PI / F_PI) ** 2) / abs(slope)
    check("mass errors give dln M_match = 1.7%", round(100 * dlnM, 1) == 1.7, f"{100 * dlnM:.3f}%")
    check("mu_* = 1.96 +- 0.25 GeV", round(mu_star / 1000, 2) == 1.96
          and round(mu_star * dlnmu / 1000, 2) == 0.25,
          f"{mu_star / 1000:.4f} +- {mu_star * dlnmu / 1000:.4f} GeV")
    lo_a = crossing(Running(L11, ALPHA_S_MZ - D_ALPHA_S))
    hi_a = crossing(Running(L11, ALPHA_S_MZ + D_ALPHA_S))
    check("alpha_s(M_Z) = 0.1171 / 0.1189 give mu_* = 1.958 / 1.962 GeV",
          round(lo_a / 1000, 3) == 1.958 and round(hi_a / 1000, 3) == 1.962,
          f"{lo_a / 1000:.4f}, {hi_a / 1000:.4f}")
    ORBIT["mu_star"] = mu_star


# ============================================================
# 4. Literal seesaw
# ============================================================
def spread(lep, qk, kappa):
    """sqrt(T_max/T_min), T_i = m_l H_+(m_l, M = m_q, kappa)."""
    T = []
    for ml, mq in zip(lep, qk):
        H = (kappa * ml + math.sqrt(4 * mq * mq + (kappa * kappa - 4) * ml * ml)) / 2
        T.append(ml * H)
    return math.sqrt(max(T) / min(T))


def check_literal_seesaw():
    print("\n=== 4. Literal seesaw with quark-mass mediators ===")
    best = (LEPTONS, (L11[2], L11[1], L11[0]))          # (e, mu, tau) <-> (b, s, d)
    off = [math.sqrt(ml * (ml + mq)) for ml, mq in zip(*best)]
    check("best pairing needs off-diagonals (46.24, 145.06, 1779.28) MeV",
          all(round(x, 2) == t for x, t in zip(off, (46.24, 145.06, 1779.28))),
          ", ".join(f"{x:.2f}" for x in off))
    kgrid = (2.0, 2.2, 2.5, 3.0, 4.0, 6.0, 10.0, 30.0, 100.0)
    ok_mono = True
    spreads2 = {}
    for perm in itertools.permutations(L11):
        sp = [spread(LEPTONS, perm, k) for k in kgrid]
        ok_mono &= all(b >= a * (1 - 1e-12) for a, b in zip(sp, sp[1:]))
        spreads2[perm] = sp[0]
    best_perm = min(spreads2, key=spreads2.get)
    check("spread nondecreasing in kappa for all six pairings", ok_mono)
    check("minimum spread 38.5 at kappa = 2, pairing (e, mu, tau) <-> (b, s, d)",
          round(spreads2[best_perm], 1) == 38.5 and best_perm == (L11[2], L11[1], L11[0]),
          f"{spreads2[best_perm]:.3f}")
    s2 = min(spread(LEPTONS, p, 2.0) for p in itertools.permutations(RUN.masses(2000.0)))
    st = min(spread(LEPTONS, p, 2.0) for p in itertools.permutations(RUN.masses(M_T)))
    check("common-scale minimum spread 35.4 at 2 GeV and 47.6 at m_t",
          round(s2, 1) == 35.4 and round(st, 1) == 47.6, f"{s2:.3f}, {st:.3f}")
    lights = [(math.sqrt(mq * mq + 4 * F_PI ** 2) - mq) / 2 for mq in L11]
    check("common off-diagonal f_pi gives light values (89.75, 56.51, 2.03) MeV",
          all(round(x, 2) == t for x, t in zip(lights, (89.75, 56.51, 2.03))),
          ", ".join(f"{x:.3f}" for x in lights))


# ============================================================
# 5. Direct image
# ============================================================
def check_image():
    print("\n=== 5. Direct image M^2/m_i ===")
    q = ORBIT["2 GeV"][0]
    r1 = q[0] / q[1]
    check("m_d/m_s = 0.0503 vs m_mu/m_tau = 0.0595, quotient 0.845",
          round(r1, 4) == 0.0503 and round(M_MU / M_TAU, 4) == 0.0595
          and round(r1 / (M_MU / M_TAU), 3) == 0.845, f"{r1 / (M_MU / M_TAU):.4f}")
    r2 = q[1] / q[2]
    check("common-scale m_s/m_b = 0.01888 vs m_e/m_mu = 0.004836, factor 3.90",
          round(r2, 5) == 0.01888 and round(M_E / M_MU, 6) == 0.004836
          and round(r2 / (M_E / M_MU), 2) == 3.90, f"{r2:.5f}, {r2 / (M_E / M_MU):.3f}")
    ph_l = phase(LEPTONS)
    check("lepton phase 0.2222 rad", round(ph_l, 4) == 0.2222, f"{ph_l:.5f}")
    M = ORBIT["2 GeV"][2]
    img = sorted(M * M / m for m in q)
    check("image spectrum at 2 GeV: (1.70, 90.1, 1793) MeV",
          round(img[0], 2) == 1.70 and round(img[1], 1) == 90.1 and round(img[2]) == 1793,
          ", ".join(f"{x:.3f}" for x in img))
    check("image normalization equals C_ell automatically", close(C_lep(img), C_lep(LEPTONS), 1e-12))


# ============================================================
# 6. Reference scales and chiral limit
# ============================================================
def check_reference():
    print("\n=== 6. Reference scales and chiral limit ===")
    mn3 = (M_P + M_N_) / 6
    ew = ALPHA0 * math.sqrt(M_Z26 ** 2 - M_W26 ** 2)
    check("m_N/3 = 312.973 MeV", round(mn3, 3) == 312.973, f"{mn3:.4f}")
    check("alpha(0) sqrt(M_Z^2 - M_W^2) = 314.473 MeV (M_Z = 91.1879, M_W = 80.3625 GeV)",
          abs(ew - 314.473) < 0.01, f"{ew:.4f}")
    c27 = F_PI ** 2 / mn3                       # 3 f_pi^2 / m_N
    check("3 f_pi^2 / m_N = 27.085 MeV", round(c27, 3) == 27.085, f"{c27:.4f}")
    q = ORBIT["2 GeV"][0]
    ratio = C_inv(q) / (9 * q[0])
    check("C_d = 9 m_d w_d^2 with w_d^2 = 0.635 at a common scale",
          round(ratio, 3) == 0.635, f"{ratio:.4f}")
    check("f_pi/F - 1 = 6.4% (FLAG 2016) exceeds the 0.76% agreement",
          F_PI_OVER_F - 1 > 0.06)
    dq = 2 * math.pi * 89.8 / math.sqrt(3)
    check("Delbourgo-Scadron M_q = 2 pi f_pi^chi / sqrt3 = 325.8 MeV, 3.8% above C_ell",
          round(dq, 1) == 325.8 and round(100 * (dq / C_lep(LEPTONS) - 1), 1) == 3.8)


# ============================================================
# 7. Quoted strings
# ============================================================
QUOTED = [
    "313.8509", "26.5991", "91.368", "26.7405", "91.611", "0.3014", "0.2247",
    "0.9040", "0.8446", "0.5780", "0.5512", "0.632", "0.563", "0.553", "0.551",
    "1.4983", "0.190", "0.797", "0.179", "0.025",
    "26.86", "24.28", "22.68", "15.52", "14.80",
    "91.81", "87.29", "84.37", "69.80", "68.16", "-0.141", "1.96", "0.25",
    "1.958", "1.962", "46.24", "145.06", "1779.28", "38.5", "35.4", "47.6",
    "89.75", "56.51", "2.03", "0.0503", "0.0595", "0.845", "0.01888", "0.004836",
    "3.90", "0.2222", "1.70", "90.1", "1793", "312.973", "314.473", "27.085",
    "0.635", "1.064", "325.8", "68.05", "67.98", "2.574",
]


def check_quoted_strings():
    print("\n=== 7. Quoted values present in INVERSE-KOIDE-SCALE.md ===")
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
    print("Inverse-Koide scale test")
    print("=" * 70)
    check_definitions()
    check_running()
    check_orbit()
    check_literal_seesaw()
    check_image()
    check_reference()
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
