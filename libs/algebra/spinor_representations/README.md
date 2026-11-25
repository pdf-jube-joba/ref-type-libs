# Complex spinor representations

Construct Clifford/Spin/Spin-c representations from creation/annihilation on complex exterior algebras.
Inner products are conjugate-linear first, linear second; real Clifford multiplication is self-adjoint.
Finite-dimensional constructions include dimension zero.

`Complex.Dimension[n]` uses all-degree exterior forms on \(\mathbb C^n\) as spinors.
`TotalInner.Adjoint` gives creation/annihilation adjoints; `TotalInner.Adjoint.Isometry.PinAction` gives isometric Spin-c actions.
`RealCoordinates.Clifford.Spin.Phase` gives Spin-c actions from standard real \(2n\)-Clifford algebras, orthogonal projections, and determinant characters.

`homomorphism` in `UnitaryOrthogonal.CanonicalLift` is \(U(n)\to\operatorname{Spin}^c(2n)\), determined by fixing the vacuum.
`CanonicalLift.FockWords.Complete.actionEqual` compares its spinor action with exterior pullback.
`Pairing.Determinant.correspondence` identifies Spin-c determinant characters with inverse unitary determinants.
The pullback convention acts by inverse determinant in top degree.

`Topology.topology` is the spinor topology from all-degree evaluations.
`Families.liftedOrbitContinuous` proves standard-lift orbits of fixed spinors continuous for continuous unitary families.
`Families.determinantContinuous` also proves continuity of standard-lift Spin-c determinant characters along continuous unitary families.
`UnitaryOrthogonal.Smooth.lifted` proves lifts of entrywise smooth unitary families smooth in Spin-c coefficient coordinates.
`UnitaryOrthogonal.Smooth.FromManifold.On.smoothEntries` gives standard lifts as smooth maps from arbitrary smooth manifolds to actual Spin-c manifolds; `continuousEntries` gives continuity. Assumes local matrix-entry smoothness and applies to smooth transitions.
General continuity from U(n)'s matrix-entry topology to the Spin-c manifold topology remains unproved.

`Over.Direct.Total.comparison` is the linear tensor comparison from left/right spinors to direct-sum exterior algebras.
With finite bases on the right and sum, `Over.Direct.Total.Isomorphism` constructs a linear isomorphism with this forward map.
Left/right contraction coefficients separate kernels for injectivity; generation from the vacuum proves surjectivity.
`Over.Direct.Total.Grading.intertwines` proves parity preservation; `Complex.Graded.Comparison.Algebra.intertwining` full Clifford-action compatibility; `Over.Direct.Total.Vacuum.Words` correspondence of creation-generated states.

[Examples](src/Examples.ref) includes one-dimensional square/adjoint and standard-lift/determinant examples; [ZeroTensor](src/Examples/ZeroTensor.ref) checks zero-dimensional tensor round trips; [Manifold](src/Examples/Manifold/On.ref) gives smooth lifts of identity unitary families on arbitrary smooth manifolds.

[Build and check](../../USAGE.md) from the repository root:

```sh
ref-type/target/debug/cli libs/algebra/spinor_representations --memory-mib 8192 --cache-stats --no-progress
```
