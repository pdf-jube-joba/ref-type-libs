# `lp_spaces` notes

[Package API](../../../libs/analysis/lp_spaces/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

`lp_spaces.On[A, mu]` uses existing `functional_analysis.Measure.Lp.Finite` quotients on arbitrary measure spaces.
Provides real linear/norm structures for \(1\le p<\infty\), Hölder/Minkowski, completeness, real/complex \(L^2\) Hilbert structures, and density of integrable simple functions.
Existing `LInfinity` quotients also receive essential-supremum norms and real Banach structures.
No finiteness, σ-finiteness, or measure completeness required.

Auxiliary nonnegative exponent APIs follow `PositivePower.atZero`, assigning zero to zero bases.
Lp exponents and norm-root exponents are positive.

`On.ConjugateExponents` groups two existing finite exponents and \(p^{-1}+q^{-1}=1\).
`Holder.representative` represents actual pointwise integrable products, deriving product measurability from factor measurability.

Completeness selects Cauchy subsequences with dyadically small differences, applying monotone convergence to p-powers of absolute-difference partial sums.
Set a.e. limits to zero on measurable exceptional null sets; measure completeness is unnecessary.
Simple approximation uses existing positive/negative finite simple approximations, separately proving each stage L1.

Complex L2 inner products are second-variable linear and integrate pointwise `conj(f) * g`.
Construct complex L2 limits from real L2 limits of real/imaginary Cauchy components.

Euclidean density uses box truncation, finite simple cells, measure regularity, G01 cutoffs, and Lp dominated convergence.
Density is claimed only for finite p, not L∞.

L∞ completeness combines countable exceptional sets for terms/difference bounds, takes pointwise Cauchy limits outside, and sets representatives to zero on measurable null sets.

Borel representatives reuse completeness a.e. limits of smooth approximations, covering exceptions by Borel null sets and zeroing there.
Joint measurability follows by pulling back Borel σ-algebras through measurable product coordinates/differences.

Define convolution everywhere by \((f*\rho)(x)=\int f(y)\rho(x-y)\,dy\); reflection/translation substitution identifies \(\int f(x-y)\rho(y)\,dy\).
Local L1, compact kernels, and bounded partials interchange derivatives/integrals, inductively proving all finite-order smoothness.
Fubini in contraction estimates uses proved joint measurability of Borel moments and kernels.
Since a.e.-equal representatives have everywhere-equal convolutions, transfer operators to original Lebesgue quotients.

`Convolution.ApproximateIdentity` is a sequence of nonnegative smooth mass-one kernels with support radii at most one shrinking to zero.
`approximateIdentity` normalizes G01 bumps by integrals at dyadic radii.
`Smoothing[identity].convergence` gives norm convergence for arbitrary such sequences and finite-p classes, requiring no smoothness/compact support of inputs.
Extend compact-smooth-input dominated convergence to general inputs by contraction and density.
These Euclidean theorems include dimension zero.

## Examples

```ref
\import lp_spaces.On[A := A, mu := mu] \as L;
\import L.Finite[p := p] \as F;
\import L.Finite[p := p].Vector[] \as V;
\import L.Norm[p := p] \as N;
\import functional_analysis.Normed[V := F.Space, space := V.space] \as Normed;

\definition complete: Normed.IsBanach N.norm := L.Completion[p := p].complete;
```

`Examples` uses general measures and quotient elements; `EuclideanExamples[n, p]` handles arbitrary dimensions and finite exponents.
