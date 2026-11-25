# Validation records

Checked changes based on main `6e2106dfaf0a5370e84213a1c60fccf126d359a4` on 2026-11-19.
This base includes `dce3d353e75972c507928253d6c33420f6f55a0f`.
No Rust/checker source changes.
Rebuilt the checker from current sources; used Rust 1.100.0 release builds.
Machine-readable summaries, input/result SHA-256, raw-record locations: [verification.json](verification.json).

## Targets and dependency closure

`--full-check-local` **rechecked all 137 modules of `morse_lemma` and accepted them**.
Includes ordinary/parameterized top existence, index connections, local constancy, all standalone examples.
Focused checks also verify the entire loaded dependency closure.

| Metric | Result |
| --- | --- |
| Target modules rechecked | 137 / 137 |
| Verified modules including dependencies | 1,926 |
| Newly checked modules including dependencies | 142 |
| Matching verified modules reused | 1,784 |
| source steps | 1,952 |
| Elapsed time | 36.49 seconds |
| Peak RSS | 1,936,868 KiB |
| Worker recoveries/duplicates/reruns/missing steps | All 0 |
| Cache corruption/save failures | Both 0 |

README usage examples also accepted from standalone packages.
No additional axioms or unproved parts.
Uses existing function/set extensionality.

## Full library

Full `python3 scripts/check_all.py libs` check **failed**.
Enumerated 111 packages/15,524 targets; accepted 68 scopes/7,522 targets, then stopped at existing `euclidean_sobolev`.
Total 461.73 seconds, peak RSS 2,167,828 KiB.
Zero corrupt caches/save failures/worker recoveries.

Stop location: `positiveNonzero _ (positive x)` in `Reciprocal` module arguments at [Euclidean/Order/Weight.ref:14](../../analysis/euclidean_sobolev/src/Euclidean/Order/Weight.ref#L14).

```text
Resolution Error: module arguments do not allow inference holes (`_` or `?`)
```

File matches base main; SHA-256: `c98df52b2a9936e8e6ac7d5760e45ce4264498fe13fa6308d9a5b485ec23c802`.
Confirmed all full-run sources/targets unchanged before/after; 1,738 target-check sources match the full snapshot.

Remaining **8,002 targets are unverified by the full driver**.
Includes the failed scope and subsequent unreached scopes.
G13/full-dependency success comes from the separate focused recheck above.
No full-check success claimed.

## Rust checks

`cargo test --workspace --locked -j 4` accepted: 34 suites, **384 passed / 0 failed / 0 ignored**.
Changes only affect math libraries, registration, and documentation; Rust test sources remain as checked.
`git diff --cached --check` also passed.

## Reproduction commands and scope

```sh
cargo build -p cli --release --locked -j 4
target/release/cli libs/geometry/morse_lemma --full-check-local --memory-mib 4096 --cache-stats --time-limit-seconds 1800 --report-json /tmp/g13-target.json
python3 scripts/check_all.py libs --memory-mib 4096 --cache-budget-mib 12288 --min-free-mib 512 --time-limit-seconds 3600 --state-dir /tmp/g13-repository-check
cargo test --workspace --locked -j 4
```

Used matching shared workspace caches.
No cold check rechecked every dependency proof without cache.
Scopes after the full-driver stop were not run; the existing error above blocks full completion.
