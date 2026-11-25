# Finite models and coefficient comparisons

Finite-free-integer/singular chain equivalences give arbitrary-coefficient universal short exact sequences.
Finite model `homological_algebra.Finite.Bounded.Complex` stores degreewise finiteness, square-zero boundaries, boundedness.

| API | Contents |
| --- | --- |
| `Integer.Middle.exact` | Transport short exact sequences through middle module isomorphisms. |
| `Integer.CoefficientTensor.On.map` | Tensor integer chain maps with coefficients. |
| `Integer.CoefficientTensor.Homotopy.With.homotopy` | Tensor-transferred chain homotopies. |
| `Integer.CoefficientEquivalence.With.equivalence` | Arbitrary coefficient tensors preserve chain equivalences. |
| `Integer.HomZero.At.isomorphism` | Zero-differential nonnegative cohomology identified with termwise Hom. |
| `Integer.HomTransport.With.isomorphism` | Coefficient Hom isomorphisms by precomposing carrier isomorphisms. |
| `Integer.ProjectiveCone.On.equivalenceExists` | Bounded-below projective quasi-isomorphisms give equivalences retaining forward maps. |
| `Integer.Attachment.On.Kernel` / `Cokernel` | Arbitrary doubling kernels/cokernels from exact sequences with doubling connecting maps. |
| `Integer.Units.classification` | Integer products equal one imply both factors are 1 or both −1. |
| `Integer.Orientation.Normalize.existence` | Orientation-reversing top-degree automorphisms give homeomorphisms matching oriented generators. |
| `Integer.Finite.Compared.At` | Finite/singular universal-coefficient comparisons. |

`model` in `Finite` specifies finite-free integer complexes.
`comparison` in `Compared` specifies equivalences from them to actual singular chains.
Transfer comparisons to Hom/tensors, compose induced isomorphisms with finite-model universal sequences.

`universalCoefficient` middle terms are actual cohomology; ends Ext¹/Hom of model homology.
`homologyUniversalCoefficient` middle terms are coefficient singular homology; ends tensor/Tor₁ of model homology.
`homologyIsomorphism` identifies integer homology of both models.
`cohomologyIsomorphism` and `coefficientHomologyIsomorphism` expose arbitrary coefficient comparisons.
`splitting` comes from finite matrix splittings; the natural objects are exact sequences/endpoint maps.

`Integer.Finite.Groups.CohomologyCompared` and `HomologyCompared` transfer sequences directly from proved group isomorphisms.
Also applies when skeleton long exactness constructs comparisons.

`ProjectiveCone` takes integer complexes with projective nonnegative terms/zero negatives.
Restrict quasi-isomorphism cones nonnegatively to projective resolutions of zero.
Resolution homotopies contract cones; matrix components give inverses/both homotopies.
Forward maps remain actual supplied maps; inverse choices stay within existence propositions.

`HomZero` takes nonnegative complexes/coefficients, extracting coordinates from zero differentials.
By `At.onClass`, forward isomorphisms send cocycle classes to original cochains.

`Integer.Product.Compared.At.kunneth` gives integral product Künneth short exactness from finite-model tensor comparisons.
`Field.Product.Compared.At.kunneth` gives field cohomology tensor-sum/product isomorphisms from bounded finite cochain comparisons.
Both retain model/coefficient requirements in argument types.

Given comparisons for each factor, these entries put actual-space groups at endpoints.

| API | Inputs and results |
| --- | --- |
| `Integer.Product.Factors.nativeEquivalence` | Factorwise nonnegative-model/singular equivalences give tensor-total/product-singular equivalences. |
| `Integer.Product.Compared.Factors.At.kunneth` | Integer comparisons transfer endpoints to actual factor-homology tensor/Tor₁ sums. |
| `Integer.Product.Compared.Factors.At.Component.Resolution.resolution` | Projective resolutions of actual first-factor homology via transported model augmentations. |
| `Integer.Product.Compared.Factors.At.Splitting.isomorphism` | Chosen splitting isomorphisms from actual endpoint sums to product homology. |
| `Field.IntegralModel` | From bounded finite-free integer \(P\), finite field-coordinate cochains for \(\operatorname{Hom}_{\mathbb Z}(P,K)\). |
| `Field.IntegralProduct.Factors.At.kunneth` | Nonnegative factor chain comparisons give tensor-sum \(H^*(X;K)\), \(H^*(Y;K)\) to \(H^*(X\times Y;K)\) isomorphisms. |

`Field.IntegralProduct` tensors factor comparisons, then composes inverse Eilenberg–Zilber equivalences.
`singular_tensor_dual.Over.Mixed.On` connects integer-chain field Hom with field tensor products.
`IntegralModel` differentials conjugate boundary precomposition by coordinates; square zero/boundedness follow from models.

`Integer.Product.Factors.Signed` takes proofs that both integer models vanish negatively.
Compose integer/nonnegative-zero-extended tensor isomorphisms, constructing `comparison` and actual-factor-endpoint `At.kunneth`, `At.splitting`.
