# Integer-graded tensor chain complexes

`tensor_chains.TensorChain` constructs tensor totals and external products of integer-graded chains over commutative rings.
General double-complex totals use finite-support sums on each integer diagonal.

- `Grading` exposes standard integer addition, diagonals `Index n`, degree-lowering maps, `complement n p` and degree identities.
- `BoundedDiagonal.At[n, leftBound, rightBound]` constructs finite diagonals retaining both factor bounds; `finite` and `includes` prove finiteness/inclusion.
- `Over[R, ring].Tensor[C, D]` constructs tensor double complexes.
- `Total[C].complex` carries differential \(d_h+(-1)^p d_v\) and a square-zero proof.
- `Tensor[C, D].TotalTerm[p, q].differential` exposes pure-tensor differential formulas.
- `Exterior[C, D, p, q].map` is \(H_p(C)\otimes H_q(D)\to H_{p+q}(C\otimes D)\); `onClass` is its cycle-representative formula.
- `ExteriorTransport[C, D, p, q].onClass` compares degree-transported external classes with classes on specified diagonals.
- `CycleProductNaturality[C, D, E, F, p, q].With[f, g].Exterior.naturality` proves external-product naturality under maps of both complexes.
- `Map`, `End`, `TensorMapping`, `TensorIdentity`, `TensorComposition` handle total induced maps and identity/composition laws.
- `TensorSquare[A, B, C, D, E, F].With[a0, a1, b0, b1, g]` transfers a left-factor square and right-factor chain map to a tensor-total square.
  `Commutes` is equality of left composites; `square` derives agreement in all total degrees/elements.
- `Row[E, p].complex` shifts degree-\(n\) terms to \(E_{n-p}\) with differential \((-1)^p d_E\).
  `Row[E, p].Homology[n].isomorphism` exposes \(H_{n-p}(E)\cong H_n(\mathrm{Row}_p(E))\); `onClass` gives representative formulas.

External products first annihilate both boundaries, then descend from cycle tensors to homology tensors.
Integer shifts compare `Chain.Prior` type transport and derive homology comparisons from cycle/boundary isomorphisms.

[Build and check](../../../USAGE.md) from the repository root:

```sh
cargo run --manifest-path reftype/Cargo.toml -p cli -- libs/algebra/homological/tensor_chains --module tensor_chains.TensorChain
```
