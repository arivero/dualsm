#!/usr/bin/env python3
"""
Corpus linter for the Dualised Standard Model repository.

Covers every TeX source (lectures 1-11 and preamble, exercise sets 1-9,
papers 1-4), the 23 reference PDFs in sources/ and the related-papers
snapshot. Checks, in order:

  A. inventory      every .tex has a tracked PDF and vice versa
  B. freshness      no PDF older than its source: in git history (the last
                    commit of a .tex, and of lectures/preamble.tex for files
                    that \\input it, is not later than the last commit of the
                    PDF) and, with --staged, in the commit being made
  C. LaTeX hygiene  every \\ref/\\eqref resolves to a \\label and every \\cite
                    to a \\bibitem in the same file (cross-document references
                    print ??); no scratch text ("Wait ---", "let me recompute")
  D. cross-file numerics
                    v = 246 GeV (174 GeV only as v/sqrt 2); Lambda_D ~ 10^11 GeV;
                    alpha_s(M_Z) = 0.118; one-loop Lambda_QCD^(6) recomputed
                    from alpha_s(M_Z); m_u + m_d; Paper 4's generation windows
                    recomputed route by route and compared with its master table;
                    the n_g bounds quoted in Lectures 6-7 and Paper 1
  E. bibliography   every \\bibitem that cites one of the sources/ PDFs (or a few
                    other often-miscited papers) names the right authors and
                    arXiv archive; arXiv:2407.17281 carries its canonical title
  F. sources index  sources/README.md lists every PDF and the right total
                    (warning only)
  G. related-papers index.html is current and the dualsm_paper* copies equal
                    papers/*/paper.{tex,pdf} (scripts/gen_related_index.py)
  H. verify scripts every scripts/verify_*.py exits 0

Errors make the exit status 1; warnings do not.

Usage:
    python3 scripts/lint_corpus.py            # full report
    python3 scripts/lint_corpus.py --quiet    # problems and summary only
    python3 scripts/lint_corpus.py --staged   # also check the staged commit
                                              # (used by .git/hooks/pre-commit)

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA
"""

import glob
import math
import os
import re
import subprocess
import sys
import unicodedata
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

QUIET = "--quiet" in sys.argv
STAGED = "--staged" in sys.argv

errors = []
warnings = []
passes = 0


def rel(path):
    return os.path.relpath(path, ROOT)


def error(msg):
    errors.append(msg)
    print(f"  [ERROR] {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  [WARN]  {msg}")


def ok(msg):
    global passes
    passes += 1
    if not QUIET:
        print(f"  [PASS]  {msg}")


