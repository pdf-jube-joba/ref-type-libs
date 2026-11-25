# Bundle metrics, orthogonal complements, and isomorphism classes

Construction details and records for [bundle_complements](../../../libs/geometry/bundle_complements/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Entry: `bundle_complements.Complements.Over[K, field, conjugation, scalar]`.
Supply real/complex [vector_bundles](../../../libs/geometry/vector_bundles/README.md) scalars; operations use [bundle_operations](../../../libs/geometry/bundle_operations/README.md), orthonormalization/matrix continuity use [hermitian_frames](../../../libs/algebra/hermitian_frames/README.md).

## Metrics and finite embeddings

`For[X, F, bundle].embeddingExists` constructs finite partitions subordinate to trivializations on compact Hausdorff bases.
`Weighted` extends weighted local coordinates by zero off supports; `build` concatenates coordinates.
`FromPartition` derives zero kernels from weights summing to one.
Existing `PartitionOfUnity` and `ZeroExtension` prove extension-by-zero continuity.
Ambient dimension sums finitely many local dimensions; no connectedness/constant-rank assumption.

`Embedding` groups dimension, continuous bundle maps, fiberwise injectivity.
`FromEmbedding.metric` pulls back standard positive real/Hermitian metrics, with continuous evaluation on total direct sums.
`metricExists` applies this to finite embeddings.
`CoordinateEmbedding` turns continuous injective matrix families into actual continuous trivial-bundle maps.

## Projection images and orthogonal complements

`Finite.ImageBasis[map, idempotent]` processes columns of general idempotents to construct orthonormal image-spanning frames.
`Finite.ProjectionBasis` applies the shared construction to Hermitian projections, deriving coordinate reconstruction.

Projection uniqueness uses `Finite.Range.unique`; matrix/inverse-coordinate continuity uses L01/L03.

## Set presentations and naturality

`Representations[X, baseSpace].Presentation` pairs finite ambient dimension with continuous orthogonal projections.
`Realize[p].bundle` constructs image bundles.
`Equivalent p q` asserts isomorphism of two such bundles, allowing different ambient dimensions.
Prove equivalence laws; construct isomorphism-class set `Classes` using existing `std.Set.Quotient`.
`classCriterion` equates class equality with bundle isomorphism existence.

`Of[F, original, same].class` is the isomorphism class of general bundles on compact Hausdorff bases.
`Of.classification` compares realizations of projection presentations; `Comparison.criterion` equates general bundle isomorphisms with class equality.
Classes are subsets of all isomorphic projection presentations, independent of embedding/frame choices.

`Projection.Pullback.isomorphism` compares composed-projection images with pullbacks of image bundles.
Prove fiberwise compatibility for inclusions/projections/complements and both direct-sum directions.
`For.Pullback.metric` pulls back arbitrary continuous metrics.
`FromEmbedding.Pullback` pulls back embeddings, proving metric evaluation and image-projection agreement.
`Representations.Pullback.map` pulls back class sets; `onClass` gives representative formulas; `Of.naturality` compares general bundle classes.

## Examples

[Moving](../../../libs/geometry/bundle_complements/src/Complements/Over/Examples/Moving.ref) reuses L03 columns \((1,z)\), constructing metrics, complements, and trivial-sum isomorphisms.
Also uses equal classes for ambient dimensions one/two, square-map pullbacks, metric/projection/class naturality.
[FiniteBases](../../../libs/geometry/bundle_complements/src/Complements/Over/Examples/FiniteBases.ref) proves two-point compact Hausdorffness; applies embedding/metric existence to rank-zero/one bundles, zero bundles, and empty bases.
[Examples](../../../libs/geometry/bundle_complements/src/Complements/Examples.ref) instantiates real/complex scalars.

## Coordinate families and general idempotents

`CoordinateFamily` turns arbitrary continuous coordinate-linear families into trivial-bundle maps without injectivity.
`CoordinateEmbedding` shares that construction, also exposing finite embeddings when injective.
[uniform_approximation](../../../libs/analysis/uniform_approximation/README.md) uses this API/image comparisons to return matrix approximations to bundle endomorphisms.

`Over.Idempotents[n]` handles real/complex idempotents without self-adjointness.
`Algebra`, `With` give complements, finite image bases, both kernels, and direct sums.
`Image` gives image bundles/inclusions/projections/complements/pullbacks; `Comparison` gives invertible-intertwiner isomorphisms; `Gap` gives open nearby-comparison invertibility.
This B09 entry applies K06 image construction to the same `Finite.ImageBasis` and general scalars.

## Validation

Historical upstream [PR #41](https://github.com/pdf-jube-joba/ref-type/pull/41), merged at `6bf92837`.
The K06 shared-basis recheck at `e3aecc2e` accepted 4,345 reused dependency-closure modules with zero save failures or worker recoveries.
The later B09 idempotent entry accepted 569 modules including dependencies, with zero save failures.
See [checking the libraries](../../../libs/USAGE.md) and [K06 validation](../algebra/spectral_splitting.md#validation-and-resuming) for reruns and historical context.
