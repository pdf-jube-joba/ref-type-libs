# `singular_cohomology` notes

[Package API](../../../../libs/topology/singular/cohomology/README.md) · [Checking](../../../../libs/USAGE.md)

## Construction

Singular chains are free integer modules on continuous standard-simplex maps; coefficient Hom gives cochains/cohomology.
Direct dependencies: [ref.toml](../../../../libs/topology/singular/cohomology/ref.toml); public modules: [root.ref](../../../../libs/topology/singular/cohomology/src/root.ref).
Barycentric subdivision/small chains/open covers: [singular_subdivision](../../../../libs/topology/singular/subdivision/README.md).

`Chains.boundary n` is \(C_{n+1}\to C_n\).
Alternating boundaries start positive in `module_theory.Module.Over.Alternating.sum`; face \(i\) has sign \((-1)^i\).
Ordinary integer chains have zero negative terms.
Augmented chains `Chains.Reduced.complex` use augmentation \(C_0\to C_{-1}=\mathbb Z\), zero in degrees \(-2\) and below.

Supply `Bundle` of `module_theory.Module.Over` integer modules as coefficients.
Cochains are all functions on simplices; finite support is required only for chains.
`Cochains.With.At.productIsomorphism` exposes this as a module isomorphism.
`Relative.LongExact` connecting signs read boundaries of lifted relative cycles as subspace chains.

Reexporting complexes under aliases retains captured type arguments in module instantiation.

`OverRing.With.integerCoefficients` gives canonical integer actions on coefficient additive groups.
Ring cochain/cohomology carriers are shared with ordinary underlying-integer-module theory.

Relative induced chain/cochain maps live in `Relative.Maps.Over.On.Integer` and its `With`.
Long-exact compatibility/comparison theorems live in each `Naturality`.

## Examples

[Examples](../../../../libs/topology/examples/cohomology/README.md) checks representatives, both square-zero laws, augmentation, coefficient maps, relative connecting, and empty spaces from another package.
[Singular theory index](../../../../libs/topology/singular/README.md) and [concrete computations](../../../../libs/topology/examples/finite_models/README.md) collect excision/finite comparisons/products/examples.
