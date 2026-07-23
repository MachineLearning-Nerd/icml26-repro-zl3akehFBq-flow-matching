# Claim 3 limitations and deviations

- “Faster” is evaluated according to the paper's displayed upper-bound
  complexity, not asserted as pointwise dominance at equal arbitrary steps.
- Integer second-phase lengths approximate requested `delta`; achieved
  endpoints and relative errors are recorded.
- Hidden theorem constants are unavailable. The comparison uses the explicit
  displayed terms with common multiplicative constant and matched tolerance.
- Exact KL diagnostics use the solvable Claim 2 witness.
