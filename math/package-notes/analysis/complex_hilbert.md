# Complex Hilbert spaces

Construction details and records for [complex_hilbert](../../../libs/analysis/complex_hilbert/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Complex Hilbert spaces and compact operators.
Restrict complex scalars to existing real functional analysis; construct complex Riesz representation, bounded adjoints, and closed-subspace projections.

## ImplementationStatus

| Requirement | Status |
| --- | --- |
| Complex normed/Hilbert spaces and real-analysis connection | Implemented and checked |
| Complex Riesz construction, formula, uniqueness | Implemented and checked |
| Bounded adjoints with the same bound, adjoint identities/uniqueness | Implemented and checked |
| Contractive idempotent self-adjoint closed-subspace projections | Implemented and checked |
| Orthogonal-complement/quotient comparison | Quotient norms, isometric linear isomorphisms, minimal-norm representatives implemented and checked |
| Finite-rank factorizations, zero, sums, pre/postcomposition | Implemented and checked |
| Compact operators, zero maps, totally bounded images | Implemented and individually checked |
| Equivalence of compactness and finite-rank approximation | Implemented and individually checked |
| Compactness closed under sums, pre/postcomposition, norm limits, adjoints | Implemented and individually checked |
| Compact identity implies finite dimensionality | Identity factorization through finite coordinates implemented and individually checked |

## Public API

Inner products are complex-linear in the second variable.
Riesz vectors satisfy \(f(x)=\langle y,x\rangle\); adjoints satisfy
\[
\langle Tx,y\rangle=\langle x,T^*y\rangle
\]
From a bound \(c\ge0\) for bounded \(T\), prove with the same constant
\(\lVert T^*y\rVert\le c\lVert y\rVert\).

Apply real Riesz to the real-part functional; evaluate on \(i\)-multiples to recover imaginary equality.
Adjoint row-functional boundedness uses real-inner-product Cauchy–Schwarz from completing positive squares.

Closed subspaces are linear subspaces closed under norm-convergent sequences.
`closedOfTopological` transfers ordinary norm-topology closedness to this condition.
Prove completeness of restricted Hilbert spaces; construct projections from their Riesz representation.
Projection/adjoint existence is not assumed in the structures.

`FiniteRank.Through[n].Factor f` stores linear factorizations \(V\to\mathbb C^n\to W\).
Finite rank is algebraic existence of this factorization, without boundedness/compactness in its definition.

## Compactness and finite dimensionality

Compact operators are bounded linear operators whose closed-unit-ball images have compact closure.
Construct finite-rank self-adjoint projections fixing finite nets to uniformly approximate compact operators.
Finite-rank compactness follows from compact projections fixing finitely many image generators and precomposition.
Rank-one projections are compact because their images lie in sums of two compact real segments.
Adjoint compactness follows from finite-rank projection approximation and norm limits.

`Compact.Identity.FiniteDimensional` is a linear retract factoring identity through finitely many complex coordinates, constructed from compact identity.

Metric `Compactness.TotalBounded` and `Compactness.RelativelyCompact` handle finite nets and relative compactness.
`functional_analysis.Metric.Geometry.TotalBoundedCompact` proves totally bounded sets in complete spaces have compact closures.
