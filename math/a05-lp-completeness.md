# A05 Norms and completeness of Lp spaces

## Requirements

- Primary implementation: `lp_spaces`.
- Equip the existing Lp quotient with a norm and linear structure; prove Hölder, Minkowski, and completeness.
- Prove real and complex L2 Hilbert structures and density of integrable simple functions and compactly supported continuous functions.
- Construct continuity of translations and smoothing by approximate identities; expose density of compactly supported smooth functions.

## Dependencies

- [A03 Product measures and Fubini](a03-product-integration.md)
- [G01 Smooth bump functions and partitions of unity](g01-smooth-partitions.md)

## Implementation

`libs/analysis/lp_spaces/README.md` documents the public API and applicable measures and exponents.
`On.Finite` and `On.Infinity` give real Banach structures on the existing quotient; `On.Hilbert` and `On.Complex` give real and complex L2 Hilbert structures.
Prove simple-function approximation, density of compactly supported continuous and smooth functions on Euclidean space, translation continuity, Borel representatives and joint measurability, and smoothness, contraction estimates, and approximate-identity convergence for convolutions.
`Examples` and `EuclideanExamples` are checked examples using general measures, dimensions, finite real exponents, and quotient elements.
