# `euclidean_forms`

Local differential forms, wedge products/exterior derivatives, coordinate expressions, pullbacks.

APIs specialize `Euclidean[n].On[U]` on open Euclidean sets. Form smoothness can be tested on fixed arguments or basis coefficients.

| Entry | Purpose |
| --- | --- |
| `At[k].space` / `DegreeZero.isomorphism` | Vector spaces, degree-zero forms/smooth functions |
| `Above[k]` / `coefficientExt` | Vanishing above dimension, coefficient equality criteria |
| `Wedge` / `Associativity` / `GradedCommutativity` / `UnitLaws` | Shuffle wedges and laws |
| `Partial` / `ExteriorDerivative` / `Square` / `Leibniz` | \(d\omega=\sum_i dx^i\wedge\partial_i\omega\), \(d^2=0\), Leibniz |
| `FunctionDifferential.law` | Degree-zero exterior/total derivative agreement |
| `DeRham` / `DeRham.At` | Natural/integer complexes, closed/exact quotients |
| `DeRham.DegreeZero` | Isomorphism with \(df=0\) functions |
| `CoordinateBasis.At.Enumeration` / `Differential.formula` | Finite bases, coefficient reconstruction/exterior formulas |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
