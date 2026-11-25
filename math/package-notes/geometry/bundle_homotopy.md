# `bundle_homotopy` notes

[Package API](../../../libs/geometry/bundle_homotopy/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Reuses [B03 metrics/embeddings/images](../../../libs/geometry/bundle_complements/README.md), [K06 nearby-projection comparisons](../../../libs/algebra/spectral_splitting/README.md) and interval local-to-global principles, [B02 operations](../../../libs/geometry/bundle_operations/README.md).
Shared real/complex constructions are in `Homotopy.Over`.

### Conventions

[Real-line examples](../../../libs/geometry/bundle_homotopy/src/Homotopy/Examples/Mobius.ref) construct circle bundles from signs on two-point boundaries.
[Complex-line examples](../../../libs/geometry/bundle_homotopy/src/Homotopy/Examples/CircleLine.ref) construct 2-sphere bundles from complex unit-circle coordinates.
Expose actual `Fiber` and `bundle` respectively.

`alignedIsomorphismExists` in `Clutching.With.Pullback` and `With.Sum` groups comparison isomorphisms and local-frame compatibility `alignment`.
Compatibility: \(h_-g=g' h_+\).
The same real API requires explicit gauges on both disks for isomorphism criteria.

## Historical validation

Historical upstream [PR #43](https://github.com/pdf-jube-joba/ref-type/pull/43), implementation `2f786058`:

| Input | Result |
| --- | --- |
| Package `ca2a13df` | 4,728 target/dependency modules accepted |
| Workspace `ad9d9af9` | 7,557 modules accepted on same-snapshot retry after a save-time timeout |
| Rust / integration tests | 383 / 401 passed; CLI tests, format, and Clippy passed |

Successful runs reported zero save failures, recoveries, duplicate/rerun checks, or lost steps.
