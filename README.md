# Research Gap to Idea

`research-gap-to-idea` is a portable agent skill for turning a small set of related scientific papers into a problem map, evidence boundary, and falsifiable research direction.

It is designed for researchers who want more than paper summaries or figure translation. The workflow compares papers around a shared question, reconstructs the causal chain, identifies technical, knowledge, and assumption gaps, and converts those gaps into testable Idea Cards.

## What it produces

- A first-principles definition of the shared research problem
- Enhanced `WHY / HOW / WHAT` records for each paper
- An evidence matrix separating observations, measurements, interpretations, and claims
- Technical, knowledge, and assumption gap analysis
- Cross-paper convergence, complementarity, contradiction, and anomaly analysis
- Incremental, integrative, and transformative research ideas
- Minimal discriminating experiments, predictions, falsification conditions, and Go/No-Go criteria

## Repository layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evidence-rubric.md
│   ├── gap-taxonomy.md
│   ├── idea-operators.md
│   ├── output-template.md
│   └── quality-gates.md
└── assets/
    └── idea-card-template.md
```

## Use with an agent

Point your agent at `SKILL.md`, or invoke it explicitly:

```text
Use $research-gap-to-idea to synthesize these related papers into a shared problem, evidence matrix, three gap classes, and falsifiable research ideas.
```

The default response language is Chinese unless the user requests another language. Keep paper titles, technical terms, identifiers, and citations in their original form when precision matters.

## Recommended input

Provide 3–8 papers that address one shared problem. Include PDFs, abstracts, DOI/PMID/arXiv identifiers, or stable URLs when available. If only one or two papers are available, the skill should label cross-paper conclusions as provisional rather than presenting them as a field-level synthesis.

Literature discovery can be paired with a separate paper-search skill such as [`paper-3w-research`](https://github.com/Yaobin29/Robin-paper-3w-research). This repository intentionally keeps the synthesis workflow independent of a particular search provider or agent framework.

## Design principle

> The unit of analysis is the research problem, not the paper.

The workflow treats author explanations as hypotheses unless the paper directly tests the relevant causal link. Every selected idea must state what result would falsify it.

## License

MIT License. See [LICENSE](LICENSE).
