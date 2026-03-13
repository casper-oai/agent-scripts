# Personal Customization

Use this file for personal preferences and local onboarding notes.

This file is intentionally flexible Markdown, not machine-parsed config.
The agent should read it before creating deliverables, then choose explicit
values such as output paths, project slugs, naming conventions, and style
decisions.

## How To Onboard

Fill in the sections below before first use.

Things to personalize:

1. Your preferred root folder for visual outputs.
2. Your recurring client, project, or workstream mappings.
3. Any naming conventions you want for folders and files.
4. Your design preferences and any strong dislikes.
5. Any organization- or team-specific rules the agent should remember.

Keep personal names, local filesystem paths, and client-specific routing notes
here rather than hardcoding them in the skill itself.

## Paths

- Preferred visuals root: `/path/to/your/work/visuals`
- Optional secondary root for experiments:

## Project Mapping Notes

Write down how requests should map to project slugs.

Examples:

- Clinical trial and study design work -> `clinical_design_client`
- Internal product strategy work -> `internal_strategy`
- Brand or design-system work -> `design_system`

## Naming Preferences

- Prefer timestamped folders under the project folder
- Use short snake_case request slugs
- Include date folders before timestamp folders

## Visual Preferences

- Preferred font stack:
- Prefer light or dark backgrounds by default:
- Colors to avoid:
- Overall visual taste:
- Notes about density, whitespace, or typography:

## Team / Org Notes

- Add any reusable rules about where outputs should live
- Add any project categories that should always map to the same slug
- Add any stakeholder preferences the agent should preserve

## Notes For Future Reuse

- This is the main file a new adopter should personalize first.
- The helper script will not read this file automatically. The agent should
  read it and pass explicit `--base-dir` and `--project-slug` values to the
  output helper when needed.
