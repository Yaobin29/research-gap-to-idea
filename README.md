# Research Gap to Idea

`research-gap-to-idea` is a portable agent skill for turning a small set of related scientific papers into a problem map, evidence boundary, and falsifiable research direction.

It is designed for researchers who want more than paper summaries or figure translation. The workflow compares papers around a shared question, reconstructs the causal chain, identifies technical, knowledge, and assumption gaps, and converts those gaps into testable Idea Cards.

## What it produces

- A first-principles definition of the shared research problem
- A curated and quality-graded core/context literature set
- One integrated Paper Analysis Card per paper, including journal metadata and enhanced `WHY / HOW / WHAT`
- A cited causal evidence ledger with `[D]`, `[C]`, `[L]`, and `[U]` boundaries
- First-principles derivation of Evidence Matrix dimensions and failure boundaries
- An evidence matrix separating observations, measurements, interpretations, and claims
- Technical, knowledge, and assumption gap analysis
- Cross-paper convergence, complementarity, contradiction, and anomaly analysis
- Incremental, integrative, and transformative research ideas
- Minimal discriminating experiments, predictions, falsification conditions, and Go/No-Go criteria
- Markdown and standalone offline HTML reports rendered from the same source

## Repository layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
│   └── render_report.py
├── references/
│   ├── anti-adhesion-hydrogel-example.md
│   ├── causal-model.md
│   ├── evidence-rubric.md
│   ├── gap-taxonomy.md
│   ├── idea-operators.md
│   ├── literature-curation.md
│   ├── output-template.md
│   └── quality-gates.md
└── assets/
    ├── report-template.html
    └── idea-card-template.md
```

## Use with an agent

Point your agent at `SKILL.md`, or invoke it explicitly:

```text
Use $research-gap-to-idea to synthesize these related papers into a shared problem, evidence matrix, three gap classes, and falsifiable research ideas.
```

The default response language is Chinese unless the user requests another language. Keep paper titles, technical terms, journal names, identifiers, and citations in their original form when precision matters.

When a report file is requested, render the Markdown report as a single offline HTML file:

```bash
python scripts/render_report.py report.md report.html
```

The renderer uses only the Python standard library and does not load external assets or CDN resources. Its default visual direction is a scientific editorial / research field-notes layout with responsive and print-friendly styling.

## Worked reference

[`references/anti-adhesion-hydrogel-example.md`](references/anti-adhesion-hydrogel-example.md) is a complete worked example for postoperative anti-adhesion hydrogels. It demonstrates the expected level of literature curation, journal metadata, causal evidence tracing, first-principles comparison dimensions, gap analysis, and non-combinatorial Idea Cards. It is a structural example, not a substitute for re-verifying sources in a new project.

## Recommended input

Provide 3–8 core papers that address one shared problem. Include PDFs, abstracts, DOI/PMID/arXiv identifiers, or stable URLs when available. The skill should add a separate context/adversarial set of reviews, clinical benchmarks, stronger comparison studies, or conflicting sources when literature discovery is possible. If only one or two papers are available, the skill should label cross-paper conclusions as provisional rather than presenting them as a field-level synthesis.

Literature discovery can be paired with a separate paper-search skill such as [`paper-3w-research`](https://github.com/Yaobin29/Robin-paper-3w-research). This repository intentionally keeps the synthesis workflow independent of a particular search provider or agent framework.

## Design principle

> The unit of analysis is the research problem, not the paper.

The workflow treats author explanations as hypotheses unless the paper directly tests the relevant causal link. Every selected idea must state what result would falsify it.

## License

MIT License. See [LICENSE](LICENSE).
