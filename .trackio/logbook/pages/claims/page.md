# Claims


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_d3dbfc34dd87", "created_at": "2026-07-21T21:58:24+00:00", "title": "Claims to reproduce"}
-->
## Claims to reproduce

1. For the non-early-stopping, constant step-size setting, Theorem 1 establishes KL convergence bounds for Brownian-motion-based diffusion flow matching scaling as O(d^3) in dimension, improving on prior O(d^4) results, decomposing into a drift-approximation term epsilon^2 and a discretization term scaling as O(h) (Theorem 1).
2. Theorem 2 relaxes the assumptions of Theorem 1 to require score integrability only of the conditional coupling pi_{0|1} rather than the full coupling pi, while preserving the O(d^3) dimensional scaling under early stopping (Theorem 2).
3. Theorem 3 introduces a novel non-uniform step-size schedule (h_k = h early, then h_k = h*min(t_k, 1-t_k) later) that yields faster convergence in the early-stopping regime while retaining O(d^3) complexity (Theorem 3).
4. Theorem 4 extends the analysis to 2-Wasserstein distance, giving bounds that decompose into a drift error epsilon and a discretization error scaling as O(sqrt(h))*O(sqrt(d^3)), under a weak log-concavity assumption on the coupling and first-order score integrability (Theorem 4).
5. Corollary 3 specializes the Wasserstein result of Theorem 4 to the independent coupling pi = mu tensor nu*, allowing assumptions to be stated on the marginals rather than the joint distribution (Corollary 3).
6. The dimensional improvement from O(d^4) to O(d^3) is obtained by using integration-by-parts to transfer derivatives onto the coupling instead of directly expanding three logarithmic-derivative terms, reducing the required differentiation order from three to two (Section on Key Methodological Innovations).
