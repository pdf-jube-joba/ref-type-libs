# Tensor duals of finite-free chains

Construction details and records for [singular_tensor_dual](../../../../libs/topology/singular/tensor_dual/README.md).
See [building and checking](../../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`Over[R, ring]` is over commutative rings.
`Finite[V, rank].Frame` decomposes identity by finite vectors/functionals, including projective dual frames beyond free bases.
Standard frames: `Finite.Coordinates.frame`; frames from finite-coordinate basis isomorphisms: `Finite.FromIsomorphism[e].frame`.

`On[P, Q, ranks, frames]` takes nonnegative \(P,Q\) and finite dual frames for each \(P_n\).
No finiteness of \(Q_n\) or global boundedness needed.
Diagonals \(p+q=n\) are finite.

`source` is \(\operatorname{Tot}(\operatorname{Hom}(P,R)\otimes_R\operatorname{Hom}(Q,R))\); `target` is \(\operatorname{Hom}(\operatorname{Tot}(P\otimes_R Q),R)\).
`forward` and `backward` are inverse cochain maps; `equivalence` is an equivalence with zero homotopies.
`Degree[n].isomorphism` gives degreewise module isomorphisms.

`Evaluation[n, i].law` proves for components \(i=(p,q)\)

\[
(\varphi\otimes\psi)(x\otimes y)=\varphi(x)\psi(y)
\]

Signs follow tensor horizontal/vertical differentials, the latter weighted by \((-1)^p\).
Using dual frames \((e_i,e^i)\), local inverses are

\[
h\longmapsto\sum_i e^i\otimes\bigl(y\longmapsto h(e_i\otimes y)\bigr)
\]

`Selected[P, Q, p, q]` gives specified-diagonal evaluation/closure/chain-map naturality without finiteness.
`onPure` proves same-component products; `offInjection` cross-component zero.
`Integer.Convert[P]` compares standard integral actions with additive-group-induced integer actions on cochains.
`Integer.Singular[A, source, p, q]` identifies singular cup tensor evaluation with `Selected` evaluation through that equivalence.

`IntegerCoordinates[rank].isomorphism` identifies integer-linear maps from integer coordinates into \(R\) with \(R^{\mathrm{rank}}\) by standard-basis values.
Integer actions come from \(R\)'s additive group; cochains remain \(R\)-modules.

`Mixed.On[P,Q,ranks,frames]` takes nonnegative integer chains and finite-free basis isomorphisms of each \(P_n\), constructing the cochain isomorphism
\[
\operatorname{Tot}\bigl(\operatorname{Hom}_{\mathbb Z}(P,R)\otimes_R\operatorname{Hom}_{\mathbb Z}(Q,R)\bigr)
\cong \operatorname{Hom}_{\mathbb Z}\bigl(\operatorname{Tot}(P\otimes_{\mathbb Z}Q),R\bigr)
\]
`Mixed.On.Evaluation.law` pure tensors use the same \(\varphi(x)\psi(y)\) formula.
`Mixed.HomEquivalence.At.isomorphism` gives \(R\)-module cohomology isomorphisms from integer chain equivalences for arbitrary commutative coefficients.
