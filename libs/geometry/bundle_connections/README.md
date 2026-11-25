# Connections and covariant derivatives

`bundle_connections` constructs connections on [smooth_bundles](../smooth_bundles/README.md) smooth bundles.
Bases are second-countable Hausdorff finite-dimensional real manifolds.
Express local frame matrices as actual smooth one-forms, prove affine chart-change laws, and glue.

## Local covariant derivatives and connection matrices

`Local[n,r].On[U].Connection` has smooth coefficients \(A_{i,a,b}\).
`Of[connection].partial` is \(\nabla_i s=\partial_i s+A_i s\), additive with the smooth-function Leibniz rule.
`Dual` gives negative-transpose dual connections/evaluation derivatives; `Of.Tensor` tensor coefficients/product derivatives.
`Flat` proves zero coefficients recover ordinary derivatives and constant sections parallel.

`Form[k]` in `Forms[n,r].On[U]` is a local-frame bundle-valued \(k\)-form.
`Connection` is a one-form matrix; `Covariant` constructs \(d_A\omega=d\omega+A\wedge\omega\).
`Coordinates` and `Coefficients` convert local coefficients/matrices both ways, proving reconstruction.
`Pullback.Between` pulls back forms/matrices and proves covariant-exterior naturality.
`After` handles composition; `Forms.On.Identity` identities.

## Global connections and existence

`Real[n,r].On[M].Family[F,space].Of[I,bundle].Connection` assigns B07 frames connection matrices satisfying overlap transformations.
`existsConnection` constructs this family from smooth partitions of unity.
Transfer flat connections between frames, weight by partition functions, extend by zero off closed supports, and take locally finite sums.
Triple-overlap affine cocycles and unit weight sums imply transformation laws.
Handle empty index types separately.

`SectionCoordinates` derives local coefficient smoothness from actual B07 smooth total-space sections and constructs sections conversely.
`Operators.covariant` acts on actual smooth sections, returning compatible bundle-valued one-forms.
Prove section addition/smooth-scaling rules and agreement with local `Local.Of.partial`.

`Complex[n,r].On[M].Family[F,space].Of[I,bundle]` constructs connections preserving complex structure \(J\) on realifications.
Project real matrices \(A\) to \((A-JAJ)/2\); derive transforms from \(J^2=-I\) and complex-linear transitions.
`existsConnection` asserts complex-connection existence by this construction.
`Operators` constructs actual \(is\) and proves \(\nabla(is)=i\nabla s\).

## Bundle-valued forms and bundle operations

`BundleForms[n,r].On[M].Family[F,space].Of[I,bundle].Alternating[k,enumeration].Tensor[enumeration]` constructs actual smooth bundles \(E\otimes\Lambda^kT^*M\).
`Form` is their B07 smooth-section type, with zero sections and fiberwise pure tensors.
Finite-index enumerations use [bundle_operations](../bundle_operations/README.md) enumeration types.
`TensorIndex` proves single/double sums over them agree.

`Real.On.Family.Of.InducedDual[connection].value` is a connection on B07 dual bundles.
Inverse-transition derivatives and negative transposes give overlap laws.
`PullbackGlobal` refines source charts and target frames together to construct actual pullbacks.
`Exterior` constructs alternating exterior connection coefficients, comparing zero connections/zeroth powers.

`GlobalForms` proves arbitrary-degree local pullback/restriction naturality, smooth-frame covariance, and right-scalar graded Leibniz.
`Real.On.Family.Of.ValuedForms[k]` is a compatible local-form family; `TensorForms.Using.form` sends it to actual bundle-valued smooth sections.
`Operators.TensorForms.Using.derivative` returns ordinary covariant derivatives in this section type.
`GlobalForms.OnManifold.Family.Of.At[k].apply` raises degree globally; `Native.Using` converts results to actual sections.
`Operators.DegreeZero.comparison` identifies degree-zero covariant exterior derivatives with ordinary covariant section derivatives.
`GlobalForms.OnManifold.Family.Of.Wedge.Leibniz` gives global-scalar graded Leibniz.
`GlobalForms.Complex.On.Family.Of.At` represents complex-bundle forms on realifications, proving complex-structure/scalar compatibility.
`PullbackGlobal.Between.Family.Of.Connection.Valued[k].apply` returns forms on actual pullbacks; `Naturality.law` proves global covariant-exterior compatibility.

`Real.On.Family.Of.InducedPaired.Using.Tensor.value` constructs induced B07 tensor connections; `InducedExterior` exterior connections.
Tensor coefficients are \(A\otimes I+I\otimes B\); prove transformation laws for arbitrary finite enumerations.
Prove exterior representation products, differentiate along first matrix jets, derive induced coefficients/transforms.
`ComplexPullbackGlobal` constructs actual complex pullbacks and complex-structure-preserving connections.
`Complex.On.Family.Of.InducedDual.value` is a connection on actual complex dual bundles.
With realified conjugation \(K\), construct coefficients \(-KA^{\mathsf T}K\).
Dual-frame evaluation/real bilinear pairings identify transitions and prove transforms/complex linearity.

Complex induced coefficients use `ComplexMatrices`.
Represent complex one-forms by real/imaginary pairs; recover complex coefficients from real matrices commuting with complex structure.
`ComplexTensorGauge` proves complex finite-sum tensor identities and connection transforms.
Distinguish realified and complex-tensor ranks.
`Complex.On.Family.Of.Coefficients` extracts local complex connection matrices; `FromCoefficients` constructs global connections from complex transforms.
Prove both reconstruction laws and derivative/product/pullback comparisons.
`Complex.On.Family.Of.InducedPaired.Using.Tensor.value` and `InducedExterior.value` are induced connections on actual B07 complex tensor/exterior bundles.
`ComplexEvaluation` differentiates smooth complex multilinear forms on varying vectors; `ComplexExteriorGauge` derives exterior-representation derivatives/frame naturality.

## Metrics and Levi–Civita connections

`Metric` and `ComplexMetric` handle real symmetric/Hermitian local metrics.
Construct smooth inverses from positivity.
`MetricCorrection` corrects arbitrary connections to metric-compatible ones, proving compatibility, frame/pullback/restriction naturality, and fixing compatible connections.
`Real.On.Family.Of.WithMetric` gives global compatible connections for B07 real metrics.
`Complex.On.Family.Of.WithMetric` gives Hermitian existence from real parts and complex structures.
Recover imaginary parts by \(\operatorname{Im}h(v,w)=-\operatorname{Re}h(v,iw)\).

`LeviCivita[n].On[U].Riemannian[metric]` raises Koszul coefficients with inverse metrics.
Directly prove zero torsion/metric compatibility; `Unique.unique` proves uniqueness under both conditions.
`CoordinateChange` uses actual transition Jacobians/Hessians and mixed-partial commutation to derive torsion transforms.
Local uniqueness yields affine connection transforms.
`OnManifold.With[metric].connection`, `laws`, `unique`, `value`, `exists` give global Levi–Civita constructions/properties/uniqueness/existence for B07 tangent metrics.
`Restriction` and `Euclidean` compare open restrictions and standard Euclidean flat connections.

## Examples and checks

`Examples` handles real/complex rank-zero bundles over dimension-zero bases, \(\nabla1=1\) for nonzero constant one-dimensional connections, flat parallel constants, and Euclidean Levi–Civita.

```sh
cargo build -p cli --release --locked
python3 scripts/check_all.py libs/geometry/bundle_connections
python3 scripts/check_all.py
```
