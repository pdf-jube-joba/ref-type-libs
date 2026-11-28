# C11 Leray–Hirsch comparison

## Requirements

- Primary implementation: `leray_hirsch`.
- For locally trivial fibrations over finite CW bases, formulate lifting a finite free fiber-cohomology basis to total-space classes.
- Prove the module isomorphism given by multiplying pulled-back base classes with basis classes, using cells and Mayer–Vietoris comparisons.
- Expose naturality for pairs, coefficients, and base pullback; identify the trivial-bundle case with the external-product isomorphism.

## Dependencies

- [C03 Thom classes and the Thom isomorphism](../libs/topology/cohomology_thom/README.md)

## Proof

Let \(\pi:E\to X\) be a locally trivial bundle with fiber \(F\), let \(K\)
be a commutative ring, and let \(u_i\in H^{d_i}(E;K)\) be a finite
homogeneous family restricting to a basis on every fiber. For \(A\subset X\)
write \(E_A=\pi^{-1}(A)\). The comparison in degree \(n\) is
\[
\Phi_{X,A}:\bigoplus_i H^{n-d_i}(X,A;K)\longrightarrow H^n(E,E_A;K),
\qquad (a_i)_i\longmapsto\sum_i \pi^*a_i\smile u_i .
\]

### Product calculation on a chart

For an arbitrary pair \((V,W)\), the relative singular chain group
\(C_p(V,W;\mathbb Z)\) is free on the \(p\)-simplices of \(V\) whose images
are not contained in \(W\). Alexander–Whitney and the shuffle equivalence
respect the chains of \(W\times F\), so adjunction identifies the cochains
of \((V\times F,W\times F)\), up to cochain homotopy equivalence, with the
total cochains of
\[
D^{p,q}=\operatorname{Hom}_{\mathbb Z}
 \bigl(C_p(V,W;\mathbb Z), C^q(F;K)\bigr).
\]
Put \(H^*(F;K)\) in a cochain complex with zero differential and send each
basis element to any representing cocycle. The resulting chain map to
\(C^*(F;K)\) is a quasi-isomorphism. Applying
\(\operatorname{Hom}_{\mathbb Z}(C_p(V,W;\mathbb Z),-)\) preserves it for
each \(p\), since those chain groups are free. Filtering the two
first-quadrant totals by \(p\) gives a quasi-isomorphism of totals. The
filtration in each total degree is finite. The finite basis identifies
the source total with the direct sum of the shifted relative cochain
complexes of \((V,W)\). On cohomology the resulting map is external cup
product by Alexander–Whitney's formula. This proves the product
isomorphism for the chosen pulled-back fiber classes.

Over a chart \(V\times F\), expand the given lifts \(u_i|_{V\times F}\)
in the product isomorphism for \((V,\varnothing)\), with matrix entries in
\(H^{d_i-d_j}(V;K)\) in row \(j\), column \(i\). An entry can be nonzero
only for \(d_j\le d_i\). On equal fiber degrees the entries belong
to \(H^0(V;K)\). Fiber restriction evaluates those functions on
path components, so the equal-degree blocks are pointwise invertible by
the fiber basis hypothesis. Their inverses are again matrices of
functions on path components. On the relative source, cup multiplication
by these blocks gives an invertible diagonal operator. The strictly
lowering part in fiber degree is nilpotent after composition with the
inverse diagonal operator, since the set of basis degrees is finite.
The finite geometric series gives the inverse. Thus the comparison for
the specified lifts is an isomorphism on the chart and on every open
subspace of the chart.

### Finite CW gluing

Each characteristic disk of the finite CW structure is compact. Its
image is compact, and the finitely many images cover \(X\), so the open
chart cover admits a finite subcover. Induct on the number of charts
in its union. The empty case has zero cohomology. At an induction step
the new chart and its intersection with the previous union have the
product calculation above. The induction hypothesis treats the
previous union.

Take relative Mayer–Vietoris for the two opens in the new union and for
their inverse images in \(E\). For each \(i\), pullback commutes with
connecting maps, and so does right cup by \(u_i\). For the cup assertion,
lift an overlap cocycle to a pair of cochains and multiply both lifts
by the restrictions of a single cocycle representing \(u_i\).
The Leibniz rule gives \(d(c\smile u_i)=dc\smile u_i\), so the resulting
connecting class is \(\delta(c)\smile u_i\). Restriction and the signed
difference commute by cup naturality and additivity. Taking the finite
direct sum of the shifted exact sequences, the five lemma proves the
comparison on the union. The induction applies with \(A\) restricted to
each open, so it proves the relative comparison as well as the
absolute one.

For a map of pairs and its bundle pullback, pullback of the comparison
equals the comparison using the pulled-back \(u_i\) and the pulled-back
\(a_i\). A unital coefficient homomorphism gives the same identity with
both classes changed by that homomorphism. These identities hold for
the comparison maps before imposing the basis hypothesis. For a product
bundle with classes pulled back from the fiber, the comparison is the
external product just calculated.

## Ref implementation status

The package constructs the fiberwise basis hypothesis, a cocycle model
realizing that basis, the shifted finite direct-sum comparison map,
and the positive bidegree identities
for pullbacks, coefficients, and external cup products. The chart
subcover and Mayer–Vietoris pullback constructions use C03's shared
topology and relative-cohomology machinery. The product isomorphism
and its identification with Alexander–Whitney, the change of lifted
basis on chart pairs, and the cup compatibility and five-lemma
argument for the finite CW comparison remain to be formalized.
