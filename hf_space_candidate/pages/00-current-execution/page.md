# CURRENT executed evidence — read this before the legacy pages

This page records the current executable reproduction. The preserved
**LEGACY judged baseline** pages later in the logbook contain the obsolete
3-dimensional script, including `c2 = c1`, arbitrary thresholds, and an
ImportError. They remain immutable historical evidence and are not the code
or output assessed below.

## Actual ORX run

| Field | Recorded value |
| --- | --- |
| Run ID | `83508b8b-b868-4a51-8a5e-47018b7ef0dd` |
| Git commit cloned by runner | `a28a88e192d99c17ed6a98b633a5766d3bb2d019` |
| Status | `done`, exit code 0 |
| ORX duration | `1m00s` |
| Captured stdout size | `460,987` bytes |
| Hardware | local Apple arm64 CPU, 8 logical cores; no GPU |
| Environment | Python 3.12.11; `uv.lock`; 36 resolved packages |
| Fixed command | `uv sync --frozen && uv run --frozen python repro/src/verify_fm.py` |

The following is a literal excerpt from `orx logs
83508b8b-b868-4a51-8a5e-47018b7ef0dd --head`:

```text
CLAIM 1: VERIFIED
Independent symbolic limits: current/d^3 -> 5; prior/d^4 -> 6
Dimensions=[1, 2, 4, 8, 16, 32, 64, 128, 256];
steps=[8, 16, 32, 64, 128, 256, 512];
epsilon=[0.0, 0.02, 0.04, 0.08]; exact rows=252
Negative controls: 3/3 rejected
CLAIM 2: VERIFIED
Distinct relaxed-assumption witness: H3=False, H4=True;
dimensions=[1, 2, 4, 8, 16, 32, 64, 128, 256];
deltas=[0.375, 0.25, 0.125, 0.0625]; exact rows=648
Independent Claim 2 limit: factor/d^3 -> 1 + delta**(-4);
negative controls=3/3 rejected
CLAIM 3: VERIFIED
Exact theorem schedule rows=80; complexity rows=36;
uniform/nonuniform work ratios at delta=2^-10=
[6458175738.26, 13490411542.03, 14806549253.44, 15105269144.23]
Negative controls=3/3 rejected
CLAIM 4: VERIFIED
Exact correlated-Gaussian W2 rows=1008; rho=[0,0.25,0.5,0.75];
H3/H6/H7 certified; matrix checker difference=6.31e-16
Negative controls=3/3 rejected
CLAIM 5: VERIFIED
Independent unequal-marginal rows=280; H8 and Lemma 1 block identities
certified; independent matrix difference=6.94e-17
Negative controls=3/3 rejected
CLAIM 6: VERIFIED
Integration-by-parts rows=27; maximum residual=2.22e-16;
kernel derivative order 3 -> 2 plus coupling score
Negative controls=3/3 rejected
```

The same log then prints every contract, source audit, method, raw CSV,
independent checker, negative-control result, runtime record, evaluation, and
limitation between explicit `BEGIN EVIDENCE FILE` / `END EVIDENCE FILE`
markers. Total raw rows are 2,331. Any contract failure or accepted negative
control raises an exception and makes the fixed command exit nonzero.

## Published machine-readable artifacts

These files are text payloads in this same Space revision, not unavailable
local references:

| Claim | Raw rows | Raw file SHA-256 |
| --- | ---: | --- |
| 1 | 252 | `680cb1998f5c9c33955081a63f1a196f05fd8b204a7d31c93cb47134adb04289` |
| 2 | 648 | `625fce232d119f0e6570f4cf0ade989479b6d8516b70d414ed8293740eac7225` |
| 3 | 80 schedule + 36 work | `7d4f06a81150effcc5c4a368ece06c63241a2ca76f0e79c0f6a8955dd416e2f6` and `9f4fb0d27d74f440bcd389f54fc4e3533b56773cb0d4e86b067f18b76ca47c89` |
| 4 | 1,008 | `8c7529f14e80f0e37c48cab6e64cc32a7c749b62f99f13a7bb111df19bc223db` |
| 5 | 280 | `b1db45993542f9e4f769990cd716523750edb0d3406338ffd859ddf2387c31bf` |
| 6 | 27 | `de1a981576287e123926e72c7b06e068d4f0c43427453e9630edf59e00647ab0` |

The next six pages expose representative rows, the executable formula, the
assumption witness, independent-checker output, and deliberately failing
control for each claim so assessment does not depend on following a file link.

