# Lp spaces

`lp_spaces.On[A, mu]` uses existing `functional_analysis.Measure.Lp.Finite` quotients on arbitrary measure spaces.
Provides real linear/norm structures for \(1\le p<\infty\), Hölder/Minkowski, completeness, real/complex \(L^2\) Hilbert structures, and density of integrable simple functions.
Existing `LInfinity` quotients also receive essential-supremum norms and real Banach structures.
No finiteness, σ-finiteness, or measure completeness required.

| API | Contents |
| --- | --- |
| `Powers.value` / `Powers.law` / `Powers.Unique.unique` | Nonnegative-real powers, agreement/uniqueness with rational-power comparisons |
| `Powers.Algebra` / `Powers.Convergence` | Power products/iteration/order/roots/sequence limits |
| `Powers.Young.inequality` | Young inequalities for finite positive conjugate exponents |
| `On.Finite[p]` | Existing quotients, addition/inverses/scaling, canonical moments/norms of representatives |
| `On.Infinity.Vector.space` / `Norm.structure` / `Completion.complete` | Existing L∞ real vector/norm/Banach structures |
| `On.Endpoint.inequality` / `rightInequality` | L1–L∞/L∞–L1 integrable products and Hölder bounds |
| `On.Finite[p].Vector.space` | Real vector structures on existing quotients |
| `On.Norm[p].norm` / `metric` | Normed spaces including Minkowski, induced metrics |
| `On.Holder[exponents]` | Integrable conjugate-exponent products and Hölder |
| `On.Norm[p].Dominated[d].theorem` | Norm convergence under common Lp domination |
| `On.Completion[p].complete` | Quotient limits for arbitrary Cauchy sequences |
| `On.Hilbert.inner` / `hilbert` | Real L2 integral inner products and Hilbert structures |
| `On.Complex.Geometry.norm` / `On.Complex.Inner.inner` / `On.Complex.Complete.hilbert` | Complex L2 norms/inner products/completeness over arbitrary measures |
| `On.Complex.Characterization.equivalence` | Equivalence of component L2 and complex measurability/modulus L2 conditions |
| `On.SimpleApproximation[p].dense` | Lp approximation by L1-integrable real simple functions |
| `On.Restriction[p, S].integrable` | L1 integrability of finite-p functions restricted to finite-measure sets |
| `On.Parametric.continuous` / `On.Differentiation.derivative` | Parameter-limit/derivative interchange under common integrable domination |
| `On.Jensen[p].inequality` | Integral p-power bounds for nonnegative mass-one densities |
| `On.Pullback[p, map]` | Measure-preserving pullbacks, a.e.-quotient definitions, norm/distance preservation |
| `Euclidean[n].Translation[p].continuous` / `Group.continuousAt` | Finite-p Lebesgue translation ε–δ norm continuity, composition/isometry |
| `Euclidean[n].BorelRepresentative[p].existsRepresentative` | Borel representatives of all finite-p Lebesgue classes |
| `Euclidean[n].Joint.measurableKernel` | Joint measurability of `f(x−y)ρ(y)` for Borel representatives in product σ-algebras |
| `Euclidean[n].Compact[p]` | Measurability/bounds/Lp representatives of continuous/smooth compact-support functions |
| `Euclidean[n].Approximation[p].smoothDense` / `continuousDense` | Euclidean compact-support smooth/continuous density for finite real exponents `1 ≤ p < ∞` |
| `Euclidean[n].Convolution[p].smooth` / `Derivative.derivative` | Finite-p representative/smooth compact-kernel convolution, everywhere integral existence/smoothness/partial formulas |
| `Euclidean[n].Convolution[p].Normalized.norm` / `Operator` | Nonnegative mass-one Lp contractions, representative-independent quotient definitions |
| `Euclidean[n].Convolution[p].approximateIdentity` / `Smoothing.convergence` | Approximate identities from normalized bumps and norm convergence for all Lp classes |
| `Euclidean[n].Convolution[p].CompactSupport.value` | Smooth compact-support convolutions of continuous compact-support functions |
| `Examples[A, mu, p]` | Checked examples with general representatives/quotients/exponents |

Auxiliary nonnegative exponent APIs follow `PositivePower.atZero`, assigning zero to zero bases.
Lp exponents and norm-root exponents are positive.

`On.ConjugateExponents` groups two existing finite exponents and \(p^{-1}+q^{-1}=1\).
`Holder.representative` represents actual pointwise integrable products, deriving product measurability from factor measurability.

Completeness selects Cauchy subsequences with dyadically small differences, applying monotone convergence to p-powers of absolute-difference partial sums.
Set a.e. limits to zero on measurable exceptional null sets; measure completeness is unnecessary.
Simple approximation uses existing positive/negative finite simple approximations, separately proving each stage L1.

```ref
\import lp_spaces.On[A := A, mu := mu] \as L;
\import L.Finite[p := p] \as F;
\import L.Finite[p := p].Vector[] \as V;
\import L.Norm[p := p] \as N;
\import functional_analysis.Normed[V := F.Space, space := V.space] \as Normed;

\definition complete: Normed.IsBanach N.norm := L.Completion[p := p].complete;
```

Complex L2 inner products are second-variable linear and integrate pointwise `conj(f) * g`.
Construct complex L2 limits from real L2 limits of real/imaginary Cauchy components.

Euclidean density uses box truncation, finite simple cells, measure regularity, G01 cutoffs, and Lp dominated convergence.
Density is claimed only for finite p, not L∞. `EuclideanExamples[n, p]` is a checked example for general dimensions/exponents/classes.

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

[Build and check](../../USAGE.md) from the repository root:

```sh
reftype/target/release/cli libs/analysis/lp_spaces --module lp_spaces --diagnostics compact --no-progress --memory-mib 12288
```
