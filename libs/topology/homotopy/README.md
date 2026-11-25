# `algebraic_topology`

Homotopies, pointed quotients, mapping cones, finite CW pairs, standard-simplex coordinates.

Unreduced cones and suspensions of empty inputs are empty; cone contractions require an input point. Reduced suspensions and smash products require basepoints.

| Entry | Purpose |
| --- | --- |
| `Interval` / `Arithmetic` / `IntervalFunctions` | Unit intervals, reversal/product/contraction time operations and continuity |
| `Interval.Convex` / `Initial` / `Halves` | Convex interpolation, initial subintervals, continuous half-interval reparametrizations |
| `Interval.Subdivision` / `SquareSubdivision` | Interval/square local-to-global principles via Lebesgue numbers and iterated bisection |
| `Interval.DiscreteMaps` / `SquareGluing` | Discrete-path constancy, square gluing |
| `Cylinder` / `Homotopy` | Cylinders, endpoints, constant/reversed/relative homotopies |
| `Homotopy.Composition` / `Concatenation` / `RelativeConcatenation` / `RelativeRelation` | Pre/postcomposition, closed-half concatenation, relative equivalence |
| `HomotopyEquivalence` / `Composition` / `Inverse` | Homotopy equivalence, homeomorphism construction, composition/inverses |
| `Pointed` / `Smash` | Pointed spaces/maps, smash products |
| `Collapse` / `Cone` / `Suspension` | Subset collapse, cones/contractions, reduced/unreduced suspensions |
| `Cofiber` / `Cofibration` / `Cofibration.ForTarget` | Mapping cones, cylinder-retraction cofibrations, homotopy extension |
| `Euclidean.Dimension` / `Geometry` | Finite coordinates, closed disks/boundary spheres/interiors, norms/closedness |
| `Simplex` / `At` / `Insertion` | Standard simplices, graded carriers, coordinate faces |
| `Simplex.Faces` / `Identities` | Continuous faces/composition identities |
| `Simplex.Vertices` / `Affine` / `AffineIdentity` / `AffineFaces` | Vertices, affine continuity/composition/face compatibility |
| `Simplex.Reindex` / `ReindexIdentity` / `ReindexFace` | Affine maps from vertex maps, composition/identity/face formulas |
| `Simplex.Degeneracy` / `Sections` / `Composition` / `Mixed` | Continuous adjacent-duplication degeneracies, two face right inverses, degeneracy/mixed identities |
| `Simplex.Boundary` / `BoundaryFace.Cover` | Closed/compact zero-coordinate boundaries, continuous face inclusions/coverage |
| `Simplex.Interval` | One-simplex/unit-interval inverse maps, endpoints/faces |
| `Simplex.Compactness` / `Barycentre` / `Metric` | Closedness/compactness, equal-weight barycenters, maximal-coordinate distances/Lebesgue numbers |
| `Simplex.Convex` / `Contraction` | Continuous convex combinations, point contractions |
| `Simplex.AffineMetric` / `Barycentre` | Diameter bounds from vertices, barycenter-distance shrink factors |
| `Simplex.Affine.Hull` / `ConvexFamily` | Affine convex closure, intersections of convex sets |
| `Simplex.BarycentricSubdivision` / `Mesh` / `At.Iterated.Decay` | Face-sequence subdivision cells, affine continuity, iterated diameter bounds/arbitrary-radius shrinking |
| `Semisimplicial` | Graded sets, face identities, preserving maps |
| `Simplex.Cylinder` / `CylinderAffine` | Cylinder affine evaluation, face/vertex/postcomposition formulas |
| `Contraction` / `Interval.Contraction` | Point homotopy equivalence, explicit interval contractions |
| `PathComponent` / `IntervalPaths` / `Functions` | Path-component quotients, interval-path comparison, descent of componentwise constants |
| `CW` / `Attach` / `Pair` | Finite CW complexes, attachments, subcomplexes/quotients |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
