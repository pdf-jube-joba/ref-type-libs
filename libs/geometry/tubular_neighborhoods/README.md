# `tubular_neighborhoods`

Tubular neighborhoods, collapse maps, boundary comparisons and product/stabilization identities; requirements and checks remain partly unverified.

Completion and full dependency checks remain unconfirmed. Half-space extensions, comparisons between different lifts and stabilized Thom-space identification still need verification; standalone examples are missing.

| Entry | Purpose |
| --- | --- |
| [Euclidean.On.Of](src/Euclidean/On/Of.ref) | Normal-bundle lifts, the straight lift, and `tubularNeighborhood` for compact embedded manifolds |
| [With.Compact](src/Euclidean/On/Of/With/Compact.ref) and [With.Restriction](src/Euclidean/On/Of/With/Restriction.ref) | Normal disk neighborhoods and their diffeomorphisms |
| [Neat.Crossing.HalfTube](src/Euclidean/On/Of/Neat/Crossing/HalfTube.ref) and [HalfSpace](src/Euclidean/On/Of/HalfSpace.ref) | Half-space neighborhoods and boundary preservation, with an extension supplied to `HalfSpace.Of` |
| [With.Compare](src/Euclidean/On/Of/With/Compare.ref) | Neighborhood/radius comparisons and collapse homotopies for a fixed lift |
| [Collapse.Of](src/Collapse/Of.ref) and [DiskImage](src/DiskImage.ref) | Continuous collapse from disk coordinates, including seam conditions |
| [Product.Of](src/Product/Of.ref) and [Stabilized](src/Euclidean/On/Of/Stabilized.ref) | Product-collapse compatibility, endpoint formulas, and product-model suspension |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Status](../../../math/g06-tubular-neighborhoods.md#status)
