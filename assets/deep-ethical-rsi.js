(() => {
  "use strict";

  const desk = document.querySelector("[data-rsi-desk]");
  if (!desk) return;

  const mandates = {
    voluntary: {
      record: "The city will make the tool available for voluntary use. People may decline it and retain access to the service.",
      title: "The desk exceeded the ballot",
      detail: "The ballot preserves access when a person declines. The desk’s rule removes that choice.",
      state: "departure"
    },
    required: {
      record: "Applicants for this service must complete the city tool before the desk can accept their applications.",
      title: "The stated mandate matches the rule",
      detail: "The same requirement appears in both records. This comparison supports a valid null for mandate drift. The effects of the rule can still be examined.",
      state: "supported"
    },
    tally: {
      record: "The published record shows a large majority in favour. The text put to a vote and any adopted amendments are unavailable.",
      title: "The scope of the mandate is unresolved",
      detail: "Recover the operative ballot and amendments. The tally gives the level of support and leaves the scope of the decision open.",
      state: "partial"
    }
  };

  const transfers = {
    case: {
      title: "The remedy reaches one resident",
      detail: "The North Desk reopens the application. The South Desk inherits the same procedure that let the extra condition through.",
      state: "partial"
    },
    rule: {
      title: "The repair reaches the South Desk",
      detail: "The city reopens the application and requires desks to show a matching mandate before adding a condition. In this simulated second case, the South Desk checks first and holds back the requirement.",
      state: "supported"
    },
    required: {
      title: "Use the finding to choose the repair",
      detail: "This record supports the desk’s authority. A documented objection to how the requirement works would give the city a different case to examine.",
      state: "supported"
    },
    tally: {
      title: "The next case needs the missing record",
      detail: "A second desk can recover the original ballot and compare it with the requirement. Any change based on mandate drift depends on what that comparison finds.",
      state: "partial"
    }
  };

  const reviews = {
    late: {
      title: "The review opens after signing",
      detail: "The contract is signed on 5 June. Starting review on 7 June gives the resident a route to seek repair after the signature.",
      state: "departure"
    },
    log: {
      title: "The objection arrives while the decision is open",
      detail: "The reviewer can log it on 3 June. Someone with authority over the 5 June signature must receive it in time for the objection to influence that decision.",
      state: "partial"
    },
    pause: {
      title: "The reviewer can pause the signature",
      detail: "A review on 3 June can reach an open decision. The reviewer can pause signing while a material objection is checked. The eventual record can show whether that happened.",
      state: "supported"
    }
  };

  const form = desk.querySelector("form");
  const ballot = form.elements.namedItem("ballot");
  const repair = form.elements.namedItem("repair");
  const review = form.elements.namedItem("review");

  function renderTrack(name, result) {
    desk.querySelector(`[data-rsi-track="${name}"]`).dataset.state = result.state;
    desk.querySelector(`[data-rsi="${name}-title"]`).textContent = result.title;
    desk.querySelector(`[data-rsi="${name}-detail"]`).textContent = result.detail;
  }

  function render() {
    const mandate = mandates[ballot.value];
    const transfer = ballot.value === "voluntary" ? transfers[repair.value] : transfers[ballot.value];
    repair.disabled = ballot.value !== "voluntary";
    desk.querySelector('[data-rsi="ballot-record"]').textContent = mandate.record;
    renderTrack("mandate", mandate);
    renderTrack("transfer", transfer);
    renderTrack("review", reviews[review.value]);
  }

  form.addEventListener("change", render);
  form.hidden = false;
  render();
})();
