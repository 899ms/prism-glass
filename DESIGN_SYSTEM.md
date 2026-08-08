# Dark Glass Design System + Palette Engine

## 1. System definition

This design system separates **material** from **color atmosphere**.

Stable material DNA: dark canvas, layered translucent glass, subtle borders, soft inner light, diffused shadows, restrained typography, consistent geometry, spacing and hierarchy.

Variable palette layer: canvas tint, ambient light, glass tint, accent, highlight, data visualization, hover/focus states and optional effects.

The default teal-green appearance is only one preset.

## 2. Palette architecture

### Raw palette
Every preset contains exactly five raw colors: C1 Anchor, C2 Primary, C3 Secondary, C4 Soft, C5 Highlight.

### Semantic mapping
Components must consume semantic tokens from `references/dark-glass-tokens.css`. Runtime derivation is implemented in `references/palette-engine.js`.

### Optional effects
Effects are palette-scoped and optional. They may decorate surfaces but must not carry essential information.

## 3. Material stack

1. deep canvas base;
2. restrained ambient radial light;
3. translucent surface base;
4. subtle 1px border;
5. top-edge highlight;
6. soft inset illumination;
7. deep diffused shadow;
8. optional backdrop blur.

Avoid opaque gray cards, hard white borders, excessive bloom and plastic gloss.

## 4. Color balance

Neutral / canvas / surfaces should occupy roughly 70%–90% of the visual area. Palette accents/highlights generally occupy 10%–30%.

Palette switching must recolor the whole UI atmosphere, not only buttons.

## 5. Geometry

- Large panel radius: 22–26px
- Metric / feature card radius: 28–32px
- Controls: 10–16px
- Primary gap: 12–18px
- Keep internal padding consistent and readable.

## 6. Typography

Use system sans fonts for reliable Chinese and Latin rendering.

- 12px metadata
- 13–14px body/table
- 16–18px section title
- 22–26px page title

## 7. Layout

The canonical three-region composition is only a reference. The same material and palette system can be used for one-column, two-column, card-grid, analytics and inspector layouts.

## 8. Blue-gold compound effects

For `US-11 blue-gold`, blue remains the main material. Gold appears as restrained edge light, stroke, sparkle, gradient endpoint or localized glow. Do not replace the interface with a gold background.

## 9. Custom palettes

Custom palettes must contain exactly five colors. First derive semantic tokens; do not inject custom Hex values throughout component CSS.

## 10. Responsive adaptation

Responsive layout may change structure, but it must retain the same material depth, palette semantics and typography hierarchy.
