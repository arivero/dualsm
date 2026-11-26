#!/usr/bin/env python3
"""
Numerical observation on the two charged-meson cross-ratios
(papers/CROSS-RATIO-OBSERVATION.md).

With the six charged pseudoscalar masses M(ud), M(us), M(ub), M(cd), M(cs),
M(cb) = pi+, K+, B+, D+, D_s+, B_c+,

    R_ds = M(ud) M(cs) / (M(us) M(cd)),   R_db = M(ud) M(cb) / (M(ub) M(cd)).

  1. rho = log R_ds / log R_db and its propagated uncertainty.
  2. The equivalent mass relation R_db = R_ds^2, written as a value of the
     B_c mass computed from the other five masses.
  3. The same relation as M(us)^2 / M(ud) = M(cs)^2 M(ub) / (M(cd) M(cb)).
  4. Leading-order value Delta_ds / Delta_db of the proposition in
     FIVE-FLAVOUR-MATCHING.md, from quark masses, with and without running
     m_b and m_c to 2 GeV, and the coefficient C implied by each ratio.
  5. The exact value for the classical meson metric 1/(h_i + h_j), where
     R_jk = (m_u + m_j)(m_c + m_k) / ((m_u + m_k)(m_c + m_j)).
  6. The vector-meson analogue for a range of the unmeasured B_c* mass.
  7. The numbers quoted in the note.

Inputs. Pseudoscalar masses, D*+, D_s*+ and B*: Particle Data Group, 2025
update of the Review of Particle Physics (S. Navas et al., Phys. Rev. D 110,
030001 (2024) and 2025 update), fit values of the summary tables, read from
the PDG database file pdgall-2025-v0.2.2.sqlite. Quark masses: the same
review as listed in the 2026 edition tables (u, d, s at 2 GeV in the MS-bar
scheme, m_c(m_c), m_b(m_b)). The rho+ and K*+ masses are rounded values
(775 and 892 MeV); part 6 varies them by 5 MeV.

Python 3 standard library.
"""
import math
import sys

passed = failed = 0


def check(name, ok, detail=""):
    global passed, failed
    if ok:
        passed += 1
    else:
        failed += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  [{detail}]" if detail else ""))


# masses in MeV: (value, uncertainty)
PS = {
    "ud": (139.57039, 0.00018),   # pi+
    "us": (493.6766, 0.0154),     # K+
    "cd": (1869.661, 0.048),      # D+
    "cs": (1968.351, 0.069),      # D_s+
    "ub": (5279.406, 0.071),      # B+
    "cb": (6274.47, 0.32),        # B_c+
}
# quark masses in MeV
QUARK = {"u": 2.16, "d": 4.70, "s": 92.9, "c": 1272.9, "b": 4186.0}


def logs(m):
    f_ds = math.log(m["ud"] * m["cs"] / (m["us"] * m["cd"]))
    f_db = math.log(m["ud"] * m["cb"] / (m["ub"] * m["cd"]))
    return f_ds, f_db


def central(table):
    return {k: v[0] for k, v in table.items()}


def propagated(fun, table):
    """Linear propagation of independent uncertainties by finite differences."""
    base = central(table)
    var = 0.0
    for k, (v, s) in table.items():
        up = dict(base)
        up[k] = v + s
        var += (fun(up) - fun(base)) ** 2
    return fun(base), math.sqrt(var)


print("=== 1. The ratio of the two logarithms ===")
f_ds, f_db = logs(central(PS))
rho, s_rho = propagated(lambda m: logs(m)[0] / logs(m)[1], PS)
print(f"  log R_ds = {f_ds:.5f}, log R_db = {f_db:.5f}, rho = {rho:.5f} +- {s_rho:.5f}")
check("rho = 0.5003 to four decimals", abs(rho - 0.5003) < 5e-5, f"{rho:.6f}")
check("rho differs from 1/2 by several standard deviations of the measurement",
      abs(rho - 0.5) / s_rho > 5, f"{(rho - 0.5) / s_rho:.1f} sigma")

print("=== 2. The B_c mass from the other five masses ===")


def bc_from_five(m):
    return m["ub"] * m["ud"] * m["cs"] ** 2 / (m["us"] ** 2 * m["cd"])


five = {k: v for k, v in PS.items() if k != "cb"}
bc, s_bc = propagated(bc_from_five, five)
diff = PS["cb"][0] - bc
sig = diff / math.hypot(s_bc, PS["cb"][1])
print(f"  M(B_c) from R_db = R_ds^2: {bc:.2f} +- {s_bc:.2f} MeV; measured {PS['cb'][0]} +- {PS['cb'][1]}")
print(f"  difference {diff:.2f} MeV = {1e3 * diff / PS['cb'][0]:.2f} per mille = {sig:.1f} sigma")
check("computed B_c mass within 0.2 per cent of the measured one", abs(diff) / PS["cb"][0] < 2e-3)
check("exact equality is excluded by the measurement errors", abs(sig) > 5, f"{sig:.1f} sigma")

