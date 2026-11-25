# Smooth vector bundles

Construction details and records for [smooth_bundles](../../../libs/geometry/smooth_bundles/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`Real[n,r].On[M].Family[F,space]` and `Complex[n,r].On[M].Family[F,space]` construct constant-rank real/complex smooth bundles on second-countable Hausdorff real manifolds.
`Bundle[I]` has base-chart/fiber-isomorphism covers and smooth overlap matrices.
`Of[I,bundle].manifold` is the actual total smooth manifold constructed from local coordinates.
Real total dimension: \(n+r\); complex: \(n+2r\).

## Sections, maps, and forgetting structure

`Of.Sections` sections are fiber-element families with smooth total-space maps.
Exposes zero sections, base projections, formulas.
Complex sections have the same type as realified smooth sections.
`Maps[n,r,s]` and `ComplexMaps[n,r,s]` are smooth real/complex linear bundle maps over common bases.
`Applying` section actions and `After.Of` composition use actual total smooth-map composition.
`Of.Identity.map` is the identity bundle map.

Real `Of.Forget.forget` and complex `Of.Forget.continuous` construct [vector_bundles](../../../libs/geometry/vector_bundles/README.md) bundles.
Prove total topology/trivialization/inverse continuity; expose `homeomorphism` or two-way `embed`, `recover` with smooth totals.
Complex `Of.forget` separately returns rank-\(2r\) real smooth bundles.

## Linear operations and metrics

`Paired` takes other-bundle frames over the same charts; `Using` receives transition smoothness.
Tensor/exterior coordinates take [bundle_operations](../../../libs/geometry/bundle_operations/README.md) finite enumerations.
`PairIndices.existsEnumeration`, `ExteriorIndices.existsEnumeration` prove enumeration existence.
Includes rank zero/zeroth exterior powers.

Metric existence uses [smooth_partitions](../../../libs/geometry/smooth_partitions/README.md).
Pull back standard local metrics by weighted linear maps; sum locally finitely.
With weights \(\rho_i\), local terms are \(\rho_i^2 h_i\).
Unit weight sums/nonnegative terms give positivity; zero extension off closed supports/local finiteness give smooth coefficients.
Handles empty cover indices.
Hermitian forms are conjugate-linear first, linear second.

## General linear groups, frame bundles, associated bundles

`GeneralLinear` constructs finite-dimensional automorphism groups.
`MatrixModel.homeomorphism` identifies open nonzero-determinant coefficient matrices, proving continuous products/inverses.
`RealLinear.Smooth` and `ComplexLinear.Smooth` prove smooth matrix-family products/inverses.
Complex real differentiability uses real/imaginary coordinates.

`Of.Frames` fibers are isomorphisms \(\phi:F_x\to K^r\).
Right action \(\phi\cdot g=g^{-1}\phi\) has identity/composition/freeness/transitivity proofs.
`Frames.Local` has inverse coordinates between local frames and \(GL_r(K)\).
Local coordinates \(c_i\phi^{-1}\), changes \(g\mapsto(c_jc_i^{-1})g\); `coordinateFormula` and `coordinateSmooth` give formulas/smoothness.
`actionFormula` and `actionSmooth` give local right-action matrices.

`Of.Frames.Smooth[enumeration].manifold` is the open basis-column submanifold of column bundles.
`Columns.FrameBundle` proves inverse/determinant equivalence, openness, frame correspondence/unique reconstruction, right actions/smooth projections.
`Frames.Smooth.groupManifold` is GL as a real-coordinate nonsingular-matrix manifold; `toGroupPoint`, `fromGroupPoint` compare linear isomorphisms.
`Frames.Smooth.Local[i].diffeomorphism` is actual `Diffeomorphism` between frame-bundle opens over chart \(i\) and base-coordinate/GL-open products.
Both maps are `manifolds.SmoothMap` values; `basePreserved` proves base projection agreement; `groupFormula` GL/local-frame coordinate agreement.
`ChartDomain.On.At` constructs domain/image chart diffeomorphisms used here.

`Frames.Smooth.Action.productManifold` is the product manifold from frame bundles and real matrix trivial bundles restricted to nonsingular matrices.
`firstMap` and `secondMap` are smooth projections; `Pair[d].From[X].Of[f,g].map` pairs arbitrary smooth maps.
`Frames.Smooth.Action.map` is the actual smooth right-action map from this product to frame bundles.
`formula` proves agreement with linear-isomorphism actions; `identity` and `composition` prove action laws.
Construct local actions as smooth matrix products; glue global `SmoothMap` using chart-cover agreement.

`RealLinear.Representation` and `ComplexLinear.Representation` are smooth group representations.
Smoothness preserves arbitrary finite-dimensional smooth matrix parameter families.
Also constructs identity representation `standard`.
`Of.Associated[s,representation].associated` glues via represented transitions \(\rho(\tau_{ij})\).
Proves identity/triple cocycles, local fiber isomorphisms, actual transition formulas/smoothness.

## Comparison with existing geometry

`Tangent.On.bundle` and `Normal.On.Of.bundle` transfer existing tangent/normal frames to general smooth bundles.
Tangent bundles expose `FrameComparison.diffeomorphism`; normal bundles expose total topology/projection agreement.
`Normal.On.Of.Splitting.directSum` is the general sum with total topology matching existing tangent/normal decompositions.
`Splitting.diffeomorphism` exposes existing decompositions to ambient trivial bundles.
`Stabilization.diffeomorphism` gives stabilized-normal/original-normal-times-scalar diffeomorphisms; `splittingCompatibility` sum compatibility.

[Examples](../../../libs/geometry/smooth_bundles/src/Examples.ref) gives metrics on real/complex rank-zero bundles over dimension-zero bases and identity representations for both scalars.
