# Finite models and coefficient comparisons

Construction details and records for [singular_finite_algebra](../../../../libs/topology/singular/finite_algebra/README.md).
See [building and checking](../../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Finite-free-integer/singular chain equivalences give arbitrary-coefficient universal short exact sequences.
Finite model `homological_algebra.Finite.Bounded.Complex` stores degreewise finiteness, square-zero boundaries, boundedness.

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

`Field.IntegralProduct` tensors factor comparisons, then composes inverse Eilenberg–Zilber equivalences.
`singular_tensor_dual.Over.Mixed.On` connects integer-chain field Hom with field tensor products.
`IntegralModel` differentials conjugate boundary precomposition by coordinates; square zero/boundedness follow from models.

`Integer.Product.Factors.Signed` takes proofs that both integer models vanish negatively.
Compose integer/nonnegative-zero-extended tensor isomorphisms, constructing `comparison` and actual-factor-endpoint `At.kunneth`, `At.splitting`.
