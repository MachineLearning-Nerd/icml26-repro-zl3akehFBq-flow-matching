# 2026 claim-contract results

This additive page records the new source-faithful reproduction candidate. It
does not replace or reinterpret the five original pages. In particular, the
ImportError on the original **Evidence** page and the successful output on the
original **Verification run** page remain preserved as judged evidence.

The results below are local assessments. This candidate has not been published
or evaluated by the live judge, so no score increase is claimed.

| Claim | Exact contract | Observed evidence | Verdict |
| --- | --- | --- | --- |
| 1 — Theorem 1 | `ε² + O(h)`, explicit `O(d³)` factor, and cited `O(d⁴)` comparison | 252 exact Gaussian rows; normalized symbolic limits are `5` for current/`d³` and `6` for prior/`d⁴`; every refinement and ε² check passes | **VERIFIED** |
| 2 — Theorem 2 | H4 without H3 under positive early stopping, retaining `O(d³)` | 648 rows for `N(0,I_d) ⊗ δ₀`; singular full joint makes H3 false, conditional Gaussian makes H4 true | **VERIFIED** |
| 3 — Theorem 3 | Exact implicit schedule and faster displayed-bound complexity | 80 schedule rows and 36 work rows; recurrence residual at most `5.6e-17`; `log(1/δ)` replaces `δ⁻⁴` at matched tolerance | **VERIFIED** |
| 4 — Theorem 4 | `ε + O(√h)O(√d³)` in W₂ under H3/H6/H7 | 1,008 correlated-Gaussian rows; all assumptions certified; independent matrix formula differs by at most `6.31e-16` | **VERIFIED** |
| 5 — Corollary 3 | Independent product coupling with assumptions on marginals | 280 unequal-marginal rows; zero cross-covariance and every Lemma 1 block relation checked | **VERIFIED** |
| 6 — Section 5 mechanism | Integration by parts changes kernel derivative order `3→2` and supports `d⁴→d³` | 27 nonzero identities; maximum numerical residual `2.22e-16`; symbolic degree and dimension factors independently checked | **VERIFIED** |

All 18 adversarial negative controls are rejected. A contract failure, checker
failure, or accepted negative control terminates the verifier with a nonzero
exit code.

The exact fixed command is:

```bash
uv sync --frozen && uv run --frozen python repro/src/verify_fm.py
```

The cumulative scientific run used an 8-logical-core Apple CPU, no GPU or
remote compute, and cost $0. It took 1m10s end to end (56.1s inside the
verifier).

These are exact solvable specializations and a direct mechanism check. They do
not estimate hidden comparison constants, claim tightness, or formalize the
full proofs in a proof assistant.
