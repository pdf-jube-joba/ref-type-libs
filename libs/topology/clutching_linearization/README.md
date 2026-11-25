# Stable clutching linearization (K07)

Entry: `clutching_linearization.Linearization`.
Reuses K04 Laurent approximation, K06 spectral splitting, K01 bundle classes/K0.
Shears/signed swaps share `linear_algebra.Commutative.Blocks`, `Rotation` implementations.

| API | Constructions and proofs |
| --- | --- |
| `linear_algebra.Commutative.Blocks` | Upper/lower shears, inverses, Schur decompositions, invertible paths |
| `Uniform` / `MatrixNeighborhoods.Perturbation` | Common matrix-neighborhood errors, compact-base invertibility margins |
| `On.Matrices.exists` / `Result` | Invertible Laurent approximations/homotopies, endpoint equalities, continuous two-sided inverses |
| `LaurentNormal.exists` / `finiteExists` | Polynomials clearing negative powers, finite coefficients |
| `LaurentNormal.Matrices.commonExists` / `finiteMatrixExists` | Common shifts/degrees/finite coefficient arrays |
| `Coordinates.At.frame` / `Families` | Finite coordinate-block isomorphisms, continuous families |
| `Companion.FromRow.Eigen` | Eigenvectors to polynomial kernels, unit-circle eigenvalue exclusion |
| `Companion.Families.Separated` / `KClass` | Continuous companion matrices, spectral image bundles/K0 differences |
| `On.SpectralIndex.Pullback.naturality` / `Sum.Difference.additivity` | Spectral differences: pullback naturality/sum additivity |
| `On.SpectralHomotopy.invariant` | Endpoint K0 differences agree for unit-circle-separated families |
| `On.Matrices.Clutched.Scaling` / `Normalized.With.Shifted.Leading.Clutching` | Clutching comparisons under scaling/normalization perturbations |
| `CanonicalProjection.recovered` / `loopRecovery` | Spectral projection/standard-loop recovery for \(c(1-P)\) |
| `On.CanonicalIndex.recovery` / `ScalarChoice.independent` | Original/spectral-image isomorphisms, K0 recovery, auxiliary-scalar independence |
| `On.SpectralIndex.Canonical.invariant` / `Examples.Nilpotent.canonicalInvariant` | Canonical spectral models and explicit \(c=2\) examples |
| `On.Matrices.Construction.Clutching.shiftedComparisonExists` | Stabilized shifted-loop/spectral-normal-form comparisons |
| `On.Matrices.ChoiceComparison.independent` / `Inverse.value` | Inverse classes independent of Laurent/shift/degree/normalization choices |
| `Inverse.Naturality.naturality` / `Inverse.Homotopy.With.invariant` | Continuous-pullback naturality, invertible-loop homotopy invariance |
| `On.DirectSum.additivity` | Inverse-class additivity for arbitrary invertible loop sums |
| `Inverse.Reconstruction.reconstruction` | Recover reduced clutching classes as line differences times inverse classes |
| `On.ProjectionInverse.recovery` / `standardFormula` | Inverse classes of \(zP+(1-P)\) equal original image classes |
| `RowOrders.Monic.recovery` / `LinearPolynomial.Index.recovery` | Polynomial recovery, especially \(zI-A\)/spectral-index identification |
| `Examples.Empty` / `Examples.Nilpotent` | Rank-zero/nilpotent/basic-product/inverse-class/sum examples |

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

Working branch: `math/k07-clutching-linearization`; [PR #46](https://github.com/pdf-jube-joba/ref-type/pull/46).
Shared cache: `libs/refcache`.
Fast-forward existing branches through GitHub integration; confirm equal local/remote trees before saving.

| Check | Saved input | Result |
| --- | --- | --- |
| All K07 targets/references | `bb2e4c2f` | 1,491 modules, accepted, exit 0, save failures 0 |
| K07 full dependency closure (earlier input) | `58f2d50a` | 5,781 modules, accepted, exit 0, save failures 0 |
| Full workspace (earlier input) | `0a2e29ec` | 7,878 modules, accepted, exit 0, save failures 0 |
| Rust workspace/format/Clippy | Same checker | 383 tests passed; format and warnings-as-errors Clippy exited 0 |
| Outside-factor degree adjustments | `073b61c3` | accepted, exit 0, save failures 0 |
| Matrix sums/power addition | `13a479b9` | accepted, exit 0, save failures 0 |
| Polynomial-sum/block identification | `8bdb90ae` | accepted, exit 0, save failures 0 |

`On.DirectSum.additivity` on `1972b9e5`: accepted, exit 0, save failures 0.
General inverse-class sum additivity verified.
Full K07 including nilpotent/sum examples: `6c784da7`, 1,505 modules, accepted/exit 0/save failures 0 (`k07-complete.json`, roughly 189 seconds).
Same-math full workspace: 8,065 modules, accepted/exit 0/save failures 0 (`k07-final-workspace.json`, roughly 26 seconds).
Shared cache reused; zero recoveries/duplicates/lost steps.
Subsequent changes only public index/roadmap/validation records.
Final PR-head confirmation/main merge remain.

```sh
target/debug/cli libs --parse-only --save-source-snapshot /tmp/k07-resume/final.source.json
target/debug/cli libs --source-snapshot /tmp/k07-resume/final.source.json --memory-mib 10240 --cache-dir libs/refcache --cache-budget-mib 12288 --diagnostics compact --time-limit-seconds 3600 --report-json /tmp/k07-resume/final.json
```

For K07 alone, input `libs/topology/clutching_linearization` and add `--module clutching_linearization`.
Omit `--module` for full package dependencies.
Confirm process exit 0 and report `outcome=accepted`, `storage.save_failures=0`.
