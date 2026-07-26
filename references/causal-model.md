# First-Principles Causal Model and Evidence Ledger

Use this reference to derive comparison dimensions and to audit the causal chain before generating Ideas.

## Derivation sequence

Start from the desired outcome and work backward:

```text
desired outcome Y
  → necessary system state
  → physical/chemical/biological condition maintaining that state
  → intervention that can change the condition
  → measurable readout
  → failure boundary
```

Only promote a property to an Evidence Matrix dimension when it has a plausible route to Y, a measurable readout, and a meaningful failure boundary.

## Dimension derivation record

```markdown
| Dimension | Causal link ID | Necessary state | Why necessary for Y | Readout | Failure boundary |
|---|---|---|---|---|---|
```

Examples of valid reasoning:

- If the outcome requires two tissues not to contact, coverage and continuity are causal dimensions, not merely formulation descriptors.
- If the injury evolves over time, residence and exit timing are dimensions because a static endpoint cannot establish temporal matching.
- If the intervention claims to alter inflammation, the relevant dimension is the measured inflammatory state and its relation to the outcome, not the presence of an antioxidant molecule alone.

## Causal Evidence Ledger

Give every arrow a stable link ID:

```markdown
| Link ID | Causal link | Supporting sources | Evidence type | What is measured | Unknown or alternative explanation | Minimal discriminator |
|---|---|---|---|---|---|---|
```

Use:

- `[D]` directly measured in the source under a stated comparator;
- `[C]` correlated with the outcome but not isolated causally;
- `[L]` supported by prior literature rather than directly tested in the core paper;
- `[U]` untested or currently speculative.

Do not label an entire chain as demonstrated when only its endpoint was measured. Annotate each arrow independently.

## Evidence-boundary rules

- A source can support a node without proving the arrow leaving that node.
- A changed animal adhesion score does not by itself demonstrate a specific molecular or cellular mechanism.
- A mechanistic assay in vitro does not establish the same mechanism at tissue or organism scale without a bridge measurement.
- A review can support background biology and a clinical benchmark, but it cannot be cited as a primary experiment for a new material.
- If no source supports an arrow, mark `[U]` and convert it into a G2 or G3 candidate only after specifying the missing discriminator.

## Causal chain quality check

Before finalizing, ask:

1. What is the earliest intervention-controlled state?
2. What is the first biological or physical transduction step?
3. Which intermediate state connects the local change to the final outcome?
4. Which arrow is only inferred from an endpoint?
5. What observation would distinguish the leading explanation from its strongest alternative?
