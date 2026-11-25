# L² Fourier transform and multipliers

Extend A06 [fourier_schwartz](../fourier_schwartz/README.md) Lebesgue Fourier transforms to unitary isomorphisms on existing [lp_spaces](../lp_spaces/README.md) `On.Complex.Space`.
Dimensions are arbitrary natural numbers, including zero.
Inner products are linear in the second variable.

Following A06, set Gaussian mass \(M_n=(\sqrt{2\pi})^n\) and normalize
\[
\mathcal F f=M_n^{-1}\widehat f,
\qquad
\mathcal F^{-1}f=M_n\,\widehat{\ }^{-1}f
\]
`Schwartz.coefficient` gives \(M_n^{-1}\); `Unitary.forward` and `backward` give the extended maps.

| API | Contents |
| --- | --- |
| `Euclidean[n].Embedding` | Linear maps from Schwartz functions to existing complex L² quotients |
| `Parseval[f, g].law` | Unnormalized Parseval: \(\langle\widehat f,\widehat g\rangle=M_n^2\langle f,g\rangle\) |
| `Schwartz.parseval` / `norm` | Normalized inner-product/norm preservation |
| `CompactEmbedding[f]` / `Density.dense` | Compact-support smooth functions are Schwartz and dense in complex L² |
| `Extension[map, preserves]` | Approximation-independent extension of dense isometries to complete spaces |
| `Unitary.forward` / `backward` | Inverse complex-linear maps on existing complex L² |
| `Unitary.operator` / `inverseOperator` | Bounded operators with bound one |
| `Unitary.norm` / `parseval` / `adjoint` | Norm/inner-product preservation, \(\mathcal F^*=\mathcal F^{-1}\) |
| `Multiplication.Symbol` / `By[symbol]` | L² multiplication by bounded measurable complex functions |
| `Multiplier[symbol].value` / `bound` | \(T_a=\mathcal F^{-1}a\mathcal F\)、\(\|T_af\|_2\le C\|f\|_2\) |
| `Multiplier[symbol].adjoint` | \(T_a^*=T_{\overline a}\) |
| `Conjugation.value` / `fourier` | Quotient conjugation, \(\mathcal F\overline f=\overline{\mathcal F^{-1}f}\) |
| `Weights.Weight` / `Weighted[weight]` | Weighted Fourier spaces for \(w\ge1\) with bounded measurable reciprocals |
| `Weights.Integer[m]` / `Integer[m].ofSchwartz` | Weighted norms for \(w_m(\xi)=(1+|\xi|^2)^m\) |
| `Integer[m].norm` | \(\|w_m\mathcal Ff\|_2=\|(1-\Delta)^mf\|_2\) |
| `Derivatives.Comparison[m].derivative` | \(\|D^df\|_2\le\|w_m\mathcal Ff\|_2\) for all iterated partials with \(|d|\le2m\) |
| `Expansion.comparison` | Reverse estimates by finite sums of integer-derivative norms |
| `Examples[n]` | Checked examples for arbitrary dimensions, L² classes, Schwartz functions, and symbols |

`Weighted.Vector` is the existing L² element corresponding to \(w\mathcal Ff\).
L² gives norm, inner product, and completeness; `physical` embeds into the original function space as \(\mathcal F^{-1}(w^{-1}u)\).
`injective` proves embedding injectivity; `controlsPhysical` proves \(\|f\|_2\le\|f\|_w\).
`Input` and `ofFunction` send arbitrary L² representatives with proofs of weighted L² membership into this space.
`inputFrequency` and `inputPhysical` confirm the correspondence.

`Expansion.derivativeSum` gives
\[
B_0(f)=\|f\|_2,\qquad
B_{m+1}(f)=B_m(f)+\sum_jB_m(\partial_j^2f)
\]
below.
Thus \(B_m\) is a finite sum of actual partial-derivative L² norms through order \(2m\), giving
\[
\|D^df\|_2\le\|w_m\mathcal Ff\|_2\le B_m(f)
\quad (|d|\le2m)
\]
the stated estimates.

Parseval constructs L² representatives from Schwartz L¹ membership/boundedness, using Fubini and A06 inversion.
Extensions use dyadic-error Schwartz approximations; isometry proves Fourier images Cauchy.
Completeness gives limits common to all approximations, uniquely defining the map.
Derivative estimates bound squared symbols by \((1+|\xi|^2)^{|d|}\), then use actual L² norm monotonicity.
No new mathematical axioms.

[Build and check](../../USAGE.md) from the repository root:

```sh
ref-type/target/release/cli libs/analysis/fourier_l2 --module fourier_l2 --memory-mib 8192 --diagnostics compact --no-progress --cache-stats
```

Rechecked all 22 fixed-source A07 modules from source; reused 970 dependencies.
A06/Lp/complex-Hilbert regressions and the standard full 11,729-target check exited 0.
Full standard check: 11,337 new, 392 reused, zero save failures/corrupt reads, one worker recovery.
Final existing package `compact_support_k` resumed from checkpoint 35685 after allocation failure; all targets accepted.
