#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

site = Path(__file__).resolve().parents[2]
source = site / "Deep-Ethical-PDFs"
out = source / "ACCM-Deep-Ethics-Project-All-Public-Pages-124-PDFs-2026-10-16.zip"

pdfs = sorted(source.glob("*.pdf"), key=lambda p: p.name.casefold())
if len(pdfs) != 124:
    raise SystemExit(f"Expected 124 PDFs, found {len(pdfs)}")

extras = [source / name for name in ("PDF-INDEX.md", "PDF-INDEX.csv", "BUILD-REPORT.txt", "SHA256SUMS.txt")]
for path in extras:
    if not path.is_file():
        raise SystemExit(f"Missing archive record: {path.name}")

with ZipFile(out, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
    for path in [*pdfs, *extras]:
        info = ZipInfo(path.name, date_time=(2026, 10, 16, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)

print(f"Created {out.name}: {len(pdfs)} PDFs, {out.stat().st_size} bytes")
