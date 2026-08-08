# Visual Regression Specification

## Browser
Use Playwright Chromium with:

```js
chromium.launch({
  executablePath: "/usr/lib/chromium/chromium",
  headless: true
});
```

## Required review
1. Load `canonical-demo-single-file.html`.
2. Capture default `US-00` at 1536×864.
3. Open Palette panel and switch to `US-11 blue-gold`; capture.
4. Switch to `US-15 forest-green`; confirm the canvas/surfaces/ambient colors change together.
5. Capture 1366×768.
6. Fail on console/page errors.
7. Do not claim visual consistency from source inspection alone.
