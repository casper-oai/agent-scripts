---
name: html-slide-pages
description: Create polished standalone, editable HTML pages as a replacement for PPTX slides. Use when a user asks for slide-like visuals, presentation pages, or browser-first deliverables in HTML. Save outputs under the configured visuals root, preview the rendered page, and visually validate it before replying.
metadata:
  short-description: Build browser-first HTML slide pages.
---

# HTML Slide Pages

Use this skill when the user wants HTML pages instead of PPTX slides.

## Personal Customization

- Before sharing or reusing this skill on a different machine, update [references/personal-customization.md](references/personal-customization.md).
- This file is where personal paths, default project mappings, and style preferences belong.
- Keep user-specific details there instead of hardcoding them in the skill instructions, templates, or helper scripts.
- The output helper script does not parse this file automatically. The agent should read it and pass explicit values when needed.

Onboarding notes:
- Fill in your preferred visuals root folder.
- Add your common client/project mappings and naming notes.
- Write down personal visual preferences you want future edits to respect.
- Keep anything person-specific or org-specific in that file instead of the main skill.

## Workflow

1. Pick the project slug.
   - Reuse an existing folder under your configured visuals root when it already fits.
   - Read [references/personal-customization.md](references/personal-customization.md) first and use its notes to choose `project_slug`, `base_dir`, and local style decisions.
   - If the mapping is still ambiguous, ask once or note the assumption.

2. Create the output folder with the helper script:

```bash
python3 scripts/create_visual_dir.py \
  --request-slug <short_request_slug> \
  --project-slug <project_slug_from_personal_preferences> \
  --base-dir <visuals_root_from_personal_preferences> \
  --hint "<user request or topic>" \
  --cwd "$PWD"
```

3. Build the page in that folder.
   - Use `index.html` when there are multiple pages.
   - For multi-slide decks, prefer starting from [assets/slide-deck-wrapper-template.html](assets/slide-deck-wrapper-template.html) so the landing page, agenda, and embedded slide previews stay consistent.
   - For multi-slide decks, start `index.html` with a numbered agenda that lists each slide title in order and links directly to that slide page.
   - Give the index page a content-forward title that summarizes what the slides cover.
   - Use `page-01-*.html`, `page-02-*.html` for supporting pages when helpful.
   - Keep screenshots and review artifacts in the same request folder.
   - Make slide text editable by default. The user should be able to click into titles, subtitles, cards, and example text and revise them directly in the page.
   - Treat editable content as slide text boxes, not web form controls. Prefer `contenteditable` regions styled like the slide itself instead of visible `<textarea>` or input fields.
   - Include a minimal fullscreen affordance when the page is meant to be presented.
   - If there are multiple slides/pages, standardize fullscreen deck navigation with explicit left/right arrow buttons. Do not use click-anywhere navigation.
   - Keep the controls presentation-like: fullscreen visible in normal mode, previous/next arrows always visible on every slide, and make those arrows small and bottom-centered. When navigation is unavailable, grey the arrow out instead of hiding it.
   - Follow the navigation styling standard from [references/style-guide.md](references/style-guide.md): small circular arrows, bottom center cluster, subtle white surface, light border, disabled grey state, no oversized side-mounted controls.
   - Center the slide content vertically within the viewport so it reads like a slide canvas, not a long webpage with dead space below.

4. Follow the styling guidance in [references/style-guide.md](references/style-guide.md).

5. Validate the rendered page before replying.
   - Follow [references/validation.md](references/validation.md).
   - Do not return the work without a real visual pass.

6. Return clickable absolute paths to the main HTML file and the output directory.

## Output Rules

- Save everything under the visuals root described in [references/personal-customization.md](references/personal-customization.md).
- Keep each request in its own timestamped folder.
- Prefer browser-friendly files over export-only artifacts.
- If you create helper images or screenshots, keep them beside the HTML.
- For decks, make the index page usable as a launch surface, not just a file dump. The agenda should show the slide order clearly.
- The index hero title and subtitle should describe the deck content itself, not the fact that it is HTML, browser-first, or a slide set.

## Common Pitfalls

- Do not leave raw `\n` in visible text. Use real line breaks and `white-space: pre-line` when the content should break across lines.
- Do not ship pages with overflowing cards, clipped headlines, or uneven spacing.
- Do not default to dark mode or purple-heavy styling unless the user asks for it.
- Do not mimic slide decks mechanically; the goal is a clean visual page that is easier to view, edit, and share than PPTX.
- Do not use meta titles like "HTML slides", "browser version", or "slide deck index" in the visible deck heading when a content summary would be clearer.
- Do not add app-like furniture that would never exist on a slide: autosave badges, download bars, floating inspector panels, debug labels, or visible editing toolbars.
- Do not make fullscreen mode feel like a dead-end. When the page is part of a deck, fullscreen should behave like a presentation surface.
- Do not rely on hidden click targets for navigation. Prefer explicit arrows.
- Do not style navigation arrows as large side handles or floating app controls.
- Do not leave the content anchored at the top with a large empty tail below it unless the user wants a document-like layout.

## Resources

- Style system: [references/style-guide.md](references/style-guide.md)
- Validation loop: [references/validation.md](references/validation.md)
- Personal customization: [references/personal-customization.md](references/personal-customization.md)
- Output directory helper: [scripts/create_visual_dir.py](scripts/create_visual_dir.py)
- Starter template: [assets/slide-page-template.html](assets/slide-page-template.html)
- Deck wrapper template: [assets/slide-deck-wrapper-template.html](assets/slide-deck-wrapper-template.html)
- Deck index template: [assets/slide-index-template.html](assets/slide-index-template.html)
