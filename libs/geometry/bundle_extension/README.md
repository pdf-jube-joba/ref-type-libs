# `bundle_extension`

Tietze, neighborhood extension of bundles/maps/isomorphisms over closed subspaces, shrinking comparisons and stabilization.

Extensions start from closed subsets of compact Hausdorff spaces and land in open neighborhoods. Empty subsets and componentwise varying finite ranks are included.

| Entry | Purpose |
| --- | --- |
| `Real.tietze`, `Complex.tietze` | Extend real/complex continuous functions to all \(X\) |
| `Real.Components`, `Complex.Components` | Extend arbitrarily indexed component families |
| `Real.Matrices`, `Complex.Matrices` | Entrywise extension of finite rectangular matrices |
| `Real.Square`, `Complex.Square` | Invertible extensions to open neighborhoods, continuous inverses/restriction laws |
| `RealProjections`, `Complex.Projections` | Idempotent neighborhood extensions, image bundles/restriction comparisons |
| `RealBundleExtension`, `Complex.BundleExtension` | Neighborhood extension of arbitrary finite-rank bundles |
| `Sections`, `RealSections.extend`, `ComplexSections.extend` | Extend closed-subspace sections of \(X\)-bundles globally |
| `RealMaps.extend`, `ComplexMaps.extend` | Extend closed-subspace maps between \(X\)-bundles globally |
| `RealIsomorphisms.extend`, `ComplexIsomorphisms.extend` | Extend closed-subspace isomorphisms to open neighborhoods |
| `RealLocalIsomorphisms.extend`, `ComplexLocalIsomorphisms.extend` | Extend isomorphisms between neighborhood bundles to smaller common neighborhoods |
| `CompactNeighborhood` | Compact closed neighborhoods inside open ones; lift relatively open neighborhoods to \(X\) |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/bundle_extension.md)
