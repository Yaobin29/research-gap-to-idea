# Quality Gates

Run these checks before calling a synthesis complete.

## Gate 1 — Anti-summary

Fail if the response is mainly:

- figure-by-figure translation;
- sequential Paper A → Paper B → Paper C summaries;
- repeated abstracts or introductions;
- generic “the authors found” statements without an integrated judgment;
- a report with no shared problem, evidence matrix, or causal model.

Repair by rewriting around the shared problem and adding the cross-paper matrix before expanding paper records.

## Gate 2 — Evidence boundary

For every central claim, check:

- Is it directly measured, supported across papers, inferred, or speculative?
- Is the comparator or control clear?
- Is the claim within the tested system, scale, and time window?
- Has an author interpretation been mistakenly written as an observation?
- Does each source-specific claim have a DOI, PMID, arXiv ID, stable URL, or supplied source reference?

Repair by downgrading wording or adding the missing source and limitation.

## Gate 3 — Gap specificity

For each G1, G2, and G3 entry, require:

- a concrete missing capability, link, measurement, comparison, or premise;
- at least one source observation;
- a reason existing evidence is insufficient;
- a consequence if the gap remains unresolved;
- a minimal discriminator or next measurement.

“More research is needed” is not a gap statement.

## Gate 4 — Anti-empty-Idea

Reject an Idea Card if it lacks any of:

- a new variable or state condition;
- a causal mechanism;
- a minimum discriminating experiment;
- a predicted result;
- a falsification condition;
- a meaningful alternative explanation or control.

Generic suggestions such as larger samples, more cell types, animal studies, long-term work, or AI integration are not ideas without these fields.

## Gate 5 — Selection integrity

Before selecting a preferred idea, verify:

- Incremental, Integrative, and Transformative candidates were considered;
- the preferred idea is not selected only because it is easiest;
- feasibility and evidence strength are reported separately from novelty;
- the first experiment can produce a Go/No-Go decision;
- the main risk is explicit.

If a gate fails, state the failure and revise the synthesis instead of presenting a confident final recommendation.
