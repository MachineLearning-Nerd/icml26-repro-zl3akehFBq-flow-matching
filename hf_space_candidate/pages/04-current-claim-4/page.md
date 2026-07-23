# CURRENT Claim 4 — executed Wasserstein decomposition

The executed joint is a correlated standard Gaussian with
`Cov(X₀,X₁)=ρI_d`, for `ρ∈{0,.25,.5,.75}`. It has a positive smooth density
(H3), weak-log-concavity constants
`α_π=1/(1+|ρ|)>0, M_π=0` (H6), and finite score-Hessian operator norm
`1/(1-|ρ|)` (H7). These constants are recorded in every row.

The approximate drift adds a vector of norm `ε`; therefore the H5 sum is
exactly `ε`. Exact Gaussian propagation records

`W₂² = mean_component² + d(1-sqrt(variance))²`.

## Literal refinement rows for ρ=0.5 and ε=0

| d | N | h | covariance W₂ | total W₂ | α_π | Hessian norm |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 8 | 0.125 | 0.0589736 | 0.0589736 | 0.6667 | 2 |
| 1 | 512 | 0.001953125 | 0.000889819 | 0.000889819 | 0.6667 | 2 |
| 64 | 8 | 0.125 | 0.471789 | 0.471789 | 0.6667 | 2 |
| 64 | 512 | 0.001953125 | 0.00711855 | 0.00711855 | 0.6667 | 2 |
| 256 | 8 | 0.125 | 0.943577 | 0.943577 | 0.6667 | 2 |
| 256 | 512 | 0.001953125 | 0.0142371 | 0.0142371 | 0.6667 | 2 |

At `d=16,N=64,ρ=.5`, `ε=[0,.02,.04,.08]` produces mean components
`[0,.0125225,.0250450,.0500900]`, exactly linear in ε, while the covariance
component stays `0.0285959`. This separately exposes drift and
discretization contributions rather than testing `W₂<10`.

The run contains 1,008 rows and refinement succeeds for every dimension and
ρ. A separate `scipy.linalg.sqrtm` matrix implementation differs from the
analytic W₂ by `6.31e-16`. SymPy verifies the displayed dimension term
divided by `d^(3/2)` has a finite nonzero limit. Controls omitting H5,
leaving weak log-concavity uncertified, or using the old loose threshold are
rejected.

