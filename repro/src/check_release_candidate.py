"""Fail-closed integrity checker for the cumulative release candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ARTIFACTS = REPO / ".openresearch" / "artifacts"
CANDIDATE = REPO / "hf_space_candidate"
ORIGINAL_PROTECTED_MANIFEST = (
    CANDIDATE / "protected" / "judged-af641c4e-manifest.tsv"
)
ORIGINAL_PROTECTED_LOGBOOK = CANDIDATE / "protected" / "judged-logbook.json"
PROTECTED_MANIFEST = CANDIDATE / "protected" / "judged-22e4c6cc-manifest.tsv"
PROTECTED_LOGBOOK = CANDIDATE / "protected" / "judged-22e4c6cc-logbook.json"
ALLOWLIST = CANDIDATE / "release" / "upload-allowlist.txt"
UPLOAD_MANIFEST = CANDIDATE / "release" / "text-sha256-manifest.tsv"

REQUIRED_CLAIM_FILES = {
    "claim_contract.json",
    "source_audit.md",
    "method.md",
    "independent_checker_output.json",
    "negative_control_output.json",
    "runtime.json",
    "EVAL.md",
    "limitations.md",
}


def digest(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), len(data)


def parse_manifest(path: Path) -> dict[str, tuple[str, int]]:
    rows: dict[str, tuple[str, int]] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines and lines[0] == "sha256\tbytes\tpath", f"bad manifest header: {path}"
    for line in lines[1:]:
        sha256, size, relative = line.split("\t", 2)
        assert relative not in rows, f"duplicate manifest path: {relative}"
        rows[relative] = (sha256, int(size))
    return rows


def walk_logbook(node: dict) -> list[str]:
    files = [node["file"]]
    for child in node.get("children", []):
        files.extend(walk_logbook(child))
    return files


def check_one_protected_tree(
    manifest_path: Path, logbook_path: Path
) -> dict[str, int]:
    judged = parse_manifest(manifest_path)
    candidate_paths = {
        path.relative_to(CANDIDATE).as_posix()
        for path in CANDIDATE.rglob("*")
        if path.is_file()
    }
    missing = sorted(set(judged) - candidate_paths)
    assert not missing, f"judged paths missing from candidate: {missing}"

    for relative, expected in judged.items():
        if relative == "logbook.json":
            continue
        assert digest(CANDIDATE / relative) == expected, f"protected path changed: {relative}"
    assert digest(logbook_path) == judged["logbook.json"], (
        f"judged logbook snapshot changed: {logbook_path}"
    )
    return {
        "judged_paths": len(judged),
        "candidate_paths": len(candidate_paths),
        "byte_identical_non_logbook_paths": len(judged) - 1,
    }


def check_protected_tree() -> dict[str, dict[str, int]]:
    return {
        "original_af641c4e": check_one_protected_tree(
            ORIGINAL_PROTECTED_MANIFEST, ORIGINAL_PROTECTED_LOGBOOK
        ),
        "current_22e4c6cc": check_one_protected_tree(
            PROTECTED_MANIFEST, PROTECTED_LOGBOOK
        ),
    }


def check_logbook() -> int:
    logbook = json.loads((CANDIDATE / "logbook.json").read_text(encoding="utf-8"))
    assert logbook["space_id"] == "DineshAI/zl3akehFBq"
    pages = walk_logbook(logbook["root"])
    for relative in pages:
        assert (CANDIDATE / relative).is_file(), f"logbook page missing: {relative}"
    required_slugs = {
        "pages/00-current-execution/page.md",
        "pages/01-current-claim-1/page.md",
        "pages/02-current-claim-2/page.md",
        "pages/03-current-claim-3/page.md",
        "pages/04-current-claim-4/page.md",
        "pages/05-current-claim-5/page.md",
        "pages/06-current-claim-6/page.md",
        "pages/claim-contract-results/page.md",
        "pages/release-evidence/page.md",
        "pages/release-manifest/page.md",
    }
    assert required_slugs <= set(pages), "new evidence pages are not reachable"
    assert pages[1:8] == sorted(required_slugs)[:7], (
        "current executed-evidence pages are not first after the index"
    )
    return len(pages)


def check_claim_evidence() -> dict[str, int]:
    raw_rows = 0
    controls = 0
    for claim_id in range(1, 7):
        claim_dir = ARTIFACTS / f"claim_{claim_id}"
        names = {path.name for path in claim_dir.iterdir() if path.is_file()}
        missing = REQUIRED_CLAIM_FILES - names
        assert not missing, f"claim {claim_id} missing: {sorted(missing)}"
        assert any(name.startswith("raw_") for name in names), f"claim {claim_id} has no raw data"

        contract = json.loads((claim_dir / "claim_contract.json").read_text(encoding="utf-8"))
        if "verdict_vocabulary" in contract:
            assert contract["verdict_vocabulary"] == ["VERIFIED", "FALSIFIED", "BLOCKED"]
        assert "nonzero" in contract["fail_policy"]

        evaluation = (claim_dir / "EVAL.md").read_text(encoding="utf-8")
        verdict_lines = [line for line in evaluation.splitlines() if line.startswith("Verdict:")]
        assert verdict_lines == ["Verdict: **VERIFIED**"], f"claim {claim_id} verdict malformed"

        negative = json.loads(
            (claim_dir / "negative_control_output.json").read_text(encoding="utf-8")
        )
        assert negative["passed"] is True, f"claim {claim_id} negative control accepted"
        assert negative["expected_rejections"] == negative["observed_rejections"]
        assert all(item["observed"] == "REJECTED" for item in negative["outcomes"])
        controls += len(negative["outcomes"])

        for raw_path in claim_dir.glob("raw_*.csv"):
            raw_rows += max(0, len(raw_path.read_text(encoding="utf-8").splitlines()) - 1)
    assert controls == 18, f"expected 18 rejected controls, observed {controls}"
    assert raw_rows == 2331, f"expected 2331 raw rows, observed {raw_rows}"
    return {"claims": 6, "raw_rows": raw_rows, "rejected_controls": controls}


def check_upload_payloads() -> int:
    allowlisted = ALLOWLIST.read_text(encoding="utf-8").splitlines()
    assert allowlisted == sorted(set(allowlisted)), "allowlist is not sorted and unique"
    assert allowlisted, "empty upload allowlist"

    protected = parse_manifest(PROTECTED_MANIFEST)
    expected_changed: set[str] = set()
    metadata = {
        ALLOWLIST.relative_to(CANDIDATE).as_posix(),
        UPLOAD_MANIFEST.relative_to(CANDIDATE).as_posix(),
    }
    for path in CANDIDATE.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(CANDIDATE).as_posix()
        if relative in metadata:
            continue
        if protected.get(relative) != digest(path):
            expected_changed.add(relative)
    assert set(allowlisted) == expected_changed, "allowlist is not the exact changed/new path set"

    manifest = parse_manifest(UPLOAD_MANIFEST)
    assert set(manifest) == set(allowlisted), "upload manifest and allowlist differ"
    for relative in allowlisted:
        assert not relative.startswith("/") and ".." not in Path(relative).parts
        path = CANDIDATE / relative
        assert path.is_file() and not path.is_symlink(), f"invalid upload path: {relative}"
        data = path.read_bytes()
        assert b"\0" not in data, f"binary payload allowlisted: {relative}"
        data.decode("utf-8")
        assert digest(path) == manifest[relative], f"upload hash mismatch: {relative}"
        if path.suffix == ".json":
            json.loads(data)
    return len(allowlisted)


if __name__ == "__main__":
    result = {
        "protected_tree": check_protected_tree(),
        "reachable_logbook_pages": check_logbook(),
        "claim_evidence": check_claim_evidence(),
        "text_upload_paths": check_upload_payloads(),
        "verdict": "VERIFIED",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
