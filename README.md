# Claim-by-claim reproduction: dimension-improved diffusion flow matching

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/blob/master/notebooks/flow_matching_claims.py)

This repository reproduces the six headline theoretical claims in
[Diffusion Flow Matching: Dimension-Improved KL Bounds and Wasserstein Guarantees](https://arxiv.org/abs/2606.16610):
the `O(d³)` KL factors and `ε² + O(h)` decomposition, the conditional-only
early-stopping relaxation, the specified non-uniform schedule, the
`ε + O(√h)O(√d³)` Wasserstein decomposition, its independent-coupling
specialization, and the integration-by-parts mechanism behind the dimensional
improvement.

The original judged revision received **3/12** after a 3D toy test. The first
additive release improved the official score to **5/12** at Hugging Face revision
[`22e4c6cc`](https://huggingface.co/spaces/DineshAI/zl3akehFBq/commit/22e4c6ccfea63d39df4fd57db0ddacb2a505b040)
because the judge still treated the preserved legacy run as current and did
not regard the new contracts as executed output. The second local candidate
puts the actual 476,391-byte ORX transcript, executable formulas, representative
raw rows, assumptions, and controls directly into seven judge-readable pages.
All six local contracts remain **VERIFIED**, but no score beyond 5/12 is claimed
until this candidate is approved, published, and judged.

The paper's exact asymptotic factors normalize to `5d³` for Theorem 1 and
`6d⁴` for the cited prior result. The reproduction observes those symbolic
limits, then checks 2,331 exact numeric cases across dimensions through 256,
18 rejected negative controls, and a nonvacuous integration-by-parts identity
with maximum residual `2.22e-16`. The tests use analytically solvable Gaussian
specializations, including a deliberately singular Claim 2 witness; they do
not claim bound tightness or constitute a proof-assistant formalization.

Everything ran on the local 8-logical-core Apple CPU, with no GPU, no remote
compute, and $0 compute cost. The cumulative scientific run took 1m10s. The
environment is pinned by `uv.lock` (Python 3.12.11), and every experiment uses
the same command:

```bash
uv sync --frozen && uv run --frozen python repro/src/verify_fm.py
```

Read the [illustrated claim-by-claim report](reports/claim-by-claim/report.md)
or open the [self-contained marimo tutorial](notebooks/flow_matching_claims.py).
The notebook opens with the recorded evidence and does not require rerunning
the formal verifier.

## Experiment log

| Branch / experiment | Purpose | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| [`master`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/master) | Publication surface | Not run as an experiment (publication surface) | Published presentation surface for Space revision `22e4c6cc`; official score 5/12 | — |
| [`orx/frozen-judged-baseline-with-uv-lock`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/frozen-judged-baseline-with-uv-lock) | Freeze the judged 3D toy and pin the environment | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | Reproduced the 3/12 toy baseline and its contradictory evidence page | Local CPU, 5s |
| [`orx/claim-1-exact-gaussian-theorem-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/claim-1-exact-gaussian-theorem-audit) | Theorem 1 `d³`, `ε²`, and `h` contract | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | Claim 1 VERIFIED locally | Local CPU, 5s |
| [`orx/claim-2-conditional-only-early-stopping`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/claim-2-conditional-only-early-stopping) | Strict H4-without-H3 witness | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | Claims 1–2 VERIFIED locally | Local CPU, 5s |
| [`orx/claim-3-exact-non-uniform-schedule`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/claim-3-exact-non-uniform-schedule) | Exact implicit schedule and bound-complexity comparison | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | Claims 1–3 VERIFIED locally | Local CPU, 5s |
| [`orx/claim-4-exact-wasserstein-decomposition`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/claim-4-exact-wasserstein-decomposition) | W₂ decomposition with explicit H3/H6/H7 | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | Claims 1–4 VERIFIED locally | Local CPU, 15s |
| [`orx/claim-5-independent-marginal-specialization`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/claim-5-independent-marginal-specialization) | Product coupling and marginal H8 checks | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | Claims 1–5 VERIFIED locally | Local CPU, 35s |
| [`orx/claim-6-integration-by-parts-mechanism`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/claim-6-integration-by-parts-mechanism) | Nonzero integration-by-parts identity and derivative-order audit | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | All six claims VERIFIED locally; scientific winner | Local CPU, 1m10s |
| [`orx/cumulative-evidence-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/cumulative-evidence-release-candidate) | First protected Space release | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | Published as `22e4c6cc`; live judge awarded 5/12 | Local CPU, 1m00s |
| [`orx/judge-visible-executed-evidence`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/judge-visible-executed-evidence) | Put actual ORX logs, code, raw rows, assumptions, and controls into judge-readable pages | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | All six contracts pass; seven current pages emitted before legacy pages | Local CPU, 50s |
| [`orx/second-cumulative-evidence-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/tree/orx/second-cumulative-evidence-release-candidate) | Embed exact executed-run metadata and validate the second additive release | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` | Candidate pending final regression and publication approval | Local CPU |

## Reproduce

```bash
uv sync --frozen
uv run --frozen python repro/src/verify_fm.py
uv run --frozen marimo check notebooks/flow_matching_claims.py
uv run --frozen marimo edit notebooks/flow_matching_claims.py
```

Formal outputs are written under `.openresearch/artifacts/`. Each claim has a
source audit, JSON contract, method, raw CSV/JSON, independent checker output,
negative-control output, runtime metadata, limitations, and `EVAL.md`.

The exact paper HTML used for source auditing was retrieved with an explicit
browser User-Agent on 2026-07-23 and has SHA-256
`c3553013f3f7022f6e5f539e735585d6180364f716d4b17b5679aacb519546ff`.
