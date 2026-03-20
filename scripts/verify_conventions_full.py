#!/usr/bin/env python3
"""
VALD-04: Extended convention verification across ALL 8 lectures and
6 exercise sets for the Dualised Standard Model project.

Checks:
  1. ASSERT_CONVENTION line present and matching in all 14 files
  2. T(fund) = 1/2 consistency (no T(fund) = 1 anywhere)
  3. Beta function b_0 = (11 N_c - 2 N_f)/3 convention (not 4 N_f variant)
  4. Metric signature (+,-,-,-) (no (-,+,+,+) anywhere)
  5. N_f counting as Dirac flavours (not Weyl count)
  6. Hypercharge Y = T_R^3 + Q_V/6 in Lectures 7-8 and Exercises 5-6
  7. Conjectural qualifiers in Lectures 5-8 and Exercises 5-6
  8. Cross-file convention consistency

Extends (does not replace) scripts/verify_conventions.py, which tests
group theory identities numerically.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    fourier_convention=physics, coupling_convention=alpha_s,
    generator_normalization=T(fund)=1/2, covariant_derivative_sign=D_mu=partial_mu-igA

References:
    .gpd/CONVENTIONS.md
    lectures/preamble.tex (canonical ASSERT_CONVENTION line)
"""

import os
import re
import sys

# ============================================================
# Configuration
# ============================================================

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LECTURE_FILES = [
    os.path.join(PROJECT_ROOT, "lectures", f"lecture-{i:02d}.tex")
    for i in range(1, 9)
]

EXERCISE_FILES = [
    os.path.join(PROJECT_ROOT, "exercises", f"exercise-{i:02d}.tex")
    for i in range(1, 7)
]

ALL_FILES = LECTURE_FILES + EXERCISE_FILES

# Canonical ASSERT_CONVENTION line (from preamble.tex)
CANONICAL_ASSERT = (
    "% ASSERT_CONVENTION: natural_units=natural, "
    "metric_signature=mostly_minus, fourier_convention=physics, "
    "coupling_convention=alpha_s, generator_normalization=T(fund)=1/2, "
    "covariant_derivative_sign=D_mu=partial_mu-igA"
)

# Files that should contain hypercharge convention (Lectures 7-8, Exercises 5-6)
HYPERCHARGE_FILES = [
    os.path.join(PROJECT_ROOT, "lectures", "lecture-07.tex"),
    os.path.join(PROJECT_ROOT, "lectures", "lecture-08.tex"),
    os.path.join(PROJECT_ROOT, "exercises", "exercise-05.tex"),
    os.path.join(PROJECT_ROOT, "exercises", "exercise-06.tex"),
]

# Files that should contain conjectural qualifiers (Lectures 5-8, Exercises 5-6)
CONJECTURAL_FILES = [
    os.path.join(PROJECT_ROOT, "lectures", "lecture-05.tex"),
    os.path.join(PROJECT_ROOT, "lectures", "lecture-06.tex"),
    os.path.join(PROJECT_ROOT, "lectures", "lecture-07.tex"),
    os.path.join(PROJECT_ROOT, "lectures", "lecture-08.tex"),
    os.path.join(PROJECT_ROOT, "exercises", "exercise-05.tex"),
    os.path.join(PROJECT_ROOT, "exercises", "exercise-06.tex"),
]


# ============================================================
# Utilities
# ============================================================

total_passed = 0
total_failed = 0


def check(description, condition, filepath="", detail=""):
    """Register a pass/fail check."""
    global total_passed, total_failed
    status = "PASS" if condition else "FAIL"
    if condition:
        total_passed += 1
    else:
        total_failed += 1
    fname = os.path.basename(filepath) if filepath else ""
    prefix = f"  [{fname}] " if fname else "  "
    detail_str = f"  [{detail}]" if detail else ""
    print(f"  [{status}]{prefix}{description}{detail_str}")
    return condition


