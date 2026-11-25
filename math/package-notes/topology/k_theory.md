# `topological_k_theory` notes

[Package API](../../../libs/topology/k_theory/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Construct commutative \(K^0\) from complex bundles on compact Hausdorff spaces.
Reuses [B03 classes/complements](../../../libs/geometry/bundle_complements/README.md), [B02 operations](../../../libs/geometry/bundle_operations/README.md), existing [`algebra.GroupCompletion`](../../../libs/algebra/basic/README.md).

### Conventions

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

## Examples

`Examples` checks positive/negative ranks over empty/point/two-point spaces.

For example, use point-integer virtual bundles as follows.

```ref
\import topological_k_theory.KTheory[].Point[] \as Point;
\import std.Arithmetic[].Int[] \as I;
\definition minusOne: Point.Carrier := Point.backward (I.Neg.specification I.One.specification);
\definition rank: Point.forward minusOne = I.Neg.specification I.One.specification := Point.rightInverse (I.Neg.specification I.One.specification);
```

Checked consumers of the same public API: `KTheory.Examples`.

## Historical validation

Historical upstream [PR #44](https://github.com/pdf-jube-joba/ref-type/pull/44):

| Input | Result |
| --- | --- |
| Package/dependencies `d48cc565` | 4,236 modules checked, 4,345 reused |
| Targets/examples `bac1d6e9` | 841 modules accepted |
| Workspace `764af78a` | 7,644 modules reused |

All exited 0; package/workspace runs reported zero save failures, recoveries, duplicate/rerun checks, or lost steps.
Original reports used `work/k01-{package,complete,workspace}`.
