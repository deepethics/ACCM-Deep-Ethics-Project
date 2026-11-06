# ACCM Deep Ethics Project · Field Navigator

A lightweight, responsive, static companion to the canonical **ACCM Deep Ethics Project** website. The public title is intentionally preserved in full; it is never shortened to “ACCM”.

This comparison preview preserves the design, search behavior, artwork and page-index snapshot supplied by the Agent of Arena.ai. The publication pass labels the preview and isolates its offline cache from other apps. The canonical project remains the source of truth.

## What is inside

- A smartphone- and tablet-friendly page navigator with compact link names, search, reading clusters, current development routes, the 52 numbered destinations, and an A–Z link list.
- A local JSON snapshot derived from the linked lists on the official `PAGES` index. The original site remains the source of truth; every destination opens its original project page in a new tab.
- Supplied artwork optimized for web use, subtle animated 🦜🦋🌳 symbols, and a ZIP download link for visitors.
- A small service worker and web app manifest for installability/offline access to the navigator shell after the first visit.

## Run locally

Extract the app ZIP, then serve the extracted `navigator` folder over HTTP so the browser can load `pages.json` and register the service worker:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

The offline cache covers the navigator itself; opening original project articles or downloading the hosted ZIP requires an internet connection.

## Deploy as a static site

Upload the contents of this folder to any static web host (GitHub Pages, Netlify, etc.). Keep `pages.json`, `styles.css`, `app.js`, `sw.js`, the `assets/` directory and `downloads/` directory alongside `index.html`; the visitor download button points to `downloads/ACCM-Deep-Ethics-Project-App.zip`.

## Update the page index

`pages.json` is the offline navigation snapshot. `build_data.py` can rebuild it from the official PAGES index (requires Python packages `beautifulsoup4`). Review changes before publishing; links and counts evolve as the project evolves.

## Attribution and scope

Project text and destinations are linked back to the [official ACCM Deep Ethics Project](https://deepethics.github.io/ACCM-Deep-Ethics-Project/). Artwork and the founder portrait were supplied by John Kuhles for this request. This navigator is a navigation aid, not an alternative source, score, or final partition of the project.
