# Integration

Construction details and records for [integration](../../../libs/analysis/integration/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Riemann integration on bounded Dedekind-real closed intervals and Lebesgue integration by \(L^1\) completion.
Real estimates/limits use `real.Analysis.Estimates` / `Sequence`.

## Riemann integration

For \(a\le b\), \(x_{n,k}=a+(b-a)k/2^n\), and arbitrary tags \(\xi_k\in[x_{n,k},x_{n,k+1}]\), define
\[
S_n(f;\xi)=\sum_{k=0}^{2^n-1}(x_{n,k+1}-x_{n,k})f(\xi_k)
\]
`HasIntegral[f, I]` requires boundedness and uniform convergence of these sums to I over all tags.
`Function` bundles functions, integral values, and proofs.
Constant c integrates to \((b-a)c\), including zero-length intervals.

`Continuous.Of[f].integral` proves continuous closed-interval Riemann sums Cauchy, constructing their limit.
Interval compactness gives boundedness/uniform continuity and convergence for arbitrary tags.
`primitive` limits sums truncated at arbitrary endpoints, zero at the left and integral at the right.
`fundamentalTheorem` proves \(F'(x)=f(x)\) for \(a<x<b\).
Uses uniform refinement and small-interval slope increment estimates.
`Uniform.Comparison.primitiveBound` bounds primitive differences by uniform input differences.
Proves the same maximum-norm estimates for vectors, including dimension zero.
`Continuous.Of.Uniqueness.agrees` uses the mean value theorem to identify continuous functions with the same derivative as initial values plus primitives.

## Lebesgue integration

Bound tagged sums of \(|f-g|\) on the same partitions; define `SmallL1`, Cauchy conditions, and equivalence by differences tending to zero.
`Representation` consists of \(L^1\) Cauchy sequences of Riemann-integrable functions; `Function` is their quotient.
Construct integrals by unique choice of limits of representative Riemann integrals; `IntegralLaw` requires this limit for every representative.

`ofRiemann` embeds Riemann functions as constant-sequence classes; `riemannAgreement` proves equal integrals.
`riemannLebesgueAgreement` directly quantifies functions/integral values in the agreement theorem.
[Integral properties](../../../libs/analysis/integration/src/Real/Riemann/Prop.ref) collects constant/interval laws.
