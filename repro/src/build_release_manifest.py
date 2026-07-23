"""Build deterministic evidence and Hugging Face text-upload manifests."""

from __future__ import annotations

import hashlib
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ARTIFACTS = REPO / ".openresearch" / "artifacts"
CANDIDATE = REPO / "hf_space_candidate"
PROTECTED_MANIFEST = CANDIDATE / "protected" / "judged-22e4c6cc-manifest.tsv"
RELEASE_DIR = CANDIDATE / "release"
ALLOWLIST = RELEASE_DIR / "upload-allowlist.txt"
UPLOAD_MANIFEST = RELEASE_DIR / "text-sha256-manifest.tsv"


def digest(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), len(data)


def read_protected_manifest() -> dict[str, tuple[str, int]]:
    rows: dict[str, tuple[str, int]] = {}
    for line in PROTECTED_MANIFEST.read_text(encoding="utf-8").splitlines()[1:]:
        sha256, size, relative = line.split("\t", 2)
        rows[relative] = (sha256, int(size))
    return rows


def is_text(path: Path) -> bool:
    data = path.read_bytes()
    if b"\0" in data:
        return False
    data.decode("utf-8")
    return True


def build_artifact_manifest() -> None:
    output = ARTIFACTS / "MANIFEST.tsv"
    rows = ["sha256\tbytes\tpath"]
    for path in sorted(ARTIFACTS.rglob("*")):
        if not path.is_file() or path == output:
            continue
        sha256, size = digest(path)
        rows.append(f"{sha256}\t{size}\t{path.relative_to(ARTIFACTS).as_posix()}")
    output.write_text("\n".join(rows) + "\n", encoding="utf-8")


def build_upload_manifest() -> None:
    protected = read_protected_manifest()
    metadata = {
        ALLOWLIST.relative_to(CANDIDATE).as_posix(),
        UPLOAD_MANIFEST.relative_to(CANDIDATE).as_posix(),
    }
    payloads: list[str] = []
    for path in sorted(CANDIDATE.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(CANDIDATE).as_posix()
        if relative in metadata:
            continue
        current_sha, current_size = digest(path)
        old = protected.get(relative)
        if old == (current_sha, current_size):
            continue
        if not is_text(path):
            raise ValueError(f"changed or new non-text payload: {relative}")
        payloads.append(relative)

    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    ALLOWLIST.write_text("\n".join(payloads) + "\n", encoding="utf-8")

    rows = ["sha256\tbytes\tpath"]
    for relative in payloads:
        sha256, size = digest(CANDIDATE / relative)
        rows.append(f"{sha256}\t{size}\t{relative}")
    UPLOAD_MANIFEST.write_text("\n".join(rows) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_artifact_manifest()
    build_upload_manifest()
    print(f"artifact manifest: {ARTIFACTS / 'MANIFEST.tsv'}")
    print(f"upload allowlist: {ALLOWLIST}")
    print(f"upload manifest: {UPLOAD_MANIFEST}")
