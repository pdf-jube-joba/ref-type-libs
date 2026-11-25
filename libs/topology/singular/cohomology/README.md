# `singular_cohomology`

Singular chains/cochains, relative/reduced theories, homotopy invariance, path components and contractible spaces.

Chains are finitely supported; cochains are all simplex functions with coefficients in integer modules.

| Entry | Purpose |
| --- | --- |
| `Simplices` / `At` / `Faces` / `Identities` | All simplices, constants, face maps/composition |
| `Chains` / `Boundary` / `SquareZero` | Free integer chains, alternating boundary/square zero, nonnegative/integer complexes |
| `Chains.Augmentation` | Degree-zero augmentation, boundary vanishing, point right inverses |
| `Chains.Reduced.NegativeOne` | Reduced degree-minus-one vanishing when nonempty, integer isomorphisms when empty |
| `Chains.Reduced` | Augmented chains with integers in degree \(-1\), coefficient reduced Hom |
| `Cochains.With` / `Cohomology` | Arbitrary-integer-module cochains, cocycles/classes/cohomology modules |
| `Cochains.With.At` | Isomorphism of arbitrary simplex assignments with cochains |
| `Cochains.OverRing.With` / `Relative.OverRing.With` | Commutative-ring coefficients, pointwise scaling, linear coboundaries, ordinary/relative ring modules |
| `Cochains.Abelian` | Canonical integer modules from abelian groups for cohomology |
| `Maps` / `Differential` / `Composition` | Postcomposition chain maps, boundary/composition laws, integer zero extensions |
| `Identity` / `Identity.Coefficients` | Continuous identities induce chain/cochain/cohomology identities |
| `Maps.Coefficients` | Space-contravariant/coefficient-covariant maps, generator evaluations |
| `Maps.Coefficients.Integer.At` | Integer/nonnegative cohomology comparison naturality in space/coefficients |
| `Maps.Composition.Coefficients` | Continuous-composition cohomology laws |
| `Homotopy` / `Coefficients` | Affine-prism chain homotopies, arbitrary-coefficient homotopy invariance |
| `Homotopy.Homology.At` | Integer singular-homology homotopy invariance |
| `Equivalence.With` | Cohomology module isomorphisms from space equivalences |
| `Relative` / `Injection` | Injective subspace chains, image quotients, relative short exactness |
| `Relative.Homology` / `LongExact` | Relative homology/connecting maps, zero composites, long exactness |
| `Relative.Split` / `Relative.With.PairSequence` | Degreewise split inclusions, cochain short/long exactness |
| `Relative.With.Vanishing` | Relative/vanishing-on-subspace cochain isomorphisms |
| `Relative.With` | Quotient-chain coefficient Hom/relative cohomology |
| `Relative.Support` | Subspace-valued simplex lifting, induced-chain images lie in subspace chains |
| `Relative.Equivalence.Over.On` | Relative homology/arbitrary-cohomology isomorphisms from inverse pair homotopies |
| `Relative.Identity` / `Maps.Over.Composition` | Relative identities/composition, homology/cohomology functoriality |
| `Relative.Maps.Over.Homotopy.On` | Subspace-preserving prisms induce relative homotopies/equal induced maps |
| `Relative.Maps.Over.On` / `Integer.With` / `Naturality` | Pair chain/cochain maps, inclusion/quotient/connecting naturality |
| `Coefficients.Sequence.On` / `Bockstein` | Coefficient-induced short exact cochains, Bockstein/exactness |
| `OrderedTuples` / `ConeBoundary` / `SquareZero` | Vertex-list free chains, alternating complexes, prepend-cone boundaries |
| `OrderedTuples.Prism` | Two-vertex-map prisms, boundaries, pre/postcomposition naturality |
| `OrderedTuples.Subdivision` / `Homotopy` / `Natural` | Chosen-center subdivision, boundary compatibility, identity homotopies, center-preserving naturality |
| `CylinderChains` | Vertex-to-affine-cylinder chain maps, universal prisms, face compatibility |
| `SimplicialChains.On` | Free chains/functoriality from arbitrary graded face-identity sets |
| `Zero.With.Functions` | Degree-zero cohomology as all coefficient-valued functions on path components |
| `Zero.Homology` | Degree-zero integer homology as free modules on path components |
| `Calculations.With.Singleton` | Point degree-zero coefficient isomorphisms/positive vanishing |
| `Calculations.With.Contractible` | Actual contractions give degree-zero coefficients/positive vanishing |
| `Calculations.With` | Empty-space nonnegative ordinary vanishing/zero-module isomorphisms |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../../USAGE.md) · [Notes](../../../../math/package-notes/topology/singular/cohomology.md)
