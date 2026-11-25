# Chain algebra for Čech comparisons

`Algebra[R, ring].ProjectiveQuasi[C, D, f].equivalenceExists` constructs chain equivalences retaining forward nonnegative \(f:C\to D\).
Assumes projective terms, degreewise surjectivity, and kernel cycles bounding inside kernels.
Degreewise sections split projective kernels; comparison homotopies of zero resolutions contract them.
`Algebra.Concentrated[C]` puts \(C\) in row \(q=0\), giving original/zero-row isomorphisms.

`PartialCone.On[X]` tests existing vertices and adds missing ones to simplices.
`Cone` gives face-compatible data; `With[cone].homotopy` extends to free integer chains.
`Positive.cycle` and `Zero.cycle` actually fill positive cycles/degree-zero augmentation kernels.
`Coproduct.On[Index, objects]` forms semisimplicial sums, constructing contractions/augmentation sections from component contractions.

`CarrierModel.On[C, D]` models submodule families of \(\operatorname{Hom}(C_n,D_z)\).
Closure under target differentials/source boundaries gives commuting square-zero operators.
`With[S, closed].Diagonal[delta, carried].cells` gives closed diagonals from actual supported chain maps.
Finite-simplicial applications resolve star-cover Čech rows by least-vertex addition and columns by contractible intersections; carrier homotopies identify both augmentations with affine comparisons.
Concrete covers/carriers/comparison assembly: `singular_simplicial.Complex.On.Cech`.

`Algebra.Restriction` restricts integer complexes/maps to nonnegative degrees.
Negative-term vanishing also restricts homotopies/equivalences.
`RestrictionZeroExtension` identifies restricted zero extensions with originals.
`TensorEquivalence` constructs tensor-total equivalences from two nonnegative chain equivalences.

Package/bridge example checks:

[Build and check](../../../USAGE.md) from the repository root:

```sh
cargo run --manifest-path ref-type/Cargo.toml -p cli -- libs/topology/singular/cech --cache-dir libs/refcache
cargo run --manifest-path ref-type/Cargo.toml -p cli -- libs/topology/singular/cech --module singular_cech.Algebra.ProjectiveQuasi.Contracted.Equivalence --module-only --cache-dir libs/refcache
```
