# Claim 6 method

The core boundary-free identity is tested directly. For the heat kernel
`K_s(x|u)` and a smooth Gaussian coupling density `pi(u)`,

`integral (partial_u^3 K_s) pi du
 = - integral (partial_u^2 K_s) (partial_u log pi) pi du`.

The left side directly differentiates the kernel three times. The right side
has only a second kernel derivative and one coupling score—the transfer
described in Section 5 and used in the appendix.

Three non-symmetric parameter settings keep every integral nonzero. SciPy
adaptive quadrature evaluates both sides, while the third derivative of the
Gaussian convolution supplies an independent analytic value. SymPy separately
checks that the kernel derivative polynomial degree changes from three to two.

Across dimensions 1 through 256, the run also records the exact current
`d(d^2+score^4)` factor and prior `d^4+5m_8(d)` specialization. Their symbolic
normalized limits are 5 and 6 respectively.
