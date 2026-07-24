# Claim 1 limitations and deviations

- The experiment uses an analytically solvable independent-Gaussian family;
  it does not numerically cover every coupling allowed by H1-H3.
- The theorem states an upper bound. In this specialization the actual Euler
  KL discretization error decreases faster than the allowed order, so the run
  verifies compatibility and decomposition rather than tightness.
- The asymptotic exponents are derived from the exact displayed factors, not
  estimated from noisy finite-dimensional regression.
- No stochastic seeds are needed because all endpoint quantities are computed
  in closed form.
