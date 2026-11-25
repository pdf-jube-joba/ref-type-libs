# `linear_algebra`

Linear, multilinear, and exterior algebra over commutative rings; real/complex specializations.

`Space` abbreviates `Commutative[K, scalarRing]`. Complex inner products are linear in the second argument; matrix rows index codomain bases and columns index domain bases.

| Entry | Purpose |
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
| `Euclidean` / `Hermitian` | Shared Gram–Schmidt, adjoints, orthogonal projections and image coordinates |
| `Commutative.Blocks` / `Rotation` | Shears, Schur complements and invertible stabilized rotation families |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
