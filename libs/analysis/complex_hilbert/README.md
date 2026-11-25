# `complex_hilbert`

Complex Riesz representation, bounded adjoints, closed-subspace projections, finite-rank factorization and compact operators.

Inner products are linear in the second argument. Finite rank means algebraic factorization through finite coordinates; boundedness is a separate condition.

| Entry | Purpose |
| --- | --- |
| `Scalars` | Real/imaginary products, real parts after \(i\)-scaling, \(\lvert\operatorname{Re}z\rvert\le\lvert z\rvert\) |
| `Space[V, space]` | Real restriction of complex spaces, complex-homogeneous norms |
| `Space.Hilbert[norm, inner]` | Real parts of Hermitian products, norm compatibility, completeness, real Hilbert structure |
| `Space.Hilbert.Riesz` | Riesz vectors, formulas, existence/uniqueness for bounded complex functionals |
| `Space.Hilbert.FiniteProjection` | Finite-rank self-adjoint projections fixing finite sets |
| `Space.Hilbert.RankOne` | Unit-vector projections, contraction, boundedness, finite-rank factorization |
| `Space.Hilbert.Estimates` | Completing squares, real-inner-product Cauchy–Schwarz |
| `Space.Operators[W, target, norm, targetNorm]` | Bounded complex operators and real bounded conversion |
| `Space.Operators.Continuous` | Continuity of bounded operators |
| `Space.Operators.Compact` / `Compact.After` / `Compact.Before` / `Compact.Addition` / `Compact.Limit` / `Compact.Approximation` / `Compact.FiniteRank` / `Compact.Adjoint` / `Compact.Identity` | Compact closures of unit-ball images, zero maps, total boundedness, sums, bounded pre/postcomposition, norm limits, finite-rank approximation, adjoints, finite dimensionality |
| `Space.Operators.Adjoints[inner, targetInner]` | Adjoint construction, complex linearity, boundedness, uniqueness |
| `Space.Hilbert.Subspaces` | Closed subspaces and connection from topological closedness |
| `Space.Hilbert.Subspaces.In[S].Projection[complete]` | Orthogonal projections from subspace Riesz representation |
| `Projection.Complement` / `Complement.Norm` | Orthogonal complements, complementary projections, quotient norms, isometric isomorphisms, minimal representatives |
| `FiniteRank[V, W, source, target]` | Finite-free factorizations, sum/composition factorizations |
| `Examples` | Zero Hilbert spaces, Riesz, identity adjoints, whole-space projections, quotient comparison, zero/sum finite rank, compact sums/composites/adjoints/limits, compact-identity finite dimensionality |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/analysis/complex_hilbert.md)
