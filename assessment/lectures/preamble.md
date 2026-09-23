# Preamble Assessment

## Source
`lectures/preamble.tex`

## Scope
This preamble defines the shared notation, standard packages, theorem-like boxes, and global macros used by the lecture corpus. Its main role is semantic: it fixes the interpretive framework that the later lectures depend on.

## Strengths
The preamble is doing useful work beyond LaTeX housekeeping. It centralizes the core conventions for metric signature, normalization, anomaly coefficients, and gauge-group macros, which makes the notation stable across a large and conceptually dense corpus. The box environments are also pedagogically well chosen: `conventionbox`, `warningbox`, and `previewbox` support the course’s repeated pattern of stating assumptions, flagging limits, and signaling forward references.

From a content perspective, the preamble encourages coherence. By giving the same symbolic treatment to gauge groups, beta-function coefficients, and SUSY quantities, it makes cross-lecture reuse easier and reduces the chance that the same concept will be reintroduced under a new notation.

## Concerns
- The preamble fixes a fairly narrow core notation and then relies on later lectures to add special-case conventions. That is workable, but it increases the risk of inconsistent extensions when the corpus moves beyond SU-based SUSY material into SO/Sp, Pati--Salam, and meson physics.
- Some macros are semantically overloaded for a course of this breadth. For example, `\Wsup`, `\Tadj`, `\bzero`, and `\Nf` are useful in the SUSY lectures, but later non-SUSY or hadronic sections have to reinterpret them carefully.
- The preamble does not itself encode a hierarchy between universal conventions and lecture-local conventions, so the reader has to infer which symbols are stable across the entire course and which are provisional.

## Suggestions
- Separate the notation into “course-wide” and “lecture-local” layers in comments, even if the macros remain in one file. That would make later conceptual drift easier to manage.
- Add a brief notation-policy note explaining that new physical settings may introduce their own conventions, but only after explicitly declaring them in the lecture body.
- If the corpus continues to grow, consider a small convention ledger for the major recurring symbols so that later assessments and lectures can keep the semantic map aligned.
