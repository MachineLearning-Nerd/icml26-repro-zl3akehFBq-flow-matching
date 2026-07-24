"""Fail-closed checks for the artifact an evaluator can actually discover."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any


LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REQUIRED_INLINE = (
    "Exact claim and quantifiers",
    "Assumption audit",
    "Executable source",
    "Fixed command",
    "Raw numerical results",
    "Independent checker",
    "Negative control",
    "Limitations and deviations",
    "Git SHA",
    "CPU/runtime",
    "nonzero",
)


def visible_root(repository: Path) -> Path:
    candidate = repository / "hf_space_candidate"
    return candidate if candidate.is_dir() else repository


def resolve_link(page: Path, target: str, root: Path) -> Path | None:
    clean = target.split("#", 1)[0].split("?", 1)[0]
    if not clean or clean.startswith(("http://", "https://", "#/")):
        return None
    resolved = (page.parent / clean).resolve()
    if root.resolve() not in (resolved, *resolved.parents):
        raise AssertionError(f"link escapes evaluator artifact: {page}: {target}")
    return resolved


def linked_files(page: Path, root: Path) -> list[Path]:
    result: list[Path] = []
    for target in LINK.findall(page.read_text(encoding="utf-8")):
        resolved = resolve_link(page, target, root)
        if resolved is not None:
            if not resolved.is_file():
                raise AssertionError(f"broken evaluator-visible link: {page}: {target}")
            result.append(resolved)
    return result


def check_visible_artifact(repository: Path) -> dict[str, Any]:
    root = visible_root(repository)
    entrypoints = [root / "README.md", root / "pages" / "index.md", root / "logbook.json"]
    for path in entrypoints:
        assert path.is_file(), f"canonical entrypoint missing: {path}"

    logbook = json.loads(entrypoints[2].read_text(encoding="utf-8"))
    children = logbook["root"]["children"]
    current = children[:7]
    expected = [
        "pages/10-current-execution/page.md",
        *[f"pages/{claim + 10:02d}-current-claim-{claim}/page.md" for claim in range(1, 7)],
    ]
    assert [item["file"] for item in current] == expected
    historical = children[7:]
    assert historical, "historical evidence disappeared"
    assert all(
        item["title"].startswith("Historical rejected baseline")
        for item in historical
    ), "historical pages are not unambiguously labeled"

    index_text = entrypoints[1].read_text(encoding="utf-8")
    readme_text = entrypoints[0].read_text(encoding="utf-8")
    for relative in expected:
        assert relative in index_text or Path(relative).parent.name in index_text
    assert "Current verification" in readme_text
    assert "Historical rejected baseline" in readme_text

    page_results: list[dict[str, Any]] = []
    for claim in range(1, 7):
        page = root / expected[claim]
        text = page.read_text(encoding="utf-8")
        missing = [phrase for phrase in REQUIRED_INLINE if phrase not in text]
        assert not missing, f"claim {claim} page missing inline fields: {missing}"
        links = linked_files(page, root)
        suffixes = {path.suffix for path in links}
        assert ".py" in suffixes, f"claim {claim}: executable Python not linked"
        assert ".csv" in suffixes, f"claim {claim}: raw CSV not linked"
        assert ".json" in suffixes, f"claim {claim}: JSON checker/control not linked"
        page_results.append(
            {
                "claim": claim,
                "page": page.relative_to(root).as_posix(),
                "linked_files": len(links),
                "complete": True,
            }
        )

    matrix_path = root / "evidence" / "evaluator_visibility_matrix.csv"
    with matrix_path.open(newline="", encoding="utf-8") as handle:
        matrix = list(csv.DictReader(handle))
    assert len(matrix) == 6
    required_true = (
        "code_visible",
        "data_inline",
        "raw_link",
        "checker",
        "control",
    )
    for row in matrix:
        assert all(row[key] == "yes" for key in required_true), row
        assert row["exact_claim_tested"], row
        assert row["reviewer_verdict"] in {"release-ready", "1/2-scoped"}

    for relative in ("pyproject.toml", "uv.lock", "repro/src/verify_fm.py"):
        assert (root / relative).is_file(), f"published executable input missing: {relative}"

    first_hits = list(
        csv.DictReader(
            (root / "evidence" / "current" / "claim_3" / "raw_first_hit.csv").open(
                newline="", encoding="utf-8"
            )
        )
    )
    assert len(first_hits) == 18
    assert all(float(row["uniform_to_nonuniform_work_ratio"]) > 1 for row in first_hits)
    return {
        "visible_root": str(root),
        "canonical_entrypoints": 3,
        "current_pages": page_results,
        "visibility_rows": len(matrix),
        "first_hit_rows": len(first_hits),
        "verdict": "VERIFIED",
    }


if __name__ == "__main__":
    repository = Path(__file__).resolve().parents[2]
    print(json.dumps(check_visible_artifact(repository), indent=2, sort_keys=True))
