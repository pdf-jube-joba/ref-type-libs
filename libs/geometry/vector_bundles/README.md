# Real and complex finite-rank vector bundles

Public entry: `vector_bundles.Bundles`.
`Bundles.Real.scalar` and `Bundles.Complex.scalar` group [L03](../../algebra/hermitian_frames/README.md) topological fields/conjugation and existing real/complex dimension uniqueness.
`Over[K, field, conjugation, scalar]` uses this shared API.
Reuse [linear_algebra](../../algebra/linear_algebra/README.md) maps/isomorphisms/bases/traces.

## Bundles and local trivializations

`Family[X := X, F := F]` takes base \(X\), fiber sets \(F:X\to\mathrm{Set}\).
`Point` pairs base `base` and vector `vector: F base` dependently; `include`, `projection` insert/project total spaces.
`Data` stores base/total topologies and fiber linear structures; `Bundle` is locally trivial data.

`With[data].ChartData` groups open domains, finite dimensions, fiber/standard-coordinate isomorphisms.
`With.In[c].Laws` means open base/total regions and continuous coordinates/inverses.
`Chart` is a trivialization with these laws.
`With.In.homeomorphism` constructs homeomorphisms from total opens to base-open/standard products using inverse linear laws.

`Of[bundle].projectionContinuous` glues trivializations to prove projection continuity.
`Of.Fiber[x].isomorphism` linearly identifies actual projection preimages with \(F(x)\); `decodeEncode`, `encodeDecode` guarantee inverses.

Rank is not input data.
`Dimension.At.basis` constructs finite bases from coordinate isomorphisms, proving unique dimensions via traces and injective scalar natural embeddings.
`Of.rank` is unique dimension; `rankFrame` agrees with local dimensions.
`rankLocallyConstant` proves rank locally constant.
Handles empty bases, dimension zero, varying finite component ranks.

## Bundle maps, isomorphisms, and sections

| API | Contents |
| --- | --- |
| `Over.Morphisms` | Fiber-linear maps over \(f:X\to Y\) with total continuity. |
| `Morphisms.total` / `projection` / `onFiber` / `ext` | Total maps, projection compatibility, fiber formulas/extensionality. |
| `Morphisms.Composition.compose` / `Over.Identity.map` | Composition/identity bundle maps. |
| `Over.ArrowLaws` / `Associativity` | Unit/associative laws, base continuity derived using zero sections. |
| `Over.Isomorphisms` | Inverse maps over common bases, total homeomorphisms, inverse bundle isomorphisms. |
| `Isomorphisms.inverseExists` | Reverse isomorphism existence from forward existence. |
| `Of.Sections` | Sections as dependent vectors giving continuous total maps. |
| `Sections.regular` / `zero` | Local-coordinate section continuity, zero sections. |

## Pullback and restriction

`Of.Pullback[Y, source, f]` constructs actual totals with fibers \(F(f(y))\).
Topology is induced by the natural embedding into \(Y\times E\); `pulled[regular]` constructs pullback bundles from continuous \(f\).
`mapContinuous` gives continuity to original totals; `In[c].trivialization` pulls back original coordinates.

`Universal.Cone` stores commuting maps to bases/totals.
`lift` transports vectors along fiber equalities to universal maps; `baseFormula`, `mapFormula`, `liftContinuous`, `unique` prove compatibility/continuity/uniqueness.
`Pullback.Of.rank` pulls ranks back; `Sections.pullback`, `formula` pull sections back.
`ArrowLaws.Pullback.Of.map` pulls bundle maps back.

`Of.PullbackIdentity.isomorphism` and `Of.PullbackComposition.Of.isomorphism` give actual identity/composite pullback isomorphisms.
Comparisons are fiber identities; universality proves continuity between induced topologies.
`Of.Restriction[U].restricted` restricts arbitrary subspaces via inclusion pullbacks.
`Restriction.homeomorphism` compares totals with original projection preimages in subspace topology.

## Constructions and examples

`Over.Trivial[X, n, baseSpace].bundle` is trivial bundles over arbitrary bases; `homeomorphism` compares totals with ordinary products.
`Over.TwoRanks[n, m].bundle` constructs bundles on discrete two-point bases from coproduct topologies.
Components have ranks \(n,m\); prove both trivialization continuities.

[Examples.ref](src/Bundles/Examples.ref) pulls real section \(s(x)=x\) along squares, computing \(s(x^2)=x^2\).
Checks identity/composite comparisons, empty totals on empty bases, rank-zero bundles, rank-zero/one components, complex lines.

[Build and check](../../USAGE.md) from the repository root:

```sh
ref-type/target/debug/cli libs/geometry/vector_bundles --memory-mib 8192 --cache-stats
ref-type/target/debug/cli libs --module vector_bundles --memory-mib 8192 --cache-stats
ref-type/target/debug/cli libs --memory-mib 8192 --cache-stats
```

Total induced topology/continuity universality exposed as `topological_constructions.Induced`.
Check targets/dependencies/examples and full workspace effects of shared topology changes using shared caches.

Final target/dependency standard check passed: 38 modules, 548 source steps, 1,380 dependencies reused.
Peak RSS roughly 1,033 MiB, one worker; zero recoveries/duplicates/reruns/lost steps/cache save failures.
Earlier dependency-closure checks also passed 11,963 source steps.

Full workspace including shared topology changes passed: 69 packages/6,976 modules.
Initial full run processed 73,864 steps; one shutdown checkpoint recovery recorded 4,739 unsaved steps, but rechecking all 6,976 committed caches accepted the entire scope.
Committed-source target/dependency standard recheck passed with 1,418 modules reused and zero source steps.
Workspace `--module vector_bundles` passed 38 modules/548 recheck steps with 411 reused; all final recoveries/duplicates/reruns/lost steps/cache save failures zero.
