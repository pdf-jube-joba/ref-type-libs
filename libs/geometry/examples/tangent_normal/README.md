# Tangent and normal bundle examples

Check public `tangent_bundles` and `normal_bundles` APIs from another package.
Each isomorphism has actual maps/inverses, smoothness, and inverse proofs.

| Module | Contents |
| --- | --- |
| `Euclidean[n]` | \(T\mathbb R^n\cong\mathbb R^n\times\mathbb R^n\), explicit tangent formulas, tangent identity laws |
| `CoordinateInclusion[n,k]` | Embedding \(x\mapsto(x,0)\), normal trivialization \((x,a)\mapsto(x,(0,a))\) |
| `CoordinateInclusion.Splitting` | Actual direct-sum vector formulas and stabilization compatibility |
| `Parabola.Curve` / `Curve.At` | Smooth \(t\mapsto(t,t^2)\), derivative \(v\mapsto(v,2tv)\) |
| `Parabola.At` | Normal \((-2t,1)\), orthogonality, arbitrary-normal reconstruction |
| `Parabola.Trivialization` | Normal-bundle diffeomorphism \((t,a)\mapsto(t,a(-2t,1))\), inverse by second ambient coordinate |
| `Parabola.Trivialization.addition` / `scaling` | Concrete public normal-fiber operations |
| `Parabola.Functor` | Parabola/first-projection tangent composition, sums/stabilization |
| `Empty[n,k]` | Actual smooth empty-manifold immersions, empty tangent/normal totals |
| `Degenerate` | Zero-dimensional tangent bundles, codimension-zero normal vanishing, \(n=k=0\) |

Parabola first-coordinate projection is a smooth left inverse, yielding embeddings via `manifolds.EmbeddingRetraction`.
`Parabola.At.reconstruction` proves \(w=w_2(-2t,1)\) from orthogonality alone.
`Trivialization` uses this unnormalized global frame; `FromAmbient` proves smoothness into general totals defined by orthonormal local frames.
Real parameters use one-coordinate standard isomorphism `CoordinateLine` because indices are finite-dimensional.

Run checks at the repository root.

[Build and check](../../../USAGE.md) from the repository root:

```sh
ref-type/target/debug/cli libs/geometry/examples/tangent_normal --cache-dir libs/refcache --memory-mib 7168 --diagnostics compact
```

Standard checks cover this package and every dependency-closure module.
