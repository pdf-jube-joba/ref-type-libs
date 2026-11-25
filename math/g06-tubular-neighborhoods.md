# G06 Tubular neighborhoods and collapse maps

<a id="status"></a>

## Status

Read-only inspection of main `dce3d353e75972c507928253d6c33420f6f55a0f` on 2026-11-19.
`tubular_neighborhoods` is registered in the workspace with 40 `.ref` files.
An implementation exists, but the following verification remains; full-plan completion is unconfirmed.

| Scope | Implementation and outstanding verification |
| --- | --- |
| Compact submanifolds | [Euclidean.On.Of.tubularNeighborhood](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of.ref) and `With.Compact` construct normal disk neighborhoods; [Restriction.diffeomorphism](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/With/Restriction.ref) gives a diffeomorphism. |
| Boundary compatibility | [Neat.Crossing.HalfTube](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/Neat/Crossing/HalfTube.ref) provides a half-space homeomorphism and boundary preservation. [HalfSpace.Of](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/HalfSpace.ref) requires `Extension[f]`; construction from G05 neat embeddings remains unconfirmed. |
| Choices and homotopies | [With.Compare](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/With/Compare.ref) compares neighborhoods/radii for the same `lift`, providing embedding families and collapse homotopies. Coverage of comparisons between different tubular-map choices remains unconfirmed. |
| Collapse and products | [Collapse.Of](../libs/geometry/tubular_neighborhoods/src/Collapse/Of.ref) provides continuity, `Disk.CollapseLaw` inside/outside-disk formulas, and [Product.Of](../libs/geometry/tubular_neighborhoods/src/Product/Of.ref) provides `multiplicative`. |
| Stabilization | [Stabilized](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/Stabilized.ref) contains `endpointFormula` and product-model `suspension`. Completeness of comparison, including stabilized normal Thom-space identification, remains unconfirmed. |
| Documentation and examples | The [package README](../libs/geometry/tubular_neighborhoods/README.md) now describes the available modules and remaining gaps. Standalone examples are still missing; `Line` is the disk model used in construction. |

No record confirming successful type checking of the current sources and dependency closure has been found.
The scope of inspected records is documented in the [roadmap check status](_roadmap.md#progress-and-checks).

## Requirements

- Primary implementation: `tubular_neighborhoods`.
- Construct a diffeomorphism from a zero-section neighborhood in the normal bundle of a compact Euclidean submanifold to a neighborhood of its image.
- Construct boundary-compatible versions for neat half-space embeddings and families comparing tubular choices.
- Construct continuous collapse outside the normal disk bundle; prove stabilization, product, and homotopy comparisons.

## Dependencies

- [G05 Embeddings of compact manifolds](../libs/geometry/compact_embeddings/README.md)
- [Smooth bundles, frame bundles, and associated bundles](../libs/geometry/smooth_bundles/README.md)
- [C02 Disk bundles, sphere bundles, and Thom spaces](c02-thom-spaces.md)
