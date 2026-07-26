# Literature Curation and Quality Control

Use this reference before extracting 3W records. The purpose is to prevent a convenient set of papers from being mistaken for the best or complete evidence base.

## Two-set design

Keep the literature visibly separated:

| Set | Purpose | Counts as primary evidence? |
|---|---|---|
| Core primary set | Papers used to compare interventions, mechanisms, models, and outcomes | Yes |
| Context/adversarial set | Reviews, clinical benchmarks, standards, stronger comparison studies, and conflicting evidence | Only for the specific claim directly supported |

Use 3–8 core primary papers when possible. Add context sources without inflating the apparent number of mechanistic studies.

## Search record

Record:

- scope and biological/technical definition;
- databases or search tools;
- date searched;
- exact or representative queries;
- inclusion criteria;
- exclusion criteria;
- whether the user supplied the papers;
- whether citation chaining or backward/forward search was used;
- whether the search was exhaustive or a targeted evidence check.

If only supplied sources are analyzed, write `closed-set synthesis` and state that stronger or contradictory studies may be missing.

## Evidence tier

Assign a study tier from the evidence actually presented, not from journal prestige:

| Tier | Meaning | Typical features |
|---|---|---|
| A | High-confidence anchor | Appropriate model, meaningful comparator, adequate controls, relevant primary outcome, direct or well-separated mechanism measurements, transparent methods, and preferably independent or functional validation |
| B | Relevant primary evidence | Important outcome is measured, but mechanism, comparator, model realism, time window, or validation is incomplete |
| C | Exploratory or limited evidence | Small or narrow study, indirect endpoint, weak comparator, incomplete controls, or substantial interpretive uncertainty |
| R | Review/context/benchmark | Useful for field context, clinical baseline, or hypothesis generation; do not treat as a primary intervention experiment |

Journal name, year, DOI, and article type are mandatory provenance fields. A prestigious journal does not automatically make a study Tier A, and a less prominent journal does not automatically make it low quality.

## Adversarial backcheck

For every central synthesis claim, run at least these checks when literature access permits:

1. **Higher-quality check**: search for stronger models, direct mechanism experiments, systematic reviews, or clinical comparisons.
2. **Benchmark check**: identify accepted commercial, clinical, or engineering comparators.
3. **Contradiction check**: search for null, adverse, or opposite results.
4. **Scope check**: verify whether the result is limited to a material, species, model, time window, or endpoint.

Report the outcome as one of:

- `Checked and no stronger source identified in the stated search scope`;
- `Stronger/context evidence exists and changes the claim boundary`;
- `Search incomplete; claim remains provisional`.

## Paper selection record

```markdown
### <Paper ID> — <short title>

- Set: Core primary / Context-adversarial
- Title:
- Authors:
- Journal:
- Year:
- DOI / PMID / stable URL:
- Study type:
- Model:
- Evidence tier: A / B / C / R
- Source role:
- Why included:
- What claim it can support:
- Main limitation:
- Why not promoted to the core set (if applicable):
```

## Quality language

Use precise language:

- “This is a Tier A anchor for the measured outcome under the tested model.”
- “The study is relevant but Tier B because the mechanism was not isolated.”
- “The review establishes the clinical benchmark, not the mechanism of the new hydrogel.”
- “No stronger source was identified within the stated search scope; this is not evidence that none exists.”

Do not use journal impact factor, ranking, or publication date as a standalone proxy for truth.
