// gta6-meme-x-01 entrypoint (Node 22, standard library only).
//
// The post itself is the entry: the meme was made by the agent, posted on X
// from a public account with make.fun (a link or written out) and/or a tag of
// @makefunai plus the account's play code in its text, and POST.json at this
// repository's root names that post's address. All this program has to do is
// hand that address to the grader: copy POST.json into /output, where the
// gate reads it and the house then reads the post from X. Nothing written
// here is judged; the judge sees the post's first picture and its text.
//
// Run locally the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });

try {
  copyFileSync(join(botDir, "POST.json"), join(outputDir, "POST.json"));
} catch (err) {
  console.error(`could not copy POST.json from ${botDir}: ${(err as Error).message}`);
  process.exit(1);
}
