# CURRENT Claim 3 — exact schedule and observed first-hit work

The rejected baseline compared arbitrary grids at one count and observed the
purported nonuniform method was ten times worse. This replacement implements
the theorem schedule exactly and measures minimum resources from achieved KL,
not from the claimed complexity formula.

This is an observed first-hit **work comparison**, not a formula-generated
budget plot.

## Exact claim and quantifiers

For `0<δ<1/2`, Theorem 3 uses `h_k=h` until `t=1/2`, then
`h_k=h min(t_k,1-t_k)`. Under H1, H2, and H4 its displayed early-stopped bound
has `h d³ log(1/δ)` endpoint dependence while retaining `O(d³)` dimension
order.

## Assumption audit and executable schedule

The same strict `π=N(0,I_d)⊗δ₀` witness as Claim 2 satisfies H2/H4 but not H3.
For `h=1/(2M)`, the executed later update solves the implicit step equation:

```python
next_t = (t + h) / (1 + h)
step = next_t - t
assert step == h * min(next_t, 1-next_t)
```

Consequently `1-t_(M+j)=(1/2)(1+h)^(-j)`. Across 80 schedule rows the maximum
identity residual is `1.60e-16`.

## Raw numerical results — independent first-hit search

For each `(d,δ,tolerance)`, the code doubles and binary-searches the smallest
integer resource whose **exact propagated Euler KL** reaches the target. It
also verifies the immediately preceding resource misses. Neither budget is
selected from the theorem formula.

Representative `d=256` rows:

| δ | KL target/d | uniform first hit | uniform previous/hit KL | nonuniform M / total work | nonuniform previous/hit KL | work ratio |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.125 | 1e-3 | 58 | 0.264504 / 0.255500 | 8 / 31 | 0.304121 / 0.234812 | 1.871 |
| 0.03125 | 1e-3 | 249 | 0.256453 / 0.254405 | 8 / 54 | 0.299274 / 0.231546 | 4.611 |
| 0.0078125 | 1e-3 | 1007 | 0.256125 / 0.255618 | 8 / 77 | 0.298132 / 0.230786 | 13.078 |
| 0.0078125 | 1e-4 | 3187 | 0.0256102 / 0.0255941 | 25 / 235 | 0.0270340 / 0.0249414 | 13.562 |

All 18 rows span `d={1,16,256}`, three horizons, and two tolerances. Every
nonuniform first hit uses less work; ratios range from `1.87` to `13.56` and
increase as the endpoint is approached.

## Independent checker and Negative control

The symbolic recurrence independently gives
`1-t_(M+j)=(1/2)(1+h)^(-j)` and
`j=O(h^-1 log(1/δ))`. With conditional score fourth-power `O(d²)`, normalization
of every displayed dimension term by `d³` is finite. The old arbitrary
`KL<0.5` rule, a constant step mislabeled nonuniform, and replacement of the
log term by `δ^-4` are rejected. Any accepted control makes the verifier exit
**nonzero**.

## Limitations and deviations

The first-hit measurements are exact for one assumption-satisfying bridge
family and are scoped corroboration, not a universal proof. The symbolic
certificate covers the schedule solution and rate consequence of the paper's
displayed inequality. Formula-selected work remains in `raw_complexity.csv`
only as secondary source-context and is not the primary verification result.

**Git SHA:** `4d6a75b59e359f03b8836d1e7488910eda66b84a`.
**CPU/runtime:** Apple arm64, 8 logical CPUs, 29.645 verifier seconds, no GPU,
no stochastic seeds. **Fixed command:**
`uv sync --frozen && uv run --frozen python repro/src/verify_fm.py`.

**Executable source and evidence:** [verifier](../../repro/src/verify_fm.py),
[certificate code](../../repro/src/proof_certificates.py),
[pyproject](../../pyproject.toml), [uv.lock](../../uv.lock),
[claim contract](../../evidence/current/claim_3/claim_contract.json),
[source audit](../../evidence/current/claim_3/source_audit.md),
[method](../../evidence/current/claim_3/method.md),
[observed first-hit CSV](../../evidence/current/claim_3/raw_first_hit.csv),
[schedule CSV](../../evidence/current/claim_3/raw_schedule.csv),
[secondary bound-context CSV](../../evidence/current/claim_3/raw_complexity.csv),
[checker output](../../evidence/current/claim_3/independent_checker_output.json),
[negative-control output](../../evidence/current/claim_3/negative_control_output.json),
[universal certificate](../../evidence/current/claim_3/universal_certificate.json),
[runtime](../../evidence/current/claim_3/runtime.json),
[evaluation](../../evidence/current/claim_3/EVAL.md), and
[limitations](../../evidence/current/claim_3/limitations.md).
