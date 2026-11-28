# G06 Tubular neighborhoods and collapse maps

## Requirements

- Primary implementation: [`tubular_neighborhoods`](../libs/geometry/tubular_neighborhoods/README.md).
- Construct a diffeomorphism from a zero-section neighborhood in the normal bundle of a compact Euclidean submanifold to a neighborhood of its image.
- Construct boundary-compatible versions for neat half-space embeddings and families comparing tubular choices.
- Construct continuous collapse outside the normal disk bundle; prove stabilization, product, and homotopy comparisons.

## Dependencies

- [G05 Embeddings of compact manifolds](../libs/geometry/compact_embeddings/README.md)
- [Smooth bundles, frame bundles, and associated bundles](../libs/geometry/smooth_bundles/README.md)
- [C02 Disk bundles, sphere bundles, and Thom spaces](c02-thom-spaces.md)

## Status

G06 remains partially complete. This follow-up builds on the reflected doubles merged at `42e02b15`.

| Scope | Implementation and outstanding verification |
| --- | --- |
| Compact submanifolds | [Euclidean.On.Of.tubularNeighborhood](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of.ref) and `With.Compact` construct normal disk neighborhoods; [Restriction.diffeomorphism](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/With/Restriction.ref) gives a diffeomorphism. |
| Boundary compatibility | [HalfSpace.Of](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/HalfSpace.ref) constructs a homeomorphism onto an open subset of the G05 half-space and identifies its boundary with height zero on the base image. [Reflection on the double](../libs/geometry/tubular_neighborhoods/src/ReflectedDouble/On/With/Into/Reflected.ref) gives a continuous injective map whose nonnegative preimage is the original copy. For the G05 product collar, [Smooth](../libs/geometry/tubular_neighborhoods/src/ReflectedDouble/On/With/Into/Reflected/WithCollar/Using/Smooth.ref) constructs the ordinary smooth map. The immersion and transverse differential remain open. Smooth extension for arbitrary neat embeddings requires handling boundary jets beyond the product collar. |
| Choices and homotopies | [With.Compare](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/With/Compare.ref) supplies embedding families and collapse homotopies for a fixed lift. [Transition.Between](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/Transition/Between.ref) compares different lifts over their common open image by a diffeomorphism fixing the zero section. Homotopies between different lifts remain open. |
| Collapse and products | [Collapse.Of](../libs/geometry/tubular_neighborhoods/src/Collapse/Of.ref) provides continuity, `Disk.CollapseLaw` inside/outside-disk formulas, and [Product.Of](../libs/geometry/tubular_neighborhoods/src/Product/Of.ref) provides `multiplicative`. |
| Stabilization | [Stabilized](../libs/geometry/tubular_neighborhoods/src/Euclidean/On/Of/Stabilized.ref) contains `endpointFormula` and product-model `suspension`. Completeness of comparison, including stabilized normal Thom-space identification, remains unconfirmed. |
| Examples | [Flat](../libs/geometry/tubular_neighborhoods/src/Examples/Flat.ref) constructs a half-line extension and a tube through the boundary point. [Point](../libs/geometry/tubular_neighborhoods/src/Examples/Point.ref) constructs a compact interior tube using the G05 point embedding. [Interval](../libs/geometry/tubular_neighborhoods/src/Examples/Interval/Reflected.ref) uses the G05 neat embedding of the compact interval and locates both endpoints on the seam of its reflected double. |

Check the package through `python3 scripts/check.py run --scope changed --package tubular_neighborhoods` with the official checker. The [roadmap check status](_roadmap.md#progress-and-checks) describes the distinction between newly checked and reused modules.
