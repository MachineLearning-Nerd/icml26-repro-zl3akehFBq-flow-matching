# CURRENT Claim 3 — executed theorem schedule and work comparison

The paper's claim is a displayed-bound/complexity improvement, not a promise
that every arbitrary equal-count grid has smaller realized KL. The preserved
legacy run used an unrelated schedule and observed `0.0452 > 0.0042`; the
current verifier explicitly rejects that result as evidence.

The executed schedule uses `h=1/(2M)` until `t_M=1/2`. Afterwards it solves
the paper's implicit equation:

```python
next_t = (t + h) / (1 + h)
h_k = next_t - t
assert h_k == h * min(next_t, 1-next_t)
```

Thus `1-t_{M+j}=(1/2)(1+h)^(-j)`. Across 80 rows the maximum schedule
identity residual is `1.60e-16`.

## Executed endpoint and work rows

For `d=256, δ≈0.03125`:

| M | total steps | achieved δ | exact early-stopped KL | max schedule residual |
| ---: | ---: | ---: | ---: | ---: |
| 8 | 54 | 0.0307496 | 0.2315460 | 1.60e-16 |
| 128 | 839 | 0.0312705 | 0.0009718 | 5.55e-17 |

The code separately solves the displayed Theorem 2 and Theorem 3 bounds for
the smallest integer work at the same normalized tolerance `0.05d³`:

| d | δ | uniform work | non-uniform work | uniform/non-uniform |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 2^-5 | 23,485,259 | 1,595 | 14,724.3 |
| 1 | 2^-10 | 22,461,535,217,657 | 3,478 | 6.458e9 |
| 256 | 2^-5 | 23,485,055 | 524 | 44,818.8 |
| 256 | 2^-10 | 22,461,535,217,469 | 1,487 | 1.511e10 |

This directly exposes the source change from `δ⁻⁴` to `log(1/δ)`. The work
advantage is greater than one for every `δ≤2^-5` and grows monotonically as
δ decreases. SymPy independently returns the normalized dimension limit
`2-log(δ)`, which is finite in `d`, hence the displayed factor is `O(d³)`.

Controls using the old arbitrary `KL<0.5` rule, relabeling constant steps, or
restoring `δ⁻⁴` are rejected.

