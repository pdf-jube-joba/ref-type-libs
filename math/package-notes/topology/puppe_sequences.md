# CW cofibrations and Puppe sequences (K02)

Construction details and records for [puppe_sequences](../../../libs/topology/puppe_sequences/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Entry: `puppe_sequences.Puppe`.
Disk/finite-CW homotopy extension, iterated pointed cofibers, reduced-suspension comparisons, contravariant pointed-homotopy Hom exactness.

## Public API

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

Added shared `topological_constructions.Quotient.Descent`, `Coproduct.ProductUniversal`, `Pushout.Of.Families`, `RelationQuotient.Families` APIs.
Product/quotient interchange uses compact Hausdorff intervals.
[Relative K03](../../../libs/topology/relative_k_theory/README.md) uses these sequences/finite-CW comparisons.

## Validation and saving

Recorded results in this section belong to the original combined repository.
See [validation records](../../../libs/USAGE.md#validation-records) for their scope and current rerun instructions.

Base: K07-integrated main `76e6084094f810eaf51e18663bb33d111dd409d7`.
Branch: `math/k02-cofibration-puppe`; [PR #47](https://github.com/pdf-jube-joba/ref-type/pull/47).
Public entries/dependencies/examples: 393 modules, accepted, exit 0, save failures 0.
Full 2026-10-26 workspace with shared `libs/refcache`: 8,149 modules accepted, exit 0, save failures 0 (roughly 3,037 seconds).
Checked remote: `5d90703b376cb27ad0273821eda2e28f5ba65a87`; source tree: `848d26bfebe5268fbcf58c954098857afd021b4a`.
Full report: `workspace-unbounded.json`; one recovery, `lost_steps` 4,322, reruns/duplicates zero; final worker reused all 8,149 saved modules and exited normally.
Successful completion resolved previous time-limit incompleteness.
Roadmap/K03/B08/C02/T02 links updated to public APIs.
B09 integrated in [PR #49](https://github.com/pdf-jube-joba/ref-type/pull/49).
[Relative K-groups](../../../libs/topology/relative_k_theory/README.md) exposes negative exactness/naturality using these foundations.
