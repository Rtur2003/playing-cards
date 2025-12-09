# Playing Cards Page

A small RTL-friendly page that shows five sample playing cards with correct suits, semantic structure, and responsive styling.

## Features
- Semantic list-based deck with accessible `aria-label` on each card
- Suit symbols rendered via HTML entities (`&spades;`, `&hearts;`, `&clubs;`, `&diams;`) and colored by `data-suit`
- Responsive grid layout with design tokens for sizing, radius, and shadows
- Focus-visible outlines for keyboard users plus hover lift for clarity
- Persian heading and subtitle with Vazirmatn webfont

## Structure
- `index.html` - cards and layout markup
- `style.css` - design tokens, grid, card styling, and accessibility states
- `README.md` - project overview and usage

## Usage
Open `index.html` in a browser. All assets are local except the Google Font reference included in the `<head>`.

## Notes
- Colors for hearts/diamonds are red; spades/clubs are dark ink
- Card size scales with the viewport via CSS `clamp()` to remain legible on mobile
