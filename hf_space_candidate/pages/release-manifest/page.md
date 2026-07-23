# Protected revision and manifest

The exact judged Hugging Face revision is:

```text
DineshAI/zl3akehFBq@af641c4e7cc7775c33d10295b73ef75347a7ab1b
```

Its 17-path SHA-256 manifest is preserved at
`protected/judged-af641c4e-manifest.tsv`. The original root logbook is
preserved byte-for-byte at `protected/judged-logbook.json`; its manifest hash
is `bf69d302dad91e7da2a2af10876885ecc050b8818bcd54cfeaa6beeed0f7fa1b`.

Every original path remains in the candidate. The 16 paths other than the
root `logbook.json` remain byte-for-byte identical. The root logbook changes
only to make these three additive pages reachable; its judged bytes remain
available under `protected/`.

The release checker verifies:

1. the judged path set is a subset of the candidate path set;
2. protected hashes and byte counts match;
3. the original logbook snapshot has the judged hash;
4. every page referenced by the candidate logbook exists;
5. the upload allowlist contains only regular text files;
6. the upload SHA-256 manifest matches every allowlisted payload.

No Hugging Face update has occurred. Publication requires an explicit user
approval after the local release report.
