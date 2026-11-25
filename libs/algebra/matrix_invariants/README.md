# `matrix_invariants`

Determinants, cofactors/adjugates, inverses, continuity and openness of real/complex matrix families.

Matrices are indexed by row, then column. Ring APIs include zero rings and dimension zero; field inverses require nonzero determinant.

| Entry | Purpose |
| --- | --- |
| `Ring.At` | Matrices/products/transpose/identity/determinants, column multilinearity/alternation, multiplicativity |
| `Ring.At.Expansion` / `RowTerms` / `Rows` | Finite-multiple-sum basis expansions, row multilinearity/alternation, `transposeInvariant` |
| `Ring.At.Cofactors` / `Adjugate` | Row/column cofactor expansion, `adjugateProduct` and `productAdjugate`, cofactor/adjugate transpose formulas |
| `Ring.At.Adjugate.bumpDeterminant` | Entry increment identity \(\det(A+E_{ij})=\det(A)+C_{ij}(A)\) |
| `Ring.At.Operations` | Associativity/units, inverse-proof type `Inverse`, uniqueness, inverse determinant, `basisChange` |
| `Ring.At.Representation` | Linear-map/entry round trips, composition/products, determinant agreement, inverse-matrix proofs from inverse maps |
| `Ring.At.CommutativeComparison` | Product/transpose/identity agreement with `commutative_algebra.Modules.Matrix`, inverse-proof round trips |
| `Field.At` | `invertibleIff`, nonzero-determinant types `Nonsingular` and `inverse`, `componentFormula`, `inverseDeterminant` |
| `Topological.At` / `Real.At` / `Complex.At` | Determinant continuity, open invertibility and continuous inverse families |
| `Real.At.Smooth` | Cofactor formulas compared with smooth inverse maps |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/matrix_invariants.md)
