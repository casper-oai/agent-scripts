# HTML Slide Page Style Guide

Use this when replacing a slide with a browser-first HTML page.

If [personal-customization.md](personal-customization.md) includes style notes, treat those as the first tie-breaker for local preferences such as font stack, density, color restraint, or other recurring taste decisions.

## Visual Direction

- Match the clean PPTX-like feel: light background, large title, airy spacing, restrained color.
- Prefer white or very light gray surfaces over saturated backgrounds.
- Use black or near-black primary text and muted gray supporting text.
- Keep the page feeling presentation-ready, not app-like.

Recommended tokens:

```css
:root {
  --bg: #f4f6f8;
  --panel: #ffffff;
  --text: #111827;
  --muted: #667085;
  --line: #d0d5dd;
  --accent: #175cd3;
}
```

## Layout

- Design against a mental 1600x900 canvas even though the page is HTML.
- Good default padding: top `64px`, side `80px`, bottom `48px`.
- Center the main content block vertically within the viewport by default.
- Avoid tall page layouts where the content hugs the top and leaves a large empty area below.
- Use one dominant idea per page.
- Keep to 3-6 content blocks on a page unless the user asks for density.
- Prefer card grids, two-column sections, or simple vertical rhythm over bespoke layouts.

Recommended shell:

```css
body {
  margin: 0;
  min-height: 100vh;
  display: flex;
  align-items: center;
  background: linear-gradient(180deg, #f8fafc 0%, #eef2f6 100%);
  color: var(--text);
  font-family: Arial, Helvetica, sans-serif;
}

.page {
  width: min(1480px, calc(100vw - 48px));
  max-width: 1480px;
  margin: 0 auto;
  padding: 32px 24px 48px;
}

.panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 24px;
  box-shadow: 0 18px 50px rgba(16, 24, 40, 0.06);
}
```

## Typography

- Big headline: `34-56px`.
- Section title: `20-24px`.
- Body: `16-20px`.
- Use short headlines and compact supporting text.
- When text should preserve line breaks, use real newlines plus `white-space: pre-line`.

## Components That Work Well

- Hero panel with title + subtitle.
- Rounded cards with thin gray borders.
- Pill-like labels for metadata.
- Numbered agenda list on the deck landing page, with each slide title linking to its slide file.
- Embedded iframes only when you need a wrapper page that previews multiple child pages.

## Deck Index Pattern

- When a deck has more than one slide, `index.html` should begin with a numbered agenda.
- Prefer starting from the dedicated deck wrapper template when you want agenda plus embedded slide previews.
- The main deck heading should summarize what the slides are about.
- The supporting copy should describe the subject matter covered by the deck, not the delivery format.
- Each agenda item should show the slide title and link directly to the slide HTML.
- A short one-line note under each title helps the user remember what lives on that slide.
- Keep the agenda visually light and presentation-like, not dashboard-like.

Recommended agenda pattern:

```html
<h1>Short summary of the deck</h1>
<p>What the slides cover, in one or two short sentences.</p>
<ol class="agenda">
  <li>
    <a href="./bundle/slide-01-topic.html">Slide 1: Topic</a>
    <span class="agenda-note">What this slide covers.</span>
  </li>
  <li>
    <a href="./bundle/slide-02-example.html">Slide 2: Example</a>
    <span class="agenda-note">Concrete worked example.</span>
  </li>
</ol>
```

For a stronger default wrapper, use `assets/slide-deck-wrapper-template.html`. It includes:

- hero summary block
- numbered agenda navigation
- repeated section preview blocks with `iframe` embeds
- consistent section heading treatment across slides

## Interaction Defaults

- Make visible text blocks editable by default when the page is intended for iteration.
- Style editable regions so they still look like slide text, not application inputs.
- Prefer subtle focus states only when the user clicks into text. No permanent editing chrome.
- Use minimal presentation controls: a fullscreen toggle in normal mode, plus previous/next arrow buttons when fullscreen deck navigation is available.
- Keep navigation arrows small and place them together at the bottom center of the slide.
- Show navigation arrows on every slide, not only in fullscreen.
- Avoid any extra UI that reads like a web app: autosave chips, export buttons, floating toolbars, side panels, or mode banners.

Recommended interaction pattern:

```html
<h1 contenteditable="true">Slide Title</h1>
<p contenteditable="true">Editable supporting copy.</p>
<button class="fullscreen-toggle" aria-label="Enter fullscreen">&#x26F6;</button>
<button class="slide-nav-button slide-nav-button--prev" aria-label="Previous slide">&#x2039;</button>
<button class="slide-nav-button slide-nav-button--next" aria-label="Next slide">&#x203A;</button>
```

```css
[contenteditable="true"] {
  outline: none;
}

[contenteditable="true"]:focus {
  box-shadow: inset 0 0 0 2px rgba(23, 92, 211, 0.18);
  border-radius: 12px;
}

.fullscreen-toggle {
  position: fixed;
  top: 18px;
  right: 18px;
  width: 42px;
  height: 42px;
  border: 1px solid rgba(17, 24, 39, 0.12);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.9);
}

.slide-nav-button {
  position: fixed;
  bottom: 18px;
  width: 40px;
  height: 40px;
  border-radius: 999px;
}

.slide-nav-button--prev {
  left: calc(50% - 44px);
}

.slide-nav-button--next {
  left: calc(50% + 4px);
}
```

## Fullscreen Behavior

- Fullscreen should make the page feel like a deck, not just a bigger browser tab.
- In fullscreen, use explicit previous/next arrow buttons for navigation.
- Keep those arrows small and grouped at the bottom center instead of the slide edges.
- Keep the fullscreen button separate from slide navigation.
- Support keyboard navigation in fullscreen with `ArrowLeft` and `PageUp` for back, `ArrowRight`, `Space`, and `PageDown` for forward.
- On the first or last slide, keep the arrow visible and disabled instead of hiding it.
- Do not hijack keyboard navigation while the user is actively editing text.

## Navigation Styling Standard

- Previous and next arrows should be small circular buttons, roughly `36-40px` square on desktop.
- Place them as a tight pair near the bottom center of the slide with a small gap.
- Use a light surface, thin neutral border, and subtle shadow so they feel like slide chrome rather than app UI.
- Keep them visible in both normal mode and fullscreen.
- Disabled arrows should remain visible and feel inactive through reduced opacity.

## Copy Density

- Compress aggressively for visuals.
- Replace paragraphs with short sentences when possible.
- For example blocks, keep to one concrete example, not a mini-essay.
- Avoid slide-filler labels like "Overview" unless they clarify the page.

## Responsive Behavior

- Pages should still read cleanly on laptop widths.
- Collapse multi-column sections to a single column below roughly `900px`.
- Reduce corner radii and padding on narrow screens.

## Things To Check Before Returning

- No raw `\n` is visible.
- No card content is cut off.
- Headline and subtitle fit naturally.
- Deck index heading summarizes the content instead of talking about format.
- Spacing looks intentional.
- The content block feels vertically centered on the slide.
- The page still looks credible as a presentation artifact.
- Editable regions still look like slide text.
- There is no visible non-slide UI beyond the presentation controls.
