# UI Integration Guide

## Existing page restyle

1. Read the existing information hierarchy.
2. Import/map `dark-glass-tokens.css`.
3. Load `palette-presets.json` and `palette-engine.js` or reproduce the same semantic mapping in the target framework.
4. Replace repeated hard-coded theme colors with semantic tokens.
5. Map existing regions to glass surfaces.
6. Apply the selected palette to canvas, ambient, surfaces, accents, highlights and charts.
7. Preserve real content and semantic structure.
8. Check responsive behavior and visual QA.

## New page design

1. Start from information architecture.
2. Choose a suitable layout.
3. Establish material tokens and palette mapping before styling modules.
4. Build major surfaces, then cards/controls/data visualization.
5. Validate hierarchy and density.
6. Test at 1536×864, 1366×768, and at least one narrower breakpoint.

## Custom palette

Accept exactly five colors. Map them to C1–C5, derive semantic tokens, then apply. Do not scatter custom Hex values inside component CSS.

## Optional fluid glass

If real-time fluid glass is required, integrate `fluidglass-ui` while preserving the same semantic palette tokens, spacing, radius, typography and hierarchy.
