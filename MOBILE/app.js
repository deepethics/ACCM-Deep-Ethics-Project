(() => {
  "use strict";

  const data = window.PROJECT_CATALOG;
  const search = document.querySelector("#search");
  const catalog = document.querySelector("#catalog");
  if (!search || !catalog) return;

  const clear = document.querySelector("#clear-search");
  const alphabet = document.querySelector("#alphabet");
  const expand = document.querySelector("#expand-groups");
  const expandLabel = expand?.querySelector("[data-expand-label]") || expand;
  const empty = document.querySelector("#empty") || document.createElement("div");
  const modeButtons = [...document.querySelectorAll("button[data-mode]")];
  const densityButtons = [...document.querySelectorAll("button[data-density]")];
  const compare = new Intl.Collator("en", { numeric: true, sensitivity: "base" }).compare;
  const formatCount = new Intl.NumberFormat("en").format;
  const bookmarkKey = "deep-ethics-navigator-bookmarks-v1";
  const densityKey = "deep-ethics-navigator-density-v1";
  const views = {
    clusters: "Browse clusters",
    az: "Browse A–Z",
    saved: "Bookmarks"
  };

  if (window.location?.protocol === "file:") {
    const archive = "ACCM-Deep-Ethics-Project-Mobile-Navigator.zip";
    document.querySelectorAll("a[download]").forEach(link => {
      if (link.getAttribute("href") !== "./" + archive) return;
      link.href = "https://deepethics.github.io/ACCM-Deep-Ethics-Project/MOBILE/" + archive;
      link.removeAttribute("download");
    });
  }

  function element(tag, className, label) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (label) node.textContent = label;
    return node;
  }

  function setText(selector, value) {
    const node = document.querySelector(selector);
    if (node && node.textContent !== value) node.textContent = value;
  }

  function load(key, fallback) {
    try {
      return JSON.parse(window.localStorage.getItem(key)) ?? fallback;
    } catch {
      return fallback;
    }
  }

  function save(key, value) {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch {
      // Bookmarks and density still work for the current visit.
    }
  }

  function normalize(value) {
    return value.normalize("NFKD")
      .toLowerCase()
      .replace(/\p{M}/gu, "")
      .replace(/\b([a-z])\.(?=[a-z](?:\.|\b))/g, "$1")
      .replace(/\+/g, " plus ")
      .replace(/[^\p{L}\p{N}\p{Extended_Pictographic}]+/gu, " ")
      .trim();
  }

  function searchablePath(url) {
    try {
      return decodeURIComponent(new URL(url).pathname).replace(/^\/ACCM-Deep-Ethics-Project\/?/i, "");
    } catch {
      return "";
    }
  }

  const uniquePages = new Map();
  const clusters = (data?.clusters || []).map((cluster, index) => {
    const group = {
      id: cluster.id,
      title: cluster.title,
      badge: String(index + 1).padStart(2, "0"),
      terms: normalize(cluster.title).split(" "),
      pages: []
    };
    for (const entry of cluster.pages) {
      if (!/^https:\/\//i.test(entry.url)) continue;
      let page = uniquePages.get(entry.url);
      if (!page) {
        page = {
          title: entry.title,
          url: entry.url,
          terms: new Set(normalize(searchablePath(entry.url)).split(" ")),
          clusterTerms: new Set()
        };
        uniquePages.set(page.url, page);
      }
      if (group.pages.includes(page)) continue;
      normalize(entry.title).split(" ").forEach(term => page.terms.add(term));
      group.terms.forEach(term => page.clusterTerms.add(term));
      group.pages.push(page);
    }
    return group;
  }).filter(group => group.pages.length);

  const pages = [...uniquePages.values()].sort((a, b) => compare(a.title, b.title));

  const letterGroups = new Map();
  for (const page of pages) {
    const first = normalize(page.title).match(/[\p{L}\p{N}]/u)?.[0] || "";
    const letter = /^[a-z]$/.test(first) ? first.toUpperCase() : "#";
    const badge = /^\d$/.test(first) ? "0–9" : letter;
    if (!letterGroups.has(badge)) {
      const id = badge === "0–9" ? "numbers" : badge === "#" ? "other" : badge;
      letterGroups.set(badge, { id, title: badge, badge, pages: [] });
    }
    letterGroups.get(badge).pages.push(page);
  }
  const az = [...letterGroups.values()].sort((a, b) => {
    if (a.badge === "#") return 1;
    if (b.badge === "#") return -1;
    return compare(a.badge, b.badge);
  });

  const prior = window.history.state?.deepEthicsNavigator;
  let mode = Object.hasOwn(views, prior?.mode) ? prior.mode : "clusters";
  if (typeof prior?.search === "string") search.value = prior.search;

  const storedBookmarks = load(bookmarkKey, []);
  const bookmarks = new Set(Array.isArray(storedBookmarks) ? storedBookmarks : []);
  const openGroups = {
    clusters: new Set(prior?.clusters || clusters.slice(0, 1).map(group => group.id)),
    az: new Set(prior?.az || az.slice(0, 1).map(group => group.id))
  };

  const sourceDate = document.querySelector("#source-date");
  if (sourceDate && /^\d{4}-\d{2}-\d{2}$/.test(data?.asOf || "")) {
    const date = new Date(data.asOf + "T00:00:00Z");
    if (!Number.isNaN(date.getTime())) {
      sourceDate.dateTime = data.asOf;
      sourceDate.textContent = date.toLocaleDateString("en-GB", {
        day: "numeric",
        month: "long",
        year: "numeric",
        timeZone: "UTC"
      });
    }
  }

  function pageCount(count) {
    return formatCount(count) + (count === 1 ? " page" : " pages");
  }

  function setDensity(value) {
    const density = value === "comfortable" ? "comfortable" : "compact";
    document.body.dataset.density = density;
    densityButtons.forEach(button => {
      button.setAttribute("aria-pressed", String(button.dataset.density === density));
    });
  }

  function bookmarkIcon() {
    const namespace = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(namespace, "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("width", "16");
    svg.setAttribute("height", "16");
    svg.setAttribute("aria-hidden", "true");
    svg.setAttribute("focusable", "false");

    const path = document.createElementNS(namespace, "path");
    path.setAttribute("d", "M6 4.75h12v15l-6-4-6 4z");
    path.setAttribute("stroke", "currentColor");
    path.setAttribute("stroke-width", "1.6");
    path.setAttribute("stroke-linejoin", "round");
    svg.append(path);
    return svg;
  }

  function updateBookmark(button, url) {
    const active = bookmarks.has(url);
    button.setAttribute("aria-pressed", String(active));
    button.title = active ? "Remove bookmark" : "Save bookmark";
    button.firstElementChild.setAttribute("fill", active ? "currentColor" : "none");
  }

  function pageGrid(list) {
    const grid = element("ul", "page-grid");
    grid.setAttribute("role", "list");
    for (const page of list) {
      const row = element("li", "page-row");
      const link = element("a", "page-link");
      link.href = page.url;
      link.append(element("span", "page-title", page.title));

      const button = element("button", "save-page");
      button.type = "button";
      button.dataset.bookmark = page.url;
      button.setAttribute("aria-label", "Bookmark " + page.title);
      button.append(bookmarkIcon());
      updateBookmark(button, page.url);
      row.append(link, button);
      grid.append(row);
    }
    return grid;
  }

  function groupNode(group, filtering) {
    const details = element("details", "catalog-group");
    details.id = "group-" + mode + "-" + group.id;
    details.open = filtering || openGroups[mode].has(group.id);
    const summary = element("summary", "group-summary");
    const number = element("span", "group-number", group.badge);
    number.setAttribute("aria-hidden", "true");
    const chevron = element("span", "group-chevron", "⌄");
    chevron.setAttribute("aria-hidden", "true");
    summary.append(
      number,
      element("span", "group-title", group.title.replace(/^\d+\.\s+/, "")),
      element("span", "group-count", pageCount(group.pages.length)),
      chevron
    );
    details.append(summary, pageGrid(group.pages));
    const remembered = openGroups[mode];
    details.addEventListener("toggle", () => {
      if (!details.isConnected) return;
      if (!filtering) {
        if (details.open) remembered.add(group.id);
        else remembered.delete(group.id);
      }
      syncExpand();
    });
    return details;
  }

  function syncExpand() {
    if (!expand) return;
    const groups = [...catalog.querySelectorAll("details")];
    expand.hidden = groups.length < 2;
    const allOpen = groups.length > 0 && groups.every(group => group.open);
    expandLabel.textContent = allOpen ? "Collapse all" : "Expand all";
  }

  function showAlphabet(groups) {
    if (!alphabet) return;
    alphabet.hidden = !groups.length;
    alphabet.replaceChildren();
    for (const group of groups) {
      const id = "group-az-" + group.id;
      const button = element("button", "alphabet-jump", group.badge);
      button.type = "button";
      button.setAttribute("aria-label", "Jump to " + group.title);
      button.setAttribute("aria-controls", id);
      button.addEventListener("click", () => {
        const details = document.getElementById(id);
        details.open = true;
        const summary = details.querySelector("summary");
        summary.focus({ preventScroll: true });
        summary.scrollIntoView({ block: "start" });
      });
      alphabet.append(button);
    }
  }

  function showEmpty(noResults, filtering) {
    empty.hidden = !noResults;
    if (!empty.isConnected) catalog.after(empty);
    if (!noResults) return;

    let title = "The directory is unavailable";
    let description = "You can still use the original project index.";
    if (filtering) {
      title = "No matching pages";
      description = "Try a shorter search or switch to another view.";
    } else if (mode === "saved" && pages.length) {
      title = "No bookmarks yet";
      description = "Use the bookmark button beside any page to keep it here.";
    }

    empty.replaceChildren(element("h3", "empty-title", title), element("p", "empty-copy", description));
    if (filtering) {
      const button = element("button", "empty-action", "Clear search");
      button.type = "button";
      button.addEventListener("click", resetSearch);
      empty.append(button);
    } else if (mode === "saved" && pages.length) {
      const button = element("button", "empty-action", "Browse clusters");
      button.type = "button";
      button.addEventListener("click", () => {
        setMode("clusters");
        modeButtons.find(candidate => candidate.dataset.mode === "clusters")?.focus();
      });
      empty.append(button);
    } else if (data?.source && /^https:\/\//i.test(data.source)) {
      const link = element("a", "empty-action", "Open the project index");
      link.href = data.source;
      empty.append(link);
    }
  }

  function syncSavedCount() {
    const count = pages.filter(page => bookmarks.has(page.url)).length;
    setText("#saved-count", formatCount(count));
  }

  function includesTerm(words, term) {
    return term.length <= 2 ? words.includes(term) : words.some(word => word.includes(term));
  }

  function render() {
    const query = normalize(search.value);
    const terms = query ? query.split(" ") : [];
    const matches = (page, clusterTerms = page.clusterTerms) => {
      const words = [...page.terms, ...clusterTerms];
      return terms.every(term => includesTerm(words, term));
    };
    if (clear) clear.hidden = !search.value;

    const groups = mode === "saved" ? [] : (mode === "az" ? az : clusters)
      .map(group => ({ ...group, pages: group.pages.filter(page => matches(page, group.terms)) }))
      .filter(group => group.pages.length);
    const matchingPages = mode === "saved"
      ? pages.filter(page => bookmarks.has(page.url) && matches(page))
      : [...new Set(groups.flatMap(group => group.pages))];

    if (mode === "saved") {
      catalog.replaceChildren(...(matchingPages.length ? [pageGrid(matchingPages)] : []));
    } else {
      catalog.replaceChildren(...groups.map(group => groupNode(group, Boolean(query))));
    }
    setText("#result-count", pageCount(matchingPages.length));
    setText("#catalog-heading", views[mode]);
    showAlphabet(mode === "az" ? groups : []);
    showEmpty(!matchingPages.length, Boolean(query));
    syncSavedCount();
    syncExpand();
  }

  function setMode(value) {
    if (!Object.hasOwn(views, value)) return;
    mode = value;
    modeButtons.forEach(button => {
      button.setAttribute("aria-pressed", String(button.dataset.mode === mode));
    });
    render();
  }

  function resetSearch() {
    search.value = "";
    render();
    search.focus();
  }

  function rememberView() {
    try {
      window.history.replaceState({
        ...window.history.state,
        deepEthicsNavigator: { mode, search: search.value, clusters: [...openGroups.clusters], az: [...openGroups.az] }
      }, "");
    } catch {
      // Returning with the browser cache still preserves the live page.
    }
  }

  clear?.addEventListener("click", resetSearch);
  search.addEventListener("input", render);
  search.form?.addEventListener("submit", event => event.preventDefault());
  search.addEventListener("keydown", event => {
    if (event.key === "Escape" && search.value) {
      event.preventDefault();
      resetSearch();
    }
  });

  modeButtons.forEach(button => {
    button.addEventListener("click", () => setMode(button.dataset.mode));
  });
  densityButtons.forEach(button => {
    button.addEventListener("click", () => {
      setDensity(button.dataset.density);
      save(densityKey, document.body.dataset.density);
    });
  });

  expand?.addEventListener("click", () => {
    const groups = [...catalog.querySelectorAll("details")];
    const shouldOpen = groups.some(group => !group.open);
    groups.forEach(group => { group.open = shouldOpen; });
    syncExpand();
  });

  catalog.addEventListener("click", event => {
    const button = event.target.closest("button[data-bookmark]");
    if (!button) {
      if (event.target.closest("a.page-link")) rememberView();
      return;
    }
    const url = button.dataset.bookmark;
    if (bookmarks.has(url)) bookmarks.delete(url);
    else bookmarks.add(url);
    save(bookmarkKey, [...bookmarks]);

    const buttons = [...catalog.querySelectorAll("button[data-bookmark]")];
    if (mode === "saved") {
      const index = buttons.indexOf(button);
      render();
      const remaining = catalog.querySelectorAll("button[data-bookmark]");
      const next = remaining[index] || remaining[index - 1] ||
        modeButtons.find(candidate => candidate.dataset.mode === "saved");
      next?.focus();
    } else {
      buttons.filter(candidate => candidate.dataset.bookmark === url)
        .forEach(candidate => updateBookmark(candidate, url));
      syncSavedCount();
    }
  });

  window.addEventListener("pagehide", rememberView);
  setText("#catalog-count", formatCount(pages.length));
  setText("#cluster-count", formatCount(clusters.length));
  setDensity(load(densityKey, "compact"));
  setMode(mode);
})();
