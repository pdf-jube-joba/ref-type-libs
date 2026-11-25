# Finite ordered simplicial complexes

Construction details and records for [singular_simplicial](../../../../libs/topology/singular/simplicial/README.md).
See [building and checking](../../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`Complex[d].Object` is a downward-closed family of subsets of \(\{0,\ldots,d\}\).
`Complex[d].On[K].Simplex n` is strictly increasing \((n+1)\)-vertex lists spanning faces.
`Finiteness[n]` proves finite degreewise simplices, vanishing for \(n>d\).

`Realization` realizes unions of affine faces as standard-simplex subspaces.
`Chains.comparison` sends oriented simplices to affine singular simplices; face formulas prove chain compatibility.
`Chains.integerComparison` exposes the same integer-degree map.
`Chains.With` pulls cochains back for arbitrary integer modules.

`Realization.Stars` gives positive-barycentric-coordinate star covers.
Face-star intersections contract linearly to face barycenters.
`Cech` builds double complexes from ordered cover indices/intersection simplices.
Contract intersections vertically; add least cover vertices horizontally.
Both augmentations and carrier-preserving homotopies identify affine comparisons.

`Chains.HomotopyEquivalence.existence` and `integerExistence` prove equivalences with actual affine comparisons forward.
`quasiIsomorphism` and `At[z].isomorphism` expose integer homology comparisons.
`Chains.With[coefficients].Comparison.At[n].isomorphism` maps forward by cohomology induced from cochain restriction.

`Coordinates.Indexing` is finite-order degreewise enumeration data; `indexingExistence` proves existence.
`Coordinates.With[indexing].Bounded.model` is bounded finite-free with boundary matrices.
`Comparison.equivalenceExists` compares this matrix model to actual singular chains.

`Cup[R, ring].Product[p, q]` defines front/back Alexander–Whitney products.
`Compatibility.law` proves affine restriction strictly preserves them.
`Cup.Finite.Leibniz[p, q].law` gives finite-cochain Leibniz; `Finite.Product[p, q].Closed.law` closed finite products.
`Finite.Boundaries.left` and `right` prove boundary/cocycle products bound.
`Finite.Product[p, q].Cohomology.leftDescent` and `rightDescent` give representative invariance; `onClasses` identifies face-formula classes with compared products.

`Complex[d].LineGraph[V, E]` constructs one-dimensional complexes from vertex labels/distinct ordered edges.
`With[graph].Chains.Zero` and `One` identify vertex/edge free modules with actual simplicial chains.
`Higher[n].vanishes` vanishes above degree one; `Boundary.law` gives endpoint-minus-start incidence boundaries.
`Coefficients[A].Zero` and `One` identify arbitrary coefficient cochains with vertex/edge functions.
`Differential.law` identifies zero coboundaries with endpoint-value minus start-value maps.
