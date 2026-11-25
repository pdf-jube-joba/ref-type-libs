# Product measures and iterated integrals

`product_integration` provides σ-finite products, Tonelli/Fubini, and convolution estimates.
Measure/real integration: `functional_analysis.Measure`; Euclidean measure: [euclidean_measure](../euclidean_measure/README.md); complex/finite-dimensional integration: [measure_convergence](../measure_convergence/README.md).

`Finiteness[A, mu].Exhaustion` expresses countable covers by finite-measure measurable sets.
Split into disjoint increments; `Product[A, B, mu, nu, left, right].measure` sums products of finite restricted measures countably.
`ProductSigma.sigma` is the rectangle-generated σ-algebra; slices are measurable both ways.
`Product.sigmaFinite` proves the product itself σ-finite.
`Product.Rectangle.formula` gives extended double-series formulas for measurable rectangles; `FiniteRectangle.theorem` gives product formulas when both measures are finite.
`Symmetry.map` expresses measure-preserving factor swaps.

```ref
\import product_integration.Integration[
  A := A, B := B, mu := mu, nu := nu, left := left, right := right] \as F;
\import product_integration.Product[
  A := A, B := B, mu := mu, nu := nu, left := left, right := right] \as P;
\import product_integration.ProductSigma[
  A := A, B := B, left := mu.sigma, right := nu.sigma] \as S;
\import functional_analysis.Measure[A := S.Point].Integral[mu := P.measure] \as I;

\definition example: \forall (f: I.Representatives) -> \exists F.AEFubini[f] := F.fubini;
```

`Integration.tonelli` identifies product lower integrals of nonnegative measurable real functions with iterated slice lower integrals.
Includes infinite inner integrals; `ExtendedIntegral.lowerIntegral` represents outer extended-nonnegative integration.
`Integration.fubini` proves `AEFubini` exists for absolutely integrable real functions.
This structure includes measurable exceptions, integrable slice representatives agreeing off them, outer integrable slice-integral representatives, and interchange equalities.
`Complex.fubini` and `Vector[n].fubini` extend to real/imaginary and finite components, returning common null exceptions.
Includes zero-dimensional vectors.

`Euclidean[n].exhaustion` covers Lebesgue spaces by finite boxes.
`EuclideanProduct[m, n].join` concatenates coordinate lists; `split` is its inverse.
`Volumes.theorem` identifies box volumes; `Comparison.theorem` proves concatenated products agree with higher-dimensional Lebesgue measure on all Borel sets.
`Comparison.domination` bounds transported product measure by Euclidean outer measure on arbitrary product-measurable sets.
Equality is on Borel sets; no assertion completes the product σ-algebra.

`Convolution[A, mu, exhaustion].For[translations, f, g]` handles families of measure-preserving translations and two real integrable functions.
`kernel(x, y)` corresponds to \(f(x-y)g(y)\); `exists` derives a.e. integrable slices and outer integrable representatives from joint measurability, together with
\[
\int f*g=(\int f)(\int g),\qquad \|f*g\|_1\leq\|f\|_1\|g\|_1
\]
Joint measurability is an explicit sufficient product-σ-algebra condition.
`Support.theorem` proves if \(f,g\) vanish off \(S,T\), convolution vanishes outside common null exceptions and \(S+T\).
`Euclidean[n].translation` gives measure-preserving \(x\mapsto x-a\); `Euclidean[n].Convolution` is the Euclidean API.

Auxiliary APIs: π–λ for generated σ-algebras, finite-measure uniqueness, real-integral transport by measure-preserving maps, lower integrals of countable measure sums, suprema/nonnegative-series interchange.
`Examples[n]` has checked zero Fubini, zero/arbitrary-integrable convolution, and box-comparison examples.

Run these standard checks from the repository root:

```sh
target/release/cli libs/analysis/product_integration --module product_integration --diagnostics compact --no-progress --memory-mib 6144
cargo build -p cli --release --locked && python3 scripts/check_all.py
```
