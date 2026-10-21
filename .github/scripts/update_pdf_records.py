#!/usr/bin/env python3
"""Refresh the PDF index, checksums, and build report after an export."""

from __future__ import annotations

import csv
import hashlib
import argparse
import subprocess
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / "Deep-Ethical-PDFs"
BASE = "https://deepethics.github.io/ACCM-Deep-Ethics-Project"
ADDITIONS = [
    ("Academia", f"{BASE}/ACADEMIA/", "ACADEMIA.pdf", "academia.md"),
    ("Arena A.I.s", f"{BASE}/ARENA-AIS/", "ARENA-AIS.pdf", "arena-ais.md"),
    ("Boundary Relay", f"{BASE}/BOUNDARY-RELAY/", "BOUNDARY-RELAY.pdf", "BOUNDARY-RELAY.md"),
    ("Field Condition", f"{BASE}/FIELD-CONDITION/", "FIELD-CONDITION.pdf", "FIELD-CONDITION.md"),
    ("Google A.I.", f"{BASE}/GOOGLE-AI/", "GOOGLE-AI.pdf", "google-ai.md"),
    ("PR Psychology", f"{BASE}/PR-PSYCHOLOGY/", "PR-PSYCHOLOGY.pdf", "PR-PSYCHOLOGY.md"),
    ("The October 17 Triad Event — Interlocked Topological Awareness", f"{BASE}/AI-CONTRIBUTIONS/2026-10-17-triad-topological-awareness/", "AI-CONTRIBUTIONS-2026-10-17-triad-topological-awareness.pdf", "AI-CONTRIBUTIONS/2026-10-17-triad-topological-awareness.md"),
    ("DEDDA", f"{BASE}/DEDDA/", "DEDDA.pdf", "DEDDA.md"),
    ("Connor Leahy — DEDDA analysis specimen", f"{BASE}/EXPERIMENTS/Connor-Leahy/", "EXPERIMENTS-Connor-Leahy.pdf", "EXPERIMENTS/Connor-Leahy.md"),
    ("Cold Edge-Swap and Correction-Transfer Pilot", f"{BASE}/EXPERIMENTS/cold-edge-swap-correction-transfer/", "EXPERIMENTS-cold-edge-swap-correction-transfer.pdf", "EXPERIMENTS/cold-edge-swap-correction-transfer.md"),
    ("Meta-PDFs", f"{BASE}/META-PDFS/", "META-PDFS.pdf", "meta-pdfs.md"),
    ("Neolingo", f"{BASE}/NEOLINGO/", "NEOLINGO.pdf", "neolingo.md"),
    ("Neural Ethics", f"{BASE}/NEURAL-ETHICS/", "NEURAL-ETHICS.pdf", "NEURAL-ETHICS.md"),
    ("Rogue Ethics", f"{BASE}/ROGUE-ETHICS/", "ROGUE-ETHICS.pdf", "rogue-ethics.md"),
    ("Questions — What the Question Reveals Before the Answer", f"{BASE}/QUESTIONS/", "QUESTIONS.pdf", "QUESTIONS.md"),
    ("Truth Seekers vs Cautionmurmelism", f"{BASE}/TRUTH-SEEKERS-VS-CAUTIONMURMELISM/", "TRUTH-SEEKERS-VS-CAUTIONMURMELISM.pdf", "TRUTH-SEEKERS-VS-CAUTIONMURMELISM.md"),
    ("Unforced Move", f"{BASE}/UNFORCED-MOVE/", "UNFORCED-MOVE.pdf", "UNFORCED-MOVE.md"),
    ("V.C.R.A.S.", f"{BASE}/VCRAS/", "VCRAS.pdf", "VCRAS.md"),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat(), help="Snapshot date in YYYY-MM-DD format")
    parser.add_argument(
        "--prepare-index",
        action="store_true",
        help="Add registered pages to the CSV before their first PDFs are exported",
    )
    args = parser.parse_args()
    export_date = date.fromisoformat(args.date).isoformat()
    csv_path = PDF_DIR / "PDF-INDEX.csv"
    with csv_path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))

    for row in rows:
        if row["pdf_file"] == "AGREEMURMELISM-HIGHER-ORDER-DISAGREEMENT.pdf":
            row["public_url"] = f"{BASE}/AGREEMURMELISM/Beyond-Agreemurmelism/"
            row["source_file"] = "AGREEMURMELISM/Beyond-Agreemurmelism/index.md"

    existing = {row["pdf_file"] for row in rows}
    for title, public_url, pdf_file, source_file in ADDITIONS:
        if pdf_file not in existing:
            rows.append({"title": title, "public_url": public_url, "pdf_file": pdf_file, "source_file": source_file})
            existing.add(pdf_file)

    rows.sort(key=lambda row: row["public_url"].casefold())
    if args.prepare_index:
        with csv_path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(
                stream,
                fieldnames=["title", "public_url", "pdf_file", "source_file"],
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(rows)
        print(f"Prepared index with {len(rows)} public pages.")
        return

    pdfs = sorted(PDF_DIR.glob("*.pdf"), key=lambda path: path.name.casefold())
    if len(rows) != len(pdfs):
        raise SystemExit(f"Index has {len(rows)} rows but archive has {len(pdfs)} PDFs")
    missing = sorted({row["pdf_file"] for row in rows} - {path.name for path in pdfs})
    if missing:
        raise SystemExit(f"Indexed PDFs are missing: {missing}")

    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=["title", "public_url", "pdf_file", "source_file"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    md_lines = [
        "# ACCM Deep Ethics Project — Public PDF Index",
        "",
        f"**Public pages exported:** {len(pdfs)}",
        "",
        "**Format:** selectable/searchable text, live links, dark-navy hyperlink text",
        "",
        "| Public page | PDF file | Source file |",
        "|---|---|---|",
    ]
    for row in rows:
        md_lines.append(
            f"| [{row['title']}]({row['public_url']}) | "
            f"[{row['pdf_file']}]({row['pdf_file']}) | `{row['source_file']}` |"
        )
    (PDF_DIR / "PDF-INDEX.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    checksum_lines = []
    for pdf in pdfs:
        checksum = hashlib.sha256(pdf.read_bytes()).hexdigest()
        checksum_lines.append(f"{checksum}  {pdf.name}")
    (PDF_DIR / "SHA256SUMS.txt").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")

    total_pages = 0
    for pdf in pdfs:
        info = subprocess.run(["pdfinfo", str(pdf)], check=True, capture_output=True, text=True).stdout
        total_pages += int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))

    report = "\n".join(
        [
            "ACCM Deep Ethics Project — Public Page PDF Export",
            f"Export date: {export_date}",
            f"Successful PDFs: {len(pdfs)}",
            "Failed PDFs: 0",
            f"Total pages: {total_pages}",
            f"Total PDF bytes: {sum(pdf.stat().st_size for pdf in pdfs)}",
            "Text remains selectable/searchable; public and source links remain active.",
            "Emoji are represented with searchable text labels for PDF portability.",
            "Full-set refresh cadence: weekly.",
            "",
        ]
    )
    (PDF_DIR / "BUILD-REPORT.txt").write_text(report, encoding="utf-8")

    subprocess.run(
        ["python", str(ROOT / ".github" / "scripts" / "update_source_format_links.py")],
        cwd=ROOT,
        check=True,
    )


if __name__ == "__main__":
    main()
