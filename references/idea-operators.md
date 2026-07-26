# Idea Operators and Scoring

Use these operators to transform a documented gap into a research hypothesis. Each operator must preserve a traceable link to the evidence map.

## Five operators

### 1. Remove a Bottleneck

```text
Current method achieves X but fails at Y.
Introduce Z to remove the failure boundary while preserving A.
```

Use for a technical gap. Define the performance threshold and the biological or scientific consequence of crossing it.

### 2. Explain an Anomaly

```text
Several studies observe X, but mechanism M cannot explain condition C.
Hypothesis N proposes that state variable Z switches the outcome.
```

Use for a knowledge gap with a reproducible anomaly and competing explanations.

### 3. Resolve a Contradiction

```text
Paper A and Paper B report opposite outcomes for X.
The difference arises from unmeasured state variable Z or regime boundary T.
```

Test parameter windows, material state, cell state, time, scale, and measurement definitions before proposing a new mechanism.

### 4. Bridge Scales

```text
Local change L is established, but transfer to system outcome Y is not.
Hypothesis M specifies the intermediate coupling that transmits L to Y.
```

Make the intermediate variable measurable. Do not jump from molecular or cellular data to tissue or organism function without a bridge.

### 5. Reverse the Causality

```text
The field assumes A causes B.
Test whether B or a remodeling process changes A and controls the long-term state.
```

Use when the dominant causal direction is inferred from static or endpoint data.

## Idea Card schema

Every candidate must use this schema:

```markdown
## Idea <ID> — <short title>

- Class: Incremental / Integrative / Transformative
- Operator: <one of the five operators>
- Source gap: G1 / G2 / G3 / contradiction <ID>
- Unresolved problem: <bounded statement>
- New hypothesis: When <X> changes under <condition>, <Y> changes through <M>.
- Why existing explanations are insufficient: <specific evidence boundary>
- Critical experiment: <smallest experiment that separates explanations>
- Predicted result: <what should be observed if true>
- Falsification condition: <what would make it false>
- Controls and alternative explanation: <minimum controls>
- Scientific value: Technical / Mechanistic / Contradiction / Cross-scale / Assumption challenge
- Feasibility: <resources, platform fit, key dependency>
- Risks: <interpretation, execution, or novelty risk>
- Potential paper story: <one bounded sentence>
```

## Candidate generation rule

Generate one candidate for each class before selecting a preferred idea. If a class is not defensible from the evidence, state why rather than forcing a decorative idea.

## Scoring rubric

Score each dimension from 1 to 5:

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Novelty | Direct repetition | Meaningful extension | Changes the explanatory or technical frame |
| Importance | Narrow local optimization | Improves a useful capability or explanation | Could change field-level understanding or practice |
| Mechanistic depth | Phenotypic association | Tests an intermediate link | Establishes or overturns a causal model |
| Testability | No clear discriminator | Test exists but is multi-step | Minimal decisive test is available |
| Feasibility | Requires unavailable infrastructure | Requires substantial adaptation | Fits current platform and resources |
| Leverage | Little reuse of existing capability | Reuses some platform or data | Strongly compounds existing capability |

Use the profile of scores, not only the total. A transformative idea with a low feasibility score may remain valuable as a long-term direction, while a high-feasibility idea with weak mechanistic depth may be suitable only as a short-term experiment.
