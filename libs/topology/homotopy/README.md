# Algebraic-topology space constructions

Construct homotopies, pointed spaces, cell attachments, finite CW pairs from real closed intervals.

| Module | Contents |
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
| `Simplex.Reindex` / `ReindexIdentity` / `ReindexFace` | Affine maps from vertex maps, composition/identity/face formulas. |
| `Simplex.Degeneracy` / `Sections` / `Composition` / `Mixed` | Continuous adjacent-duplication degeneracies, two face right inverses, degeneracy/mixed identities. |
| `Simplex.Boundary` / `BoundaryFace.Cover` | Closed/compact zero-coordinate boundaries, continuous face inclusions/coverage. |
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

`FiniteComplex` is a subset type storing characteristic maps, attachments, Hausdorffness, weak topology.
Disk opens use `Euclidean.Dimension.diskTopology`, checking characteristic continuity with the same singular-chain topology.
`Cofibration.ForTarget.homotopyExtension` proves extension assuming cofibrations.

`Cone` and unreduced suspensions quotient cylinders, hence are empty for empty inputs.
`Cone.Contraction.contract` takes an input-space point.
Reduced suspensions/smash products take input basepoints.

[Examples](../examples/cells/src/root.ref) includes intervals, disks/spheres, one-cell attachments, empty CW pairs, graded simplices.
Check instructions: [library index](../../README.md#type-checking).
