# `normal_bundles`

Immersion normal bundles, local orthonormal frames, direct-sum decompositions, base change and stabilization.

Normal bundles retain basepoints in the source manifold, so immersions may have self-intersections.

| Entry | Purpose |
| --- | --- |
| `Fiber` / `fiberSpace` / `fiberDimension` | Fibers, vector spaces, \(k\)-element bases |
| `At.Quotient.isomorphism` / `onClass` | Canonical \(\mathbb R^{n+k}/\operatorname{im}(di_x)\)-normal isomorphisms |
| `Local` / `LocalFrame.At.isomorphism` | Smooth local orthonormal frames, inverse trivializations |
| `covers` / `changes` / `manifold` | Frame covers, smooth transitions, \(n+k\)-dimensional totals |
| `SubspaceTopology.explicitHomeomorphism` | Homeomorphisms to orthogonality subspaces of \(M\times\mathbb R^{n+k}\) |
| `Projection` / `Zero` / `Addition` / `Scaling` | Projections/zero sections/fiber operations and smoothness |
| `Vector.map` / `FromAmbient.From.Of` | Ambient vector expressions, maps from smooth orthogonal families |
| `Splitting.diffeomorphism` | Diffeomorphisms \(TM\oplus\nu_i\to M\times\mathbb R^{n+k}\) |
| `BaseChange.Between.Of` | Ambient-vector-preserving normal diffeomorphisms covering base diffeomorphisms |
| `Stabilization.On.Of` | Standard-inclusion \(\nu_{i^+}\cong\nu_i\oplus\varepsilon^1\), sum compatibility |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/normal_bundles.md)
