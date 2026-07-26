# Research Gap to Idea

![Research Gap to Idea scientific synthesis cover](assets/research-gap-to-idea-cover.png)

`research-gap-to-idea` is a portable agent skill for turning a small set of related scientific papers into a shared problem map, an evidence boundary, and falsifiable research directions.

It is designed for researchers who want more than paper summaries or figure translation. The workflow compares papers around a shared question, reconstructs the causal chain from first principles, identifies technical, knowledge, and assumption gaps, and converts those gaps into testable Idea Cards.

## 中文简介

`research-gap-to-idea` 是一个可移植的科学文献综合 Skill，用于把一组围绕同一问题的相关论文转化为：共同底层问题、因果证据边界、Technical / Knowledge / Assumption Gaps，以及可以被实验否证的研究方向。

它不以逐篇摘要或逐图翻译为目标，而是先从目标结果和必要状态出发重建因果链，再将论文嵌入统一的 Paper Analysis Card，最后从尚未闭合的因果环节推导非拼接式 Idea。

## What it produces / 主要产出

- A first-principles definition of the shared research problem / 共同研究问题的第一性原理定义
- A curated and quality-graded core/context literature set / 分层策展的核心文献与背景/反查文献集
- One integrated Paper Analysis Card per paper, including journal metadata and enhanced `WHY / HOW / WHAT` / 每篇论文一个完整分析卡，包含期刊信息和增强版 `WHY / HOW / WHAT`
- A cited causal evidence ledger with `[D]`, `[C]`, `[L]`, and `[U]` boundaries / 带来源的因果证据账本，并标记 `[D]`、`[C]`、`[L]`、`[U]`
- First-principles derivation of Evidence Matrix dimensions and failure boundaries / 从目标结果推导 Evidence Matrix 维度与失效边界
- Technical, knowledge, and assumption gap analysis / Technical、Knowledge、Assumption 三类 Gap
- Cross-paper convergence, complementarity, contradiction, and anomaly analysis / 跨论文的收敛、互补、冲突与异常分析
- Incremental, integrative, and transformative research ideas / Incremental、Integrative、Transformative 三类 Idea
- Minimal discriminating experiments, predictions, falsification conditions, and Go/No-Go criteria / 最小判别实验、预测、证伪条件和 Go/No-Go 标准
- Markdown and standalone offline HTML reports rendered from the same source / 从同一 Markdown 源文件生成 Markdown 与可离线打开的单文件 HTML 报告

## Repository layout / 仓库结构

