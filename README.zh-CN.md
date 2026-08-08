# Prism Glass / 棱镜玻璃

![演示](docs/demo.png)

Prism Glass 是一个面向 Coding Agent 的开源深色玻璃 UI Design Skill。

本版将原先“固定青绿色主题”升级为 **Dark Glass Material + Palette Engine**：玻璃材质、层级、字体、间距、圆角与信息结构保持一致，而页面背景、环境光、玻璃染色、强调色、高光和图表颜色可以整体切换。

## 核心能力

- 深色玻璃视觉设计语言
- 语义化 Design Token
- 16 套内置描述型 Palette（US-00 ~ US-15）
- 整页换色：Canvas / Ambient / Surface / Accent / Highlight / Data Viz
- 5 色自定义 Palette
- 色彩强度、环境光、玻璃染色、强调色占比可调
- `US-11 blue-gold` 蓝金交织复合效果
- 灵活 Dashboard / 内容页布局
- 响应式 UI 规则
- Canonical Demo 与截图验收规范
- 可选 `fluidglass-ui` 实时流体玻璃增强

## 重要设计原则

青绿色只是一个预设，不是 Skill 的固定品牌色。切换 Palette 时，应重新着色整个 UI 氛围，而不是只改按钮颜色。

## 快速开始

1. 将整个目录放入 Agent Skill 目录。
2. 提供现有 HTML、截图、模块清单或页面需求。
3. 让 Agent 读取 `SKILL.md` 与 `references/palette-presets.json`。
4. 可直接指定：`使用 US-11 blue-gold`，或提供 5 个自定义品牌色。
5. 完成后按照 `ACCEPTANCE_CHECKLIST.md` 实际运行并截图验收。

## 作者

**清晨方白晓** · `csuyincs-creator`

中南工科研究生 · 非 AI 从业者，热衷探索 AI 落地实践与 Vibe Coding，持续记录分享好玩的东西。

- 公众号 🔍：清晨方白晓
- 小红书 / 抖音 同号：清晨方白晓

本包采用仓库内 `LICENSE` 与 `NOTICE` 所述许可。作者品牌素材不属于 UI 设计系统的必要运行依赖。
