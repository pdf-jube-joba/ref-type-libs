# Convergence of measure integrals

`measure_convergence.On[A, mu]` provides convergence theorems based on `functional_analysis.Measure` measures and simple integrals.
Real integrals are constructed for measurable functions with finite absolute lower integrals.

```ref
\import measure_convergence.On[A := A, mu := mu] \as Integration;
\import functional_analysis.Measure[A := A].Integral[mu := mu] \as RealIntegral;
\import RealIntegral.Linear[] \as Linear;
\import real.Analysis[] \as Real;

\definition addExample: \forall (f, g: RealIntegral.Representatives) ->
  RealIntegral.integral (Linear.addRepresentative f g) =
    Real.add (RealIntegral.integral f) (RealIntegral.integral g) := Integration.integralAdd;
```

`monotone` proves lower-integral monotone convergence for pointwise suprema of increasing measurable real sequences.
`FatouFor[f].inequality` bounds suprema of tail-infimum lower integrals by lower limits of integrals for nonnegative measurable sequences.
When finite pointwise lower limits exist, `finiteLiminf` and `finiteInequality` address their lower integrals.
`NonnegativeAdd[p, q].lowerIntegralAdd` proves nonnegative measurable lower-integral additivity.

`Dominated[d]` derives limit integrability and integral convergence for pointwise-convergent integrable sequences dominated in modulus by one integrable function.
`AEDominated[d]` handles convergence/domination off measurable null sets, constructing integrable a.e.-equal limit representatives.
If the original limit is measurable, `limitIntegrable` makes it integrable too.
Without measurability, representatives are needed since subsets of null sets may be nonmeasurable for incomplete measures.

`IntegralClasses` and `integral` represent a.e. classes and their integrals.
`addClasses`, `scaleClass`, `integralClassAdd`, `integralClassScalar` provide quotient operations/integral linearity.
For representatives use `integralAdd`, `integralScalar`, `integralNeg`, `integralMono`, `integralAbsBound`.

`Series[terms].Exchange` interchanges integrals/series when integrable partial sums converge pointwise under common integrable domination.
`Series[terms].AEExchange` gives integrable limit representatives/interchange when conditions hold off measurable null sets.
Both prove integrals of partial sums equal partial sums of integrals.

`Complex` integrates real/imaginary components; `Vector[n]` integrates finitely many real coordinates.
Provides addition/scaling/a.e. invariance, componentwise dominated convergence/series interchange, and complex scaling for complex integrals.
`Complex.integralNormBound` bounds complex-integral modulus by summed integrals of absolute real/imaginary parts; `Vector[n].integralL1Bound` bounds coordinate ℓ¹ norms by summed coordinate absolute integrals.
These are component bounds; no claim replaces the right side by the integral of the vector norm.

`Indicator[p]` gives nonnegative constants on measurable sets, zero outside, and lower integrals equal to coefficient times measure.
`On.Examples` includes indicators, zero integrals, quotient addition, zero-sequence dominated convergence, and series examples.
