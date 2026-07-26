---
name: research-gap-to-idea
description: Synthesize 3–8 related scientific papers from first principles, reconstruct the shared research problem, separate observations from interpretations, compare evidence and assumptions, identify technical, knowledge, and assumption gaps, resolve cross-paper contradictions, and generate falsifiable research hypotheses with minimal validation experiments. Use when the user wants multi-paper scientific synthesis, research-gap analysis, or testable research ideas rather than paper summaries, figure translation, or a conventional literature review.
---

# Research Gap to Idea

Use this skill to move from **papers as documents** to **problems as systems**. The required endpoint is a bounded research model that explains what is established, what remains unknown, which assumptions may fail, and what experiment could discriminate between competing explanations. Produce both a reusable Markdown report and, when a report artifact is requested, a standalone offline HTML version rendered from the same Markdown source.

## Operating rules

- Classify the request as `WHY`, `HOW`, or `MIX` before reading deeply. For `MIX`, separate the evidence/causal track from the design/idea track until the evidence map is complete.
- Prefer 3–8 core papers addressing one shared problem, supplemented by a separate context set of reviews, clinical benchmarks, standards, or stronger comparison studies. Do not silently treat the context set as mechanistic primary evidence.
- Before 3W extraction, run literature curation. Record the search scope, query logic, date, source set, inclusion/exclusion rationale, source role, journal, study type, model, and evidence tier. If only supplied papers are used, label the synthesis `closed-set synthesis` and do not claim field-wide completeness.
- Use journal metadata as provenance and context, not as a substitute for study quality. Judge evidence quality from controls, model fit, directness of mechanism measurements, comparator quality, outcome relevance, transparency, and external validation.
- Perform an adversarial backcheck for central claims: look for higher-quality primary studies, systematic reviews, clinical benchmarks, and conflicting evidence. Use `references/literature-curation.md`.
- Use supplied papers, stable URLs, DOIs, abstracts, figures, methods, results, supplementary information, and verified literature sources as the evidence base. Do not invent paper content or citations.
- When literature discovery is needed, reuse `paper-3w-research` when available or use an appropriate literature search tool, then verify DOI, PMID, journal, year, and stable URL before making source-specific claims.
- Default to Chinese output unless the user asks for another language. Keep paper titles, technical terms, variable names, journal names, and source identifiers in their original form where precision matters.
- Mark important conclusions as `Demonstrated`, `Supported`, `Inferred`, or `Speculative`.
- Never turn an author's interpretation into an observation. Never call an idea novel merely because it sounds plausible or combines named components.

## Workflow

### 1. Classify and define the shared problem

Start with a compact problem frame:

| Field | Required question |
|---|---|
| Problem type | Is this `WHY`, `HOW`, or `MIX`? |
| System S | What biological, physical, material, device, or computational system is being studied? |
| Target Y | What state, function, or outcome is desired? |
| Current state | What can the field do now, and under which conditions? |
| Controllable X | Which intervention, parameter, or state variable can be changed? |
| Mechanism M | What intermediate state could transmit the effect? |
| Main constraint | What must be preserved or cannot be changed? |
| Observable | What measurement could distinguish competing explanations? |

Rewrite the shared question as:

> For system **S**, can controlling **X**, through mechanism **M**, change outcome **Y** while satisfying **the main constraint**?

Do not accept a paper title or author framing as the final problem definition without testing it against methods, measurements, controls, and outcome definitions.

### 2. Curate and grade the literature set

Read `references/literature-curation.md`. Create two visibly separate sets:

- **Core primary set**: papers used for the cross-paper mechanistic synthesis.
- **Context and adversarial set**: reviews, clinical or commercial benchmarks, standards, higher-quality comparison studies, and conflicting studies used to calibrate claims.

For every paper, record complete metadata and a reason for inclusion. For every important omitted or discovered source, record why it was not promoted into the core set. Do not infer quality from journal prestige alone.

### 3. Build one integrated Paper Analysis Card per core paper

Do not create a detached paper-selection list followed by disconnected 3W summaries. Each paper must appear as one analysis card containing:

- Citation metadata: title, authors, journal, year, DOI/PMID/stable URL;
- study type, model, source role, evidence tier, and why included;
- **WHY**: author-claimed problem, problem the design can actually address, hidden assumptions;
- **HOW**: intervention, controllable variables, causal chain, and evidence status for every link;
- **WHAT**: Observation, Measurement, Interpretation, Claim, controls, comparator, parameter range, time point, spatial scale, functional readout;
- direct evidence, unknown links, main limitation, and contribution to the cross-paper comparison.

Read `references/evidence-rubric.md` for the evidence labels and card schema.

### 4. Derive first-principles comparison dimensions

Before building the Evidence Matrix, derive dimensions through:

```text
target outcome Y
  → necessary system states
  → physical/biological conditions maintaining those states
  → failure boundaries
  → measurable readouts
  → cross-paper comparison dimensions
```

