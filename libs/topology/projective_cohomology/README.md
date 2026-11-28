# Projective cohomology

The real and complex spaces in dimension (n) are the rank-one Grassmannians in ambient dimension (n+1). Their line bundles are the universal subbundles of those Grassmannians.

| Entry | Result |
| --- | --- |
| `Symbols` | Rank-one Schubert symbols correspond to pivots, with real cell dimension (i) and complex cell dimension (2i) |
| `Real.Schubert` and `Complex.Schubert` | Finite CW models with one cell per pivot and explicit cell bounds |
| `Real.Inclusion` and `Complex.Inclusion` | Ambient inclusions preserve and reflect the Schubert filtration |
| `Real.Inclusion.Bundle.Total.Naturality` | The real dimension inclusions pull back the fiber-normalized Thom class, the mod-2 Euler class, and each of its powers |
| `Complex.Inclusion.Bundle.Total.Naturality` | The complex dimension inclusions pull back the signed Thom class, the integral Euler class, and every power |
| `Cellular.With` | Cellular-to-singular chain equivalence, the resulting cohomology comparison, and cup products via a transferred diagonal |
| `CanonicalLine.Hopf` | The unit sphere bundle is homeomorphic to the ambient unit sphere over the line-projection map |
| `Real.CanonicalLine.Hopf.Standard` | Comparison with the standard real sphere and its intermediate-degree cohomology vanishing |
| `Complex.CanonicalLine.Realification` | The underlying real bundle has rank two and carries a metric induced by its ambient embedding |
| `Complex.CanonicalLine.Realification.Norm.Sphere.Standard` | The realified unit sphere bundle is homeomorphic to \(S^{2n+1}\) |
| `Real.Additive` | Vanishing above the dimension and at most one nonzero mod-2 class in each cellular degree |
| `Real.CanonicalLine.ModTwo` | Fiber-normalized Thom class and its Euler class, whose powers survive through degree \(n\) |
| `Real.Ring` | \(H^*(\mathbb{RP}^n;\mathbb{F}_2)\cong\mathbb{F}_2[t]/(t^{n+1})\), with \(t\) the mod-2 Euler class of the universal line |
| `Complex.Additive` | Integral groups are free of rank one in degrees \(0,2,\ldots,2n\) and vanish in odd degrees and above \(2n\) |
| `Complex.CanonicalLine.Integral` | Even-degree zero-section isomorphisms in degrees \(2,\ldots,2n\), and the degree-zero basis given by the cup unit |
| `Complex.CanonicalLine.Integral.Charts` | Complex frame changes give the same signed relative class on each disk fiber |
| `Complex.CanonicalLine.Integral.EvenPowers` | Cup products of powers of a degree-two class, with explicit transport between the graded groups |
| `Complex.CanonicalLine.Integral.Canonical` | \(H^*(\mathbb{CP}^n;\mathbb{Z})\cong\mathbb{Z}[t]/(t^{n+1})\), with \(t\) the Euler class of the canonically oriented underlying real plane bundle |
| `RealPlane` and `ComplexLineSphere` | Homeomorphisms with the antipodal quotient model of the real projective plane and the standard two-sphere model of the complex projective line |
| `RealPlane.ModTwo` | The Euler generator and its square pull back to the two distinguished positive-degree classes of the real projective plane model |
| `ZeroDegree` | Evaluation of constant classes and surjectivity of degree-zero pullback from a path-connected source |

[Source](src/root.ref) · [Plan](../../../math/c04-projective-cohomology.md) · [Checking](../../USAGE.md)
