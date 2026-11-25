# Disk bundles, sphere bundles, and Thom quotients

Construction details and records for [thom_spaces](../../../libs/topology/thom_spaces/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Implements C02 disk/sphere bundles and Thom spaces.
For real/complex continuous metrics, constructs metric-independent comparisons, trivial suspensions, sum iterated quotients, finite-CW-pair types, cofibration/relative-singular comparisons.

## Disk bundles and basepoints

Entry: `Thom.Over[K, field, conjugation, scalar].For[X, F, bundle].With[metric]`.
Metrics use continuous positive `bundle_complements`.
`DiskBundle` and `SphereBundle` are squared-norm sublevel/level sets with induced topologies.
Exposes `diskProjectionContinuous`, `sphereProjectionContinuous`, `sphereInclusionContinuous` and zero sections.

`Thom` adds a disk basepoint, then collapses sphere bundles together with it.
Hence rank zero gives \(X_+\), empty bases a point.
`class`, `point`, `collapsed`, `quotientContinuous` are basic quotient APIs.
`Thom.Collapse.Lift` descends continuous maps taking spheres to specified basepoints.

## Comparisons

Metric-change total maps send zeros to zero, other vectors to
\(v\mapsto\lVert v\rVert_h\lVert v\rVert_k^{-1}v\).
`Quadratic.Over` applies the same construction to continuous positive quadratic gauges.
Require real-scaling quadratic homogeneity, covering squared metrics and maximum disk-product models with one API.
Compact local bounds on standard-sphere coefficients and `CompactAction` tube lemmas also prove continuity at zero.
Complex cases use existing realification/real coordinates.

Sum comparisons pass through disk products \(\max(\lVert v\rVert^2,\lVert w\rVert^2)\leq1\).
`Thom.Iterated.homeomorphism` compares successive boundary collapse with simultaneous union collapse.
This presents relative Thom quotients of pullbacks to disk bundles.

`DiskSuspension[X, space, n]` is the disk-suspension model
\(((X\times D^n)\amalg\{*\})/(X\times\partial D^n\amalg\{*\})\)
`Step.Cylinder.suspensionHomeomorphism` constructs pointed existing-suspension homeomorphisms in every natural dimension.
Radially transport disks to head/tail maximum gauges; move head unit intervals to \([0,1]\).
General pair-cylinder/suspension comparison: `SuspendedPair.homeomorphism`; product/quotient continuity uses compact-Hausdorff-factor `RelationQuotient.Families`.
`SuspensionPresentation` inductively compares disks with arbitrary sequences starting at \(X_+\), then existing suspensions.
Inputs specify iteration, not disk-model comparison.
`FirstSuspensions` and real/complex examples compare direct one/two-level nested suspensions.

`Collapse.Relative` excises added isolated points from arbitrary pairs, identifying complements with originals.
`ordinaryIsomorphism` composes excision/collar comparisons, with actual unpointed \((D(E),S(E))\) relative domains/codomains.
No sphere-point assumption for rank zero/empty bases.

## Finite CW pairs

For finite CW bases, `FiniteBase.Coordinates.sphereFiniteType` identifies actual sphere bundles with finite CW complexes up to homotopy.
`Real.For.FiniteBase` and `Complex.For.FiniteBase` select standard real coordinates.
Present cellwise sphere bundles by two disk attachments; use cellular attaching approximations/attachment homotopy comparisons.
`FiniteBase.Coordinates.sphereCompact` and `diskCylinderHomeomorphism` give compact spheres and projection-mapping-cylinder/actual-disk homeomorphisms.
At cylinder tops, homeomorphisms agree with sphere inclusions.

`CWType.NativeSubcomplex.result` constructs finite CW structures on induced subcomplex topologies; `Cellularity` compares skeleton inclusions.
`PairTools` comparisons contain two subspace-preserving maps/both homotopies.
`CellAttachment.Subset.Homotopic` and `BaseEquivalence` transfer disk attachments to pair comparisons; `Inside` also adds new cells to specified subspaces.
`PairFiniteType` groups finite complexes/subcomplexes/actual pair equivalences.
`PairFiniteCellTypes` and `CellAttachment.Subset.Type` preserve pair types under arbitrary disk attachments inside/outside specified subspaces.
`SphericalAttachment.Of.Subsets` and `CellPresentation.Of.Comparison.Subsets` compare actual attachments to these pair types.
`FiniteBase.Coordinates.Cell.pairExists` constructs disk/sphere coordinates from common trivializations, retaining boundary agreement/squared norms.

`FiniteBase.Coordinates.pairFiniteType` inducts over base skeleta/finite cells, constructing actual \(D(E),S(E)\)/finite-CW pair equivalences.
Each base cell adds sphere parts by two attachments, then disk products as single disk cells.
Approximate attachments into appropriate skeleta for inside/outside cells; compose preserving maps/homotopies.
`PairModel` retains both maps/homotopies, passing to `singular_cohomology.Relative.Equivalence`.

## Examples

[Examples.Real](../../../libs/topology/thom_spaces/src/Thom/Examples/Real.ref) and [Examples.Complex](../../../libs/topology/thom_spaces/src/Thom/Examples/Complex.ref) compare moving-embedding B03 metrics with standard metrics over noncompact scalar lines.
Instantiate Thom homeomorphisms, sphere cofibrations, real-one/two disk suspensions, and one/two-fold existing suspensions.
[Examples.Edges](../../../libs/topology/thom_spaces/src/Thom/Examples/Edges.ref) checks empty rank-zero spheres and all empty-base Thom points equal basepoints.

[Examples.Finite](../../../libs/topology/thom_spaces/src/Thom/Examples/Finite.ref) uses `pairFiniteType` on arbitrary-rank real/complex point-trivial bundles.
Also exposes rank-zero, real/complex lines, empty-base examples.
