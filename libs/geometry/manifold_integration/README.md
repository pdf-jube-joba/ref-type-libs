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
| Flat.Of.stokes | Integrate the exterior derivative of a compactly supported form of degree (n) on (mathbb R^{n+1}) |
| Interval.On.Exact.stokes | Integrate the exterior derivative of a smooth function on a closed interval with its increasing orientation |
| Interval.On.Simplex.stokes | Integrate pullbacks along smooth singular paths into a Euclidean open set and compare with the signed endpoint coboundary |
| Collar.On.With.Of.At | Compute the outward-first contraction along the actual boundary inclusion from a G04 collar and prove the sign of its normal coefficient |
| Corner.On.Over.cancel | Integrate the two orders of normal contraction over a common codimension-two parametrization and prove cancellation |

The interval API uses an open neighborhood of the parameter interval and allows the unit interval for singular paths. Its signed endpoints are the terminal vertex with coefficient \(+1\) and the initial vertex with coefficient \(-1\).

Global partition-of-unity integration, Stokes for arbitrary compact manifolds with boundary or corners, and the higher-dimensional smooth singular cochain map remain open.

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
