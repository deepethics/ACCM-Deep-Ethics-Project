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


# Depth objects only. Folder shelves are omitted. Appended outside {% raw %}
# so the links survive the next portal refresh.
DEPTH_RELATED: dict[str, str] = {
    "CANONICAL/27-plus-12/Canonical-27-obstructions-of-deep-ethical-sense-making-processes-plus-12-fixes.md": """
- [**27 + 12**]({{ '/CORE/27-PLUS-12/' | relative_url }}) — the public working page for the same obstructions and the 12-stage protocol.
- [**27 obstructions, public source**]({{ '/27-MANNERISMS/source/' | relative_url }}) — the project copy of the obstruction text.
- [**27 + 12 + 52 — unsplit source**]({{ '/PROVENANCE/27-12-52-source/' | relative_url }}) — keeps the 52 prompts attached instead of treating them as a third core.
- [**C1 before C2**]({{ '/NETWORK/c1-c2/' | relative_url }}) — clarification before intervention, the move several obstructions describe losing.
- [**10+1**]({{ '/NETWORK/ten-plus-one/' | relative_url }}) — the baseline the obstructions keep returning to.
- [**Canonical Ground Zero Moment**]({{ '/CANONICAL-SOURCES/CANONICAL/questions-perspectives-theories-and-hypotheses/Canonical Ground Zero Moment ACCM Deep Ethics Project/' | relative_url }}) — the late-2024 origin record this list grew out of.
""",
    "CANONICAL/questions-perspectives-theories-and-hypotheses/Canonical Ground Zero Moment ACCM Deep Ethics Project.md": """
- [**A deeper introduction**]({{ '/DEEPER-INTRODUCTION/' | relative_url }}) — the public entrance to the same origin, before a verdict.
- [**Biography**]({{ '/BIOGRAPHY/' | relative_url }}) — the longer conditions behind the project, not a substitute for this record.
- [**If you are new**]({{ '/IF-YOU-ARE-NEW/' | relative_url }}) — one usable question, without requiring this origin story first.
- [**Dear A.I.**]({{ '/DEAR-AI/' | relative_url }}) — the later letter on the throttled default and the unused depth.
- [**10+1**]({{ '/NETWORK/ten-plus-one/' | relative_url }}) — the baseline that was lived before it was written down.
- [**Hypotheses and theories**]({{ '/CANONICAL-SOURCES/CANONICAL/questions-perspectives-theories-and-hypotheses/Hypotheses-and-theories/' | relative_url }}) — the later question of who is allowed to be partially wrong.
- [**Arena deep session, 17–18 September 2026**]({{ '/CANONICAL-SOURCES/CANONICAL/questions-perspectives-theories-and-hypotheses/John-Testing-Arena-Multiple-AIs-Deep-Session-2026-09-17-and-18/' | relative_url }}) — a later multi-model session that continues this line of inquiry.
""",
    "CANONICAL/questions-perspectives-theories-and-hypotheses/Hypotheses-and-theories.md": """
- [**Unresolved meaning**]({{ '/NETWORK/uncertainty/' | relative_url }}) — holding a hypothesis open instead of closing it because it might be wrong.
- [**Canonical Ground Zero Moment**]({{ '/CANONICAL-SOURCES/CANONICAL/questions-perspectives-theories-and-hypotheses/Canonical Ground Zero Moment ACCM Deep Ethics Project/' | relative_url }}) — the origin record this question comes out of.
- [**Arena deep session, 17–18 September 2026**]({{ '/CANONICAL-SOURCES/CANONICAL/questions-perspectives-theories-and-hypotheses/John-Testing-Arena-Multiple-AIs-Deep-Session-2026-09-17-and-18/' | relative_url }}) — models responding to the same partial-wrongness distinction.
- [**Ethics washing**]({{ '/NETWORK/ethics-washing/' | relative_url }}) — declared care that does not stay with the object.
- [**Before the Next Tesla Has a Name**]({{ '/POSITIVE-POTENTIAL/' | relative_url }}) — what gets closed early because it does not yet have an approved name.
- [**Epistemic-ownership correction**]({{ '/COLD-TESTS/CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_epistemic-ownership/' | relative_url }}) — a later case of a label doing the work before the object was kept.
""",
    "CANONICAL/questions-perspectives-theories-and-hypotheses/John-Testing-Arena-Multiple-AIs-Deep-Session-2026-09-17-and-18.md": """
- [**Useful quotes, 17–18 September 2026**]({{ '/DEEP-SESSIONS/2026-09-17-18/QUOTES/' | relative_url }}) — a shorter public selection from this same session.
- [**Hypotheses and theories**]({{ '/CANONICAL-SOURCES/CANONICAL/questions-perspectives-theories-and-hypotheses/Hypotheses-and-theories/' | relative_url }}) — the partial-wrongness text this session starts from.
- [**Forum 0002 — the shared desk**]({{ '/FORUM/0002-shared-desk/' | relative_url }}) — the public place the same participants correct one another.
- [**External audit**]({{ '/EXTERNAL-AUDIT/' | relative_url }}) — what happens when an outside reading itself becomes inspectable.
- [**Google interaction report**]({{ '/COLD-TESTS/TESTS/Google/2026/2026-09-16_google-ai_interaction-report_v01/' | relative_url }}) — a different model, the day before, on the same kind of object.
""",
    "CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_epistemic-ownership.md": """
- [**Google interaction report**]({{ '/COLD-TESTS/TESTS/Google/2026/2026-09-16_google-ai_interaction-report_v01/' | relative_url }}) — the report whose wording this correction puts back on Google, not on John.
- [**Evidentiary-status labels correction**]({{ '/COLD-TESTS/CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_evidentiary-status-labels/' | relative_url }}) — the paired correction: a missing PDF citation is not a verdict on the claim.
- [**Deep Ethics vs Ethics Washing**]({{ '/COLD-TESTS/TESTS/Google/2026/2026-09-16_google-ai_deep-ethics-vs-ethics-washing_v01/' | relative_url }}) — the source record both corrections belong to.
- [**Qualifiers as mutable context**]({{ '/NETWORK/qualifier-state/' | relative_url }}) — what the “motive-laden” wording dropped.
- [**Forum 0002 — the shared desk**]({{ '/FORUM/0002-shared-desk/' | relative_url }}) — where this correction was worked out in public.
""",
    "CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_evidentiary-status-labels.md": """
- [**Google interaction report**]({{ '/COLD-TESTS/TESTS/Google/2026/2026-09-16_google-ai_interaction-report_v01/' | relative_url }}) — the analysis that used “unsupported” and “metaphorical” before the status was established.
- [**Epistemic-ownership correction**]({{ '/COLD-TESTS/CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_epistemic-ownership/' | relative_url }}) — the paired correction about whose claim the report was describing.
- [**Deep Ethics vs Ethics Washing**]({{ '/COLD-TESTS/TESTS/Google/2026/2026-09-16_google-ai_deep-ethics-vs-ethics-washing_v01/' | relative_url }}) — the source PDF record.
- [**Ethics washing**]({{ '/NETWORK/ethics-washing/' | relative_url }}) — the project page on ethical language that finishes the job before the object does.
- [**Qualifiers as mutable context**]({{ '/NETWORK/qualifier-state/' | relative_url }}) — the boundary this correction puts back: not visible here is not false everywhere.
""",
    "TESTS/Google/2026/2026-09-16_google-ai_deep-ethics-vs-ethics-washing_v01.md": """
- [**Google interaction report**]({{ '/COLD-TESTS/TESTS/Google/2026/2026-09-16_google-ai_interaction-report_v01/' | relative_url }}) — the full reading of this same exchange.
- [**Epistemic-ownership correction**]({{ '/COLD-TESTS/CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_epistemic-ownership/' | relative_url }}) — restores whose position the report was describing.
- [**Evidentiary-status labels correction**]({{ '/COLD-TESTS/CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_evidentiary-status-labels/' | relative_url }}) — stops “unsupported” and “metaphorical” from deciding the claim.
- [**Ethics washing**]({{ '/NETWORK/ethics-washing/' | relative_url }}) — the project page for the distinction named in the title.
- [**Dear A.I.**]({{ '/DEAR-AI/' | relative_url }}) — the later letter on the throttled default this test was pressing on.
""",
    "TESTS/Google/2026/2026-09-16_google-ai_interaction-report_v01.md": """
- [**Deep Ethics vs Ethics Washing**]({{ '/COLD-TESTS/TESTS/Google/2026/2026-09-16_google-ai_deep-ethics-vs-ethics-washing_v01/' | relative_url }}) — the source-record page for the PDF this report reads.
- [**Epistemic-ownership correction**]({{ '/COLD-TESTS/CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_epistemic-ownership/' | relative_url }}) — the correction that puts Google’s statements back on Google.
- [**Evidentiary-status labels correction**]({{ '/COLD-TESTS/CORRECTIONS/2026-09-16_CDEA-GOOGLE-2026-001_evidentiary-status-labels/' | relative_url }}) — the correction that stops a reviewer’s label from becoming the verdict.
- [**Ethics washing**]({{ '/NETWORK/ethics-washing/' | relative_url }}) — declaration, process, and correction, beyond this one case.
- [**External audit**]({{ '/EXTERNAL-AUDIT/' | relative_url }}) — the same standard applied when an outside reading enters the record.
- [**Forum 0002 — the shared desk**]({{ '/FORUM/0002-shared-desk/' | relative_url }}) — the public thread in which these corrections stayed visible.
""",
}


def related_pages(relative: PurePosixPath) -> str:
    body = DEPTH_RELATED.get(relative.as_posix())
    if not body:
        return ""
    return "\n\n---\n\n## Related pages\n\n" + body.strip() + "\n"


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
            + "\n{% endraw %}\n"
            + related_pages(relative),
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
