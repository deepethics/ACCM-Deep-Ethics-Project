#!/usr/bin/env python3
"""Export one Jekyll Markdown page as a portable, linked A4 PDF."""

from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PUBLIC_BASE = "https://deepethics.github.io/ACCM-Deep-Ethics-Project"


def frontmatter_value(text: str, key: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    frontmatter = text.split("---\n", 2)[1]
    match = re.search(rf"^{re.escape(key)}:\s*[\"']?(.*?)[\"']?\s*$", frontmatter, re.MULTILINE)
    return match.group(1) if match else None


def expand_includes(text: str, source: Path) -> str:
    relative_pattern = re.compile(r"{%\s*include_relative\s+([^\s%]+)(?:\s+[^%]*)?%}")

    def replace_relative(match: re.Match[str]) -> str:
        include_path = source.parent / match.group(1)
        if include_path.is_file():
            return include_path.read_text(encoding="utf-8")
        return ""

    text = relative_pattern.sub(replace_relative, text)
    pattern = re.compile(r"{%\s*include\s+([^\s%]+)(?:\s+[^%]*)?%}")

    def replace(match: re.Match[str]) -> str:
        include_path = ROOT / "_includes" / match.group(1)
        if include_path.is_file():
            return include_path.read_text(encoding="utf-8")
        return ""

    return pattern.sub(replace, text)


def normalize_markdown(source: Path) -> tuple[str, str]:
    text = source.read_text(encoding="utf-8")
    title = frontmatter_value(text, "title") or source.stem.replace("-", " ").title()
    if text.startswith("---\n"):
        text = text.split("---\n", 2)[2]
    text = re.sub(
        r"<!-- ACCM_FORMAT_LINKS_START -->.*?<!-- ACCM_FORMAT_LINKS_END -->\n*",
        "",
        text,
        flags=re.DOTALL,
    )
    text = expand_includes(text, source)

    # Turn Jekyll-generated internal links into durable public URLs.
    text = re.sub(
        r"{{\s*['\"]([^'\"]+)['\"]\s*\|\s*relative_url\s*}}",
        lambda match: PUBLIC_BASE + (match.group(1) if match.group(1).startswith("/") else "/" + match.group(1)),
        text,
    )
    text = re.sub(r"{{\s*site\.baseurl\s*}}", PUBLIC_BASE, text)
    text = re.sub(r"{{.*?}}", "", text)
    text = re.sub(r"{%.*?%}", "", text)
    text = re.sub(r"(?m)^\$$", "$$", text)

    # Keep the project's symbol signature readable in PDF fonts.
    text = text.replace("🦜🦋🌳", "[parrot] [butterfly] [tree]")
    return title, text.strip() + "\n"


def export_pdf(source: Path, output: Path) -> None:
    title, body = normalize_markdown(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="accm-pdf-") as temp_dir:
        normalized = Path(temp_dir) / "page.md"
        normalized.write_text(body, encoding="utf-8")
        command = [
            "pandoc",
            str(normalized),
            "--from=markdown+raw_html+smart+tex_math_single_backslash-strikeout",
            "--pdf-engine=xelatex",
            "--toc",
            "--number-sections",
            f"--metadata=title:{title}",
            "--metadata=author:ACCM Deep Ethics Project",
            "--variable=papersize:a4",
            "--variable=geometry:margin=24mm",
            "--variable=fontsize:10pt",
            "--variable=mainfont:DejaVu Sans",
            "--variable=sansfont:DejaVu Sans",
            "--variable=monofont:DejaVu Sans Mono",
            "--variable=colorlinks:true",
            "--variable=linkcolor:NavyBlue",
            "--variable=urlcolor:NavyBlue",
            "--variable=toccolor:NavyBlue",
            f"--resource-path={source.parent}:{ROOT}",
            "--output",
            str(output),
        ]
        subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    source = args.source if args.source.is_absolute() else ROOT / args.source
    output = args.output if args.output.is_absolute() else ROOT / args.output
    export_pdf(source, output)


if __name__ == "__main__":
    main()
