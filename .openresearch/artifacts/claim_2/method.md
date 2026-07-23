# Claim 2 method

Take the independent coupling
`pi=N(0,I_d) tensor point-mass(0)`. Its full joint is singular, so H3 fails.
Its conditional coupling is exactly `N(0,I_d)`, so H4 holds. Both marginals
have finite eighth moments.

At time `t<1`, the Brownian bridge marginal is
`N(0,(1-t^2)I_d)` and the mimicking drift is
`beta_t(x)=-x/(1-t)`. Uniform Euler-Maruyama is linear Gaussian, allowing
exact recurrence of its mean and scalar covariance until `t=1-delta`.
The KL direction is the theorem's
`KL(exact early-stopped marginal || Euler marginal)`.

The conditional Gaussian score gives
`||grad log pi_{0|1}||_L8^4=sqrt(d(d+2)(d+4)(d+6))`.
SymPy checks that the full displayed factor divided by `d^3` tends to
`delta^(-4)+1`. A separate 50-digit Decimal recurrence cross-checks the
floating-point implementation.
