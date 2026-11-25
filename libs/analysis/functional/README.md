# Functional analysis

Normed/Hilbert spaces and linear functionals over Dedekind reals.
Uses real vector spaces from `linear_algebra`, real distances from `metric_spaces`, and open-set partials from `calculus`.

| Module | Contents |
| --- | --- |
| `Metric[Carrier]` / `Metric.Geometry[d]` | Convergence/Cauchy/completeness, nested closed intersections, Baire |
| `Normed[V, space]` | Norms, induced metrics, Banach spaces, norm continuity |
| `Normed.Operators` / `Operators.OpenMapping[f]` | Bounded maps, distance bounds, convergent images, Banach open mapping |
| `Normed.Hilbert[norm]` | Inner-product/norm compatibility, completeness, representation uniqueness |
| `Normed.Hilbert.Quadratic` | Parallelogram identities, midpoint quadratic forms/continuity |
| `Normed.Hilbert.Quadratic.Minimization` | Minimum-norm points in nonempty closed midpoint-convex sets |
| `Normed.Hilbert.Riesz` | Inner-product representation and representing vectors of bounded real functionals |
| `Order.Towers` / `Order.Maximality` | Inflationary inclusion-order fixed points, maximal chains, Zorn |
| `Normed.HahnBanach` | Full extensions of partial functionals dominated by sublinear functions |
| `Normed.HahnBanach.OnSubspace` | Extension theorems accepting subspace linear maps |
| `Support[A]` | Supports/compact supports, vanishing outside, closed/compact support bounds |
| `Continuous[A, topology]` / `Continuous.Uniform` | Continuous/compact-support functions, equicontinuity, pointwise bounds, uniform convergence/topology |
| `Continuous.ArzelaAscoli` | Arzelà–Ascoli compactness of closed families and relative compactness of general families |
| `Filters[A]` / `Filters.Compactness` | Ultrafilter extension/images and compactness via ultrafilter limits |
| `Measure[A]` / `Measure.Integral` | σ-algebras, nonnegative extended measures, null sets, simple nonnegative integrals, signed-integral conditions |
| `Powers` / `Measure.Lp` | Positive real-exponent powers, finite-exponent \(L^p\), \(L^\infty\) classes |
| `Sobolev[n].On[U].WithMeasure` | Test functions, weak derivatives, \(W^{k,p}\) classes |
| `ScalarLimits` | Product limits, closed half-lines, dyadic geometric bounds |
| `Examples` / `Examples.Ascoli` | Real-line Hilbert space, identity Riesz vectors/Hahn–Banach/open mapping, relative compactness of bounded constants |

## Hahn–Banach

`Sublinear` has \(p(0)=0\), subadditivity, and nonnegative-real homogeneity.
`LinearGraph` is a subspace-functional graph bounded above pointwise by \(p\).
`hahnBanach` asserts existence of full real functionals from this graph and sublinearity.
`GlobalExtension` groups graph agreement, additivity, homogeneity, domination.

Construct one-direction extension values from real infima; apply Zorn to unions of partial-extension chains.
`Functional` and `hahnBanachOnSubspace` in `OnSubspace[subspace]` apply directly to existing `linear_algebra` subspaces/maps.

## Hilbert spaces and Riesz representation

`Hilbert[inner]` requires \(\langle x,x\rangle=\lVert x\rVert^2\) and induced-metric completeness.
`Riesz.Functional` is a norm-bounded real functional.
`riesz` proves that each \(f\) has a representing vector \(y\) satisfying
\[
f(x)=\langle y,x\rangle\qquad(x\in V)
\]
`vector` constructs the vector by unique choice; `vectorLaw` gives representation, `representingVectorUnique` uniqueness.

Construct minimum-norm points in closed affine \(f^{-1}(1)\).
Parallelogram identities make minimizing sequences Cauchy; completeness gives limits, kernel orthogonality yields representation.
Handle zero functionals separately.
`Examples.identityVector` checks the real-line identity functional has representing vector \(1\).

