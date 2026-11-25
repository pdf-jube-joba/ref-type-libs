# `characteristic_series`

Rational symmetric polynomials, Newton identities, truncated series, finite Chern-character/Todd/L/A-hat polynomials and coefficients.

`Series.cut n` retains degrees `0` through `n-1`. Chern roots have cohomological degree two; universal formulas are available through degree eight.

| Entry | Purpose |
| --- | --- |
| `Rational` | Commutative ring from the existing rational quotient, positive-integer and nonzero-rational reciprocals |
| `Polynomials[n]` | Rational polynomials in \(n\) variables, permutation-invariant subtype, elementary symmetric functions, evaluation, sums/products/negation/constants |
| `Symmetric[R, ring]` | Elementary symmetric functions of root lists, permutation invariance, coefficient-change naturality |
| `Symmetric.Newton.PowerSums` | Ordinary power sums and Newton identities for arbitrary root counts/degrees |
| `Series[R, ring]` | Finite coefficient-list truncation, sums/products/scaling/negation/powers, unit-series inverses, composition into zero-constant series |
| `Series.Finite` | Agreement with existing `algebra.Polynomial.Over.Finite` coefficient and truncation operations |
| `FormalSeries` | Rational-series inverses with arbitrary nonzero constant term, product laws, truncation compatibility |
| `Exponential` | Formal exponentials from reciprocal factorials, truncation compatibility |
| `Characteristic` | Chern/Todd/L/A-hat generating series, precision compatibility, coefficient tables through degree eight |
| `Genus[R, ring, coefficient]` | Finite polynomials of rootwise factors, multiplicative sequences, additive Chern-character sequences, permutation invariance, finite coefficients/truncation |
| `Genus.Precision` | Precision compatibility for both generating series and multiplicative sequences |
| `Genus.DegreeEight` | Universal formulas through cohomological degree eight in elementary symmetric functions |
| `Examples` | Symmetric polynomials, empty roots, two-line Todd polynomials, geometric-series inverses, precision-change examples |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/characteristic_series.md)
