# CW cofibrations and Puppe sequences (K02)

Entry: `puppe_sequences.Puppe`.
Disk/finite-CW homotopy extension, iterated pointed cofibers, reduced-suspension comparisons, contravariant pointed-homotopy Hom exactness.

## Public API

| API | Contents |
| --- | --- |
| `Cofibration.fromExtension` | Cylinder-gluing retractions from existing homotopy extension |
| `Disk.Boundary.cofibration` | All-dimensional disk-boundary cofibrations |
| `CW.Subcomplex.cofibration` | Finite-CW subcomplex cofibrations via boundary extension/skeleton induction |
| `Maps` | Pointed homotopies/quotients, pre/postcomposition |
| `ReducedCone`, `Cone`, `Suspension` | Pointed cones/mapping cones/reduced suspensions, continuous induced maps |
| `Cone.Exactness.exact` | Kernel/image equality in \([C_f,Z]\to[B,Z]\to[A,Z]\) |
| `Cone.Connecting`, `Cone.Morphisms.Of` | Connecting maps, pair-square induced maps/naturality |
| `Cone.Iteration.Inverse.equivalence` | \(C_{B\to C_f}\simeq\Sigma A\), actual projections/inverses/both pointed homotopies |
| `Cone.Iteration.Successor.homotopy` | Next connecting maps compared with time-reversed \(\Sigma f\) |
| `Cone.Iteration.Exactness.exact` | Exact \([\Sigma A,Z]\to[C_f,Z]\to[B,Z]\) |
| `Pair.equivalence` | Mapping-cone/quotient comparison equivalences for cofibrations |
| `CW.Subcomplex.Pointed.equivalence` | Quotient comparison for basepoint-containing finite CW subcomplexes |
| `Sequence.Of.At` | Iterated natural cofiber stages/suspension comparisons, `Hom.exact`, `Hom.connectingExact` |
| `Sequence.Natural` | Inductive stagewise commuting diagrams from pair maps |
| `Equivalence.Contravariant` | Inverse contravariant homotopy-class maps from equivalences |

`Sequence.Arrow` bundles pointed maps.
Supply two carriers and `Sequence.Details` to `Sequence.pack`; construct sequences via `Sequence.Of`.
Stage zero is the given map; stage one mapping-cone inclusion; stage-two codomains compare with original-domain suspension.
Repeat at every stage; `successorComparison` explicitly gives next-map time reversal.
Convention follows cone base time zero/apex time one.

`Pair.equivalence` accepts existing `algebraic_topology.Cofibration.IsCofibration`, returning equivalences with specified comparisons forward.
Construct inverses by homotopy extension rather than assuming them.

## Examples and checks

`Examples.intervalBoundary` and `Examples.planeBoundary` check one/two-dimensional disk-boundary inclusions.
`Examples.identityComparison` and `Examples.constantComparison` iterate two-point identity/constant comparisons; `identityOnClasses`, `constantOnClasses` check actual class actions.

[Build and check](../../USAGE.md) from the repository root:

```sh
ref-type/target/debug/cli libs/topology/puppe_sequences --module puppe_sequences.Puppe --memory-mib 10240 --cache-dir libs/refcache --cache-budget-mib 12288 --diagnostics compact
ref-type/target/debug/cli libs --memory-mib 10240 --cache-dir libs/refcache --cache-budget-mib 12288 --diagnostics compact
```

Added shared `topological_constructions.Quotient.Descent`, `Coproduct.ProductUniversal`, `Pushout.Of.Families`, `RelationQuotient.Families` APIs.
Product/quotient interchange uses compact Hausdorff intervals.
[Relative K03](../relative_k_theory/README.md) uses these sequences/finite-CW comparisons.

## Validation and saving

Recorded results in this section belong to the original combined repository.
See [validation records](../../USAGE.md#validation-records) for their scope and current rerun instructions.

Base: K07-integrated main `76e6084094f810eaf51e18663bb33d111dd409d7`.
Branch: `math/k02-cofibration-puppe`; [PR #47](https://github.com/pdf-jube-joba/ref-type/pull/47).
Public entries/dependencies/examples: 393 modules, accepted, exit 0, save failures 0.
Full 2026-10-26 workspace with shared `libs/refcache`: 8,149 modules accepted, exit 0, save failures 0 (roughly 3,037 seconds).
Checked remote: `5d90703b376cb27ad0273821eda2e28f5ba65a87`; source tree: `848d26bfebe5268fbcf58c954098857afd021b4a`.
Full report: `workspace-unbounded.json`; one recovery, `lost_steps` 4,322, reruns/duplicates zero; final worker reused all 8,149 saved modules and exited normally.
Successful completion resolved previous time-limit incompleteness.
Roadmap/K03/B08/C02/T02 links updated to public APIs.
B09 integrated in [PR #49](https://github.com/pdf-jube-joba/ref-type/pull/49).
[Relative K-groups](../relative_k_theory/README.md) exposes negative exactness/naturality using these foundations.
