# Stone–Weierstrass and Laurent approximation

Uniform real/complex approximation on compact Hausdorff spaces and Laurent approximation on circles.
Applies to finite matrix entries and finite-embedding complex-bundle endomorphisms.
Entry: `Approximation`; package: `uniform_approximation`.

## Real and complex functions

`On[X, space]` handles real functions; `ComplexOn[X, space]` complex functions.
`SubalgebraLaws` groups continuity, all constants, closure under sums/negation/products; complex versions add conjugation closure.
`Separates` asserts existence of elements separating distinct points.
`Error f g epsilon` gives strict errors at all points; `Approximates A f` gives subalgebra approximants for every positive error.
Complex errors use existing Euclidean modulus `complex.Complex.Absolute.abs`.

| API | Contents |
| --- | --- |
| `Polynomials` | Existing real polynomial rings/evaluation/induction, iterative polynomials `absolutePolynomial` |
| `Absolute.unitBounded` | Uniform polynomial approximation of modulus on \(\lvert x\rvert\leq1\) |
| `On.Dini.uniform` | Uniformization of pointwise approximation with decreasing continuous nonnegative errors via finite subcovers |
| `On.Compact.RealAlgebra.StoneWeierstrass.approximation` | Uniform approximation of arbitrary real continuous functions by point-separating subalgebras |
| `ComplexOn.Algebra.Compact.StoneWeierstrass.approximation` | Uniform approximation by conjugation-closed point-separating complex subalgebras |
| `ComplexOn.Naturality` | Pullback compatibility of errors/approximations/constants/sums/products/conjugation |

Construct \(p_0=0\), \(p_{n+1}=p_n+(x^2-p_n^2)/2\) in existing polynomial rings.
Prove \(0\leq p_n(x)\leq\lvert x\rvert\leq1\) and pointwise geometric convergence; compactness uniformizes.
Prove uniform closures closed under algebra/limits/modulus/max/min; two-point interpolation and two finite subcovers yield the real theorem.
Extract real/imaginary parts by conjugation and use the real theorem; component errors bound complex modulus.

## Circles and continuous coefficients

`Circle` uses existing `sphere_maps.Circle`, obtaining compact Hausdorffness from existing-sphere homeomorphisms.

| API | Contents |
| --- | --- |
| `Circle.Scalar.Polynomial` / `value` | Complex-coefficient `algebra.LaurentPolynomial.Over` elements and circle evaluations |
| `Circle.Scalar.Approximate.exists` | Laurent approximation of arbitrary complex continuous circle functions |
| `Circle.Scalar.Matrices[n, m].exists` | Simultaneous equal-error Laurent entry approximations of finite matrices, including zero size |
| `ComplexOn.FunctionRing` | Continuous complex function rings, conjugation, evaluation homomorphisms |
| `Circle.Coefficients[X, space, baseCompact, baseHausdorff]` | Existing Laurent ring `Polynomial` over continuous coefficients, `value` on \(X\times S^1\) |
| `Circle.Coefficients.valueContinuous` | Continuity of continuous-coefficient Laurent evaluation |
| `Circle.Coefficients.Approximate.exists` / `Matrices.exists` | Continuous-coefficient Laurent approximation of product functions/matrices |
| `Laurent.On.Reparameterization` | Evaluation/error compatibility under base maps and circle-unit composition |

Coefficient subalgebras are actual evaluation images of Laurent-ring elements.
Laurent induction proves continuity/conjugation closure; Urysohn functions separate base points, variables separate circle points.
Circle-only versions translate one-point coefficient functions to complex coefficients, proving evaluation agreement.
`Circle.Scalar.Translation` exposes this comparison; `Subalgebra`, `algebraLaws`, `separation` also apply to finite entries/bundles.

## Finite entries, bundles, and invertibility

`FiniteChoices` and `ComplexOn.FiniteComponents` select finitely many common-error approximations; `Matrices.On.density` assembles actual matrix families.
`FiniteComplex` reuses existing finite sums/enumerations.
`Matrices.actionError` turns entry errors \(\leq\delta\) into action errors \(\leq\delta\sum_j\lvert v_j\rvert\).
`compressedError` also bounds left-matrix amplification by finite sums.

