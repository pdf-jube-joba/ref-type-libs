# `singular_cap` notes

[Package API](../../../../libs/topology/singular/cap/README.md) · [Checking](../../../../libs/USAGE.md)

## Construction

`singular_cap` provides integral singular caps and relative versions. `map beta` in `Integral[A, source].At[p, q]` maps \((p+q)\)-chains to \(p\)-chains, outputting front faces and evaluating `beta` on back faces. `onGenerator` gives generator values; `Adjunction.law` cup-evaluation adjunction.

Under this convention, `Integral.Diagonal.Boundary.Formula.law` expresses
\[
 (\partial c)\frown\beta=\partial(c\frown\beta)+(-1)^p c\frown\delta\beta
\]
The right-hand output degree is \(p\). `Integral.Natural` gives continuous projection formulas; `Integral.Pair.Natural` pair-map homology/cohomology formulas; `Integral.Excision` excision-isomorphism/forward-map cap compatibility; `Integral.Unit` degree-zero unit actions.

`Integral.Pair.At.Quotient` constructs absolute-cochain actions on relative chains; `RelativeCochain` relative-cochain/relative-chain actions into absolute chains. Boundary formulas: `Pair.Boundary.Formula`, `Pair.RelativeCochainBoundary.Formula`; relative cup adjunction: `Pair.At.Adjunction`. Closed actions descend via `Pair.CohomologyAction`, `Pair.RelativeCohomologyAction` and corresponding zero-degree modules.

`CochainPair` compares quotient/vanishing relative cochains, giving both relative cups, Leibniz, and descent for arbitrary commutative coefficients. `CochainPair.Comparison.Cohomology` maps relative to absolute classes; `RelativeEvaluation.With` gives arbitrary-integer-module Kronecker; `External` absolute external cup; `Triple` chain/cochain/cohomology operations preserving each triple subspace.

If \(A,B\subseteq X\) are open in their union, `Triple.Union.Cover.On.Cup` gives \(H^p(X,A)\times H^q(X,B)\to H^{p+q}(X,A\cup B)\). Under the same condition, `CapCohomology*.Transfer` gives \(H^q(X,A)\times H_{p+q}(X,A\cup B)\to H_p(X,B)\); `Transfer.onSmall` agrees with small-relative-chain actions. Positive/zero cases: `CapCohomology`, `CapCohomologyZero`, `CapCohomologyZeroTarget`, `CapCohomologyZeroZero`.

`ExternalIntegral.Cup` gives union-of-projection-preimages external cup; `ExternalIntegral.Cross.At.Relative` bilinear relative-chain cross products; `onClasses` agrees with ordinary representative cross products. `Cross.Boundary` gives positive/axis boundary formulas; each `Descent` in `Cross.Homology`'s `Positive`, `RightZero`, `LeftZero`, `ZeroZero` gives homology products. `Cross.Homology.All` and `Cross.Natural.On.All` unify the nonnegative degree cases. Total degree follows `singular_products.Cross.degree p q = q + p`; each `Descent.onClasses` gives cycle formulas. `Cross.Natural.On.ProjectionGeneral` proves chain projection formulas for pair-map products with explicit degree equalities; `Projection` specializes cochain degree to left-factor degree. `Positive`, `CochainZero`, `TargetZero`, `ZeroZero` in `ProjectionClasses` give class projection formulas with independent external/cap degrees and explicit input equalities.

`Cross.Natural` proves pair-map products preserve union subspaces and naturality of relative chain/homology products. `Integral.Pair.ConnectingZeroZero`, `ConnectingZeroPositive`, `ConnectingPositiveZero`, `ConnectingPositivePositive` give closed-cap/homology-connecting compatibility. `CochainConnecting.ZeroZeroClasses`, `PositiveZeroClasses`, `PositiveOutputZeroCochain`, `PositiveOutputPositiveCochain` give signed cohomology/homology-connecting compatibility in all nonnegative degrees, with \((-1)^p\) for positive output.
`ConnectingPositivePositive.On.Compatibility` handles both-positive degrees, completing all nonnegative closed-cap/connecting formulas. Subspace actions use degree transport and zero-extension homology isomorphisms.

## Examples

Point-unit, relative-cross-product, and connecting-map examples: [cap_models](../../../../libs/topology/examples/cap/README.md), including `RelativeCross` and `Connecting`.

## Historical validation

Historical work on branch `codex/c01-cap-products`, through the 2026-10-28 integration of upstream main `e0f1db4f` in merge `1c39f1af`.

After integration, the full `singular_cap` check accepted 3,017 newly checked modules and 173 reused modules, with zero cache save failures.
Regressions for `singular_cohomology`, `singular_products`, `singular_excision`, and `singular_subdivision` also exited 0.
A later fixed-snapshot `singular_cap` recheck accepted 3,685 reused modules with zero save failures.

The post-integration workspace run failed while saving `relative_k_theory.Relative.Pullback`, reporting `The serialize buffer is full`, 78 save failures, and `No space left on device`.
The preserved [report](../../../records/c01-workspace.json) has outcome `internal-error`; see the [log](../../../records/c01-workspace.log).
Full post-integration workspace success remains unconfirmed.
An earlier 8,287-module workspace pass preceded this integration and does not cover it.

[Earlier diagnostic log](../../../records/c01-paused.log).
