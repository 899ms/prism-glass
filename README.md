<p align="center">
  <img src="./assets/readme/hero.gif" width="100%" alt="Prism Glass — one stable dark-glass dashboard panel crossfading between the US-00 teal, US-11 blue-gold and US-08 deep-blue palettes, while material, typography and layout stay identical.">
</p>

<h1 align="center">Prism Glass / 棱镜玻璃</h1>

<p align="center">
  <img src="https://img.shields.io/badge/palettes-16-10DF9A.svg" alt="16 built-in palettes">
  <img src="https://img.shields.io/badge/palette--engine-v2.0-4B70BE.svg" alt="palette engine v2.0">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License"></a>
</p>

<p align="center"><strong>English</strong> · <a href="README.zh-CN.md">简体中文</a></p>

**An open-source dark-glass UI Design Skill for coding agents.** It separates stable dark-glass material DNA from a configurable Palette Engine. Glass depth, typography, spacing, geometry and hierarchy remain consistent while canvas, ambient light, surface tint, accents, highlights and data visualization can be recolored as one coherent system.

## Canonical demo

![Canonical dark-glass demo](docs/demo.png)

## The principle

> **Dark Glass material is stable; the palette changes the atmosphere.**
> Teal-green is only one preset, not a fixed brand color. Switching a palette must recolor the whole UI — canvas, ambient light, glass tint, accents, highlights, charts — not just buttons.

## Features

- Dark glass design language
- Semantic design tokens
- 16 built-in descriptive palettes (US-00 ~ US-15)
- Whole-UI recoloring instead of accent-only switching
- Five-color custom palettes
- Adjustable palette intensity, ambient strength, surface tint and accent usage
- Optional blue-gold compound effects for US-11
- Flexible dashboard/content layouts
- Responsive rules
- Runnable canonical demo and screenshot-based QA
- Optional `fluidglass-ui` integration

## Built-in palettes

Every preset is exactly five raw colors: **C1 Anchor · C2 Primary · C3 Accent · C4 Soft · C5 Highlight**. Full data: [`references/palette-presets.json`](references/palette-presets.json).

| ID | Name | C1 Anchor | C2 Primary | C3 Accent | C4 Soft | C5 Highlight |
| --- | --- | --- | --- | --- | --- | --- |
| US-00 | teal-green | `#02100D` | `#0B3A30` | `#10DF9A` | `#66CDB1` | `#C8F5E8` |
| US-01 | cool-blue-pink | `#3A6E8E` | `#6E9EAE` | `#B4C8D8` | `#E0C8D4` | `#F2C8D0` |
| US-02 | purple-gold-warm | `#3E2564` | `#7B5E8E` | `#B898A0` | `#D4B896` | `#E5C87B` |
| US-03 | blue-orange-soft | `#1E3E6E` | `#5A6E9E` | `#9E8EAA` | `#D49E8A` | `#F0B878` |
| US-04 | peach-warm-light | `#E8A890` | `#EDC8B8` | `#F2D8C8` | `#F5E8D0` | `#F9F0E0` |
| US-05 | cyan-purple | `#1A3A3A` | `#2E6E6E` | `#5A8E9E` | `#8E6E9E` | `#B888C4` |
| US-06 | mint-light | `#5A9E8E` | `#8EC8B8` | `#B8E0D4` | `#D8F0E8` | `#F2F8F0` |
| US-07 | cyan-gray-neutral | `#5A6E6E` | `#8A9E9E` | `#B4C4C4` | `#D4DCD8` | `#EEF0EE` |
| US-08 | deep-blue-purple | `#0E1A3E` | `#2E3E6E` | `#5E4E8E` | `#9E7BBE` | `#D0A8E0` |
| US-09 | dark-neutral | `#080A0D` | `#11151A` | `#20262D` | `#424B55` | `#AEB6BF` |
| US-10 | light-neutral | `#202327` | `#666D75` | `#BCC2C8` | `#ECEFF1` | `#FAFBFC` |
| US-11 | blue-gold | `#0A1335` | `#163B7A` | `#4B70BE` | `#C89A55` | `#F2D79E` |
| US-12 | lake-blue | `#1E3E4A` | `#3A6E7E` | `#6EA0AE` | `#A8D0D8` | `#E2EEF0` |
| US-13 | ice-blue | `#2A3E4E` | `#4A6E8E` | `#8EAEC8` | `#C8DCE8` | `#EEF4F8` |
| US-14 | rock-green | `#2A2A2E` | `#4A4A4E` | `#7A7A78` | `#A8B0A0` | `#D8E0D0` |
| US-15 | forest-green | `#1E2E22` | `#2E4536` | `#4A6B52` | `#8AA890` | `#D8E8DC` |

## Quick start

1. Put the directory in your Agent Skill directory.
2. Ask the Agent to read `SKILL.md` and `references/palette-presets.json`.
3. Specify a preset such as `US-11 blue-gold`, or provide five custom brand colors.
4. Validate the result with `ACCEPTANCE_CHECKLIST.md`.

## Author

**清晨方白晓** · `csuyincs-creator` · 中南工科研究生，热衷探索 AI 落地实践与 Vibe Coding，持续记录分享好玩的东西。

- 公众号 🔍：清晨方白晓
- 小红书 / 抖音 同号：清晨方白晓

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE) for licensing details.
