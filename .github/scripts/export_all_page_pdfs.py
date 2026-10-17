#!/usr/bin/env python3
"""Regenerate every indexed public-page PDF from its current Markdown source."""

from __future__ import annotations

import csv
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from export_page_pdf import export_pdf


ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / "Deep-Ethical-PDFs"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=4, help="Number of concurrent PDF exports")
    args = parser.parse_args()
    with (PDF_DIR / "PDF-INDEX.csv").open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))

    failures: list[str] = []
    def export_row(row: dict[str, str]) -> str:
        source = ROOT / row["source_file"]
        output = PDF_DIR / row["pdf_file"]
        if not source.is_file():
            raise FileNotFoundError(f"{row['source_file']}: source file not found")
        export_pdf(source, output)
        return f"{row['source_file']} -> {row['pdf_file']}"

    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {executor.submit(export_row, row): row for row in rows}
        for number, future in enumerate(as_completed(futures), start=1):
            row = futures[future]
            try:
                result = future.result()
                print(f"[{number:03}/{len(rows):03}] {result}", flush=True)
            except Exception as error:  # Report every failed source in one run.
                failures.append(f"{row['source_file']}: {error}")

    if failures:
        raise SystemExit("PDF export failures:\n" + "\n".join(failures))
    print(f"Regenerated {len(rows)} public-page PDFs.")


if __name__ == "__main__":
    main()