## Open mapping theorem

`Operators.OpenMapping[f].openMapping` proves bounded surjective maps between real Banach spaces open.
Inputs: domain/codomain completeness, surjectivity, and domain open sets; outputs: open images.
`unitLifting` quantitatively gives open-unit-ball preimages for vectors near zero.

Prove the approximation-image set closed; codomain Baire yields a zero neighborhood.
Halve errors dyadically; nested closed balls in the domain give exact preimages.
`Metric.Geometry.Baire` provides dense countable intersections of open dense sets and nonempty interiors in countable closed covers.

## Arzelà–Ascoli

`Continuous.Uniform.topology` is the uniform topology on real continuous functions.
Domains are arbitrary compact spaces, including empty ones.
`Continuous.ArzelaAscoli.arzelaAscoliClosure` proves equicontinuous pointwise-bounded families have compact uniform closures.
`arzelaAscoli` additionally assumes the family closed, concluding its compactness.

The proof uses ultrafilters.
Put point values in compact real intervals and take limits; equicontinuity proves limit continuity.
Finite subcovers turn pointwise into uniform convergence; apply ultrafilter compactness.
`Examples.Ascoli` verifies assumptions for constant functions bounded in modulus by \(1\), then applies the theorem.

## Measure, \(L^p\), and Sobolev spaces

`Measure.Value` represents nonnegative extended reals as downward-open real cuts, including infinity.
Measures have σ-algebras and countable additivity.
`Null` means containment in measurable null sets; `AlmostEqual` means the disagreement set is null.

`Integral.lowerIntegral` is nonnegative integration using finite simple functions on disjoint measurable sets with nonnegative coefficients.
`Integral.Finite` requires function nonnegativity and integral finiteness.
`Integral.HasIntegral` expresses absolute integrability and differences of positive/negative integrals; `integralUnique` proves unique values.
`lowerIntegralMono` proves lower-integral monotonicity; `finiteMono` downward inheritance of nonnegative finiteness.
`Integral.integral` integrates integrable functions; `Integral.Null.quotientIntegral` integrates their a.e.-representative quotient.
`Measure.Finite` gives finite measure additivity/monotonicity; `Measure.Continuity` increasing-measure convergence/countable null unions.
`Measure.AlmostEverywhere` proves a.e. equality an equivalence.
`Integral.Convergence.Monotone.monotone` identifies lower integrals of measurable increasing pointwise suprema with suprema of stage integrals.
`Integral.Examples` has quotient integration from representatives examples.

`Powers.Exponent` is real \(p\ge1\).
`PositivePower[a,p,y]` expresses nonnegative-real \(y=a^p\) by rational comparisons of natural powers.
`Lp.Finite[p].Space` is the a.e. quotient of measurable functions with finite \(p\)-moments.
`LInfinity` is the same quotient for essentially bounded measurable functions.
These define function spaces, without bundled norms/completeness.

Sobolev spaces accept user-specified measures.
Tests on open \(U\subset\mathbb R^n\) require continuous partial families in every order and compact support.
Define weak derivatives by
\[
\int_U u\,D^\alpha\varphi\,d\mu
=(-1)^{|\alpha|}\int_U g\,\varphi\,d\mu
\]
for every test function, then take equivalence classes of functions whose weak derivatives through order \(k\) lie in \(L^p\).
Supply Lebesgue measure for ordinary \(W^{k,p}(U)\).
This package does not construct Euclidean Lebesgue measure.

## Checks

```sh
cargo run -p cli -- libs/analysis/functional --module functional_analysis
cargo run -p cli -- libs/analysis/functional --module functional_analysis.Examples
```

Share workspace `libs/refcache/`.

On whole Euclidean Lebesgue spaces, [distributions](../distributions/README.md) provides test conversions, distribution-derivative equivalence, and inverse comparisons with existing \(W^{k,p}\) quotients.
