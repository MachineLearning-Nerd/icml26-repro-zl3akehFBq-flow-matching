# CURRENT Claim 2 — executed strict H4-without-H3 witness

This is not `c2 = c1`. The executed coupling is

`π = N(0,I_d) ⊗ δ₀`.

Its support `R^d×{0}` has zero `2d`-dimensional Lebesgue measure, so the full
joint has no positive density and **H3 is false**. Conditional on `X₁=0`,
`π_{0|1}=N(0,I_d)`, whose positive smooth density has an L8 Gaussian score,
so **H4 is true**. H2 also holds. This strictly distinguishes Theorem 2's
assumptions from Theorem 1's.

For `t≤1-δ`, the exact bridge marginal is
`N(0,(1-t²)I_d)`. The executed Euler recurrence is:

```python
variance = 1.0
for k in range(round((1-delta)*steps)):
    t = k / steps
    a = 1 - (1/steps) / (1-t)
    variance = a*a*variance + 2/steps
```

## Literal raw rows

At `d=256, δ=0.125, ε=0`:

| N | h | exact target variance | Euler variance | KL | H3 | H4 |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 16 | 0.0625 | 0.234375 | 0.3058451417 | 4.1568883423 | false | true |
| 512 | 0.001953125 | 0.234375 | 0.2363077596 | 0.0043048285 | false | true |

The full run contains 648 rows over `d=1…256`, four strictly positive
early-stopping values, six grids, and three drift errors. KL decreases under
every refinement.

The independent checker used a separate 50-digit Decimal recurrence:
`0.24222774541289898660868642617553026795713500843924`, versus the floating
implementation `0.24222774541289904`, absolute difference `5.55e-17`.
SymPy returned
`theorem_factor/d³ → 1+δ⁻⁴`.

Controls setting `δ=0`, pretending the singular joint satisfies H3, or
replacing the conditional score by a nonexistent full-joint score all exit
through rejection.

## Evaluator evidence map

**Exact claim and quantifiers.** For all `0<δ<1/2` under H1, H2, and H4,
Theorem 2 replaces the full-joint score assumption by conditional-score
integrability and retains fixed-δ `O(d³)` dimension order under early stopping.

**Assumption audit.** The executed `N(0,I_d)⊗δ₀` witness has finite H2
moments and smooth conditional Gaussian score (H4), while its joint support
has zero Lebesgue measure, so H3 is genuinely false rather than assumed.

**Raw numerical results.** Two representative rows and the strict H3/H4
audit are inline above; all 648 rows are linked below.

**Independent checker.** A 50-digit Decimal recurrence agrees to `5.55e-17`
and symbolic normalization gives `1+δ⁻⁴`. **Negative control.** `δ=0`, a
fabricated full-joint density, and substitution of the nonexistent joint score
are rejected. Any acceptance exits **nonzero**.

**Limitations and deviations.** The singular witness proves the relaxation is
strict and gives exact-family corroboration; it does not alone prove the
universal stochastic inequality. The certificate covers the displayed rate
and assumption logic.

**Git SHA:** `6915a6b848e070fc2497b46fc64d9011622023eb`.
**CPU/runtime:** Apple arm64, 8 logical CPUs, 35.957 verifier seconds, no GPU,
no stochastic seeds. **Fixed command:**
`uv sync --frozen && uv run --frozen python repro/src/verify_fm.py`.

**Executable source and evidence:** [verifier](../../repro/src/verify_fm.py),
[certificate code](../../repro/src/proof_certificates.py),
[pyproject](../../pyproject.toml), [uv.lock](../../uv.lock),
[claim contract](../../evidence/claim_2/claim_contract.json),
[source audit](../../evidence/claim_2/source_audit.md),
[method](../../evidence/claim_2/method.md),
[raw CSV](../../evidence/claim_2/raw_results.csv),
[checker output](../../evidence/claim_2/independent_checker_output.json),
[negative-control output](../../evidence/claim_2/negative_control_output.json),
[universal certificate](../../evidence/claim_2/universal_certificate.json),
[runtime](../../evidence/claim_2/runtime.json),
[evaluation](../../evidence/claim_2/EVAL.md), and
[limitations](../../evidence/claim_2/limitations.md).
