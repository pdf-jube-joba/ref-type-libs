# Hermitian matrices and continuous local frames

Construction details and records for [hermitian_frames](../../../libs/algebra/hermitian_frames/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Positive-definite real/complex Hermitian forms, Gram–Schmidt, continuous local frames and inverse coordinates for constant-rank orthogonal projections.
Finite dimensions include zero; bases are arbitrary topological spaces.
Complex inner products are conjugate-linear in the first argument and linear in the second.

## Scalars and shared orthonormalization

Algebraic constructions are shared with [linear_algebra.Hermitian](../../../libs/algebra/linear_algebra/README.md).
`Hermitian.Scalar` groups real embedding, real part, and field conjugation; real/complex implementations are `Hermitian.Real.scalar` and `Hermitian.Complex.scalar`.
`Hermitian.Over.Inner.Of.Algorithm.exists` constructs orthonormal frames, invertible triangular coefficient matrices, and decomposition identities from positive-definite Hermitian forms and injective finite-column matrices.
`Gram.Of` gives frame adjoints, inverse image coordinates, and self-adjoint idempotent orthogonal projections.
Existing real `Euclidean.Normalization` and `Euclidean.Gram.Step.On.With` also use this construction, connecting smooth Gram–Schmidt and tangent/normal bundles.

Package entry: `Hermitian`.
`Hermitian.Real.topological` and `Hermitian.Complex.topological` group continuous field operations, conjugation, real parts, and real embeddings.
Below, write `Hermitian.Over[K, field, scalar, topological].At[n]` as `At`.

`HasRank` bases algebraically present images by \(B:K^k\to K^n\), \(C:K^n\to K^k\), with \(CB=I\), \(BC=P\).
Inputs need not be orthonormal or continuous; `frameExists` orthonormalizes them.
`ProjectionFrames.exists` takes an open neighborhood where \(C_0P(x)B_0\) has nonzero determinant for a central basis \(B_0,C_0\).
L01 inverses and constant rank give neighborhood bases/inverse coordinates, then continuous Gram–Schmidt applies.
`Local` stores the open set, central membership, frame, inverse image coordinates, and continuity of both maps.

## Examples and checks

[Examples.MovingLine](../../../libs/algebra/hermitian_frames/src/Hermitian/Examples/MovingLine.ref) orthonormalizes the continuous column family \((1,z)\), then applies the local-frame theorem to its rank-one projection.
Specializes to [reals](../../../libs/algebra/hermitian_frames/src/Hermitian/Examples/Real.ref) and [complexes](../../../libs/algebra/hermitian_frames/src/Hermitian/Examples/Complex.ref); also checks dimension-zero complex unitary groups.

Historical checks accepted 913 newly checked modules and 1,098 reused modules, including the dependency closure.
Tangent/normal examples and `lie_groups` regressions passed; the final workspace reused 6,852 modules across 65 packages.
The runs reported zero save failures, recoveries, duplicate/rerun checks, or lost steps; see [historical-record scope](../../../libs/USAGE.md#validation-records).
