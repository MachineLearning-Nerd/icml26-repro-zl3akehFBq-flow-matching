# Claim 1 method

For the independent coupling `pi=N(0,I_d) tensor N(0,I_d)`, the Brownian
bridge interpolant has stationary standard-Gaussian marginals and mimicking
drift `beta(t,x)=-x`. Euler-Maruyama with approximate drift
`s(t,x)=-x+q`, `||q||=epsilon`, therefore has an exact Gaussian endpoint:

`X_N ~ N((1-(1-h)^N)q, v_N I_d)`,

where

`v_N=(1-h)^(2N)+2h(1-(1-h)^(2N))/(1-(1-h)^2)`.

The verifier evaluates `KL(N(0,I_d) || Law(X_N))` in closed form. This removes
Monte Carlo error and makes the H1 identity and epsilon-squared decomposition
exactly checkable.

For the current bound, the joint score is standard Gaussian in `2d`
dimensions, so
`||grad log pi||_L8^4=sqrt((2d)(2d+2)(2d+4)(2d+6))`.
The resulting factor is
`d[d^2+sqrt((2d)(2d+2)(2d+4)(2d+6))]`.

For the prior bound, every independent-Gaussian marginal or score eighth
moment equals `d(d+2)(d+4)(d+6)`, including the tilted-coupling score term.
Its specialized factor is `d^4+5d(d+2)(d+4)(d+6)`.

SymPy independently takes the asymptotic limits. Three deliberately corrupted
checks—removing the outer dimension, omitting drift error, and inferring a
dimension exponent from one dimension—must all be rejected.
