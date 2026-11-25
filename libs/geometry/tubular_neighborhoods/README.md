# Tubular neighborhoods and collapse maps

`tubular_neighborhoods` contains the G06 implementation for compact Euclidean submanifolds, boundary-compatible neighborhoods, and collapse maps.
The public entry point is [src/root.ref](src/root.ref); direct dependencies are in [ref.toml](ref.toml).

| Module | Implemented scope |
| --- | --- |
| [Euclidean.On.Of](src/Euclidean/On/Of.ref) | Normal-bundle lifts, the straight lift, and `tubularNeighborhood` for compact embedded manifolds |
| [With.Compact](src/Euclidean/On/Of/With/Compact.ref) and [With.Restriction](src/Euclidean/On/Of/With/Restriction.ref) | Normal disk neighborhoods and their diffeomorphisms |
| [Neat.Crossing.HalfTube](src/Euclidean/On/Of/Neat/Crossing/HalfTube.ref) and [HalfSpace](src/Euclidean/On/Of/HalfSpace.ref) | Half-space neighborhoods and boundary preservation, with an extension supplied to `HalfSpace.Of` |
| [With.Compare](src/Euclidean/On/Of/With/Compare.ref) | Neighborhood/radius comparisons and collapse homotopies for a fixed lift |
| [Collapse.Of](src/Collapse/Of.ref) and [DiskImage](src/DiskImage.ref) | Continuous collapse from disk coordinates, including seam conditions |
| [Product.Of](src/Product/Of.ref) and [Stabilized](src/Euclidean/On/Of/Stabilized.ref) | Product-collapse compatibility, endpoint formulas, and product-model suspension |

Full G06 completion remains unconfirmed.
Construction of the half-space extension from G05 neat embeddings, comparisons between different lifts, and identification with stabilized normal Thom spaces still need verification.
`Line` is a construction model; standalone usage examples are still missing.
See the [G06 requirements and status](../../../math/g06-tubular-neighborhoods.md#status) for the detailed gaps.

No successful check of the current package and its full dependency closure is established by the records reviewed here.
For current commands and reporting requirements, see [checking the libraries](../../USAGE.md).
