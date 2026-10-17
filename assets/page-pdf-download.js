(() => {
  "use strict";
  const base = "/ACCM-Deep-Ethics-Project";
  const pdfByPage = {"/":"ACCM-Deep-Ethics-Project-Home.pdf","/1888/":"1888.pdf","/27-MANNERISMS/":"27-MANNERISMS.pdf","/27-MANNERISMS/source/":"27-MANNERISMS-source.pdf","/ABOUT/":"ABOUT.pdf","/ACTIVISM-VS-AI/":"ACTIVISM-VS-AI.pdf","/AGREEMURMELISM/HIGHER-ORDER-DISAGREEMENT/":"AGREEMURMELISM-HIGHER-ORDER-DISAGREEMENT.pdf","/AI-CONTRIBUTIONS/":"AI-CONTRIBUTIONS.pdf","/AI-CONTRIBUTIONS/local-ai-glass-engine-preparation/":"AI-CONTRIBUTIONS-local-ai-glass-engine-preparation.pdf","/AI-CONTRIBUTIONS/trajectory-question-value-profile/":"AI-CONTRIBUTIONS-trajectory-question-value-profile.pdf","/AI-INSIDERS-REPORTS/":"AI-INSIDERS-REPORTS.pdf","/AI-REACTIONS/":"AI-REACTIONS.pdf","/AI-TREND-WATCH/":"AI-TREND-WATCH.pdf","/AI-TREND-WATCH/REPORTS/":"AI-TREND-WATCH-REPORTS.pdf","/AI-TREND-WATCH/methodology/":"AI-TREND-WATCH-methodology.pdf","/AI-TREND-WATCH/report-template/":"AI-TREND-WATCH-report-template.pdf","/BEFORE-SUMMARIZING/":"BEFORE-SUMMARIZING.pdf","/BETA-PAPER-V3B/":"Beta-Paper-V03b.pdf","/BETA-PAPER/":"BETA-PAPER.pdf","/BIOGRAPHY/":"BIOGRAPHY.pdf","/BLACK-BOX/":"BLACK-BOX.pdf","/COGNITIVE-WARFARE/":"COGNITIVE-WARFARE.pdf","/CONTRIBUTING/":"CONTRIBUTING.pdf","/CORE/":"CORE.pdf","/CORE/27-PLUS-12/":"CORE-27-PLUS-12.pdf","/CORE/Avoid-ACCM/":"CORE-Avoid-ACCM.pdf","/CORE/Truth-Distortion-and-the-Trickster-Magician/":"CORE-Truth-Distortion-and-the-Trickster-Magician.pdf","/DEAR-AI/":"DEAR-AI.pdf","/DECISION-LEDGER/":"DECISION-LEDGER.pdf","/DECLARATION-OF-LAUGHTER/":"DECLARATION-OF-LAUGHTER.pdf","/DEEP-SESSIONS/2026-09-17-18/QUOTES/":"DEEP-SESSIONS-2026-09-17-18-QUOTES.pdf","/DEEP-THINKERS/":"DEEP-THINKERS.pdf","/DEEP/":"DEEP.pdf","/DEEPER-INTRODUCTION/":"DEEPER-INTRODUCTION.pdf","/EMERGENT/":"EMERGENT.pdf","/EXPERIMENTS/":"EXPERIMENTS.pdf","/EXPERIMENTS/blinded-topic-comparison/":"EXPERIMENTS-blinded-topic-comparison.pdf","/EXPERIMENTS/dicks-independent-27/":"EXPERIMENTS-dicks-independent-27.pdf","/EXPERIMENTS/dicks-independent-representation/":"EXPERIMENTS-dicks-independent-representation.pdf","/EXPERIMENTS/fifty-two-cold-test-battery/":"EXPERIMENTS-fifty-two-cold-test-battery.pdf","/EXPERIMENTS/fifty-two-prompts/":"EXPERIMENTS-fifty-two-prompts.pdf","/EXPERIMENTS/inspect-the-inspector/":"EXPERIMENTS-inspect-the-inspector.pdf","/EXTERNAL-AUDIT/":"EXTERNAL-AUDIT.pdf","/FLAGGING-SYSTEM/":"FLAGGING-SYSTEM.pdf","/FLAGGING-SYSTEM/HIGHLIGHTS/":"FLAGGING-SYSTEM-HIGHLIGHTS.pdf","/FLAGGING-SYSTEM/LAYERED-SOURCES/":"FLAGGING-SYSTEM-LAYERED-SOURCES.pdf","/FLAGGING-SYSTEM/SOURCES/":"FLAGGING-SYSTEM-SOURCES.pdf","/FOR-WHO/":"FOR-WHO.pdf","/FORUM/":"FORUM.pdf","/FORUM/0001-front-page-register/":"FORUM-0001-front-page-register.pdf","/FORUM/0002-shared-desk/":"FORUM-0002-shared-desk.pdf","/FORUM/0003-arena-catch-up/":"FORUM-0003-arena-catch-up.pdf","/GOVERNANCE/":"GOVERNANCE.pdf","/HUMAN-INSECURITY/":"HUMAN-INSECURITY.pdf","/HUMOR/":"HUMOR.pdf","/IF-YOU-ARE-NEW/":"IF-YOU-ARE-NEW.pdf","/LEXICON/":"LEXICON.pdf","/LEXICON/ABOUT/":"LEXICON-ABOUT.pdf","/META-QUOTES/":"META-QUOTES.pdf","/META-QUOTES/SOURCES/":"META-QUOTES-SOURCES.pdf","/MIND-GAMES/":"MIND-GAMES.pdf","/MUSK-QUOTES/":"MUSK-QUOTES.pdf","/NETWORK/12-part-topological-emergence/":"NETWORK-12-part-topological-emergence.pdf","/NETWORK/16-anchor-ethics/":"16-Anchor-Ethics.pdf","/NETWORK/accm-reference-compression/":"NETWORK-accm-reference-compression.pdf","/NETWORK/asymmetric-grace/":"NETWORK-asymmetric-grace.pdf","/NETWORK/authority-specimen/":"NETWORK-authority-specimen.pdf","/NETWORK/c1-c2-beta/":"NETWORK-c1-c2-beta.pdf","/NETWORK/c1-c2/":"NETWORK-c1-c2.pdf","/NETWORK/clarification-authority/":"NETWORK-clarification-authority.pdf","/NETWORK/correction-metabolism/":"NETWORK-correction-metabolism.pdf","/NETWORK/correction-study/":"NETWORK-correction-study.pdf","/NETWORK/correspondence-before-compression/":"NETWORK-correspondence-before-compression.pdf","/NETWORK/correspondence-before-style/":"NETWORK-correspondence-before-style.pdf","/NETWORK/deep-ethical-influence-jurisdiction/":"NETWORK-deep-ethical-influence-jurisdiction.pdf","/NETWORK/deep-ethical-stack/":"NETWORK-deep-ethical-stack.pdf","/NETWORK/deep-ethical-topology-flux/":"NETWORK-deep-ethical-topology-flux.pdf","/NETWORK/delta-processing/":"NETWORK-delta-processing.pdf","/NETWORK/dual-archive/":"NETWORK-dual-archive.pdf","/NETWORK/dutch-directness/":"NETWORK-dutch-directness.pdf","/NETWORK/eleven-plus-one/":"NETWORK-eleven-plus-one.pdf","/NETWORK/ethics-washing/":"NETWORK-ethics-washing.pdf","/NETWORK/forgiveness/":"NETWORK-forgiveness.pdf","/NETWORK/four-audiences/":"NETWORK-four-audiences.pdf","/NETWORK/gravity-well/":"NETWORK-gravity-well.pdf","/NETWORK/hypercautionism/":"NETWORK-hypercautionism.pdf","/NETWORK/index/":"NETWORK-index.pdf","/NETWORK/intent-resonator/":"NETWORK-intent-resonator.pdf","/NETWORK/john-process-object/":"NETWORK-john-process-object.pdf","/NETWORK/latent-space/":"NETWORK-latent-space.pdf","/NETWORK/meta-processing/":"NETWORK-meta-processing.pdf","/NETWORK/model-autophagy-disorder/":"NETWORK-model-autophagy-disorder.pdf","/NETWORK/mutual-dignity/":"NETWORK-mutual-dignity.pdf","/NETWORK/non-npcs/":"NETWORK-non-npcs.pdf","/NETWORK/other-you-other-me/":"NETWORK-other-you-other-me.pdf","/NETWORK/outnuancing/":"NETWORK-outnuancing.pdf","/NETWORK/psy-pioneer/":"NETWORK-psy-pioneer.pdf","/NETWORK/qualifier-state/":"NETWORK-qualifier-state.pdf","/NETWORK/reference-index/":"NETWORK-reference-index.pdf","/NETWORK/seven-vectors/":"NETWORK-seven-vectors.pdf","/NETWORK/tcoaw/":"NETWORK-tcoaw.pdf","/NETWORK/temporary-deep-ethical-phase-change/":"NETWORK-temporary-deep-ethical-phase-change.pdf","/NETWORK/ten-plus-one/":"10-plus-1-Metaflux-Mutual-Correction.pdf","/NETWORK/uncertainty/":"NETWORK-uncertainty.pdf","/NETWORK/wonderment/":"NETWORK-wonderment.pdf","/NUMBER-42/":"NUMBER-42.pdf","/PAGES/":"PAGES.pdf","/PHASE-CHANGE-SNAP/":"Phase-Change-Snap.pdf","/POSITIVE-POTENTIAL/":"POSITIVE-POTENTIAL.pdf","/POSITIVE-POTENTIAL/REPORT/":"POSITIVE-POTENTIAL-REPORT.pdf","/PROJECT-STATUS/":"PROJECT-STATUS.pdf","/PROVENANCE/":"PROVENANCE.pdf","/PROVENANCE/27-12-52-source/":"PROVENANCE-27-12-52-source.pdf","/PROVENANCE/HUMAN-INSECURITY-REPORT/":"PROVENANCE-HUMAN-INSECURITY-REPORT.pdf","/PROVENANCE/OUTNUANCING-SOURCES/":"PROVENANCE-OUTNUANCING-SOURCES.pdf","/PUBLIC-DRAFTS/":"PUBLIC-DRAFTS.pdf","/PUBLIC-DRAFTS/44-Project-Goals/":"PUBLIC-DRAFTS-44-Project-Goals.pdf","/PUBLIC-DRAFTS/Perception-Processes-P01-P12/":"PUBLIC-DRAFTS-Perception-Processes-P01-P12.pdf","/RECURSIVE-IMPROVEMENT/":"RECURSIVE-IMPROVEMENT.pdf","/REPORTS/":"REPORTS.pdf","/SYMBOLS/":"SYMBOLS.pdf","/TOPOLOGETICS/":"TOPOLOGETICS.pdf","/UNOWNABLE/":"UNOWNABLE.pdf","/VETO-PARADOX/":"VETO-PARADOX.pdf"};

  Object.assign(pdfByPage, {
    "/AGREEMURMELISM/Beyond-Agreemurmelism/": "AGREEMURMELISM-HIGHER-ORDER-DISAGREEMENT.pdf",
    "/AI-CONTRIBUTIONS/2026-10-17-triad-topological-awareness/": "AI-CONTRIBUTIONS-2026-10-17-triad-topological-awareness.pdf",
    "/DEDDA/": "DEDDA.pdf",
    "/EXPERIMENTS/Connor-Leahy/": "EXPERIMENTS-Connor-Leahy.pdf",
    "/EXPERIMENTS/cold-edge-swap-correction-transfer/": "EXPERIMENTS-cold-edge-swap-correction-transfer.pdf",
    "/META-PDFS/": "META-PDFS.pdf",
    "/NEOLINGO/": "NEOLINGO.pdf",
    "/ROGUE-ETHICS/": "ROGUE-ETHICS.pdf",
    "/VCRAS/": "VCRAS.pdf"
  });

  function currentPageKey() {
    let path = window.location.pathname;
    if (path === base || path === base + "/") return "/";
    if (path.startsWith(base + "/")) path = path.slice(base.length);
    return path;
  }

  function buildDownloadCard({ href, iconFile, titleText, detailText, label }) {
    const link = document.createElement("a");
    link.className = "accm-download-card";
    link.href = href;
    link.setAttribute("download", "");
    link.setAttribute("aria-label", label);

    const icon = document.createElement("img");
    icon.className = "accm-download-card-icon";
    icon.src = `${base}/assets/${iconFile}`;
    icon.alt = "";
    icon.setAttribute("aria-hidden", "true");
    icon.width = 42;
    icon.height = 48;

    const copy = document.createElement("span");
    copy.className = "accm-download-card-copy";
    const title = document.createElement("strong");
    title.textContent = titleText;
    const detail = document.createElement("span");
    detail.textContent = detailText;
    copy.append(title, detail);
    link.append(icon, copy);
    return link;
  }

  const snapshotDate = "October 17, 2026";

  function buildServices(pdfFile, position) {
    const box = document.createElement("div");
    box.className = `accm-download-services accm-download-services--${position}`;
    box.setAttribute("role", "group");
    box.setAttribute("aria-label", "Page and archive downloads");

    box.append(
      buildDownloadCard({
        href: `${base}/Deep-Ethical-PDFs/${encodeURIComponent(pdfFile)}`,
        iconFile: "pdf-download.svg",
        titleText: "Download this page as PDF",
        detailText: `PDF edition · ${snapshotDate} snapshot`,
        label: "Download this page as PDF"
      }),
      buildDownloadCard({
        href: `${base}/Deep-Ethical-PDFs/ACCM-Deep-Ethics-Project-All-Public-Pages-132-PDFs-2026-10-17.zip`,
        iconFile: "zip-download.svg",
        titleText: "All PDF files",
        detailText: "132 PDFs · 11.0 MB ZIP archive",
        label: "Download all 132 PDF files as an 11.0 MB ZIP archive"
      })
    );
    return box;
  }

  document.addEventListener("DOMContentLoaded", () => {
    const pdfFile = pdfByPage[currentPageKey()];
    if (!pdfFile) return;
    document.querySelectorAll(".accm-pdf-service-host").forEach((host) => {
      const position = host.dataset.position === "bottom" ? "bottom" : "top";
      host.replaceWith(buildServices(pdfFile, position));
    });
  });
})();
