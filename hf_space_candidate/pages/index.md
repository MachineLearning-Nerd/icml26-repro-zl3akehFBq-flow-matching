# Repro - Diffusion Flow Matching: Dimension-Improved KL Bounds

## Current verification

This is the canonical evaluator entrypoint. The current verifier is
[`repro/src/verify_fm.py`](../repro/src/verify_fm.py), executed with the
locked [`pyproject.toml`](../pyproject.toml) and
[`uv.lock`](../uv.lock). Any failed contract or accepted negative control
terminates with a nonzero exit.

| Order | Current evidence page | Result |
| ---: | --- | --- |
| 0 | [Execution, command, environment, and visibility gate](#/10-current-execution) | exit 0 |
| 1 | [Claim 1 — KL d³ and ε² + O(h)](#/11-current-claim-1) | VERIFIED |
| 2 | [Claim 2 — conditional-score assumption](#/12-current-claim-2) | VERIFIED |
| 3 | [Claim 3 — nonuniform schedule and observed first hits](#/13-current-claim-3) | VERIFIED |
| 4 | [Claim 4 — Wasserstein ε + O(√h d³/²)](#/14-current-claim-4) | VERIFIED |
| 5 | [Claim 5 — arbitrary product-coupling identities](#/15-current-claim-5) | VERIFIED |
| 6 | [Claim 6 — general integration by parts](#/16-current-claim-6) | VERIFIED |

Direct file links for evaluators that do not use the hash router:
[execution](10-current-execution/page.md),
[claim 1](11-current-claim-1/page.md),
[claim 2](12-current-claim-2/page.md),
[claim 3](13-current-claim-3/page.md),
[claim 4](14-current-claim-4/page.md),
[claim 5](15-current-claim-5/page.md), and
[claim 6](16-current-claim-6/page.md).

The six-row [visibility matrix](../evidence/evaluator_visibility_matrix.csv)
records whether code, inline data, raw data, checker, control, and exact claim
are discoverable from these pages.

The [primary-source claim and quantifier audit](../evidence/source/current-paper-claims.md)
links the exact ar5iv theorem anchors, assumptions H1–H8, retrieval metadata,
and response SHA-256.

## Historical rejected baseline

These preserved pages are provenance only and are not the current verifier:
[overview](#/overview), [claims](#/claims), [ImportError evidence](#/evidence),
[obsolete 3D run](#/verification-run), [obsolete conclusion](#/conclusion),
[older contract results](#/claim-contract-results),
[older release evidence](#/release-evidence), and
[older release manifest](#/release-manifest).
