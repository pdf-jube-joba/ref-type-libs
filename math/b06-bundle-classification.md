# B06 Bundle classifying maps and stabilization

## Requirements

- Primary implementation: `bundle_classification`.
- Construct classifying maps to finite Grassmannians for bundles over compact Hausdorff bases.
- Prove independence of classifying-map choices and a bijection between homotopy classes and bundle isomorphism classes in sufficiently large ambient dimension.
- Extend to oriented real bundles and framed bundles; expose naturality under base maps, direct sums, and stabilization.

## Dependencies

- [B04 Bundle homotopy invariance and clutching](../libs/geometry/bundle_homotopy/README.md)
- [B05 Finite Grassmannians and universal bundles](b05-grassmannians.md)

## Implementation

Implemented in [bundle_classification](../libs/geometry/bundle_classification/README.md).

- Continuous finite-Grassmannian classifying maps for real and complex bundles, and comparison isomorphisms to universal-bundle pullbacks.
- Classification of bundles with componentwise varying ranks by all-rank projection families in finite-dimensional spaces.
- Choice independence by interpolating embeddings; equivalence and bijection between stabilized projection homotopy classes and bundle isomorphism classes.
- Classification of oriented real bundles by positive rays in determinant cotangent lines, and orientation-preserving homotopy classification.
- Finite Stiefel classifying maps and stabilization homotopies for framed bundles.
- Naturality for pullback, direct sums, and adding trivial bundles; minimal examples.

Additional public APIs implement direct sums and stabilization on framed-classification quotients and compatibility with the classification API.
For oriented bundles, proved products of finite-dimensional top forms, basis independence, and block-diagonal determinant products, constructing standard direct-sum orientations from factor orientations.
Prove openness of products of positive forms and continuity of determinant-bundle products using continuous coefficients in local trivializations.
Published stabilization by standard oriented trivial bundles, naturality for pullback, factor isomorphisms, finite classification, and choice independence of classification data.
Examples: `Examples.Trivial.Naturality.Oriented`.
