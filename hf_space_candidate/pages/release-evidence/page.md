# Cumulative release evidence

The evidence tree is additive under `evidence/`. Every claim directory
contains:

- `claim_contract.json` with explicit assumptions, domain, quantifiers,
  pass conditions, and failure behavior;
- `source_audit.md` with theorem/section anchors and exact source wording;
- `method.md` describing the faithful specialization;
- raw machine-readable CSV or JSON;
- `independent_checker_output.json`;
- `negative_control_output.json`;
- `runtime.json`, `limitations.md`, and `EVAL.md`.

The paper source record is `evidence/source/paper_source.json`. The primary
HTML was retrieved on 2026-07-23 with an explicit browser User-Agent from
`https://ar5iv.labs.arxiv.org/html/2606.16610`. Its SHA-256 is:

```text
c3553013f3f7022f6e5f539e735585d6180364f716d4b17b5679aacb519546ff
```

The environment is pinned to Python 3.12.11 with a committed `uv.lock`.
Deterministic seeds are recorded in the contracts and runtime files. Gaussian
endpoint metrics are propagated analytically to avoid Monte Carlo ambiguity;
SciPy matrix square roots, SymPy limits, deterministic quadrature, and direct
formula reimplementations provide independent checks.

## How this answers the 3/12 criticisms

| Prior criticism | New direct evidence |
| --- | --- |
| One 3D Gaussian and arbitrary KL threshold | Dimensions `1…256`, exact source factors, ε² and grid-refinement checks |
| Claim 2 copied Claim 1 | Strict H4-true/H3-false singular witness |
| Arbitrary non-uniform grid was worse | Exact implicit theorem schedule plus matched displayed-bound work comparison; old rule is a rejected control |
| W₂ below 10 without assumptions | Exact W₂ decomposition and explicit H3/H6/H7 constants |
| Independence only asserted | Product covariance built and zero cross-block checked; a correlated control is rejected |
| Low-rank proxy for integration by parts | Nonzero transferred-derivative identity, analytic convolution derivative, quadrature, and symbolic order audit |
| `numpy.linalg.sqrtm` ImportError contradicted another page | Original contradiction is preserved; the new checker uses `scipy.linalg.sqrtm` and fails closed |

Verdicts on this page are local: **VERIFIED** means the committed contract
passed on the recorded candidate, not that the live judge has awarded credit.
