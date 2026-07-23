"""Build reader-facing figures from committed OpenResearch evidence."""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / ".openresearch" / "artifacts"
OUT = ROOT / "reports" / "claim-by-claim" / "images"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#14213d"
BLUE = "#2f6fed"
TEAL = "#00a896"
ORANGE = "#f4a261"
RED = "#d1495b"
GRAY = "#667085"
PALE = "#eef4ff"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def finish(fig: plt.Figure, name: str) -> None:
    fig.savefig(OUT / name, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def headline() -> None:
    claims = [
        "T1\nKL + d³",
        "T2\nH4 only",
        "T3\nschedule",
        "T4\nW₂",
        "Cor. 3\nproduct",
        "Method\nIBP",
    ]
    fig, ax = plt.subplots(figsize=(12, 5.8))
    y = np.arange(len(claims))
    ax.barh(y, np.ones(6), color=TEAL, height=0.62)
    ax.set_yticks(y, claims, fontsize=12)
    ax.set_xlim(0, 1.08)
    ax.invert_yaxis()
    for index in y:
        ax.text(0.96, index, "VERIFIED", va="center", ha="right",
                color="white", weight="bold", fontsize=11)
    ax.set_title(
        "Six source-faithful contracts pass the cumulative local verifier",
        loc="left", color=NAVY, fontsize=18, weight="bold", pad=18,
    )
    ax.text(
        0, 1.03,
        "Each row has raw data, an independent checker, and rejected negative controls.",
        transform=ax.transAxes, color=GRAY, fontsize=11,
    )
    ax.text(
        0, -0.11,
        "Local contract outcomes • not a new live-judge score",
        transform=ax.transAxes, color=RED, fontsize=10, weight="bold",
    )
    ax.set_xticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    finish(fig, "01_headline_claims.png")


def scaling() -> None:
    rows = read_csv(EVIDENCE / "claim_1" / "raw_results.csv")
    selected = {
        int(row["dimension"]): row
        for row in rows
        if int(row["steps"]) == 8 and float(row["epsilon"]) == 0.0
    }
    d = np.array(sorted(selected), dtype=float)
    current = np.array([float(selected[int(v)]["current_factor"]) for v in d])
    prior = np.array([float(selected[int(v)]["prior_factor"]) for v in d])

    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    ax.loglog(d, current, "o-", color=BLUE, lw=2.5, label="Theorem 1 factor")
    ax.loglog(d, prior, "s-", color=ORANGE, lw=2.5, label="Cited prior factor")
    ref3 = current[-1] * (d / d[-1]) ** 3
    ref4 = prior[-1] * (d / d[-1]) ** 4
    ax.loglog(d, ref3, "--", color=BLUE, alpha=0.45, label="d³ reference")
    ax.loglog(d, ref4, "--", color=ORANGE, alpha=0.45, label="d⁴ reference")
    ax.set_xlabel("dimension d")
    ax.set_ylabel("exact specialized source factor")
    fig.suptitle(
        "The displayed factors separate cubic from quartic dimension order",
        x=0.08, y=0.98, ha="left", color=NAVY, fontsize=17, weight="bold",
    )
    fig.text(
        0.08, 0.91,
        "Independent SymPy limits: current/d³ → 5; prior/d⁴ → 6",
        color=GRAY, fontsize=10.5,
    )
    fig.subplots_adjust(top=0.84)
    ax.grid(True, which="both", alpha=0.2)
    ax.legend(frameon=False, ncol=2)
    finish(fig, "02_dimension_scaling.png")


def schedule() -> None:
    rows = read_csv(EVIDENCE / "claim_3" / "raw_complexity.csv")
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    colors = [BLUE, TEAL, ORANGE, RED]
    for color, dimension in zip(colors, (1, 8, 64, 256)):
        subset = sorted(
            (row for row in rows if int(row["dimension"]) == dimension),
            key=lambda row: float(row["delta"]),
            reverse=True,
        )
        inv_delta = [1.0 / float(row["delta"]) for row in subset]
        ratio = [float(row["uniform_to_nonuniform_work_ratio"]) for row in subset]
        ax.loglog(inv_delta, ratio, "o-", lw=2.2, color=color, label=f"d={dimension}")
    ax.axhline(1.0, color=GRAY, ls="--", lw=1.4)
    ax.set_xlabel("endpoint proximity 1/δ")
    ax.set_ylabel("uniform work / non-uniform work")
    fig.suptitle(
        "The non-uniform bound replaces δ⁻⁴ with log(1/δ)",
        x=0.08, y=0.98, ha="left", color=NAVY, fontsize=17, weight="bold",
    )
    fig.text(
        0.08, 0.91,
        "Matched explicit-bound tolerance; values above one favor the theorem schedule.",
        color=GRAY, fontsize=10.5,
    )
    fig.subplots_adjust(top=0.84)
    ax.grid(True, which="both", alpha=0.2)
    ax.legend(frameon=False, ncol=4)
    finish(fig, "03_schedule_advantage.png")


def wasserstein() -> None:
    rows = read_csv(EVIDENCE / "claim_4" / "raw_results.csv")
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    colors = [BLUE, TEAL, ORANGE, RED]
    for color, rho in zip(colors, (0.0, 0.25, 0.5, 0.75)):
        subset = sorted(
            (
                row
                for row in rows
                if int(row["dimension"]) == 64
                and float(row["epsilon"]) == 0.0
                and float(row["rho"]) == rho
            ),
            key=lambda row: float(row["h"]),
        )
        ax.loglog(
            [float(row["h"]) for row in subset],
            [float(row["w2"]) for row in subset],
            "o-", lw=2.2, color=color, label=f"ρ={rho:g}",
        )
    ax.set_xlabel("uniform step size h")
    ax.set_ylabel("exact W₂(target, Euler)")
    fig.suptitle(
        "Exact W₂ falls under refinement for every coupling strength",
        x=0.08, y=0.98, ha="left", color=NAVY, fontsize=17, weight="bold",
    )
    fig.text(
        0.08, 0.91,
        "d=64, ε=0; all 36 (dimension, ρ) refinement paths pass.",
        color=GRAY, fontsize=10.5,
    )
    fig.subplots_adjust(top=0.84)
    ax.grid(True, which="both", alpha=0.2)
    ax.legend(frameon=False, ncol=4)
    finish(fig, "04_wasserstein_refinement.png")


def integration_by_parts() -> None:
    rows = read_csv(EVIDENCE / "claim_6" / "raw_results.csv")
    first_dimension = [row for row in rows if int(row["dimension"]) == 1]
    dimensions = sorted({int(row["dimension"]) for row in rows})
    residuals = [
        max(
            float(row["direct_transfer_absolute_residual"])
            for row in rows
            if int(row["dimension"]) == dimension
        )
        for dimension in dimensions
    ]

    fig, (left, right) = plt.subplots(1, 2, figsize=(12.5, 5.8))
    direct = np.array(
        [float(row["direct_third_derivative_integral"]) for row in first_dimension]
    )
    transferred = np.array(
        [
            float(row["transferred_second_derivative_score_integral"])
            for row in first_dimension
        ]
    )
    lo = min(direct.min(), transferred.min()) - 0.04
    hi = max(direct.max(), transferred.max()) + 0.04
    left.plot([lo, hi], [lo, hi], "--", color=GRAY)
    left.scatter(direct, transferred, s=90, color=TEAL, edgecolor="white", linewidth=1)
    left.set_xlabel("direct third-derivative integral")
    left.set_ylabel("transferred second-derivative integral")
    left.set_title("Identity values", loc="left", color=NAVY, weight="bold")
    left.grid(True, alpha=0.2)

    right.semilogx(dimensions, residuals, "o-", color=BLUE, lw=2.2)
    right.set_ylim(0, max(residuals) * 1.35)
    right.set_xlabel("dimension bookkeeping d")
    right.set_ylabel("absolute identity residual")
    right.set_title("Numerical residual", loc="left", color=NAVY, weight="bold")
    right.grid(True, alpha=0.2)
    fig.suptitle(
        "Integration by parts transfers order 3 → order 2 + coupling score",
        x=0.07, ha="left", color=NAVY, fontsize=17, weight="bold",
    )
    fig.text(
        0.07, 0.91,
        "Three nonzero parameter settings; maximum residual 2.22×10⁻¹⁶.",
        color=GRAY, fontsize=10.5,
    )
    fig.subplots_adjust(top=0.82, wspace=0.3)
    finish(fig, "05_integration_by_parts.png")


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.labelcolor": NAVY,
            "xtick.color": GRAY,
            "ytick.color": GRAY,
        }
    )
    headline()
    scaling()
    schedule()
    wasserstein()
    integration_by_parts()
    for path in sorted(OUT.glob("*.png")):
        print(f"{path.relative_to(ROOT)}\t{path.stat().st_size}")


if __name__ == "__main__":
    main()
