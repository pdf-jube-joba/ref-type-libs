# Field extensions and Galois theory

Subfields, field embeddings, polynomial division, minimal polynomials, automorphism extension, fixed fields, radical generation, and constructible numbers.
Package: `galois`.

| Module | Contents |
| --- | --- |
| `Field.Over` | Arbitrary field arithmetic, nonzero reciprocals, zero-normalized reciprocal operations. |
| `Field.Over.Subfield` | Subfields, intersections, generated subfields, simple adjunction, minimality/monotonicity/idempotence. |
| `Field.Over.Subfield.Of` | Subfield carriers and field laws. |
| `Field.Over.Morphism` | Field homomorphisms, injectivity, embeddings, composition, preservation of powers. |
| `Field.Over.Automorphism` | Automorphisms, inverses, composition. |
| `Field.Over.Correspondence` | Fixed fields, stabilizers, Galois groups, contravariant Galois connection, triple-application identities. |
| `Field.Over.Polynomial` | Coefficient lists/monic polynomials, evaluation, existing-polynomial conversion, splitting, algebraicity, radical solvability. |
| `Field.Over.Polynomial.Raw` | Coefficient-list addition/multiplication/normalization, monic division and degree bounds. |
| `Field.Over.Polynomial.Extension.At` | Minimal-polynomial existence, divisibility of annihilators, embedding extension to roots. |
| `Field.Over.Polynomial.Splitting` | Linear division at roots, complete splitting from algebraic closedness, inclusion of roots of unity. |
| `Field.Over.Partial.Countable` | Extend subfield isomorphisms to automorphisms of countable algebraically closed extensions. |
| `Field.Over.Automorphism.Kummer` / `RadicalAction` | Commutators of automorphisms fixing roots of unity and radicals; radical-closure elements fixed at some derived-series stage. |
| `Field.Over.Generation` | Radical/square-root closures, subfield closure, constructibility implies expression by radicals. |
| `Field.Over.Generation.Construction` | Finite field/square-root expressions, validity, equivalence with constructibility. |
| `Field.Over.Generation.RadicalExpression` | Finite field/radical expressions, equivalence with radical closure. |
| `Permutation` | Permutations, subgroups, normal/commutator subgroups, derived series, solvability, finite chains with abelian quotients. |
| `Quintic` | Explicit five-point permutations proving \(S_5\) nonsolvable and absence of finite subgroup chains with abelian quotients. |
| `RationalClosure` | Rational embeddings, algebraic numbers, algebraic-closure structure for \(\mathbb Q\). |
| `Examples.InField` | Constructibility/finite expression for \(\sqrt2\), coefficients of \(X^5-X-1\). |

## Usage

```toml
[dependencies]
galois = { path = "../galois" }
```

```text
\import std.Alg[].Field[] \as Fields;
\module InField(K: \Set, field: Fields.Field[K]) {
  \import galois.Field[].Over[K := K, field := field].Generation[] \as Generation;
  \import galois.Field[].Over[K := K, field := field].Polynomial[] \as Polynomial;
}
\import galois.Quintic[] \as Quintic;
\import galois.RationalClosure[] \as Closure;
```

`Generation.Constructible S x` states \(x\) belongs to every subset containing the base set \(S\) and closed under field operations and square roots.
`Construction.characterization` proves equivalence with finite field/square-root expressions.
`RadicalExpression.characterization` proves the analogous result for radicals of exponent at least two.
Applied to subfields of the reals, this is the usual algebraic definition of real constructibility.

Monic polynomials are ascending coefficient lists omitting the leading one.
The empty list is one; length is degree; algebraicity witnesses require positive degree.
Leading coefficient one excludes the zero polynomial.
Splitting is equality with products of linear factors in the `algebra.Polynomial.Over` polynomial ring.
`SolvableByRadicals` requires splitting inside the radical closure of the specified ambient field and all roots in that closure.

## Nonsolvability of \(S_5\)

`Quintic.symmetricFiveNotSolvable` proves \(\neg\operatorname{Solvable}(S_5)\) without assumptions.
For the 3-cycle \(c=(a\ b\ c)\) and explicit permutations \(s,t\),

\[
[scs^{-1},tct^{-1}]=c
\]

prove the identity by computation on all five points.
Closure of commutator subgroups under conjugation leaves \(c\) in every derived-series stage.
Since \(c(a)\ne a\), the series never reaches the trivial subgroup.
`Permutation.Obstruction.persists` is the general form of this argument.

`Correspondence.galoisConnection` states the order connection between fixed fields and stabilizers.
`Quintic.Field.Over.threeLiftsObstruction` combines the group obstruction with radical actions to show roots lie outside radical closure.
[quintic](../quintic/README.md) constructs automorphisms from five independent roots, proving general-quintic radical insolubility and nonconstructibility.

## Algebraic closure of the rationals

`RationalClosure.AlgebraicClosureOfQ` bundles a carrier, field structure, rational embedding, algebraicity of all elements over \(\mathbb Q\), and algebraic closedness.
Algebraic closedness means every positive-degree monic polynomial has a root.
`RationalClosure.In.AlgebraicNumbers` refines an ambient field to elements algebraic over the rationals.
Providing algebraic-closure structure requires proofs of algebraicity and algebraic closedness.

## Checks

[Build and check](../../USAGE.md) from the repository root:

```sh
cargo run --manifest-path reftype/Cargo.toml -p cli -- libs/algebra/galois --module galois
```
