# Claim 1 source audit

The primary source is the ar5iv HTML for arXiv 2606.16610, retrieved on
2026-07-23 with an explicit browser User-Agent. Its SHA-256 is
`c3553013f3f7022f6e5f539e735585d6180364f716d4b17b5679aacb519546ff`.

Theorem 1 is anchored at `#Thmtheorem1`. It quantifies over uniform
`h=1/N` under H1-H3, with marginal eighth moments bounded at dimension-four
order. Its displayed upper bound is

`KL(nu* || nu_1^theta) <= C [epsilon^2 + h(h^(1/8)+1)(d^2 + ||grad log pi||_L8^4)d]`.

H1 (`#Thmassumption1`) is the integrated squared drift-approximation error.
H2 (`#Thmassumption2`) requires finite marginal eighth moments. H3
(`#Thmassumption3`) requires a positive C1 joint density and an L8-integrable
joint score.

The cited prior result is Theorem 2 of arXiv 2409.08311. Its ar5iv HTML was
retrieved with the same method and has SHA-256
`7d628ac2440638c90ad11b3fd6c24d4eb9857be99457665a8c3068382d94c5b9`.
Its displayed factor contains `d^4`, two marginal eighth moments, and three
eighth-score-moment terms. The comparison in this verifier specializes both
displayed bounds to the same independent standard-Gaussian coupling.

This audit tests the exact displayed factors and a valid nontrivial
specialization. It does not substitute an empirical power-law fit for the
source quantifiers.
