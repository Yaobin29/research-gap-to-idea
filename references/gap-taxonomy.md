# Gap Taxonomy

Use the three gap classes to distinguish missing capability, missing explanation, and a potentially wrong premise. Do not collapse all limitations into “more research is needed.”

## G1 — Technical Gap

### Definition

The field cannot reliably create, control, measure, maintain, scale, or reproduce a required state.

### Diagnostic questions

- Which variable cannot be controlled independently?
- Which spatial or temporal scale is inaccessible?
- Does the method fail under long-term, three-dimensional, or dynamic conditions?
- Is the readout too indirect, endpoint-only, averaged, or poorly standardized?
- Does performance degrade when the system is enlarged, integrated, or made more biologically realistic?

### Evidence pattern

```text
desired capability → current method → first failure boundary → consequence
```

### Typical output

An engineering intervention with a measurable performance target and a test of whether the missing capability changes the scientific conclusion.

## G2 — Knowledge Gap

### Definition

The field observes an outcome but cannot explain the relevant causal link, transition, threshold, or scale transfer.

### Diagnostic questions

- Which “may be due to” explanation lacks a discriminating experiment?
- Why does an effect appear only within a parameter window?
- Why do similar structures produce different functions?
- Why does a short-term effect fail to persist or translate into function?
- Which local event is assumed to cause the higher-scale phenotype?

### Evidence pattern

```text
reproducible observation → competing explanations → missing discriminator
```

### Typical output

A mechanism hypothesis with a minimal experiment that separates at least two plausible explanations.

## G3 — Assumption Gap

### Definition

Multiple studies rely on a premise that is treated as self-evident but is not independently tested or may be false.

### Diagnostic questions

- Is a proxy being treated as the target function?
- Is a static endpoint being used to explain a dynamic process?
- Is an average value hiding spatial heterogeneity?
- Is a local cell or molecular result being generalized to tissue or organism scale?
- Is a material or device parameter treated as a fixed input even though the biological system remodels it?
- Is “more alignment,” “more expression,” or “more stiffness” assumed to mean “better function” without a direct functional test?

### Evidence pattern

```text
shared premise → weak or indirect support → alternative prediction if premise fails
```

### Typical output

A decisive test that could overturn a dominant interpretation, not merely optimize the existing method.

## Cross-paper relationships

| Relationship | Identification rule | Idea opportunity |
|---|---|---|
| Convergence | Independent methods support the same bounded proposition | Test whether the shared proposition is causal or only a common proxy |
| Complementarity | Papers control or measure different links in one causal chain | Combine capabilities to close a previously unmeasured link |
| Contradiction | Comparable papers report incompatible outcomes or mechanisms | Search for an unmeasured state variable, threshold, or scale dependence |

## Gap statement template

```markdown
### G<number>: <short gap title>

- Class: Technical / Knowledge / Assumption
- Evidence: <paper IDs and exact observations>
- Missing link or capability: <what is not established>
- Existing explanation: <bounded summary>
- Why it is insufficient: <specific evidence limitation>
- Alternative hypothesis: <one causal sentence>
- Minimal discriminator: <experiment or analysis>
- Evidence status: Demonstrated / Supported / Inferred / Speculative
```
