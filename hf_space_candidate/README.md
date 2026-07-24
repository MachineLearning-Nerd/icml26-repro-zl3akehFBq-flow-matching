---
title: "Repro - Diffusion Flow Matching: Dimension-Improved KL Bounds"
emoji: 🎯
colorFrom: yellow
colorTo: red
sdk: static
pinned: false
tags:
 - trackio
 - trackio-logbook
 - open-experiment
 - icml2026-repro
 - paper-zl3akehFBq
---

# Repro - Diffusion Flow Matching: Dimension-Improved KL Bounds

## Current verification — evaluator start here

This revision supersedes the rejected three-dimensional baseline with one
fail-closed CPU command covering all six paper claims. Start with the
[current evidence index](pages/index.md), then open each claim page. Every
page displays its important numerical output inline and directly links the
executable code, pinned environment, raw CSV, checker, negative control,
certificate, assumptions, runtime, and limitations in this same revision.
The [primary-source audit](evidence/source/current-paper-claims.md) links the
exact theorem anchors and records the retrieved HTML hash.

Fixed command:

```bash
uv sync --frozen && uv run --frozen python repro/src/verify_fm.py
```

The scientific evidence run was
`8c10975f-a2f4-4176-b678-50a2d55aa962` at Git SHA
`4d6a75b59e359f03b8836d1e7488910eda66b84a` on an 8-logical-core Apple
arm64 CPU. It completed with exit 0 in 29.645 verifier seconds. No GPU was
used. All 18 executed mutation controls were rejected; any failed
acceptance check raises and exits nonzero.

The universal theorem statements are not inferred from finite Gaussian
examples. Claims 1–4 pair exact-family corroboration with independent symbolic
rate/decomposition certificates; Claims 5–6 additionally have general
pointwise calculus/IBP certificates. Each page states the remaining proof
scope explicitly.

A strict evaluator-blind review still forecasts **6/12**, because this artifact
does not contain complete formal stochastic proofs of the universal theorems.
That limitation is explicit; local `VERIFIED` means the machine-checkable
claim contract passed, not that a live evaluator must award full credit.

## Historical rejected baseline

The old pages remain byte-for-byte available for provenance, but their
ImportError, `c2=c1`, arbitrary thresholds, and obsolete “6/6 PASS” conclusion
are not the current verifier. They are labeled **Historical rejected
baseline** in navigation. Current executable source:
[repro/src/verify_fm.py](repro/src/verify_fm.py).
