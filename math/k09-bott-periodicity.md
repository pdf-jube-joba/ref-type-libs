# K09 Bott periodicity and integer degrees

## Requirements

- Primary implementation: `periodic_k_theory`.
- Construct two-periodic Bott external-product isomorphisms in relative/reduced theories; extend to all integer degrees.
- Prove graded-product signs, six-term exact sequences, and naturality.
- Compute point/sphere K-groups and iterated Bott generators; prove degree-minus-one vanishing at a point.

## Dependencies

- [K08 Bott's basic product theorem](k08-bott-product.md) (implemented)

## Published implementation

Implemented in [periodic_k_theory](../../libs/topology/periodic_k_theory/README.md).

- `Reduced` and `RelativePair` construct actual Bott external products/inverses; `Formula.productFormula` proves agreement with existing relative external products.
- `TwoShift`, `Negative`, `Integer` give double-suspension comparisons, natural two-periodicity, all integer degrees, and comparisons with original negative degrees.
- `Product.gradedCommutative` proves Koszul signs for actual factor swaps.
- `SixTerm` and `SixTerm.Naturality` give exactness at six positions and six natural commutative diagrams.
- `Point.oddZero` proves ordinary-point degree-minus-one vanishing from general-linear-group path connectedness and interval/boundary-pair computations.
- `Point.At`, `Spheres.At`, `Spheres.Ordinary`, `Spheres.OrdinaryOdd` compute point/sphere groups; `BottSpheres` gives iterated Bott external-product generators.
- `Examples` exposes minimal point-vanishing, generator, Bott-isomorphism, and negative-periodicity round-trip examples.

Standard checks use repository `cargo build -p cli --release --locked` and `python3 scripts/check_all.py --memory-mib 10240`.
