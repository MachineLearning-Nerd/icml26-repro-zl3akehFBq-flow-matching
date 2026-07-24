# Claim 4 source audit

Theorem 4 (`#Thmtheorem4`) assumes H5, H2, H3, H6, and H7 on a uniform
`h=1/N` grid. Its displayed result is

`W2(nu*,nu_1^theta) <= C [epsilon + sqrt(h)(h^(1/16)+1)sqrt((d^2+||grad log pi||_L8^4)d)]`.

H5 (`#Thmassumption5`) sums step length times the root mean squared drift
error along the generated process. H6 (`#Thmassumption6`) requires weak
log-concavity with parameters `alpha_pi>0` and `M_pi>=0`. H7
(`#Thmassumption7`) requires a positive C2 density and finite L2 operator norm
of the score Hessian.

The paper describes the two terms as drift error `epsilon` and discretization
order `sqrt(h) sqrt(d^3)`. This contract tests both terms and the assumptions;
`W2<10` alone is not an admissible criterion.
