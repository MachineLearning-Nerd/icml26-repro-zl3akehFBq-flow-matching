"""Regenerate the two figures changed by the evaluator-gate research round."""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "hf_space_candidate" / "evidence" / "current" / "claim_3" / "raw_first_hit.csv"
IMAGES = Path(__file__).resolve().parent / "images"


with RAW.open(newline="", encoding="utf-8") as handle:
    rows = [
        row
        for row in csv.DictReader(handle)
        if int(row["dimension"]) == 256
        and float(row["kl_tolerance_per_dimension"]) == 1e-3
    ]

deltas = [float(row["requested_delta"]) for row in rows]
ratios = [float(row["uniform_to_nonuniform_work_ratio"]) for row in rows]
uniform = [int(row["uniform_first_hit_steps"]) for row in rows]
nonuniform = [int(row["nonuniform_first_hit_total_steps"]) for row in rows]
labels = [f"2$^{{-{round(-__import__('math').log2(value))}}}$" for value in deltas]

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(9.4, 4.8))
bars = ax.bar(labels, ratios, color=["#4C78A8", "#2A9D8F", "#E76F51"])
ax.set(
    title="Observed first-hit advantage grows toward the endpoint",
    xlabel="early-stopping δ",
    ylabel="uniform work / nonuniform work",
)
ax.axhline(1, color="#333333", linewidth=1, linestyle="--")
for bar, ratio, u_work, n_work in zip(bars, ratios, uniform, nonuniform, strict=True):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.25,
        f"{ratio:.2f}×\n{u_work:,} vs {n_work:,}",
        ha="center",
        va="bottom",
        fontsize=10,
    )
ax.set_ylim(0, max(ratios) * 1.25)
fig.tight_layout()
fig.savefig(IMAGES / "01_headline_claims.png", dpi=180)
plt.close(fig)

fig, ax = plt.subplots(figsize=(9.4, 4.8))
x = range(len(labels))
width = 0.38
ax.bar([value - width / 2 for value in x], uniform, width, label="uniform first hit", color="#4C78A8")
ax.bar([value + width / 2 for value in x], nonuniform, width, label="nonuniform first hit", color="#2A9D8F")
ax.set_yscale("log")
ax.set_xticks(list(x))
ax.set_xticklabels(labels)
ax.set(
    title="Minimum exact-KL resource found by binary search",
    xlabel="early-stopping δ",
    ylabel="drift evaluations (log scale)",
)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "03_schedule_advantage.png", dpi=180)
plt.close(fig)
