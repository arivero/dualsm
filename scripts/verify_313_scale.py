#!/usr/bin/env python3
"""Reproduce the spectroscopy, electroweak and flavour tables in papers/313-MEV-SCALE.md.

Inputs are in MeV except for G_F in GeV^-2. Run with python3 -I from any directory.
The cited simulations and global fits enter as published results.
ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA
"""

import argparse
import csv
import sys
from math import atan, exp, hypot, log, pi, sqrt
from pathlib import Path
from statistics import mean

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_inverse_koide_scale as inv

DATA = Path(__file__).resolve().parents[1] / "sources" / "313-mev"
GF = 1.1663785e-5
VEV = 1000 / sqrt(sqrt(2) * GF)
LEPTONS = (0.51099895069, 105.6583755, 1776.93)
A_LEP = mean(LEPTONS) / 2
H_N = (inv.M_P + inv.M_N_) / 6


def show(label, *values):
    print(f"{label:47s} " + "  ".join(f"{v:.12g}" for v in values))


def spectrum():
    masses, errors = {}, {}
    with (DATA / "spectroscopy.tsv").open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            masses[row["family"]] = mean(map(float, row["masses_MeV"].split(",")))
            errors[row["family"]] = mean(map(float, row["errors_MeV"].split(",")))
    return masses, errors


