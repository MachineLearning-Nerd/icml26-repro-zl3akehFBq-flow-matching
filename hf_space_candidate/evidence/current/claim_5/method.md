# Claim 5 method

Let `mu=N(0,sigma_0^2 I_d)` and
`nu*=N(m,sigma_1^2 I_d)`, with `||m||=1`, and form their product joint.
Four unequal variance pairs ensure this is distinct from the stationary
standard-Gaussian test.

Each marginal is strongly log-concave with `alpha=sigma^-2`, `M=0`; its score
and Hessian norms are analytic. Product factorization gives a block score and
block-diagonal Hessian. The implementation evaluates the joint eighth moment
from precision-matrix traces and checks the Lemma 1 inequalities and constants.

The Brownian-bridge marginal and mimicking drift are affine Gaussian. Euler
mean and covariance are propagated exactly, and W2 to the unequal target is
computed in closed form. `scipy.linalg.sqrtm` independently evaluates the
matrix Gaussian formula.
