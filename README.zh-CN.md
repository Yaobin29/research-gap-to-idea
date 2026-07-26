# Research Gap to Idea

![Research Gap to Idea 科学文献综合封面](assets/research-gap-to-idea-cover.png)

[English README](README.md)

`research-gap-to-idea` 是一个可移植的科学文献综合 Skill，用于把一组围绕同一问题的相关论文转化为：共同底层问题、因果证据边界、Technical / Knowledge / Assumption Gaps，以及可以被实验否证的研究方向。

它不以逐篇摘要或逐图翻译为目标，而是先从目标结果和必要状态出发重建因果链，再将论文嵌入统一的 Paper Analysis Card，最后从尚未闭合的因果环节推导非拼接式 Idea。

## 主要产出

- 共同研究问题的第一性原理定义
- 分层策展的核心文献与背景/反查文献集
- 每篇论文一个完整分析卡，包含期刊信息和增强版 `WHY / HOW / WHAT`
- 带来源的因果证据账本，并标记 `[D]`、`[C]`、`[L]`、`[U]`
- 从目标结果推导 Evidence Matrix 维度与失效边界
- Technical、Knowledge、Assumption 三类 Gap
- 跨论文的收敛、互补、冲突与异常分析
- Incremental、Integrative、Transformative 三类研究 Idea
- 最小判别实验、预测、证伪条件和 Go/No-Go 标准
- 从同一 Markdown 源文件生成 Markdown 与可离线打开的单文件 HTML 报告

## 从 GitHub 安装

如果 Agent 支持开放的 `skills` CLI，可以直接把下面的命令发给 Agent，或在终端运行：

```bash
npx skills add Yaobin29/research-gap-to-idea --skill research-gap-to-idea -g -a codex -y
```

该命令会将 Skill 全局安装到 Codex。使用其他受支持的 Agent 时，将 `-a` 后面的 `codex` 换成对应名称，或者省略 `-a codex` 让 CLI 自动选择可用的 Agent 集成。该 CLI 可以直接通过 `npx` 运行，不需要额外全局安装 npm 包。

安装完成后，重新启动一个 Agent 会话并调用 `$research-gap-to-idea`。如果你的 Agent 不支持 `skills` CLI，可以克隆本仓库，然后直接将 [`SKILL.md`](SKILL.md) 提供给 Agent。

## 使用方式

将 Agent 指向 `SKILL.md`，或显式调用：

```text
Use $research-gap-to-idea to synthesize these related papers into a shared problem, evidence matrix, three gap classes, and falsifiable research ideas.
```

默认输出语言为中文，除非用户指定其他语言。论文标题、技术术语、期刊名称、标识符和引用信息在需要保证精确时保留原文。

当用户要求生成报告文件时，将 Markdown 渲染为单文件、可离线打开的 HTML：

```bash
python scripts/render_report.py report.md report.html
```

渲染器只使用 Python 标准库，不加载外部资源或 CDN。默认排版采用科学编辑 / research field-notes 风格，并支持响应式显示和打印。

## 示例 Reference

[`references/anti-adhesion-hydrogel-example.md`](references/anti-adhesion-hydrogel-example.md) 是关于术后腹腔/腹膜粘连预防的中文完整示例；同时提供 [英文 worked reference](references/anti-adhesion-hydrogel-example.en.md)。

这两个 reference 展示了文献策展、期刊元数据、因果证据追踪、第一性原理比较维度、Gap 分析和非拼接式 Idea Card。它们是结构与推理示例，不应替代新项目中的重新检索和来源核验。

## 推荐输入

建议提供 3–8 篇围绕同一问题的核心论文，并尽量提供 PDF、摘要、DOI/PMID/arXiv 标识符或稳定链接。如果可以进行文献发现，Skill 应主动加入独立的背景/反查文献集，包括综述、临床基准、更强的比较研究或相反结论的研究。

如果只有一两篇论文，Skill 应将跨论文结论标记为 provisional，不应把它们表述为领域共识。文献发现可以与独立的论文检索 Skill（如 [`paper-3w-research`](https://github.com/Yaobin29/Robin-paper-3w-research)）配合使用。

## 设计原则

> 分析单位是研究问题，而不是单篇论文。

除非论文直接检验了相关因果环节，否则将作者的解释视为假设。每个入选 Idea 都必须明确什么结果会使它被证伪。

## 仓库结构

```text
.
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── scripts/
│   └── render_report.py
├── references/
│   ├── anti-adhesion-hydrogel-example.md
│   ├── anti-adhesion-hydrogel-example.en.md
│   ├── causal-model.md
│   ├── evidence-rubric.md
│   ├── gap-taxonomy.md
│   ├── idea-operators.md
│   ├── literature-curation.md
│   ├── output-template.md
│   └── quality-gates.md
└── assets/
    ├── research-gap-to-idea-cover.png
    ├── report-template.html
    └── idea-card-template.md
```

## 许可证

MIT License，详见 [LICENSE](LICENSE)。
