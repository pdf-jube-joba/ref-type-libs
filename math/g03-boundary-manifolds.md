# G03 Manifolds with boundary and corners

## Requirements

- Primary implementation: `boundary_manifolds`.
- Construct manifolds with boundary/corners, boundary faces, and smooth maps using half-space and orthant charts.
- Define boundary tangent bundles, inward/outward directions, neat embeddings, and product faces; prove coordinate-change compatibility.
- Construct intervals, disks, and manifold–interval products; compare restrictions to existing boundaryless manifolds.

## Dependencies

- [G02 Inverse and implicit functions and local forms of regular values](g02-inverse-implicit.md)

## Implementation

Implemented.
Public API and assumptions: [boundary_manifolds](../../libs/geometry/boundary_manifolds/README.md).

| Requirements | Implementation |
| --- | --- |
| Half-space/orthant charts, manifolds, and smooth maps | `Model`, `Dimension`, `SmoothMap`, `MapIdentity`, `MapComposition` |
| Boundary faces and tangent bundles | Faces retaining corners and tangent bundles in `Face.On`; globally embedded faces in `Face.Global`; boundary manifolds and tangent bundles from half-space covers in `Boundary.Of.Build` |
| Inward/outward directions and coordinate invariance | `OneSided`, `Model.RayControl`, `ConeMap`, `Extensions.Local`, `Tangent.On.At.Cones`, `Differential` |
| Neat embeddings | Intrinsic conditions and normal-coordinate criteria in `Immersion`, `Neat`; `NeatIdentity` |
| Product boundary faces | Product charts, factorwise face criteria, and intrinsic boundary-union laws in `Product` |
| Intervals, disks, and manifold–interval products | G02 local-form construction in `Sublevel`; `Disk`, `Interval`, `Cylinder`, `Examples` |
| Boundaryless-manifold comparison | Empty-coordinate-constraint construction/homeomorphism in `Boundaryless`; restriction to existing ordinary manifolds in `Interior` |
