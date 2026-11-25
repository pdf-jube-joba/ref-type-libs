# Differentiation

Limits and derivatives over Dedekind reals.

| Module | Contents |
| --- | --- |
| `Real` | Real arithmetic, constant/identity/linear functions |
| `Real.Limit.Def` / `Prop` | Punctured ε–δ limits, constants/identity, equality transport |
| `Real.Derivative.Def` / `Prop` / `Operations` / `Product` / `Chain` | Difference-quotient limits, uniqueness, continuity, sum/product/chain rules |
| `Real.MeanValue.Interval` | Fermat, Rolle, mean value theorem, derivative difference bounds |
| `Real.Multivariable[n].Space.Def` | Finite coordinates and maximum norm (zero in dimension zero) |
| `Real.Multivariable[n].Partial.Def` / `Differential.Def` / `Directional.Def` | Partial derivatives/gradients, total derivatives, curvewise directional derivatives |
| `Real.Multivariable[n].Smooth.Def` | Iterated partials, \(C^k\) and \(C^\infty\) |
| `Real.Multivariable[n].Open` / `Open.Smooth` | Open restrictions, relative partials, operations/gluing |
| `Open.C1` / `Open.Smooth.Differential` / `Open.Smooth.Mixed` / `Real.Schwarz.Rectangle` | Total derivatives from continuous partials, double mean value theorem, mixed-partial commutation |
| `Maps[n, m]` / `Maps.Composition` / `Vector[n, m]` | Smooth open-set maps, Jacobians, vector total derivatives/chain rules |
| `Maps.WithPartials` / `Maps.Preimage` | Chain rules for continuous partials, open-preimage restrictions |
| `Real.OneDimension` / `Blocks[n, m]` | Real/one-dimensional partial comparison, coordinate-block products/projections/slices |
| `Curves[n]` / `Maps.Corestriction` | Global representatives/derivatives of smooth real curves, derivatives of open-range restrictions |
| `Scaling[n]` / `Translation[n]` | Smooth dilations/translations, translation derivatives |
| `Identity[n]` / `Diffeomorphism[n, m]` | Identities, inverse/composite diffeomorphisms, induced homeomorphisms |

`ContDiff k f` asserts continuous derivative families through order k; `Smooth f` is `ContDiff k f` for every k.
`Open.Smooth.Derivative.Function U` accepts smooth functions; `derivative U f i` returns smooth partial derivatives.
`Maps.Differential[U, V, f, a].value` is a linear map on `linear_algebra`; `matrixEntry` is a smooth scalar function.

`Directional` uses curves on open intervals containing zero and two-sided limits.
`HasDirectionalDerivativeAt` quantifies over all curves with equal starting points/tangent vectors; tangent vectors include parameter speed.

Examples: [Calculus.ref](../../geometry/coordinate_calculus/src/Calculus.ref) and [nonlinear diffeomorphisms](../../geometry/coordinate_calculus/src/Shear.ref).

`Real.Derivative.SquareRoot` differentiates square roots of positive differentiable functions.
`Real.Multivariable.Open.Analysis.SquareRoot` transfers this to partials; `Open.Smooth.SquareRoot` proves square roots of positive smooth functions smooth.
Higher smoothness follows inductively from \(r=\sqrt f\), \(\partial_i r=\frac12 r f^{-1}\partial_i f\).

## Matrix families and local orthonormal frames

`LinearFamily` and `MatrixFamily` construct smooth matrix actions \((u,v)\mapsto A(u)v\) from finite sums.
`Maps.Tangent` exposes smooth \((u,v)\mapsto(f(u),Df_u v)\); `Maps.FixedDifferential` exposes derivative actions on fixed vectors.
`SmoothCoordinates` handles finite inner products and coordinate concatenation.
`GramSchmidt.On.Rank` decomposes smooth injective matrix families into smooth orthonormal frames and invertible coefficients.
Its `Projections` gives smooth tangent/normal projections and image inverses.
`ProjectionFrames` constructs orthonormal frames from constant-rank smooth projections on positive-norm neighborhoods.
`InverseFamily` derives smooth pointwise inverses of smooth invertible families; `LinearMap` shares linear smoothness/derivative formulas.

Real Gram–Schmidt algebraic proofs are shared with `linear_algebra.Hermitian`.
Real/complex continuous orthonormalization and projection frames over arbitrary topological bases: [hermitian_frames](../../algebra/hermitian_frames/README.md).
