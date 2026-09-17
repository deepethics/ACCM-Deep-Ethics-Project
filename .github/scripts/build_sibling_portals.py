#!/usr/bin/env python3
"""Build read-only GitHub Pages mirrors from the two public sibling repositories."""

from __future__ import annotations

import argparse
import posixpath
import re
import shutil
import subprocess
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


LINK_RE = re.compile(r"(?P<label>!?\[[^\]]*\])\((?P<target>[^)]+)\)")
SITE_BASEURL = "/ACCM-Deep-Ethics-Project"


def public_link(route: str) -> str:
    """Return an absolute project-site path for generated source content."""
    return SITE_BASEURL + route


def git_commit(repo: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    return text[end + 5 :] if end != -1 else text


def title_from(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback.replace("-", " ").replace("_", " ").strip().title()


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def md_route(prefix: str, relative: PurePosixPath) -> str:
    if relative.name.lower() == "readme.md":
        parts = relative.parent.parts
    else:
        parts = relative.with_suffix("").parts
    suffix = "/".join(parts)
    return f"/{prefix}/{suffix}/" if suffix else f"/{prefix}/"


def destination_for(site: Path, prefix: str, relative: PurePosixPath) -> Path:
    route = md_route(prefix, relative).strip("/")
    return site / route / "index.md"


def resolve_relative(source: PurePosixPath, target: str) -> PurePosixPath:
    decoded = unquote(target)
    resolved = posixpath.normpath(posixpath.join(str(source.parent), decoded))
    return PurePosixPath(resolved)


def rewrite_links(
    text: str,
    source: PurePosixPath,
    prefix: str,
    source_repo_url: str,
    known_markdown: set[PurePosixPath],
    known_directories: set[PurePosixPath],
) -> str:
    def replace(match: re.Match[str]) -> str:
        label = match.group("label")
        target = match.group("target").strip()
        if target.startswith(("http://", "https://", "mailto:", "#", "{{")):
            return match.group(0)

        path_part, hash_mark, anchor = target.partition("#")
        resolved = resolve_relative(source, path_part)
        anchor_text = f"#{anchor}" if hash_mark else ""

        if resolved in known_markdown:
            new_target = public_link(md_route(prefix, resolved)) + anchor_text
        elif resolved in known_directories and resolved / "README.md" in known_markdown:
            new_target = public_link(md_route(prefix, resolved / "README.md")) + anchor_text
        elif resolved.suffix.lower() == ".pdf":
            new_target = public_link(f"/{prefix}/{resolved.as_posix()}") + anchor_text
        else:
            new_target = f"{source_repo_url}/blob/main/{resolved.as_posix()}" + anchor_text
        return f"{label}({new_target})"

    return LINK_RE.sub(replace, text)


def build_portal(
    *,
    source_repo: Path,
    site_repo: Path,
    prefix: str,
    source_repo_name: str,
    source_repo_url: str,
    role: str,
    mirror_canonical_warning: bool,
) -> None:
    output_root = site_repo / prefix
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True)

    commit = git_commit(source_repo)
    markdown_files = sorted(
        PurePosixPath(path.relative_to(source_repo).as_posix())
        for path in source_repo.rglob("*.md")
        if ".git" not in path.parts
    )
    known_markdown = set(markdown_files)
    known_directories = {p.parent for p in markdown_files}

    for relative in markdown_files:
        source_file = source_repo / Path(relative.as_posix())
        original = strip_front_matter(source_file.read_text(encoding="utf-8"))
        title = title_from(original, relative.stem)
        if relative.parts[0] == "CANONICAL" and relative.name.lower() != "readme.md":
            title = relative.stem.replace("-", " ").replace("_", " ")
        rewritten = rewrite_links(
            original,
            relative,
            prefix,
            source_repo_url,
            known_markdown,
            known_directories,
        )
        destination = destination_for(site_repo, prefix, relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        source_link = f"{source_repo_url}/blob/{commit}/{relative.as_posix()}"
        canonical_note = (
            " This rendered copy helps visitors read the source; canonical status remains "
            "controlled by the Canonical Index and checksum manifest in the source repository."
            if mirror_canonical_warning
            else " This rendered copy does not replace the archived source record."
        )
        destination.write_text(
            "---\n"
            "layout: page\n"
            f"title: {yaml_quote(title)}\n"
            f"permalink: {md_route(prefix, relative)}\n"
            "---\n\n"
            f"> **Read-only generated mirror.** Source: [{source_repo_name}]({source_link}) at commit "
            f"[`{commit[:12]}`]({source_repo_url}/commit/{commit}).{canonical_note}\n\n"
            f"[Back to the {role} portal]({public_link(f'/{prefix}/')})\n\n"
            "---\n\n"
            "{% raw %}\n"
            + rewritten.rstrip()
            + "\n{% endraw %}\n",
            encoding="utf-8",
        )

    for pdf in source_repo.rglob("*.pdf"):
        if ".git" in pdf.parts:
            continue
        relative = pdf.relative_to(source_repo)
        destination = output_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, destination)

    landing = output_root / "index.md"
    readme = source_repo / "README.md"
    readme_content = strip_front_matter(readme.read_text(encoding="utf-8")) if readme.exists() else ""
    readme_content = rewrite_links(
        readme_content,
        PurePosixPath("README.md"),
        prefix,
        source_repo_url,
        known_markdown,
        known_directories,
    )

    page_links = []
    for relative in markdown_files:
        if relative == PurePosixPath("README.md"):
            continue
        source_text = (source_repo / Path(relative.as_posix())).read_text(encoding="utf-8")
        page_title = title_from(strip_front_matter(source_text), relative.stem)
        if relative.parts[0] == "CANONICAL" and relative.name.lower() != "readme.md":
            page_title = relative.stem.replace("-", " ").replace("_", " ")
        page_links.append(f"- [{page_title}]({public_link(md_route(prefix, relative))})")

    pdf_links = []
    for pdf in sorted(source_repo.rglob("*.pdf")):
        if ".git" in pdf.parts:
            continue
        relative = PurePosixPath(pdf.relative_to(source_repo).as_posix())
        pdf_links.append(
            f"- [{relative.name}]({public_link(f'/{prefix}/{relative.as_posix()}')})"
        )

    warning = (
        "The source repository—not this generated rendering—controls canonical status, wording, "
        "checksums, supersession, and withdrawal."
        if mirror_canonical_warning
        else "The testing repository remains the source archive. Publication here is not endorsement of an A.I. output or interpretation."
    )
    landing.write_text(
        "---\n"
        "layout: page\n"
        f"title: {yaml_quote(role)}\n"
        f"permalink: /{prefix}/\n"
        "---\n\n"
        f"# {role}\n\n"
        f"> **Automatically refreshed read-only portal.** Built from [{source_repo_name}]({source_repo_url}) "
        f"at commit [`{commit[:12]}`]({source_repo_url}/commit/{commit}).\n\n"
        f"{warning}\n\n"
        "## Rendered pages\n\n"
        + ("\n".join(page_links) if page_links else "No Markdown pages found.")
        + "\n\n"
        + ("## PDF records\n\n" + "\n".join(pdf_links) + "\n\n" if pdf_links else "")
        + "## Source-repository introduction\n\n"
        + "{% raw %}\n"
        + readme_content.rstrip()
        + "\n{% endraw %}\n",
        encoding="utf-8",
    )

    print(
        f"Generated {prefix}: {len(markdown_files)} Markdown pages, "
        f"{len(pdf_links)} PDFs, source commit {commit}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--canonical", type=Path, required=True)
    parser.add_argument("--cold-tests", type=Path, required=True)
    args = parser.parse_args()

    build_portal(
        source_repo=args.canonical,
        site_repo=args.site,
        prefix="CANONICAL-SOURCES",
        source_repo_name="Canonical Files — ACCM Deep Ethics Project",
        source_repo_url="https://github.com/deepethics/Canonical-Files-ACCM-Deep-Ethics-Project",
        role="Canonical Sources — ACCM Deep Ethics Project",
        mirror_canonical_warning=True,
    )
    build_portal(
        source_repo=args.cold_tests,
        site_repo=args.site,
        prefix="COLD-TESTS",
        source_repo_name="Cold Deep-Ethics Testing of Default A.I.s",
        source_repo_url="https://github.com/deepethics/Cold-DeepEthics-Testing-Default-AIs",
        role="Cold Deep-Ethics Testing of Default A.I.s",
        mirror_canonical_warning=False,
    )


if __name__ == "__main__":
    main()
