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
| `Projection.Charts.Cover.Induction.whole` | Finite-union induction from local and gluing lemmas |
| `Projection.Lifts.Given.LiftsBasis` | Homogeneous basis hypothesis on each actual fiber |
| `Projection.Lifts.Fiber.Model.Given.isomorphism` | Fiber cocycle model built from a lifted basis |
| `Projection.Over.Component.linear` | Relative pullback followed by cup with a total-space class |
| `Projection.Over.Comparison.With.At.linear` | Finite direct-sum comparison in integer total degree |
| `Projection.Pullback.Over.Degree.law` | Bidegree naturality for base change and inverse-image pairs |
| `Projection.Over.Change.Degree.law` | Bidegree naturality for unital ring homomorphisms |
| `Projection.Over.MayerVietoris.At.connectingLaw` | Naturality of the relative connecting map under projection |
| `Projection.Over.MayerVietoris.Shifted.At` | Exact products of the shifted base terms |
| `Trivial.Over.Degree.law` | Agreement with relative external cup on a product bundle |

The [C11 plan](../../../math/c11-leray-hirsch.md) records the
mathematical proof and the remaining formalization of bijectivity.

Run the checker from the repository root.

```sh
python3 scripts/check.py run --scope changed --package leray_hirsch --json
```
