# Manifolds

`Dimension[n := n]` uses coordinate spaces \(\mathrm{Fin}(n)\to\mathbb R\).

| Module | Contents |
| --- | --- |
| `Chart.Transition` | Open homeomorphisms and transitions |
| `Topological` / `AtlasData` / `Atlas` | Hausdorff second-countable covers, smooth transitions |
| `Atlas.saturate` / `Smooth.From` | Maximal atlases, construction from small atlases |
| `SmoothMap.Between` | Smooth maps via actual open-coordinate formulas |
| `Tangent.On.At` | Chart/vector quotients, tangent/cotangent spaces, coordinate isomorphisms |
| `Differential.Between.At` | Chart-independent derivatives |
| `DifferentialIdentity` / `DifferentialComposition` / `DiffeomorphismDifferential` | Identity/composition/diffeomorphism laws |
| `OpenSubmanifold.On.In` | Open submanifolds, inclusions/derivatives |
| `SmallAtlasSmoothMap` / `Presentation` | Atlas smoothness criteria, identity presentation diffeomorphisms |
| `SmoothCover` / `Tangent.On.Transport` | Open-cover gluing of smooth Euclidean maps, tangent/coordinate transport over equal bases |
| `Dimension.Examples` | Euclidean spaces/opens, point/empty manifolds |
| `EuclideanMap.Between` / `ChartMap.On.At` | Open-map/manifold-map conversions, smooth chart parametrizations |

Examples: [Geometry.ref](../coordinate_calculus/src/Geometry.ref).

## Bundle totals and immersion foundations

`IndexedAtlas` constructs topology/smoothness from arbitrarily indexed local parameters.
`BundleAtlas.Over` shares base-chart/finite-coordinate local products, selects countable subcovers, proving second countability of all-local-coordinate topologies.
Separate different bases in the base; different same-fiber points in one local product.
`FromCharts.Between.Covered` constructs smooth maps from covering small atlases without enumerating maximal atlases.
`ChartRestriction` restricts open chart images; `GlobalChart` constructs explicit diffeomorphisms from single covering charts.

`Immersion.Between.IsImmersion` means pointwise derivative injectivity.
`IsEmbedding` means immersion and image-subspace homeomorphism.
`EmbeddingLaws` equivalently requires point injectivity/open ambient lifts; `embeddingCriterion` connects them.
`OfEmbedding.homeomorphism` constructs actual image-subspace homeomorphisms.
`ImmersionIdentity`, `ImmersionComposition`, `DiffeomorphismImmersion` handle identity/composition/diffeomorphism pre/postcomposition.
`EmbeddingRetraction` constructs embeddings from smooth left inverses.
`EuclideanGlobal`, `EuclideanLinear`, `EuclideanPair` pass concrete whole-Euclidean maps/derivatives to manifold APIs.
Tangent/normal examples: [tangent_normal](../examples/tangent_normal/README.md).
