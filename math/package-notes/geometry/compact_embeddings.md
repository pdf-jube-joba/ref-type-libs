# Embeddings of compact manifolds

Construction details and records for [compact_embeddings](../../../libs/geometry/compact_embeddings/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Construct finite-dimensional Euclidean embeddings of compact smooth manifolds from finite charts and compact cutoffs.

Embeddings are actual `manifolds.Immersion.Embedding` maps with injective derivatives/points and open-set lifts giving image homeomorphisms.

## Closed manifolds

`Compact[n].On[M].exists compact` proves existence of `Result`.

`Result.dimension` is constructed dimension; `Result.embedding` its smooth Euclidean embedding.

Includes empty manifolds, using dimension zero.

Nonempty zero-dimensional manifolds use the same cutoffs.

Choose `smooth_partitions` local bumps on chart covers; compactness gives finite plateau covers.

For charts \(\phi_i\), cutoffs \(b_i\), each block is
\[
x\longmapsto \bigl(b_i(x),b_i(x)\phi_i(x)\bigr)
\]

Extend product coordinates by zero off charts.

Support containment ensures smooth zero extension.

Near every point some \(b_i\) equals one, recovering chart coordinates.

This proves map/derivative injectivity.

Compact closed images in Hausdorff targets give image homeomorphisms.

Finite chart/cutoff choices are not assumptions on results.

`Naturality.On.Comparison` joins arbitrary choices by smooth stabilized embedding families.

## Stabilized embedding families

`Stabilization[n,a,b].On[M].Between[f,g]` constructs for smooth embeddings \(f:M\to\mathbb R^a\), \(g:M\to\mathbb R^b\)
\[
H_t(x)=((1-t)f(x),t g(x))\in\mathbb R^{a+b}
\]

`embedding[t]` returns actual `manifolds.Immersion.Embedding` at every real \(t\).

For \(t\ne0\), recover \(g\) by right projection scaled by \(t^{-1}\); at zero recover \(f\) by left projection.

Smooth recovery proves derivative/point injectivity and open lifts, without compactness of the original manifold.

`leftEndpoint` and `rightEndpoint` give endpoints \((f,0)\), \((0,g)\).

`Linear.InChart[c].map` is an actual smooth coordinate map on \(\mathbb R\times c.image\); `formula` identifies it with \(H\).

`Parameters[k].On[U,s].Local[c]` handles arbitrary open parameter domains/smooth scalar clocks \(s\).

`Reparametrization[j].From[V,r].natural` proves compatibility with smooth parameter pullback.

`Relative.embeddingAt[t]` uses `smooth_partitions.Exponential.Step.value` as a clock, equal to \((f,0)\) for \(t\le0\) and \((0,g)\) for \(t\ge1\).

`Relative.InChart[c].map` proves actual smoothness across endpoints.

Parameterized `fixedLeft` and `fixedRight` also fix endpoints on regions where clocks equal zero/one.

`Naturality[p].From[P].Of[h]` handles smooth embedding precomposition \(h:P\to M\), proving agreement for linear/relative clocks.

`Example` instantiates coordinate-axis families with fixed ends from real-line identity embeddings.

## Naturality and examples

`Naturality[n].On[M].From[p].On[P].Along[d].Of[result].transport` constructs diffeomorphism pullbacks of embeddings.

`dimension`, `formula`, `recover` give dimension preservation, precomposition formulas, inverse recovery.

`Naturality.On.Comparison[left,right]` compares arbitrary existence results, exposing stabilized embeddings/endpoints/smooth families fixed outside the parameter interval.

`Examples.Point.exists` applies existence to the point in zero-dimensional Euclidean space.

`Examples.Empty[n].exists` handles empty manifolds of arbitrary dimension.

`Examples.Point.At[a].embedding` embeds points at real \(a\); `Point.path` and `Point.relative` join zero/one embeddings after stabilization.

## Boundary manifolds and exact collar compatibility

`NeatExistence[n].On[M].With[cover].Compact[compact].exists` constructs `Result` for compact boundary manifolds of dimension \(1+n\).
`cover` is the existing boundary-chart cover.
Results include finite dimension `dimension`, constructed collars/positive widths, actual `boundary_manifolds.Neat.Embedding`.
Target `HalfSpace[k].manifold` is Euclidean space times the nonnegative half-line; `HalfSpace.coordinates` and inverse identify standard finite half-spaces.

Construct smooth doubles; collar/interior coordinates prove one-sided inclusion immersions.
Compact boundaryless doubles give Euclidean embeddings \(e\) by the closed theorem.
Global collar height \(h\) is zero exactly on boundaries, positive inside, with inward normal derivative surjecting positively.

Also construct smooth collar-time collapse \(r\).
In narrow collars \(r(c(b,t))=b\); off compact collar support, \(r\) is identity.
Final embedding: \(x\mapsto(e(r(x)),h(x))\).
Prove \(r,h\) separate points and their joint derivative injective.
Thus `Result.compatible` guarantees exact \(F(c(b,t))=(F_{\partial}(b),t)\) on a positive-width collar.

`Examples.Interval.Compactness.compact` proves concrete closed-interval compactness.
`Examples.Interval.Neat.exists` applies existence there; `Of[result]` proves only endpoints hit target boundaries, endpoint images differ, and exact collar compatibility.
