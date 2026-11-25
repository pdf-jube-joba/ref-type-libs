# Singular chains and singular cohomology

Singular chains are free integer modules on continuous standard-simplex maps; coefficient Hom gives cochains/cohomology.
Direct dependencies: [ref.toml](ref.toml); public modules: [root.ref](src/root.ref).
Barycentric subdivision/small chains/open covers: [singular_subdivision](../subdivision/README.md).

| Module | Constructions and proofs |
| --- | --- |
| `Simplices` / `At` / `Faces` / `Identities` | All simplices, constants, face maps/composition. |
| `Chains` / `Boundary` / `SquareZero` | Free integer chains, alternating boundary/square zero, nonnegative/integer complexes. |
| `Chains.Augmentation` | Degree-zero augmentation, boundary vanishing, point right inverses. |
| `Chains.Reduced.NegativeOne` | Reduced degree-minus-one vanishing when nonempty, integer isomorphisms when empty. |
| `Chains.Reduced` | Augmented chains with integers in degree \(-1\), coefficient reduced Hom. |
| `Cochains.With` / `Cohomology` | Arbitrary-integer-module cochains, cocycles/classes/cohomology modules. |
| `Cochains.With.At` | Isomorphism of arbitrary simplex assignments with cochains. |
| `Cochains.OverRing.With` / `Relative.OverRing.With` | Commutative-ring coefficients, pointwise scaling, linear coboundaries, ordinary/relative ring modules. |
| `Cochains.Abelian` | Canonical integer modules from abelian groups for cohomology. |
| `Maps` / `Differential` / `Composition` | Postcomposition chain maps, boundary/composition laws, integer zero extensions. |
| `Identity` / `Identity.Coefficients` | Continuous identities induce chain/cochain/cohomology identities. |
| `Maps.Coefficients` | Space-contravariant/coefficient-covariant maps, generator evaluations. |
| `Maps.Coefficients.Integer.At` | Integer/nonnegative cohomology comparison naturality in space/coefficients. |
| `Maps.Composition.Coefficients` | Continuous-composition cohomology laws. |
| `Homotopy` / `Coefficients` | Affine-prism chain homotopies, arbitrary-coefficient homotopy invariance. |
| `Homotopy.Homology.At` | Integer singular-homology homotopy invariance. |
| `Equivalence.With` | Cohomology module isomorphisms from space equivalences. |
| `Relative` / `Injection` | Injective subspace chains, image quotients, relative short exactness. |
| `Relative.Homology` / `LongExact` | Relative homology/connecting maps, zero composites, long exactness. |
| `Relative.Split` / `Relative.With.PairSequence` | Degreewise split inclusions, cochain short/long exactness. |
| `Relative.With.Vanishing` | Relative/vanishing-on-subspace cochain isomorphisms. |
| `Relative.With` | Quotient-chain coefficient Hom/relative cohomology. |
| `Relative.Support` | Subspace-valued simplex lifting, induced-chain images lie in subspace chains. |
| `Relative.Equivalence.Over.On` | Relative homology/arbitrary-cohomology isomorphisms from inverse pair homotopies. |
| `Relative.Identity` / `Maps.Over.Composition` | Relative identities/composition, homology/cohomology functoriality. |
| `Relative.Maps.Over.Homotopy.On` | Subspace-preserving prisms induce relative homotopies/equal induced maps. |
| `Relative.Maps.Over.On` / `Integer.With` / `Naturality` | Pair chain/cochain maps, inclusion/quotient/connecting naturality. |
| `Coefficients.Sequence.On` / `Bockstein` | Coefficient-induced short exact cochains, Bockstein/exactness. |
| `OrderedTuples` / `ConeBoundary` / `SquareZero` | Vertex-list free chains, alternating complexes, prepend-cone boundaries. |
| `OrderedTuples.Prism` | Two-vertex-map prisms, boundaries, pre/postcomposition naturality. |
| `OrderedTuples.Subdivision` / `Homotopy` / `Natural` | Chosen-center subdivision, boundary compatibility, identity homotopies, center-preserving naturality. |
| `CylinderChains` | Vertex-to-affine-cylinder chain maps, universal prisms, face compatibility. |
| `SimplicialChains.On` | Free chains/functoriality from arbitrary graded face-identity sets. |
| `Zero.With.Functions` | Degree-zero cohomology as all coefficient-valued functions on path components. |
| `Zero.Homology` | Degree-zero integer homology as free modules on path components. |
| `Calculations.With.Singleton` | Point degree-zero coefficient isomorphisms/positive vanishing. |
| `Calculations.With.Contractible` | Actual contractions give degree-zero coefficients/positive vanishing. |
| `Calculations.With` | Empty-space nonnegative ordinary vanishing/zero-module isomorphisms. |

`Chains.boundary n` is \(C_{n+1}\to C_n\).
Alternating boundaries start positive in `module_theory.Module.Over.Alternating.sum`; face \(i\) has sign \((-1)^i\).
Ordinary integer chains have zero negative terms.
Augmented chains `Chains.Reduced.complex` use augmentation \(C_0\to C_{-1}=\mathbb Z\), zero in degrees \(-2\) and below.

Supply `Bundle` of `module_theory.Module.Over` integer modules as coefficients.
Cochains are all functions on simplices; finite support is required only for chains.
`Cochains.With.At.productIsomorphism` exposes this as a module isomorphism.
`Relative.LongExact` connecting signs read boundaries of lifted relative cycles as subspace chains.

[Examples](../../examples/cohomology/README.md) checks representatives, both square-zero laws, augmentation, coefficient maps, relative connecting, and empty spaces from another package.
[Singular theory index](../README.md) and [concrete computations](../../examples/finite_models/README.md) collect excision/finite comparisons/products/examples.

[Build and check](../../../USAGE.md) from the repository root:

```sh
reftype/target/debug/cli libs/topology/singular/cohomology --module singular_cohomology --diagnostics compact
reftype/target/debug/cli libs/topology/examples/cohomology --module cohomology_models --diagnostics compact
```

Use shared workspace `libs/refcache/`.
Reexporting complexes under aliases retains captured type arguments in module instantiation.

`OverRing.With.integerCoefficients` gives canonical integer actions on coefficient additive groups.
Ring cochain/cohomology carriers are shared with ordinary underlying-integer-module theory.

Relative induced chain/cochain maps live in `Relative.Maps.Over.On.Integer` and its `With`.
Long-exact compatibility/comparison theorems live in each `Naturality`.
