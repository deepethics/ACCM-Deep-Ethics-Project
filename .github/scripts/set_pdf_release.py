#!/usr/bin/env python3
"""Update the visible PDF release metadata after a complete export."""

from __future__ import annotations

import argparse
import re
import subprocess
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / "Deep-Ethical-PDFs"


def total_pages(pdfs: list[Path]) -> int:
    pages = 0
    for pdf in pdfs:
        info = subprocess.run(["pdfinfo", str(pdf)], check=True, capture_output=True, text=True).stdout
        pages += int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    return pages


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat(), help="Snapshot date in YYYY-MM-DD format")
    args = parser.parse_args()
    release_date = date.fromisoformat(args.date)
    human_date = f"{release_date:%B} {release_date.day}, {release_date.year}"

    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    count = len(pdfs)
    pages = total_pages(pdfs)
    zip_name = f"ACCM-Deep-Ethics-Project-All-Public-Pages-{count}-PDFs-{release_date.isoformat()}.zip"
    zip_path = PDF_DIR / zip_name
    if not zip_path.is_file():
        raise SystemExit(f"Missing release archive: {zip_name}")
    size = f"{zip_path.stat().st_size / 1024 / 1024:.1f}"

    js_path = ROOT / "assets" / "page-pdf-download.js"
    js = js_path.read_text(encoding="utf-8")
    js = re.sub(r'const snapshotDate = "[^"]+";', f'const snapshotDate = "{human_date}";', js)
    js = re.sub(
        r"ACCM-Deep-Ethics-Project-All-Public-Pages-\d+-PDFs-\d{4}-\d{2}-\d{2}\.zip",
        zip_name,
        js,
    )
    js = re.sub(r'\d+ PDFs · \d+(?:\.\d+)? MB ZIP archive', f'{count} PDFs · {size} MB ZIP archive', js)
    js = re.sub(
        r'Download all \d+ PDF files as an \d+(?:\.\d+)? MB ZIP archive',
        f'Download all {count} PDF files as an {size} MB ZIP archive',
        js,
    )
    js_path.write_text(js, encoding="utf-8")

    meta_path = ROOT / "meta-pdfs.md"
    meta = meta_path.read_text(encoding="utf-8")
    meta = re.sub(
        r"\*\*\d+ public-page PDF editions · [\d,]+ pages · exported through [^*]+\*\*",
        f"**{count} public-page PDF editions · {pages:,} pages · exported through {human_date}**",
        meta,
    )
    meta = re.sub(r"- \*\*PDF files:\*\* \d+", f"- **PDF files:** {count}", meta)
    meta = re.sub(r"- \*\*Total pages:\*\* [\d,]+", f"- **Total pages:** {pages:,}", meta)
    meta = re.sub(r"verified across all \d+ files", f"verified across all {count} files", meta)
    meta = re.sub(r"- \*\*Build result:\*\* \d+ successful PDFs; 0 failures", f"- **Build result:** {count} successful PDFs; 0 failures", meta)
    meta_path.write_text(meta, encoding="utf-8")

    print(f"Release metadata: {count} PDFs, {pages} pages, {size} MB, {human_date}")


if __name__ == "__main__":
    main()
