# Differential forms on Euclidean spaces

`Euclidean[n := n].On[U := U]` handles smooth alternating forms on open \(U\subseteq\mathbb R^n\).
`Form(k)` smoothness uses fixed-argument evaluation; `CoefficientSmooth.family` tests basis coefficients.

| API | Contents |
| --- | --- |
| `At[k].space` / `DegreeZero.isomorphism` | Vector spaces, degree-zero forms/smooth functions |
| `Above[k]` / `coefficientExt` | Vanishing above dimension, coefficient equality criteria |
| `Wedge` / `Associativity` / `GradedCommutativity` / `UnitLaws` | Shuffle wedges and laws |
| `Partial` / `ExteriorDerivative` / `Square` / `Leibniz` | \(d\omega=\sum_i dx^i\wedge\partial_i\omega\), \(d^2=0\), Leibniz |
| `FunctionDifferential.law` | Degree-zero exterior/total derivative agreement |
| `DeRham` / `DeRham.At` | Natural/integer complexes, closed/exact quotients |
| `DeRham.DegreeZero` | Isomorphism with \(df=0\) functions |
| `CoordinateBasis.At.Enumeration` / `Differential.formula` | Finite bases, coefficient reconstruction/exterior formulas |

`Euclidean.Pullback[m, U, V, f]` gives Jacobian pullbacks; `Identity`, `After` identity/composition laws.
`Pullback.Product`, `DegreeZero` prove wedge/degree-zero exterior compatibility.
`Evaluation` handles varying smooth evaluation; `Gluing` open-cover gluing.
`Restriction` has inclusion restrictions commuting with partials/products/exterior derivatives.
`Regrade[k,l].cast` gives set-valued transport; `RegradeIdentity`, `composition` its laws; `bridge` agrees with list transport.
