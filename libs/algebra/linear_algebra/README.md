# Linear algebra

`Commutative[K := K, scalarRing := ring]` handles `std.Alg.Ring.RingModule` over arbitrary commutative rings.
Below, `Space` denotes this specialization.
Finite-free modules, multilinear forms, exterior algebras, and standard-basis determinants also apply to zero rings.
`Field.Space` provides scalar cancellation using field inverses.
`Real.field` uses Dedekind reals; `Complex.field` uses complex real pairs.

| Module | Contents |
| --- | --- |
| `Space.Isomorphism` / `DirectSum` / `Coordinates` | Isomorphisms, binary direct sums, coordinate spaces |
| `Space.Linear.Operations` / `Laws` | Linear-map operations and module laws |
| `Space.Subspace` / `Subspace.Image` / `Quotient` | Subspaces, kernels, images, quotients, map descent |
| `Space.Dual.Precomposition` / `Tensor.Universal` | Dual pullbacks, tensor universality |
| `Space.Multilinear` / `Alternating` | Multilinear/alternating forms, precomposition/contraction |
| `Alternating.Finite` / `PermutationRule` / `Dimension.Above` | Basis expansions, sign changes, vanishing above dimension |
| `Space.Shuffle` / `Sign` / `Exterior.Degrees` | Shuffle wedge products and degrees |
| `Exterior.Bilinearity` / `Associativity` / `GradedCommutativity` / `UnitLaws` / `Pullback.Naturality` | Wedge-product laws |
| `Space.Finite` / `Finite.Prop` | Finite bases, coordinates/reconstruction, dimension, trace |
| `Space.Finite.Representation` / `Rebase` / `Trace` | Matrix representations, basis changes, diagonal sums/cyclicity |
| `Space.Finite.Dimension` / `Finite.Dual` | Scalar dimension values, dual bases |
| `Space.FiniteCoordinates` / `FiniteExterior.At` | Standard bases, arbitrary-degree exterior bases/reconstruction |
| `Space.Matrix` / `Square` | Rectangular/square matrices, operations/actions/eigenvalues |
| `Space.Eigen` / `EigenCoordinates` | Eigenvalues/eigenspaces of abstract maps and coordinate representations |
| `Space.Form` | Bilinear forms, nondegeneracy, adjoints |
| `Real.InnerProduct` / `Complex.InnerProduct` | Real/Hermitian inner products, orthogonality, isometries/self-adjoint maps |
| `Real.Dimension.Space` / `Complex.Dimension.Space` | Dimension invariance |
| `Complex.Matrix` / `Square` | Conjugate transpose, Hermitian matrices |

`Representation.toMatrix b c f` rows use codomain basis `c`; columns use domain basis `b`.
`Rebase.traceIndependent` proves agreement across bases/index sets.
Complex inner products are conjugate-linear first, linear second; `selfAdjointEigenvalueReal` needs no finite-dimensionality.
Compare wedge degree transport through common list representations.
Examples: [SmallSpaces.ref](src/SmallSpaces.ref).

## Finite-dimensional constructions for smooth local frames

`Euclidean` has finite-sum standard inner products, positivity, normalization, adjoints, and orthogonal projections.
`Euclidean.Matrix.OfIsometry` constructs projections onto orthonormal-column images and orthogonal complements.
`Euclidean.Gram.Factorization` and `Step` decompose injective columns into orthonormal frames/triangular isomorphisms; `Gram.Of` gives image inverses and orthogonal decompositions.
`Euclidean.OnProjection.Resolution` inductively constructs frames for orthogonal projections of trace-specified rank.
`Euclidean.Blocks` and `Space.CoordinateSum` identify consecutive coordinate blocks with direct sums.
`Space.CoordinateBasis` recovers actual finite bases/dimensions from coordinate isomorphisms.
`Space.Pullback` transports vector spaces along explicit bijections; `Isomorphism.OfBijective` constructs inverses of bijective linear maps.

## Shared Hermitian geometry

`Hermitian.Real` and `Hermitian.Complex` instantiate real/complex fields, conjugation, real embedding, and real parts.
`Hermitian.Over.Inner` separates Hermitian forms and positivity; `Of.Normalize` normalizes using square roots.
`Of.Algorithm.exists` constructs Gram–Schmidt for positive-definite forms and injective columns by induction on column length.
`Of.Matrix` gives adjoint coordinates; `Of.Gram.Of` gives frame left inverses, inverse image coordinates, and orthogonal projections.
`Hermitian.Complex.FromInnerProduct` transfers existing `Complex.InnerProduct` to this shared form.
Existing real normalization and Gram–Schmidt proofs also use this shared implementation.
For continuity, local frames, Hermitian matrices, unitary groups, and sums, see [hermitian_frames](../hermitian_frames/README.md).

For characteristic polynomials/Cayley–Hamilton of finitely based maps and coprime-factor invariant projections, see [polynomial_linear_algebra](../polynomial_linear_algebra/README.md).

`Commutative.Blocks` constructs upper/lower shears and inverses over commutative rings, plus Schur-complement decompositions.
`Commutative.Rotation` uses shear products to construct invertible families from identity to signed swap, and stabilized-product-to-sum families.
