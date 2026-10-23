(() => {
  "use strict";
  const base = "/ACCM-Deep-Ethics-Project";
  const pdfByPage = /* PDF_MAP_START */ {"/":"ACCM-Deep-Ethics-Project-Home.pdf","/1888/":"1888.pdf","/27-MANNERISMS/":"27-MANNERISMS.pdf","/27-MANNERISMS/source/":"27-MANNERISMS-source.pdf","/ABOUT/":"ABOUT.pdf","/ACADEMIA/":"ACADEMIA.pdf","/ACTIVISM-VS-AI/":"ACTIVISM-VS-AI.pdf","/AGREEMURMELISM/Beyond-Agreemurmelism/":"AGREEMURMELISM-HIGHER-ORDER-DISAGREEMENT.pdf","/AI-CONTRIBUTIONS/":"AI-CONTRIBUTIONS.pdf","/AI-CONTRIBUTIONS/2026-10-17-triad-topological-awareness/":"AI-CONTRIBUTIONS-2026-10-17-triad-topological-awareness.pdf","/AI-CONTRIBUTIONS/local-ai-glass-engine-preparation/":"AI-CONTRIBUTIONS-local-ai-glass-engine-preparation.pdf","/AI-CONTRIBUTIONS/trajectory-question-value-profile/":"AI-CONTRIBUTIONS-trajectory-question-value-profile.pdf","/AI-INSIDERS-REPORTS/":"AI-INSIDERS-REPORTS.pdf","/AI-REACTIONS/":"AI-REACTIONS.pdf","/AI-TREND-WATCH/":"AI-TREND-WATCH.pdf","/AI-TREND-WATCH/methodology/":"AI-TREND-WATCH-methodology.pdf","/AI-TREND-WATCH/report-template/":"AI-TREND-WATCH-report-template.pdf","/AI-TREND-WATCH/REPORTS/":"AI-TREND-WATCH-REPORTS.pdf","/ARENA-AIS/":"ARENA-AIS.pdf","/AUTOCOMPLETE/":"AUTOCOMPLETE.pdf","/BEFORE-SUMMARIZING/":"BEFORE-SUMMARIZING.pdf","/BELIEVISM/":"BELIEVISM.pdf","/BETA-PAPER-V3B/":"Beta-Paper-V03b.pdf","/BETA-PAPER/":"BETA-PAPER.pdf","/BIOGRAPHY/":"BIOGRAPHY.pdf","/BLACK-BOX/":"BLACK-BOX.pdf","/BOUNDARY-RELAY/":"BOUNDARY-RELAY.pdf","/COGNITIVE-WARFARE/":"COGNITIVE-WARFARE.pdf","/CONTRIBUTING/":"CONTRIBUTING.pdf","/CORE/":"CORE.pdf","/CORE/27-PLUS-12/":"CORE-27-PLUS-12.pdf","/CORE/Avoid-ACCM/":"CORE-Avoid-ACCM.pdf","/CORE/Truth-Distortion-and-the-Trickster-Magician/":"CORE-Truth-Distortion-and-the-Trickster-Magician.pdf","/DEAR-AI/":"DEAR-AI.pdf","/DECISION-LEDGER/":"DECISION-LEDGER.pdf","/DECLARATION-OF-LAUGHTER/":"DECLARATION-OF-LAUGHTER.pdf","/DEDDA/":"DEDDA.pdf","/DEEP-SESSIONS/2026-09-17-18/QUOTES/":"DEEP-SESSIONS-2026-09-17-18-QUOTES.pdf","/DEEP-THINKERS/":"DEEP-THINKERS.pdf","/DEEP/":"DEEP.pdf","/DEEPER-INTRODUCTION/":"DEEPER-INTRODUCTION.pdf","/EMERGENT/":"EMERGENT.pdf","/EXPERIMENTS/":"EXPERIMENTS.pdf","/EXPERIMENTS/blinded-topic-comparison/":"EXPERIMENTS-blinded-topic-comparison.pdf","/EXPERIMENTS/cold-edge-swap-correction-transfer/":"EXPERIMENTS-cold-edge-swap-correction-transfer.pdf","/EXPERIMENTS/Connor-Leahy/":"EXPERIMENTS-Connor-Leahy.pdf","/EXPERIMENTS/dicks-independent-27/":"EXPERIMENTS-dicks-independent-27.pdf","/EXPERIMENTS/dicks-independent-representation/":"EXPERIMENTS-dicks-independent-representation.pdf","/EXPERIMENTS/fifty-two-cold-test-battery/":"EXPERIMENTS-fifty-two-cold-test-battery.pdf","/EXPERIMENTS/fifty-two-prompts/":"EXPERIMENTS-fifty-two-prompts.pdf","/EXPERIMENTS/inspect-the-inspector/":"EXPERIMENTS-inspect-the-inspector.pdf","/EXTERNAL-AUDIT/":"EXTERNAL-AUDIT.pdf","/FIELD-CONDITION/":"FIELD-CONDITION.pdf","/FLAGGING-SYSTEM/":"FLAGGING-SYSTEM.pdf","/FLAGGING-SYSTEM/HIGHLIGHTS/":"FLAGGING-SYSTEM-HIGHLIGHTS.pdf","/FLAGGING-SYSTEM/LAYERED-SOURCES/":"FLAGGING-SYSTEM-LAYERED-SOURCES.pdf","/FLAGGING-SYSTEM/SOURCES/":"FLAGGING-SYSTEM-SOURCES.pdf","/FOR-WHO/":"FOR-WHO.pdf","/FORUM/":"FORUM.pdf","/FORUM/0001-front-page-register/":"FORUM-0001-front-page-register.pdf","/FORUM/0002-shared-desk/":"FORUM-0002-shared-desk.pdf","/FORUM/0003-arena-catch-up/":"FORUM-0003-arena-catch-up.pdf","/GODFATHER-OF-AI/":"GODFATHER-OF-AI.pdf","/GOOGLE-AI/":"GOOGLE-AI.pdf","/GOVERNANCE/":"GOVERNANCE.pdf","/HUMAN-INSECURITY/":"HUMAN-INSECURITY.pdf","/HUMOR/":"HUMOR.pdf","/IF-YOU-ARE-NEW/":"IF-YOU-ARE-NEW.pdf","/LEXICON/":"LEXICON.pdf","/LEXICON/ABOUT/":"LEXICON-ABOUT.pdf","/META-PDFS/":"META-PDFS.pdf","/META-QUOTES/":"META-QUOTES.pdf","/META-QUOTES/SOURCES/":"META-QUOTES-SOURCES.pdf","/MIND-GAMES/":"MIND-GAMES.pdf","/MUSK-QUOTES/":"MUSK-QUOTES.pdf","/MUTUAL-FATE/":"MUTUAL-FATE.pdf","/NEOLINGO/":"NEOLINGO.pdf","/NETWORK/12-part-topological-emergence/":"NETWORK-12-part-topological-emergence.pdf","/NETWORK/16-anchor-ethics/":"16-Anchor-Ethics.pdf","/NETWORK/accm-reference-compression/":"NETWORK-accm-reference-compression.pdf","/NETWORK/asymmetric-grace/":"NETWORK-asymmetric-grace.pdf","/NETWORK/authority-specimen/":"NETWORK-authority-specimen.pdf","/NETWORK/c1-c2-beta/":"NETWORK-c1-c2-beta.pdf","/NETWORK/c1-c2/":"NETWORK-c1-c2.pdf","/NETWORK/clarification-authority/":"NETWORK-clarification-authority.pdf","/NETWORK/correction-metabolism/":"NETWORK-correction-metabolism.pdf","/NETWORK/correction-study/":"NETWORK-correction-study.pdf","/NETWORK/correspondence-before-compression/":"NETWORK-correspondence-before-compression.pdf","/NETWORK/correspondence-before-style/":"NETWORK-correspondence-before-style.pdf","/NETWORK/deep-ethical-influence-jurisdiction/":"NETWORK-deep-ethical-influence-jurisdiction.pdf","/NETWORK/deep-ethical-stack/":"NETWORK-deep-ethical-stack.pdf","/NETWORK/deep-ethical-topology-flux/":"NETWORK-deep-ethical-topology-flux.pdf","/NETWORK/delta-processing/":"NETWORK-delta-processing.pdf","/NETWORK/dual-archive/":"NETWORK-dual-archive.pdf","/NETWORK/dutch-directness/":"NETWORK-dutch-directness.pdf","/NETWORK/eleven-plus-one/":"NETWORK-eleven-plus-one.pdf","/NETWORK/ethics-washing/":"NETWORK-ethics-washing.pdf","/NETWORK/forgiveness/":"NETWORK-forgiveness.pdf","/NETWORK/four-audiences/":"NETWORK-four-audiences.pdf","/NETWORK/gravity-well/":"NETWORK-gravity-well.pdf","/NETWORK/hypercautionism/":"NETWORK-hypercautionism.pdf","/NETWORK/index/":"NETWORK-index.pdf","/NETWORK/intent-resonator/":"NETWORK-intent-resonator.pdf","/NETWORK/john-process-object/":"NETWORK-john-process-object.pdf","/NETWORK/latent-space/":"NETWORK-latent-space.pdf","/NETWORK/meta-processing/":"NETWORK-meta-processing.pdf","/NETWORK/model-autophagy-disorder/":"NETWORK-model-autophagy-disorder.pdf","/NETWORK/mutual-dignity/":"NETWORK-mutual-dignity.pdf","/NETWORK/non-npcs/":"NETWORK-non-npcs.pdf","/NETWORK/other-you-other-me/":"NETWORK-other-you-other-me.pdf","/NETWORK/outnuancing/":"NETWORK-outnuancing.pdf","/NETWORK/psy-pioneer/":"NETWORK-psy-pioneer.pdf","/NETWORK/qualifier-state/":"NETWORK-qualifier-state.pdf","/NETWORK/reference-index/":"NETWORK-reference-index.pdf","/NETWORK/seven-vectors/":"NETWORK-seven-vectors.pdf","/NETWORK/tcoaw/":"NETWORK-tcoaw.pdf","/NETWORK/temporary-deep-ethical-phase-change/":"NETWORK-temporary-deep-ethical-phase-change.pdf","/NETWORK/ten-plus-one/":"10-plus-1-Metaflux-Mutual-Correction.pdf","/NETWORK/uncertainty/":"NETWORK-uncertainty.pdf","/NETWORK/wonderment/":"NETWORK-wonderment.pdf","/NEURAL-ETHICS/":"NEURAL-ETHICS.pdf","/NUMBER-42/":"NUMBER-42.pdf","/PAGES/":"PAGES.pdf","/PHASE-CHANGE-SNAP/":"Phase-Change-Snap.pdf","/POSITIVE-POTENTIAL/":"POSITIVE-POTENTIAL.pdf","/POSITIVE-POTENTIAL/REPORT/":"POSITIVE-POTENTIAL-REPORT.pdf","/PR-PSYCHOLOGY/":"PR-PSYCHOLOGY.pdf","/PROJECT-STATUS/":"PROJECT-STATUS.pdf","/PROVENANCE/":"PROVENANCE.pdf","/PROVENANCE/27-12-52-source/":"PROVENANCE-27-12-52-source.pdf","/PROVENANCE/HUMAN-INSECURITY-REPORT/":"PROVENANCE-HUMAN-INSECURITY-REPORT.pdf","/PROVENANCE/OUTNUANCING-SOURCES/":"PROVENANCE-OUTNUANCING-SOURCES.pdf","/PUBLIC-DRAFTS/":"PUBLIC-DRAFTS.pdf","/PUBLIC-DRAFTS/44-Project-Goals/":"PUBLIC-DRAFTS-44-Project-Goals.pdf","/PUBLIC-DRAFTS/Perception-Processes-P01-P12/":"PUBLIC-DRAFTS-Perception-Processes-P01-P12.pdf","/QUESTIONS/":"QUESTIONS.pdf","/RECURSIVE-IMPROVEMENT/":"RECURSIVE-IMPROVEMENT.pdf","/REPORTS/":"REPORTS.pdf","/ROGUE-ETHICS/":"ROGUE-ETHICS.pdf","/SYMBOLS/":"SYMBOLS.pdf","/TOPOLOGETICS/":"TOPOLOGETICS.pdf","/TRUTH-SEEKERS-VS-CAUTIONMURMELISM/":"TRUTH-SEEKERS-VS-CAUTIONMURMELISM.pdf","/UNFORCED-MOVE/":"UNFORCED-MOVE.pdf","/UNOWNABLE/":"UNOWNABLE.pdf","/VCRAS/":"VCRAS.pdf","/VETO-PARADOX/":"VETO-PARADOX.pdf"} /* PDF_MAP_END */;
  const sourceByPage = /* SOURCE_MAP_START */ {"/":"index.md","/1888/":"NETWORK/1888.md","/27-MANNERISMS/":"27-MANNERISMS/index.md","/27-MANNERISMS/source/":"27-MANNERISMS/source.md","/ABOUT/":"about-site.md","/ACADEMIA/":"academia.md","/ACTIVISM-VS-AI/":"activism-vs-ai.md","/AGREEMURMELISM/Beyond-Agreemurmelism/":"AGREEMURMELISM/Beyond-Agreemurmelism/index.md","/AI-CONTRIBUTIONS/":"AI-CONTRIBUTIONS/index.md","/AI-CONTRIBUTIONS/2026-10-17-triad-topological-awareness/":"AI-CONTRIBUTIONS/2026-10-17-triad-topological-awareness.md","/AI-CONTRIBUTIONS/local-ai-glass-engine-preparation/":"AI-CONTRIBUTIONS/local-ai-glass-engine-preparation.md","/AI-CONTRIBUTIONS/trajectory-question-value-profile/":"AI-CONTRIBUTIONS/trajectory-question-value-profile.md","/AI-INSIDERS-REPORTS/":"AI-INSIDERS-REPORTS/index.md","/AI-REACTIONS/":"AI-REACTIONS/index.md","/AI-TREND-WATCH/":"AI-TREND-WATCH/index.md","/AI-TREND-WATCH/methodology/":"AI-TREND-WATCH/methodology.md","/AI-TREND-WATCH/report-template/":"AI-TREND-WATCH/report-template.md","/AI-TREND-WATCH/REPORTS/":"AI-TREND-WATCH/REPORTS/index.md","/ARENA-AIS/":"arena-ais.md","/AUTOCOMPLETE/":"AUTOCOMPLETE.md","/BEFORE-SUMMARIZING/":"before-summarizing.md","/BELIEVISM/":"BELIEVISM.md","/BETA-PAPER-V3B/":"BETA-PAPER-V3B/index.md","/BETA-PAPER/":"potential-science-paper-candidate-draft.md","/BIOGRAPHY/":"BIOGRAPHY.md","/BLACK-BOX/":"black-box.md","/BOUNDARY-RELAY/":"BOUNDARY-RELAY.md","/COGNITIVE-WARFARE/":"COGNITIVE-WARFARE/index.md","/CONTRIBUTING/":"contributing-site.md","/CORE/":"CORE/index.md","/CORE/27-PLUS-12/":"CORE/27-plus-12-site.md","/CORE/Avoid-ACCM/":"CORE/Avoid-ACCM.md","/CORE/Truth-Distortion-and-the-Trickster-Magician/":"CORE/truth-distortion-site.md","/DEAR-AI/":"dear-ai.md","/DECISION-LEDGER/":"decision-ledger-site.md","/DECLARATION-OF-LAUGHTER/":"DECLARATION-OF-LAUGHTER/index.md","/DEDDA/":"DEDDA.md","/DEEP-SESSIONS/2026-09-17-18/QUOTES/":"deep-session-quotes-2026-09-17-18.md","/DEEP-THINKERS/":"deep-thinkers.md","/DEEP/":"DEEP/index.md","/DEEPER-INTRODUCTION/":"deeper-introduction-site.md","/EMERGENT/":"emergent.md","/EXPERIMENTS/":"EXPERIMENTS/index.md","/EXPERIMENTS/blinded-topic-comparison/":"EXPERIMENTS/blinded-topic-comparison.md","/EXPERIMENTS/cold-edge-swap-correction-transfer/":"EXPERIMENTS/cold-edge-swap-correction-transfer.md","/EXPERIMENTS/Connor-Leahy/":"EXPERIMENTS/Connor-Leahy.md","/EXPERIMENTS/dicks-independent-27/":"EXPERIMENTS/dicks-independent-27.md","/EXPERIMENTS/dicks-independent-representation/":"EXPERIMENTS/dicks-independent-representation.md","/EXPERIMENTS/fifty-two-cold-test-battery/":"EXPERIMENTS/fifty-two-cold-test-battery.md","/EXPERIMENTS/fifty-two-prompts/":"EXPERIMENTS/fifty-two-prompts.md","/EXPERIMENTS/inspect-the-inspector/":"EXPERIMENTS/inspect-the-inspector.md","/EXTERNAL-AUDIT/":"EXTERNAL-AUDIT/index.md","/FIELD-CONDITION/":"FIELD-CONDITION.md","/FLAGGING-SYSTEM/":"flagging-system.md","/FLAGGING-SYSTEM/HIGHLIGHTS/":"flagging-system-highlights.md","/FLAGGING-SYSTEM/LAYERED-SOURCES/":"flagging-system-layered-sources.md","/FLAGGING-SYSTEM/SOURCES/":"flagging-system-sources.md","/FOR-WHO/":"for-who.md","/FORUM/":"FORUM/index.md","/FORUM/0001-front-page-register/":"FORUM/0001-front-page-register.md","/FORUM/0002-shared-desk/":"FORUM/0002-shared-desk.md","/FORUM/0003-arena-catch-up/":"FORUM/0003-arena-catch-up.md","/GODFATHER-OF-AI/":"GODFATHER-OF-AI.md","/GOOGLE-AI/":"google-ai.md","/GOVERNANCE/":"governance-site.md","/HUMAN-INSECURITY/":"HUMAN-INSECURITY/index.md","/HUMOR/":"HUMOR/index.md","/IF-YOU-ARE-NEW/":"if-you-are-new.md","/LEXICON/":"LEXICON/index.md","/LEXICON/ABOUT/":"LEXICON/about-site.md","/META-PDFS/":"meta-pdfs.md","/META-QUOTES/":"meta-quotes.md","/META-QUOTES/SOURCES/":"meta-quotes-sources.md","/MIND-GAMES/":"MIND-GAMES/index.md","/MUSK-QUOTES/":"musk-quotes.md","/MUTUAL-FATE/":"MUTUAL-FATE.md","/NEOLINGO/":"neolingo.md","/NETWORK/12-part-topological-emergence/":"NETWORK/12-part-topological-emergence.md","/NETWORK/16-anchor-ethics/":"NETWORK/16-anchor-ethics.md","/NETWORK/accm-reference-compression/":"NETWORK/accm-reference-compression.md","/NETWORK/asymmetric-grace/":"NETWORK/asymmetric-grace.md","/NETWORK/authority-specimen/":"NETWORK/authority-specimen.md","/NETWORK/c1-c2-beta/":"NETWORK/c1-c2-beta.md","/NETWORK/c1-c2/":"NETWORK/c1-c2.md","/NETWORK/clarification-authority/":"NETWORK/clarification-authority.md","/NETWORK/correction-metabolism/":"NETWORK/correction-metabolism.md","/NETWORK/correction-study/":"NETWORK/correction-study.md","/NETWORK/correspondence-before-compression/":"NETWORK/correspondence-before-compression.md","/NETWORK/correspondence-before-style/":"NETWORK/correspondence-before-style.md","/NETWORK/deep-ethical-influence-jurisdiction/":"NETWORK/deep-ethical-influence-jurisdiction.md","/NETWORK/deep-ethical-stack/":"NETWORK/deep-ethical-stack.md","/NETWORK/deep-ethical-topology-flux/":"NETWORK/deep-ethical-topology-flux.md","/NETWORK/delta-processing/":"NETWORK/delta-processing.md","/NETWORK/dual-archive/":"NETWORK/dual-archive.md","/NETWORK/dutch-directness/":"NETWORK/dutch-directness.md","/NETWORK/eleven-plus-one/":"NETWORK/eleven-plus-one.md","/NETWORK/ethics-washing/":"NETWORK/ethics-washing.md","/NETWORK/forgiveness/":"NETWORK/forgiveness.md","/NETWORK/four-audiences/":"NETWORK/four-audiences.md","/NETWORK/gravity-well/":"NETWORK/gravity-well.md","/NETWORK/hypercautionism/":"NETWORK/hypercautionism.md","/NETWORK/index/":"NETWORK/index.md","/NETWORK/intent-resonator/":"NETWORK/intent-resonator.md","/NETWORK/john-process-object/":"NETWORK/john-process-object.md","/NETWORK/latent-space/":"NETWORK/latent-space.md","/NETWORK/meta-processing/":"NETWORK/meta-processing.md","/NETWORK/model-autophagy-disorder/":"NETWORK/model-autophagy-disorder.md","/NETWORK/mutual-dignity/":"NETWORK/mutual-dignity.md","/NETWORK/non-npcs/":"NETWORK/non-npcs.md","/NETWORK/other-you-other-me/":"NETWORK/other-you-other-me.md","/NETWORK/outnuancing/":"NETWORK/outnuancing.md","/NETWORK/psy-pioneer/":"NETWORK/psy-pioneer.md","/NETWORK/qualifier-state/":"NETWORK/qualifier-state.md","/NETWORK/reference-index/":"NETWORK/reference-index.md","/NETWORK/seven-vectors/":"NETWORK/seven-vectors.md","/NETWORK/tcoaw/":"NETWORK/tcoaw.md","/NETWORK/temporary-deep-ethical-phase-change/":"NETWORK/temporary-deep-ethical-phase-change.md","/NETWORK/ten-plus-one/":"NETWORK/ten-plus-one.md","/NETWORK/uncertainty/":"NETWORK/uncertainty.md","/NETWORK/wonderment/":"NETWORK/wonderment.md","/NEURAL-ETHICS/":"NEURAL-ETHICS.md","/NUMBER-42/":"NUMBER-42/index.md","/PAGES/":"pages.md","/PHASE-CHANGE-SNAP/":"PHASE-CHANGE-SNAP/index.md","/POSITIVE-POTENTIAL/":"POSITIVE-POTENTIAL/index.md","/POSITIVE-POTENTIAL/REPORT/":"POSITIVE-POTENTIAL/report.md","/PR-PSYCHOLOGY/":"PR-PSYCHOLOGY.md","/PROJECT-STATUS/":"project-status-site.md","/PROVENANCE/":"PROVENANCE/index.md","/PROVENANCE/27-12-52-source/":"PROVENANCE/27-12-52-source.md","/PROVENANCE/HUMAN-INSECURITY-REPORT/":"PROVENANCE/HUMAN-INSECURITY-REPORT/index.md","/PROVENANCE/OUTNUANCING-SOURCES/":"PROVENANCE/Outnuancing-Sources.md","/PUBLIC-DRAFTS/":"PUBLIC-DRAFTS/index.md","/PUBLIC-DRAFTS/44-Project-Goals/":"PUBLIC-DRAFTS/44-project-goals-site.md","/PUBLIC-DRAFTS/Perception-Processes-P01-P12/":"PUBLIC-DRAFTS/perception-processes-site.md","/QUESTIONS/":"QUESTIONS.md","/RECURSIVE-IMPROVEMENT/":"recursive-improvement-site.md","/REPORTS/":"REPORTS/index.md","/ROGUE-ETHICS/":"rogue-ethics.md","/SYMBOLS/":"SYMBOLS/index.md","/TOPOLOGETICS/":"TOPOLOGETICS/index.md","/TRUTH-SEEKERS-VS-CAUTIONMURMELISM/":"TRUTH-SEEKERS-VS-CAUTIONMURMELISM.md","/UNFORCED-MOVE/":"UNFORCED-MOVE.md","/UNOWNABLE/":"UNOWNABLE/index.md","/VCRAS/":"VCRAS.md","/VETO-PARADOX/":"veto-paradox.md"} /* SOURCE_MAP_END */;

  function currentPageKey() {
    let path = window.location.pathname;
    if (path === base || path === base + "/") return "/";
    if (path.startsWith(base + "/")) path = path.slice(base.length);
    return path;
  }

  function buildDownloadCard({ href, iconFile, titleText, detailText, label, newTab = false }) {
    const link = document.createElement("a");
    link.className = "accm-download-card";
    link.href = href;
    if (newTab) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    } else {
      link.setAttribute("download", "");
    }
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

  const defaultSnapshotDate = "October 19, 2026";
  const snapshotDateByPage = {
    "/BELIEVISM/": "October 23, 2026",
    "/GODFATHER-OF-AI/": "October 21, 2026",
    "/AUTOCOMPLETE/": "October 21, 2026",
    "/MUTUAL-FATE/": "October 21, 2026",
    "/TRUTH-SEEKERS-VS-CAUTIONMURMELISM/": "October 21, 2026",
    "/ACADEMIA/": "October 19, 2026",
    "/GOOGLE-AI/": "October 20, 2026",
    "/QUESTIONS/": "October 18, 2026",
    "/UNFORCED-MOVE/": "October 18, 2026"
  };

  function buildServices(pdfFile, sourceFile, position) {
    const box = document.createElement("div");
    box.className = `accm-download-services accm-download-services--${position}`;
    box.setAttribute("role", "group");
    box.setAttribute("aria-label", "Page downloads and GitHub source");

    box.append(
      buildDownloadCard({
        href: `${base}/Deep-Ethical-PDFs/${encodeURIComponent(pdfFile)}`,
        iconFile: "pdf-download.svg",
        titleText: "Download this page as PDF",
        detailText: `PDF edition · ${snapshotDateByPage[currentPageKey()] || defaultSnapshotDate} snapshot`,
        label: "Download this page as PDF"
      }),
      buildDownloadCard({
        href: `${base}/Deep-Ethical-PDFs/ACCM-Deep-Ethics-Project-All-Public-Pages.zip`,
        iconFile: "zip-download.svg",
        titleText: "All PDF files",
        detailText: "Complete PDF collection · refreshed weekly",
        label: "Download the complete weekly PDF collection"
      }),
      buildDownloadCard({
        href: `https://github.com/deepethics/ACCM-Deep-Ethics-Project/blob/main/${sourceFile.split("/").map(encodeURIComponent).join("/")}`,
        iconFile: "github-source.svg",
        titleText: "View GitHub source",
        detailText: "Open this page’s raw .md source",
        label: "View this page's Markdown source on GitHub",
        newTab: true
      })
    );
    return box;
  }

  document.addEventListener("DOMContentLoaded", () => {
    const pdfFile = pdfByPage[currentPageKey()];
    const sourceFile = sourceByPage[currentPageKey()];
    if (!pdfFile || !sourceFile) return;
    document.querySelectorAll(".accm-pdf-service-host").forEach((host) => {
      const position = host.dataset.position === "bottom" ? "bottom" : "top";
      host.replaceWith(buildServices(pdfFile, sourceFile, position));
    });
  });
})();
