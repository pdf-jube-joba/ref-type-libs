# Bundle homotopy invariance and clutching (B04)

Construction details and records for [bundle_homotopy](../../../libs/geometry/bundle_homotopy/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Reuses [B03 metrics/embeddings/images](../../../libs/geometry/bundle_complements/README.md), [K06 nearby-projection comparisons](../../../libs/algebra/spectral_splitting/README.md) and interval local-to-global principles, [B02 operations](../../../libs/geometry/bundle_operations/README.md).
Shared real/complex constructions are in `Homotopy.Over`.

## Public API

[Real-line examples](../../../libs/geometry/bundle_homotopy/src/Homotopy/Examples/Mobius.ref) construct circle bundles from signs on two-point boundaries.
[Complex-line examples](../../../libs/geometry/bundle_homotopy/src/Homotopy/Examples/CircleLine.ref) construct 2-sphere bundles from complex unit-circle coordinates.
Expose actual `Fiber` and `bundle` respectively.

`alignedIsomorphismExists` in `Clutching.With.Pullback` and `With.Sum` groups comparison isomorphisms and local-frame compatibility `alignment`.
Compatibility: \(h_-g=g' h_+\).
The same real API requires explicit gauges on both disks for isomorphism criteria.

## Checks and integration records

Historical upstream [PR #43](https://github.com/pdf-jube-joba/ref-type/pull/43), implementation `2f786058`:

| Input | Result |
| --- | --- |
| Package `ca2a13df` | 4,728 target/dependency modules accepted |
| Workspace `ad9d9af9` | 7,557 modules accepted on same-snapshot retry after a save-time timeout |
| Rust / integration tests | 383 / 401 passed; CLI tests, format, and Clippy passed |

Successful runs reported zero save failures, recoveries, duplicate/rerun checks, or lost steps.
For current commands and the scope of historical results, see [checking the libraries](../../../libs/USAGE.md).
