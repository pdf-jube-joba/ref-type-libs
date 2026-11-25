# `sphere_maps` notes

[Package API](../../../libs/topology/spheres/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Construct continuous existing-Euclidean-sphere maps and compute singular cohomology actions.

`Circle.Coordinates` identifies the sphere in Euclidean two-space with unit complex numbers.
`Circle.Powers.map` gives circle maps for integer \(k\), using conjugation negatively.
`Circle.Powers.Actions.integer` proves first-cohomology multiplication by \(k\) for arbitrary integer modules; `Degree.integer` gets degree \(k\) from integral generators.
`Actions.Signed.integer` and `Actions.Reduced.integer` give ordinary/reduced integer-degree actions; `Actions.DegreeZero` degree-zero actions.

`Circle.Powers.square` is continuous coordinate \((x,y)\mapsto(x^2-y^2,2xy)\).
`Circle.Roots` gives square roots; `Circle.Powers.Antipodal.Fibers` identifies square fibers with antipodal pairs.
`Circle.Quotient.homeomorphism` constructs actual-square-map \(S^1/(x\sim-x)\cong S^1\).

`Reflection` reflects first/remaining coordinates.
`Hemispheres` computes hemisphere-swap Mayer–Vietoris signs using actual chain maps/short-exact naturality.
`Hemispheres.Homology.Whole.head` proves first-coordinate reflection negates top homology.
`Antipodal.degree` proves antipodal degree \((-1)^{n+2}\) on positive spheres \(S^{n+1}\).
`IntegerPowers.power` is the integer natural power in this formula.

`ZeroAntipodal.With` computes arbitrary-coefficient degree-zero evaluation swaps and negated differences.

`ZeroAntipodal.With.Reduced.law` proves antipodal reduced-zero action \(-1\), since constant cochains are augmentation coboundaries.

`ZeroHomology.Sphere.isomorphism` identifies actual reduced \(S^0\) homology with integers; `onOne` gives north-minus-south generators.
Extending discrete weighted cochains from small chains also supplies cell-endpoint signs.
