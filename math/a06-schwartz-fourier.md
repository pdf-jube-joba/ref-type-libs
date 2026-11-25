# A06 Schwartz spaces and the Fourier transform

## Requirements

- Primary implementation: `fourier_schwartz`.
- Construct the Fourier kernel using complex exponentials, Schwartz seminorms, and the Fourier transform.
- Prove formulas for differentiation, coordinate multiplication, translation, and convolution, and preservation of Schwartz spaces.
- Prove Fourier inversion using the Gaussian transform and approximate identities; fix normalization constants.

## Dependencies

- [A05 Norms and completeness of Lp spaces](a05-lp-completeness.md)
- [G01 Smooth bump functions and partitions of unity](g01-smooth-partitions.md)

## ImplementationStatus

All required constructions and proofs are implemented in `libs/analysis/fourier_schwartz`.
Includes the complex exponential Fourier kernel, real and complex Schwartz seminorms, L1 integrability of all weighted partial derivatives, differentiation/coordinate multiplication/translation/convolution formulas, Schwartz preservation, the Gaussian Fourier formula, and inversion by Gaussian approximate identities.
Normalization is \((2\pi)^{-n}\), using a constant constructed from the Gaussian integral; both inverse identities for the Schwartz-valued inverse are proved.