For every dimension, state its causal-link ID, why it is necessary, its readout, and its failure boundary. Do not compare arbitrary material properties without explaining how they can affect Y.

### 5. Build the causal evidence ledger and cross-paper evidence map

Read `references/causal-model.md` and construct a cited ledger for every causal arrow:

| Link ID | Causal link | Sources | Evidence type | Measured | Unknown/alternative | Minimal discriminator |
|---|---|---|---|---|---|---|

Use `[D]` directly measured, `[C]` correlated, `[L]` supported by prior literature, and `[U]` untested. Every arrow must have a source or an explicit `[U]` label.

Then build an Evidence Matrix whose rows are derived dimensions and include the rationale, causal link, missing measurement, and failure boundary. Classify relationships as:

- **Convergence**: independent methods support the same bounded proposition;
- **Complementarity**: different papers address different links in one causal chain;
- **Contradiction**: comparable papers report incompatible outcomes or mechanisms.

Before calling a contradiction scientific, test material, cell or organism, parameter window, timing, spatial scale, measurement definition, analysis method, and model severity.

### 6. Identify G1, G2, and G3 gaps

Read `references/gap-taxonomy.md` and connect every gap to source evidence and a causal ledger link:

- **G1 Technical Gap**: what cannot be controlled, measured, maintained, scaled, or reproduced;
- **G2 Knowledge Gap**: what is observed but not causally explained;
- **G3 Assumption Gap**: what is treated as true without sufficient testing.

For each gap, state the evidence boundary, consequence, competing explanation, and minimal discriminator. A gap is not merely a Discussion sentence.

### 7. Generate non-combinatorial candidate hypotheses

Read `references/idea-operators.md`. Generate at least one defensible candidate in each class:

- **Incremental**: bounded extension testing a missing variable or control;
- **Integrative**: closes a missing causal link between complementary capabilities;
- **Transformative**: changes the problem definition or challenges a shared assumption.

Every candidate must trace:

```text
unresolved phenomenon
  → unresolved causal link
  → why existing studies cannot resolve it
  → minimal state variable
  → new hypothesis
  → discriminating experiment
  → new prediction
```

Apply the non-combination test: remove paper names and component names from the idea. If no independent causal proposition, state variable, threshold, coupling, or new prediction remains, reject it as simple stitching. Require ablation or factorial controls whenever the idea uses multiple modules.

### 8. Falsify before ranking

For every candidate, write:

> When **X** changes under **condition C**, it changes **Y** through **mechanism M**.

Then specify source evidence IDs, unresolved causal link, why existing explanations are insufficient, minimal experiment, predicted result, falsification condition, alternative explanation, ablation/factorial control, feasibility, risk, and scientific value. Score 1–5 for `Novelty`, `Importance`, `Mechanistic depth`, `Testability`, `Feasibility`, and `Leverage`; use the profile to rank rather than hide uncertainty.

### 9. Produce Markdown and standalone HTML

Use `references/output-template.md`. The final synthesis must contain the literature curation, integrated Paper Analysis Cards, first-principles dimension derivation, cited causal ledger, Evidence Matrix, evidence states, gaps, cross-paper relationships, three Idea Cards, preferred idea, experiments, and evidence ceiling.

When an artifact is requested, render the final Markdown with `scripts/render_report.py` using `assets/report-template.html`. The HTML must be a single offline file with embedded CSS, responsive layout, print styles, navigation, collapsible paper cards, horizontally scrollable matrices, evidence-state styling, and Idea Card styling. Do not use external CDN assets.

### 10. Run quality gates

Read `references/quality-gates.md` before finalizing. If the answer is mostly sequential summaries, lacks literature curation, has uncited causal arrows, uses arbitrary matrix dimensions, or proposes component stitching without a new causal prediction, revise it. If a central conclusion has no evidence status or a selected idea has no falsification condition, do not present the synthesis as complete.

## Compact completion contract

The task is complete only when:

- the literature set has a documented scope, quality tier, inclusion rationale, and adversarial backcheck;
- every core paper has one integrated card with journal metadata and enhanced WHY/HOW/WHAT;
- the shared problem is stated independently of paper titles;
- comparison dimensions are derived from necessary states, causal links, readouts, and failure boundaries;
- every causal arrow has a source or explicit `[U]` status;
- direct evidence is separated from interpretation and claim;
- G1, G2, and G3 gaps are connected to evidence;
- convergence, complementarity, and contradiction have been tested;
- at least three non-combinatorial falsifiable Idea Cards are present;
- the selected idea has a minimal discriminating experiment, ablation/factorial control, and Go/No-Go rule;
- citations or stable source identifiers support source-specific claims;
- uncertainty and evidence limits are visible;
- Markdown and standalone HTML are generated from the same report content when requested.
