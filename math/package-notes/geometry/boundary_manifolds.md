# `boundary_manifolds` notes

[Package API](../../../libs/geometry/boundary_manifolds/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Local models intersect open finite-dimensional Dedekind-real sets with orthants constraining selected coordinates nonnegative.
`Dimension.Manifold` has local homeomorphisms to these models, open covers, smoothly extendible transitions, Hausdorffness, and second countability.
One constraint gives half-spaces, all give orthants, none give ordinary open sets.

### Coordinate invariance

Smoothness assumes existence of open-set extensions.
Agreement of extension derivatives and cone preservation are not inputs.
`Model.Extension` proves partial agreement using positive-direction difference quotients valid at boundaries.
`Extensions.Local` intersects neighborhoods and lifts to total-derivative agreement.
Apply to inverse/composite transitions to derive tangent equivalence, coordinate isomorphisms, and derivative transformation laws.

`Model.RayControl` proves short positive rays stay in orthants for vectors nonnegative in active coordinates.
`ConeMap` proves cone preservation using `OneSided` one-sided minimum derivative inequalities.
`Cones.criterion` transfers one-chart criteria to every chart; `Lineality.criterion` identifies tangent directions with active-coordinate zeros.
Here `Inward` and `Outward` are weak cones including tangent directions.
For regular defining functions, `Sublevel.Of.Face.Kernel` exposes strict inward/outward/tangent directions by positive/negative/zero derivatives.

`Neat.Laws` requires embedding, boundary preimage conditions, derivative surjectivity modulo target tangents, and tangent-preimage conditions.
`Neat.At.Coordinates.criterion` equates surjectivity with active-coordinate normal equations.
Identity example: `NeatIdentity`.

### Boundary faces

`cover` in `Boundary.Build` covers the boundary by half-space charts.
At corners, `Face.On` retains remaining constraints, constructing faces as corner manifolds.
`Face.Global` normal forms identify face images with selected normal coordinates zero.
`Product.Boundary.criterion` and `Product.Of.At.boundaryCriterion` give
coordinate and intrinsic formulas for \(\partial(M\times N)=(\partial M\times N)\cup(M\times\partial N)\).
Product constraints sum both factors, retaining both at face intersections.

`Sublevel` assumes defining derivatives surjective at zeros.
Use actual local diffeomorphisms from G02 `Submersion.localExistence` to straighten regions to half-spaces.
`Disk[n]` uses \(1-\sum_i x_i^2\), proving surjectivity from sphere radial derivatives.
`Disk.boundary` is the general boundary construction; `regularBoundary` is the G02 regular-value sphere.
`Interval.At.criterion` identifies interval boundaries with endpoints; `Cylinder.On.At.criterion` identifies product boundaries with two end faces.

## Examples

[Examples.ref](../../../libs/geometry/boundary_manifolds/src/Examples.ref) instantiates half-lines, planar orthants, face embeddings, disks, intervals, strips, and ordinary interiors.
`Examples.Nonlinear` checks smoothness/derivatives of \(t\mapsto t^2\) on half-lines.
`Examples.EmptyCoordinates` handles zero-dimensional disks and empty coordinate sets.
