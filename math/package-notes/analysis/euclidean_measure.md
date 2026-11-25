# `euclidean_measure` notes

[Package API](../../../libs/analysis/euclidean_measure/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

`euclidean_measure.Euclidean[n]` constructs outer measure from countable closed-box covers.
Volumes multiply side lengths; empty boxes are allowed.
Cover costs are volume series as extended-nonnegative lower cuts; `outer` rounds the infimum of these costs to a lower cut.

`outerNonnegative`, `monotone`, `outerEmpty`, `boundedByCover`, `greatestLowerBound` prove basic infimum properties.
`boxUpper` bounds box outer measure by volume.
`Countable.subadditive` proves countable subadditivity; `subadditivePair` finite subadditivity; `nullCaratheodory` measurability of outer-null sets.
`translationInvariant` proves translation invariance; `scaledVolume` gives box-volume transformation under nonnegative coordinate dilations.
`Positive[k].singletonNull` proves singleton outer measure zero in positive dimensions; `countableNull` extends to countable sets.
`Zero.singletonVolume` proves dimension-zero singleton outer measure one.

`Caratheodory` is the outer-measure splitting condition, closed under empty sets, complements, finite unions/intersections, giving finite additivity on disjoint sets.
`weave` interleaves two cover sequences with summed costs.
`CaratheodorySets.sigma` is the Carathéodory σ-algebra; `MeasureConstruction.measure` is the complete restricted outer measure.
`MeasureConstruction` provides translation invariance and countable null unions.
`Scaling` gives measurability/measure transformation under positive coordinate dilations.
`Borel` constructs the least σ-algebra containing Euclidean open sets.
`EuclideanBorel` proves open/Borel measurability in every dimension.

`CoverExpansion.outerRegular` identifies arbitrary-set outer measures with infima over containing open sets.
`InnerRegular.innerRegular` identifies measurable-set measures with suprema over contained compact sets.
Lower-cut equalities include infinite measure.
`BoxCompact.compact` proves closed-box compactness; `Exhaustion` gives increasing box exhaustion.
`GdeltaHull.finiteHull` encloses finite-outer-measure sets in Gδ sets of equal outer measure.

`BoxVolume.boxVolume` identifies closed-box outer measure with the product of side lengths.
`Hyperplane.null` proves coordinate hyperplanes null.
`GeneralDiagonal.formula` gives measurability/measure transforms for arbitrary diagonal dilations, including signs and zeros.
`RealLine` transports measure to the real line and gives interval lengths.
`RealLine.RiemannMap` constructs measure-integrable interval restrictions of arbitrary Riemann-integrable functions and identifies integral values.
`RealLine.CompletionAgreement.linkedRepresentative` compares arbitrary existing L1-completion representative sequences with measure-integrable representatives and equal integrals.
Select a subsequence with summable L1 successive differences from the original Cauchy sequence, then take its a.e. limit.
`linkedAgreement` gives this correspondence for arbitrary completion elements; `agreement` extracts integral equality.

## Examples

`Examples` contains examples of these results.
