# Foundations of Lie groups

Construction details and records for [lie_groups](../../../libs/geometry/lie_groups/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`Dimension[n].OnManifold[M].LieGroup` is a group on Hausdorff second-countable smooth \(M\) with smooth multiplication/inversion.
Joint multiplication smoothness means products of two smooth maps from arbitrary finite-dimensional manifolds are smooth.

`Ad g` differentiates conjugation \(x\mapsto gxg^{-1}\) at identity.
Transport target tangents to identity tangents using conjugation's identity-fixing equality.

`LocalProduct.VectorField` constructs coordinate fields from specified tangents and multiplication Jacobians.
`Initial.atInitial` proves identity values equal specified tangent coordinates.
`LocalCurve` constructs smooth identity-passing group curves from local ODE solutions.
`Translation.Composition` derives local-translation composition/derivative laws from associativity.
`VectorField.Product.equivariance` expresses left invariance.
`LocalCurve.Uniform.On.Comparison.addition` compares translated/time-shifted curves to the same Picard solution, proving local addition.
`Homomorphism` extends local addition to real-domain homomorphisms.
`Homomorphism.Smooth` constructs smooth curves on dyadic open-time domains and glues.
`Generator.generates` proves zero derivatives equal original tangents.
`On.integralExists` packages chart/local-solution existence for arbitrary tangents.

`LocalHom.On` uses \(f(t/2^k)^{2^k}\) for small enough \(t/2^k\).
`At.independent` proves subdivision independence; `Addition.law` global addition.
`Uniqueness.equal` proves uniqueness of global homomorphisms agreeing locally.

`On.integralExists` and `On.integralUnique` uniquely determine one-parameter subgroups with initial velocity \(v\).
`On.integral v` is the smooth subgroup, `On.flow v t` time-\(t\) value, `On.exp v` time-one value.
`flowZero`, `flowAddition`, `flowGenerates` prove identity/time-addition/initial-velocity laws.
`OneParameter.Of.Coordinates.Field` makes arbitrary one-parameter subgroups solve their generator's local field.
Picard uniqueness gives local agreement; dyadic subdivision extends globally.
`OneParameter.Integration` structures one-parameter families; `On.integration` is its canonical value.

`Euclidean[n].orthogonalGroup` and `specialOrthogonalGroup` are group structures on linear maps.
SO(n) preserves all degree-\(n\) alternating forms.
`soLieAlgebra` is the commutator algebra of \(\langle Ax,y\rangle=-\langle x,Ay\rangle\) endomorphisms.
`cliffordScalarInjective` and `cliffordVectorInjective` prove injectivity of standard-inner-product Clifford inclusions.
`PinRepresentation.map` uniquely selects orthogonal maps agreeing with generator twisted adjoints.
Positive unit vectors give reflections, signs identity; product/inverse closure extends to all Pin.
`Kernel.iff` proves kernel exactly \(\{\pm1\}\); `PinSurjectivity.surjective n` gives surjectivity.
`homomorphism` is the group homomorphism, `spinHomomorphism` its Spin restriction, `spinOnVector` ordinary-conjugation expression.

`OrthogonalAtlas.atlasData` inducts O(n) coordinates using sphere stereographic charts/complement restrictions.
Each stage proves local/inverse formulas, chart coverage, and coordinate smoothness along smooth matrix families.
`Euclidean.Atlas.On.FromPlots` tests manifold-to-O(n) smoothness by entries; `Lie` proves smooth products/inverses.
`OrthogonalAtlas.Dimension[n].lieGroup` is its standard-orthogonal-group value.

`OrthogonalOrientation.determinantSign` derives orthogonal determinants \(\pm1\) by reflection determinants/dimension induction.
Determinants are smooth multilinear evaluations; `SpecialOrthogonal[n]` constructs the positive open subgroup.
`SpecialOrthogonal[n].lieGroup` is the SO(n) Lie structure.

`PinFrame[n]` decomposes Pin into sphere-direction local sections times lower-dimensional Pin, proving existence/uniqueness/both smooth directions.
`PinAtlas.atlasData` inducts atlases from dimension-zero two-point atlases; `PinAtlas.Dimension[n].lieGroup` gives actual Lie structures.

`SpinGroup[n]` proves even Pin open, restricting to Spin Lie groups.
Coefficients separate grading-fixed elements from sign-reversed ones to prove openness.

`PinC[n]` and `SpinC[n]` equip existing diagonal-sign quotient carriers with manifolds.
`ComplexRepresentation` real/imaginary coefficients separate quotient points; phase squares are quadratic in them.
Local unit-circle phase square roots uniquely split quotient elements into one real phase coordinate and original Pin/Spin elements.
This gives countable atlases; coefficient formulas prove joint product/inverse smoothness.
Dimensions: \(n(n-1)/2\) for O(n)/SO(n)/Pin(n)/Spin(n), plus \(1\) for complex extensions; includes zero.

`On.SmoothFunctions.Function` consists of real functions smooth after every smooth Euclidean plot.
`On.LieAlgebra.Carrier` consists of their linear endomorphisms satisfying Leibniz and commuting with left-translation pullbacks.
Derivation/left invariance survive commutators; construct `lie` as an endomorphism commutator subalgebra.
`bracket` and `ad` are operations on this Lie algebra.
`TangentAtOne` gives tangent APIs for `Ad` and `exp`; `Euclidean.soLieAlgebra` gives skew-matrix Lie APIs.
