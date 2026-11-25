# Concrete singular cohomology examples

Construction details and records for [cohomology_examples](../../../../libs/topology/examples/finite_models/README.md).
See [building and checking](../../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Finite-chain computations and comparisons with actual-space singular cohomology.
Supply coefficients \(A\) as integer-module bundles.
Explicit cochain values, quotient projections, coefficient changes track products/connecting maps on common representatives.

## Representatives and signs

Surface constructs semisimplicial chains from vertices/edges/triangles/three faces.
Edge coboundaries subtract start from end; triangle coboundaries are back minus diagonal plus front.
Surface.On.Simplicial.Coefficients compares free-chain linear maps with pointwise cochains.

Write projective edges \(a,b,d\), triangles \(P,Q\); then
\[
\partial P=a-d+b,\qquad \partial Q=a-b+d.
\]
For two-element \(u=(1,0,1)\), Alexander–Whitney gives \(u^2=(0,1)\).
Integral lifts have coboundary \((0,2)\); Bockstein is the degree-two generator class \((0,1)\).

On tori let projection classes be \(a,b\), oriented by \(a\smile b\).
Ring square vanishing/graded commutativity give
\[
a^2=b^2=0,\qquad b\smile a=-a\smile b
\]
Factor swaps interchange \(a,b\), acting by \(-1\) in degree two.

## Comparison entries

Graph.On.Geometry.Indexing gives injective integer vertex labels, subdivided-edge order, injective endpoint pairs.
Apply singular_simplicial realization comparisons to the resulting simplicial complexes.

ProjectivePlane.Geometry.Attachment.Comparison.Pair identifies attached-disk interiors with base complements and gives punctured-disk radial deformations fixing bases.
Relative homology/cohomology comparisons are induced by actual characteristic maps.

Two.Quotient identifies integer cyclic quotients with the two-element field.
Two.Quotient.Sequence constructs the coefficient sequence; Surface.On.Simplicial.Sequence transfers it to free-cochain short exact sequences.

ProjectivePlane.Geometry.CoefficientSequence proves finite restriction commutes with coefficient connecting maps.
This naturality identifies finite Bockstein values with actual quotient generators.
