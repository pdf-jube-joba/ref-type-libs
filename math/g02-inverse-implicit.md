# G02 Inverse and implicit functions and local forms of regular values

## Requirements

- Primary implementation: `inverse_implicit`.
- Prove the finite-dimensional inverse function theorem including existence of neighborhoods and inverse maps.
- Prove parameterized implicit-function and constant-rank theorems; construct local coordinates for regular-value preimages.
- Construct regular-value submanifolds for manifold maps and identify their tangent spaces with kernels.

## Dependencies

- [L01 Determinants and invertible matrices](../libs/algebra/matrix_invariants/README.md)

## Implementation

[inverse_implicit](../libs/geometry/inverse_implicit/README.md) implements each item for smooth finite-dimensional maps.

| Requirements | Public API |
| --- | --- |
| Inverse function theorem with neighborhoods and inverse maps | `Euclidean.InverseFunction.localExistence` and `LocalInverse` |
| Parameterized implicit function theorem | `Product.Implicit.localExistence` and `Solution` |
| Constant-rank theorem | `Rank.Witness`, `ConstantRank.On.localExistence`, and `NormalForm` with two-sided coordinate changes |
| Local coordinates of regular fibers | `Product.Submersion.localExistence`, `LocalFiber` |
| Regular-value submanifolds and tangent kernels | `Product.RegularValue.Of.manifold`, `Smooth.embedding`, `Smooth.At.identificationExists` |

[Examples](../libs/geometry/inverse_implicit/src/Examples.ref) instantiate nonlinear shears, implicit functions, nonlinear rank-one maps, the parabola as a regular-value submanifold and its tangent kernel, and dimension zero.
