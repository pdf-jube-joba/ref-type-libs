# Hermitian matrices and continuous local frames

Positive-definite real/complex Hermitian forms, Gram–Schmidt, continuous local frames and inverse coordinates for constant-rank orthogonal projections.
Finite dimensions include zero; bases are arbitrary topological spaces.
Complex inner products are conjugate-linear in the first argument and linear in the second.

## Scalars and shared orthonormalization

Algebraic constructions are shared with [linear_algebra.Hermitian](../linear_algebra/README.md).
`Hermitian.Scalar` groups real embedding, real part, and field conjugation; real/complex implementations are `Hermitian.Real.scalar` and `Hermitian.Complex.scalar`.
`Hermitian.Over.Inner.Of.Algorithm.exists` constructs orthonormal frames, invertible triangular coefficient matrices, and decomposition identities from positive-definite Hermitian forms and injective finite-column matrices.
`Gram.Of` gives frame adjoints, inverse image coordinates, and self-adjoint idempotent orthogonal projections.
Existing real `Euclidean.Normalization` and `Euclidean.Gram.Step.On.With` also use this construction, connecting smooth Gram–Schmidt and tangent/normal bundles.

Package entry: `Hermitian`.
`Hermitian.Real.topological` and `Hermitian.Complex.topological` group continuous field operations, conjugation, real parts, and real embeddings.
Below, write `Hermitian.Over[K, field, scalar, topological].At[n]` as `At`.

| Module | Public contents |
| --- | --- |
| `At.Matrices` | Conjugate transpose `adjoint`, double adjoints, `Hermitian` matrix/linear-map self-adjointness comparison |
| `At.Matrices.Of` / `OfForm` | Hermitian matrix/form round trips, positivity transport, positive identity matrices |
| `At.Forms.Gram` | `Factorization` for arbitrary positive-definite forms and its existence |
| `At.Forms.Families` | Continuous orthonormalization of continuous injective matrix families over arbitrary bases for fixed forms |
| `At.Forms.Families.Normalize` | Continuous normalization of continuous vector families with positive norm |
| `At.Families.Matrix` | Entrywise/fixed-vector continuity comparison, evaluation on varying vectors |
| `At.OnProjection.Rank` | `HasRank` from algebraic image bases, orthonormal `Frame` and inverse coordinates |
| `At.Families.ProjectionFrames` | Continuous local orthonormal frames and inverse coordinates near every point for constant-rank continuous projections |
| `At.Families.Orthonormalized` | Continuous projections, ranks, and local frames from orthonormalization |
| `At.Square` | Left inverses imply right inverses for square maps via [L01](../matrix_invariants/README.md) |
| `At.Square.Families` | Continuous inverse matrix families and openness of invertibility |
| `At.Unitary` | Unitary products/inverses/group laws, conjugate-transpose inverse entries, entry-induced topology |
| `At.Unitary.Operations` | Continuous products and inverses in product topology |
| `At.OnProjection` | Images, complementary projections, mutual annihilation, orthogonal decomposition |
| `At.Blocks` | Block-sum entries/composition/identity, projection/complement comparisons, unitary sums and product preservation |

`HasRank` bases algebraically present images by \(B:K^k\to K^n\), \(C:K^n\to K^k\), with \(CB=I\), \(BC=P\).
Inputs need not be orthonormal or continuous; `frameExists` orthonormalizes them.
`ProjectionFrames.exists` takes an open neighborhood where \(C_0P(x)B_0\) has nonzero determinant for a central basis \(B_0,C_0\).
L01 inverses and constant rank give neighborhood bases/inverse coordinates, then continuous Gram–Schmidt applies.
`Local` stores the open set, central membership, frame, inverse image coordinates, and continuity of both maps.

## Examples and checks

[Examples.MovingLine](src/Hermitian/Examples/MovingLine.ref) orthonormalizes the continuous column family \((1,z)\), then applies the local-frame theorem to its rank-one projection.
Specializes to [reals](src/Hermitian/Examples/Real.ref) and [complexes](src/Hermitian/Examples/Complex.ref); also checks dimension-zero complex unitary groups.

```sh
cargo build -p cli --locked
target/debug/cli libs/algebra/hermitian_frames --memory-mib 8192 --cache-stats
```

Use the shared workspace cache to check targets and all loaded dependency packages.

Target/full-dependency-closure standard check passed: 10,851 source steps, 913 modules checked, 1,098 reused, peak RSS roughly 908 MiB.
Existing tangent/normal examples and `lie_groups` were also checked through dependencies with shared caches matching current sources.
Full fixed-final-source workspace standard check passed, reusing results for 65 packages and 6,852 modules.
Zero worker recoveries, duplicate checks, reruns, lost steps, or cache save failures.

```sh
target/debug/cli libs/geometry/examples/tangent_normal --memory-mib 8192 --cache-stats
target/debug/cli libs/geometry/lie_groups --memory-mib 8192 --cache-stats
target/debug/cli libs --memory-mib 8192 --cache-stats
```
