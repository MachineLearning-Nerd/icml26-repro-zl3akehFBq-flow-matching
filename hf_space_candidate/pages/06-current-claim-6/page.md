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

