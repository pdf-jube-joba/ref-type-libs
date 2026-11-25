# Complex polynomial roots and factorization

Construction details and records for [fundamental_algebra](../../../libs/algebra/fundamental_algebra/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Package: `fundamental_algebra`; public entry: `Complex`.
Prove the fundamental theorem of algebra for the constructed complex field using L02 [polynomial_linear_algebra](../../../libs/algebra/polynomial_linear_algebra/README.md) and [galois](../../../libs/algebra/galois/README.md) polynomial rings, coefficient lists, normalization, and degree induction.

## General polynomials

The polynomial carrier applies `algebra.Polynomial.Over` to the commutative ring of `complex.Complex.Algebra.field`.
Evaluation uses existing `galois.Field.Over.Polynomial.AbstractEvaluation.apply`.

`Complex.Normalization.exists` converts nonzero polynomials to nonzero leading coefficients and monic coefficient lists.
Coefficients ascend as in existing APIs; monic forms omit the leading \(1\).
For example, \(X^2+1\) is `[one, zero]`.

## Multiplicities and unordered presentations

Root lists retain every occurrence of repeated roots.
Matching removes equal roots one at a time, so uniqueness includes multiplicities.
The general minimum theorem covers zero polynomials; factorization theorems requiring nonzero leading coefficients exclude them.
`Complex.Naturality` connects root transport under field automorphisms and coefficient/factorization compatibility to existing `RootProduct.natural`.

## Proof structure

`Bounds` proves growth bounds from absolute coefficient sums using Horner evaluation and reverse triangle inequalities.
`Minimum` extends a minimum on a sufficiently large square to a global minimum using compact products of closed intervals and the continuous minimum theorem.
`Difference` and `FirstTerm` construct \(p(a+X)-p(a)=X^n h(X)\) with \(n>0\), \(h(0)\ne0\).
`UnitRoots` and `Directions` construct directions decreasing the lowest term using unit-circle square roots and parity induction.
`Variation.Decrease` uses squared-norm identities and continuity to decrease values with arbitrarily small positive displacements.
This contradicts a nonzero minimum, proving root existence.
Factorization reuses existing `Splitting.splitsOverClosed` degree induction; uniqueness uses linear-factor cancellation and root-removal induction.
No new axioms or checker changes.

## Examples and checks

[Complex/Examples.ref](../../../libs/algebra/fundamental_algebra/src/Complex/Examples.ref) checks roots and complete factorization of \(X^2+1\), root-family equality under swapping two roots, and distinction between double-root and simple-root families.
Also includes nonmonic \(i(X^2+1)\) factorization/unordered presentation and minimum theorems for zero/constants.
Public APIs can be imported from children of [Complex.ref](../../../libs/algebra/fundamental_algebra/src/Complex.ref).

Target `--full-check-local` passed: 32 modules and 399 source-check steps rechecked, verified caches for 1,424 dependency modules reused.
Peak RSS roughly 1,120 MiB; one worker; zero recoveries, duplicates, or lost steps.
Unchanged standard recheck passed with all 1,456 modules reused and zero source-recheck steps.
Workspace `--module fundamental_algebra` registration/dependency-closure checks and existing `polynomial_linear_algebra` cache regressions across all 1,424 modules also passed.

See [complex_polynomial_roots](../../../libs/algebra/complex_polynomial_roots/README.md) for fixed-degree symmetric-product/coefficient homeomorphisms and continuity of separated-region root counts/factors.
