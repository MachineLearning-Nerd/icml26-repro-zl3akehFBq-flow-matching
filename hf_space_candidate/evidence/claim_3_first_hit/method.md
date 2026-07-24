# Claim 3 method

After the first `M` constant steps, `t_M=1/2`. In the second phase,
`h_k=h(1-t_k)` and `t_k=t_{k-1}+h_k`, so

`t_k=(t_{k-1}+h)/(1+h)` and
`1-t_{M+j}=(1/2)(1+h)^(-j)`.

The implementation solves this implicit rule exactly and records the residual
for every step. It propagates the same singular-target Gaussian witness from
Claim 2, whose linear drift makes endpoint KL exact.

For the claim of acceleration, the primary checker independently doubles and
binary-searches the minimum integer resources for which exact propagated
Euler KL reaches a fixed target. It records the immediately preceding KL and
requires that value to miss, so the first-hit claim is machine checked.
Neither resource budget comes from the theorem formula. The 18 cases cover
three dimensions, three horizons, and two tolerances.

The displayed Theorem 2/Theorem 3 bound comparison remains in
`raw_complexity.csv` only as secondary source-context. SymPy independently
checks the schedule recurrence and cubic dimensional rate consequence.
