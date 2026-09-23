# Preamble Adjudication

## Source Triple
`lectures/preamble.tex` + `assessment/lectures/preamble.md` + `assessment/audit/lectures/preamble.md`

## Final Ruling
REPLACE

## Confidence
High

## Why Keep/Revise/Replace
The first-pass assessment over-reads the file's role enough that it should not be used as the final assessment. It is not wholly wrong: the preamble does more than load packages, and it does define shared theorem environments, reusable box styles, page layout, and a common set of physics macros such as `\SU`, `\UU`, `\Nc`, `\Nf`, `\bzero`, and `\alphas`. Its praise for the pedagogical value of `conventionbox`, `warningbox`, `previewbox`, and `comparisontable` is well grounded.

But the assessment's central thesis is materially off. The preamble's main job is not semantic governance of the lecture corpus. It is mostly infrastructure: package loading, theorem setup, formatting, and a thin common notation layer. The top comments record a few locked conventions, but the file does not centrally manage the later course-specific conventions the first pass implies. There is no explicit hierarchy of universal versus lecture-local conventions, no dedicated anomaly ledger, and no support machinery for later SO/Sp group conventions, Pati-Salam embeddings, hypercharge assignments, or meson-sector notation. Those are introduced inside the lecture files themselves.

Because of that misframing, several concerns in the first pass are speculative rather than source-grounded. Worries about semantic overload in `\Wsup`, `\Tadj`, `\bzero`, and `\Nf` depend on how later lectures use those macros, not on what this file itself documents. The first pass therefore judges the preamble against responsibilities it does not actually claim.

## Minimum Changes Needed
This is a replace, not a revise. A usable final assessment would need to:

- rewrite the scope around "shared technical infrastructure plus modest notation layer";
- keep the praise for common macros and box environments;
- replace speculative downstream-convention concerns with the concrete limitation visible here: the preamble is intentionally thin, so lecture-local convention boxes must carry most specialized semantic work.

## Notes For Final Summary
Only file where the first pass's core framing is wrong enough that targeted edits are not sufficient.
