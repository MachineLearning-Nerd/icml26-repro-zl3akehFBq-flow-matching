import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def _(mo, np, plt):
    labels = ["T1 KL+d³", "T2 H4", "T3 schedule", "T4 W₂", "Cor.3", "IBP"]
    status = np.ones(6)
    _fig, _ax = plt.subplots(figsize=(9, 3.6))
    _ax.barh(labels[::-1], status[::-1], color="#00a896")
    _ax.set_xlim(0, 1.08)
    _ax.set_xticks([])
    _ax.set_title("Six local claim contracts: VERIFIED", loc="left", weight="bold")
    for index in range(6):
        _ax.text(0.97, index, "VERIFIED", ha="right", va="center",
                 color="white", weight="bold")
    _ax.spines[["top", "right", "bottom"]].set_visible(False)
    evidence = mo.vstack(
        [
            mo.md(
                """
                # Dimension-improved diffusion flow matching

                **Evidence first:** the cumulative CPU verifier reports a source-faithful
                result for all six paper claims. The current official score is 5/12;
                the second release is published at revision `f2b258ac`, but these
                local outcomes are not a claim that the live score has changed.
                """
            ),
            _fig,
        ]
    )
    evidence
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## The central question

        The paper improves a KL-bound dimension factor from `O(d⁴)` to `O(d³)`
        and extends the argument to early stopping and Wasserstein distance.
        The original reproduction tested only one 3D flow. This notebook embeds
        the small numerical summaries from the completed evidence so that opening
        it does not rerun the expensive verifier.
        """
    )
    return


@app.cell
def _(mo, np, plt):
    d = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256], dtype=float)
    m8_joint = (2*d)*(2*d+2)*(2*d+4)*(2*d+6)
    current = d * (d**2 + np.sqrt(m8_joint))
    m8 = d*(d+2)*(d+4)*(d+6)
    prior = d**4 + 5*m8
    _fig, _ax = plt.subplots(figsize=(8.5, 4.8))
    _ax.loglog(d, current, "o-", label="Theorem 1 factor")
    _ax.loglog(d, prior, "s-", label="cited prior factor")
    _ax.loglog(d, current[-1]*(d/d[-1])**3, "--", alpha=.5, label="d³")
    _ax.loglog(d, prior[-1]*(d/d[-1])**4, "--", alpha=.5, label="d⁴")
    _ax.set(xlabel="dimension d", ylabel="exact specialized factor")
    _ax.grid(True, which="both", alpha=.2)
    _ax.legend(frameon=False, ncol=2)
    mo.vstack(
        [
            mo.md(
                """
                ## Exact dimension scaling

                SymPy independently gives `current/d³ → 5` and `prior/d⁴ → 6`.
                The plotted values are embedded formulas, not a finite-sample fit.
                """
            ),
            _fig,
        ]
    )
    return


@app.cell
def _(mo):
    dimension = mo.ui.slider(
        start=1,
        stop=256,
        step=1,
        value=64,
        label="dimension d",
        show_value=True,
    )
    dimension
    return (dimension,)


@app.cell
def _(dimension, mo):
    _d = float(dimension.value)
    _joint_m8 = (2 * _d) * (2 * _d + 2) * (2 * _d + 4) * (2 * _d + 6)
    _current = _d * (_d**2 + _joint_m8**0.5)
    _m8 = _d * (_d + 2) * (_d + 4) * (_d + 6)
    _prior = _d**4 + 5 * _m8
    mo.md(
        f"""
        At **d={int(_d)}**, the specialized Theorem 1 factor is
        **{_current:,.0f}** (`factor/d³ = {_current / _d**3:.4f}`), while the
        cited prior factor is **{_prior:,.0f}**
        (`factor/d⁴ = {_prior / _d**4:.4f}`). The slider is explanatory only;
        formal evidence uses the committed 1…256 sweep.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Why the other contracts are distinct

        - **Relaxed assumptions:** `π=N(0,I_d)⊗δ₀` has no full-joint density
          (H3 is false), while `π₀|₁=N(0,I_d)` has an integrable score (H4 is
          true). This is a strict witness, not Claim 1 repeated.
        - **Non-uniform schedule:** after `t=1/2`, the implicit rule
          `h_k=h(1-t_k)` gives `t_k=(t_{k-1}+h)/(1+h)`. The source bound replaces
          the uniform endpoint cost `δ⁻⁴` with `log(1/δ)`.
        - **Wasserstein guarantees:** correlated Gaussian couplings make
          log-concavity and score-Hessian constants explicit. Independent
          unequal marginals then test Corollary 3 as a genuinely different
          product coupling.
        - **Mechanism:** quadrature checks
          `∫(∂³K)π=-∫(∂²K)(∂logπ)π` with nonzero sides, directly exposing the
          derivative transfer used in the paper.
        """
    )
    return


@app.cell
def _(mo):
    rows = [
        {"Claim": "1", "Contract": "KL: ε² + h, d³ vs d⁴", "Rows": 252, "Verdict": "VERIFIED"},
        {"Claim": "2", "Contract": "H4 true while H3 false", "Rows": 648, "Verdict": "VERIFIED"},
        {"Claim": "3", "Contract": "exact schedule; log(1/δ)", "Rows": 116, "Verdict": "VERIFIED"},
        {"Claim": "4", "Contract": "W₂: ε + √h√d³", "Rows": 1008, "Verdict": "VERIFIED"},
        {"Claim": "5", "Contract": "independent unequal marginals", "Rows": 280, "Verdict": "VERIFIED"},
        {"Claim": "6", "Contract": "IBP order 3 → 2", "Rows": 27, "Verdict": "VERIFIED"},
    ]
    mo.vstack(
        [
            mo.md("## Claim ledger"),
            mo.ui.table(
                rows,
                label="Completed evidence",
                pagination=False,
                selection=None,
            ),
            mo.md(
                """
                The final scientific run took **1m10s** on an 8-logical-core
                local Apple CPU, used no GPU or remote compute, and rejected all
                18 negative controls. See the linked report for assumptions,
                deviations, and the protected Hugging Face release gate.
                """
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Interpretation and limits

        `VERIFIED` here means a source-faithful contract passed on the recorded
        branch. The live judge assigned 5/12 to the first release; publication
        of revision `f2b258ac` does **not** mean it has received new credit.
        These exact Gaussian specializations test the theorem factors,
        decompositions, assumption relaxation, schedule, and proof mechanism;
        they do not estimate hidden constants, establish tightness, or replace
        the paper's proofs.

        [Read the illustrated report on GitHub](https://github.com/MachineLearning-Nerd/icml26-repro-zl3akehFBq-flow-matching/blob/master/reports/claim-by-claim/report.md).
        """
    )
    return


if __name__ == "__main__":
    app.run()
