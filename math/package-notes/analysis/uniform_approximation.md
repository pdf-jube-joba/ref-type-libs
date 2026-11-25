# `uniform_approximation` notes

[Package API](../../../libs/analysis/uniform_approximation/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Uniform real/complex approximation on compact Hausdorff spaces and Laurent approximation on circles.
Applies to finite matrix entries and finite-embedding complex-bundle endomorphisms.
Entry: `Approximation`; package: `uniform_approximation`.

### Real and complex functions

`On[X, space]` handles real functions; `ComplexOn[X, space]` complex functions.
`SubalgebraLaws` groups continuity, all constants, closure under sums/negation/products; complex versions add conjugation closure.
`Separates` asserts existence of elements separating distinct points.
`Error f g epsilon` gives strict errors at all points; `Approximates A f` gives subalgebra approximants for every positive error.
Complex errors use existing Euclidean modulus `complex.Complex.Absolute.abs`.

Construct \(p_0=0\), \(p_{n+1}=p_n+(x^2-p_n^2)/2\) in existing polynomial rings.
Prove \(0\leq p_n(x)\leq\lvert x\rvert\leq1\) and pointwise geometric convergence; compactness uniformizes.
Prove uniform closures closed under algebra/limits/modulus/max/min; two-point interpolation and two finite subcovers yield the real theorem.
Extract real/imaginary parts by conjugation and use the real theorem; component errors bound complex modulus.

### Circles and continuous coefficients

`Circle` uses existing `sphere_maps.Circle`, obtaining compact Hausdorffness from existing-sphere homeomorphisms.

Coefficient subalgebras are actual evaluation images of Laurent-ring elements.
Laurent induction proves continuity/conjugation closure; Urysohn functions separate base points, variables separate circle points.
Circle-only versions translate one-point coefficient functions to complex coefficients, proving evaluation agreement.
`Circle.Scalar.Translation` exposes this comparison; `Subalgebra`, `algebraLaws`, `separation` also apply to finite entries/bundles.

### Finite entries, bundles, and invertibility

`FiniteChoices` and `ComplexOn.FiniteComponents` select finitely many common-error approximations; `Matrices.On.density` assembles actual matrix families.
`FiniteComplex` reuses existing finite sums/enumerations.
`Matrices.actionError` turns entry errors \(\leq\delta\) into action errors \(\leq\delta\sum_j\lvert v_j\rvert\).
`compressedError` also bounds left-matrix amplification by finite sums.

`Bundles.Over[X, F, bundle].splittingExists` constructs actual bundle maps \(E,C\), \(CE=1\), from B03 embeddings/image comparisons.
Below write `Split[n, include, project, retraction]` as `Split` and set \(P=EC\).

`Matrices.invertibleOfDeterminantError` requires \(\lvert\det a-\det b\rvert<\lvert\det a\rvert\).
`Matrices.On.Margin.exists` constructs \(0<\eta\leq\lvert\det a(x)\rvert\) on compact bases; `invertibleError` derives inverses from uniform determinant error \(<\eta\).
Impose this on `Lift.matrix` for bundles, reusing L01 inverses/L03 continuity.

## Examples

[Examples.Circle](../../../libs/analysis/uniform_approximation/src/Approximation/Examples/Circle.ref) approximates \(\lvert\operatorname{Re}z\rvert\) using 2×2 and zero-size Laurent matrices.
[Examples.Coefficients](../../../libs/analysis/uniform_approximation/src/Approximation/Examples/Coefficients.ref) compares actual polynomials/evaluations for \(g(x)z^{-1}\).
[Examples.Bundle](../../../libs/analysis/uniform_approximation/src/Approximation/Examples/Bundle.ref) uniformly approximates trivial-circle-line endomorphisms on the unit ball.
[Examples.IdentityMatrix](../../../libs/analysis/uniform_approximation/src/Approximation/Examples/IdentityMatrix.ref) uses invertibility-error conditions on arbitrary identity dimensions.

## Historical validation

Historical upstream [PR #45](https://github.com/pdf-jube-joba/ref-type/pull/45):

| Input | Result |
| --- | --- |
| Package/dependencies `97e259ec` | 4,702 modules checked, 640 reused |
| Workspace `9004f57b` | 2,314 modules checked, 5,439 reused |

Both exited 0 with zero save failures, recoveries, duplicate/rerun checks, or lost steps; the workspace included shared-API consumers and examples.
Original reports: `work/k04-package-retry` and `work/k04-workspace`.
