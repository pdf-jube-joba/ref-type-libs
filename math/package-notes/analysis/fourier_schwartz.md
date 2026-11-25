# `fourier_schwartz` notes

[Package API](../../../libs/analysis/fourier_schwartz/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Construct finite-dimensional real/complex Schwartz functions, Lebesgue Fourier transforms, Schwartz preservation, Gaussian transforms, and inversion via approximate identities.
Dimensions are arbitrary natural numbers, including zero.

Convention:
\[
K(x,\xi)=e^{-i\sum_jx_j\xi_j},\qquad
\widehat f(\xi)=\int_{\mathbb R^n}f(x)K(x,\xi)\,dx
\]
`Translation.translate a f` denotes \(x\mapsto f(x+a)\).

`Directions` is a finite coordinate list; `jet f d` iterates partials in that order.
Construct the seminorm
\[
p_{m,d}(f)=\sup_x(1+\sum_jx_j^2)^m|D^df(x)|
\]
using supremum completeness.
`Schwartz` assumes smoothness and these bounds for all \(m,d\).
Real/imaginary-sum estimates are auxiliary; complex seminorms themselves use complex modulus.

`Transform.Identities.spatialDerivative` proves \(\widehat{\partial_jf}(\xi)=i\xi_j\widehat f(\xi)\).
`coordinateReal` / `coordinateImaginary` give both components of \(\partial_{\xi_j}\widehat f=-i\widehat{x_jf}\).
`translation` proves \(\widehat{f(\mathord\cdot+a)}(\xi)=e^{i a\cdot\xi}\widehat f(\xi)\).
`Convolution.partialFunction` and `Convolution.Complex.partial` move convolution partials to the second factor.
`Convolution.Complex.commutative` swaps both factors.

### Gaussian and normalization

\[
M_n=\int G_n(x)\,dx,\quad c=M_1,\quad \pi=\frac{c^2}{2},\quad
M_n=c^n=(\sqrt{2\pi})^n
\]
Adopt the Gaussian-integral definition above.
`Mass.positive`, `Factorization.law`, `Normalization.dimension`, `squareRoot` prove positivity, product factorization, dimension and square-root formulas respectively.
No axioms assume numerical constants or Gaussian integral values.

\[
\widehat{G_n}(\xi)=M_nG_n(\xi),\qquad
H_\varepsilon(x)=\frac{G_n(x/\varepsilon)}{\varepsilon^nM_n},\qquad
\int H_\varepsilon=1
\]
These identities are provided by `Gaussian.Fourier.formula` and `Gaussian.Density`.
`Gaussian.Approximation.approximateIdentity` gives
\[
\frac1{M_n}\int G_n(y)f(x-2^{-k}y)\,dy\longrightarrow f(x)
\]

Main inversion theorem:
\[
f(x)=\frac1{(2\pi)^n}\int\widehat f(\xi)e^{i x\cdot\xi}\,d\xi
\]
`Inversion.inverse` defines the right-hand side; `theorem` proves equality.
`inverseSchwartz`, `inverseValue`, `leftInverse`, `rightInverse` give the same inverse as Schwartz functions.

### Proof structure

`Decay` constructs integrable common bounds from increasing dyadic-box indicator sums, deriving Schwartz integrability.
The mean value theorem verifies `lp_spaces.On.Differentiation.derivative` difference-quotient domination; continuity uses `On.Parametric.continuous`.
Prove integration by parts by differentiating translation invariance of Lebesgue integrals.
Fourier preservation follows from \((1-\Delta)^m\) formulas and L1 estimates.
Construct explicit Hermite polynomials for iterated Gaussian derivatives.
Convolution formulas and Gaussian-regularization interchange follow from existing Fubini.
Inversion identifies the Gaussian approximate-identity limit of regularized integrals with the dominated-convergence Fourier limit.

```ref
\import fourier_schwartz.Euclidean[n := n] \as E;
\import E.Complex[] \as S;
\import E.Transform[] \as Fourier;
\import E.Inversion[] \as Inversion;

\definition transformed[f: S.Function]: S.Function := Fourier.Preservation[].value f;
\definition recovered[f: S.Function][x: E.Point]:
  Inversion.inverse (transformed f) x = S.value f x := Inversion.theorem f x;
```
