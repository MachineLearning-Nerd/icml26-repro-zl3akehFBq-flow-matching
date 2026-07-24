# Claim 2 source audit

Theorem 2 is at `#Thmtheorem2` in the primary HTML whose retrieval metadata is
recorded in the campaign source manifest. It fixes `0<delta<1/2`, uses a
uniform `h=1/N`, and assumes H1, H2, and H4—not H3.

H4 (`#Thmassumption4`) requires the conditional law `pi_{0|1}` of `X_0`
given `X_1` to have a strictly positive C1 density and L8-integrable score.
The paper explicitly notes that for an independent coupling,
`pi_{0|1}=mu`, so the target only needs H2.

The displayed bound is

`KL(nu*_{1-delta} || nu^theta_{1-delta}) <= C [epsilon^2 + h(h^(1/8)+1)(d^2/delta^4 + ||grad log pi_{0|1}||_L8^4)d]`.

The contract therefore requires a witness where H4 holds but H3 does not.
Reusing the smooth Gaussian joint from Claim 1 would not test relaxation.