print("=== 3. Light and heavy sides of the relation ===")
m = central(PS)
light = m["us"] ** 2 / m["ud"]
heavy = m["cs"] ** 2 * m["ub"] / (m["cd"] * m["cb"])
print(f"  M(K)^2/M(pi) = {light:.2f} MeV; M(D_s)^2 M(B)/(M(D) M(B_c)) = {heavy:.2f} MeV; ratio {light / heavy:.5f}")
check("the two sides agree to 0.2 per cent", abs(light / heavy - 1) < 2e-3)

print("=== 4. Leading order of the proposition ===")
RUN_B, RUN_C = 1.18, 0.86   # rough factors m_b(2 GeV)/m_b(m_b), m_c(2 GeV)/m_c(m_c)
lead = []
for label, fb, fc in (("m_b(m_b), m_c(m_c)", 1.0, 1.0), ("m_b, m_c at 2 GeV (rough)", RUN_B, RUN_C)):
    q = dict(QUARK, b=QUARK["b"] * fb, c=QUARK["c"] * fc)
    d_ds = math.log(q["d"] / q["s"])
    d_db = math.log(q["d"] / q["b"])
    d_uc = math.log(q["u"] / q["c"])
    lead.append(d_ds / d_db)
    c_ds, c_db = f_ds / (d_uc * d_ds), f_db / (d_uc * d_db)
    print(f"  {label}: Delta_ds/Delta_db = {d_ds / d_db:.4f}; Delta_uc = {d_uc:.2f}; C from ds {c_ds:.4f}, from db {c_db:.4f}")
    check(f"implied C between -0.07 and -0.05 ({label})", -0.07 < c_ds < -0.05 and -0.07 < c_db < -0.05)
check("leading-order ratio between 0.42 and 0.45", all(0.42 < x < 0.45 for x in lead))
check("leading order misses the measured ratio by more than 10 per cent", all(rho / x - 1 > 0.10 for x in lead))

print("=== 5. Classical meson metric, exact in the masses ===")
q = QUARK
r_ds = (q["u"] + q["d"]) * (q["c"] + q["s"]) / ((q["u"] + q["s"]) * (q["c"] + q["d"]))
r_db = (q["u"] + q["d"]) * (q["c"] + q["b"]) / ((q["u"] + q["b"]) * (q["c"] + q["d"]))
rho_cl = math.log(r_ds) / math.log(r_db)
print(f"  log R_ds = {math.log(r_ds):.3f}, log R_db = {math.log(r_db):.3f}, ratio = {rho_cl:.4f}")
print(f"  measured over classical: {f_ds / math.log(r_ds):.3f} (ds), {f_db / math.log(r_db):.3f} (db)")
check("classical-metric ratio between 0.50 and 0.53", 0.50 < rho_cl < 0.53, f"{rho_cl:.4f}")
check("its logarithms are about twice the measured ones",
      0.45 < f_ds / math.log(r_ds) < 0.50 and 0.45 < f_db / math.log(r_db) < 0.50)

print("=== 6. Vector analogue ===")
V = {"cd": 2010.264, "cs": 2112.194, "ub": 5324.745}
lo, hi = 1.0, 0.0
for rho_m in (770.0, 775.0, 780.0):
    for kst in (887.0, 892.0, 897.0):
        for extra in (0.0, 50.0, 100.0, 200.0, 300.0):
            v = dict(V, ud=rho_m, us=kst, cb=PS["cb"][0] + extra)
            a, b = logs(v)
            lo, hi = min(lo, a / b), max(hi, a / b)
print(f"  ratio for M(B_c*) between M(B_c) and M(B_c) + 300 MeV: {lo:.3f} to {hi:.3f}")
v = dict(V, ud=775.0, us=892.0)
need = math.exp(2 * math.log(v["ud"] * v["cs"] / (v["us"] * v["cd"]))) * v["ub"] * v["cd"] / v["ud"]
print(f"  M(B_c*) needed for the ratio 1/2: {need / 1000:.1f} GeV")
check("vector ratio stays below 0.2", hi < 0.2, f"{lo:.3f}..{hi:.3f}")
check("the ratio 1/2 would need a B_c* above 10 GeV", need > 10000)

print("=== 7. Quoted values present in the note ===")
try:
    import pathlib
    text = (pathlib.Path(__file__).resolve().parent.parent / "papers" / "CROSS-RATIO-OBSERVATION.md").read_text()
    quoted = ["0.5003", f"{bc:.1f}", "6274.47", f"{light:.1f}", f"{heavy:.1f}", f"{rho_cl:.2f}", f"{need / 1000:.1f}"]
    missing = [x for x in quoted if x not in text]
    check(f"{len(quoted) - len(missing)}/{len(quoted)} quoted values found", not missing, f"missing {missing}")
except FileNotFoundError:
    check("note file present", False)

print("=" * 70)
print(f"RESULTS: {passed} passed, {failed} failed")
print("=" * 70)
sys.exit(1 if failed else 0)
