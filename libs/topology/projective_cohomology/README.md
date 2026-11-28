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
| `Complex.CanonicalLine.Hopf.CircleAction` | Unit complex scalars act continuously, freely, and transitively on the Hopf fibers |
| `Complex.CanonicalLine.Hopf.CircleAction.Associated.Product` | Scalar evaluation is continuous and surjective onto the tautological bundle. Its fibers are the orbits of the unit circle acting by the inverse scalar on the associated coordinate |
| `Complex.CanonicalLine.Hopf.CircleAction.Associated.Product.AssociatedLine` | The quotient by the inverse-weight circle action is homeomorphic over projective space to the tautological line bundle |
| `Complex.CanonicalLine.Hopf.CircleAction.Associated.Product.DualCoordinates.Orbits` | Evaluation into the complex dual has fibers given by the direct-weight circle action |
| `Complex.CanonicalLine.Hopf.CircleAction.Associated.Product.DualCoordinates.AssociatedLine` | The quotient by the direct-weight circle action is homeomorphic over projective space to the complex-linear dual |
| `Complex.CanonicalLine.Hopf.CircleAction.Associated.Product.Fiber` and `DualCoordinates.Fiber` | Each scalar evaluation in a fixed unit frame is a complex-linear isomorphism onto the corresponding associated line fiber |
| `Complex.CanonicalLine.Hopf.CircleAction.Associated.Product.DualCoordinates.Euler` | The two character bundles have opposite integral Euler classes, with the identity character giving the canonical generator |
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
| `Complex.CanonicalLine.Dual.Riesz` | The Hermitian Riesz identification with the complex-linear dual is continuous in both directions and conjugate-linear on each fiber |
| `Complex.CanonicalLine.Dual.Realification.Norm.Home` | The Riesz identification preserves the ambient norms and gives a homeomorphism of the corresponding disk and boundary pairs over projective space |
| `Complex.CanonicalLine.Dual.Realification.Norm.Chart` | Unit directions in complex dual coordinates are conjugates of the corresponding directions under Riesz |
| `Complex.CanonicalLine.Integral.PlaneDisk.Comparison.Negative` | Maps of disk pairs whose boundary directions differ by complex conjugation pull back relative integral classes with opposite signs in degree two |
| `Complex.CanonicalLine.Dual.Realification.Norm.Home.Fiber.Compare.Relative` | On each fiber, the Riesz pullback sends the dual complex orientation class to the negative of the tautological orientation class |
| `Complex.CanonicalLine.Dual.Realification.Norm.Home.Orientation` | The native complex dual chart orientations define a signed C03 orientation on the underlying real dual bundle |
| `Complex.CanonicalLine.Dual.Realification.Norm.Home.Integral.Euler` | Riesz pulls the dual Thom class back to the negative of the tautological Thom class. The dual Euler class is the negative of the canonical projective generator |
| `RealPlane` and `ComplexLineSphere` | Homeomorphisms with the antipodal quotient model of the real projective plane and the standard two-sphere model of the complex projective line |
| `ComplexLineSphere.PulledHopf` | The underlying real bundle of the sphere model line is the pullback of the realified projective tautological line |
| `ComplexLineSphere.Equator` | In the standard two-sphere model, the second complex frame coordinate on the equator is the first multiplied by the inverse unit-circle coordinate |
| `ComplexLineSphere.Section.Relative.Forgetting` | The projected coordinate section on the standard two-sphere pulls the punctured-bundle Thom class back to a relative class whose absolute image is the tautological Euler class |
| `ComplexLineSphere.Section.Frame.Thom` | The projected north frame defines a continuous complex trivialization, and its standard local disk class equals the restriction of the canonical Thom class |
| `ComplexLineSphere.Section.Frame.EquatorProjection` | The projected coordinate section has complex coordinate \(x+iy\) in the northern frame on the equator |
| `ComplexLineSphere.Section.Frame.DiskCoordinates.Puncture` | The northern section gives a map into the disk relative to its punctured subspace. Its normalized equatorial restriction is the identity on the circle |
| `ComplexLineSphere.Section.Frame.DiskCoordinates.LocalPuncture` and `OpenToModel` | The northern punctured disk bundle retracts onto its boundary. The northern chart map preserves the boundary and the punctured disk pairs |
| `ComplexLineSphere.Section.Frame.DiskCoordinates.EquatorialPull` | The angular section map induces the same integral degree-one pullback as the equatorial retraction |
| `ComplexLineSphere.Section.Frame.DiskCoordinates.Connecting` | The connecting class of the punctured disk restricts to the connecting class of the boundary-circle pullback in the closed disk pair |
| `ComplexLineSphere.Orientation` | The chosen integral generator of the standard two-sphere is obtained from its northern relative generator by the excision comparison and forgetting |
| `ComplexLineSphere.Orientation.PositiveConnecting` | The positive-degree comparison from ordinary to reduced cohomology commutes with the connecting map of a pair |
| `ComplexLineSphere.Orientation.PullCompatibility` | Positive-degree integral pullbacks commute with the reduced-to-ordinary comparison |
| `ComplexLineSphere.DiskOrientation.ZeroSphereSign.DiscreteRepresentative.Spherical` | The chosen reduced integral generator of the standard zero-sphere is represented by the cocycle with values one and zero at its positive and negative points |
| `ComplexLineSphere.DiskOrientation.SphereCoverSign.CohomologyLaw` | The ordinary Mayer–Vietoris connecting map for the standard sphere cover agrees with the northern relative connecting map followed by inverse excision and forgetting |
| `ComplexLineSphere.DiskOrientation.CircleSmallSign` | The normalized zero-sphere cocycle gives the chosen integral circle generator under the ordinary Mayer–Vietoris connecting map |
| `ComplexLineSphere.DiskOrientation.DiskBoundary.Connecting` | The ordinary connecting maps of the round, box, and cylinder disk pairs agree under the C03 coordinate homeomorphisms |
| `RealPlane.ModTwo` | The Euler generator and its square pull back to the two distinguished positive-degree classes of the real projective plane model |
| `ZeroDegree` | Evaluation of constant classes and surjectivity of degree-zero pullback from a path-connected source |

[Source](src/root.ref) · [Plan](../../../math/c04-projective-cohomology.md) · [Checking](../../USAGE.md)
