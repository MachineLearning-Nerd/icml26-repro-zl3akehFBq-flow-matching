# Claim 4 method

Use a centered Gaussian endpoint coupling with standard marginals and
cross-covariance `rho I_d`, `0<=rho<1`. Its precision matrix is the Hessian of
the negative log density. Thus H6 holds strongly with
`alpha_pi=1/(1+rho)`, `M_pi=0`, while H7 has finite operator norm
`1/(1-rho)`. H3 and H2 also hold.

The Brownian-bridge marginal covariance is
`[1+2 rho t(1-t)]I_d`, and the mimicking drift is linear. Uniform Euler with
an added constant vector `q`, `||q||=epsilon`, therefore remains Gaussian.
Its mean and covariance are propagated exactly and

`W2^2 = ||mean||^2 + d(1-sqrt(variance))^2`.

The H5 sum is exactly `epsilon`. A separate implementation using
`scipy.linalg.sqrtm` checks the full Gaussian matrix formula. The joint-score
eighth moment is derived from traces of the precision matrix, and SymPy checks
the asymptotic square-root dimension factor.
