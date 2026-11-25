# Determinants and invertible matrices

Construction details and records for [matrix_invariants](../../../libs/algebra/matrix_invariants/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Finite-square determinants, cofactors, adjugates, inverses, and continuity.
`Ring[K := K, scalars := ring]` covers arbitrary commutative rings, including zero rings and dimension zero.
Exterior algebras and normalized top-form proofs are shared with [linear_algebra.Commutative](../../../libs/algebra/linear_algebra/README.md).

## Algebraic API

`Matrix` in `Ring.At[n := n]` is `Fin n -> Fin n -> K`, indexed row first, column second.
`determinant` substitutes columns into normalized top forms.
`cofactor A i j` is the determinant replacing column \(j\) by \(e_i\); define `adjugate A i j = cofactor A j i`.

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

[Examples.ref](../../../libs/algebra/matrix_invariants/src/Examples.ref) checks determinant \(1\) in dimension zero and determinant/invertibility/continuous inverses of real shear matrices \(\begin{pmatrix}1&t\\0&1\end{pmatrix}\).

The historical target/dependency check accepted 1,205 newly checked modules and 88 reused modules, with zero recoveries, duplicates, or lost steps.
See [historical-record scope](../../../libs/USAGE.md#validation-records).

For polynomial-determinant/adjugate Cayley–Hamilton proofs, see [polynomial_linear_algebra](../../../libs/algebra/polynomial_linear_algebra/README.md).
