# Manifolds with boundary and corners

Local models intersect open finite-dimensional Dedekind-real sets with orthants constraining selected coordinates nonnegative.
`Dimension.Manifold` has local homeomorphisms to these models, open covers, smoothly extendible transitions, Hausdorffness, and second countability.
One constraint gives half-spaces, all give orthants, none give ordinary open sets.

| Module | Public constructions and laws |
| --- | --- |
| `Model[n]` | Constraints, orthants, active coordinates, faces, inward cones, tangent subspaces, actual subspace topology |
| `Dimension[n].Quadrant[C, U]` | Corner manifolds from arbitrary open/orthant intersections |
| `Dimension.Chart.At.Extension` | Smooth extensions agreeing with transitions near basepoints in ordinary open sets |
| `Extensions.Local` / `ConeMap.On` | Extension-independent derivatives and tangent-cone preservation by orthant-preserving derivatives |
| `Tangent[n].On[M].At[x]` | Tangent spaces as chart/vector quotients, vector structures, coordinate isomorphisms |
| `Tangent.On.At.Cones` | Invariant `Inward`, `Outward`, `Tangential`, `Boundary` and chartwise criteria |
| `SmoothMap[n, m].Between[M, N]` | Smooth maps via continuous maps and local smooth extensions |
| `MapIdentity` / `MapComposition` | Identities, composition, extension chain rules |
| `Differential[n, m].Between[M, N]` | Actual tangent linear maps, cone preservation, domain/codomain coordinate-change laws |
| `Immersion` / `Neat` | Immersions, embeddings homeomorphic onto images, neat embeddings and normal-coordinate criteria |
| `Face[n, r].On[C, U]` | Faces setting rightmost \(r\) coordinates zero, remaining constraints, smooth embeddings/face tangent bundles |
| `Face.On.At` | Inverse correspondence of face-inclusion derivatives and normal-coordinate kernels, criteria in arbitrary ambient charts |
| `Face[n, r].Global[F, M]` | Embedded global-face normal forms and image conditions |
| `Boundary[n].Of[M].Build[cover]` | Ordinary \(n\)-dimensional boundary manifolds from half-space-chart covers, tangent bundles |
| `Product[n, m].Of[M, N]` | Product topology/charts/second countability, factorwise boundary criteria |
| `Interior[n].Of[M].Build[]` | Existing `manifolds` manifolds with saturated atlases from interior restrictions |
| `Boundaryless[n].Of[M]` | Existing boundaryless manifolds as unconstrained corner manifolds, homeomorphisms/empty boundaries |
| `Sublevel[n].Of[U, f].Build[regular]` | Half-space charts for regular nonnegative regions, boundary zeros, boundary manifolds/tangent bundles |
| `Sublevel.Of.Face[regular]` | G02 regular-value manifolds of the same zero set, inclusion embeddings, tangent/actual-derivative-kernel isomorphisms |
| `Disk[n]` / `Interval[]` / `Cylinder[n].On[M]` | Closed disks \(D^{n+1}\), intervals \([-1,1]\), existing-manifold/interval products |

## Coordinate invariance

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

## Faces and examples

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

[Examples.ref](src/Examples.ref) instantiates half-lines, planar orthants, face embeddings, disks, intervals, strips, and ordinary interiors.
`Examples.Nonlinear` checks smoothness/derivatives of \(t\mapsto t^2\) on half-lines.
`Examples.EmptyCoordinates` handles zero-dimensional disks and empty coordinate sets.

## Checks

[Build and check](../../USAGE.md) from the repository root:

```sh
reftype/target/release/cli libs/geometry/boundary_manifolds --module boundary_manifolds --full-check-local --memory-mib 12288 --cache-stats
```
