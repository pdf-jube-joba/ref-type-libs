# Stable clutching linearization (K07)

Construction details and records for [clutching_linearization](../../../libs/topology/clutching_linearization/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Entry: `clutching_linearization.Linearization`.
Reuses K04 Laurent approximation, K06 spectral splitting, K01 bundle classes/K0.
Shears/signed swaps share `linear_algebra.Commutative.Blocks`, `Rotation` implementations.

`algebra.Polynomial.Over.Finite` exposes finite coefficients/operations/padding over arbitrary commutative rings.
Existing field `galois` coefficient operations and `polynomial_linear_algebra.Field.Representatives.exists` share it.
Expose K04 `Circle.Coefficients.valueContinuous` and use evaluation continuity.

## Connecting proofs

Compare adding monic-companion linear factors with triangular blocks by continuous similarity.
Zero factors increase rank corrections; outside-circle factors preserve corrected indices.
Error-controlled Laurent approximation of arbitrary invertible homotopies and endpoint comparisons prove choice independence.
Common shift/degree sum presentations give polynomial spectral-index additivity.
Standard-loop recovery and clutching products give both inverse identities for the basic product theorem.

## Validation and resuming

Historical upstream [PR #46](https://github.com/pdf-jube-joba/ref-type/pull/46):

| Input | Result |
| --- | --- |
| Full K07 with nilpotent/sum examples `6c784da7` | 1,505 modules accepted (`k07-complete.json`) |
| Matching-math workspace | 8,065 modules accepted (`k07-final-workspace.json`) |
| Earlier dependency closure `58f2d50a` | 5,781 modules accepted |
| Rust workspace / format / Clippy | 383 tests passed; format and Clippy passed |

Library runs exited 0 with zero save failures; final runs reported zero recoveries, duplicates, or lost steps.
See [checking the libraries](../../../libs/USAGE.md) for fresh runs and historical-record scope.
