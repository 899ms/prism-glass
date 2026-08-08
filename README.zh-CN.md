# Prism Glass / 棱镜玻璃

![演示](docs/demo.png)

Prism Glass 是一个面向 Coding Agent 的开源深色玻璃 UI Design Skill。

本版将原先「固定青绿色主题」升级为 **Dark Glass Material + Palette Engine**：玻璃材质、层级、字体、间距、圆角与信息结构保持一致，而页面背景、环境光、玻璃染色、强调色、高光和图表颜色可以整体切换——一次换色，整页氛围随之流动。

> 🇺🇸 English documentation: [README.md](README.md)

## 核心能力

- 深色玻璃（Dark Glass）视觉设计语言，质感统一、层级清晰
- 语义化 Design Token，便于二次开发与主题扩展
- 16 套内置描述型 Palette（US-00 ~ US-15）
- 整页换色：Canvas / Ambient / Surface / Accent / Highlight / Data Viz 作为一套系统联动
- 5 色自定义 Palette，适配品牌色
- 色彩强度、环境光、玻璃染色、强调色占比均可微调
- `US-11 blue-gold` 蓝金交织复合效果
- 灵活的 Dashboard / 内容页布局
- 响应式 UI 规则
- Canonical Demo 与截图验收规范，可量化核对
- 可选 `fluidglass-ui` 实时流体玻璃增强

## 重要设计原则

青绿色（teal-green）只是 16 个预设里的其中一个，**不是 Skill 的固定品牌色**。切换 Palette 时，应当重新着色整个 UI 氛围（背景、环境光、玻璃染色、强调色、高光、图表），而不是只改按钮颜色。

调色引擎的核心理念：**稳定的玻璃材质 DNA + 可整体替换的调色板**。材质不变，色彩随 Palette 流动。

## 安装 / 部署

将整个目录作为 Agent Skill 放入 Skill 目录即可，无需构建步骤：

```bash
# WorkBuddy 用户级技能目录（推荐）
cp -r prism-glass ~/.workbuddy/skills/dark-glass-dashboard-ui

# 或项目级技能目录
cp -r prism-glass <你的项目>/.workbuddy/skills/dark-glass-dashboard-ui
```

- 内部 `name` 为 `dark-glass-dashboard-ui`，与历史版本一致，可平滑覆盖旧版。
- 让 Agent 读取入口文件 `SKILL.md` 以及 `references/palette-presets.json` 即可开始工作。

## 快速开始

1. 将整个目录放入 Agent Skill 目录（见上）。
2. 向 Agent 提供现有 HTML、页面截图、模块清单或新的页面需求。
3. 让 Agent 读取 `SKILL.md` 与 `references/palette-presets.json`。
4. 直接指定预设，例如：`使用 US-11 blue-gold`，或提供 5 个自定义品牌色。
5. 完成后，按 `ACCEPTANCE_CHECKLIST.md` 实际运行并截图验收。

## 调色引擎与 Palette 清单

内置 16 套描述型 Palette，默认预设为 `US-00`；另有 5 色自定义模式（C1 锚点 / C2 主色 / C3 辅助 / C4 柔和 / C5 高光）。

| ID | 英文名 | 中文名 | 备注 |
|----|--------|--------|------|
| US-00 | teal-green | 青绿深色系 | 原始预设，保留作可选风格 |
| US-01 | cool-blue-pink | 冷蓝粉系 | 冷静、编辑感 |
| US-02 | purple-gold-warm | 紫金暖调系 | 高级深色界面 |
| US-03 | blue-orange-soft | 蓝橙柔和系 | |
| US-04 | peach-warm-light | 杏粉浅暖系 | |
| US-05 | cyan-purple | 青紫渐变系 | |
| US-06 | mint-light | 薄荷浅绿系 | |
| US-07 | cyan-gray-neutral | 青灰中性系 | |
| US-08 | deep-blue-purple | 深蓝紫系 | |
| US-09 | dark-neutral | 深色中性系 | |
| US-10 | light-neutral | 浅色中性系 | |
| US-11 | blue-gold | 蓝金交织系 | 复合蓝金效果（blue-gold-hybrid） |
| US-12 | lake-blue | 湖蓝晨光系 | |
| US-13 | ice-blue | 冰川浅蓝系 | |
| US-14 | rock-green | 岩灰苔绿系 | |
| US-15 | forest-green | 森林雾绿系 | |

可调参数（默认值见 `references/palette-presets.json`）：

- `intensity` 色彩强度：0.55
- `ambientStrength` 环境光强度：0.42
- `surfaceTint` 玻璃染色：0.28
- `accentUsage` 强调色占比：0.34
- `effects` 复合效果开关：开启

## 目录结构与资源说明

```
prism-glass/
├── SKILL.md                    # 技能入口与编排指引
├── manifest.json               # 技能元信息（displayName / tagline / 版本）
├── README.md                   # 英文文档
├── README.zh-CN.md             # 本文件（中文文档）
├── LICENSE / NOTICE            # 许可与署名声明
├── DESIGN_SYSTEM.md            # 设计系统总览
├── COMPONENT_API.md            # 组件 API
├── CONFIG_SCHEMA.json          # 配置 schema
├── REFERENCE_CONFIG.json       # 参考配置
├── CANONICAL_CORE_HASHES.json  # 验收核心哈希
├── ACCEPTANCE_CHECKLIST.md     # 验收清单
├── CHANGELOG.md                # 变更日志
├── MASTER_PROMPT.md            # 主提示词
├── QUICK_START_PROMPT.md       # 快速开始提示词
├── INTEGRATION_GUIDE.md        # 集成指南
├── docs/
│   ├── demo.png                # 演示图
│   └── brand/                  # 作者授权品牌素材占位
├── references/
│   ├── canonical-demo-single-file.html  # 单文件典范 demo
│   ├── canonical-reference.png
│   ├── dark-glass-tokens.css   # 玻璃材质 token
│   ├── component-recipes.css   # 组件配方
│   ├── palette-engine.js       # 调色引擎实现
│   ├── palette-presets.json    # 16 套 palette 定义
│   └── visual-regression-spec.md
├── screenshots/                # 截图与验收报告
├── tools/
│   └── package_qa.py           # 打包质量检查
└── .github/workflows/qa.yml    # CI 验收
```

## 相关文档

- 设计系统：`DESIGN_SYSTEM.md`
- 组件 API：`COMPONENT_API.md`
- 集成指南：`INTEGRATION_GUIDE.md`
- 验收清单：`ACCEPTANCE_CHECKLIST.md`
- 配置 schema：`CONFIG_SCHEMA.json`
- 调色板定义：`references/palette-presets.json`
- 典范 Demo（单文件）：`references/canonical-demo-single-file.html`

## 许可证

本包采用仓库内 `LICENSE`（Apache-2.0）与 `NOTICE` 所述许可。作者品牌素材（docs/brand）不属于 UI 设计系统的必要运行依赖。

## 作者

**清晨方白晓** · `csuyincs-creator`

中南工科研究生 · 非 AI 从业者，热衷探索 AI 落地实践与 Vibe Coding，持续记录分享好玩的东西。

- 公众号 🔍：清晨方白晓
- 小红书 / 抖音 同号：清晨方白晓

如需在项目里引用本 Skill，欢迎注明「Prism Glass / 棱镜玻璃 · by 清晨方白晓」。
