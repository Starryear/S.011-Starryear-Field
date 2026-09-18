<div align="center">

# ◫ Starryear-Fourgrid

**把一张照片转译成「摄影证据—诗意提炼—节奏结构—抽象灵魂」相互连通的 2×2 艺术四宫格**

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-000000?style=for-the-badge&logo=openai&logoColor=white)](./SKILL.md)
[![Usage](https://img.shields.io/badge/Usage-Personal%20%26%20Non--commercial-lightgrey?style=for-the-badge)](./LICENSE.md)
[![Language](https://img.shields.io/badge/🌐_中文-English-blue?style=for-the-badge)](#)

</div>

---

## ⚠️ 声明

> **仅限个人学习、非营利研究与非商业创作。**
> 任何商业使用均须事先取得 Starryear年 的书面许可。
>
> 分享作品时，欢迎标注来源并 **@Starryear年**。

---

## 📖 关于本项目

Starryear-Fourgrid 是一个摄影转译 Codex Skill。它把一张原始照片组织为四个连续状态：左上保留真实摄影证据，右上提炼诗意记忆，左下抽取结构节奏，右下释放抽象灵魂，并用一个来自原主体轮廓的中央拼贴铰链把四格连接起来。

- ✅ 左上格使用原照片像素，不把摄影证据重新生成
- ✅ 所有抽象形状、色彩、节奏与轻超现实事件均可追溯到原图
- ❌ 不是四种滤镜、四张重复图、通用水墨山水或无来源的风格迁移

> 📝 The Skill includes complete production prompts in **Chinese** and **English**, with both Markdown and plain-text editions.

---

## 🖼️ 示例作品

> 测试通过后补充。当前 `assets/examples/` 保持为空，不放置参考图、测试图、临时生成图或借用作品。

---

## 📋 目录

- [使用方法](#-使用方法)
- [快速运行策略](#-快速运行策略)
- [可自由调整的部分](#️-可自由调整的部分)
- [核心原则](#-核心原则)
- [内容结构](#-内容结构)
- [许可证](#-许可证)

---

## 🚀 使用方法

### 方式一：作为 Codex Skill 使用

1. 将整个文件夹改名为 `starryear-fourgrid`，复制到 Codex skills 目录，例如 `~/.codex/skills/`。
2. 开启新对话并上传一张你拥有或获准使用的照片。
3. 提出需求：

   > 使用 `starryear-fourgrid` 把这张照片制作成 Starryear 2×2 摄影抽象四宫格。

4. Skill 会保留左上原片，生成其余三个转译状态和中央连接母题，再确定性拼版为一张竖向 2:3 PNG。

### 方式二：直接使用完整提示词

| 语言 | Markdown 版 | TXT 纯文本版 |
| :---: | :--- | :--- |
| 🇨🇳 中文 | [references/starryear-fourgrid-prompt.zh-CN.md](references/starryear-fourgrid-prompt.zh-CN.md) | [prompts/Starryear-Fourgrid-完整提示词-中文.txt](prompts/Starryear-Fourgrid-完整提示词-中文.txt) |
| 🇬🇧 English | [references/starryear-fourgrid-prompt.en.md](references/starryear-fourgrid-prompt.en.md) | [prompts/Starryear-Fourgrid-Full-Prompt-English.txt](prompts/Starryear-Fourgrid-Full-Prompt-English.txt) |

---

## ⚡ 快速运行策略

- 只分析原图一次，并把观察结果锁定后复用于所有生成步骤。
- Panels 2–4 与中央连接素材在工具支持时并行生成。
- 只进行一次最终总检；没有明确缺陷时不重复放大检查。
- 发现问题只重做失败部件一次，不重新生成整组，也绝不重画左上原片。

---

## 🎛️ 可自由调整的部分

| 参数 | 说明 |
| :--- | :--- |
| **源图适配** | 在不破坏关键证据的前提下，选择轻微裁切或使用源图浅色进行补边 |
| **中央母题** | 可微调覆盖面积、方向和跨格位置，但通常保持在总画布的 3%–8% |
| **材质强度** | 可在精确墨线、干印残迹和透明彩墨之间调节，始终保持局部、干净、低幅度 |
| **抽象程度** | 可调整第二至第四格的辨识度递减速度，但四格必须保持同一组视觉 DNA |
| **文字** | 默认无文字；需要标题时后期确定性添加，不让生成器制造乱码 |

---

## 💡 核心原则

1. **摄影证据锁定** — 左上格必须使用真实原图像素，只允许确定性的裁切、缩放或补边。
2. **转译可追溯** — 其余三格的形状、方向、节奏、色彩和超现实变化必须来自原图事实。
3. **四态递进** — 从可见事实逐步走向非写实表达，不做四种滤镜或四张互不相关的画。
4. **中央线索相连** — 中央母题应由主体碎片与特征线构成，像材料转换的铰链，而不是贴纸或第五格。

---

## 📁 内容结构

```text
starryear-fourgrid/
├── README.md
├── LICENSE.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── examples/                    # 测试通过前保持为空
├── prompts/
│   ├── Starryear-Fourgrid-完整提示词-中文.txt
│   └── Starryear-Fourgrid-Full-Prompt-English.txt
├── references/
│   ├── starryear-fourgrid-prompt.zh-CN.md
│   ├── starryear-fourgrid-prompt.en.md
│   ├── source-analysis.md
│   ├── art-direction.md
│   ├── production-prompts.md
│   ├── quality-gate.md
│   └── usage-rights.md
└── scripts/
    └── assemble_fourgrid.py
```

> ⚠️ `assets/examples/` 仅用于收录 Starryear年 明确认可的最终作品。不得复制参考仓库的图片、二维码或他人摄影作品，也不得把示例中的主体、色彩和构图当作新作品模板。

---

## 📄 许可证

本项目采用 [LICENSE.md](./LICENSE.md) 中规定的 Starryear年 原创使用条款。商业产品、收费服务、客户委托、企业用途、付费教学、商业 Agent、转售或再授权均须事先取得书面许可。

---

<div align="center">

**如果这个项目对你有帮助，欢迎 Star ⭐ 支持！**

Authored by **Starryear年**

</div>