`Bundles.Over[X, F, bundle].splittingExists` constructs actual bundle maps \(E,C\), \(CE=1\), from B03 embeddings/image comparisons.
Below write `Split[n, include, project, retraction]` as `Split` and set \(P=EC\).

| API | Contents |
| --- | --- |
| `Split.MatrixMap.compressed` | Bundle maps \(CaE\) from continuous matrices \(a\) |
| `Split.Approximate[h].matrix` / `regular` | Transfer endomorphisms \(h\) to ambient matrices \(EhC\) |
| `Split.Approximate.Density.uniformExists` | Actual approximating matrices with subalgebra entries and compressed maps; entry errors \(<\epsilon\) on \(\sum_j\lvert(Ev)_j\rvert\leq1\) |
| `Split.ProjectionBound.exists` | Compactness gives common positive bounds for projection rows |
| `Split.Invertible.isomorphism` | Bundle isomorphisms/continuous inverses from projection-commuting invertible matrix families |
| `Split.Lift` | Continuity/projection commutation of \(PaP+(1-P)\), original-compression agreement |
| `Split.Lift.Invertible.isomorphism` / `forwardEquals` | Isomorphisms from relative determinant-error conditions with the original compression as forward map |

`Matrices.invertibleOfDeterminantError` requires \(\lvert\det a-\det b\rvert<\lvert\det a\rvert\).
`Matrices.On.Margin.exists` constructs \(0<\eta\leq\lvert\det a(x)\rvert\) on compact bases; `invertibleError` derives inverses from uniform determinant error \(<\eta\).
Impose this on `Lift.matrix` for bundles, reusing L01 inverses/L03 continuity.

## Examples, validation, and resuming

[Examples.Circle](src/Approximation/Examples/Circle.ref) approximates \(\lvert\operatorname{Re}z\rvert\) using 2×2 and zero-size Laurent matrices.
[Examples.Coefficients](src/Approximation/Examples/Coefficients.ref) compares actual polynomials/evaluations for \(g(x)z^{-1}\).
[Examples.Bundle](src/Approximation/Examples/Bundle.ref) uniformly approximates trivial-circle-line endomorphisms on the unit ball.
[Examples.IdentityMatrix](src/Approximation/Examples/IdentityMatrix.ref) uses invertibility-error conditions on arbitrary identity dimensions.

Base: K01-integrated main `f6c3dcfb`; branch: `math/k04-uniform-approximation`; [PR #45](https://github.com/pdf-jube-joba/ref-type/pull/45).
Target/examples `work/k04-examples` on `71ddcdd1`: saved successfully, exit 0.
Target/full-dependency `work/k04-package-retry` on `97e259ec` snapshot: saved successfully, exit 0.
4,702 modules checked, 640 reused, 59,627 source steps, peak RSS 5,708,712 KiB; zero recoveries/duplicates/reruns/unsaved steps/cache-write or save failures.
`work/k04-workspace` on `9004f57b` snapshot also saved successfully, exit 0.
Includes B03 shared-API consumers/all examples: of 7,753 modules, 2,314 checked, 5,439 reused; 31,422 steps, peak RSS 9,112,984 KiB; zero recoveries/duplicates/reruns/unsaved steps/cache-write or save failures.
Math sources/package settings match verified snapshots; no unverified math sources or implementation remain.
Check PR #45/main for integration; recreate snapshots with the commands below for revalidation.

```sh
target/debug/cli libs/analysis/uniform_approximation --parse-only --save-source-snapshot work/k04-package-retry.source.json
target/debug/cli libs/analysis/uniform_approximation --source-snapshot work/k04-package-retry.source.json --memory-mib 8192 --cache-budget-mib 12288 --time-limit-seconds 1800 --report-json work/k04-package-retry.report.json
target/debug/cli libs --parse-only --save-source-snapshot work/k04-workspace.source.json
target/debug/cli libs --source-snapshot work/k04-workspace.source.json --memory-mib 10240 --cache-budget-mib 12288 --time-limit-seconds 7200 --report-json work/k04-workspace.report.json
```

Initial `work/k04-package` exited 2 due to snapshot/input-entry mismatch; resolved by package-entry rechecks above.
Updated dependencies/library index/roadmap to match implementation, moving completed plans to public APIs.
