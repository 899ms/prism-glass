---
name: dark-glass-dashboard-ui
description: Prism Glass — Builds production-grade dark glass web interfaces with a palette-driven color engine. Preserves glass material, spacing, typography, hierarchy, geometry, responsiveness, and component language while allowing the entire UI atmosphere—canvas, ambient glow, glass tint, accents, highlights, and data visualization—to switch between built-in or custom palettes. Use for dashboards, admin panels, data interfaces, knowledge interfaces, control panels, and existing HTML that needs a cohesive premium dark-glass visual system without being locked to one fixed color.
---

# Skill: Prism Glass / 棱镜玻璃

> 深色玻璃 UI 设计系统 · 可整体切换的调色引擎

## 1. Purpose

将现有网页、后台、数据面板、知识界面或模块清单转换为统一、克制、高级的深色玻璃 UI，并通过 **Palette Engine** 控制整个页面的色彩氛围。

核心定义：

> **固定 Dark Glass 视觉 DNA + 可切换 Palette System。**

青绿色只是内置预设之一，不属于不可改变的视觉 DNA。

## 2. Required References

执行前优先读取：

- `references/canonical-reference.png`
- `references/canonical-demo-single-file.html`
- `references/dark-glass-tokens.css`
- `references/component-recipes.css`
- `references/palette-presets.json`
- `references/palette-engine.js`
- `DESIGN_SYSTEM.md`
- `CONFIG_SCHEMA.json`
- `ACCEPTANCE_CHECKLIST.md`

Canonical Demo 是视觉语言参考，不是业务模板。不得复制 Demo 业务文案。

## 3. Stable Visual DNA

无论 Palette 如何变化，都必须保持：

1. 深色或低亮度画布作为空间底座；
2. 多层半透明玻璃表面；
3. 低对比度 1px 边框；
4. 轻微顶部高光与柔和内层光；
5. 深而扩散的阴影；
6. 克制的系统字体层级；
7. 高信息密度但不牺牲可读性；
8. 统一圆角、间距、透明度与层级；
9. 装饰图标最小化；
10. Palette 只能改变色彩氛围，不能破坏几何、材质和信息层级。

## 4. Palette Engine

### Layer A — Raw Palette

每套 Palette 固定 5 色：

- `C1` Anchor：深色锚点
- `C2` Primary：核心主色
- `C3` Secondary：辅助色
- `C4` Soft：柔和环境色
- `C5` Highlight：高光浅色

### Layer B — Semantic Tokens

Raw Palette 必须映射到：

- `--canvas-base`
- `--canvas-secondary`
- `--surface-base-rgb`
- `--surface-strong-rgb`
- `--surface-soft-rgb`
- `--accent-primary`
- `--accent-secondary`
- `--highlight`
- `--ambient-primary-rgb`
- `--ambient-secondary-rgb`
- text / border / state tokens

组件只消费 Semantic Token。禁止组件散落硬编码主题 Hex。

### Layer C — Optional Effects

允许 Palette 声明可选效果，例如：

- `edge-glow`
- `mixed-gradient`
- `sparkle`
- `ribbon`
- `hybrid`

效果不能成为可读性的前提。

## 5. Built-in Presets

内置 `US-00 ~ US-15` 共 16 套通用描述型色系。完整色值见 `references/palette-presets.json`。

- US-00 `teal-green`
- US-01 `cool-blue-pink`
- US-02 `purple-gold-warm`
- US-03 `blue-orange-soft`
- US-04 `peach-warm-light`
- US-05 `cyan-purple`
- US-06 `mint-light`
- US-07 `cyan-gray-neutral`
- US-08 `deep-blue-purple`
- US-09 `dark-neutral`
- US-10 `light-neutral`
- US-11 `blue-gold`
- US-12 `lake-blue`
- US-13 `ice-blue`
- US-14 `rock-green`
- US-15 `forest-green`

公开命名使用描述性名称，不依赖外部来源命名。

## 6. Whole-UI Recolor Rule

切换 Palette 时必须同步改变：

- Canvas 页面背景
- Ambient 环境光
- Glass Surface Tint 玻璃染色
- Accent 交互强调
- Highlight 高光
- Data Visualization 图表与数据视觉
- Hover / Active / Focus
- Palette 明确声明时的 Effect

错误：保留青绿色 Canvas，只把按钮改成紫色。

正确：紫色 Palette 同时重新着色 Canvas、Ambient、Surface、Accent、Highlight 和 Data Viz。

## 7. Color Balance

默认页面仍应由 Neutral / Surface 承担主要视觉面积：

- Neutral / Canvas / Surface：70%~90%
- Theme / Accent / Highlight：10%~30%

禁止把 5 个 Palette 色平均分给 5 张卡片。

## 8. Palette Controls

实现设置面板时，优先暴露：

- `preset`
- `intensity`
- `ambientStrength`
- `surfaceTint`
- `accentUsage`
- `effects`
- `customColors`（正好 5 色）

预设按钮应使用 5 色迷你色带，而不是只显示单个颜色点。

## 9. Blue-Gold Special Rule

`US-11 blue-gold` 允许蓝金复合效果。

原则：

> 蓝是主体，金是高光；蓝是材质，金是流动。

一般 UI 金色建议占 5%~15%；Hero / 强视觉可到 15%~25%。推荐：金色描边、碎金颗粒、局部高光、渐变端点、少量流光。禁止整页铺金或把蓝金搅成脏灰色。

## 10. Custom Palette

用户可提供任意 5 个品牌色。Agent 必须先映射为 Raw Palette，再由 Palette Engine 派生 Semantic Token，不应让自定义色直接污染组件代码。

## 11. Layout

Canonical Reference 使用 `Left Navigation / Primary Workspace / Context Panel` 三域构图，仅作为 Dashboard 参考，不是强制结构。

可选择：单栏、双栏、三域、Card Grid、Analytics、Detail / Inspector。布局可变，材质和 Token 不变。

## 12. Optional Fluid Glass Integration

若需要实时流体玻璃卡片，可选接入独立 `fluidglass-ui` Skill。仍由本 Skill 控制布局、字体、间距、圆角、Palette Token 与信息层级。

## 13. Agent Workflow

1. 读取用户现有页面 / HTML / 截图 / 模块清单。
2. 读取 Canonical Reference、Design System、Palette Presets、Tokens 和 Recipes。
3. 确定信息架构与布局。
4. 选择最匹配的 Palette；用户未指定时使用 `US-00` 或根据内容选择低饱和预设。
5. 先应用 Raw → Semantic Token 映射，再构建组件。
6. 保留用户真实内容，不复制 Demo 文案。
7. 页面整体重新着色，而不是只换 Accent。
8. 检查桌面、窄屏与交互状态。
9. 实际启动浏览器并截图复核。

## 14. Hard Prohibitions

- 不得把青绿色写死为视觉 DNA。
- 不得为每张卡片随机分配一个 Palette 色。
- 不得在组件内部重复硬编码主题 Hex。
- 不得无理由加入荧光蓝、荧光紫或彩虹渐变。
- 不得用高饱和纯色大面积覆盖玻璃材质。
- 不得声称截图验收通过，除非实际运行并生成截图。

## 15. Output

按任务需要输出：

- 可运行 HTML / 项目源码
- Palette 配置
- Design Token
- Component Recipe
- 响应式规则
- 截图与视觉验收结果
