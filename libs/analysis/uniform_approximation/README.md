# `uniform_approximation`

Real/complex Stone–Weierstrass, Laurent approximation on circles/products, uniform matrix/bundle-endomorphism estimates.

Approximation bases are compact Hausdorff spaces. Complex subalgebras must be closed under conjugation.

| Entry | Purpose |
| --- | --- |
| `Polynomials` | Existing real polynomial rings/evaluation/induction, iterative polynomials `absolutePolynomial` |
| `Absolute.unitBounded` | Uniform polynomial approximation of modulus on \(\lvert x\rvert\leq1\) |
| `On.Dini.uniform` | Uniformization of pointwise approximation with decreasing continuous nonnegative errors via finite subcovers |
| `On.Compact.RealAlgebra.StoneWeierstrass.approximation` | Uniform approximation of arbitrary real continuous functions by point-separating subalgebras |
| `ComplexOn.Algebra.Compact.StoneWeierstrass.approximation` | Uniform approximation by conjugation-closed point-separating complex subalgebras |
| `ComplexOn.Naturality` | Pullback compatibility of errors/approximations/constants/sums/products/conjugation |
| `Circle.Scalar.Polynomial` / `value` | Complex-coefficient `algebra.LaurentPolynomial.Over` elements and circle evaluations |
| `Circle.Scalar.Approximate.exists` | Laurent approximation of arbitrary complex continuous circle functions |
| `Circle.Scalar.Matrices[n, m].exists` | Simultaneous equal-error Laurent entry approximations of finite matrices, including zero size |
| `ComplexOn.FunctionRing` | Continuous complex function rings, conjugation, evaluation homomorphisms |
| `Circle.Coefficients[X, space, baseCompact, baseHausdorff]` | Existing Laurent ring `Polynomial` over continuous coefficients, `value` on \(X\times S^1\) |
| `Circle.Coefficients.valueContinuous` | Continuity of continuous-coefficient Laurent evaluation |
| `Circle.Coefficients.Approximate.exists` / `Matrices.exists` | Continuous-coefficient Laurent approximation of product functions/matrices |
| `Laurent.On.Reparameterization` | Evaluation/error compatibility under base maps and circle-unit composition |
| `Split.MatrixMap.compressed` | Bundle maps \(CaE\) from continuous matrices \(a\) |
| `Split.Approximate[h].matrix` / `regular` | Transfer endomorphisms \(h\) to ambient matrices \(EhC\) |
| `Split.Approximate.Density.uniformExists` | Actual approximating matrices with subalgebra entries and compressed maps; entry errors \(<\epsilon\) on \(\sum_j\lvert(Ev)_j\rvert\leq1\) |
| `Split.ProjectionBound.exists` | Compactness gives common positive bounds for projection rows |
| `Split.Invertible.isomorphism` | Bundle isomorphisms/continuous inverses from projection-commuting invertible matrix families |
| `Split.Lift` | Continuity/projection commutation of \(PaP+(1-P)\), original-compression agreement |
| `Split.Lift.Invertible.isomorphism` / `forwardEquals` | Isomorphisms from relative determinant-error conditions with the original compression as forward map |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/analysis/uniform_approximation.md)
