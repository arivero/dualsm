# Audit Of The Assessments

This folder is a second-pass review of the first-pass assessment files.

For each source, the audit reads:

- the original `.tex` file
- the matching file under `assessment/`

and then judges whether the first-pass assessment is:

- accurate
- accurate but incomplete
- overstated
- mistaken in important respects

In this context, phrases like "directionally right" or "directionally plausible"
mean:

- the first-pass assessment identified the general area of concern
- but it was not precise enough about the actual source text
- and may have missed stronger source-level evidence, internal contradictions,
  or places where the original text already included the requested caveat

The most serious misses found in this audit include:

- assessments that criticized material the source had already qualified
- assessments that missed direct prompt-solution contradictions
- assessments that understated internal contradictions inside a paper
- at least one assessment that appears to describe a different file structure

The audit files are organized in parallel to the original review set:

- `assessment/audit/lectures/`
- `assessment/audit/exercises/`
- `assessment/audit/papers/`
