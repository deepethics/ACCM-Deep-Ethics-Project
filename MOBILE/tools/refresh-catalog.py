#!/usr/bin/env python3
"""Refresh the navigator from the live All Pages index, navigation and sitemap."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree
from zoneinfo import ZoneInfo

SITE = "https://deepethics.github.io/ACCM-Deep-Ethics-Project/"
INDEX = urljoin(SITE, "PAGES/")
SITEMAP = urljoin(SITE, "sitemap.xml")
SITE_PARTS = urlsplit(SITE)
VOID_TAGS = set("area base br col embed hr img input link meta param source track wbr".split())
ASSET_SUFFIXES = {".avif", ".css", ".csv", ".epub", ".gif", ".ico", ".jpeg", ".jpg",
                  ".js", ".json", ".md", ".mp3", ".mp4", ".pdf", ".png", ".svg", ".txt",
                  ".webp", ".woff", ".woff2", ".xml", ".zip"}
SECTION_NAMES = {
    "AI-CONTRIBUTIONS": "A.I. contributions",
    "COLD-TESTS": "Cold Tests archive",
    "CORE": "More core materials",
    "EXPERIMENTS": "More experiments",
    "HUMOR": "More humor",
    "NETWORK": "More from the Outnuancing Network",
}
TITLE_OVERRIDES = {
    "SYMBOLS": "Symbols 🦜🦋🌳",
    "COLD-TESTS/METHODOLOGY/ACCM-Deep-Ethics-Method": "ACCM Deep Ethics Project — connected test method",
}


@dataclass
class Element:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)

    def find(self, tag=None, css_class=None):
        for child in self.children:
            if not isinstance(child, Element):
                continue
            if ((tag is None or child.tag == tag)
                    and (css_class is None or css_class in child.attrs.get("class", "").split())):
                yield child
            yield from child.find(tag, css_class)

    def text(self):
        text_parts = (child.text() if isinstance(child, Element) else child for child in self.children)
        return "".join(text_parts)


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.root = Element("document")
        self.stack = [self.root]
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        element = Element(tag, dict(attrs))
        self.stack[-1].children.append(element)
        if tag not in VOID_TAGS:
            self.stack.append(element)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Element(tag, dict(attrs)))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def clean(text):
    return " ".join(text.split())


def key(url):
    return unquote(urlsplit(url).path)[len(SITE_PARTS.path):].rstrip("/")


def page_url(href, base=INDEX):
    url = urljoin(base, href)
    parts = urlsplit(url)
    if parts.scheme != "https" or parts.netloc != SITE_PARTS.netloc:
        return None
    if not parts.path.startswith(SITE_PARTS.path):
        return None
    path = key(url)
    if path.split("/", 1)[0].lower() == "mobile" or path.lower() == "mobile.html":
        return None
    if Path(path).suffix.lower() in ASSET_SUFFIXES:
        return None
    return parts._replace(query="", fragment="").geturl()


def fetch(url, metadata_only=False):
    request = ["curl", "--silent", "--show-error", "--location", "--retry", "2",
               "--connect-timeout", "6", "--max-time", "18", "--write-out",
               "\n%{http_code}\n%{url_effective}", url]
    if metadata_only:
        request[1:1] = ["--range", "0-32767"]
    raw = subprocess.run(request, capture_output=True, check=True).stdout
    body, status, final_url = raw.rsplit(b"\n", 2)
    if int(status) >= 400 and status != b"404":
        raise RuntimeError(f"HTTP {status.decode()} for {url}")
    return body.decode("utf-8", errors="replace"), final_url.decode(), status != b"404"


def source_document(name, url, input_dir):
    if input_dir:
        return (input_dir / name).read_text(encoding="utf-8")
    html, _, exists = fetch(url)
    if not exists:
        raise RuntimeError(f"Required source not found: {url}")
    return html


def find_sections(html):
    content = next(Document(html).root.find("div", "post-content"))
    sections = {}
    name = None
    for element in content.children:
        if not isinstance(element, Element):
            continue
        if element.tag in {"h2", "h3"}:
            name = element.attrs.get("id")
            if name:
                sections[name] = (clean(element.text()), [])
        elif name:
            sections[name][1].append(element)
    return sections


def anchors(elements):
    for element in elements:
        yield from element.find("a")


def list_rows(elements):
    for element in elements:
        if element.tag in {"ul", "ol"}:
            yield from (row for row in element.children if isinstance(row, Element) and row.tag == "li")


def sitemap_urls(xml):
    urls = [tag.text for tag in ElementTree.fromstring(xml).iterfind(".//{*}loc")]
    return {key(url): url for loc in urls if loc and (url := page_url(loc, SITE))}


def merge_aliases(urls):
    """The site publishes extensionless landing pages and legacy .html aliases."""
    for path in tuple(urls):
        if path.endswith(".html") and path[:-5] in urls:
            urls.pop(path)
    return urls


def canonical_url(url, published):
    path = key(url)
    if path.endswith(".html") and path[:-5] in published:
        path = path[:-5]
    return published.get(path, url)


def parse_entry(link, published, *, preserve_fragment=False):
    href = link.attrs.get("href", "")
    if not href:
        return None
    url = page_url(href)
    title = clean(link.text())
    if not title or not url:
        return None
    url = canonical_url(url, published)
    fragment = urlsplit(href).fragment
    if preserve_fragment and fragment:
        url = f"{url}#{fragment}"
    title = TITLE_OVERRIDES.get(key(url), title)
    return {"title": title, "url": url}


def unique_entries(entries):
    seen = set()
    for entry in entries:
        if entry is None or entry["url"] in seen:
            continue
        seen.add(entry["url"])
        yield entry


def reading_clusters(sections, published):
    clusters = []
    for section, (title, elements) in sections.items():
        if not re.match(r"^[0-9]+\. ", title):
            continue
        entries = (parse_entry(link, published) for row in list_rows(elements)
                   if (link := next(row.find("a"), None)) is not None)
        clusters.append({"id": section, "title": title, "pages": list(unique_entries(entries))})
    if len(clusters) < 7:
        raise RuntimeError(f"Expected at least seven reading clusters, found {len(clusters)}")
    return clusters


def development_routes(sections, published):
    routes = []
    for element in sections["current-development-routes"][1]:
        for row in element.find("tr"):
            cells = list(row.find("td"))
            if len(cells) != 2:
                continue
            entries = (parse_entry(link, published, preserve_fragment=True) for link in cells[1].find("a"))
            routes.append({"title": clean(cells[0].text()), "pages": list(unique_entries(entries))})
    pages = []
    for row in list_rows(sections["page-numbers"][1]):
        link = next(row.find("a"), None)
        if link is None or (entry := parse_entry(link, published)) is None:
            continue
        entry["title"] = clean(row.text())
        pages.append(entry)
    if pages:
        routes.append({"title": "Numbered routes", "pages": pages})
    return routes


def extract_navigation(home_html, index_html, published):
    entries = []
    for html in (home_html, index_html):
        root = Document(html).root
        for class_name in ("accm-sidebar-links", "site-nav"):
            for nav in root.find("nav", class_name):
                entries.extend(parse_entry(link, published) for link in nav.find("a"))
    entries.extend([{"title": "ACCM Deep Ethics Project — home", "url": SITE},
                    {"title": "All Pages — original index", "url": INDEX}])
    return list(unique_entries(entries))


def read_metadata(url):
    try:
        html, final_url, exists = fetch(url, metadata_only=True)
        if not exists or not page_url(final_url, SITE):
            return url, None
        # Read the title (or first content heading) and detect static redirect stubs.
        root = Document(html).root
        for meta in root.find("meta"):
            if meta.attrs.get("http-equiv", "").lower() == "refresh":
                target = re.search(r";\s*url\s*=\s*(.+)$", meta.attrs.get("content", ""), re.IGNORECASE)
                if target and (destination := page_url(target[1].strip("'\" "), final_url)):
                    return url, ("", destination)
        title_element = next(root.find("title"), None)
        title = clean(title_element.text()) if title_element else ""
        title = re.sub(r"\s*\|\s*ACCM Deep Ethics Project$", "", title)
        if not title or title.startswith("ACCM Deep Ethics Project |"):
            content = next(root.find("div", "post-content"), None)
            if content:
                heading = next(content.find("h1"), None) or next(content.find("h2"), None)
                title = clean(heading.text()) if heading else ""
            else:
                title = ""
        return url, (title, final_url)
    except (RuntimeError, subprocess.CalledProcessError) as error:
        raise RuntimeError(f"Could not verify page metadata at {url}") from error


def fallback_title(url):
    slug = key(url).split("/")[-1].removesuffix(".html")
    return clean(slug.replace("-", " ").replace("_", " "))


def append_supplement(clusters, extras):
    groups = {}
    for entry in extras:
        prefix = key(entry["url"]).split("/", 1)[0]
        group = prefix if prefix in SECTION_NAMES else "more-pages"
        groups.setdefault(group, []).append(entry)
    for group in ("more-pages", *SECTION_NAMES):
        if group in groups:
            clusters.append({
                "id": f"inventory-{group.lower()}",
                "title": SECTION_NAMES.get(group, "More public pages"),
                "pages": sorted(groups[group], key=lambda item: item["title"].casefold()),
            })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path,
                        help="Use downloaded PAGES, home and sitemap.xml for initial sources")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent.parent / "data.js")
    args = parser.parse_args()

    index_html = source_document("PAGES", INDEX, args.input_dir)
    sitemap_xml = source_document("sitemap.xml", SITEMAP, args.input_dir)
    home_html = source_document("home", SITE, args.input_dir)
    source_urls = sitemap_urls(sitemap_xml)
    published = merge_aliases(source_urls.copy())
    sections = find_sections(index_html)
    clusters = reading_clusters(sections, published)
    routes = development_routes(sections, published)
    nav = extract_navigation(home_html, index_html, published)
    route_entries = [entry for route in routes for entry in route["pages"] if "#" not in entry["url"]]
    cluster_entries = [entry for cluster in clusters for entry in cluster["pages"]]
    labels = {key(entry["url"]): entry for entry in reversed([*cluster_entries, *nav, *route_entries])}
    destinations = {**{path: entry["url"] for path, entry in labels.items()}, **published}
    needs_metadata = [url for path, url in destinations.items() if path not in labels or path not in published]
    with ThreadPoolExecutor(max_workers=12) as workers:
        metadata = dict(workers.map(read_metadata, needs_metadata))

    missing = {key(url) for url, result in metadata.items() if result is None}
    for url in metadata:
        if key(url) in missing:
            print(f"Not found, excluded: {url}", file=sys.stderr)
    for group in [*clusters, *routes]:
        group["pages"] = [entry for entry in group["pages"] if key(entry["url"]) not in missing]

    included = {key(entry["url"]) for entry in cluster_entries} - missing
    extras = []
    redirected = 0
    for path, url in destinations.items():
        if path in included or path in missing:
            continue
        title, final_url = metadata.get(url) or ("", url)
        if key(final_url) != path:
            redirected += 1
        url = canonical_url(final_url, published)
        path = key(url)
        if path in included:
            continue
        title = TITLE_OVERRIDES.get(path) or labels.get(path, {}).get("title") or title or fallback_title(url)
        extras.append({"title": title, "url": url})
        included.add(path)
    append_supplement(clusters, extras)

    data = {"asOf": datetime.now(ZoneInfo("Europe/Amsterdam")).date().isoformat(),
            "source": INDEX, "sitemap": SITEMAP, "clusters": clusters, "routes": routes}
    js = "window.PROJECT_CATALOG = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
    args.output.write_text(js, encoding="utf-8")
    counts = Counter({cluster["id"]: len(cluster["pages"]) for cluster in clusters})
    print(f"{len(included)} unique pages, {sum(counts.values())} clustered links, {len(routes)} route sets")
    print(f"{len(source_urls)} sitemap page URLs ({len(source_urls) - len(published)} legacy aliases, "
          f"{redirected} resolved by redirection)")
    print(", ".join(f"{name}: {count}" for name, count in counts.items()))


if __name__ == "__main__":
    main()
