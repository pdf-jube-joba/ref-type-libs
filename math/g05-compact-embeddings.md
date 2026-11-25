# G05 Embeddings of compact manifolds

## Requirements

- Primary implementation: `compact_embeddings`.
- Construct smooth finite-dimensional Euclidean embeddings of closed compact manifolds from finite charts and cutoffs.
- Construct neat half-space embeddings compatible with collars for manifolds with boundary.
- Construct families joining stabilized embeddings; expose relative versions fixing the endpoints.

## Dependencies

- [G01 Smooth bump functions and partitions of unity](../../libs/geometry/smooth_partitions/README.md)
- [G02 Inverse and implicit functions and local forms of regular values](../../libs/geometry/inverse_implicit/README.md)
- [G04 Collars and boundary gluing](../../libs/geometry/manifold_gluing/README.md)

## Implementation

Implemented in [compact_embeddings](../../libs/geometry/compact_embeddings/README.md).

- `Compact.On.exists`: constructs actual Euclidean embeddings from finite charts/cutoffs, including empty manifolds.
- `NeatExistence.On.With.Compact.exists`: constructs neat half-space embeddings from compact doubles, Euclidean embeddings, collar collapse, and height; proves exact product formulas on positive-width collars.
- `Stabilization.On.Between`: exposes smooth stabilized embedding families, endpoint-fixing relative versions, and naturality under parameter changes and precomposition.
- `Naturality.On`: diffeomorphism pullback and comparisons of arbitrary construction results.
- `Examples`: empty manifold, point, real-line families, and closed-interval examples with endpoint images and collar conditions.
