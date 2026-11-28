# `tubular_neighborhoods`

Tubular neighborhoods and collapse maps for Euclidean embeddings, with half-space restrictions and product comparisons.

| Entry | Purpose |
| --- | --- |
| [Euclidean.On.Of](src/Euclidean/On/Of.ref) | Normal-bundle lifts, the straight lift, and `tubularNeighborhood` for compact embedded manifolds |
| [With.Compact](src/Euclidean/On/Of/With/Compact.ref) and [With.Restriction](src/Euclidean/On/Of/With/Restriction.ref) | Normal disk neighborhoods and their diffeomorphisms |
| [Neat.Crossing.HalfTube](src/Euclidean/On/Of/Neat/Crossing/HalfTube.ref) and [HalfSpace](src/Euclidean/On/Of/HalfSpace.ref) | Half-space neighborhoods and a homeomorphism onto an open subset of the G05 half-space, with a zero-section formula and boundary equivalence |
| [ReflectedDouble](src/ReflectedDouble/On/With/Into/Reflected.ref) | Continuous injective reflection on the double and coverage of the nonnegative half by the original manifold |
| [Reflected.WithCollar.Using](src/ReflectedDouble/On/With/Into/Reflected/WithCollar/Using.ref) | Compact ordinary double using the G05 collar on both sides, with the signed product formula on its seam |
| [Reflected.WithCollar.Using.Smooth](src/ReflectedDouble/On/With/Into/Reflected/WithCollar/Using/Smooth.ref) | Smooth reflected map on the collared double, including its ordinary Euclidean coordinate map |
| [Reflected.WithCollar.Using.Smooth.Immersion](src/ReflectedDouble/On/With/Into/Reflected/WithCollar/Using/Smooth/Immersion.ref) | Ordinary reflected embedding and normal derivative witnesses along the seam |
| [Transverse.InCodimension.Of](src/ReflectedDouble/On/With/Into/Reflected/WithCollar/Using/Smooth/Immersion/Transverse/InCodimension/Of.ref) | Constructs the `Extension` required by `HalfSpace.Of` for a G05 product collar in the represented ambient dimension. Its tube is the boundary-preserving restriction of an ordinary diffeomorphism. |
| [Reflected.WithCollar.Extend](src/ReflectedDouble/On/With/Into/Reflected/WithCollar/Extend.ref) | Local smooth coordinate extensions across the seam for arbitrary neat embeddings |
| [Examples](src/Examples.ref) | The flat half-line tube, a compact isolated-point tube using the G05 point embedding, and the reflected G05 interval |
| [With.Compare](src/Euclidean/On/Of/With/Compare.ref) | Neighborhood/radius comparisons and collapse homotopies for a fixed lift |
| [Transition.Between](src/Euclidean/On/Of/Transition/Between.ref) | Diffeomorphism between two tubular choices over their common open image, fixing the zero section |
| [Collapse.Of](src/Collapse/Of.ref) and [DiskImage](src/DiskImage.ref) | Continuous collapse from disk coordinates, including seam conditions |
| [Product.Of](src/Product/Of.ref) and [Stabilized](src/Euclidean/On/Of/Stabilized.ref) | Product-collapse compatibility, endpoint formulas, and product-model suspension |

For a G05 collar-compatible embedding, the reflected map gives the ordinary embedded extension for the half-space tube. The resulting tube maps are restrictions of smooth maps on the doubled neighborhoods. For an arbitrary neat embedding, the local extensions still need to be glued with injectivity and the height sign controlled on the extended side. Intrinsic boundary tubular charts, homotopies between different lifts, and the stabilized normal Thom-space identification remain open.

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Status](../../../math/g06-tubular-neighborhoods.md#status)
