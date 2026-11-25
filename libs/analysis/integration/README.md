# Integration

Riemann integration on bounded Dedekind-real closed intervals and Lebesgue integration by \(L^1\) completion.
Real estimates/limits use `real.Analysis.Estimates` / `Sequence`.

| Module | Contents |
| --- | --- |
| [Real](src/Real.ref) | Real arithmetic, `Interval` with ordered endpoints |
| `Real.Division` | Dyadic tagged partitions, Riemann sums/laws |
| `Real.Division.Bounds` / `Mesh` / `Refinement` | Uniform estimates, mesh size, refinement errors |
| `Real.Division.Prefix` | Truncated interval lengths/sums, refinement/increment estimates |
| `Real.Riemann[interval].Def` / `Prop` | Boundedness, integral conditions/uniqueness, constants, \(L^1\) estimates |
| `Real.Riemann[interval].Uniform.Of` | Integrals/primitives of bounded uniformly continuous functions |
| `Real.Riemann[interval].Continuous.Of` | Continuous closed-interval integrability, fundamental theorem |
| `Real.Lebesgue[interval].Def` / `Prop` | \(L^1\) Cauchy quotients, integral construction, representative independence |
| `Vector[n, interval].Of` / `Comparison` | Finite-dimensional integrals/primitives, coordinate derivatives, norm estimates |

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
[Integral properties](src/Real/Riemann/Prop.ref) collects constant/interval laws.
