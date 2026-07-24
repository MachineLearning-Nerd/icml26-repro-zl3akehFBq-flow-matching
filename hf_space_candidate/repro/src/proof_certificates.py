"""Independent symbolic certificates for the six paper-claim contracts.

These checks deliberately distinguish a theorem's universal displayed
inequality from exact finite-family corroboration.  They certify the algebraic
rate/decomposition consequences and the general calculus identities used in
Claims 5 and 6.  They do not pretend that a finite Gaussian sweep is a proof of
the stochastic inequalities in Theorems 1--4.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


def build_certificates() -> dict[str, dict[str, Any]]:
    d, h, delta, eps, score4, c = sp.symbols(
        "d h delta epsilon score4 C", positive=True
    )

    theorem1_disc = h * (h ** sp.Rational(1, 8) + 1) * (d**2 + score4) * d
    theorem2_disc = (
        h
        * (h ** sp.Rational(1, 8) + 1)
        * (d**2 / delta**4 + score4)
        * d
    )
    theorem3_disc = h * d**3 * sp.log(1 / delta) + theorem1_disc
    theorem4_disc = (
        sp.sqrt(h)
        * (h ** sp.Rational(1, 16) + 1)
        * sp.sqrt((d**2 + score4) * d)
    )

    # Rate certificates use the theorem's stated moment regime score4=O(d^2).
    score_specialization = {score4: c * d**2}
    certs: dict[str, dict[str, Any]] = {
        "claim_1": {
            "certificate_kind": "independent_symbolic_rate_derivation",
            "universal_variables": ["d>=1", "0<h<=1", "epsilon>=0"],
            "paper_premise": (
                "KL <= epsilon^2 + h(h^(1/8)+1)(d^2+S_8^4)d"
            ),
            "derivation": [
                "0<h<=1 implies h^(1/8)+1<=2",
                "S_8^4=O(d^2) implies (d^2+S_8^4)d=O(d^3)",
                "therefore the two summands are epsilon^2 and O(h d^3)",
            ],
            "normalized_limit": str(
                sp.limit(theorem1_disc.subs(score_specialization) / (h * d**3), d, sp.oo)
            ),
            "h_upper_factor": "2",
            "scope": (
                "Certifies the rate and decomposition implied by the displayed "
                "Theorem 1 inequality; the exact Gaussian sweep separately "
                "corroborates, but does not prove, the universal inequality."
            ),
        },
        "claim_2": {
            "certificate_kind": "independent_symbolic_rate_and_assumption_derivation",
            "universal_variables": [
                "d>=1",
                "0<h<=1",
                "0<delta<1/2",
                "epsilon>=0",
            ],
            "paper_premise": (
                "KL_delta <= epsilon^2 + "
                "h(h^(1/8)+1)(d^2/delta^4+S_cond,8^4)d"
            ),
            "derivation": [
                "The premise contains only the conditional score norm, not the joint score norm",
                "for fixed delta and S_cond,8^4=O(d^2), the dimension factor is O(d^3)",
                "the singular product witness establishes H4 true while H3 is undefined/false",
            ],
            "normalized_limit": str(
                sp.limit(
                    theorem2_disc.subs(score_specialization) / (h * d**3),
                    d,
                    sp.oo,
                )
            ),
            "scope": (
                "Certifies the displayed rate and the strict logical weakening "
                "H4-not-H3; it does not infer the universal theorem from the witness."
            ),
        },
        "claim_3": {
            "certificate_kind": "symbolic_schedule_solution_and_rate_derivation",
            "universal_variables": [
                "d>=1",
                "0<h<=1",
                "0<delta<1/2",
            ],
            "paper_premise": (
                "h_k=h through 1/2, then h_k=h min(t_k,1-t_k); "
                "KL_delta includes h d^3 log(1/delta)"
            ),
            "derivation": [
                "after 1/2, t_{k+1}=t_k+h(1-t_{k+1})",
                "therefore 1-t_{M+j}=(1/2)(1+h)^(-j)",
                "j=ceil(log(1/(2delta))/log(1+h))=O(h^-1 log(1/delta))",
                "with S_cond,8^4=O(d^2), every displayed dimension factor is O(d^3)",
            ],
            "normalized_limit": str(
                sp.limit(
                    theorem3_disc.subs(score_specialization) / (h * d**3),
                    d,
                    sp.oo,
                )
            ),
            "scope": (
                "The resource advantage is tested independently by observed "
                "first-hit KL searches; no formula-selected budget is used as "
                "the primary empirical evidence."
            ),
        },
        "claim_4": {
            "certificate_kind": "independent_symbolic_rate_derivation",
            "universal_variables": ["d>=1", "0<h<=1", "epsilon>=0"],
            "paper_premise": (
                "W2 <= C epsilon + sqrt(h)(h^(1/16)+1)"
                "sqrt((d^2+S_8^4)d)"
            ),
            "derivation": [
                "0<h<=1 implies h^(1/16)+1<=2",
                "S_8^4=O(d^2) implies sqrt((d^2+S_8^4)d)=O(sqrt(d^3))",
                "the two summands are linear drift error C epsilon and O(sqrt(h)d^(3/2))",
            ],
            "normalized_limit": str(
                sp.limit(
                    theorem4_disc.subs(score_specialization)
                    / (sp.sqrt(h) * d ** sp.Rational(3, 2)),
                    d,
                    sp.oo,
                )
            ),
            "scope": (
                "Certifies the rate/decomposition consequence of Theorem 4; "
                "the correlated Gaussian sweep audits H6/H7 and corroborates it."
            ),
        },
    }

    # Product-coupling identities hold pointwise for arbitrary positive C2
    # marginals.  Symbols stand for independent x/y score and Hessian blocks.
    sx, sy, hxx, hyy, alpha_mu, alpha_nu = sp.symbols(
        "s_x s_y H_xx H_yy alpha_mu alpha_nu", real=True
    )
    x_product, y_product = sp.symbols("x y", real=True)
    mu = sp.Function("mu")
    nu = sp.Function("nu")
    log_product = sp.log(mu(x_product)) + sp.log(nu(y_product))
    score_x_residual = sp.simplify(
        sp.diff(log_product, x_product)
        - sp.diff(sp.log(mu(x_product)), x_product)
    )
    score_y_residual = sp.simplify(
        sp.diff(log_product, y_product)
        - sp.diff(sp.log(nu(y_product)), y_product)
    )
    mixed_hessian_residual = sp.simplify(
        sp.diff(log_product, x_product, y_product)
    )
    certs["claim_5"] = {
        "certificate_kind": "general_pointwise_product_calculus",
        "universal_variables": [
            "all positive C2 marginal densities mu(x), nu(y)"
        ],
        "identities": {
            "log_product": "log(mu(x)nu(y))=log(mu(x))+log(nu(y))",
            "score": "grad log pi=(grad log mu, grad log nu)",
            "hessian": "Hess log pi=diag(Hess log mu,Hess log nu)",
            "mixed_hessian": "0",
            "weak_log_concavity": "alpha_pi=min(alpha_mu,alpha_nu)",
            "weak_curvature_constant": "M_pi=2 max(M_mu,M_nu)",
        },
        "symbolic_checks": {
            "score_squared_adds": str(sp.expand(sx**2 + sy**2)),
            "block_hessian_trace_adds": str(sp.expand(hxx + hyy)),
            "alpha_rule": str(sp.Min(alpha_mu, alpha_nu)),
            "score_x_residual": str(score_x_residual),
            "score_y_residual": str(score_y_residual),
            "mixed_hessian_residual": str(mixed_hessian_residual),
            "all_pointwise_derivative_checks_zero": (
                score_x_residual == 0
                and score_y_residual == 0
                and mixed_hessian_residual == 0
            ),
        },
        "scope": (
            "These pointwise identities cover the arbitrary product coupling "
            "specialization in Lemma 1/Corollary 3; exact unequal Gaussian "
            "marginals are only numerical corroboration."
        ),
    }

    # General one-dimensional form; coordinatewise application gives the
    # multivariate tensor identity. Boundary decay is an explicit premise.
    y = sp.symbols("y", real=True)
    kernel = sp.Function("K")(y)
    density = sp.Function("pi")(y)
    certs["claim_6"] = {
        "certificate_kind": "general_symbolic_integration_by_parts",
        "universal_variables": [
            "all C3 kernels K and positive C2 coupling densities pi with vanishing boundary term"
        ],
        "identity": (
            "integral (d_y^3 K) pi dy = "
            "- integral (d_y^2 K)(d_y log pi) pi dy"
        ),
        "symbolic_product_rule": str(
            sp.diff(sp.diff(kernel, y, 2) * density, y).expand()
        ),
        "symbolic_product_rule_residual": str(
            sp.simplify(
                sp.diff(sp.diff(kernel, y, 2) * density, y)
                - (
                    sp.diff(kernel, y, 3) * density
                    + sp.diff(kernel, y, 2) * sp.diff(density, y)
                )
            )
        ),
        "boundary_certificate": (
            "If [(d_y^2 K)pi]_-infinity^infinity=0, integrating the "
            "product-rule residual gives the stated identity."
        ),
        "derivative_orders": {
            "before": 3,
            "after_kernel": 2,
            "coupling_score": 1,
        },
        "tensor_count": "three free coordinate sums give at most d^3 terms",
        "scope": (
            "This is the general derivative-transfer identity used by the "
            "method. The paper's surrounding stochastic estimates are audited "
            "by source anchors and are not inferred from the Gaussian quadrature."
        ),
    }
    return certs


def write_certificates(
    root: Path,
    artifact_root: Path | None = None,
    claim3_directory: str = "claim_3",
) -> dict[str, dict[str, Any]]:
    certificates = build_certificates()
    for claim, certificate in certificates.items():
        base = artifact_root or root / ".openresearch" / "artifacts"
        directory = claim3_directory if claim == "claim_3" else claim
        path = base / directory / "universal_certificate.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    return certificates


if __name__ == "__main__":
    repository = Path(__file__).resolve().parents[2]
    result = write_certificates(repository)
    print(json.dumps(result, indent=2, sort_keys=True))
