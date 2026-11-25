# Foundations of real analysis

Constructed real arithmetic, distance estimates, sequences, square roots, and finite sums.

| Module | Contents |
| --- | --- |
| [Analysis](src/Analysis.ref) | Constructed Dedekind-real types and operations |
| `Analysis.Algebra` | Arithmetic identities, nonnegative squares, `Field` structure |
| `Analysis.Distance` | Rational embeddings, maxima/minima, distance laws |
| `Analysis.Estimates` | Weighted distances, midpoints, order/equality criteria from arbitrarily small errors |
| `Analysis.Sequence` | Real Cauchy sequences, convergence, limit construction and uniqueness |
| `Analysis.SquareRoot` | Square roots from suprema, nonnegativity/square/uniqueness, square-root distance bounds |
| `Analysis.Estimates.Product` / `Analysis.Inverse` | Product/reciprocal distance bounds, reciprocal control on positive/negative regions |
| `Analysis.FiniteSums.Convex` / `Exclusion` | Convex-combination distance bounds, finite-sum bounds excluding one vanishing term |
| `Analysis.Geometric` | Powers of nonnegative coefficients below 1 become smaller than any positive value |

`metric_spaces.RealMetric` connects to metric spaces; `linear_algebra.Real` connects to vector spaces.

```text
\import real.Analysis[] \as R;
\import R.Distance[] \as Distance;
\definition selfDistance: \forall (x: R.Real) -> R.distance x x = R.zero :=
  Distance.distanceSelf;
```

[Examples](../../analysis/scalar_compatibility/src/Compatibility.ref) check constant-sequence limits and shared arithmetic across fields.


`Analysis.FiniteSums.blocks` splits sums over consecutive finite-index blocks, for inner-product formulas on direct-sum coordinates.
