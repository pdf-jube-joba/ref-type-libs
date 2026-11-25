# Grothendieck rings of bundles (K01)

Construct commutative \(K^0\) from complex bundles on compact Hausdorff spaces.
Reuses [B03 classes/complements](../../geometry/bundle_complements/README.md), [B02 operations](../../geometry/bundle_operations/README.md), existing [`algebra.GroupCompletion`](../../algebra/basic/README.md).

## Public API

`KTheory.On[X, baseSpace, compact, hausdorff]` handles compact-Hausdorff complex bundles.
`Bundle.value` and `Compare.criterion` compare general bundles with B03 projection classes.
`AdditiveMonoid`, `MultiplicativeMonoid`, `Semiring` derive operation laws from actual B02 isomorphisms.
`K0` uses existing semiring completion; `Stability.ForBundles.criterion` tests equality by adding common trivial bundles.
`Stability.differenceCriterion` reduces virtual-difference equality to common trivial stabilization of cross sums.
`Pullback.K0.map`, `IdentityPullback.onK0`, `Pullback.Composition.onK0` give contravariant functors.
`Pullback.Ranks.naturality` proves rank/pullback compatibility.
`Pullback.Ranks.Reduced` pulls reduced groups back along pointed maps.
`Ranks.rank` is locally constant integer rank; `Ranks.Reduced[point].group` its basepoint kernel.
`VariableRanks` constructs arbitrary natural-rank bundles over discrete bases.
`FiniteDiscrete.Classification` classifies by rank; `FiniteDiscrete.Computation` gives inverse integer-function maps.
`FiniteDiscrete.RingComputation.isomorphism` and `Point.Ring.isomorphism` identify integer-function rings/integer rings respectively.
`Examples` checks positive/negative ranks over empty/point/two-point spaces.

For example, use point-integer virtual bundles as follows.

```ref
\import topological_k_theory.KTheory[].Point[] \as Point;
\import std.Arithmetic[].Int[] \as I;
\definition minusOne: Point.Carrier := Point.backward (I.Neg.specification I.One.specification);
\definition rank: Point.forward minusOne = I.Neg.specification I.One.specification := Point.rightInverse (I.Neg.specification I.One.specification);
```

Checked consumers of the same public API: `KTheory.Examples`.

## Validation and resuming

Base: B04-integrated main `4f411dda`; work: `math/k01-grothendieck-k` / [PR #44](https://github.com/pdf-jube-joba/ref-type/pull/44).
Full-requirement `d48cc565` package/dependencies saved/exit 0 via `work/k01-package`: 4,236 checked, 4,345 reused, 53,089 steps, zero recoveries/duplicates/reruns/lost steps/save failures.
Target/examples also passed `work/k01-complete` on `bac1d6e9`: 841 modules, saved/exit 0.
Package command: `target/debug/cli libs/topology/k_theory --source-snapshot work/k01-package.source.json --memory-mib 8192 --cache-budget-mib 12288 --time-limit-seconds 1800 --report-json work/k01-package.json`.
Later changes are completion documentation only; no unverified math changes.
Full `764af78a` workspace via `work/k01-workspace`: 7,644 reused, saved/exit 0; zero recoveries/duplicates/reruns/lost steps/save failures.
Workspace command: `target/debug/cli libs --source-snapshot work/k01-workspace.source.json --memory-mib 10240 --cache-budget-mib 12288 --time-limit-seconds 7200 --report-json work/k01-workspace.json`.
Post-validation changes only this record; no unverified math/remaining implementation.
Next inspect final PR CI/diff, merge normally, confirm main tree equals verified branch.
