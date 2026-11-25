# Complex numbers

Construct \(\mathbb{C}=\mathbb{R}\times\mathbb{R}\) as pairs of Dedekind reals.
Real multiplication and reciprocals use signed operations from `dedekind_reals.DedekindReal.Arithmetic.Prop`.

| Module | Contents |
| --- | --- |
| `Complex` | `Real`, `Complex`, constructor `make`, real part `re`, imaginary part `im` |
| `Complex.Def` | `zero`, `one`, `i`, real embedding, arithmetic, real scaling, conjugation, squared modulus |
| `Complex.Multiplication` | Real/imaginary computations for associativity of complex multiplication |
| `Complex.Prop` | Extensionality, embedding injectivity/arithmetic preservation, arithmetic laws, conjugation, squared modulus, reciprocal/division laws |
| `Complex.Algebra` | Additive abelian group, commutative ring, field structures |
| `Complex.Absolute` | Modulus as square root of squared norm, nonnegativity, zero criterion, product/conjugation/triangle inequalities |

Use `real.Analysis.Algebra` for real identities and square properties.

`make a b` represents \(a+bi\).
Conjugation, squared modulus, and reciprocals are defined below.

\[
\overline{a+bi}=a-bi,\qquad
\operatorname{normSq}(a+bi)=a^2+b^2,\qquad
(a+bi)^{-1}=\frac{a-bi}{a^2+b^2}.
\]

The reciprocal of zero and division by zero are defined as zero.

[Examples](src/SpecificValues.ref) check arithmetic, conjugation, and field structure.
