# `normal_bundles` notes

[Package API](../../../libs/geometry/normal_bundles/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

`Dimension[n := n, k := k].On[M := M].Of[i := i]` constructs normal bundles of smooth immersions \(i:M\to\mathbb R^{n+k}\).
Keeps basepoints in \(M\), not image points, allowing self-intersections.
`Point` is the dependent basepoint/normal-vector pair; `At[x].subspace` is
\[
\{w\in\mathbb R^{n+k}\mid\forall v\in T_xM,\ \langle w,di_xv\rangle=0\}
\]

`InChart` and `Cover` prove local frames exist from derivative injectivity.
Smooth Gram–Schmidt orthonormalizes tangent directions, giving smooth complementary projections.
`calculus.ProjectionFrames` selects nonzero projection columns, shrinks to positive-norm opens, normalizes and reduces rank inductively.
Implements projection of central normal bases and Gram–Schmidt using projection columns/traces.
Includes positive denominators, smooth square roots/reciprocals, and rank equals codimension.

Sum decomposition: \((x,v,w)\mapsto(x,di_xv+w)\).
Inverses use orthogonal projections and derivative-image inverses from tangent Gram–Schmidt.
This yields smooth normal retractions and agreement of trivialization/ambient-product subspace topologies.
Stabilization appends real coordinates; dimension equalities transport via isometric isomorphisms.

Coordinate inclusions/parabolas: [tangent_normal](../../../libs/geometry/examples/tangent_normal/README.md).
General bundles, boundary manifolds, embedding existence, and tubular neighborhoods are subsequent topics.
