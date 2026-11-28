# `tubular_neighborhoods`

Tubular neighborhoods and collapse maps for Euclidean embeddings, with half-space restrictions and product comparisons.

| Entry | Purpose |
| --- | --- |
| [Euclidean.On.Of](src/Euclidean/On/Of.ref) | Normal-bundle lifts, the straight lift, and `tubularNeighborhood` for compact embedded manifolds |
| [With.Compact](src/Euclidean/On/Of/With/Compact.ref) and [With.Restriction](src/Euclidean/On/Of/With/Restriction.ref) | Normal disk neighborhoods and their diffeomorphisms |
| [Neat.Crossing.HalfTube](src/Euclidean/On/Of/Neat/Crossing/HalfTube.ref) and [HalfSpace](src/Euclidean/On/Of/HalfSpace.ref) | Half-space neighborhoods and a homeomorphism onto an open subset of the G05 half-space, with a zero-section formula and boundary equivalence |
| [ReflectedDouble](src/ReflectedDouble/On/With/Into/Reflected.ref) | Continuous injective reflection on the double and coverage of the nonnegative half by the original manifold |
| [Reflected.WithCollar.Using](src/ReflectedDouble/On/With/Into/Reflected/WithCollar/Using.ref) | Compact ordinary double using the G05 collar on both sides, with the signed product formula on its seam |
| [Examples](src/Examples.ref) | The flat half-line tube, a compact isolated-point tube using the G05 point embedding, and the reflected G05 interval |
| [With.Compare](src/Euclidean/On/Of/With/Compare.ref) | Neighborhood/radius comparisons and collapse homotopies for a fixed lift |
| [Transition.Between](src/Euclidean/On/Of/Transition/Between.ref) | Diffeomorphism between two tubular choices over their common open image, fixing the zero section |
| [Collapse.Of](src/Collapse/Of.ref) and [DiskImage](src/DiskImage.ref) | Continuous collapse from disk coordinates, including seam conditions |
| [Product.Of](src/Product/Of.ref) and [Stabilized](src/Euclidean/On/Of/Stabilized.ref) | Product-collapse compatibility, endpoint formulas, and product-model suspension |

`HalfSpace.Of` takes an ordinary embedded extension. The flat and isolated-point models construct this input. The reflected construction for a G05 collar-compatible embedding still needs the ordinary smooth immersion and a proof that its differential is transverse along the seam. Smooth boundary tubular charts, homotopies between different lifts, and the stabilized normal Thom-space identification remain open.

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Status](../../../math/g06-tubular-neighborhoods.md#status)
