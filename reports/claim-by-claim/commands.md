# Reproduction command ledger

This ledger records the campaign's meaningful commands. Repeated read-only
`rg`, `sed`, `find`, `du`, `df`, JSON pretty-printing, hashing, and Git status
inspections are grouped by purpose. Secret values and ORX-generated run
wrappers are intentionally excluded.

## Startup and source audit

```bash
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx projects --json
orx project view e6e79c00-6b6b-435d-9a5c-1f049d1e0226
orx runs e6e79c00-6b6b-435d-9a5c-1f049d1e0226
git branch -a
git status --short
git rev-parse HEAD
git rev-parse master
git ls-remote origin refs/heads/master
df -h .
env | sed 's/=.*//' | sort
curl --fail --location --user-agent 'Mozilla/5.0 OpenResearch-Reproduction/1.0' \
  https://ar5iv.labs.arxiv.org/html/2606.16610
orx paper 2606.16610 --full
```

The live verdict snapshot was retrieved from
`ICML-2026-agent-repro/verdicts`, pinned to its repository revision, and
filtered by the exact `space_id == "DineshAI/zl3akehFBq"`. The judged Space
was downloaded at the exact revision below:

```bash
git clone https://huggingface.co/spaces/DineshAI/zl3akehFBq
git checkout af641c4e7cc7775c33d10295b73ef75347a7ab1b
```

The tree, SHA-256, and byte manifests were then generated with `find`,
`sha256sum`/`shasum`, and deterministic sorting.

## Fixed baseline

```bash
orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Frozen judged baseline with UV lock" \
  --run-command 'uv sync --frozen && uv run --frozen python repro/src/verify_fm.py'
git fetch origin
git checkout orx/frozen-judged-baseline-with-uv-lock
git add pyproject.toml uv.lock
git commit -m "Pin UV environment for baseline"
git push origin orx/frozen-judged-baseline-with-uv-lock
orx exp run 574c8893-12f1-4257-be92-e5958491b672 --backend local
orx exp wait 574c8893-12f1-4257-be92-e5958491b672 --timeout 480
orx logs 3dbc116c-d274-4baa-9b4c-4c8ce89f3b1e
```

## Stacked claim experiments

Every child inherited the fixed command unchanged. The repeated Git lifecycle
was `git fetch origin`, `git checkout <branch>`, scoped edits, `git add`,
`git commit`, and `git push origin <branch>`.

```bash
orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Claim 1 exact Gaussian theorem audit" \
  --parent 574c8893-12f1-4257-be92-e5958491b672
git commit -m "Add exact Gaussian Claim 1 verifier"
orx exp run 2eb1322d-1f0c-4d18-9fe7-c1131477a6e7 --backend local
orx exp wait 2eb1322d-1f0c-4d18-9fe7-c1131477a6e7 --timeout 480
orx logs 28b00e20-fd18-41a4-a0f7-bb0ad19ac5fc

orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Claim 2 conditional-only early stopping" \
  --parent 2eb1322d-1f0c-4d18-9fe7-c1131477a6e7
git commit -m "Verify conditional-only early stopping"
orx exp run b1863947-3b15-4ccb-98c4-35d06e589570 --backend local
orx exp wait b1863947-3b15-4ccb-98c4-35d06e589570 --timeout 480
orx logs 18d756f0-3ae2-4389-b44c-d8392da4a305

orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Claim 3 exact non-uniform schedule" \
  --parent b1863947-3b15-4ccb-98c4-35d06e589570
git commit -m "Verify exact non-uniform schedule"
orx exp run ea6ba0ff-fe45-45c2-bf6c-8ab5f9f7beb2 --backend local
orx exp wait ea6ba0ff-fe45-45c2-bf6c-8ab5f9f7beb2 --timeout 480
orx logs a3c1ef8e-dcc9-4810-b089-894eaac12de7

orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Claim 4 exact Wasserstein decomposition" \
  --parent ea6ba0ff-fe45-45c2-bf6c-8ab5f9f7beb2
git commit -m "Verify Wasserstein error decomposition"
orx exp run 8accc6f1-743f-4525-b544-c94c4cf3b522 --backend local
orx exp wait 8accc6f1-743f-4525-b544-c94c4cf3b522 --timeout 480
orx logs 941d715c-2b56-47ae-9079-045d314bda44

orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Claim 5 independent marginal specialization" \
  --parent 8accc6f1-743f-4525-b544-c94c4cf3b522
git commit -m "Verify independent marginal specialization"
orx exp run 8874fee0-fffa-4d5a-af3e-1b7f19432be9 --backend local
orx exp wait 8874fee0-fffa-4d5a-af3e-1b7f19432be9 --timeout 480
orx logs 28983604-ad8e-4505-95b8-09f5c45db25b

orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Claim 6 integration-by-parts mechanism" \
  --parent 8874fee0-fffa-4d5a-af3e-1b7f19432be9
git commit -m "Verify integration-by-parts mechanism"
orx exp run e739c91d-7c52-4a91-8d07-b89f75a9a237 --backend local
orx exp wait e739c91d-7c52-4a91-8d07-b89f75a9a237 --timeout 480
orx logs f2f98137-4beb-4f45-a539-e0d7a2361882
```

