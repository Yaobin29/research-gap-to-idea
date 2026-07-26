# Output Template

Use this structure for the final multi-paper synthesis. Keep the report problem-centred while keeping every core paper traceable.

## 1. Literature curation

State the search scope, date, tools/databases, query logic, inclusion/exclusion criteria, whether the set is closed or actively searched, core/context set, evidence tiers, and adversarial backcheck. Include complete journal metadata for every paper.

## 2. Core judgment

> <One sentence stating the real bottleneck or unresolved mechanism across the papers.>

Evidence status: Demonstrated / Supported / Inferred / Speculative

## 3. Problem frame

| Field | Synthesis |
|---|---|
| Problem type | WHY / HOW / MIX |
| System S |  |
| Desired outcome Y |  |
| Current state |  |
| Controllable X |  |
| Candidate mechanism M |  |
| Main constraint |  |
| Key observable |  |

Minimal causal model:

```text
X → M → Y
```

## 4. Causal Evidence Ledger

| Link ID | Causal link | Supporting sources | Evidence type | Measured | Unknown/alternative | Minimal discriminator |
|---|---|---|---|---|---|---|
|  |  |  | `[D]` / `[C]` / `[L]` / `[U]` |  |  |  |

Every causal arrow in the model must appear in this ledger or be explicitly marked `[U]`.

## 5. Integrated Paper Analysis Cards

Use exactly one compact card per core paper, with citation metadata, journal, year, study type, model, evidence tier, source role, inclusion rationale, WHY/HOW/WHAT, causal evidence, unknown links, limitations, and contribution to the comparison. Do not separate paper selection from 3W records.

## 6. First-principles dimension derivation

```text
target Y → necessary states → maintaining conditions → failure boundaries → readouts → comparison dimensions
```

| Dimension | Causal link | Necessary state | Why necessary | Readout | Failure boundary |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 7. Cross-paper Evidence Matrix

| Dimension | Why this dimension | Causal link | Paper A | Paper B | Paper C | Missing measurement | Failure boundary | Integrated judgment |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## 8. Solved and unsolved space

### Demonstrated

- <bounded result with source>

### Supported

- <cross-paper pattern with source set>

### Inferred

- <reasonable but indirect interpretation>

### Speculative

- <hypothesis that still requires testing>

## 9. Gap map

### G1 — Technical Gap

<Gap statement, evidence, failure boundary, consequence, and minimal discriminator.>

### G2 — Knowledge Gap

<Unexplained observation, competing mechanisms, missing discriminator, and causal-link ID.>

### G3 — Assumption Gap

<Shared premise, evidence weakness, alternative prediction, and decisive test.>

## 10. Cross-paper relationships

| Relationship | Evidence | Interpretation | Remaining test |
|---|---|---|---|
| Convergence |  |  |  |
| Complementarity |  |  |  |
| Contradiction |  |  |  |

## 11. Idea Cards

Include at least one `Incremental`, one `Integrative`, and one `Transformative` card. Each card must include source evidence IDs, unresolved causal link, minimal state variable, genuine novelty, non-combination novelty check, and ablation/factorial control. Use the schema in `references/idea-operators.md`.

## 12. Preferred idea

| Criterion | Judgment |
|---|---|
| Selected idea |  |
| Why it outranks alternatives |  |
| Evidence strength |  |
| Main uncertainty |  |
| First decisive experiment |  |
| Go criterion |  |
| No-Go criterion |  |

## 13. Evidence ceiling and next smallest action

- Literature limitations and evidence ceiling:
- Additional evidence to retrieve:
- First experiment or analysis:
- Key readouts:
- Controls:
- Decision date or checkpoint:
- Go/No-Go rule:

## 14. HTML deliverable

When an artifact is requested, render this Markdown source into a standalone offline HTML file with embedded CSS, navigation, collapsible Paper Analysis Cards, scrollable matrices, causal evidence styling, and Idea Card styling. The HTML must not introduce content that is absent from the Markdown source.
