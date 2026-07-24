# Claim 3 source audit

Theorem 3 (`#Thmtheorem3`) fixes `0<delta<1/2`. It specifies
`h=1/(2M_h)`, constant steps through time `1/2`, then the implicit rule
`h_k=h min(t_k,1-t_k)`. Its bound contains

`epsilon^2 + h d^3 log(1/delta) + h(h^(1/8)+1)(d^2+||grad log pi_{0|1}||_L8^4)d`.

Equation (23) states `M_h` proportional to the bracketed coefficient divided
by `2 epsilon^2`, with `N=2M_h log(1/delta)`.

The acceleration is therefore a bound/complexity statement about endpoint
dependence. It is not a claim that an arbitrary non-uniform grid must have
lower empirical KL than a uniform grid with the same ad hoc number of steps.
