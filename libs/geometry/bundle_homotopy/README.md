# Bundle homotopy invariance and clutching (B04)

Reuses [B03 metrics/embeddings/images](../bundle_complements/README.md), [K06 nearby-projection comparisons](../../algebra/spectral_splitting/README.md) and interval local-to-global principles, [B02 operations](../bundle_operations/README.md).
Shared real/complex constructions are in `Homotopy.Over`.

## Public API

Entry: `bundle_homotopy.Homotopy[].Over`.

| API | Constructions and proofs |
| --- | --- |
| `Cylinder.endpointIsomorphismExists` | Compare bundle endpoints over compact-Hausdorff/interval products |
| `For.Pullbacks.Along` / `Relative` | Compare homotopic pullbacks, prove identity on fixed subsets |
| `For.Extensions` / `To` | Relative automorphism/isomorphism extension along cofibrations |
| `For.Contractible` / `Disks.Triviality` | Trivialize arbitrary bundles over contractible compact spaces/closed disks |
| `Clutching.With` / `Pullback` | Construct two-open-set transition bundles and pullback comparisons |
| `Clutching.Homotopy` / `With.Sum` / `With.Stabilize` | Send transition homotopies, block sums, stabilization to isomorphisms |
| `Disks.Hemispheres.Cover` | Actual two-disk-pushout/sphere homeomorphisms, closed-hemisphere gluing |
| `Disks.Clutched` / `Homotopy` | Boundary GL clutching and disk-restriction trivializations |
| `Disks.Clutched.Comparison.diskGaugeCriterion` | Equivalence of compatible boundary gauges on both disks and bundle isomorphisms |
| `Homotopy.Examples.Mobius` / `CircleLine` | Real sign-transition and complex unit-circle-transition lines |

[Real-line examples](src/Homotopy/Examples/Mobius.ref) construct circle bundles from signs on two-point boundaries.
[Complex-line examples](src/Homotopy/Examples/CircleLine.ref) construct 2-sphere bundles from complex unit-circle coordinates.
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
For current commands and the scope of historical results, see [checking the libraries](../../USAGE.md).
