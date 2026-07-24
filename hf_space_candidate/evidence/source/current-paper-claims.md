# Primary-source claim and quantifier audit

Primary HTML:
[ar5iv rendering of arXiv:2606.16610](https://ar5iv.labs.arxiv.org/html/2606.16610).
Canonical record:
[arXiv abstract](https://arxiv.org/abs/2606.16610).

The HTML was retrieved on `2026-07-23T12:36:52Z` with explicit User-Agent
`Mozilla/5.0 OpenResearch-Reproduction/1.0 User-Agent`. The 1,314,182-byte
response SHA-256 was
`c3553013f3f7022f6e5f539e735585d6180364f716d4b17b5679aacb519546ff`.
The machine-readable [retrieval record](paper_source.json) is in this revision.

## Assumptions

- H1: the discrete integrated squared drift error is at most `ε²`.
- H2: both endpoint marginals have finite eighth moments; the theorem's rate
  statement uses the dimension-four moment regime.
- H3: the joint coupling has a positive C1 density with L8-integrable score.
- H4: only the conditional score of `π_{0|1}` is L8-integrable.
- H5: the discrete integrated L2 drift error is at most `ε`.
- H6: the coupling is weakly log-concave with stated constants.
- H7: the positive C2 joint has first-order score and score-Hessian
  integrability.
- H8: the corresponding density, score, Hessian, and weak-concavity
  conditions hold on the two marginals.

## Exact displayed consequences tested

1. [Theorem 1](https://ar5iv.labs.arxiv.org/html/2606.16610#Thmtheorem1),
   under H1–H3 and `h=1/N`, bounds KL by a constant times
   `ε² + h(h^(1/8)+1)(d²+||∇logπ||_L8^4)d`.
2. [Theorem 2](https://ar5iv.labs.arxiv.org/html/2606.16610#Thmtheorem2),
   for every `0<δ<1/2` under H1, H2, H4, replaces the joint score with the
   conditional score and has the explicit `d²/δ⁴` term inside the outer `d`.
3. [Theorem 3](https://ar5iv.labs.arxiv.org/html/2606.16610#Thmtheorem3)
   uses constant `h` to `1/2`, then `h_k=h min(t_k,1-t_k)`, and replaces the
   endpoint term by `h d³ log(1/δ)` while retaining the regular Theorem-1-type
   term.
4. [Theorem 4](https://ar5iv.labs.arxiv.org/html/2606.16610#Thmtheorem4),
   under H2 and H5–H7, bounds W2 by
   `Cε + √h(h^(1/16)+1)√((d²+||∇logπ||_L8^4)d)`.
5. [Corollary 3](https://ar5iv.labs.arxiv.org/html/2606.16610#Thmcorollary3)
   applies the Wasserstein result to `π=μ⊗ν*` under marginal H8 conditions.
6. The methodological derivation transfers one derivative from a third
   kernel derivative to the coupling score by integration by parts, leaving a
   second kernel derivative; the paper attributes the explicit `d⁴→d³`
   improvement to this reorganization.

These are source statements, not assumptions manufactured by the verifier.
The current pages distinguish independently checked algebra/calculus from
finite exact-family corroboration and state where a complete formal stochastic
proof is not supplied.