def spectroscopy(m, err, figure=None):
    print("\nSpectroscopy (MeV)")
    gaps, spin_masses, spin_errors = {}, {}, {}
    for label, baryon, ps, vec in [
        ("u/d", "N", "pi", "rho"),
        ("s", "Lambda", "K", "Kstar"),
        ("c", "LambdaC", "D", "Dstar"),
        ("b", "LambdaB", "B", "Bstar"),
    ]:
        spin_mass = (m[ps] + 3 * m[vec]) / 4
        gap = m[baryon] - spin_mass
        spin_masses[label], gaps[label] = spin_mass, gap
        spin_errors[label] = (err[ps] + 3 * err[vec]) / 4
        show(label + ": P, V, spin mean, baryon, gap", m[ps], m[vec], spin_mass, m[baryon], gap)
    for name in ("C", "B"):
        show(
            "spin-one light-pair control " + name,
            (m["Sigma" + name] + 2 * m["Sigma" + name + "Star"]) / 3 - m["Lambda" + name],
        )
    xc, xb = 1000 / spin_masses["c"], 1000 / spin_masses["b"]  # GeV^-1
    dc, db = gaps["c"], gaps["b"]
    ratio = xb / xc
    expected_b = A_LEP + (dc - A_LEP) * ratio
    slope = (dc - db) / (xc - xb)
    intercept = db - slope * xb
    # Triangle bound for correlated input errors, including both appearances of each spin mean.
    x, y = spin_masses["c"], spin_masses["b"]
    sigma_cap = (
        err["LambdaB"]
        + ratio * err["LambdaC"]
        + (1 - ratio) * (0.09 + 2.3e-6 + 1.6e-10) / 6
        + abs((2 * x - m["LambdaC"] + A_LEP) / y) * spin_errors["c"]
        + abs(-1 + x * (dc - A_LEP) / y**2) * spin_errors["b"]
    )
    show("gaps/H_N and difference b-c", dc / H_N, db / H_N, db - dc)
    show("fixed intercept: b, residual, sigma cap", expected_b, db - expected_b, sigma_cap)
    show("free affine intercept, slope [MeV GeV]", intercept, slope)
    coefficient2 = ((dc - A_LEP) / xc - (db - A_LEP) / xb) / (xc - xb)
    coefficient1 = (dc - A_LEP) / xc - coefficient2 * xc
    xm = (xc + xb) / 2
    xturn = -coefficient1 / (2 * coefficient2)

    def curve(u):
        return A_LEP + u * (coefficient1 + u * coefficient2)

    assert abs(curve(xc) - dc) < 1e-10 and abs(curve(xb) - db) < 1e-10
    show("fixed quadratic: c1, c2, M_turn [GeV]", coefficient1, coefficient2, 1 / xturn)
    show("M_mid [GeV], affine, quadratic", 1 / xm, intercept + slope * xm, curve(xm))
    show(
        "quadratic/linear at charm and bottom",
        coefficient2 * xc / coefficient1,
        coefficient2 * xb / coefficient1,
    )
    if figure is not None:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        grid = [i / 1000 for i in range(541)]
        fig, ax = plt.subplots(figsize=(7.4, 4.5), layout="constrained")
        ax.plot(
            grid,
            [intercept + slope * x for x in grid],
            color="#165d79",
            label="Free intercept, linear",
        )
        ax.plot(
            grid,
            [A_LEP + (dc - A_LEP) * x / xc for x in grid],
            "--",
            color="#a4491e",
            label="Lepton intercept, linear from charm",
        )
        ax.plot(
            grid, [curve(x) for x in grid], color="#734987", label="Lepton intercept, quadratic"
        )
        ax.errorbar(
            [xb, xc],
            [db, dc],
            yerr=[err["LambdaB"] + spin_errors["b"], err["LambdaC"] + spin_errors["c"]],
            color="#242424",
            fmt="o",
            zorder=4,
        )
        for label, xpos, ypos in [("bottom", xb, db), ("charm", xc, dc)]:
            ax.annotate(
                label, (xpos, ypos), xytext=(0, -25), textcoords="offset points", ha="right"
            )
        ax.errorbar(0, 319, yerr=1, fmt="s", mfc="white", color="#333333", capsize=3)
        ax.annotate(
            "static lattice (stat. only)",
            (0, 319),
            xytext=(9, 0),
            textcoords="offset points",
            va="center",
        )
        ax.scatter(
            [xm, xm],
            [intercept + slope * xm, curve(xm)],
            facecolors="white",
            edgecolors=["#165d79", "#734987"],
            zorder=3,
        )
        ax.set(
            xlabel="Inverse spin-averaged meson mass (1/GeV)",
            ylabel="Baryon minus spin-averaged meson (MeV)",
            xlim=(-0.018, 0.55),
            ylim=(299.5, 326),
        )
        ax.grid(alpha=0.18)
        ax.legend(loc="upper right", fontsize=8, frameon=False)
        fig.savefig(figure, dpi=175)
        plt.close(fig)
    octet = [m[k] for k in ("N", "Lambda", "Sigma", "Xi")]
    decuplet = [m[k] for k in ("Delta", "SigmaStar", "XiStar", "Omega")]

    def centroid(values, weights):
        return sum(v * w for v, w in zip(values, weights)) / sum(weights)

    so, sd = centroid(octet, (2, 1, 3, 2)), centroid(decuplet, (4, 3, 2, 1))
    go, gd = mean(octet), mean(decuplet)
    one = (3 * (m["Omega"] - m["Delta"]) + m["XiStar"] - m["SigmaStar"]) / 20
    two = (m["Sigma"] - m["Lambda"]) / 8
    assert abs((gd - go) - (sd - so) - one - two) < 1e-10
    show("family O, T, gap", go, gd, gd - go)
    show("charge-state O, T, gap", so, sd, sd - so)
    show("shift from decuplet and octet weights", one, two)
    show(
        "fixed flavour Delta-N, Sigma*-Sigma, Xi*-Xi",
        m["Delta"] - m["N"],
        m["SigmaStar"] - m["Sigma"],
        m["XiStar"] - m["Xi"],
    )

    return {"charm gap": dc, "bottom gap": db, "family gap": gd - go, "state gap": sd - so}


