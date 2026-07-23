"""Capture an immutable text manifest for an exact downloaded Space revision."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
PROTECTED = REPO / "hf_space_candidate" / "protected"


def digest(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), len(data)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--label", required=True)
    args = parser.parse_args()

    source = args.source.resolve()
    if not (source / "logbook.json").is_file():
        raise FileNotFoundError(f"downloaded revision has no logbook.json: {source}")

    paths = sorted(
        path
        for path in source.rglob("*")
        if path.is_file() and ".cache" not in path.relative_to(source).parts
    )
    rows = ["sha256\tbytes\tpath"]
    for path in paths:
        sha256, size = digest(path)
        rows.append(f"{sha256}\t{size}\t{path.relative_to(source).as_posix()}")

    PROTECTED.mkdir(parents=True, exist_ok=True)
    manifest = PROTECTED / f"judged-{args.label}-manifest.tsv"
    snapshot = PROTECTED / f"judged-{args.label}-logbook.json"
    manifest.write_text("\n".join(rows) + "\n", encoding="utf-8")
    shutil.copyfile(source / "logbook.json", snapshot)
    print(f"captured_paths={len(paths)}")
    print(f"manifest={manifest.relative_to(REPO)}")
    print(f"logbook_snapshot={snapshot.relative_to(REPO)}")


if __name__ == "__main__":
    main()
