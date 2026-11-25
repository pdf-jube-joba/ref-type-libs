# `lp_spaces`

Real Lp/L∞ Banach structures, real/complex L2, density, translations, convolution/approximate identities.

General-measure-space results require neither sigma-finiteness nor measure completeness. Smooth density is for finite exponents; complex L2 inner products are linear in the second argument.

| Entry | Purpose |
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

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/analysis/lp_spaces.md)
