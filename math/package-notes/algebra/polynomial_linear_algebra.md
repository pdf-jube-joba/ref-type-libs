# Polynomial and linear-map factorization

Construction details and records for [polynomial_linear_algebra](../../../libs/algebra/polynomial_linear_algebra/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`Field[K := K, field := field]` handles polynomials, quotient rings, and kernel decompositions over arbitrary fields.
Polynomials are exactly free-commutative-ring `Carrier` from [algebra.Polynomial.Over](../../../libs/algebra/basic/README.md).
Reuse existing `galois.Field.Over.Polynomial.Raw` coefficient arithmetic, monic normalization/division.
Refinements separating data/laws pass quotients, Bézout coefficients, decompositions, and linear maps as proved values.

## Division and Euclidean algorithms

Coefficient lists allow trailing zeros.
`DivisionResult.normal` presents divisors as \(c\,m(X)\), \(c\ne0\), with monic \(m\) formed by appending leading \(1\).
`degreeBound` bounds remainder length by \(\deg m\); `bound` makes it shorter than the input divisor list.
Use the latter for Euclidean termination.
Common divisors are unspecified up to units; expose maximality and Bézout identities.
Include zero-polynomial pairs; quantify nonzero division conditions in propositions.

## Quotient rings and Chinese remainder theorem

`Principal[d := d]` constructs quotients by principal ideals \((d)\).
Reuse module quotient relations/addition from `module_theory`, prove multiplicative compatibility, construct rings via `algebra.Quotient.Rings`.
`projection` is a ring homomorphism; `classEqual` / `equalDivisible` and `classZero` / `zeroDivisible` link quotient equality and divisibility both ways.

`Coprime p q` asserts existence of Bézout coefficients \(up+vq=1\).
`forwardMap` in `Chinese[p := p, q := q]` is the ring homomorphism

\[
K[X]/(pq)\longrightarrow K[X]/(p)\times K[X]/(q)
\]

`intersection` proves the divisibility direction of \((p)\cap(q)=(pq)\); `injective` proves comparison injectivity.
`Of[b := b]` constructs inverses and both inverse identities.
`Of.explicit` gives inverse class \([vqa+upc]\) for \(([a],[c])\).
Inverses are unique and representative-independent.

## Polynomial actions and kernel decompositions

`Evaluation` substitutes univariate polynomials into associative rings with central coefficient maps from commutative rings.
Inductively prove expression images commute, then descend to the existing free-commutative-ring quotient.
`Field.Action[V := V, space := space].At[T := T]` substitutes into existing `lie_algebras.Field.Endomorphisms` associative algebras, exposing `evaluate`, `apply`, and polynomial module `module`.

`Primary[V := V, space := module]` applies to arbitrary polynomial-ring modules.
For \(up+vq=1\), `projection p q b` acts by \(vq\), `complementary` by \(up\).
`decompose` decomposes \(\ker(pq)\) elements into both kernels.
`At[p := p, q := q, b := b].isomorphism` gives the polynomial-module linear isomorphism

\[
\ker(pq)\cong\ker p\oplus\ker q
\]

`onKernel` / `onOtherKernel`, `uniqueLeft` / `uniqueRight`, `idempotent`, `independent` prove projection images, vanishing, uniqueness, idempotence, and Bézout independence.
`invariant` proves each kernel invariant under every polynomial, especially \(X\).

## Characteristic polynomials and Cayley–Hamilton

`At[n := n]` matrices index rows then columns; `characteristic A` is polynomial-ring determinant \(\det(XI-A)\).
`cayleyHamilton` proves substitution into `matrix_invariants.Ring.At.linear A` is the zero map for arbitrary matrices/vectors.
`MatrixModule.determinantTrick` handles adjugate actions on arbitrary polynomial modules.
Apply the identity to standard bases and reconstruct by finite sums to derive Cayley–Hamilton.
Reuse [matrix_invariants](../../../libs/algebra/matrix_invariants/README.md) determinant/adjugate proofs, including dimension zero.

`Finite[n := n, V := V, space := space].On[b := b, T := T]` takes existing finite bases and constructs coordinate characteristic polynomials and abstract-map Cayley–Hamilton.
`Factorization` represents proved coprime two-factor factorizations.
`At.On[A := A].Splitting[factors := factors]` constructs `split`, linear `projection`, `idempotent`, `inKernel`, `unique`, `invariant` from characteristic factorizations.

## Naturality and coefficient changes

`Change[L := L, target := target, f := f]` extends coefficient homomorphisms \(f:K\to L\) to polynomial rings.
Exposes compatibility with constants/variables/sums/products/negation and preservation of Bézout identities/coprime factors.
`Intertwining` handles additive semilinear maps preserving scalars and intertwining two linear maps.
`naturality` proves substitution compatibility by generator induction; `projectionNatural` derives kernel-projection compatibility.
Compare identity coefficient changes with `IdentityChange.mapIdentity`.

## Examples and checks

[Field/Examples.ref](../../../libs/algebra/polynomial_linear_algebra/src/Field/Examples.ref) takes \(T(a,b)=(0,b)\) over arbitrary fields and computes the \(X\)/\(1-X\) projection as \((a,b)\mapsto(a,0)\).
Also uses division, Euclidean algorithms, and Chinese-remainder inverses for these factors.
[Examples.ref](../../../libs/algebra/polynomial_linear_algebra/src/Examples.ref) checks real-to-complex coefficient/projection compatibility, zero-dimensional characteristic polynomials, and Cayley–Hamilton for nonzero two-dimensional nilpotents.

Standard check passed: 972 of 1,469 modules checked, 497 reused.
12,109 source steps, peak RSS roughly 972 MiB; zero recoveries, duplicate checks, or lost steps.
Existing `galois` initially produced `definition local context is outside reference scope` during bulk expansion; verified full `galois` separately, then restored dependency caches.
No checker changes.
Target `--full-check-local` passed 415 recheck steps with 1,399 dependency modules reused; unchanged recheck also passed.
