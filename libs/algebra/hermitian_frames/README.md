# `hermitian_frames`

Hermitian forms, continuous orthonormalization, local projection frames and inverse coordinates, unitary groups.

`At` abbreviates `Hermitian.Over[K, field, scalar, topological].At[n]`. Bases are arbitrary topological spaces; inner products are linear in the second argument and dimension zero is included.

| Entry | Purpose |
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

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/hermitian_frames.md)
