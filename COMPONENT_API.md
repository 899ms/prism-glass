# Component API

## Palette API

The canonical demo exposes:

```js
DarkGlassDashboardUI.setPalette('US-11')
DarkGlassDashboardUI.getPalette()
DarkGlassDashboardUI.setPaletteOptions({
  intensity: 0.60,
  ambientStrength: 0.45,
  surfaceTint: 0.30,
  accentUsage: 0.35,
  effects: true
})
DarkGlassDashboardUI.setCustomPalette([
  '#0A1335','#163B7A','#4B70BE','#C89A55','#F2D79E'
])
DarkGlassDashboardUI.openSettings()
DarkGlassDashboardUI.closeSettings()
```

## Canonical classes

- `.glass` — translucent panel material
- `.metric` — metric / statistic card
- `.sidebar` — optional navigation region
- `.main` — primary content region
- `.right` — optional context region
- `.palette-panel` — non-modal palette settings surface

New pages may use different semantic class names if they consume the same semantic tokens and recipes.

## Token rule

Components should reference semantic tokens (`--canvas-*`, `--surface-*`, `--accent-*`, `--highlight`, text/border tokens). Do not bind components to preset IDs or raw C1–C5 colors.

## Optional fluid glass

`fluidglass-ui` may provide a real-time card rendering layer while this system continues to control palette, geometry, typography, spacing and hierarchy.