def alphaology():
    print("\nElectroweak and charged-lepton scales (MeV unless marked)")
    e, mu, tau = LEPTONS
    alpha = inv.ALPHA0
    w, z = inv.M_W26, inv.M_Z26
    B = sqrt((z - w) * (z + w))

    def pole(mass, width):
        return mass / hypot(1, width / mass)

    bp = sqrt(pole(z, 2495.5) ** 2 - pole(w, 2140) ** 2)
    K = 1 / inv.Q(LEPTONS)
    gmu_inverse = pi * VEV**2 / (w * w * (1 - (w / z) ** 2))
    show("H_N, A_sum, A_root, alpha B", H_N, A_LEP, inv.C_lep(LEPTONS), alpha * B)
    show("K, A_sum/A_root - 1", K, A_LEP / inv.C_lep(LEPTONS) - 1)
    show("313 difference, fractional, sixfold", A_LEP - H_N, A_LEP / H_N - 1, 6 * (A_LEP - H_N))
    show("B_tab, B_pole, alpha B_pole", B, bp, alpha * bp)
    show("B/H_N, B/A_sum, 1/alpha_0", B / H_N, B / A_LEP, 1 / alpha)
    for target in (H_N, A_LEP):
        show(
            "W required [GeV], observed/target-1",
            sqrt(z * z - (target / alpha) ** 2) / 1000,
            target / (alpha * B) - 1,
        )
    sigma_ew = alpha * hypot(w * 7.7, z * 2.0) / B
    show(
        "EW sigma, difference, illustrative pull",
        sigma_ew,
        alpha * B - A_LEP,
        (alpha * B - A_LEP) / hypot(sigma_ew, 0.09 / 6),
    )
    show(
        "altitude [GeV], inverse Gmu, required Dr",
        w * B / z / 1000,
        gmu_inverse,
        1 - gmu_inverse * alpha,
    )
    show(
        "alpha v, tau offset, double ratio - 1",
        alpha * VEV,
        tau / (alpha * VEV) - 1,
        (H_N / tau) / (B / VEV) - 1,
    )
    show("g' from leptons, g' from W/Z", 2 * A_LEP / tau, 2 * B / VEV)
    pion = 139.57039
    difference = VEV / tau - pion / (2 * e)
    sigma = hypot(
        VEV * 0.09 / tau**2,
        0.00018 / (2 * e),
        VEV * 6e-12 / (2 * GF * tau),
        pion * 1.6e-10 / (2 * e * e),
    )
    show(
        "inverse tau-pion difference, sigma, tau(D=2)",
        difference,
        sigma,
        VEV / (2 + pion / (2 * e)),
    )
    show("Nambu mu, pion; observed mu/e", 1.5 * e / alpha, 2 * e / alpha, mu / e)
    u = (7 + 4 * sqrt(3)) / 64

    def weak_branch(a):
        eps = sqrt(2 * a / 3)
        y = 1 / (2 * (1 + eps) + sqrt(3 * (1 + 4 * eps + eps * eps)))
        return (1 + (1 + eps * eps) * y * y) / 3

    lo, hi = 0.0, 0.02
    for _ in range(60):
        mid = (lo + hi) / 2
        if 4 * pi * mid < (1 - u) * weak_branch(mid) ** 2:
            lo = mid
        else:
            hi = mid
    show("zero-seed u, inverse alpha, forced mu/e", u, 1 / mid, 1.5 / mid)


def flavour(hadronic):
    print("\nReciprocal masses, common-scale matching and finite mixing")
    rho = (5 + sqrt(21)) / 2
    geom = (rho**-2, 1, rho**2)
    assert (
        abs(1 / inv.Q(geom) - 2 / 3) < 1e-12
        and abs(1 / inv.Q([1 / x for x in geom]) - 2 / 3) < 1e-12
    )
    show("rho, squared ratio, lepton phase", rho, rho**2, inv.phase(LEPTONS))
    x = sqrt(2 * inv.ALPHA0 / 3)
    show(
        "phase from Nambu and Thomson charge",
        atan((1 - x) / (sqrt(3) * (1 + x) + 2 * sqrt(1 + 4 * x + x * x))),
    )
    running = inv.Running(inv.L11)
    for tag, q in [("issue mixed", inv.ISSUE), ("lecture mixed", inv.L11)] + [
        (n, running.masses(s))
        for n, s in [
            ("2 GeV", 2000),
            ("3 GeV", 3000),
            ("m_b", inv.L11[2]),
            ("Z", inv.M_Z),
            ("top", inv.M_T),
        ]
    ]:
        cd = inv.C_inv(q)
        show(
            tag + ": C_d, A_d, M_match, K_inv",
            cd,
            6 / sum(1 / t for t in q),
            inv.m_match(q),
            1 / inv.Q([1 / t for t in q]),
        )
    q = running.masses(2000)
    mm = inv.m_match(q)
    show("image masses increasing", *sorted(mm**2 / t for t in q))
    show(
        "literal mixed off-diagonals",
        *[sqrt(l * (l + d)) for l, d in zip(LEPTONS, reversed(inv.ISSUE))],
    )
    show(
        "publication products (earlier, later tables)", sqrt(313.856 * 26.657), sqrt(313.85 * 26.82)
    )

    cd2 = inv.C_inv(q)
    for name, candidate in hadronic.items():
        show(
            name + " matching at 2 GeV; required C_d",
            sqrt(candidate * cd2),
            inv.F_PI**2 / candidate,
        )
    double_ratio = sqrt(hadronic["bottom gap"] / hadronic["charm gap"])
    for scale in (2000.0, 3000.0, inv.M_Z):
        cd = inv.C_inv(running.masses(scale))
        assert (
            abs(sqrt(cd * hadronic["bottom gap"]) / sqrt(cd * hadronic["charm gap"]) - double_ratio)
            < 1e-12
        )
    show("spectroscopic match: bottom/charm, required C_d ratio", double_ratio, 1 / double_ratio**2)

    # Products are invariant even when the bare mediator is not the physical H.
    def masses(d, a, b):
        trace = d * d + a * a + b * b
        high = sqrt((trace + sqrt((trace - 2 * a * b) * (trace + 2 * a * b))) / 2)
        return a * b / high, high

    pairs = [masses(d, 25.0, 40.0) for d in (1.0, 300.0, 1000.0)]
    assert all(abs(l * h - 1000) < 1e-10 for l, h in pairs)
    assert abs(inv.Q([l for l, h in pairs]) - inv.Q([1 / h for l, h in pairs])) < 1e-12
    show("partners if pivot=A_sum (MeV)", *[A_LEP**2 / l for l in LEPTONS])
    for p in (134.9768, 139.57039):
        for d in (1864.84, 1968.35):
            a, b = sqrt(p), sqrt(d)
            disc = 3 * (a * a - 4 * a * b + b * b)
            roots = (
                [] if disc < 0 else [(2 * (b - a) + k * sqrt(disc)) ** 2 / 1000 for k in (-1, 1)]
            )
            show("signed pion/D: p, d, disc, roots [GeV]", p, d, disc, *roots)


