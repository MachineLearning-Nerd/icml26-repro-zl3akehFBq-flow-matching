# Command ledger

Every experiment inherited the same command:

```bash
uv sync --frozen && uv run --frozen python repro/src/verify_fm.py
```

## ORX experiment commands

```bash
orx exp run a41a6473-d92b-46e5-a28a-11aa381df0df --backend local
orx exp wait a41a6473-d92b-46e5-a28a-11aa381df0df --timeout 55
orx logs cc1f0ac1-c742-45ef-b58b-0d329a3ae394

orx exp run 2bdd5ebe-ae65-427f-ba4c-9933eb7f89ce --backend local
orx exp wait 2bdd5ebe-ae65-427f-ba4c-9933eb7f89ce --timeout 55
orx logs 447ac6f1-9147-4c82-8bda-58b7b6c331a0

orx exp run 6e4d81e5-0c24-40d9-b1ff-c78c69030272 --backend local
orx exp wait 6e4d81e5-0c24-40d9-b1ff-c78c69030272 --timeout 55
orx logs e7d210f9-7894-4df2-bdbd-d58896a9a055

orx exp run 67707b8a-2770-435a-ac08-e05983cfbfb9 --backend local
orx exp wait 67707b8a-2770-435a-ac08-e05983cfbfb9 --timeout 55
orx logs 8c10975f-a2f4-4176-b678-50a2d55aa962

orx exp run bc1d9ca0-2db0-4cd4-8c7b-99d1e7483dea --backend local
orx exp wait bc1d9ca0-2db0-4cd4-8c7b-99d1e7483dea --timeout 55
orx logs 240f6653-8b66-401d-ac34-cb7be2be9e8d

orx exp run a968b407-e661-4f5a-b803-b4d8baafe72b --backend local
orx exp wait a968b407-e661-4f5a-b803-b4d8baafe72b --timeout 55
orx logs b9495ac6-1e71-4dd5-9afd-9c81aa1d23bf

orx exp run d53b1809-609f-4885-a07d-c5f817380c24 --backend local
orx exp wait d53b1809-609f-4885-a07d-c5f817380c24 --timeout 55
orx logs e4e94c1c-fbe1-466f-aeb9-3f561b0b890a
```

## Candidate validation

```bash
uv run --frozen python repro/src/build_release_manifest.py
uv run --frozen python repro/src/check_release_candidate.py
uv run --frozen python hf_space_candidate/repro/src/evaluator_gate.py \
  --root hf_space_candidate
uv run --frozen marimo check notebooks/flow_matching_claims.py
git diff --check
```

## Exact clean-room upload simulation

```bash
hf download DineshAI/zl3akehFBq \
  --repo-type space \
  --revision f2b258ac5c887a907b40ae0a6176236c0d574016 \
  --local-dir <empty-candidate-directory>
```

The 102 paths in `upload-allowlist.txt` were then copied over that exact parent
tree. `text-sha256-manifest.tsv` was checked path by path, the evaluator gate
was rerun from the clean-room root, inline values were compared with the raw
CSV files, all 88 parent paths were checked for subset preservation, and all
102 payloads were scanned for common credential patterns.

## Approved publication

The first `hf upload` attempt made no changes because its create-repository
preflight hit the account's Space-creation rate limit. Publication then used
`huggingface_hub.HfApi.create_commit` directly against the existing Space with
parent commit `f2b258ac5c887a907b40ae0a6176236c0d574016`, 102
`CommitOperationAdd` operations, and no delete operations.

Result:

```text
adc03f7da795a88a5c7aaa19aa44ea6c2787c78a
```

## Post-publication verification

```bash
hf download DineshAI/zl3akehFBq \
  --repo-type space \
  --revision adc03f7da795a88a5c7aaa19aa44ea6c2787c78a \
  --local-dir <empty-published-verification-directory>
uv run --frozen python <published-root>/repro/src/evaluator_gate.py \
  --root <published-root>
git ls-remote origin refs/heads/master
```

The independent download matched all 102 payload hashes, retained every
protected parent path, passed canonical traversal, and matched displayed
numbers to raw CSV before the publication surface was committed to GitHub.
