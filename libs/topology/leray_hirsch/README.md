# Leray–Hirsch comparison

For a continuous projection \(\pi:E\to X\) and a pair \((X,A)\), the
package constructs the \(K\)-linear comparison
\[
\bigoplus_i H^{n-d_i}(X,A;K)\longrightarrow
  H^n(E,\pi^{-1}A;K),\qquad (a_i)_i\longmapsto
  \sum_i\pi^*a_i\smile u_i .
\]
The input classes \(u_i\) have degrees \(d_i\), and the index type is
\(\operatorname{Fin}(m)\).

| Entry | Purpose |
| --- | --- |
| `Projection.Charts.LocallyTrivial` | Open local product charts over the projection |
| `Projection.Charts.Cover.finite` | Finite chart subcover from a finite CW structure |
| `Projection.Charts.On.Paired.chains` | Pair homeomorphism on a local product chart |
| `Projection.Charts.Cover.Induction.whole` | Finite-union induction from local and gluing lemmas |
| `Projection.Lifts.Given.LiftsBasis` | Homogeneous basis hypothesis on each actual fiber |
| `Projection.Lifts.Fiber.Model.Given.isomorphism` | Fiber cocycle model built from a lifted basis |
| `Projection.Over.Component.linear` | Relative pullback followed by cup with a total-space class |
| `Projection.Over.Comparison.With.At.linear` | Finite direct-sum comparison in integer total degree |
| `Projection.Over.Comparison.With.At.Empty.isomorphism` | Comparison isomorphism on the empty base |
| `Projection.Pullback.Over.Degree.law` | Bidegree naturality for base change and inverse-image pairs |
| `Projection.Over.Change.Degree.law` | Bidegree naturality for unital ring homomorphisms |
| `Projection.Over.MayerVietoris.At.connectingLaw` | Naturality of the relative connecting map under projection |
| `Projection.Over.MayerVietoris.SignedCup.connectingLaw` | Compatibility of the relative connecting map with a comparison summand in integer degrees |
| `Projection.Over.MayerVietoris.FiniteConnecting.At.connectingLaw` | Connecting map on the finite sum of restricted components |
| `ProductPair.AlexanderWhitney.RelativeMap.CohomologyComparison.At.isomorphism` | Relative Alexander–Whitney cohomology isomorphism over the coefficient ring |
| `ProductPair.AlexanderWhitney.RelativeMap.ExternalFormula.Cochains.law` | Relative external cup as the pullback of tensor cochains along Alexander–Whitney |
| `ProductPair.AlexanderWhitney.BaseTensor.Free.isomorphism` | Free basis of the relative base chain module |
| `FreeTensorCochains.OneColumn.On.Cohomology.comparison` | Cohomology of an unsigned tensor column with free base module |
| `ChainTruncation.Layer.Sequence.Tensor.exact` | Split exact truncation layer after tensoring |
| `ChainTruncation.Layer.TensorColumn.Model.Coefficients.At.isomorphism` | Cohomology of the reindexed tensor layer with its differential sign accounted for |
| `ChainTruncation.Layer.TensorColumn.Model.Coefficients.FreeRow.Cohomology.isomorphism` | Evaluation of the reindexed layer cohomology on a free basis of its base chain module |
| `ChainTruncation.Layer.Sequence.Cohomology.Step.glue` | Five-lemma step for the finite comparison on a cutoff sequence |
| `ChainTruncation.Comparison.With.realizations` | Induction from an empty cutoff and the comparison on each concentrated layer |
| `ChainTruncation.Comparison.With.Stable.At.With.isomorphism` | Passage from the cutoff comparisons to the unrestricted tensor comparison |
| `ChainTruncation.Layer.Comparison.NativeDegree.matched` | Evaluation of an external cup summand on a free chain generator, with its degree and sign |
| `ChainTruncation.Layer.Stable.At.isomorphism` | Stabilization of tensor cohomology when the cutoff contains degree $n+1$ |
| `TensorCochainCup.Of.Fixed.Cohomology.linear` | Tensor cohomology multiplication by a fixed right cocycle |
| `TensorCochainCup.Of.Along.At.Closed.naturality` | Compatibility of tensor cohomology multiplication with base chain maps |
| `Projection.Over.MayerVietoris.Shifted.At` | Exact products of the shifted base terms |
| `Trivial.Over.Degree.law` | Agreement with relative external cup on a product bundle |

The [C11 plan](../../../math/c11-leray-hirsch.md) records the
mathematical proof and the remaining formalization of bijectivity.

Run the checker from the repository root.

```sh
python3 scripts/check.py run --scope changed --package leray_hirsch --json
```
