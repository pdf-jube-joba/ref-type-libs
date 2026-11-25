# `boundary_manifolds`

Half-space/orthant charts, tangent cones and invariant derivatives, boundary/face tangent bundles, neat embeddings, products/intervals/disks.

Smooth maps have local open-set extensions. Weak inward/outward cones include tangent directions; strict signs are exposed separately for regular sublevels.

| Entry | Purpose |
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

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/boundary_manifolds.md)
