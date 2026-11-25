# Abstract algebra

Homomorphisms, group completion, quotients, and polynomial rings.

| Module | Public contents |
| --- | --- |
| `Hom` | Monoid/group/semiring/ring homomorphisms and composition of monoid homomorphisms. |
| `Quotient` | Equivalence quotients, operation descent, unique representative-independent extensions of maps. |
| `Quotient.Groups` / `Quotient.Rings` | Abelian-group/commutative-ring quotients by congruences. |
| `Group.Of.Subgroups` | Abelian groups on subsets closed under zero, addition, and inverses. |
| `GroupCompletion.Of` | Group completion of arbitrary commutative monoids and unique homomorphism extensions into abelian groups. |
| `GroupCompletion.Natural` | Group completion of additive naturals, isomorphism to existing integers, preservation of addition. |
| `GroupCompletion.Semiring` | Ring structures on semiring completions, unique ring extensions of semiring homomorphisms, preservation of commutative multiplication. |
| `Exact` | Kernels/images/exactness, zero composites from exactness, abelian kernel/image group structures. |
| `FreeCommutativeRing.Over.Presentation` | Presentations and universality of commutative rings from coefficient rings, variables, and relations. |
| `FreeAssociativeRing.Over.Presentation` | Noncommutative associative-ring presentations with central coefficients, associative-algebra structure and universality. |
| `Groups.On` | General group inverses/conjugation, subgroups, generated subgroups, products, quotients by central sign elements. |
| `Groups.Units` | Ring unit groups, inverse uniqueness and unit extensionality. |
| `Polynomial.Over` | Univariate polynomial rings, unique evaluation homomorphisms specified by coefficient maps and variable values. |
| `LaurentPolynomial.Over` | Laurent polynomial rings, unique evaluations at units. |

Group completion of commutative monoids is defined by the formal-difference relation

\[
(a,b)\sim(c,d)\quad\Longleftrightarrow\quad\exists e,\quad a+d+e=c+b+e
\]

below.
Proves equivalence, operation compatibility, group laws, and universality of this relation.
Extend semiring multiplication by using additive universality twice.

Construct polynomial and Laurent rings by quotienting expressions by the least ring congruence.
`FreeCommutativeRing` presentations also handle coefficient-ring algebras with additional relations.
For monic normalization/division of coefficient lists over fields, see `galois.Field.Over.Polynomial.Raw`; for division by arbitrary nonzero divisors, Euclidean algorithms, and Bézout coefficients, see [polynomial_linear_algebra](../polynomial_linear_algebra/README.md).

`Noncommutative` handles general groups, subgroups, right actions, stabilizers, and right actions on left cosets.
`Actions.At` constructs equivariant bijections between transitive right actions and coset actions of chosen-point stabilizers.

`AmalgamatedProduct` provides amalgamated-product universality and canonical isomorphisms between groups satisfying it.
`Noncommutative.Actions.PointedMaps` constructs pointed equivariant maps between transitive actions from stabilizer inclusions.
`GroupTransport` transports group structures along inverse bijections.

`Polynomial.Over.induction` and `LaurentPolynomial.Over.induction` extend propositions closed under constants, variables, sums, negation, and products to all polynomials.

`onConstant`, `onVariable`, `onInverseVariable` in `LaurentPolynomial.Over.Universal` expose evaluation laws on generators.
[uniform_approximation](../../analysis/uniform_approximation/README.md) uses polynomial/Laurent induction and evaluation to construct uniform approximations as actual ring elements.

`Two` is the two-element field on Bool.
Addition is xor, multiplication is and; commutative-ring/field laws and \(0\ne1\) are proved.
`cohomology_examples.Two` uses this shared field structure for integer-module operations and residue-ring comparisons.
