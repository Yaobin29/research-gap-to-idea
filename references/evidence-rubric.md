# Evidence Rubric

Use this reference to keep scientific evidence separate from interpretation. A paper can provide strong measurements while still supporting only a weak mechanism claim.

## Evidence status

| Status | Meaning | Safe wording |
|---|---|---|
| `Demonstrated` | Directly measured under a stated comparison, control, and condition | “The study measured…” or “The experiment demonstrated…” |
| `Supported` | Multiple observations or independent papers converge, but the causal link is not isolated | “The evidence supports…” |
| `Inferred` | A reasonable interpretation that depends on assumptions or indirect evidence | “This suggests…” or “A plausible interpretation is…” |
| `Speculative` | A proposed explanation or future hypothesis not established by the source evidence | “We hypothesize…” or “This remains to be tested…” |

Do not use `Demonstrated` for a mechanism merely because the phenotype changed after an intervention.

## Four-layer extraction

| Layer | Extract | Do not add |
|---|---|---|
| Observation | What was visibly, qualitatively, or structurally observed | A causal explanation |
| Measurement | What instrument, assay, model, or statistic quantified | A biological meaning not validated by the assay |
| Interpretation | How the authors explain the observation or measurement | Treating the explanation as a direct fact |
| Claim | The strongest conclusion the paper presents | A broader claim outside the tested system or conditions |

For every important result, record the result, condition, comparator, scale, time point, and evidence status.

## Causal-chain audit

Represent the proposed mechanism as:

```text
intervention X
  → physical / chemical state change P
  → sensing or transduction M1
  → cell / agent response M2
  → tissue / system phenotype Y1
  → functional outcome Y2
```

Annotate every arrow:

- `[D]` directly measured;
- `[C]` correlated with the outcome;
- `[L]` imported from prior literature;
- `[U]` untested in the paper.

Example:

```text
magnetic field X
  → fiber reorientation P [D]
  → altered local anisotropy M1 [D/C]
  → cytoskeletal alignment M2 [C]
  → tissue alignment Y1 [D]
  → improved contractile function Y2 [U]
```

The untested link is a knowledge gap, not a demonstrated mechanism.

## Minimum per-paper record

```markdown
### <Paper ID> — <short title>

- Title:
- Authors:
- Journal:
- Year:
- Source: DOI / PMID / arXiv / stable URL
- Set: Core primary / Context-adversarial
- Study type:
- Model:
- Evidence tier: A / B / C / R
- Source role:
- Why included:
- WHY — author-claimed problem:
- WHY — problem the design can actually address:
- WHY — hidden assumptions:
- HOW — intervention and controllable variables:
- HOW — causal chain:
- WHAT — observations:
- WHAT — measurements:
- WHAT — author interpretations:
- WHAT — strongest bounded claim:
- Controls and comparators:
- Scale and time window:
- Directly measured links:
- Unknown or alternative links:
- Main limitation:
- Evidence status:
- Contribution to cross-paper comparison:
```

The paper record is one integrated card. Do not create a separate selection table that repeats or disconnects these fields.

## Cross-paper evidence rule

Agreement is meaningful only when the papers overlap sufficiently in system, intervention, outcome definition, and observation window. Apparent disagreement must first be decomposed by material, cell or organism, parameter range, timing, spatial scale, assay, and analysis method.

## Citation discipline for causal chains

Every causal arrow must have at least one source identifier or be explicitly marked `[U]`. A source identifier may be a paper ID in the report when the paper card contains the stable DOI, PMID, or URL. Do not cite only a final reference list for a central arrow without connecting the arrow to the source.
