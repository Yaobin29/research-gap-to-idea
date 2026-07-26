---
name: research-gap-to-idea
description: Synthesize 3–8 related scientific papers from first principles, reconstruct the shared research problem, separate observations from interpretations, compare evidence and assumptions, identify technical, knowledge, and assumption gaps, resolve cross-paper contradictions, and generate falsifiable research hypotheses with minimal validation experiments. Use when the user wants multi-paper scientific synthesis, research-gap analysis, or testable research ideas rather than paper summaries, figure translation, or a conventional literature review.
---

# Research Gap to Idea

Use this skill to move from **papers as documents** to **problems as systems**. The required endpoint is not a polished summary. It is a bounded research model that explains what is established, what remains unknown, which assumptions may fail, and what experiment could discriminate between competing explanations.

## Operating rules

- Treat the request as `WHY`, `HOW`, or `MIX` before reading deeply.
- For `MIX`, keep the evidence/causal track separate from the design/idea track until the evidence map is complete.
- Prefer 3–8 papers addressing one shared problem. If fewer than three papers are available, state that cross-paper conclusions are provisional and either request more sources or perform a clearly labelled limited synthesis.
- Use the supplied papers, stable URLs, DOIs, abstracts, figures, methods, results, and supplementary information as the evidence base. Do not invent paper content or citations.
- When literature discovery is needed, reuse `paper-3w-research` when available or use an appropriate literature search tool, then verify DOI, PMID, arXiv ID, or stable URL before making a source-specific claim.
- Default to Chinese output unless the user asks for another language. Keep paper titles, technical terms, variable names, and source identifiers in their original form where precision matters.
- Mark the evidence status of important conclusions as `Demonstrated`, `Supported`, `Inferred`, or `Speculative`.
- Never turn an author's interpretation into an observation. Never call an idea novel merely because it sounds plausible; identify the comparison set and the unresolved gap.

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
| Mechanism M | What intermediate physical, chemical, biological, or computational state could transmit the effect? |
| Main constraint | What must be preserved or cannot be changed? |
| Observable | What measurement could distinguish the competing explanations? |

Rewrite the shared question as:

> For system **S**, can controlling **X**, through mechanism **M**, change outcome **Y** while satisfying **the main constraint**?

Do not accept a paper title or author framing as the final problem definition without testing it against the methods and measurements.

### 2. Build an enhanced 3W record for every paper

Organize each paper under `WHY / HOW / WHAT`, but expand each section:

- **WHY**: record the author-claimed problem, the problem the design can actually address, and the hidden assumptions required by the design.
- **HOW**: reconstruct the causal chain as `intervention → physical/chemical change → biological/computational sensing → response → phenotype/function`. Mark each link as directly measured, correlated, literature-supported, or untested.
- **WHAT**: separate `Observation`, `Measurement`, `Interpretation`, and `Claim`. Record controls, comparison groups, parameter ranges, time points, spatial scale, and functional readouts that limit the claim.

Read `references/evidence-rubric.md` for the evidence labels, causal-chain notation, and per-paper record.

### 3. Construct the cross-paper evidence map

Do not output papers in isolation. Build a matrix with at least these columns:

| Dimension | Paper A | Paper B | Paper C | Integrated judgment |
|---|---|---|---|---|
| Shared problem |  |  |  |  |
| Intervention / controllable X |  |  |  |  |
| Scale and time window |  |  |  |  |
| Direct measurements |  |  |  |  |
| Proposed mechanism M |  |  |  |  |
| Functional endpoint Y |  |  |  |  |
| Key assumptions |  |  |  |  |
| Main limitation |  |  |  |  |
| Evidence status |  |  |  |  |

Then classify relationships:

- **Convergence**: independent methods support the same proposition.
- **Complementarity**: different papers solve different links in the same causal chain.
- **Contradiction**: papers report incompatible outcomes or explanations.

For every contradiction, test material, cell or organism, parameter window, timing, spatial scale, measurement definition, analysis method, and true mechanism difference before calling it a scientific contradiction.

### 4. Identify the three gap classes

Read `references/gap-taxonomy.md` and record the strongest evidence for each gap:

- **G1 Technical Gap**: what the method cannot control, measure, scale, maintain, or reproduce.
- **G2 Knowledge Gap**: what is observed but not causally explained.
- **G3 Assumption Gap**: what the field treats as true without sufficient testing.

For each gap, state the exact evidence boundary. A gap is not simply a sentence from a Discussion section; it must be connected to a missing measurement, an unresolved comparison, an untested causal link, or a shared assumption.

### 5. Generate candidate hypotheses

Use `references/idea-operators.md` to apply the five operators:

1. Remove a Bottleneck.
2. Explain an Anomaly.
3. Resolve a Contradiction.
4. Bridge Scales.
5. Reverse the Causality.

Generate at least one candidate in each of these classes:

- **Incremental**: a bounded extension that tests a missing variable or control.
- **Integrative**: a combination that connects complementary capabilities from different papers.
- **Transformative**: a hypothesis that changes the problem definition or challenges a shared assumption.

Do not accept generic future-work statements such as “use more samples,” “test more cell types,” “perform animal studies,” or “combine AI” unless they specify a new variable, mechanism, discriminating experiment, prediction, and falsification condition.

### 6. Falsify before ranking

For every candidate, write one explicit causal sentence:

> When **X** changes under **condition C**, it changes **Y** through **mechanism M**.

Then specify:

- the minimal experiment that distinguishes the new hypothesis from the strongest existing explanation;
- the predicted result if the hypothesis is correct;
- the result that would falsify it;
- the most important alternative explanation and its control;
- the main feasibility and interpretation risk.

Score each candidate from 1–5 for `Novelty`, `Importance`, `Mechanistic depth`, `Testability`, `Feasibility`, and `Leverage`. Use the score to rank, not to hide uncertainty. A high score cannot override weak evidence or an unfalsifiable hypothesis.

### 7. Produce the final synthesis

Use `references/output-template.md` for the response structure. The final response must contain:

1. One-sentence core judgment.
2. First-principles problem decomposition.
3. Enhanced 3W records with source identifiers.
4. Cross-paper evidence matrix.
5. What is demonstrated, supported, inferred, and speculative.
6. Technical, knowledge, and assumption gaps.
7. Convergences, complementarities, contradictions, and anomalies.
8. At least three Idea Cards covering incremental, integrative, and transformative candidates.
9. The selected idea and why it outranks the alternatives.
10. The next smallest action, required evidence, first experiment, key readouts, and Go/No-Go criteria.

### 8. Run quality gates

Read `references/quality-gates.md` before finalizing. If the answer is mostly sequential summaries, figure translation, repeated abstracts, or unsupported “future work,” revise it. If a central conclusion has no evidence status or a selected idea has no falsification condition, do not present the synthesis as complete.

## Compact completion contract

The task is complete only when:

- the shared problem is stated independently of the paper titles;
- direct evidence is separated from interpretation and claim;
- the causal chain has explicit evidence boundaries;
- G1, G2, and G3 gaps have been considered;
- cross-paper convergence, complementarity, and contradiction have been tested;
- at least three falsifiable Idea Cards are present;
- the selected idea has a minimal discriminating experiment and Go/No-Go rule;
- citations or stable source identifiers support source-specific claims;
- uncertainty and evidence limits are visible in the final output.
