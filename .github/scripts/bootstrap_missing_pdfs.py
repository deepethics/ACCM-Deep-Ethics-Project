import csv, json, subprocess, sys
from pathlib import Path
from datetime import date
root = Path(__file__).resolve().parents[2]
pdfdir = root / "Deep-Ethical-PDFs"
scripts = root / ".github/scripts"
today = date.today().isoformat()
def run(name, *args):
    subprocess.run([sys.executable, str(scripts / name), *args], cwd=root, check=True)
run("update_pdf_records.py", "--date", today, "--prepare-index")
run("update_source_format_links.py")
with (pdfdir / "PDF-INDEX.csv").open() as f:
    rows = list(csv.DictReader(f))
new = []
for row in rows:
    pdf = pdfdir / row["pdf_file"]
    if pdf.exists():
        continue
    run("export_page_pdf.py", row["source_file"], str(pdf))
    links = subprocess.check_output(["pdfinfo", "-url", str(pdf)], text=True)
    if not any("https://" in l or "http://" in l for l in links.splitlines()):
        raise SystemExit("No external PDF link annotations: " + pdf.name)
    print("Verified link annotations:", pdf.name, len(links.splitlines()) - 1)
    new.append(pdf.name)
run("update_pdf_records.py", "--date", today)
run("build_pdf_zip.py", "--date", today)
run("set_pdf_release.py", "--date", today, "--initial-only", "--new-pdfs", json.dumps(new))
print("Initial PDFs:", json.dumps(new))
