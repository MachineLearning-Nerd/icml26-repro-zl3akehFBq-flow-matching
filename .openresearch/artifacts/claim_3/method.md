# Claim 3 method

After the first `M` constant steps, `t_M=1/2`. In the second phase,
`h_k=h(1-t_k)` and `t_k=t_{k-1}+h_k`, so

`t_k=(t_{k-1}+h)/(1+h)` and
`1-t_{M+j}=(1/2)(1+h)^(-j)`.

The implementation solves this implicit rule exactly and records the residual
for every step. It propagates the same singular-target Gaussian witness from
Claim 2, whose linear drift makes endpoint KL exact.

For the claim of acceleration, the checker solves the displayed Theorem 2 and
Theorem 3 inequalities for their smallest admissible integer grid sizes at a
matched normalized tolerance. This directly compares `delta^-4` with
`log(1/delta)` rather than using an arbitrary threshold. SymPy independently
checks cubic dimensional order.
