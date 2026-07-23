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

