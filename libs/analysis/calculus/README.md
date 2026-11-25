# `calculus`

Limits, mean value theorem, multivariable differentiation, smooth maps.

`ContDiff k` requires continuous derivatives through order `k`; `Smooth` requires this for every order. Directional derivatives use two-sided curve limits.

| Entry | Purpose |
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
| `Real.Multivariable.Open.Smooth.SquareRoot` | Smooth positive square roots |
| `LinearFamily` / `MatrixFamily` / `GramSchmidt` / `ProjectionFrames` | Smooth matrix actions, orthonormalization and constant-rank local frames |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
