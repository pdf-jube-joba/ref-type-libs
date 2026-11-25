# `galois`

Field extensions, minimal polynomials, automorphism extensions, Galois connections, radicals, constructibility, definition of the algebraic closure of the rationals.

Monic coefficient lists ascend and omit the leading one. `RationalClosure` defines algebraic-closure structure; constructing a value requires algebraicity and closedness proofs.

| Entry | Purpose |
| --- | --- |
| `Field.Over` | Arbitrary field arithmetic, nonzero reciprocals, zero-normalized reciprocal operations |
| `Field.Over.Subfield` | Subfields, intersections, generated subfields, simple adjunction, minimality/monotonicity/idempotence |
| `Field.Over.Subfield.Of` | Subfield carriers and field laws |
| `Field.Over.Morphism` | Field homomorphisms, injectivity, embeddings, composition, preservation of powers |
| `Field.Over.Automorphism` | Automorphisms, inverses, composition |
| `Field.Over.Correspondence` | Fixed fields, stabilizers, Galois groups, contravariant Galois connection, triple-application identities |
| `Field.Over.Polynomial` | Coefficient lists/monic polynomials, evaluation, existing-polynomial conversion, splitting, algebraicity, radical solvability |
| `Field.Over.Polynomial.Raw` | Coefficient-list addition/multiplication/normalization, monic division and degree bounds |
| `Field.Over.Polynomial.Extension.At` | Minimal-polynomial existence, divisibility of annihilators, embedding extension to roots |
| `Field.Over.Polynomial.Splitting` | Linear division at roots, complete splitting from algebraic closedness, inclusion of roots of unity |
| `Field.Over.Partial.Countable` | Extend subfield isomorphisms to automorphisms of countable algebraically closed extensions |
| `Field.Over.Automorphism.Kummer` / `RadicalAction` | Commutators of automorphisms fixing roots of unity and radicals; radical-closure elements fixed at some derived-series stage |
| `Field.Over.Generation` | Radical/square-root closures, subfield closure, constructibility implies expression by radicals |
| `Field.Over.Generation.Construction` | Finite field/square-root expressions, validity, equivalence with constructibility |
| `Field.Over.Generation.RadicalExpression` | Finite field/radical expressions, equivalence with radical closure |
| `Permutation` | Permutations, subgroups, normal/commutator subgroups, derived series, solvability, finite chains with abelian quotients |
| `Quintic` | Explicit five-point permutations proving \(S_5\) nonsolvable and absence of finite subgroup chains with abelian quotients |
| `RationalClosure` | Rational embeddings, algebraic numbers, algebraic-closure structure for \(\mathbb Q\) |
| `Examples.InField` | Constructibility/finite expression for \(\sqrt2\), coefficients of \(X^5-X-1\) |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/galois.md)
