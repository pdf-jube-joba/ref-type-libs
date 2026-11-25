# L² Fourier transform and multipliers

Construction details and records for [fourier_l2](../../../libs/analysis/fourier_l2/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Extend A06 [fourier_schwartz](../../../libs/analysis/fourier_schwartz/README.md) Lebesgue Fourier transforms to unitary isomorphisms on existing [lp_spaces](../../../libs/analysis/lp_spaces/README.md) `On.Complex.Space`.
Dimensions are arbitrary natural numbers, including zero.
Inner products are linear in the second variable.

Following A06, set Gaussian mass \(M_n=(\sqrt{2\pi})^n\) and normalize
\[
\mathcal F f=M_n^{-1}\widehat f,
\qquad
\mathcal F^{-1}f=M_n\,\widehat{\ }^{-1}f
\]
`Schwartz.coefficient` gives \(M_n^{-1}\); `Unitary.forward` and `backward` give the extended maps.

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

Rechecked all 22 fixed-source A07 modules from source; reused 970 dependencies.
A06/Lp/complex-Hilbert regressions and the standard full 11,729-target check exited 0.
Full standard check: 11,337 new, 392 reused, zero save failures/corrupt reads, one worker recovery.
Final existing package `compact_support_k` resumed from checkpoint 35685 after allocation failure; all targets accepted.
