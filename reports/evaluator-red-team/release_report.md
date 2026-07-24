# Publication and verification report

Date: 2026-07-24  
Status: **PUBLISHED; AWAITING LIVE JUDGE**

## Score and revision state

| Field | Value |
| --- | --- |
| Original judged baseline | 3/12 at `af641c4e7cc7775c33d10295b73ef75347a7ab1b` |
| Official live score | 5/12 |
| Judge head for that score | `22e4c6ccfea63d39df4fd57db0ddacb2a505b040` |
| Published Hugging Face revision | `adc03f7da795a88a5c7aaa19aa44ea6c2787c78a` |
| Strict blind forecast for candidate | 6/12, confidence 0.95 |
| Winning branch | `orx/recorded-blind-review-release-gate` |
| Winning Git SHA | `e62e0f84de8bb5b9dd5cc5e8d7d6365c49b48787` |
| Final ORX run | `e4e94c1c-fbe1-466f-aeb9-3f561b0b890a`, done |
| Fixed command | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` |

No score increase is claimed. The exact candidate is published but has not
yet been evaluated by the live judge.

## Experiment tree

The research descended through a stacked sequence:

1. `orx/evaluator-complete-proof-and-first-hit-evidence` replaced the
   formula-selected Claim 3 budget with 18 exact-KL first-hit searches.
2. `orx/evaluator-visible-complete-evidence-gate` created seven canonical
   pages with direct code, environment, data, checker, control, and limitation
   links.
3. `orx/downloaded-space-self-contained-rerun` made the fixed command
   regenerate evaluator-visible paths without Git metadata.
4. `orx/executable-controls-and-provenance-alignment` replaced declarative
   controls with 18 executed mutations and aligned evidence provenance.
5. `orx/final-evaluator-red-team-candidate` added the public report, figures,
   notebook updates, current linked evidence, and exact release gate.
6. `orx/canonical-space-provenance-alignment` fixed the only clean-room
   provenance inconsistency.
7. `orx/recorded-blind-review-release-gate` preserved the fresh blind review
   and file-access ledger in the evaluator-visible tree.

All seven runs used the same fixed command and local CPU.

## Claim-by-claim assessment

| Claim | Machine contract | Strict blind score | Evidence | Limitation blocking 2/2 |
| ---: | --- | ---: | --- | --- |
| 1 | VERIFIED | 1/2 | 252 exact rows; `epsilon^2`; symbolic `d^3`/`d^4` limits | The full universal KL inequality is a premise, not independently proved. |
| 2 | VERIFIED | 1/2 | 648 rows; strict H4-true/H3-false singular witness | The universal early-stopped inequality is not reconstructed. |
| 3 | VERIFIED | 1/2 | 80 schedule rows, 36 source-context rows, 18 non-circular first hits; 1.87–13.56x work ratios | First-hit evidence covers one exactly solvable bridge family. |
| 4 | VERIFIED | 1/2 | 1,008 W2 rows; numerical H3/H6/H7 audit; independent matrix checker | The universal stochastic W2 theorem is not independently proved. |
| 5 | VERIFIED | 1/2 | 280 unequal-product rows plus general pointwise product calculus | General dynamics inherit Theorem 4. |
| 6 | VERIFIED | 1/2 | 27 nonzero IBP rows plus symbolic product-rule identity | The full multivariate stochastic route from IBP to the final `d^3` estimate is not mechanized. |

`VERIFIED` above is the exact local contract vocabulary. It is not a forecast
that the live evaluator will award full credit.

## Evaluator-visible release gate

- Six canonical visibility rows are complete.
- The current seven pages are first in navigation.
- Every historical page remains reachable and is labeled
  **Historical rejected baseline**.
- All 2,349 raw rows regenerate from the fixed command.
- All 18 mutation controls are rejected.
- Representative inline values match the linked CSV values.
- The exact proposed Space was built in a fresh directory from the published
  `f2b258ac...` parent plus only the allowlist.
- All 102 upload hashes match and all payloads are UTF-8 text.
- Secret-pattern scan passed for all 102 payloads.
- All 88 parent files remain present; 85 are byte-identical. Only
  `README.md`, `pages/index.md`, and `logbook.json` intentionally change.
- The fresh blind reviewer began at the canonical entrypoint, recorded every
  opened file, reran the fixed command successfully, and forecast 6/12.

## Compute

Seven local ORX runs consumed approximately 5 minutes 45 seconds of wall
time on an 8-logical-core Apple arm64 CPU. No GPU or Hugging Face compute was
used. Direct compute cost: **$0**.

## Release payload

Exact upload allowlist: `upload-allowlist.txt`  
Allowlist SHA-256:
`27bb9d10b8b3e8b2651332d6d29fcd5afe368d2835b8dd3ca00c88a3c6885ac4`

Exact text manifest: `text-sha256-manifest.tsv`  
Manifest SHA-256:
`fabcbd01573512bdbe4228307fed77255ec48ca1449a68b87063c82c1ba8ea04`

Protected parent manifest: `judged-published-f2b258ac-manifest.tsv`  
Manifest SHA-256:
`9039352034ff76558deb522e5037c29e340cca97541b26099263f1390c386524`

Publication used the Hugging Face text-only commit API against the existing
Space `DineshAI/zl3akehFBq`, with 102 add/update operations and zero delete
operations. The resulting revision is
`adc03f7da795a88a5c7aaa19aa44ea6c2787c78a`.

## Post-publication verification

An independent download of the exact published revision verified all 102
payload hashes, preserved all 88 parent paths (85 byte-identical), passed the
6/6 canonical visibility traversal, kept current pages first and historical
pages labeled, and matched every displayed representative number to raw CSV.

This artifact is not an honest high-confidence 12/12 candidate. The strict
forecast remains 6/12, and the official score remains 5/12 until the live
judge records a verdict for `adc03f7d`.
