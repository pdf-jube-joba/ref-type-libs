# `smooth_bundles`

Real/complex smooth bundles and metrics, duals/tensors/exterior powers, smooth frame actions/local diffeomorphisms, representation-associated bundles, tangent/normal comparisons.

`Of` refers to `Real[n,r].On[M].Family[F,space].Of[I,bundle]`, or its complex counterpart. Ranks are constant; total real dimensions are n+r and n+2r.

| Entry | Purpose |
| --- | --- |
| `Dual.dual` | Functional bundles; smoothness from inverse transition matrices |
| `Paired.Using.directSum` / `Paired.Using.DirectSum.directSum` | Sums aligned to common base-chart covers |
| `Paired.Using.Tensor.tensor` | Algebraic tensor bundles; smoothness from finite coefficient sums |
| `Alternating.alternating` | Fiber alternating-form bundles |
| `Exterior.exterior` | Covariant exterior powers as alternating forms on duals |
| `Columns.columnsBundle` | Finite-column bundles of arbitrary fibers |
| `Metrics.existsMetric` | Smooth positive-definite metrics on arbitrary bundles |
| `GeneralLinear` / `Real.On.Family.Of.Frames.Smooth` / `Complex.On.Family.Of.Frames.Smooth` | General linear groups, frame-bundle manifolds, local product diffeomorphisms and smooth right actions |
| `RealLinear.Representation` / `ComplexLinear.Representation` / `Real.On.Family.Of.Associated` / `Complex.On.Family.Of.Associated` | Smooth representations and associated bundles |
| `Tangent` / `Normal` | General smooth-bundle comparisons with tangent/normal sums and stabilization |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/smooth_bundles.md)
