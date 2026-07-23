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