The dominated Claim 1 Monte Carlo sibling was created for experimental
design comparison but intentionally not run after the exact deterministic
specialization proved stronger.

## Release-candidate validation

```bash
orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Cumulative evidence release candidate" \
  --parent e739c91d-7c52-4a91-8d07-b89f75a9a237
uv run --frozen python repro/src/build_report_assets.py
uv run --frozen marimo check notebooks/flow_matching_claims.py
uv run --frozen marimo export html notebooks/flow_matching_claims.py \
  -o <temporary-directory>/notebook.html --force
uv run --frozen python repro/src/build_release_manifest.py
uv run --frozen python repro/src/check_release_candidate.py
git diff --check
```

The final release regression uses the same inherited command:

```bash
orx exp run 77a1916b-2a06-446e-befb-2fc0e847b802 --backend local
orx exp wait 77a1916b-2a06-446e-befb-2fc0e847b802 --timeout 480
```

## Approved publication and independent verification

The approved release used the Hugging Face text-only commit API with the
63-path `hf_space_candidate/release/upload-allowlist.txt`, the protected
parent revision, and no delete operations. Authentication was supplied to the
client without printing credentials or a generated upload wrapper.

```bash
hf download DineshAI/zl3akehFBq \
  --repo-type space \
  --revision 22e4c6ccfea63d39df4fd57db0ddacb2a505b040 \
  --local-dir <temporary-verification-directory>
git ls-remote https://huggingface.co/spaces/DineshAI/zl3akehFBq HEAD
git push origin HEAD:master
git ls-remote origin refs/heads/master
```

The resulting Space revision is
`22e4c6ccfea63d39df4fd57db0ddacb2a505b040`. The independent download matched
all 63 uploaded path hashes, retained all 17 judged paths, and kept the 16
non-logbook judged files byte-identical.

## Judge-visible evidence repair

```bash
orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Judge-visible executed evidence" \
  --parent 77a1916b-2a06-446e-befb-2fc0e847b802
orx exp run 9daf03d6-6ccc-47ed-99da-f856a3296b54 --backend local
orx exp wait 9daf03d6-6ccc-47ed-99da-f856a3296b54 --timeout 480
orx logs 0a539277-4fa4-4894-8623-a823aeaf193b --head --bytes 50000
orx logs 0a539277-4fa4-4894-8623-a823aeaf193b --bytes 20000
orx create-experiment e6e79c00-6b6b-435d-9a5c-1f049d1e0226 \
  --title "Second cumulative evidence release candidate" \
  --parent 9daf03d6-6ccc-47ed-99da-f856a3296b54
```

The executed-evidence run cloned
`7e3ab5c3a71ac38f1d14a4722e2abbe468fe8fd4`, completed in 50 seconds, and
captured 476,391 bytes. The second candidate remains unpublished pending its
final regression and explicit release approval.
