# Spin and Spin-c structures

Spin and Spin-c structures are smooth cocycle lifts over a common cover by manifold charts. An SO reduction of a real bundle atlas supplies oriented orthonormal frames. Its changes of frame identify the local orientations and preserve a common fiber metric.

| Entry | Purpose |
| --- | --- |
| `Base.On.OnCover.SmoothPrincipal` | Smooth group cocycles, local product coordinates, and associated complex bundles |
| `Orthogonal.RealFrames.Over.On.Family.Of.Reduced` | Oriented orthonormal frame bundles of SO reductions of smooth real bundle atlases |
| `Orthogonal.Over.On.Covered.Of` | Spin and Spin-c lifts and their equivariant, fiberwise surjective maps to the frame bundle |
| `Orthogonal.Plots.projectSpin` and `SpinCProjection.Smooth.smooth` | Smoothness of the two group projections in coefficient coordinates |
| `Spinors.In.With.Over.On.Covered.Of` | Even-dimensional Spin and Spin-c spinor bundles in a chosen fixed coordinate frame of the I10 spinor model |
| `Orthogonal.Over.On.Covered.Of.SpinC.DeterminantLine.determinantLine` | The complex line associated to the character sending `[g, z]` to `z²` |
| `Pullback.Between.Along.Of.Orthogonal.Of` | Pullback of the frame cocycle and its Spin or Spin-c lift along a smooth map |

The principal bundle presentation gives inverse local product coordinates with smooth group-valued transition functions. The spinor and determinant bundles use the standard `smooth_bundles` complex bundle type. Pullback refines the source chart cover using the inverse images of the original chart domains, then composes the original transitions with the map in those charts.

[Source](src/root.ref) · [Specification](../../../math/i11-spin-structures.md) · [Checking](../../USAGE.md)
