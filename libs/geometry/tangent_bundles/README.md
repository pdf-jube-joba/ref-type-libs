# Tangent bundles

Construct tangent total spaces of finite-dimensional smooth boundaryless manifolds.
Point tangents/derivatives use `manifolds.Tangent.On.At`, `manifolds.Differential`.

`Point` in `Dimension[n := n].On[M := M]` is the dependent pair of base `base` and tangent `vector`.
`Fiber[x].isomorphism` identifies projection fibers with existing tangents linearly.
`coordinate` and `point` in `InChart[c]` are inverse, with coordinate formula
\[
(x,v)\longmapsto(\varphi(x),d\varphi_xv)
\]
`Change` constructs smooth matrix transitions \((u,w)\mapsto(f(u),Df_u w)\).
`topology`, `hausdorff`, `secondCountable`, `manifold` expose total topology and \(2n\)-dimensional smoothness.
Topologies use all charts; countable subcovers are used only for second countability.

| API | Contents |
| --- | --- |
| `SmoothProjection.map` / `SmoothZero.map` | Projection/zero sections |
| `Addition` / `Scaling` | Same-base addition/scaling, domain manifolds/smooth maps |
| `Map.Between.Of[f].map` | Smooth tangent maps from point derivatives |
| `Identity.On` / `Composition.Between.Of` | Functor laws as total functions/smooth maps |
| `Diffeomorphism.Between.Of` | Diffeomorphisms inverted by inverse-diffeomorphism tangent maps |
| `FrameBundle.Over.Family` | Shared local coordinates from fiber isomorphisms |
| `Trivial.On.Covered` | \(M\times\mathbb R^r\) totals/product homeomorphisms/smooth pairing |
| `ScalarProduct.On.Covered` | \(M\times\mathbb R\) using actual real scalars |

`FrameBundle` construction data/inverse/linearity laws are grouped in `Local`, `Data` and linear isomorphisms.
`Using.Build` builds manifolds from smooth transitions; `Morphism.Build.Inverse` builds total diffeomorphisms from smooth fiber-isomorphism families.
Addition uses fiber sums, scaling real/bundle fiber products, with the same construction.

External-package public examples: [tangent_normal](../examples/tangent_normal/README.md).
Normal bundles/sums/stabilization: [normal_bundles](../normal_bundles/README.md).
