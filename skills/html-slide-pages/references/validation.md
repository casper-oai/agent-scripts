# HTML Slide Page Validation

Do a real visual pass before replying.

## 1. Open The Page

For a direct local preview:

```bash
open "/absolute/path/to/index.html"
```

If you want a local server:

```bash
python3 -m http.server 8000 --directory "/absolute/path/to/output_dir"
```

Then open `http://localhost:8000`.

If the page includes runtime interactions such as editable text or fullscreen navigation, prefer opening it in a real browser instead of relying only on a static thumbnail.

## 2. Capture A Visual Check

Preferred fast path on macOS:

```bash
mkdir -p /private/tmp/html_visual_preview
qlmanage -t -s 1600 -o /private/tmp/html_visual_preview "/absolute/path/to/page.html"
```

That produces a PNG thumbnail you can inspect with `view_image`.

If the page has meaningful runtime behavior and Playwright is available:

```bash
npx -y playwright screenshot \
  "file:///absolute/path/to/page.html" \
  "/absolute/path/to/output_dir/review.png"
```

If Playwright is missing, do not block on it. Use the Quick Look thumbnail path above.

## 3. Inspect The Screenshot

Use `view_image` on the captured PNG and check:

- no overflow or clipped text
- no visible raw `\n`
- balanced spacing
- content sits near the visual middle of the slide, without a large empty tail below
- consistent card heights when they are meant to match
- no accidental dark mode
- no broken asset paths
- no visible app chrome beyond the intended presentation controls

## 4. Check Slide Interactions

For editable slide pages, verify the interaction model before replying:

- click into at least one title or body block and confirm it is directly editable
- enter fullscreen with the page's fullscreen control
- if the page is part of a deck, confirm previous/next arrow buttons are visible on every slide
- confirm the arrows are small and grouped at the bottom center of the slide
- confirm the arrow buttons navigate backward and forward correctly
- confirm unavailable directions are greyed out rather than hidden
- confirm the fullscreen control itself does not accidentally trigger navigation
- on the first or last slide, confirm disabled arrows behave safely
- confirm keyboard navigation still works in fullscreen and does not hijack active text editing

For multi-slide decks with an `index.html`, also verify:

- the index starts with a numbered agenda
- the index heading summarizes the slide contents
- the index copy does not talk about the page being HTML, browser-first, or a slide set unless that is itself the subject
- each agenda item names the corresponding slide clearly
- each agenda link opens the intended slide file
- if the wrapper includes embedded preview sections, the section order and titles match the agenda above

If a personal customization file exists, also verify:

- local path choices and project naming follow the notes in `personal-customization.md`
- visual choices do not contradict any explicit personal style preferences recorded there

## 5. Iterate

If anything looks off, fix the HTML/CSS and re-run the visual check.

Do not return the page until the checked screenshot looks clean.
