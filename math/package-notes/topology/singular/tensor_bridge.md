# `singular_tensor_bridge` notes

[Package API](../../../../libs/topology/singular/tensor_bridge/README.md) · [Checking](../../../../libs/USAGE.md)

## Construction

`Integer.Factor[C].With[negative]` gives chain isomorphism `isomorphism` and equivalence `equivalence` between negative-vanishing integer `C` and zero-extended nonnegative restrictions.
Nonnegative maps retain elements; negative maps send to zero.
`negative` asserts all negative elements zero, not the comparison isomorphism itself.

`Integer.Indices` connects natural degree-sum indices with corresponding integer sums.
`Integer.Tensor[C, D].With[leftNegative, rightNegative].Positive[n].isomorphism` identifies integer tensor sums in degree `n` with restricted nonnegative double-total terms.
Nonnegative factor components match identical tensors; negative factors vanish by triviality.
`Negative[n].zero` proves negative total terms trivial.

`Integer.Tensor[C, D].With[leftNegative, rightNegative].isomorphism` assembles boundary-compatible degreewise isomorphisms from integer tensors to zero-extended nonnegative totals.
`equivalence` gives equivalences retaining the same forward map.
Compare horizontal/vertical signs on sum generators; boundaries crossing zero vanish by negative triviality.
`Integer.Lift[C, D].With[e]` lifts nonnegative isomorphism `e` to zero-extended isomorphisms.

No finite generation/freeness assumptions.
Sum/tensor universality constructs actual linear maps/inverse laws.
