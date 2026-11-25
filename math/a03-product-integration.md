# A03 Product measures and Fubini

## Requirements

- Primary implementation: `product_integration`.
- Construct products of σ-finite measures and compare them with Lebesgue measure on products of Euclidean spaces.
- Prove Tonelli's and Fubini's theorems and extend them to complex and finite-dimensional integrable functions.
- Expose conditions for convolution, interchange of integrals, support, and L1 norm bounds.

## Dependencies

- [A02 Lebesgue measure on Euclidean spaces](a02-lebesgue-measure.md)

## Implementation API

Implemented in [product_integration](../../libs/analysis/product_integration/README.md).
`Product` provides σ-finite product measures; `Integration` provides Tonelli and real-valued Fubini; `Complex` and `Vector` in the same module provide component-valued integrals.
`EuclideanProduct.Comparison.theorem` proves agreement of product measure under coordinate concatenation with the Borel restriction of Euclidean Lebesgue measure.
`Convolution.For.exists` derives a.e. integrability, integral interchange, and L1 bounds from conditions on jointly measurable convolution kernels; `Support.theorem` gives support inclusion.
Minimal examples are checked in `Examples`.
