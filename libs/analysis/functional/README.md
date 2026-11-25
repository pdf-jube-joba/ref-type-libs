# `functional_analysis`

Real normed/Hilbert spaces, Arzelà–Ascoli, Riesz representation, Hahn–Banach, open mapping, compact supports, definitions of \(L^p\), weak derivatives, and Sobolev spaces.

The measure/Lp/Sobolev APIs here define quotients; bundled norms and completeness are in [lp_spaces](../lp_spaces/README.md), and Euclidean Lebesgue measure is in [euclidean_measure](../euclidean_measure/README.md).

| Entry | Purpose |
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

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/analysis/functional.md)
