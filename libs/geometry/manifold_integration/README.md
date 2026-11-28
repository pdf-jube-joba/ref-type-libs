# Manifold integration

Compactly supported top forms are integrated in Euclidean coordinates by taking their coefficient in the standard ordered basis and extending it by zero. An oriented chart cover of a smooth manifold has nonnegative Jacobian determinants on its overlaps. The chart transition maps are diffeomorphisms, so these determinants are nonzero.

| Entry | Purpose |
| --- | --- |
| Euclidean.Chart | Integrate top forms with compactly supported zero extensions in an open chart |
| Euclidean.Transition.For | Transport the integral under a diffeomorphism, with the negative sign for reversing orientation |
| Euclidean.Restriction.Of.In | Restrict to a smaller open chart containing the support |
| Euclidean.Decomposition | Decompose a compactly supported coefficient over an open cover and compare finite sums of the piece integrals |
| Atlas.On.Orientation | Specify an oriented chart cover |
| Atlas.On.Compact.Compare.independent | Compare two oriented coordinate integrals for a global form supported in their overlap |
| Atlas.On.Partition.integral | Integrate a global compactly supported top form using a finite smooth partition on its support |
| Atlas.On.Partition.Compare.independent | Compare partitions by integrating their pairwise products in either oriented chart |
| Atlas.On.SupportComparison.independent | Compare integrals computed with different compact carriers containing the support |
| Flat.Of.stokes | Integrate the exterior derivative of a compactly supported form of degree \(n\) on \(\mathbb R^{n+1}\) |
| Interval.On.Exact.stokes | Integrate the exterior derivative of a smooth function on a closed interval with its increasing orientation |
| Interval.On.Simplex.stokes | Integrate pullbacks along smooth singular paths into a Euclidean open set and compare with the signed endpoint coboundary |
| Interval.On.Path.To.Along.Of.stokes | Compare the integral and endpoint coboundary for a smooth singular path in a smooth manifold |
| Region.On.Of | Integrate continuous coefficients on compact Euclidean regions by their zero extensions |
| Region.On.Partition.law | Integrate a finite partition of a coefficient with weights normalized on the compact region |
| CornerChart.On.Within | Integrate a top-form coefficient restricted to a compact region of a G03 quadrant chart |
| Interval.Box.Of.integral | Compare the compact region integral on a closed interval with its Riemann integral |
| Cylinder.Over.Of.Sections.integralLaw | Integrate one coordinate first on a compact product region using Lebesgue Fubini |
| Cylinder.Over.In.Vertical.theorem | Integrate a normal partial derivative on a compact product region and obtain the upper trace minus the lower trace |
| Cylinder.Over.In.LowerFace.Of.stokes | Identify a normal derivative's lower boundary term with its trace along the actual G03 orthant face |
| Orthant.In.outwardFirst | Give the outward contraction sign on the standard lower orthant face |
| Permute.Between.Of.invariant | Transport compact-region coefficient integrals under coordinate permutations |
| Rectangle.Of.green | Prove the planar curl integral formula with four signed edge integrals |
| Rectangle.Signs | Compute the outward-first orientation of the four rectangle edges |
| Rectangle.Differential.stokes | Integrate the exterior derivative of a smooth one-form over a rectangle and obtain the four oriented edge integrals |
| StandardInterval.stokes | Prove Stokes on the actual G03 interval with the outward-first orientation at its two endpoints |
| Collar.On.With.Of.At | Compute the outward-first contraction along the actual boundary inclusion from a G04 collar and prove the sign of its normal coefficient |
| Corner.On.Over.cancel | Integrate the two orders of normal contraction over a common codimension-two parametrization and prove cancellation |
| Simplex | Project the standard barycentric simplex onto its last \(n\) coordinates and recover the omitted coordinate |
| Simplex.Faces | Express the standard singular face maps in the integration coordinates on the slanted and coordinate faces |
| Simplex.On.Along.cochain | Integrate a pullback along a smooth extension of a simplex into a Euclidean open set |
| Simplex.On.Manifold.To.Along.cochain | Integrate a pullback along a smooth extension of a simplex into a smooth manifold |

The interval API uses an open neighborhood of the parameter interval and allows the unit interval for singular paths. The path API takes a smooth extension to that neighborhood. Its signed endpoints are the terminal vertex with coefficient \(+1\) and the initial vertex with coefficient \(-1\).

The global integral applies to smooth manifolds without boundary. The input includes an oriented chart cover and a compact carrier outside which the form vanishes. The partition construction uses compactly supported G01 bump functions and requires normalization only on the carrier.

The quadrant chart integral takes a smooth form on the ambient open set. Its value depends only on the coefficient restricted to the compact region of the quadrant.

The higher-dimensional simplex integrals use the ordered coordinates \(x_1,\ldots,x_n\) with omitted barycentric coordinate \(1-\sum_i x_i\). The current interface takes a specified smooth extension on an open neighborhood of the simplex.

For arbitrary manifolds with boundary or corners, the global integral and Stokes formula remain open. The higher-dimensional simplex integrals still need independence of the chosen extension and the comparison with the signed face coboundary.

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
