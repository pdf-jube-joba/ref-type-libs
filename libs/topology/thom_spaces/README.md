# `thom_spaces`

Disk/sphere bundles, Thom quotients, metric/suspension/direct-sum comparisons, finite CW pair types and relative singular theory.

Thom quotients collapse sphere bundles together with an added basepoint: rank zero gives X+, and empty bases give a point. Metrics are continuous and positive.

| Entry | Purpose |
| --- | --- |
| `Thom.Real.For.Change` / `Thom.Complex.For.Change` | Total/disk/Thom homeomorphisms for arbitrary continuous metrics |
| `Over.For.Change.sphereHomeomorphism` | Scalar-shared normalized sphere homeomorphisms |
| `Thom.Real.Trivial.Compare` / `Thom.Complex.Trivial.Compare` | Trivial Thom/disk-suspension homeomorphisms in real dimensions \(n\), \(2n\) |
| `Thom.Real.DirectSum.Compare` / `Thom.Complex.DirectSum.Compare` | Arbitrary-metric sum Thom/iterated-Thom homeomorphisms |
| `Over.For.With.Radial.Boundary.cofibration` | Sphere-inclusion cylinder retractions |
| `Over.For.With.ThomPair.mappingConeComparison` | Apply `puppe_sequences.Pair.equivalence` to added-point pairs |
| `Over.For.With.ThomPair.Collar` | Strong open-radius retractions, `goodPair` |
| `Collar.Homology[z].isomorphism` | Added-point disk-pair integral-relative/reduced-Thom homology isomorphisms |
| `Collar.Cohomology[M, z].isomorphism` | Reverse arbitrary-module integer-degree cohomology isomorphisms |
| `Collar.Homology[z].ordinaryIsomorphism` / `Collar.Cohomology[M, z].ordinaryIsomorphism` | Actual disk-pair comparisons after removing added points |
| `DiskSuspension.Step.Cylinder.suspensionHomeomorphism` | Pointed successor-disk/existing `puppe_sequences.Suspension` suspension homeomorphisms |
| `ZeroDiskSuspension.homeomorphism` | Zero-disk/\(X_+\) homeomorphisms |
| `SuspensionPresentation.comparison` | Arbitrary-natural-degree comparisons with existing-suspension sequences |
| `FirstSuspensions.once` / `FirstSuspensions.twice` | Direct one/two-fold existing suspension homeomorphisms |
| `Over.For.With.Contraction.equivalence` | Disk/base homotopy equivalences |
| `Real.For.FiniteBase.pairFiniteType` / `Complex.For.FiniteBase.pairFiniteType` | Actual disk pairs equivalent to finite CW complexes/subcomplexes |
| `FiniteBase.PairModel[model]` | Model `data.space`, `data.complex`, `data.part` and `comparison`, `relativeEquivalence` |
| `PairModel.Homology[z].isomorphism` / `PairModel.Cohomology[M, z].isomorphism` | Finite-CW-model integral homology/arbitrary-module cohomology comparisons |
| `Over.For.With.FiniteBase.Coordinates.Cell.pairExists` | Cellwise boundary-compatible disk/sphere coordinates |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/topology/thom_spaces.md)
