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

