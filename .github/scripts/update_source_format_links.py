#!/usr/bin/env python3
"""Add synchronized HTML/PDF routes to every indexed Markdown source."""

from __future__ import annotations

import csv
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / "Deep-Ethical-PDFs"
PUBLIC_BASE = "https://deepethics.github.io/ACCM-Deep-Ethics-Project"
START = "<!-- ACCM_FORMAT_LINKS_START -->"
END = "<!-- ACCM_FORMAT_LINKS_END -->"
BLOCK_PATTERN = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}\n*", re.DOTALL)
FRONTMATTER_PATTERN = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def format_block(public_url: str, pdf_file: str) -> str:
    pdf_url = f"{PUBLIC_BASE}/Deep-Ethical-PDFs/{quote(pdf_file)}"
    return (
        f"{START}\n"
        '<div class="accm-source-format-links" role="navigation" aria-label="Available page formats">\n'
        "<strong>Available formats:</strong> "
        f'<a href="{public_url}">🌐 Public HTML page</a>'
        '<span aria-hidden="true"> · </span>'
        f'<a href="{pdf_url}">📄 PDF edition</a>\n'
        "</div>\n"
        f"{END}\n"
    )


def main() -> None:
    with (PDF_DIR / "PDF-INDEX.csv").open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))

    changed = 0
    for row in rows:
        source = ROOT / row["source_file"]
        text = source.read_text(encoding="utf-8")
        text_without_block = BLOCK_PATTERN.sub("", text)
        frontmatter = FRONTMATTER_PATTERN.match(text_without_block)
        if not frontmatter:
            raise SystemExit(f"Indexed source has no YAML front matter: {row['source_file']}")

        block = format_block(row["public_url"], row["pdf_file"])
        updated = (
            text_without_block[: frontmatter.end()]
            + "\n"
            + block
            + "\n"
            + text_without_block[frontmatter.end() :].lstrip("\n")
        )
        if updated != text:
            source.write_text(updated, encoding="utf-8")
            changed += 1

    print(f"Source format links: {len(rows)} indexed pages, {changed} files updated")


if __name__ == "__main__":
    main()
