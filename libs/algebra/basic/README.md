# `algebra`

Homomorphisms, group completion, quotients, polynomial rings.

Polynomial and Laurent rings use quotient presentations; group completion applies to arbitrary commutative monoids.

| Entry | Purpose |
| --- | --- |
| `Hom` | Monoid/group/semiring/ring homomorphisms and composition of monoid homomorphisms |
| `Quotient` | Equivalence quotients, operation descent, unique representative-independent extensions of maps |
| `Quotient.Groups` / `Quotient.Rings` | Abelian-group/commutative-ring quotients by congruences |
| `Group.Of.Subgroups` | Abelian groups on subsets closed under zero, addition, and inverses |
| `GroupCompletion.Of` | Group completion of arbitrary commutative monoids and unique homomorphism extensions into abelian groups |
| `GroupCompletion.Natural` | Group completion of additive naturals, isomorphism to existing integers, preservation of addition |
| `GroupCompletion.Semiring` | Ring structures on semiring completions, unique ring extensions of semiring homomorphisms, preservation of commutative multiplication |
| `Exact` | Kernels/images/exactness, zero composites from exactness, abelian kernel/image group structures |
| `FreeCommutativeRing.Over.Presentation` | Presentations and universality of commutative rings from coefficient rings, variables, and relations |
| `FreeAssociativeRing.Over.Presentation` | Noncommutative associative-ring presentations with central coefficients, associative-algebra structure and universality |
| `Groups.On` | General group inverses/conjugation, subgroups, generated subgroups, products, quotients by central sign elements |
| `Groups.Units` | Ring unit groups, inverse uniqueness and unit extensionality |
| `Polynomial.Over` | Univariate polynomial rings, unique evaluation homomorphisms specified by coefficient maps and variable values |
| `LaurentPolynomial.Over` | Laurent polynomial rings, unique evaluations at units |
| `Noncommutative` / `AmalgamatedProduct` / `GroupTransport` | General-group actions, cosets, amalgamated-product universality and transport |
| `Polynomial.Over.induction` / `LaurentPolynomial.Over.induction` | Structural induction and evaluation on generators |
| `Two` | The two-element field on Bool |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/basic.md)