```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── scripts/
│   └── render_report.py
├── references/
│   ├── anti-adhesion-hydrogel-example.md       # 中文 worked reference
│   ├── anti-adhesion-hydrogel-example.en.md    # English worked reference
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

## Use with an agent / 使用方式

Point your agent at `SKILL.md`, or invoke it explicitly:

```text
Use $research-gap-to-idea to synthesize these related papers into a shared problem, evidence matrix, three gap classes, and falsifiable research ideas.
```

将 Agent 指向 `SKILL.md`，或显式调用：

```text
Use $research-gap-to-idea to synthesize these related papers into a shared problem, evidence matrix, three gap classes, and falsifiable research ideas.
```

## Install from GitHub / 从 GitHub 安装

For agents that support the open `skills` CLI, send your agent this command (or run it in a terminal):

```bash
npx skills add Yaobin29/research-gap-to-idea --skill research-gap-to-idea -g -a codex -y
```

This installs the skill globally for Codex. For another supported agent, replace `codex` after `-a`, or omit `-a codex` to let the CLI choose the available agent integrations. The CLI can be run directly through `npx`; no separate global npm installation is required.

支持 `skills` CLI 的 Agent 可以直接使用下面的命令安装（也可以把这段命令发给 Agent）：

```bash
npx skills add Yaobin29/research-gap-to-idea --skill research-gap-to-idea -g -a codex -y
```

这会将 Skill 全局安装到 Codex。使用其他受支持的 Agent 时，将 `-a` 后面的 `codex` 换成对应名称，或者省略 `-a codex` 让 CLI 自动选择可用的 Agent 集成。该 CLI 可以直接通过 `npx` 运行，不需要额外全局安装 npm 包。

After installation, start a new agent session and invoke `$research-gap-to-idea`. If your agent does not support the `skills` CLI, clone this repository and point the agent to [`SKILL.md`](SKILL.md) directly.

安装完成后，重新启动一个 Agent 会话并调用 `$research-gap-to-idea`。如果你的 Agent 不支持 `skills` CLI，可以克隆本仓库，然后直接将 [`SKILL.md`](SKILL.md) 提供给 Agent。

The default response language is Chinese unless the user requests another language. Keep paper titles, technical terms, journal names, identifiers, and citations in their original form when precision matters.

默认输出语言为中文，除非用户指定其他语言。论文标题、技术术语、期刊名称、标识符和引用信息在需要保证精确时保留原文。

When a report file is requested, render the Markdown report as a single offline HTML file:

```bash
python scripts/render_report.py report.md report.html
```

当用户要求生成报告文件时，将 Markdown 渲染为单文件、可离线打开的 HTML：

```bash
python scripts/render_report.py report.md report.html
```

The renderer uses only the Python standard library and does not load external assets or CDN resources. Its default visual direction is a scientific editorial / research field-notes layout with responsive and print-friendly styling.

渲染器只使用 Python 标准库，不加载外部资源或 CDN。默认排版采用科学编辑 / research field-notes 风格，并支持响应式显示和打印。

## Worked references / 示例 Reference

The anti-adhesion hydrogel references are complete worked examples for postoperative abdominal/peritoneal adhesion prevention. They demonstrate literature curation, journal metadata, causal evidence tracing, first-principles comparison dimensions, gap analysis, and non-combinatorial Idea Cards. They are structural examples, not substitutes for re-verifying sources in a new project.

防粘连水凝胶 reference 是关于术后腹腔/腹膜粘连预防的完整示例，展示文献策展、期刊元数据、因果证据追踪、第一性原理比较维度、Gap 分析和非拼接式 Idea Card。它们是结构与推理示例，不应替代新项目中的重新检索和来源核验。

- [中文 reference：防粘连水凝胶](references/anti-adhesion-hydrogel-example.md)
- [English reference: Anti-Adhesion Hydrogels](references/anti-adhesion-hydrogel-example.en.md)

## Recommended input / 推荐输入

Provide 3–8 core papers that address one shared problem. Include PDFs, abstracts, DOI/PMID/arXiv identifiers, or stable URLs when available. The skill should add a separate context/adversarial set of reviews, clinical benchmarks, stronger comparison studies, or conflicting sources when literature discovery is possible.

建议提供 3–8 篇围绕同一问题的核心论文，并尽量提供 PDF、摘要、DOI/PMID/arXiv 标识符或稳定链接。如果可以进行文献发现，Skill 应主动加入独立的背景/反查文献集，包括综述、临床基准、更强的比较研究或相反结论的研究。

If only one or two papers are available, the skill should label cross-paper conclusions as provisional rather than presenting them as a field-level synthesis. Literature discovery can be paired with a separate paper-search skill such as [`paper-3w-research`](https://github.com/Yaobin29/Robin-paper-3w-research).

如果只有一两篇论文，Skill 应将跨论文结论标记为 provisional，不应把它们表述为领域共识。文献发现可以与独立的论文检索 Skill（如 [`paper-3w-research`](https://github.com/Yaobin29/Robin-paper-3w-research)）配合使用。

## Design principle / 设计原则

> The unit of analysis is the research problem, not the paper.
>
> 分析单位是研究问题，而不是单篇论文。

The workflow treats author explanations as hypotheses unless the paper directly tests the relevant causal link. Every selected idea must state what result would falsify it.

除非论文直接检验了相关因果环节，否则将作者的解释视为假设。每个入选 Idea 都必须明确什么结果会使它被证伪。

## License / 许可证

MIT License. See [LICENSE](LICENSE).

MIT License，详见 [LICENSE](LICENSE)。
