# Evaluator-blind review round 3

## Scope and result

The reviewer received only an exact proposed Space tree constructed by
downloading
`DineshAI/zl3akehFBq@f2b258ac5c887a907b40ae0a6176236c0d574016`
into an empty directory and applying the 101-path text-only upload allowlist.
It received the six-claim rubric but no repository, ORX, dashboard, branch, or
evidence-path guidance. It began at `README.md` and followed only reachable
links.

Strict score: **6/12**, one scoped-evidence point for each claim.
Confidence: **high (0.95)**.

The reviewer found the artifact reproducible, fail-closed, well navigated, and
materially stronger than the rejected toy baseline. It did not award full
credit because the evidence does not contain independently reconstructed
proofs of the full stochastic inequalities in Theorems 1–4. Claim 5 inherits
Theorem 4's unverified dynamics, and Claim 6 proves the general scalar
integration-by-parts identity but not every multivariate stochastic estimate
connecting it to the complete `d^4`-to-`d^3` theorem argument.

## Claim scores

| Claim | Score | Reviewer conclusion |
| ---: | ---: | --- |
| 1 | 1/2 | Exact Gaussian recurrence, H1–H3 specialization, raw data, and symbolic limits are sound scoped evidence; the universal certificate assumes the displayed theorem inequality. |
| 2 | 1/2 | The singular witness rigorously establishes H4 without H3 and exact early-stopped Gaussian behavior; the universal KL inequality is not reconstructed. |
| 3 | 1/2 | The exact implicit schedule and 18 achieved-KL first-hit searches are non-circular and consistently favorable; universal logarithmic endpoint and `d^3` claims still rely on the theorem premise. |
| 4 | 1/2 | Correlated-Gaussian assumptions, exact W2 propagation, drift split, and matrix checker are credible; the general stochastic inequality is not proved. |
| 5 | 1/2 | General product score/block-Hessian identities and unequal-Gaussian corroboration are useful; the complete dynamics still depend on Theorem 4. |
| 6 | 1/2 | The boundary-free IBP identity is genuinely certified with nonzero checks; the complete tensor/stochastic derivation of the dimensional improvement is not mechanized. |

## Visibility matrix observed by the reviewer

Every row had directly visible exact claim wording, assumption discussion,
source code, fixed command and lock, inline values, raw CSV, checker, executed
controls, limitations, SHA/seeds/CPU/runtime, and fail-nonzero source. The
reviewer's only `partial` column was **exact universal scope**.

| Claim | Canonical page | Code | Inline data | Raw link | Checker | Control | Reviewer verdict |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `pages/11-current-claim-1/page.md` | yes | yes | yes | yes | yes | 1/2 scoped |
| 2 | `pages/12-current-claim-2/page.md` | yes | yes | yes | yes | yes | 1/2 scoped |
| 3 | `pages/13-current-claim-3/page.md` | yes | yes | yes | yes | yes | 1/2 scoped |
| 4 | `pages/14-current-claim-4/page.md` | yes | yes | yes | yes | yes | 1/2 scoped |
| 5 | `pages/15-current-claim-5/page.md` | yes | yes | yes | yes | yes | 1/2 scoped |
| 6 | `pages/16-current-claim-6/page.md` | yes | yes | yes | yes | yes | 1/2 scoped |

## Independent rerun

From the sealed Space tree, the reviewer ran:

```bash
uv sync --frozen && uv run --frozen python repro/src/verify_fm.py
```

It exited zero, reproduced the six row totals
`252 / 648 / (80+36+18) / 1008 / 280 / 27`, and rejected all 18 mutation
controls. Because the downloaded tree is not a Git checkout, regenerated
runtime metadata correctly records
`not-a-git-checkout; evidence-run=4d6a75b...`; the immutable published page
continues to record the original evidence run.

## Items the reviewer could not independently verify

- The complete universal stochastic proofs of Theorems 1–4.
- The original ORX run identity without consulting a system outside the
  sealed artifact.
- A distribution-general version of Claim 3's measured work advantage.
- The full H8-to-joint dynamics beyond the pointwise product identities.
- Every multivariate estimate between the IBP step and the final `d^3` bound.
- The downloaded source HTML hash, because only source URLs, theorem anchors,
  paraphrased quantifiers, retrieval metadata, and the hash are preserved.

## File-access ledger

The reviewer opened, in evaluator-visible traversal order:

1. `README.md`, `pages/index.md`, and `logbook.json`.
2. `pages/10-current-execution/page.md` through
   `pages/16-current-claim-6/page.md`.
3. `evidence/evaluator_visibility_matrix.csv` and
   `evidence/source/current-paper-claims.md`.
4. `evidence/source/paper_source.json`,
   `evidence/blind_review_round1.md`, and
   `evidence/blind_review_round2.md`.
5. `pyproject.toml`, `uv.lock`, `repro/src/verify_fm.py`,
   `repro/src/proof_certificates.py`, and `repro/src/evaluator_gate.py`.
6. For each `evidence/current/claim_1` through `claim_6`:
   `claim_contract.json`, `source_audit.md`, `method.md`,
   `independent_checker_output.json`, `negative_control_output.json`,
   `universal_certificate.json`, `runtime.json`, `EVAL.md`, and
   `limitations.md`.
7. Claims 1, 2, 4, 5, and 6 `raw_results.csv`; Claim 3
   `raw_schedule.csv`, `raw_complexity.csv`, and `raw_first_hit.csv`.

Historical rejected-baseline pages and all surrounding repository, ORX,
dashboard, and unpublished-branch paths were not used for scoring.

