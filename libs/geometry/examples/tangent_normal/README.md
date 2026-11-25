# `tangent_normal`

Euclidean tangent bundles, coordinate inclusions, parabolas, degenerate-degree examples.

| Entry | Purpose |
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

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../../USAGE.md)
