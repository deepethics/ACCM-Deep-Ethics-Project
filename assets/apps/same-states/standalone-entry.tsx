import { useState } from "react";
import { createRoot } from "react-dom/client";
import { CityMap } from "@/components/city-map";
import { SevenMap } from "@/components/seven-map";



function Home() {
  const [land, setLand] = useState<"21" | "7">("21");
  const on21 = land === "21";

  return (
    <main className="mx-auto flex min-h-screen max-w-3xl flex-col gap-6 px-4 py-8 sm:px-6 sm:py-12">
      <header className="flex flex-col gap-3">
        <p className="font-mono text-xs tracking-widest text-faint uppercase">
          {on21 ? "Modulo 21" : "Modulo 7"}
        </p>
        <h1 className="font-serif text-4xl text-fg sm:text-5xl">Same states</h1>
        <p className="max-w-xl text-lg text-muted">
          {on21
            ? "Twenty-one residues sit on three streets. A change of base does not move them. It only changes which arrow leaves each one."
            : "Seven residues, two triangles. Doubling stays inside one. The complement crosses."}
        </p>
        <div className="flex flex-wrap gap-2" role="radiogroup" aria-label="Landscape">
          <button
            type="button"
            role="radio"
            aria-checked={on21}
            onClick={() => setLand("21")}
            className={
              "min-h-11 rounded-full border px-3 py-2 font-mono text-sm " +
              (on21 ? "border-accent bg-accent text-ink" : "border-line bg-surface text-fg")
            }
          >
            Modulo 21
          </button>
          <button
            type="button"
            role="radio"
            aria-checked={!on21}
            onClick={() => setLand("7")}
            className={
              "min-h-11 rounded-full border px-3 py-2 font-mono text-sm " +
              (!on21 ? "border-accent bg-accent text-ink" : "border-line bg-surface text-fg")
            }
          >
            Modulo 7
          </button>
        </div>
        <a
          href="./same-states-source.zip"
          download="same-states-source.zip"
          className="w-fit font-mono text-sm text-accent underline decoration-accent underline-offset-4"
        >
          Download the supplied source ZIP
        </a>
      </header>
      {on21 ? <CityMap /> : <SevenMap />}
      {on21 ? (
        <footer className="grid gap-3 border-t border-line pt-4 text-sm text-muted sm:grid-cols-2">
          <p>Inner ring, marked 0. Multiples of three. The sevenths, and 142857.</p>
          <p>Middle and outer rings. Streets 1 and 2. Day 0 holds 0, 7, and 14, where the week-counter reads zero.</p>
        </footer>
      ) : (
        <footer className="border-t border-line pt-4 text-sm text-muted">
          Left triangle 1, 2, 4. Right triangle 3, 6, 5. Their three-bit blocks are complements. Compose
          −1 and the two triangles become one six-cycle. Retrace walks ×4 or ×3, the inverses, which are
          not named settings.
        </footer>
      )}
    </main>
  );
}
createRoot(document.getElementById("root")!).render(<Home />);
