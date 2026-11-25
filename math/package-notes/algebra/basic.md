# `algebra` notes

[Package API](../../../libs/algebra/basic/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Homomorphisms, group completion, quotients, and polynomial rings.

Group completion of commutative monoids is defined by the formal-difference relation

\[
(a,b)\sim(c,d)\quad\Longleftrightarrow\quad\exists e,\quad a+d+e=c+b+e
\]

below.
Proves equivalence, operation compatibility, group laws, and universality of this relation.
Extend semiring multiplication by using additive universality twice.

Construct polynomial and Laurent rings by quotienting expressions by the least ring congruence.
`FreeCommutativeRing` presentations also handle coefficient-ring algebras with additional relations.
For monic normalization/division of coefficient lists over fields, see `galois.Field.Over.Polynomial.Raw`; for division by arbitrary nonzero divisors, Euclidean algorithms, and Bézout coefficients, see [polynomial_linear_algebra](../../../libs/algebra/polynomial_linear_algebra/README.md).

`Noncommutative` handles general groups, subgroups, right actions, stabilizers, and right actions on left cosets.
`Actions.At` constructs equivariant bijections between transitive right actions and coset actions of chosen-point stabilizers.

`AmalgamatedProduct` provides amalgamated-product universality and canonical isomorphisms between groups satisfying it.
`Noncommutative.Actions.PointedMaps` constructs pointed equivariant maps between transitive actions from stabilizer inclusions.
`GroupTransport` transports group structures along inverse bijections.

`Polynomial.Over.induction` and `LaurentPolynomial.Over.induction` extend propositions closed under constants, variables, sums, negation, and products to all polynomials.

`onConstant`, `onVariable`, `onInverseVariable` in `LaurentPolynomial.Over.Universal` expose evaluation laws on generators.
[uniform_approximation](../../../libs/analysis/uniform_approximation/README.md) uses polynomial/Laurent induction and evaluation to construct uniform approximations as actual ring elements.

`Two` is the two-element field on Bool.
Addition is xor, multiplication is and; commutative-ring/field laws and \(0\ne1\) are proved.
`cohomology_examples.Two` uses this shared field structure for integer-module operations and residue-ring comparisons.
