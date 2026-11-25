# Concrete singular cohomology examples

Finite-chain computations and comparisons with actual-space singular cohomology.
Supply coefficients \(A\) as integer-module bundles.
Explicit cochain values, quotient projections, coefficient changes track products/connecting maps on common representatives.

| Object | Namespace | Contents |
| --- | --- | --- |
| Finite graphs | Graph.On.With | Spanning-forest primitives, finite-cochain coordinates by components/chords |
| Graph realizations | Graph.On.Geometry | Threefold edge subdivisions as actual finite simplicial complexes, mapped to affine singular simplices |
| Graph groups | Graph.On.Geometry.Coefficients.Singular | \(H^0\cong A^c\), \(H^1\cong A^k\), higher vanishing for \(c\) components, \(k=e-v+c\) chords |
| Finite circles | Circle | Zero-differential integer chains of rank one in degrees zero/one |
| Circle comparison | Circle.Geometry.FiniteComparison | Comparison with actual Euclidean-circle chains |
| Circle universal coefficients | Circle.Geometry.UniversalCoefficient | Actual singular short exact sequences for arbitrary integer modules from proved finite comparisons |
| Circle loops | Circle.Geometry.Loop.Primitive | Closed singular edges from squared upper semicircles, primitive homology classes |
| Circle evaluation | Circle.Geometry.Evaluation | Closed-cochain loop evaluation \(H^1(S^1;A)\cong A\) |
| Torus groups | Torus.Geometry.Comparison | Actual \(S^1\times S^1\) compared with tensor circle models |
| Torus top degree | Torus.Geometry.Ring.Primitive | Isomorphisms making projection products integral degree-two generators |
| Torus bases | Torus.Geometry.Ring.Basis / UnitBasis | Two degree-one projection bases, degree-zero unit generators |
| Torus products/swaps | Torus.Geometry.Ring | Projection degree-one classes, cups, factor-swap actions |
| Projective-plane space | ProjectivePlane.Geometry | Actual \(S^2/(x\sim-x)\), hemisphere quotients/disk-attachment comparisons |
| Finite projective plane | ProjectivePlane.With | Cochains with two vertices, three edges, two triangles |
| Integral coefficients | ProjectivePlane.Integral | Finite \(H^1=0\), \(H^2\cong\mathbb Z/2\) computations |
| Two-element coefficients | ProjectivePlane.ModTwo | Finite degree-one \(u\), \(u^2\ne0\) computations |
| Projective-plane groups | ProjectivePlane.Geometry.Cohomology | Arbitrary integer modules: degree-one doubling kernels, degree-two cokernels, higher zero |
| Actual integral/two-element coefficients | ProjectivePlane.Geometry.Integral / ModTwo | Quotient-space singular groups, generators/nonvanishing |
| Projective-plane ring | ProjectivePlane.Geometry.ModTwo.Ring | Actual quotient \(u^2=v\ne0\), \(u^3=0\), degree-zero units |
| Triangle restrictions | ProjectivePlane.Geometry.Restriction | Actual two-triangle restrictions, circle-loop degree-one detection, cup compatibility |
| Projective-plane Bockstein | ProjectivePlane.Geometry.Bockstein | Actual \(u\) maps to nonzero integral degree-two generators |
| Finite Bockstein | ProjectivePlane.Bockstein.Finite | Actual cochain connecting values for \(0\to\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb F_2\to0\) |

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
