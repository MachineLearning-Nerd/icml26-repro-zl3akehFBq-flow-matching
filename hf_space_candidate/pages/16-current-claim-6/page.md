# CURRENT Claim 6 — executed integration-by-parts mechanism

The current experiment directly evaluates the derivative transfer described
in Section 5 and equations (178)–(184). For a heat kernel `K_s(x|u)` and
smooth Gaussian coupling density `π(u)`, it computes both nonzero sides:

`∫ (∂_u³ K_s) π du = -∫ (∂_u² K_s)(∂_u log π)π du`.

This is the mechanism: direct third-order kernel differentiation becomes a
second-order kernel derivative plus one derivative on the coupling.

## Literal quadrature rows

For `s=.1, x=.7, coupling mean=-.3, σ=1.2`:

| d | direct third derivative | transferred second derivative × score | analytic convolution derivative | residual |
| ---: | ---: | ---: | ---: | ---: |
| 1 | -0.20409661902112286 | -0.20409661902112308 | -0.20409661902112300 | 2.22e-16 |
| 64 | -0.20409661902112286 | -0.20409661902112308 | -0.20409661902112300 | 2.22e-16 |
| 256 | -0.20409661902112286 | -0.20409661902112308 | -0.20409661902112300 | 2.22e-16 |

Three asymmetric parameter settings ensure the integral is never vacuously
zero. Adaptive quadrature, a separately derived Gaussian-convolution
derivative, and SymPy all agree.

SymPy reports:

```text
third kernel derivative ratio:
  (6*s-(u-x)^2)*(u-x)/(8*s^3)       polynomial degree 3
second kernel derivative ratio:
  (-2*s+(u-x)^2)/(4*s^2)            polynomial degree 2
coupling score:
  (mean-u)/sigma^2                   one transferred derivative
```

The executed tensor counts are `d³` index triplets after transfer, versus the
recorded prior `d⁴` leading monomial. The same source factors independently
normalize to current/d³ `→5` and prior/d⁴ `→6`.

Flipping the integration-by-parts sign, omitting the coupling score, or
substituting the legacy low-rank gradient identity all produce rejected
controls.

## Evaluator evidence map

**Exact claim and quantifiers.** For every smooth kernel/coupling term with a
vanishing boundary contribution, integration by parts transfers one of three
kernel derivatives to the coupling score, leaving a second kernel derivative.
The paper uses this to replace the prior three-log-derivative expansion and
obtain its `d³` rather than `d⁴` explicit factor.

**Assumption audit.** The certificate states positive C2 coupling density,
C3 kernel, integrability, and vanishing boundary term. Gaussian quadrature
audits these numerically with nonzero asymmetric integrals.

**Raw numerical results.** Representative direct, transferred, and analytic
values are inline; all 27 rows are linked below.

**Independent checker.** General symbolic product differentiation yields
`∂[(∂²K)π]=(∂³K)π+(∂²K)(∂π)`. **Negative control.** Sign flip, missing score,
and the unrelated low-rank identity are rejected; acceptance exits
**nonzero**.

**Limitations and deviations.** The universal IBP identity and derivative
orders are certified. The certificate does not mechanically reproduce every
surrounding stochastic estimate in the paper's proof.

**Git SHA:** `4d6a75b59e359f03b8836d1e7488910eda66b84a`.
**CPU/runtime:** Apple arm64, 8 logical CPUs, 29.645 verifier seconds, no GPU,
no stochastic seeds. **Fixed command:**
`uv sync --frozen && uv run --frozen python repro/src/verify_fm.py`.

**Executable source and evidence:** [verifier](../../repro/src/verify_fm.py),
[certificate code](../../repro/src/proof_certificates.py),
[pyproject](../../pyproject.toml), [uv.lock](../../uv.lock),
[claim contract](../../evidence/current/claim_6/claim_contract.json),
[source audit](../../evidence/current/claim_6/source_audit.md),
[method](../../evidence/current/claim_6/method.md),
[raw CSV](../../evidence/current/claim_6/raw_results.csv),
[checker output](../../evidence/current/claim_6/independent_checker_output.json),
[negative-control output](../../evidence/current/claim_6/negative_control_output.json),
[universal certificate](../../evidence/current/claim_6/universal_certificate.json),
[runtime](../../evidence/current/claim_6/runtime.json),
[evaluation](../../evidence/current/claim_6/EVAL.md), and
[limitations](../../evidence/current/claim_6/limitations.md).
