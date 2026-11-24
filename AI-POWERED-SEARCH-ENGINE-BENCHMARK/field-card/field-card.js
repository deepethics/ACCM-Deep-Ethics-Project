(() => {
  const worksheet = document.getElementById("citation-worksheet");
  if (!worksheet) return;

  const pairs = Array.from(worksheet.querySelectorAll("textarea, input, select"), (field) => {
    const printValue = document.createElement("div");
    printValue.className = "card-print-value";
    printValue.setAttribute("aria-hidden", "true");
    field.after(printValue);
    return { field, printValue };
  });

  window.addEventListener("beforeprint", () => {
    for (const { field, printValue } of pairs) printValue.textContent = field.value;
  });

  worksheet.querySelector("#print-citation-card").addEventListener("click", () => window.print());
  worksheet.querySelector("#save-citation-notes").addEventListener("click", () => {
    const sections = pairs.map(({ field }) => `${field.labels[0].textContent}\n${field.value.trim()}`);
    const notes = new Blob([`Three-Minute Citation Check\n\n${sections.join("\n\n")}\n`], {
      type: "text/plain;charset=utf-8",
    });
    const downloadUrl = URL.createObjectURL(notes);
    const link = document.createElement("a");
    link.href = downloadUrl;
    link.download = "citation-check-notes.txt";
    link.click();
    // Leave the URL available while the browser starts the download.
    window.setTimeout(() => URL.revokeObjectURL(downloadUrl), 1000);
  });

  worksheet.querySelector(".card-actions").hidden = false;
})();
