# Agent instructions

# What counts as progress

User instruction of 26 November 2026. The papers and lectures test proposed relations among gauge duality, flavour masses and generation number. Three outcomes move a line of research, in this order of value.

1. **An input is derived.** A quantity that a relation takes from a fit or by hand (a scale, a mixing, a Kähler coefficient, a choice of branch or vacuum) is computed from the dynamics, and one free choice disappears.
2. **A prediction is made and tested.** A mass relation or a number with no adjusted input is written down with its precision before the comparison, and is then compared with a held-out measurement. Agreement and disagreement both count. State how many relations were tried.
3. **A candidate mechanism is eliminated by a test it could have passed**, and the next candidate is named.

Checks, restatements, results in a simplified model and findings that a coefficient is free are support. They are recorded with the same care, and the README novelty table says that the line stands where it was.

A numerical coincidence carries weight through a structure that hosts it and a second consequence of that structure, more than through its precision. For each relation, name the hosting structure, derive a second consequence and test it.

State conjectures, labelled as such, each with the simplest test that would refute it. After a negative result, list its escapes and attempt the most promising one next. A model chosen so that the answer comes out is a scout: say so in its first sentence and keep the computation in the actual theory as the open step. Search the literature for an existing result before deriving from first principles.

When a ticket closes, the closing comment classifies the exit as reached (an input derived or a prediction tested), narrowed (a candidate eliminated, the next one named) or blocked (the decisive computation remains and is stated as the next target), and the README states what research stays open. After three exits in a row on one line without a reached one, review which single computation would decide that line.

# Integration without pull requests

Integrate finished work directly on the repository's default branch as
set on GitHub (usually `main` or `master`; check with
`gh repo view --json defaultBranchRef`). Fast-forward when the history allows it, otherwise merge
locally, then push the default branch. Do not open pull requests. A side
branch is for work in progress only; merge it back as soon as the work
is complete and delete it afterwards. User instruction of 20 November 2026.