def other_scales():
    print("\nOther strong-sector occurrences")
    coupling = 2 * pi / sqrt(3)
    show(
        "sigma model g, F needed, M(86.3), M(89.8)",
        coupling,
        A_LEP / coupling,
        coupling * 86.3,
        coupling * 89.8,
    )
    show("F from f_pi/1.064, corresponding mass", inv.F_PI / 1.064, coupling * inv.F_PI / 1.064)
    exponent = 32 / 81
    ratio = 0.47 ** (1 / exponent)
    a2 = 4 * pi / (9 * log((2000 / 226) ** 2))
    q0 = 226 * exp(2 * pi / (9 * (a2 / ratio)))
    show("pion moment: coupling ratio, alpha0, Q0", ratio, a2 / ratio, q0)
    show("Q0 from printed alpha_s(Q0)=2.14", 226 * exp(2 * pi / (9 * 2.14)))
    show("Lambda from r1 Lambda, r1 [fm]", 0.4943 * 197.3269804 / 0.3106)
    q = 113.6
    p = 134.9768
    show(
        "dipion: parallel, right angle, antiparallel",
        2 * p,
        sqrt(4 * p * p + 2 * q * q),
        2 * hypot(p, q),
    )
    show("quenched Tc and twice physical crossover", 0.7457 * 197.3269804 / 0.472, 2 * 156.5)
    show("portal doubling, relative response slopes", 2 ** (-7 / 18), 2 / 9, 7 / 9)
    show("degenerate radiative loop target", 32 * pi * pi * inv.ALPHA0)
    for zeta in (0.99, 1.01, 1.1):
        m = zeta / 2 + 1 / (4 * zeta**2)
        u = zeta**2 / 4 + 1 / (2 * zeta)
        assert abs(m - 0.75 - (zeta - 1) ** 2 * (2 * zeta + 1) / (4 * zeta**2)) < 1e-14
        assert abs(u - m - (zeta - 1) ** 3 * (zeta + 1) / (4 * zeta**2)) < 1e-14
    show(
        "selector zeta=1.01: m/Lambda, relative condensate", 1.01 / 2 + 1 / (4 * 1.01**2), 1 / 1.01
    )
    for s, p in ((1.0, 0.3), (0.25, 0.4)):
        c = p * p / s
        beta_s, beta_c = 18 * s * s + 2 * p * p, 18 * c * c + 2 * p * p
        beta_p = 6 * p * (s + c) - 8 * p * p
        flow = s * beta_c + c * beta_s - 2 * p * beta_p
        assert abs(flow - 8 * p * p * (s + c + 2 * p)) < 1e-12


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--figure", type=Path, help="also render the heavy-spectator comparison")
    candidates = spectroscopy(*spectrum(), figure=parser.parse_args().figure)
    alphaology()
    flavour(candidates)
    other_scales()
