# Bundle gluing and linear operations

Construction details and records for [bundle_operations](../../../libs/geometry/bundle_operations/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`bundle_operations.Operations.Over` constructs gluing and linear operations on [vector_bundles](../../../libs/geometry/vector_bundles/README.md) real/complex bundles.
Supply the same `K, field, conjugation, scalar` for scalars, topology, and frames.
Construct total topologies/trivializations; prove bundle-map/isomorphism continuity and inverse laws.

## Cocycles and presentation comparisons

`Cocycle[X, I, baseSpace, domain, dimension].With[cocycle]` accepts ordinary transitions and identity/composition laws.
Fibers `Fiber x` are coordinate families compatible with transitions in every chart containing the point.
Prove `At.Frame` evaluation and family assembly inverse.
`Continuous` gives open domains, coverage, continuous overlap transitions; `regular` and `Construction.bundle` construct actual totals/trivializations.
`Atlas` and `Final` construct final topologies from coordinate maps, proving universality/open restrictions.

`CocycleFromAtlas` extracts transitions from supplied frames.
`WithCover.isomorphism` compares cocycle-reconstructed and original bundles.
`With.Refine` changes covers; `With.Reframe.Using` simultaneously refines/changes frames; both expose new cocycles, glued bundles, comparisons, `transitionFormula`.
Frame changes \(g_j\) yield transitions \(g_k\tau_{\rho(j),\rho(k)}g_j^{-1}\).
`ChartRestriction`, `GaugeChart`, `CoordinateGauge`, `AtlasChange` also apply to existing bundle charts.
`ScalarGauge.regular` proves both frame-change continuities for continuous nonzero scalar families.

## Linear operations

`Mapping`, `Contramap`, realification/complexification `Maps` construct continuous maps from supplied continuous bundle maps.
`Hom.Of.Mapping.evaluation` proves evaluation of \(h\mapsto b\circ h\circ a\).
`Tensor.Of.Parametric` reduces varying-base/vector linear-action continuity to finitely many basis checks for tensor associators/Hom evaluation.
`Tensor.Of.Pure.Along`, `Dual.Pairing`, `Exterior.Wedge` also apply to continuous vector families over arbitrary parameter spaces.
`Exterior.Mapping.WedgeNaturality` proves wedge naturality under bundle maps.

Each `Pullback.isomorphism` is an actual isomorphism comparing pullback of operations with operations on pullbacks.
Binary operations use `Of[same].Pullback`.
Including realification/complexification, both comparison directions are fiber identities; compatible frames prove continuity.

## Local models and compatibility

`CoordinateSum` concatenates/splits coordinates.
`TensorFrame` maps pure tensors to coefficient products, proving finite-sum inverses.
`DualFrame` evaluates dual bases; `TensorHom.Finite` gives finite tensor/linear-map isomorphisms.
`AlternatingFrame` gives alternating coefficients/reconstruction indexed by increasing tuples.
`Scalars.RealCoordinates` and `ComplexTensor.Finite` prove usual realification/complexification coordinate isomorphisms/continuity.
Each bundle `In` uses these as actual trivializations, including dimension zero/empty indices.

Exposes `DirectSumAssociator`, `DirectSum.Of.Symmetry`, `DirectSumUnit`, `DirectSumRightUnit` and corresponding `Tensor` isomorphisms.
`DirectSumPentagon`, `TensorPentagon`, `DirectSumHexagon`, `TensorHexagon`, their `OppositeHexagon`, and `DirectSumTriangle`, `TensorTriangle` prove composite-isomorphism equalities.
`UnitAtBase` explicitly compares chosen zero/standard-line bundles over equal topologies.
`DirectSumIsomorphisms` and `TensorIsomorphisms` construct operated isomorphisms from two input isomorphisms.
`IsomorphismComposition.exists` and `DirectSumIsomorphisms.exists` derive composite/sum isomorphism existence from input existence.
`SymmetryNaturality`, `AssociatorNaturality`, `UnitNaturality`, `TensorDistributionNaturality` prove bundle-map compatibility as map equalities.
`TensorDistribution` constructs \(E\otimes(F\oplus G)\cong(E\otimes F)\oplus(E\otimes G)\) via projections/inclusions/pure tensors, proving both inverses.
`TensorRightDistribution` constructs right distribution via swap comparisons.

## Examples and checks

[Over.GaugeExample](../../../libs/geometry/bundle_operations/src/Operations/Over/GaugeExample.ref) refines real trivial lines into whole/positive-half-line charts, changing one frame by continuous nonconstant nonzero scalars.
Constructs comparisons from the newly glued bundle to the original.
[Over.Examples](../../../libs/geometry/bundle_operations/src/Operations/Over/Examples.ref) applies sums/tensors/duals/Hom/exterior powers, square-map pullback comparisons, Hom evaluation, and associator naturality.
Includes zero-bundle tensors, zeroth exterior powers, varying-rank two-component tensors, empty-base sums.
[Operations.Examples](../../../libs/geometry/bundle_operations/src/Operations/Examples.ref) instantiates both scalars and realification/complexification pullback isomorphisms.

Target/dependency checks passed for 4,265 modules: 271 new, 3,430 source steps, 3,994 reused.
Peak RSS roughly 4,843 MiB, one worker; zero recoveries/duplicates/reruns/lost steps/cache save failures.
Workspace `--module bundle_operations` reused 738 modules; full workspace passed reusing all 70 packages/7,247 modules.
Final checks had zero source rechecks/recoveries/duplicates/reruns/lost steps/cache save failures.
