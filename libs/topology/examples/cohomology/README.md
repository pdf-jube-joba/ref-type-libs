# Singular cohomology examples

Check public `singular_cohomology` APIs from another package.

| Module | Checks |
| --- | --- |
| `Basic` | Constant simplices, representative values, chain/cochain square zero, augmented degree \(-1\)/right inverses, empty/point/interval calculations, path-component degree zero, reduced degree-minus-one conventions. |
| `Relative` | Subspace-chain quotient vanishing, relative square zero, coefficient groups, connecting/exactness, vanishing-cochain isomorphisms, cochain short/long exact sequences. |
| `Coefficients` | Bockstein connecting maps/exactness from coefficient short exact sequences. |
| `OpenCovers` | Point excision, open-cover chain/cochain short exact sequences, ordinary Mayer–Vietoris. |
| `Maps` | Continuous generator maps, coefficient-cochain representative evaluation, identity cohomology action. |
| `Geometry` | Contractible Euclidean disks in all dimensions, \(S^0\)/discrete-two-point homeomorphisms. |
| `ZeroSphere.With` | \(H^0(S^0;M)\cong M\oplus M\), positive vanishing via two-point-open Mayer–Vietoris. |
| `ZeroSphere.Homology` | \(H_0(S^0;\mathbb Z)\cong\mathbb Z^2\), positive vanishing via two-point/disjoint-cover comparisons. |
| `ZeroSphere.Reduced` | Two-point reduced theory with augmentation compatibility. |
| `SphereCover` | Two contractible opens, intersection retracting onto lower spheres. |
| `Spheres.With` / `Spheres.Homology` | Ordinary/reduced arbitrary-sphere groups by Mayer–Vietoris. |
| `Spheres.Orientation` | Oriented generators, induced degrees/composition. |

[sphere_maps](../../spheres/README.md) connects reflections/circle powers with these oriented computations.
[cohomology_examples](../finite_models/README.md) uses actual-singular comparisons for finite graphs/tori/projective planes.

[Build and check](../../../USAGE.md) from the repository root:

```sh
ref-type/target/debug/cli libs/topology/examples/cohomology --module cohomology_models --diagnostics compact
```

Use common dependency `libs/refcache/`.
