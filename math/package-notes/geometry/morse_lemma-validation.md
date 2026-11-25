# Morse-lemma validation records

Historical checks from 2026-11-19, based on upstream main `6e2106dfaf0a5370e84213a1c60fccf126d359a4`, using a rebuilt Rust 1.100.0 release checker.
[The machine-readable record](morse_lemma-verification.json) preserves source/binary hashes, metrics, and raw-record locations.
These results do not establish acceptance of the current checkout.

## Targets and dependency closure

`--full-check-local` rechecked all 137 `morse_lemma` modules, including ordinary/parameterized existence, index comparisons, local constancy, and standalone examples.
The dependency closure accepted 1,926 modules: 142 newly checked and 1,784 reused.
README examples also passed as standalone packages.
Cache corruption/save failures, worker recoveries, duplicates, reruns, and missing steps were all zero.
No cold run rechecked every dependency proof without cache.

No new axioms or unproved parts were added; the implementation uses existing function/set extensionality.

## Full library

The workspace driver accepted 68 scopes/7,522 of 15,524 targets across 111 packages, then failed in `euclidean_sobolev` at [Euclidean/Order/Weight.ref:14](../../../libs/analysis/euclidean_sobolev/src/Euclidean/Order/Weight.ref#L14):

```text
Resolution Error: module arguments do not allow inference holes (`_` or `?`)
```

The failing `positiveNonzero _ (positive x)` module argument matched the upstream base; sources and targets were unchanged during the run.
The remaining 8,002 targets, including the failed scope, were unverified by this run.
G13 and its closure passed in the separate focused check above.

## Rust checks

The upstream workspace tests passed: 34 suites, 384 tests, zero failures or ignored tests.
`git diff --cached --check` also passed; no Rust/checker source changes were made.

## Current checks

Use the [package and workspace checking instructions](../../../libs/USAGE.md) for a fresh run.
