# Cap products on singular chains

`singular_cap` provides integral singular caps and relative versions. `map beta` in `Integral[A, source].At[p, q]` maps \((p+q)\)-chains to \(p\)-chains, outputting front faces and evaluating `beta` on back faces. `onGenerator` gives generator values; `Adjunction.law` cup-evaluation adjunction.

Under this convention, `Integral.Diagonal.Boundary.Formula.law` expresses
\[
 (\partial c)\frown\beta=\partial(c\frown\beta)+(-1)^p c\frown\delta\beta
\]
The right-hand output degree is \(p\). `Integral.Natural` gives continuous projection formulas; `Integral.Pair.Natural` pair-map homology/cohomology formulas; `Integral.Excision` excision-isomorphism/forward-map cap compatibility; `Integral.Unit` degree-zero unit actions.

`Integral.Pair.At.Quotient` constructs absolute-cochain actions on relative chains; `RelativeCochain` relative-cochain/relative-chain actions into absolute chains. Boundary formulas: `Pair.Boundary.Formula`, `Pair.RelativeCochainBoundary.Formula`; relative cup adjunction: `Pair.At.Adjunction`. Closed actions descend via `Pair.CohomologyAction`, `Pair.RelativeCohomologyAction` and corresponding zero-degree modules.

`CochainPair` compares quotient/vanishing relative cochains, giving both relative cups, Leibniz, and descent for arbitrary commutative coefficients. `CochainPair.Comparison.Cohomology` maps relative to absolute classes; `RelativeEvaluation.With` gives arbitrary-integer-module Kronecker; `External` absolute external cup; `Triple` chain/cochain/cohomology operations preserving each triple subspace.

Point-unit examples: [examples/cap](../../examples/cap). Focused standard checks can run as follows.

```sh
target/debug/cli libs/topology/singular/cap --module singular_cap.Integral.Pair.At.Adjunction --cache-stats --diagnostics compact
```

If \(A,B\subseteq X\) are open in their union, `Triple.Union.Cover.On.Cup` gives \(H^p(X,A)\times H^q(X,B)\to H^{p+q}(X,A\cup B)\). Under the same condition, `CapCohomology*.Transfer` gives \(H^q(X,A)\times H_{p+q}(X,A\cup B)\to H_p(X,B)\); `Transfer.onSmall` agrees with small-relative-chain actions. Positive/zero cases: `CapCohomology`, `CapCohomologyZero`, `CapCohomologyZeroTarget`, `CapCohomologyZeroZero`.

`ExternalIntegral.Cup` gives union-of-projection-preimages external cup; `ExternalIntegral.Cross.At.Relative` bilinear relative-chain cross products; `onClasses` agrees with ordinary representative cross products. `Cross.Boundary` gives positive/axis boundary formulas; each `Descent` in `Cross.Homology`'s `Positive`, `RightZero`, `LeftZero`, `ZeroZero` gives homology products. Total degree follows `singular_products.Cross.degree p q = q + p`; each `Descent.onClasses` gives cycle formulas. `Cross.Natural.On.ProjectionGeneral` proves chain projection formulas for pair-map products with explicit degree equalities; `Projection` specializes cochain degree to left-factor degree. `Positive`, `CochainZero`, `TargetZero`, `ZeroZero` in `ProjectionClasses` give class projection formulas with independent external/cap degrees and explicit input equalities.

`Cross.Natural` proves pair-map products preserve union subspaces and naturality of relative chain/homology products. `Integral.Pair.ConnectingZeroZero`, `ConnectingZeroPositive`, `ConnectingPositiveZero`, `ConnectingPositivePositive` give closed-cap/homology-connecting compatibility. `CochainConnecting.ZeroZeroClasses`, `PositiveZeroClasses`, `PositiveOutputZeroCochain`, `PositiveOutputPositiveCochain` give signed cohomology/homology-connecting compatibility in all nonnegative degrees, with \((-1)^p\) for positive output.
`ConnectingPositivePositive.On.Compatibility` handles both-positive degrees, completing all nonnegative closed-cap/connecting formulas. Subspace actions use degree transport and zero-extension homology isomorphisms.