def section(title):
    if not QUIET:
        print(f"\n=== {title} ===")


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True,
                          text=True).stdout


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def strip_comments(text):
    """Remove TeX comments (an unescaped % to the end of the line)."""
    return re.sub(r"(?<!\\)%.*", "", text)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def ascii_fold(text):
    """Lower-case ASCII rendering of TeX text: drops accent commands and braces."""
    text = re.sub(r"\\[`'^\"~=.uvHc]\s*\{?([A-Za-z])\}?", r"\1", text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[{}]", "", text).lower()


LECTURES = sorted(glob.glob(os.path.join(ROOT, "lectures", "lecture-*.tex")))
PREAMBLE = os.path.join(ROOT, "lectures", "preamble.tex")
EXERCISES = sorted(glob.glob(os.path.join(ROOT, "exercises", "exercise-*.tex")))
PAPERS = sorted(glob.glob(os.path.join(ROOT, "papers", "*", "paper.tex")))
DOCS = LECTURES + EXERCISES + PAPERS          # documents that build a PDF
SOURCES = DOCS + [PREAMBLE]

SP = r"(?:\s|~|\\[,;:!])*"                    # TeX spacing between tokens
REL = r"(=|\\approx|\\simeq|\\sim)"


def uses_preamble(text):
    return re.search(r"\\input\{(?:\.\./lectures/)?preamble\}", text) is not None


# ============================================================
# A. Inventory
# ============================================================

def check_inventory():
    section("A. Inventory: sources and PDFs")
    tracked = set(git("ls-files").split("\n"))
    for tex in DOCS:
        pdf = tex[:-4] + ".pdf"
        if rel(pdf) not in tracked:
            error(f"{rel(tex)} has no tracked PDF")
        else:
            ok(f"{rel(tex)} has {os.path.basename(pdf)}")
    for sub in ("lectures", "exercises"):
        for pdf in glob.glob(os.path.join(ROOT, sub, "*.pdf")):
            if not os.path.exists(pdf[:-4] + ".tex"):
                error(f"{rel(pdf)} has no source .tex")
    for pdf in glob.glob(os.path.join(ROOT, "papers", "*", "paper.pdf")):
        if not os.path.exists(pdf[:-4] + ".tex"):
            error(f"{rel(pdf)} has no source .tex")


# ============================================================
# B. Freshness
# ============================================================

def last_commit_time(path):
    out = git("log", "-1", "--format=%ct", "--", rel(path)).strip()
    return int(out) if out else None


def check_freshness():
    section("B. Freshness: no PDF older than its sources")
    staged = set(git("diff", "--cached", "--name-only").split("\n")) - {""}
    modified = set(git("diff", "--name-only").split("\n")) - {""}
    for tex in DOCS:
        pdf = tex[:-4] + ".pdf"
        deps = [tex] + ([PREAMBLE] if uses_preamble(read(tex)) else [])
        t_pdf = last_commit_time(pdf)
        stale = [d for d in deps
                 if t_pdf is not None and (last_commit_time(d) or 0) > t_pdf]
        if stale:
            error(f"{rel(pdf)} was last committed before "
                  f"{', '.join(rel(d) for d in stale)}")
        else:
            ok(f"{rel(pdf)} committed with or after its sources")
        # the commit being made (pre-commit hook)
        if STAGED:
            changed_deps = [d for d in deps if rel(d) in staged]
            if changed_deps and rel(pdf) not in staged:
                error(f"staged {', '.join(rel(d) for d in changed_deps)} "
                      f"without a rebuilt {rel(pdf)}")
            elif changed_deps and os.path.getmtime(pdf) < max(
                    os.path.getmtime(d) for d in changed_deps):
                error(f"{rel(pdf)} is older than {', '.join(rel(d) for d in changed_deps)}")
        # edits not yet staged: only a warning
        if rel(tex) in modified or (rel(PREAMBLE) in modified and PREAMBLE in deps):
            if os.path.getmtime(pdf) < max(os.path.getmtime(d) for d in deps):
                warn(f"{rel(tex)} (or the preamble) has unstaged edits newer than its PDF")


# ============================================================
# C. LaTeX hygiene
# ============================================================

REF = re.compile(r"\\(?:ref|eqref|autoref|pageref|nameref|cref|Cref)\{([^}]*)\}")
LABEL = re.compile(r"\\label\{([^}]*)\}")
CITE = re.compile(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
BIBITEM = re.compile(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}")
SCRATCH = [
    (re.compile(r"\bWait\b\s*(?:---|--|,|!|\.\.\.)"), "scratch text 'Wait ---'"),
    (re.compile(r"\b[Ll]et me (?:re)?(?:compute|calculate|check|think)"),
     "scratch text 'let me recompute'"),
    (re.compile(r"\b(?:TODO|FIXME|XXX)\b"), "TODO/FIXME marker"),
]


def check_hygiene():
    section("C. LaTeX hygiene: references, citations, scratch text")
    for tex in DOCS:
        text = strip_comments(read(tex))
        labels = set(LABEL.findall(text))
        bibkeys = set(k.strip() for k in BIBITEM.findall(text))
        bad = 0
        for m in REF.finditer(text):
            for key in (k.strip() for k in m.group(1).split(",")):
                if key and key not in labels:
                    error(f"{rel(tex)}:{line_of(text, m.start())}: \\ref{{{key}}} has no "
                          f"\\label in this file (prints ??)")
                    bad += 1
        for m in CITE.finditer(text):
            for key in (k.strip() for k in m.group(1).split(",")):
                if key and key not in bibkeys:
                    error(f"{rel(tex)}:{line_of(text, m.start())}: \\cite{{{key}}} has no "
                          f"\\bibitem in this file")
                    bad += 1
        for pattern, what in SCRATCH:
            for m in pattern.finditer(text):
                error(f"{rel(tex)}:{line_of(text, m.start())}: {what}")
                bad += 1
        if not bad:
            ok(f"{rel(tex)}: {len(labels)} labels, {len(bibkeys)} bibitems, all resolved")


# ============================================================
# D. Cross-file numerics
# ============================================================

M_Z = 91.1876          # GeV
ALPHA_S_MZ = 0.118


def lambda_qcd_one_loop_nf6():
    """One-loop Lambda with b_0 = 7 (N_f = 6) run down from M_Z, the scheme
    of Lecture 8 and Exercise Set 6: Lambda = M_Z exp(-2 pi / (b_0 alpha_s))."""
    return 1000 * M_Z * math.exp(-2 * math.pi / (7 * ALPHA_S_MZ))


def generation_windows():
    """Inclusive windows (edges counted) in n_g for each duality route of
    Paper 4, with N_f = 2 n_g, as sets of integers 1..10."""
    ng = range(1, 11)

    def window(nc_of, lower, upper, group_ok):
        out = set()
        for n in ng:
            nf, nc = Fraction(2 * n), nc_of(n)
            if group_ok(nc) and lower(nc) <= nf <= upper(nc):
                out.add(n)
        return out

    su_lower, su_upper = (lambda nc: Fraction(3 * nc, 2)), (lambda nc: 3 * nc)
    return {
        # magnetic SU(3)_c: N_c = N_f - 3
        "SU Seiberg": window(lambda n: 2 * n - 3, su_lower, su_upper,
                             lambda nc: nc >= 2),
        # electric SU(2n_g - 4), magnetic SU(4)_PS
        "SU Pati--Salam": window(lambda n: 2 * n - 4, su_lower, su_upper,
                                 lambda nc: nc >= 2),
        # Sp(N_c) with 2N_f fundamentals, magnetic Sp(N_f - N_c - 2) = Sp(1)
        "Sp": window(lambda n: 2 * n - 3, lambda nc: Fraction(3 * (nc + 1), 2),
                     lambda nc: 3 * (nc + 1), lambda nc: nc >= 1),
        # SO(N_c) with N_f vectors, magnetic SO(N_f - N_c + 4) = SO(6)
        "SO": window(lambda n: 2 * n - 2, lambda nc: Fraction(3 * (nc - 2), 2),
                     lambda nc: 3 * (nc - 2), lambda nc: nc >= 3),
        # Kutasov-Schwimmer, magnetic SU(k N_f - N_c) = SU(3)_c, edges from
        # b_0^el = 2N_c - N_f and b_0^mag = (2k - 1) N_f - 2 N_c
        "KS ($k=2$)": window(lambda n: 4 * n - 3, lambda nc: Fraction(2 * nc, 3),
                             lambda nc: 2 * nc, lambda nc: nc >= 2),
        "KS ($k \\geq 3$)": window(lambda n: 6 * n - 3, lambda nc: Fraction(2 * nc, 5),
                                   lambda nc: 2 * nc, lambda nc: nc >= 2),
    }


def parse_int_set(cell):
    """'$\\ngen \\in \\{3,\\ldots,6\\}$' -> {3,4,5,6}; '$\\ngen \\in \\{3,4\\}$' -> {3,4}."""
    m = re.search(r"\\\{([^}]*)\\\}", cell)
    if not m:
        return None
    body = m.group(1).replace(" ", "")
    r = re.fullmatch(r"(\d+),\\ldots,(\d+)", body)
    if r:
        return set(range(int(r.group(1)), int(r.group(2)) + 1))
    return {int(x) for x in body.split(",") if x}


def check_numerics():
    section("D. Cross-file numerics")
    texts = {tex: strip_comments(read(tex)) for tex in DOCS}

    # v = 246 GeV; 174 GeV only as v/sqrt(2)
    v_pat = re.compile(r"(?<![A-Za-z\\_^{])v" + SP + REL + SP + r"([\d.]+)")
    n_v = 0
    for tex, text in texts.items():
        for m in v_pat.finditer(text):
            val = float(m.group(2).rstrip("."))
            if 150 <= val <= 260 and val not in (246.0, 250.0):
                error(f"{rel(tex)}:{line_of(text, m.start())}: v {m.group(1)} {m.group(2)}; "
                      f"the course uses v = 246 GeV and writes 174 GeV as v/\\sqrt{{2}}")
            n_v += 1
    ok(f"v: {n_v} numeric statements, none uses 174 GeV for v")

    # Lambda_D ~ 10^11 GeV
    ld_pat = re.compile(r"\\Lambda_\{?(?:D|\\mathrm\{D\}|\\text\{D\})\}?" + SP + REL + SP +
                        r"(?:([\d.]+)" + SP + r"\\times" + SP + r")?10\^\{?(\d+)\}?")
    n_ld = 0
    for tex, text in texts.items():
        for m in ld_pat.finditer(text):
            n_ld += 1
            if m.group(3) != "11" or (m.group(2) not in (None, "1")):
                error(f"{rel(tex)}:{line_of(text, m.start())}: Lambda_D quoted as "
                      f"{m.group(2) + ' x ' if m.group(2) else ''}10^{m.group(3)}; "
                      f"the corpus uses 10^11 GeV")
    ok(f"Lambda_D: {n_ld} statements, all 10^11 GeV")

    # alpha_s(M_Z)
    as_pat = re.compile(r"\\alpha(?:s|_s|_\{s\})" + SP + r"\(" + SP + r"M_Z" + SP + r"\)"
                        + SP + REL + SP + r"(0\.\d+)")
    n_as = 0
    for tex, text in texts.items():
        for m in as_pat.finditer(text):
            n_as += 1
            if not 0.1175 <= float(m.group(2)) <= 0.1185:
                error(f"{rel(tex)}:{line_of(text, m.start())}: alpha_s(M_Z) = {m.group(2)}; "
                      f"the corpus uses 0.118")
    ok(f"alpha_s(M_Z): {n_as} statements, all 0.118")

    # one-loop Lambda_QCD with six flavours, run from alpha_s(M_Z)
    expected = lambda_qcd_one_loop_nf6()
    lq_pat = re.compile(r"\\Lambda_\{?\\?(?:QCD|\\text\{QCD\}|\\mathrm\{QCD\})\}?\^\{\(6\)\}"
                        + SP + REL + SP + r"(\d+)")
    n_lq = 0
    for tex, text in texts.items():
        for m in lq_pat.finditer(text):
            n_lq += 1
            if int(m.group(2)) != round(expected):
                error(f"{rel(tex)}:{line_of(text, m.start())}: one-loop Lambda_QCD^(6) = "
                      f"{m.group(2)} MeV; alpha_s(M_Z) = 0.118 with b_0 = 7 gives "
                      f"{expected:.1f} MeV")
    ok(f"Lambda_QCD^(6) one loop: {n_lq} statements, all {round(expected)} MeV "
       f"(recomputed {expected:.1f} MeV)")

    # m_u + m_d (MS-bar, 2 GeV; PDG 2022-2024 central values 6.83-6.86 MeV)
    mud_pat = re.compile(r"m_u" + SP + r"\+" + SP + r"m_d" + SP + r"(?:&)?" + SP + REL
                         + SP + r"([\d.]+)")
    n_mud = 0
    for tex, text in texts.items():
        for m in mud_pat.finditer(text):
            n_mud += 1
            if not 6.8 <= float(m.group(2).rstrip(".")) <= 6.95:
                error(f"{rel(tex)}:{line_of(text, m.start())}: m_u + m_d = {m.group(2)} MeV; "
                      f"the corpus uses the PDG value 6.8-6.9 MeV")
    ok(f"m_u + m_d: {n_mud} statements, all 6.8-6.9 MeV")

    check_generation_numbers(texts)


def check_generation_numbers(texts):
    windows = generation_windows()
    p4 = next(t for t in PAPERS if "generation-number" in t)
    text = texts[p4]
    m = re.search(r"\\label\{tab:master\}", text)
    table_start = text.rfind("\\begin{table", 0, m.start()) if m else -1
    if table_start < 0:
        error(f"{rel(p4)}: master table (tab:master) not found")
        return
    body = text[table_start:m.start()]
    rows = {}
    for row in body.split("\\\\"):
        cells = [c.strip() for c in row.split("&")]
        if len(cells) >= 6:
            name = re.sub(r"^.*\\midrule\s*", "", cells[0], flags=re.S).strip()
            # "$\mathrm{Sp}$ (IP)" -> "Sp", "$\mathrm{SO}$ (IS)" -> "SO"
            name = re.sub(r"^\$\\mathrm\{(\w+)\}\$\s*\(\w+\)$", r"\1", name)
            rows[name] = parse_int_set(cells[-1])
    for route, expected in windows.items():
        quoted = rows.get(route)
        if quoted is None:
            error(f"{rel(p4)}: master table has no row '{route}'")
        elif quoted != expected:
            error(f"{rel(p4)}: master table row '{route}' gives {sorted(quoted)}, "
                  f"the window algebra gives {sorted(expected)}")
        else:
            ok(f"Paper 4 master table '{route}': n_g in {sorted(expected)}")
    ks1 = rows.get("KS ($k=1$)")
    if ks1 is not None and ks1 != windows["SU Seiberg"]:
        error(f"{rel(p4)}: KS (k=1) row differs from SU Seiberg")
    su_sp = (windows["SU Seiberg"] | windows["SU Pati--Salam"]) & windows["Sp"]
    if su_sp != {3}:
        error(f"SU-Sp overlap is {sorted(su_sp)}, the papers claim {{3}}")
    else:
        ok("SU and Sp frames overlap only at n_g = 3 (edges included)")

    # Pati-Salam window edges quoted in Lectures 6-7: n_g >= 3 and n_g <= 6
    ps = windows["SU Pati--Salam"]
    for tex in LECTURES:
        name = os.path.basename(tex)
        if name not in ("lecture-06.tex", "lecture-07.tex"):
            continue
        t = texts[tex]
        lower = re.search(r"n_g" + SP + r"\\geq" + SP + r"(\d+)", t)
        upper = re.search(r"n_g" + SP + r"\\leq" + SP + r"(\d+)", t)
        if not lower or int(lower.group(1)) != min(ps):
            error(f"{rel(tex)}: lower generation bound should read n_g \\geq {min(ps)}")
        if not upper or int(upper.group(1)) != max(ps):
            error(f"{rel(tex)}: upper generation bound should read n_g \\leq {max(ps)} "
                  f"(magnetic SU(4) asymptotic freedom)")
        if lower and upper and int(lower.group(1)) == min(ps) and int(upper.group(1)) == max(ps):
            ok(f"{name}: {min(ps)} <= n_g <= {max(ps)} matches the Pati-Salam window")

    # Paper 1: Sp range and the shared headline; SM coefficient bound n_g <= 5
    p1 = next(t for t in PAPERS if "sp-duality" in t)
    headline = "sit inside or on the SUSY conformal window"
    for paper in (p1, p4):
        flat = " ".join(texts[paper].split())
        if headline not in flat:
            error(f"{rel(paper)}: headline '{headline}' missing")
        else:
            ok(f"{rel(paper)}: carries the shared n_g headline")
    sp = windows["Sp"]
    sp_pat = re.compile(r"(\d)" + SP + r"\\leq" + SP + r"(?:n_g|\\ngen)" + SP + r"\\leq" + SP + r"(\d)")
    sp_quotes = [(int(a), int(b)) for a, b in sp_pat.findall(texts[p1])]
    if (min(sp), max(sp)) not in sp_quotes:
        error(f"{rel(p1)}: Sp range {min(sp)} <= n_g <= {max(sp)} not stated")
    else:
        ok(f"{rel(p1)}: Sp range {min(sp)} <= n_g <= {max(sp)} matches Paper 4")
    # non-SUSY one-loop SU(2)_L coefficient with one Higgs doublet:
    # b_0 = 22/3 - 4 n_g/3 - 1/6 > 0
    sm_max = max(n for n in range(1, 20)
                 if Fraction(22, 3) - Fraction(4 * n, 3) - Fraction(1, 6) > 0)
    for paper in (p1, p4):
        if not re.search(r"(?:n_g|\\ngen)" + SP + r"\\leq" + SP + str(sm_max) + r"\b",
                         texts[paper]):
            error(f"{rel(paper)}: SM-coefficient bound n_g <= {sm_max} not stated")
        else:
            ok(f"{rel(paper)}: SM one-loop SU(2)_L bound n_g <= {sm_max}")


# ============================================================
# E. Bibliography against sources/
# ============================================================

# arXiv id -> (archive or None for new-style ids, required author surnames,
#              required title fragment or None, source PDF or None)
CANONICAL = {
    "1105.1510": (None, ["antipin", "mojaza", "pica", "sannino"], None,
                  "antipin-mojaza-pica-sannino-1105.1510.pdf"),
    "9603042": ("hep-th", ["argyres", "plesser", "seiberg"], None,
                "argyres-plesser-seiberg-9603042.pdf"),
    "0802.0634": (None, ["bilal"], None, "bilal-0802.0634.pdf"),
    "2208.07842": (None, ["karasik", "onder", "tong"], None, "bi-terning-2208.07842.pdf"),
    "9904406": ("hep-ph", ["chan", "tsou"], None, "chan-tsou-9904406.pdf"),
    "9801146": ("hep-th", ["cheng", "shadmi"], None, "cheng-shadmi-9801146.pdf"),
    "1106.3074": (None, ["csaki", "shirman", "terning"], None, "csaki-terning-1106.3074.pdf"),
    "9509066": ("hep-th", ["intriligator", "seiberg"], None, "intriligator-seiberg-9509066.pdf"),
    "9510426": ("hep-ph", ["maekawa", "takahashi"], None, "maekawa-9510426.pdf"),
    "9509407": ("hep-ph", ["maekawa"], None, "maekawa-ptp95-943.pdf"),
    "9511395": ("hep-ph", ["maekawa", "sato"], None, "maekawa-ptp96-979.pdf"),
    "9511399": ("hep-ph", ["bartels", "lotter", "vogt"], None, "peskin-9511399.pdf"),
    "9702094": ("hep-th", ["peskin"], None, "peskin-9702094.pdf"),
    "0711.3745": (None, ["ryttov", "sannino"], "supersymmetry inspired qcd beta function",
                  "ryttov-sannino-0711.3745.pdf"),
    "0907.1364": (None, ["sannino"], None, "sannino-0907.1364.pdf"),
    "1102.5100": (None, ["sannino"], None, "sannino-1102.5100.pdf"),
    "2407.17281": (None, ["cacciapaglia", "sannino"],
                   "charting standard model duality and its signatures",
                   "sannino-2407.17281.pdf"),
    "9708113": ("hep-th", ["sannino", "schechter"], None, "sannino-schechter-9708113.pdf"),
    "9411149": ("hep-th", ["seiberg"], None, "seiberg-9411149.pdf"),
    "9407087": ("hep-th", ["seiberg", "witten"], None, "seiberg-witten-9407087.pdf"),
    "9408099": ("hep-th", ["seiberg", "witten"], None, "seiberg-witten-9408099.pdf"),
    "0306119": ("hep-th", ["terning"], None, "terning-0306119.pdf"),
    "0110256": ("hep-th", ["tsou"], None, "tsou-0110256.pdf"),
    # often-miscited papers outside sources/
    "9505004": ("hep-th", ["kutasov", "schwimmer"], None, None),
    "9510222": ("hep-th", ["kutasov", "schwimmer", "seiberg"], None, None),
    "9505006": ("hep-th", ["intriligator", "pouliot"], None, None),
    "9610139": ("hep-th", ["csaki", "schmaltz", "skiba"], None, None),
    "9612207": ("hep-th", ["csaki", "schmaltz", "skiba"], None, None),
}

ARXIV_ID = re.compile(r"(?:\b(hep-th|hep-ph|hep-lat|hep-ex|gr-qc|cond-mat|math-ph)/)?"
                      r"(?<![\d.])(\d{4}\.\d{4,5}|\d{7})(?![\d.])")


def bib_blocks(text):
    starts = [m.start() for m in re.finditer(r"\\bibitem", text)]
    end = text.find("\\end{thebibliography}")
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else (end if end > s else len(text))
        yield s, text[s:e]


def check_bibliography():
    section("E. Bibliography against sources/")
    pdfs = {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "sources", "*.pdf"))}
    for arxiv, (_, _, _, pdf) in CANONICAL.items():
        if pdf and pdf not in pdfs:
            error(f"sources/{pdf} (arXiv {arxiv}) is missing")
    unmapped = pdfs - {c[3] for c in CANONICAL.values() if c[3]}
    for pdf in sorted(unmapped):
        warn(f"sources/{pdf} has no entry in lint_corpus.CANONICAL")
    n_items = 0
    for tex in DOCS:
        text = strip_comments(read(tex))
        for start, block in bib_blocks(text):
            folded = " ".join(ascii_fold(block).split())
            # scan the entry, not its key (keys such as CSS9612207 are labels)
            body = BIBITEM.sub("", block, count=1)
            for m in ARXIV_ID.finditer(body):
                archive, number = m.group(1), m.group(2)
                if number not in CANONICAL:
                    continue
                n_items += 1
                want_archive, authors, title, _ = CANONICAL[number]
                where = f"{rel(tex)}:{line_of(text, start)}"
                if want_archive and archive and archive != want_archive:
                    error(f"{where}: {archive}/{number} should be {want_archive}/{number}")
                missing = [a for a in authors if a not in folded]
                if missing:
                    error(f"{where}: arXiv {number} is by {', '.join(authors)}; "
                          f"bibitem lacks {', '.join(missing)}")
                if title and title not in folded:
                    error(f"{where}: arXiv {number} should carry the title "
                          f"'{title}'")
                if number == "9612207" and "lett" in folded:
                    error(f"{where}: PRL 78 (1997) 799 is hep-th/9610139; "
                          f"hep-th/9612207 is the PRD paper")
    ok(f"{n_items} bibitems cite a source or a checked paper; "
       f"authors, archives and titles agree")


