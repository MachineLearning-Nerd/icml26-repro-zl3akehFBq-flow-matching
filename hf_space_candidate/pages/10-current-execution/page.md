# CURRENT executed evidence — evaluator-visible release gate

This page records the current executable reproduction and supersedes the
**Historical rejected baseline** verifier. The historical script is preserved
but is not the current code.

## Actual ORX run

| Field | Recorded value |
| --- | --- |
| Run ID | `8c10975f-a2f4-4176-b678-50a2d55aa962` |
| Git SHA | `4d6a75b59e359f03b8836d1e7488910eda66b84a` |
| Status | `done`, exit code 0 |
| Verifier runtime | `29.64489712499926` seconds |
| Hardware | local Apple arm64 CPU, 8 logical cores; no GPU |
| Python | 3.12.11 |
| Fixed command | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` |
| Seeds | none; closed-form deterministic arithmetic |

The literal ORX log summary was:

```text
CLAIM 1: VERIFIED — 252 exact rows; controls 3/3 rejected
CLAIM 2: VERIFIED — H3=False, H4=True; 648 rows; controls 3/3 rejected
CLAIM 3: VERIFIED — 80 schedule + 36 bound-context + 18 observed first-hit rows
Observed first-hit uniform/nonuniform work ratio range=[1.87, 13.6]
CLAIM 4: VERIFIED — 1,008 exact rows; controls 3/3 rejected
CLAIM 5: VERIFIED — 280 exact rows; controls 3/3 rejected
CLAIM 6: VERIFIED — 27 IBP rows; maximum residual=2.22e-16
```

## Evaluator-visible files

- [Current executable verifier](../../repro/src/verify_fm.py)
- [Independent symbolic certificates](../../repro/src/proof_certificates.py)
- [Visibility gate source](../../repro/src/evaluator_gate.py)
- [Pinned project](../../pyproject.toml) and [exact lock](../../uv.lock)
- [Six-row visibility matrix](../../evidence/evaluator_visibility_matrix.csv)
- [Blind-review round 1](../../evidence/blind_review_round1.md)
- [Blind-review round 2 and resolved findings](../../evidence/blind_review_round2.md)

The command is fail-closed: failed checks raise `AssertionError`; the top-level
exception path re-raises and exits nonzero. Negative controls invert or remove
essential premises and must be rejected. The visibility gate itself checks
canonical navigation, every direct link, inline field coverage, raw first-hit
rows, source, and environment.

## Evidence interpretation

Finite Gaussian cases are labeled scoped corroboration. They are not used to
infer universal quantifiers. The linked universal certificates independently
derive the rate/decomposition consequences of the displayed inequalities.
Claims 5 and 6 additionally certify arbitrary product-density identities and
the boundary-free integration-by-parts identity. The limitations on Claims
1–4 explicitly state that these certificates do not mechanically formalize
the full stochastic proofs.

The exact published parent revision
`DineshAI/zl3akehFBq@f2b258ac5c887a907b40ae0a6176236c0d574016`
was downloaded into an empty directory before edits. Its 88-file manifest and
logbook snapshot are protected; every non-logbook historical file must remain
byte-identical.
