---
name: accessibility-review
description: Use when building or reviewing any user interface - web, mobile, desktop, or terminal. Covers keyboard operability, semantics and screen reader support, contrast and text sizing, motion, forms and error messaging, and how to actually test rather than assume. Use during implementation and before shipping UI, not as a late audit.
license: MIT
metadata:
  collection: dev-skills
  phase: "6-verification"
---

# Accessibility Review

**Core principle:** accessibility is a functional requirement, not a polish task. An
interface that cannot be operated by keyboard is broken for a large group of people in
exactly the way a 500 error is broken — the difference is only that your monitoring
does not see it.

Retrofitting is far more expensive than building it in, because the fixes are usually
structural: markup, focus management, and information architecture.

## The four principles

Content must be **perceivable** (it can be sensed), **operable** (it can be used),
**understandable** (it can be comprehended), and **robust** (it works with assistive
technology). Most real defects fall under operable and perceivable.

## The high-yield checks

These catch the large majority of serious defects. Do them on every UI change.

### Keyboard

- **Everything interactive is reachable and operable by keyboard alone.** Unplug the
  mouse and complete the main task. This single test finds more real defects than any
  automated tool.
- The **focus indicator is always visible** and has sufficient contrast. Never remove a
  focus outline without replacing it with something at least as clear.
- The tab order follows the visual order and is logical.
- **No keyboard traps** — focus can always move out of a component.
- Focus is **managed on change**: opening a dialog moves focus into it, closing returns
  it to the trigger, and a route change announces and moves focus sensibly.
- A way to **skip repeated navigation** to reach the main content.

### Semantics

- **Use the native element.** A real button, link, checkbox, or heading brings keyboard
  behavior, focus, semantics, and platform conventions for free. A `div` with a click
  handler brings none of it and must reimplement all of it, correctly, forever.
- Headings describe structure and nest without skipping levels.
- **Every input has a programmatically associated label** — placeholder text is not a
  label; it disappears exactly when the user needs it.
- Images have alternative text that conveys *purpose*; decorative images are marked as
  decorative rather than described.
- Landmarks/regions let a screen reader user jump between areas.
- ARIA only where native semantics cannot express it — and **incorrect ARIA is worse
  than none**, because it overrides what was correct.

### Visual

- **Contrast**: at least 4.5:1 for normal text, 3:1 for large text and for the
  meaningful parts of interface components. Check it with a tool; eyes are unreliable.
- **Never use color alone** to convey information — pair it with text, shape, or icon.
- Text reflows and stays usable at 200% zoom, and at a small viewport width.
- Respect the user's reduced-motion preference; avoid anything that flashes rapidly.
- Touch and click targets are comfortably large, with spacing between them.

### Forms and errors

- Errors are identified in text, not by color or position alone
- The message says **how to fix it**, not only that something is wrong
- The error is associated with its field and announced to assistive technology
- Focus moves to the first error on a failed submit
- Nothing depends on a timeout the user cannot extend

### Content

- Page and screen titles are unique and descriptive
- Link text makes sense out of context — a screen of "click here" is unnavigable
- The document language is declared

## How to test

1. **Keyboard only.** The main task, end to end. Non-negotiable.
2. **Automated scan** — an axe-based or platform-equivalent checker. Fast and reliable,
   but it catches roughly a third of issues and **cannot judge whether alt text is
   meaningful or whether focus order makes sense**. A clean automated report is not a
   pass.
3. **Screen reader** — one pass through the main flow with the platform's built-in
   screen reader. Nothing else reveals what your markup actually communicates.
4. **Zoom to 200%** and check a narrow viewport.
5. **Contrast checker** on the real rendered colors, including hover and disabled states.

In CI, run the automated checks on key screens so regressions are caught, while
treating the manual checks as the real bar.

## Red flags

- `onClick` on a `div` or a span styled as a button
- `outline: none` with no replacement
- A custom dropdown, modal, tab set, or tooltip built from scratch — these are the
  components that are hardest to get right; use a well-tested library implementation
- Placeholder used as the only label
- `aria-hidden` on something focusable, or ARIA roles added to fix a visual problem
- "We'll do an accessibility pass before launch" — the fixes will be structural and
  the schedule will not allow them
- Relying only on an automated score and calling it accessible
