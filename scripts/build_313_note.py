#!/usr/bin/env python3
"""Render the printable edition with Pandoc and XeLaTeX. The Markdown is canonical."""

import datetime
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "papers/313-MEV-SCALE.md"
REPO = "https://github.com/arivero/dualsm/blob/master/"
# Wrapping text in longtable columns matters in the printable edition.
WIDTHS = {
    "Quantity": (0.34, 0.48, 0.18),
    "Spectator": (0.12, 0.14, 0.14, 0.21, 0.18, 0.21),
    "Prescription": (0.42, 0.19, 0.21, 0.18),
    "Common": (0.32, 0.21, 0.21, 0.26),
    "Mass assigned": (0.48, 0.26, 0.26),
    "Condition": (0.43, 0.18, 0.39),
    "Sector": (0.21, 0.47, 0.32),
    "End of": (0.30, 0.20, 0.25, 0.25),
    "Claim": (0.28, 0.72),
}


def print_links(node):
    if isinstance(node, list):
        for child in node:
            print_links(child)
    elif isinstance(node, dict):
        if node.get("t") == "Link":
            link = node["c"][-1]
            parsed = urlsplit(link[0])
            if parsed.path and not parsed.scheme:
                path = (PAPER.parent / parsed.path).resolve().relative_to(ROOT)
                link[0] = (
                    REPO + path.as_posix() + ("#" + parsed.fragment if parsed.fragment else "")
                )
        elif node.get("t") == "Table":
            cols, head = node["c"][2], node["c"][3]
            first_cell = head[1][0][1][0][-1][0]["c"]
            label = " ".join(i["c"] for i in first_cell if i["t"] == "Str")
            widths = next(weights for key, weights in WIDTHS.items() if label.startswith(key))
            if len(widths) != len(cols):
                raise ValueError(f"Column count changed in {label}")
            for col, width in zip(cols, widths):
                col[1] = {"t": "ColWidth", "c": width}
        for child in node.values():
            print_links(child)


def main():
    title, date, body = PAPER.read_text().split("\n\n", 2)
    meta = ["-M", "title=" + title.removeprefix("# "), "-M", "date=" + date.strip("*")]
    doc = json.loads(
        subprocess.check_output(
            ["pandoc", "-f", "gfm+tex_math_dollars", "-t", "json", "--shift-heading-level-by=-1"],
            input=body.encode(),
        )
    )
    print_links(doc["blocks"])
    first_section = next(i for i, block in enumerate(doc["blocks"]) if block["t"] == "Header")
    doc["meta"]["abstract"] = {"t": "MetaBlocks", "c": doc["blocks"][:first_section]}
    doc["blocks"] = [
        {"t": "RawBlock", "c": ["latex", r"\clearpage"]},
        *doc["blocks"][first_section:],
    ]
    with tempfile.TemporaryDirectory() as scratch:
        path = Path(scratch)
        (path / "figures").mkdir()
        figure = Path("figures/313-spectroscopy.png")
        shutil.copyfile(PAPER.parent / figure, path / figure)
        args = [
            "pandoc",
            "-f",
            "json",
            "-t",
            "latex",
            "-s",
            "--toc",
            "--toc-depth=1",
            *meta,
            "-V",
            "papersize=a4",
            "-V",
            "geometry:margin=21mm",
            "-V",
            "fontsize=10pt",
            "-V",
            "colorlinks=true",
            "-V",
            "urlcolor=teal",
            "-V",
            "linkcolor=teal",
            "-V",
            "mainfont=TeX Gyre Pagella",
            "-V",
            "mathfont=TeX Gyre Pagella Math",
            "-o",
            str(path / "note.tex"),
        ]
        subprocess.run(args, input=json.dumps(doc).encode(), check=True)
        stamp = datetime.datetime(2026, 11, 27, tzinfo=datetime.UTC)
        env = {
            **os.environ,
            "SOURCE_DATE_EPOCH": str(int(stamp.timestamp())),
            "FORCE_SOURCE_DATE": "1",
        }
        previous_refs = None
        for _ in range(5):
            result = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "note.tex"],
                cwd=path,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            if result.returncode:
                raise RuntimeError(result.stdout.decode(errors="replace")[-2600:])
            refs = [(path / name).read_bytes() for name in ("note.aux", "note.toc")]
            if refs == previous_refs:
                break
            previous_refs = refs
        else:
            raise RuntimeError("PDF references did not stabilize")
        log = (path / "note.log").read_text(errors="replace").splitlines()
        for i, line in enumerate(log):
            if "Overfull" in line or "Missing character" in line:
                print(line, log[i + 1] if i + 1 < len(log) else "")
        shutil.copyfile(path / "note.pdf", PAPER.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
