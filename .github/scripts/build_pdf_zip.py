#!/usr/bin/env python3
import argparse
from datetime import date
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

parser = argparse.ArgumentParser()
parser.add_argument("--date", default=date.today().isoformat(), help="Snapshot date in YYYY-MM-DD format")
args = parser.parse_args()
release_date = date.fromisoformat(args.date)

site = Path(__file__).resolve().parents[2]
source = site / "Deep-Ethical-PDFs"

pdfs = sorted(source.glob("*.pdf"), key=lambda p: p.name.casefold())
expected = sum(1 for line in (source / "PDF-INDEX.csv").read_text(encoding="utf-8").splitlines()[1:] if line.strip())
if len(pdfs) != expected:
    raise SystemExit(f"Expected {expected} PDFs, found {len(pdfs)}")
out = source / "ACCM-Deep-Ethics-Project-All-Public-Pages.zip"
for previous in source.glob("ACCM-Deep-Ethics-Project-All-Public-Pages-*-PDFs-*.zip"):
    previous.unlink()

extras = [source / name for name in ("PDF-INDEX.md", "PDF-INDEX.csv", "BUILD-REPORT.txt", "SHA256SUMS.txt")]
for path in extras:
    if not path.is_file():
        raise SystemExit(f"Missing archive record: {path.name}")

with ZipFile(out, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
    for path in [*pdfs, *extras]:
        info = ZipInfo(path.name, date_time=(release_date.year, release_date.month, release_date.day, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)

print(f"Created {out.name}: {len(pdfs)} PDFs, {out.stat().st_size} bytes")