# ============================================================
# F. sources/README.md (warning only)
# ============================================================

def check_sources_readme():
    section("F. sources/README.md index (warnings only)")
    readme = os.path.join(ROOT, "sources", "README.md")
    pdfs = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "sources", "*.pdf")))
    text = read(readme) if os.path.exists(readme) else ""
    missing = [p for p in pdfs if p not in text]
    if missing:
        warn(f"sources/README.md does not list {len(missing)} of {len(pdfs)} PDFs: "
             f"{', '.join(missing)}")
    m = re.search(r"Total papers:\**\s*(\d+)", text)
    if not m or int(m.group(1)) != len(pdfs):
        warn(f"sources/README.md total ({m.group(1) if m else 'none'}) differs from "
             f"the {len(pdfs)} PDFs present")
    if not missing and m and int(m.group(1)) == len(pdfs):
        ok(f"sources/README.md lists all {len(pdfs)} PDFs")


# ============================================================
# G. related-papers
# ============================================================

def check_related():
    section("G. related-papers snapshot and generated index")
    import gen_related_index as gri
    rows = gri.read_rows()
    for p in gri.problems_with(rows):
        error(f"related-papers: {p}")
    with open(gri.INDEX, encoding="utf-8") as fh:
        if fh.read() != gri.render(rows):
            error("related-papers/index.html is stale; run scripts/gen_related_index.py")
        else:
            ok(f"related-papers/index.html current ({len(rows)} entries)")


# ============================================================
# H. verify scripts
# ============================================================

def check_verify_scripts():
    section("H. scripts/verify_*.py")
    for script in sorted(glob.glob(os.path.join(ROOT, "scripts", "verify_*.py"))):
        run = subprocess.run([sys.executable, script], capture_output=True, text=True,
                             cwd=ROOT)
        if run.returncode != 0:
            tail = "\n".join(run.stdout.strip().split("\n")[-5:])
            error(f"{rel(script)} exited {run.returncode}:\n{tail}")
        else:
            ok(f"{rel(script)} passes")


def main():
    print("Corpus linter: " + ", ".join([
        f"{len(LECTURES)} lectures", f"{len(EXERCISES)} exercise sets",
        f"{len(PAPERS)} papers", "preamble",
        f"{len(glob.glob(os.path.join(ROOT, 'sources', '*.pdf')))} source PDFs"]))
    for check in (check_inventory, check_freshness, check_hygiene, check_numerics,
                  check_bibliography, check_sources_readme, check_related,
                  check_verify_scripts):
        check()
    print(f"\nlint_corpus: {passes} passed, {len(errors)} errors, "
          f"{len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
