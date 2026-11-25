# `lie_groups`

Lie groups/algebras, adjoint derivatives/exponentials, Lie structures on O/SO/Pin/Spin and complex extensions.

Lie groups are Hausdorff second-countable smooth manifolds with jointly smooth multiplication and smooth inversion; dimension-zero classical groups are included.

| Entry | Purpose |
| --- | --- |
| `Smooth.Between` | Function smoothness, uniqueness of smooth maps with equal functions, constants |
| `Dimension.OnManifold.On` | Identity tangents, adjoint `Ad`, exponential `exp`, one-parameter subgroups `flow` |
| `Dimension.OnManifold.On.SmoothFunctions` | Smooth real functions, vector structures/products/smooth pullbacks |
| `Dimension.OnManifold.On.LieAlgebra` | Commutator Lie algebra of left-invariant derivations, brackets/`ad` |
| `Dimension.OnManifold.On.LocalProduct` | Smooth local multiplication coordinates and derivative vector fields |
| `Dimension.OnManifold.On.OneParameter` | Smooth one-parameter subgroups, zero velocities, `exp` from integration data |
| `Dimension.OnManifold.On.Integration` | Existence of smooth one-parameter subgroups with specified initial tangents |
| `Dimension.OnManifold.On.UniqueIntegral` | Uniqueness for equal initial velocities |
| `Classical.On.Orthogonal` | Groups of invertible bilinear-form-preserving maps |
| `Classical.On.Orthogonal.Special` | Subgroups preserving all alternating forms of specified degree |
| `Classical.On.Orthogonal.LieAlgebra` | Skew-adjoint endomorphism Lie subalgebras |
| `Euclidean[n]` | Standard inner products, O(n)/SO(n)/\(\mathfrak{so}(n)\), Clifford/Pin/Spin/complex specializations |
| `Euclidean.PinRepresentation` | Twisted-adjoint Pin-to-O(n) homomorphisms and Spin restrictions |
| `Euclidean.InnerProduct` | Positive inner products, nonzero normalization, rational reflection formulas |
| `Euclidean.SuccessorGeometry` | Successor-dimensional complements, lower-dimensional restrictions fixing first basis vectors |
| `OrthogonalAtlas.Dimension[n]` | O(n) smooth manifold `manifold` and Lie group `lieGroup` |
| `OrthogonalOrientation` | Smooth determinants, orthogonal determinants \(\pm1\) |
| `SpecialOrthogonal[n]` | SO(n) open-subgroup manifold `manifold` and Lie group `lieGroup` |
| `CliffordPlots` | Recursive coefficients proving smooth algebra/grading/reversion |
| `Euclidean.PinPlots` | Smooth Pin products/inverses/orthogonal maps by coefficients |
| `CoefficientAtlas` | General manifold/Lie-group interfaces from separating coefficients and local coordinates |
| `PinFrame[n]` | Recursive local Pin products, smooth coordinates/inverse coordinates |
| `SpinGroup[n]` | Spin(n) manifold/Lie group as grading-fixed part |
| `PinAtlas.Dimension[n]` | Pin(n) manifold `manifold` and Lie group `lieGroup` |
| `CircleGeometry` | Unit-circle stereographic charts/smooth square-root sections |
| `ComplexGroup.Over.Base.On` | Complex-extension atlases from faithful complex coefficients/local phase sections |
| `PinC[n]` / `SpinC[n]` | Pin^c(n)/Spin^c(n) manifolds `manifold` and Lie groups `lieGroup` |
| `PinSurjectivity` | Lifts of arbitrary orthogonal transformations to Pin |
| `LocalHom` | Local real homomorphisms and unique global dyadic extensions |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/lie_groups.md)
