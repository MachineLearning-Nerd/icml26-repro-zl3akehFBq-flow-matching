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

## Evaluator evidence map

**Exact claim and quantifiers.** Under H2, H5–H7, Theorem 4 universally bounds
`W₂` by `Cε + √h(h^(1/16)+1)√((d²+S₈⁴)d)`, hence drift error linear in `ε`
and discretization `O(√h)O(√d³)` under the stated score scaling.

**Assumption audit.** Every correlated Gaussian row numerically records H6
weak log-concavity, positive C2 density, L2 score-Hessian integrability (H7),
finite moments, and the exact H5 drift sum.

**Raw numerical results.** Six representative refinements and the linear
drift split are inline; all 1,008 rows are linked below.

**Independent checker.** A separate matrix-square-root W2 implementation
agrees to `6.31e-16`. **Negative control.** Missing H5, unaudited H6, and the
vacuous old `W₂<10` check are rejected; acceptance exits **nonzero**.

**Limitations and deviations.** Gaussian results are scoped corroboration.
The symbolic certificate establishes the universal rate/decomposition
consequence of the displayed inequality, not a proof-assistant formalization
of its stochastic derivation.

**Git SHA:** `6915a6b848e070fc2497b46fc64d9011622023eb`.
**CPU/runtime:** Apple arm64, 8 logical CPUs, 35.957 verifier seconds, no GPU,
no stochastic seeds. **Fixed command:**
`uv sync --frozen && uv run --frozen python repro/src/verify_fm.py`.

**Executable source and evidence:** [verifier](../../repro/src/verify_fm.py),
[certificate code](../../repro/src/proof_certificates.py),
[pyproject](../../pyproject.toml), [uv.lock](../../uv.lock),
[claim contract](../../evidence/claim_4/claim_contract.json),
[source audit](../../evidence/claim_4/source_audit.md),
[method](../../evidence/claim_4/method.md),
[raw CSV](../../evidence/claim_4/raw_results.csv),
[checker output](../../evidence/claim_4/independent_checker_output.json),
[negative-control output](../../evidence/claim_4/negative_control_output.json),
[universal certificate](../../evidence/claim_4/universal_certificate.json),
[runtime](../../evidence/claim_4/runtime.json),
[evaluation](../../evidence/claim_4/EVAL.md), and
[limitations](../../evidence/claim_4/limitations.md).
