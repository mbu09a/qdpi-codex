import fs from "node:fs";
import path from "node:path";

export function loadPrompt(): string {
  const promptPath = path.resolve(__dirname, "../../corpus/corpus-preamble.md");
  return fs.readFileSync(promptPath, "utf-8");
}

export function runAgent(_args: string[]): void {
  // For now, just print the prompt
  console.log(loadPrompt());
}
