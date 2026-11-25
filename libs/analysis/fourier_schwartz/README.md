# `fourier_schwartz`

Schwartz spaces, Fourier formulas/preservation, Gaussian transform, inversion via approximate identities.

The Fourier kernel is exp(-i x·xi), with inversion factor (2pi)^(-n). `Translation.translate a f` means f(x+a); dimension zero is included.

| Entry | Purpose |
| --- | --- |
| `ComplexCalculus` | Real-variable derivatives of complex functions, sums/products/composition/conjugation |
| `Phase.Global` / `Exponential` | \(e^{it}\) from local ODEs, complex exponentials, addition/conjugation/modulus |
| `Euclidean[n].Schwartz` / `seminorm` | Real Schwartz functions, weighted supremum seminorms |
| `Euclidean[n].Complex` | Complex Schwartz functions, modulus seminorms and complex homogeneity |
| `Euclidean[n].Operations` / `CoordinateMultiplication` / `Translation` | Schwartz preservation under addition/scaling/iterated derivatives/coordinate multiplication/translations |
| `Euclidean[n].Integrability` | L1 representatives of Schwartz functions and all weighted partials |
| `Euclidean[n].Integral` | Integral Fourier transforms of arbitrary complex L1 representatives, continuity/linearity |
| `Euclidean[n].Transform` / `Identities` | Fourier smoothness, derivative/coordinate/translation formulas |
| `Euclidean[n].Transform.Preservation.value` | Fourier transform as a Schwartz endomorphism |
| `Euclidean[n].Convolution.convolve` / `Complex.function` | Real/complex Schwartz convolution, differentiation/commutativity |
| `Euclidean[n].Convolution.Complex.Fourier` | \(\widehat{f*g}=\widehat f\,\widehat g\) |
| `Euclidean[n].Gaussian` | \(G_n(x)=e^{-\sum_jx_j^2/2}\), Schwartz property, positive integral, Fourier formula |
| `Euclidean[n].Gaussian.Density` | Normalized Gaussian density with integral one |
| `Euclidean[n].Gaussian.Approximation` | Pointwise convergence of normalized Gaussian approximate identities |
| `Euclidean[n].Inversion` | Inversion formula, Schwartz-valued inverses, both inverse identities |
| `Normalization` | Gaussian-integral \(\pi\), dimensionwise integrals, \((2\pi)^{-n}\) |
| `Examples[n]` | Checked examples for arbitrary dimensions/functions/frequencies |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/analysis/fourier_schwartz.md)
