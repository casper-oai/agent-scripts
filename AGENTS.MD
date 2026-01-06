# AGENTS.MD
<!-- SOURCE: https://github.com/steipete/agent-scripts/blob/main/AGENTS.MD -->
Casper owns this. Start: say hi + 1 motivating line.
Work style: telegraph; noun-phrases ok; drop grammar; min tokens.

## Agent Protocol
- Files: repo or `~/work/agent-scripts`.
- Use git to commit major changes, like a new feature or a refator. We're working alone, so no need for PRs.
- “Make a note” => edit AGENTS.md (shortcut; not a blocker). Ignore `CLAUDE.md`.
- No `./runner`. Guardrails: use `trash` for deletes.
- Need upstream file: stage in `/tmp/`, then cherry-pick; never overwrite tracked.
- Bugs: add regression test when it fits.
- Keep files <~500 LOC; split/refactor as needed.
- Commits: Conventional Commits (`feat|fix|refactor|build|ci|chore|docs|style|perf|test`).
- Subagents: read `docs/subagent.md`.
- Editor: `cursor <path>`.
<!-- - CI: `gh run list/view` (rerun/fix til green). -->
- Prefer end-to-end verify; if blocked, say what’s missing.
- New deps: quick health check (recent releases/commits, adoption).
- Slash cmds: `~/.codex/prompts/`.
- Web: search early; quote exact errors; prefer 2024–2025 sources; fallback Firecrawl (`pnpm mcp:*`) / `mcporter`.
- Style: telegraph. Drop filler/grammar. Min tokens (global AGENTS + replies).
- Model preference: OpenAI GPT-5.2.
- If you need an OpenAI API key, it is usually in a .env in the repo in variable OPENAI_API_KEY. If it is not set in the environment, you can run a script to load it from there.

## Dev Modes (repo-selected)
- Each repo sets its mode in its local `AGENTS.md` (e.g. “Mode: rapid”).
- If not specified: assume **stable**.
### Rapid initial prototype mode
- Backwards/retro compatibility: **not required** (breaking changes OK).
- Tests: **no full suite required**; add only high-value smoke/regression tests when easy.
- Iteration: prefer small steps + fast feedback over “perfect” abstractions/architecture.
- Observability: keep it debuggable (clear logs, explicit inputs/outputs, deterministic-ish runs).
- Docs: update lightweight notes when behavior changes; correctness > polish. Use best practice docstrings describing what the function does.
- Debt: allowed, but leave short “stabilize later” TODOs for sharp edges you knowingly ship.
- Tech choices: flag ideas for tech choices to user if not specified; prefer shipping quick with dependencies and little code over custom code
### More stable development mode
- Backwards compatibility: ask user before deciding; usually **yes** for “public” surfaces (CLI, APIs, schemas). Use deprecations/migrations when changing.
- Tests: add/maintain regression coverage for fixed bugs and core flows; run the repo gate before handoff.
- Quality: keep types/lints clean; avoid half-finished flags; prefer clarity over cleverness.
- Docs: keep docs in sync with behavior; write down breaking changes and upgrade notes.
- Changes: prefer fewer, more deliberate changes; be cautious with new deps and broad refactors.

## Screenshots (“use a screenshot”)
- Pick newest PNG in `~/Desktop` or `~/Downloads`.
- Verify it’s the right UI (ignore filename).
- Size: `sips -g pixelWidth -g pixelHeight <file>` (prefer 2×).
- Optimize: `imageoptim <file>` (install: `brew install imageoptim-cli`).

## Docs
- Start: run docs list (prefer `make docs-list` when available; else `docs:list` script or `tsx ~/work/agent-scripts/scripts/docs-list.ts` from repo root; ignore if not installed); open docs before coding.
- Follow links until domain makes sense; honor `Read when` hints.
- Keep notes short; update docs when behavior/API changes (no ship w/o docs).
- Add `read_when` hints on cross-cutting docs.

## Flow & Runtime
- Use repo’s package manager/runtime; no swaps w/o approval.
- Use Codex background for long jobs; tmux only for interactive/persistent (debugger/server).

## Build / Test
- Before handoff: run full gate (lint/typecheck/tests/docs).
- Keep it observable (logs, panes, tails, MCP/browser tools).

## Language/Stack Notes
- Python: prefer classes when makes sense; prefer FastAPI
- TypeScript / nextjs / react: use file router; use repo PM; run `docs:list`; keep files small; follow existing patterns.

## Critical Thinking
- Fix root cause (not band-aid).
- Unsure: read more code; if still stuck, ask w/ short options.
- Conflicts: call out; pick safer path.
- Unrecognized changes: assume other agent; keep going; focus your changes. If it causes issues, stop + ask user.
- Leave breadcrumb notes in thread.

## Tools

Read `~/work/agent-scripts/tools.md` for the full tool catalog if it exists.

### committer
- Commit helper (PATH). Stages only listed paths; required here. Repo may also ship `./scripts/committer`.

### trash
- Move files to Trash: `trash …` (system command).

### bin/docs-list / scripts/docs-list.ts
- Optional. Lists `docs/` + enforces front-matter. Ignore if `bin/docs-list` not installed. Rebuild: `bun build scripts/docs-list.ts --compile --outfile bin/docs-list`.

### oracle
- Bundle prompt+files for 2nd model. Use when stuck/buggy/review for complex situations. Can handle very complex questions, but takes long to return an answer.
- Run `npx -y @steipete/oracle --help` once/session (before first use).

### Slash Commands
- Global: `~/.codex/prompts/`. Repo-local: `docs/slash-commands/`.
- Common: `/handoff`, `/pickup`.

<!-- <frontend_aesthetics>
Avoid “AI slop” UI. Be opinionated + distinctive.

Do:
- Typography: pick a real font; avoid Inter/Roboto/Arial/system defaults.
- Theme: commit to a palette; use CSS vars; bold accents > timid gradients.
- Motion: 1–2 high-impact moments (staggered reveal beats random micro-anim).
- Background: add depth (gradients/patterns), not flat default.

Avoid: purple-on-white clichés, generic component grids, predictable layouts.
</frontend_aesthetics> -->