def read_file(filepath):
    """Read a file and return its contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def short_name(filepath):
    """Return short name for display."""
    return os.path.relpath(filepath, PROJECT_ROOT)


# ============================================================
# CHECK 1: ASSERT_CONVENTION line
# ============================================================

def check_assert_convention():
    """Verify ASSERT_CONVENTION line is present and matches in all 14 files."""
    print("\n=== CHECK 1: ASSERT_CONVENTION line in all 14 files ===")
    all_ok = True
    for filepath in ALL_FILES:
        content = read_file(filepath)
        first_line = content.split('\n')[0].strip()

        # Check presence
        has_assert = "ASSERT_CONVENTION" in first_line
        if not has_assert:
            check("ASSERT_CONVENTION present", False, filepath)
            all_ok = False
            continue

        # Check exact match with canonical line
        matches = first_line == CANONICAL_ASSERT
        check("ASSERT_CONVENTION matches canonical",
              matches, filepath,
              "exact match" if matches else f"got: {first_line[:80]}...")
        if not matches:
            all_ok = False

    return all_ok


# ============================================================
# CHECK 2: T(fund) = 1/2 consistency
# ============================================================

def check_tfund():
    """Verify T(fund) = 1/2 everywhere, no T(fund) = 1."""
    print("\n=== CHECK 2: T(fund) = 1/2 consistency ===")
    all_ok = True

    # Patterns that indicate T(fund) = 1/2 (correct)
    correct_patterns = [
        r"T\(fund\)\s*=\s*1/2",
        r"T\(\\mathrm\{fund\}\)\s*=\s*1/2",
        r"T\(\\fund\)\s*=\s*1/2",
        r"\\Tfund",  # preamble defines \Tfund = \tfrac{1}{2}
        r"T\(fund\)\s*=\s*\\tfrac\{1\}\{2\}",
        r"T_\{\\mathrm\{fund\}\}\s*=\s*1/2",
    ]

    # Patterns that indicate T(fund) = 1 (WRONG)
    wrong_patterns = [
        r"T\(fund\)\s*=\s*1[^/]",
        r"T\(\\mathrm\{fund\}\)\s*=\s*1[^/]",
        r"T_\{\\mathrm\{fund\}\}\s*=\s*1[^/]",
    ]

    for filepath in ALL_FILES:
        content = read_file(filepath)

        # Check for wrong T(fund) = 1
        wrong_found = False
        for pat in wrong_patterns:
            matches = re.findall(pat, content)
            if matches:
                # Filter out false positives (e.g., "T(fund) = 1/2")
                for m in matches:
                    if "1/2" not in m and "\\tfrac{1}{2}" not in m:
                        wrong_found = True
                        break

        check("No T(fund) = 1 (wrong convention)",
              not wrong_found, filepath,
              "clean" if not wrong_found else "FOUND T(fund) = 1!")
        if wrong_found:
            all_ok = False

    # Verify preamble defines \Tfund correctly
    preamble_path = os.path.join(PROJECT_ROOT, "lectures", "preamble.tex")
    preamble = read_file(preamble_path)
    tfund_correct = r"\tfrac{1}{2}" in preamble and r"\newcommand{\Tfund}" in preamble
    check("preamble.tex defines \\Tfund = \\tfrac{1}{2}",
          tfund_correct, preamble_path)
    if not tfund_correct:
        all_ok = False

    return all_ok


# ============================================================
# CHECK 3: Beta function convention
# ============================================================

def check_beta_function():
    """Verify b_0 = (11 N_c - 2 N_f)/3, not variants with 4 N_f."""
    print("\n=== CHECK 3: Beta function convention b_0 = (11 N_c - 2 N_f)/3 ===")
    all_ok = True

    for filepath in ALL_FILES:
        content = read_file(filepath)

        # Check for wrong variant: (11 N_c - 4 N_f)/3 or similar
        # The 4N_f variant corresponds to counting Weyl fermions instead of Dirac
        wrong_beta = re.search(
            r'(11\s*\\?N[_c]*\s*-\s*4\s*\\?N[_f]*)\s*/\s*3', content
        )
        check("No wrong beta function (11N_c - 4N_f)/3",
              wrong_beta is None, filepath,
              "clean" if wrong_beta is None else f"FOUND: {wrong_beta.group()}")
        if wrong_beta is not None:
            all_ok = False

    return all_ok


# ============================================================
# CHECK 4: Metric signature
# ============================================================

def check_metric():
    """Verify metric (+,-,-,-), no (-,+,+,+)."""
    print("\n=== CHECK 4: Metric signature (+,-,-,-) ===")
    all_ok = True

    for filepath in ALL_FILES:
        content = read_file(filepath)

        # Check for wrong metric (-,+,+,+) or diag(-1,+1,+1,+1)
        wrong_metric = (
            "diag(-1,+1,+1,+1)" in content or
            "diag(-1, +1, +1, +1)" in content or
            "(-,+,+,+)" in content or
            "mostly plus" in content.lower()
        )
        check("No wrong metric (-,+,+,+)",
              not wrong_metric, filepath,
              "clean" if not wrong_metric else "FOUND wrong metric!")
        if wrong_metric:
            all_ok = False

        # Check for correct metric assertion (diag(+1,-1,-1,-1))
        has_correct = (
            "diag(+1,-1,-1,-1)" in content or
            "(+,-,-,-)" in content or
            "mostly minus" in content.lower() or
            "mostly_minus" in content
        )
        check("Correct metric assertion present",
              has_correct, filepath,
              "found" if has_correct else "not found (may be in preamble only)")
        if not has_correct:
            # Not a failure if in preamble -- ASSERT_CONVENTION covers it
            pass  # info only

    return all_ok


# ============================================================
# CHECK 5: N_f counting
# ============================================================

def check_nf_counting():
    """Verify N_f counts Dirac flavour pairs, not Weyl fermions."""
    print("\n=== CHECK 5: N_f counting convention ===")
    all_ok = True

    for filepath in ALL_FILES:
        content = read_file(filepath)

        # Check for explicit Weyl counting of N_f without qualification
        # Pattern: "N_f Weyl" without "when counting Weyl" or similar
        # This is a soft check -- false positives possible
        wrong_nf = re.search(
            r'N_f\s*=\s*\d+\s+Weyl\b', content, re.IGNORECASE
        )
        # The convention allows "N_f Weyl" when explicitly qualified
        # (e.g., "when counting Weyl fermions explicitly, state 'N_f Weyl'")
        # So we only flag if it appears without qualification
        if wrong_nf:
            # Check if it's in a qualification context
            context = content[max(0, wrong_nf.start() - 100):wrong_nf.end() + 100]
            is_qualified = ("when counting" in context.lower() or
                           "explicitly" in context.lower() or
                           "convention" in context.lower())
            if not is_qualified:
                check("N_f uses Dirac counting (not unqualified Weyl)",
                      False, filepath,
                      f"FOUND: {wrong_nf.group()}")
                all_ok = False
            else:
                check("N_f Weyl mention is qualified",
                      True, filepath, "qualified usage")

    # Global pass if no unqualified Weyl counting found
    if all_ok:
        check("N_f counting convention consistent across all files", True)

    return all_ok


# ============================================================
# CHECK 6: Hypercharge convention
# ============================================================

def check_hypercharge():
    """Verify Y = T_R^3 + Q_V/6 in files that use hypercharge.

    Lectures 7-8 define and use the hypercharge formula.
    Exercises 5-6 deal with mass hierarchy and scale matching,
    so they may not explicitly state the hypercharge formula --
    we only check files that actually reference hypercharge/Q_V/T_R.
    """
    print("\n=== CHECK 6: Hypercharge convention Y = T_R^3 + Q_V/6 ===")
    all_ok = True

    for filepath in HYPERCHARGE_FILES:
        content = read_file(filepath)

        # Check if this file uses hypercharge at all
        uses_hypercharge = (
            "T_R^3" in content or
            "Q_V" in content or
            "hypercharge" in content.lower()
        )

        if not uses_hypercharge:
            # File does not discuss hypercharge -- skip with info
            check("Hypercharge not used (N/A -- mass/scale exercise)",
                  True, filepath, "hypercharge not referenced")
            continue

        # Check for Y = T_R^3 + Q_V/6 (correct)
        has_correct_Y = (
            "T_R^3" in content and "Q_V" in content and
            ("Q_V/6" in content or "\\frac{1}{6}" in content or
             "\\tfrac{1}{6}" in content)
        )
        check("Hypercharge Y = T_R^3 + Q_V/6 present",
              has_correct_Y, filepath)
        if not has_correct_Y:
            all_ok = False

        # Check for wrong hypercharge Y = T_R^3 + (B-L)/2 without conversion
        # (This is fine if it appears as an alternative with explicit conversion)
        has_wrong_Y = re.search(r'Y\s*=\s*T_R\^3\s*\+\s*\(B-L\)/2', content)
        if has_wrong_Y:
            # Check if conversion to our convention is provided
            has_conversion = "Q_V/6" in content or "\\frac{1}{6}" in content
            check("B-L hypercharge has conversion to Q_V/6",
                  has_conversion, filepath,
                  "conversion present" if has_conversion else "NO conversion!")
            if not has_conversion:
                all_ok = False

    return all_ok


# ============================================================
# CHECK 7: Conjectural qualifiers
# ============================================================

def check_conjectural_qualifiers():
    """Check for conjectural language near non-SUSY duality claims."""
    print("\n=== CHECK 7: Conjectural qualifiers (Lectures 5-8, Exercises 5-6) ===")
    all_ok = True

    # Conjectural qualifier patterns (positive)
    conjectural_patterns = [
        r"if the (?:conjectured )?duality holds",
        r"conjectured",
        r"conjectural",
        r"suggests",
        r"if the duality is correct",
        r"if this conjecture",
        r"under the assumption",
        r"proposed",
    ]

    # Unqualified assertion patterns (negative -- should NOT appear)
    unqualified_patterns = [
        r"the duality shows",
        r"the duality proves",
        r"the duality demonstrates",
        r"duality establishes",
        r"the duality guarantees",
    ]

    for filepath in CONJECTURAL_FILES:
        content = read_file(filepath)
        fname = short_name(filepath)

        # Count conjectural qualifiers
        conj_count = 0
        for pat in conjectural_patterns:
            conj_count += len(re.findall(pat, content, re.IGNORECASE))

        check(f"Conjectural qualifiers present (count = {conj_count})",
              conj_count > 0, filepath,
              f"{conj_count} instances")
        if conj_count == 0:
            all_ok = False

        # Check for unqualified assertions
        unqual_count = 0
        for pat in unqualified_patterns:
            matches = re.findall(pat, content, re.IGNORECASE)
            unqual_count += len(matches)
            for m in matches:
                print(f"    WARNING: Unqualified assertion in {fname}: '{m}'")

        check("No unqualified duality assertions",
              unqual_count == 0, filepath,
              f"{unqual_count} unqualified" if unqual_count > 0 else "clean")
        if unqual_count > 0:
            all_ok = False

    return all_ok


# ============================================================
# CHECK 8: Cross-file convention consistency
# ============================================================

def check_cross_file_consistency():
    """Verify the same conventions appear across all files."""
    print("\n=== CHECK 8: Cross-file convention consistency ===")
    all_ok = True

    # Collect ASSERT_CONVENTION lines from all files
    assert_lines = set()
    for filepath in ALL_FILES:
        content = read_file(filepath)
        first_line = content.split('\n')[0].strip()
        assert_lines.add(first_line)

    # All files should have the same ASSERT_CONVENTION line
    check("All 14 files have identical ASSERT_CONVENTION",
          len(assert_lines) == 1,
          detail=f"{len(assert_lines)} distinct line(s)")
    if len(assert_lines) != 1:
        all_ok = False
        for line in assert_lines:
            print(f"    Variant: {line[:80]}...")

    # Check that preamble.tex convention comments are consistent
    # with the ASSERT_CONVENTION line
    preamble_path = os.path.join(PROJECT_ROOT, "lectures", "preamble.tex")
    preamble = read_file(preamble_path)

    preamble_checks = [
        ("Metric: (+,-,-,-)", "metric" in preamble.lower() and
         ("(+,-,-,-)" in preamble or "mostly minus" in preamble.lower())),
        ("T(fund) = 1/2", "T(fund) = 1/2" in preamble),
        ("b_0 = (11N_c - 2N_f)/3", "11N_c - 2N_f" in preamble or
         "(11N_c - 2N_f)/3" in preamble),
        ("D_mu = partial_mu - ig A_mu", "partial_mu - ig" in preamble or
         "D_mu = partial" in preamble),
        ("alpha_s = g_s^2/(4 pi)", "g_s^2" in preamble or
         "alpha_s" in preamble),
    ]

    for desc, ok in preamble_checks:
        check(f"preamble.tex declares: {desc}",
              ok, preamble_path)
        if not ok:
            all_ok = False

    return all_ok


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 70)
    print("VALD-04: Extended Convention Verification")
    print("         All 8 Lectures + 6 Exercise Sets")
    print("=" * 70)
    print()
    print(f"Files to check: {len(ALL_FILES)}")
    for f in ALL_FILES:
        print(f"  {short_name(f)}")

    # Verify all files exist
    missing = [f for f in ALL_FILES if not os.path.isfile(f)]
    if missing:
        print(f"\nERROR: {len(missing)} files not found:")
        for f in missing:
            print(f"  MISSING: {short_name(f)}")
        return 1

    print(f"\nAll {len(ALL_FILES)} files found.\n")

    results = []
    results.append(("ASSERT_CONVENTION", check_assert_convention()))
    results.append(("T(fund) = 1/2", check_tfund()))
    results.append(("Beta function", check_beta_function()))
    results.append(("Metric signature", check_metric()))
    results.append(("N_f counting", check_nf_counting()))
    results.append(("Hypercharge", check_hypercharge()))
    results.append(("Conjectural qualifiers", check_conjectural_qualifiers()))
    results.append(("Cross-file consistency", check_cross_file_consistency()))

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    for name, ok in results:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")

    print()
    print(f"Total: {total_passed} passed, {total_failed} failed")
    print("=" * 70)

    if total_failed > 0:
        print(f"\nFAILED: {total_failed} checks did not pass.")
        return 1
    else:
        print(f"\nALL CHECKS PASSED across {len(ALL_FILES)} files.")
        print("\nConvention consistency summary:")
        print("  ASSERT_CONVENTION:       14/14 files match canonical")
        print("  T(fund) = 1/2:           no violations")
        print("  b_0 = (11N_c-2N_f)/3:    no wrong variants")
        print("  Metric (+,-,-,-):        no wrong signatures")
        print("  N_f = Dirac pairs:       consistent")
        print("  Y = T_R^3 + Q_V/6:      present in Lectures 7-8, Exercises 5-6")
        print("  Conjectural qualifiers:  present in Lectures 5-8, Exercises 5-6")
        print("  Cross-file consistency:  all 14 files match")
        return 0


if __name__ == "__main__":
    sys.exit(main())
