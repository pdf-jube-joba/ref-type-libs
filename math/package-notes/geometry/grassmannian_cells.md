# Grassmannian Schubert cells and CW structures

Construction details and records for [grassmannian_cells](../../../libs/geometry/grassmannian_cells/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Real/complex Grassmannian Schubert cells and finite CW structures, standard-inclusion comparisons, oriented real coverings, and stable finite-stage factorizations.
Historical check results appear under [type checking](#type-checking).

## Schubert symbols and echelon forms

`Symbols[n, k].Symbol` has strictly increasing zero-based pivot lists.
`Below` is componentwise order, with reflexivity/transitivity/antisymmetry.
`Free` represents nonpivot-row entries before each column's pivot.
`realDimension` is \(\sum_i(p_i-i)\); `complexDimension` is twice that.
`stabilize` increases ambient dimension by one preserving pivots; `stabilizationDimension` proves dimensions unchanged.
`FreeCount.exists` bijects free entries with \(\mathrm{Fin}(\sum_i(p_i-i))\).
`FreeCount.cardinality` equates arbitrary enumeration counts with this dimension.

`Echelon[K, field, n, k, symbol].Carrier` consists of matrices with identity pivot rows and zeros after each pivot.
`linear` forms column combinations; `coordinates` reads pivot rows.
`leftInverse` and `injective` prove column independence.
`containedUnique` proves equal-symbol echelon matrices equal if one column space contains the other.
`Topological` provides entry-induced topology/free-coordinate continuity.

`Echelon.FreeCoordinates.fill` constructs echelon forms from arbitrary free coordinates.
Define entries by free/pivot/remaining cases; prove existing echelon conditions.
`readFill` and `fillRead` give readout round trips; `FreeCoordinates.Topological.homeomorphism` gives homeomorphisms with free-coordinate product spaces.

`Real[n, k, symbol].parametrizationExists` and `Complex[n, k, symbol].parametrizationExists` use continuous Gram–Schmidt to build projection families and continuous injections into `grassmannians.Real.Model`, `Complex.Model`.
`Parametrization.image` identifies projection fixed spaces with echelon column spaces.
Orthonormalization choices are existentially constructed, not caller assumptions.
`Real.Canonical`, `Complex.Canonical` define choice-independent `map` using uniqueness of orthogonal projections from fixed spaces.
`Canonical.cell` is its image with Grassmannian subspace topology.
`Canonical.Pivot` constructs standard pivot planes/bases.
`Canonical.Pivot.homeomorphismExists` uses existing graph coordinates at those planes for free-coordinate/cell homeomorphisms.
Inverses read normalized graph columns; continuity is specified.
`Reduction` selects maximal nonzero rows, normalizes via column swaps/triangular isomorphisms, inducting by rank reduction.
Reorders pivots and returns echelon forms with the original injective map's image.
`DecompositionReal`, `DecompositionComplex` apply this to projection rank bases, proving cell coverage.
`Echelon.Comparison` derives pivot containment from image inclusion; finite-order rigidity identifies symbols.
`DecompositionReal.disjoint`, `DecompositionComplex.disjoint` state disjointness of distinct-symbol cells.
`Symbols.Enumeration` specifies finite symbol sets and duplicate-free enumerations.

## Ambient inclusions

`AmbientReal[n, k, m]`, `AmbientComplex[n, k, m]` construct rank-\(k\)-preserving inclusions appending \(m\) zero coordinates.
`RankTransportReal`, `RankTransportComplex` transport existing stabilization codomain rank \(0+k\) to \(k\), preserving entries/continuity.
Restriction to original blocks recovers projections, proving injectivity.
`ClosedEmbedding` derives image homeomorphisms/closedness from compact Hausdorffness; each `Ambient` applies it.
`AmbientReal.CW`, `AmbientComplex.CW` expose standard-inclusion skeleton `cellular`, `reflects` and cellwise `cellHomeomorphism`.
`CWReal.With.filtrationEquals`, `CWComplex.With.filtrationEquals` compare these with actual constructed finite-CW skeletons.

## Weak topology and finite stages

`WeakUnion[X, stages, spaces]` constructs weak topology for stages given as subsets of a common set.
Sets are open iff restrictions to every stage are open.
`Universal.continuous` equates outgoing continuity with stagewise continuity.

`Compact[ascending, exhaustive, separated].finiteStage` states compact subsets lie in some stage when increasing T1 stages cover the space.
From a set escaping every stage, select \(x_n\) outside stage \(n\).
Each tail \(\{x_i:i\geq n\}\) meets fixed stages finitely, hence closed; complements form open covers.
Finite subcovers miss sufficiently late \(x_i\), contradicting compactness.

`Maps.boundedImage` places continuous compact-domain images in finite stages.
`Maps.Embedded[induced].exists` returns continuous stage factorizations when stage topologies agree with ambient subspace topologies.
`Spheres[d, induced].sphereMap` and `sphereHomotopy` specialize using compact \(S^d\) and \([0,1]\times S^d\).
The entire homotopy fits in one stage.
`StableReal[k]`, `StableComplex[k]` form unions of finite projections zero-extended to natural-indexed infinite matrices.
`AmbientReal.Entries`, `AmbientComplex.Entries` prove compatibility with standard inclusions.
Reading finite blocks gives continuous stage inverses; `FiniteStage.homeomorphism` gives original finite-Grassmannian homeomorphisms.
`weakTopology` characterizes opens by pullback to finite Grassmannians.
`WeakUnion.CommonTopology` proves stages inherit weak subspace topology; `Maps.exists`, `Spheres.sphereMap`, `Spheres.sphereHomotopy` return continuous actual finite-Grassmannian factorizations.

## Finite coordinates and closed parameter spaces

`FiniteIndex` converts distinct finite enumerations to finite-index bijections.
`Symbols.FreeEnumeration` proves free-coordinate finiteness; `Symbols.Column.indexExists` bijects column-\(j\) free rows with \(\mathrm{Fin}(p_j-j)\).
`FiniteComplement` counts complements of finite injections by pigeonhole.
`Canonical.FiniteCoordinates.exists` gives real/complex finite-coordinate cell homeomorphisms; complex `realExists` doubles real dimension.

`Symbols.Widen` and `Echelon.Widen` construct symbols/echelon forms along standard inclusions.
`agrees` in `AmbientReal.Cells`, `AmbientComplex.Cells` gives projection/cell-coordinate compatibility; `homeomorphism` homeomorphisms onto corresponding cells.

`Reflection` constructs unitary sign flips on projection images and continuous hemisphere rotations from two reflections.
`Rotations` restricts free columns to closed balls and composes rotations in order.
`diagonal`, `above` specify staircase frame support; `boundaryPivot` proves corresponding principal entries vanish on ball boundaries.
`Canonical.Characteristic.map` continuously conjugates coordinate-plane projections by these unitaries.
`Characteristic.diskExists` identifies parameter spaces with standard disks, preserving boundary/interior conditions both ways.
`StandardDisk.map` composes this homeomorphism with existing continuous maps.
`StandardDisk.interiorImage` identifies interior images with cells; `interiorHomeomorphism` specifies interior homeomorphisms.
`StandardDisk.cellLaws` uses compact disks and Hausdorff Grassmannians to construct existing `CW.CellLaws`.

## Standard disks and interior algebra

`FinitePartition` sums bijections over fibers of finitely many distinct labels.
`Symbols.FreeCount` applies this to free column entries.
`FiniteCoordinates.Data.dimensionFormula` and complex `RealData.dimensionFormula` return exact Schubert dimensions, not arbitrary counts.
`schubertExists` and `realSchubertExists` expose dimension-explicit homeomorphisms.

`Rotations.Parameters` zero-extends free entries into matrices, using maximal column norms as gauges.
`FiniteMaximumReal` handles maximum bounds/minimality/attainment/continuity/nonnegative scaling.
`GaugeDisk` uses existing `thom_spaces.Thom.Quadratic` radial maps and `Levels` to identify unit closed balls of positive-definite quadratic-homogeneous gauges with standard disks.
`Rotations.Parameters.Disk` constructs gauge-ball/rotation-parameter round trips.
Free-coordinate bijections or complex realification give `Characteristic.diskExists` real dimensions \(\sum_i(p_i-i)\), \(2\sum_i(p_i-i)\).

`Reflection.Hemisphere.Disk.Inverse` subtracts axial hemisphere components to invert back to closed balls.
`TriangularGram` adds staircase support/positive real principal entries to existing Gram–Schmidt induction.
`TriangularGram.At.Support` selects maximal nonzero coefficients, proving coefficients at pivots beyond image support zero.
`FrameComparison` identifies orthonormal columns from equal images, staircase support, and positive principal entries.
`Rotations.FromFrame` reads first columns as hemispheres, removes rotations, and recursively recovers parameters.
`Rotations.FrameInjectivity` proves equal rotation frames imply equal parameters.
`Characteristic.interiorSurjective` gives interior preimages for cell points; `injectiveInterior` states interior injectivity.

## Boundaries and finite CW structures

`TriangularGram.At.FlagComparison` states staircase-supported injective frames reduce to echelon pivots bounded by original symbols.
If first \(j+1\) columns had higher pivots, restricting coefficients to first \(j\) coordinates gives an injection contradicting `Reduction.rankBound`.
`EchelonComparison` and `FrameComparison` show returning to the original cell forces positive principal entries and interior parameters.
Thus boundary symbols strictly decrease.
`Symbols.Dimensions.strict`, `complexStrict` derive strict total-dimension decrease from pivotwise comparison.
`Characteristic.boundaryLower` gives containing lower-dimensional cells for every boundary point.

`CompactCell` constructs `CW.CellLaws` and interior homeomorphisms from compact-standard-disk maps to Hausdorff spaces, assuming interior injectivity and interior fibers over interior points.
Inverse continuity uses closed images of complements of disk-open sets.
`FiniteCW` proves weak-topology conditions from finitely many such characteristic maps.
`CWReal.exists`, `CWComplex.exists` combine finite symbols and characteristic maps, asserting existing `algebraic_topology.CW.FiniteComplex` without assumptions.
Supply interior coverage/disjointness, lower-dimensional boundaries, and weak topology to this structure.

## Oriented real Grassmannians

`OrientedReal[n, k].Orientation` assigns signs to every orthonormal frame of the same plane.
`Change` constructs frame-change orthogonal matrices, using existing `lie_groups.OrthogonalOrientation.determinantSign`.
Consistency multiplies signs by the change determinant.
`fromFrame` builds assignments from one frame/sign; `reconstruct` proves the inverse.
Signs are \(\{+1,-1\}\); this model retains both choices at rank zero.

`Atlas` generates topology from local-frame sign evaluations and base projections using existing continuous frames.
`TransitionFamily.continuous` connects change-entry and determinant continuity.
`Atlas.In.homeomorphism` identifies local preimages with region/sign products.
`covering` is existing `covering_spaces.Projection.Covering`; `twoSheets` asserts fiber/two-sign bijections.
Separate different bases by Hausdorffness and same-base points by local frame signs.

`Lift` lifts each Schubert characteristic map for both signs using continuous rotating disk frames.
`Lift.Cell` constructs interior homeomorphisms and `CW.CellLaws`.
`OrientedReal.CW.exists` returns lifted finite CW structures from finite symbol/sign enumerations.
Cell dimensions match base cells; `CW.With.projects` states characteristic-map/cover-projection compatibility.
`filtrationEqualsPreimage` identifies oriented skeletons with preimages of corresponding base skeletons.

## Type checking

Historical upstream source `5deadd6563878d1a010b9b628b7e9d68229a9cfe`, checked on 2026-11-20:

| Run | Result |
| --- | --- |
| B08 target | All 225 modules actually checked; standard CLI accepted 1,206 modules including cached dependencies |
| Dependency-closure driver | All 7,852 modules accepted using verified caches |
| Workspace | 11,895/15,749 accepted; stopped at G06 name resolution, leaving 3,854 unconfirmed |
| Temporary G06 integration | 13,276/15,750 accepted; disk exhaustion and subsequent memory-related interruption left 2,474 unconfirmed |

No new axioms or unproved replacements were added; neither workspace run established full success.
See [raw validation records](../../../ref-type/work/b08-type-check/README.md) for commits, commands, diagnostics, and check/reuse counts, and [checking the libraries](../../../libs/USAGE.md) for current runs.
