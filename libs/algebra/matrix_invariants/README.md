# Determinants and invertible matrices

Finite-square determinants, cofactors, adjugates, inverses, and continuity.
`Ring[K := K, scalars := ring]` covers arbitrary commutative rings, including zero rings and dimension zero.
Exterior algebras and normalized top-form proofs are shared with [linear_algebra.Commutative](../linear_algebra/README.md).

## Algebraic API

`Matrix` in `Ring.At[n := n]` is `Fin n -> Fin n -> K`, indexed row first, column second.
`determinant` substitutes columns into normalized top forms.
`cofactor A i j` is the determinant replacing column \(j\) by \(e_i\); define `adjugate A i j = cofactor A j i`.

| Module | Public contents |
| --- | --- |
| `Ring.At` | Matrices/products/transpose/identity/determinants, column multilinearity/alternation, multiplicativity |
| `Ring.At.Expansion` / `RowTerms` / `Rows` | Finite-multiple-sum basis expansions, row multilinearity/alternation, `transposeInvariant` |
| `Ring.At.Cofactors` / `Adjugate` | Row/column cofactor expansion, `adjugateProduct` and `productAdjugate`, cofactor/adjugate transpose formulas |
| `Ring.At.Adjugate.bumpDeterminant` | Entry increment identity \(\det(A+E_{ij})=\det(A)+C_{ij}(A)\) |
| `Ring.At.Operations` | Associativity/units, inverse-proof type `Inverse`, uniqueness, inverse determinant, `basisChange` |
| `Ring.At.Representation` | Linear-map/entry round trips, composition/products, determinant agreement, inverse-matrix proofs from inverse maps |
| `Ring.At.CommutativeComparison` | Product/transpose/identity agreement with `commutative_algebra.Modules.Matrix`, inverse-proof round trips |
| `Field.At` | `invertibleIff`, nonzero-determinant types `Nonsingular` and `inverse`, `componentFormula`, `inverseDeterminant` |

Inverse entries: \((A^{-1})_{ij}=\det(A)^{-1}C_{ji}(A)\).
Over fields, prove both implications between invertibility and nonzero determinant.
Over commutative rings, prove \(\operatorname{adj}(A)A=A\operatorname{adj}(A)=\det(A)I\).
For basis changes with proved inverse \(Q=P^{-1}\), show \(\det(QAP)=\det(A)\).
Transpose/adjugate comparisons follow from the same determinant.

## Matrix families and existing analysis APIs

`Topological[K := K, ring := ring].At[n := n]` uses the product topology on `topological_algebra` matrices.
`determinantContinuous` gives continuity over arbitrary topological commutative rings.
`Families[X := X]` handles entrywise continuous families over arbitrary bases, constructing determinant/cofactor continuity and matrix-valued continuity.
Apply finite-sum/product continuity to basis expansions.

`Real.At` and `Complex.At` specialize fields/topologies, exposing `invertibleOpen` and `inverseContinuous`.
Inverse-map domains use `Nonsingular` subspace topology.
`Families.inverseContinuous` applies cofactor formulas to continuous pointwise-invertible families; `certifiedInverseContinuous` also accepts supplied pointwise inverses.
Reuse existing real/complex reciprocal-continuity proofs.

`Real.At.Smooth[d := d]` compares `calculus.MatrixFamily` standard bases and entries.
`inverseFormula` identifies existing inverse-map entries with cofactor formulas; `smoothFormula` transfers `calculus.InverseFamily.regular` smoothness to that formula.

## Examples and checks

[Examples.ref](src/Examples.ref) checks determinant \(1\) in dimension zero and determinant/invertibility/continuous inverses of real shear matrices \(\begin{pmatrix}1&t\\0&1\end{pmatrix}\).

[Build and check](../../USAGE.md) from the repository root:

```sh
reftype/target/debug/cli libs/algebra/matrix_invariants --memory-mib 8192 --cache-stats
```

The historical target/dependency check accepted 1,205 newly checked modules and 88 reused modules, with zero recoveries, duplicates, or lost steps.
See [historical-record scope](../../USAGE.md#validation-records).

For polynomial-determinant/adjugate Cayley–Hamilton proofs, see [polynomial_linear_algebra](../polynomial_linear_algebra/README.md).
