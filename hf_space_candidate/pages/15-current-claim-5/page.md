# CURRENT Claim 5 — executed independent product specialization

The current code does not reuse Claim 1. It constructs unequal marginals

`μ=N(0,σ₀²I_d)`, `ν*=N(m,σ₁²I_d)`, `||m||=1`,

then explicitly forms `π=μ⊗ν*`. Every one of 280 rows records zero
cross-covariance and `independent_factorization=True`.

Each marginal is checked separately for H8:

- positive `C∞` density and finite L8 Gaussian score;
- constant score Hessian with norms `σ₀^-2` and `σ₁^-2`;
- strong log-concavity `α=σ^-2`, `M=0`.

The product checker then verifies Lemma 1:

```text
log π(x0,x1) = log μ(x0) + log ν*(x1)
Hessian(log π) = diag(Hessian(log μ), Hessian(log ν*))
α_π = min(α_μ, α_ν*)
M_π = 2 max(M_μ, M_ν*) = 0
```

## Literal product-coupling rows

For `d=256, σ₀=.75, σ₁=2, ε=0`:

| N | cross covariance | W₂ | source Hessian | target Hessian | joint α | H8 source/target |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 8 | 0 | 1.6477281 | 1.7778 | 0.25 | 0.25 | true / true |
| 512 | 0 | 0.0268383 | 1.7778 | 0.25 | 0.25 | true / true |

All four unequal variance pairs refine monotonically in dimensions
`1,4,16,64,256`. An independent `scipy.linalg.sqrtm` matrix calculation
differs by `6.94e-17`.

The `ρ=.5` correlated-joint control is rejected because nonzero
cross-covariance violates `π=μ⊗ν*`. Reusing a KL metric and asserting
marginal conditions without the block-joint check are also rejected.

## Evaluator evidence map

**Exact claim and quantifiers.** Corollary 3 applies Theorem 4 to every
independent coupling `π=μ⊗ν*` whose marginals satisfy H8, replacing joint
assumptions by the stated marginal conditions.

**Assumption audit.** The numerical unequal-Gaussian rows record both H8
marginals and zero cross-covariance. The general certificate differentiates
`log μ(x)+log ν(y)` pointwise for arbitrary positive C2 marginals, proving the
score, block-Hessian, zero mixed block, and weak-concavity transfers.

**Raw numerical results.** Two refinements and every assumption field are
inline; all 280 rows are linked below.

**Independent checker.** A separate full-matrix W2 calculation agrees within
`6.94e-17`. **Negative control.** Correlated coupling, KL substitution, and an
unaudited block identity are rejected; acceptance exits **nonzero**.

**Limitations and deviations.** The product-calculus certificate covers the
general specialization identities; the endpoint W2 calculation remains
Gaussian corroboration and relies on Theorem 4 for the general dynamics.

**Git SHA:** `4d6a75b59e359f03b8836d1e7488910eda66b84a`.
**CPU/runtime:** Apple arm64, 8 logical CPUs, 29.645 verifier seconds, no GPU,
no stochastic seeds. **Fixed command:**
`uv sync --frozen && uv run --frozen python repro/src/verify_fm.py`.

**Executable source and evidence:** [verifier](../../repro/src/verify_fm.py),
[certificate code](../../repro/src/proof_certificates.py),
[pyproject](../../pyproject.toml), [uv.lock](../../uv.lock),
[claim contract](../../evidence/current/claim_5/claim_contract.json),
[source audit](../../evidence/current/claim_5/source_audit.md),
[method](../../evidence/current/claim_5/method.md),
[raw CSV](../../evidence/current/claim_5/raw_results.csv),
[checker output](../../evidence/current/claim_5/independent_checker_output.json),
[negative-control output](../../evidence/current/claim_5/negative_control_output.json),
[universal certificate](../../evidence/current/claim_5/universal_certificate.json),
[runtime](../../evidence/current/claim_5/runtime.json),
[evaluation](../../evidence/current/claim_5/EVAL.md), and
[limitations](../../evidence/current/claim_5/limitations.md).
