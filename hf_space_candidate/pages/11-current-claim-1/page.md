# CURRENT Claim 1 — executed KL scaling and error decomposition

The tested domain is Theorem 1's constant grid `h=1/N`, with the valid
coupling `π=N(0,I_d)⊗N(0,I_d)`. H2 and H3 hold analytically. For the exact
mimicking drift `β(t,x)=-x` and approximation `s=β+q`,
`||q||=ε`, the discrete H1 sum is exactly `ε²`.

The executable recurrence, not the legacy particle simulation, is:

```python
for _ in range(steps):
    mean = (1.0 - h) * mean + h * epsilon
variance = (1-h)**(2*steps) + 2*h*(1-(1-h)**(2*steps))/(1-(1-h)**2)
kl = 0.5 * (d/variance + mean**2/variance - d + d*log(variance))
```

## Literal raw rows from the executed CSV

With `ε=0`, refinement reduces the exact
`KL(N(0,I_d) || Euler endpoint)` in every tested dimension:

| d | N | h | KL | theorem factor | cited-prior factor |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 8 | 0.125 | 8.0069e-4 | 20.5959 | 526 |
| 1 | 512 | 0.001953125 | 1.7851e-7 | 20.5959 | 526 |
| 64 | 8 | 0.125 | 5.1244e-2 | 1,360,127.9702 | 117,308,416 |
| 64 | 512 | 0.001953125 | 1.1425e-5 | 1,360,127.9702 | 117,308,416 |
| 256 | 8 | 0.125 | 2.0498e-1 | 84,673,535.9923 | 26,790,916,096 |
| 256 | 512 | 0.001953125 | 4.5698e-5 | 84,673,535.9923 | 26,790,916,096 |

At `d=16,N=64`, the recorded H1 values for
`ε=[0,.02,.04,.08]` are `[0,.0004,.0016,.0064]` exactly. The corresponding
KL values are `[1.8464e-4,2.6475e-4,5.0505e-4,1.4663e-3]`; subtracting the
`ε=0` KL gives increments in the exact ratio `1:4:16`.

## Dimension check and independent control

The source factor evaluated by the run is

`d[d²+sqrt((2d)(2d+2)(2d+4)(2d+6))]`.

SymPy independently returned `factor/d³ → 5`. The cited prior factor
`6d⁴+60d³+220d²+240d` returned `factor/d⁴ → 6`.

The negative control that removes the outer `d` changes the order and was
rejected, as were omitting the `ε²` term and inferring an exponent from one
dimension. This evidence tests a valid exact Gaussian specialization across
dimensions 1–256; it does not claim hidden-constant tightness or universal
formal proof.

## Evaluator evidence map

**Exact claim and quantifiers.** For every coupling satisfying H1–H3 and the
stated moment regime, Theorem 1 gives the displayed uniform-grid KL upper
bound with `ε² + O(h d³)` terms; the cited prior explicit factor is `O(d⁴)`.

**Assumption audit.** H1 is exact for `s=β+q`; H2 is
`E||N(0,I_d)||⁸=d(d+2)(d+4)(d+6)`; H3 follows from the positive smooth
Gaussian product density and finite L8 score.

**Raw numerical results.** Representative values are displayed above; the
complete 252-row table is directly downloadable below.

**Independent checker.** SymPy obtains limits 5 and 6 without fitting finite
points. **Negative control.** Removing the outer `d`, omitting `ε²`, and using
one dimension are each rejected. The verifier exits **nonzero** if any is
accepted.

**Limitations and deviations.** The exact Gaussian sweep is scoped
corroboration, not a proof over all H1–H3 couplings. The universal certificate
checks the rate/decomposition consequence of the paper's displayed theorem
inequality, not the complete stochastic proof.

**Git SHA:** `6915a6b848e070fc2497b46fc64d9011622023eb`.
**CPU/runtime:** Apple arm64, 8 logical CPUs, 35.957 verifier seconds, no GPU,
no stochastic seeds. **Fixed command:**
`uv sync --frozen && uv run --frozen python repro/src/verify_fm.py`.

**Executable source and evidence:** [verifier](../../repro/src/verify_fm.py),
[certificate code](../../repro/src/proof_certificates.py),
[pyproject](../../pyproject.toml), [uv.lock](../../uv.lock),
[claim contract](../../evidence/claim_1/claim_contract.json),
[source audit](../../evidence/claim_1/source_audit.md),
[method](../../evidence/claim_1/method.md),
[raw CSV](../../evidence/claim_1/raw_results.csv),
[checker output](../../evidence/claim_1/independent_checker_output.json),
[negative-control output](../../evidence/claim_1/negative_control_output.json),
[universal certificate](../../evidence/claim_1/universal_certificate.json),
[runtime](../../evidence/claim_1/runtime.json),
[evaluation](../../evidence/claim_1/EVAL.md), and
[limitations](../../evidence/claim_1/limitations.md).
