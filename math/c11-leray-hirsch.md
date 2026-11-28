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
realizing that basis, the shifted finite direct-sum map, and the
bidegree identities for pullbacks, coefficients, and external cup products.
The chart subcover and Mayer–Vietoris pullback constructions use C03's
relative-cohomology machinery.

The relative Alexander–Whitney map descends to the two quotient
complexes. The product boundary is identified with the product of the
base subspace and the fiber. A split exact sequence identifies the
tensor quotient with the total of relative base chains tensored with
fiber chains. On dualizing these split exact sequences, the absolute
Alexander–Whitney equivalences imply the relative cohomology
isomorphism for every commutative coefficient ring. Pullback of the
tensor cochain gives the relative external cup, by evaluation on the
projected front and back faces of each simplex.
The package also identifies the relative base chain modules as free
modules on the complement of the subspace simplices.

The cutoff construction gives degreewise split exact chains for each
successive truncation of the base complex. On the layer at cutoff $p$,
the horizontal term vanishes and the remaining differential is the
vertical differential multiplied by $(-1)^p$. The layer vanishes below
$p$. Reindexing the layer by fiber degree and applying the sign change
identifies its cohomology with that of the unsigned row. Cutting the
base complex through degree $n+1$ preserves degree-$n$ cohomology of
the dual tensor total. Evaluation on a free basis identifies the
cochain complex of one free tensor column with a product of fiber
cochain complexes and carries a fiber quasi-isomorphism to a
quasi-isomorphism for the column. The tensor cup differential
formula for a closed right factor has only the horizontal term, and the
cohomology comparison at the middle of a short exact sequence follows
from the five lemma. For a cochain complex in integer degrees, the
differential twisted by $(-1)^p$ is identified with the untwisted
differential by multiplication by $(-1)^{p|q|}$ in degree $q$.

Relative right cup with a fixed absolute cocycle commutes with the
Mayer–Vietoris connecting map. The projection comparison combines this
identity with naturality of the connecting map. For a right factor of
degree $q$ and base degree $p$, its degree reindexing uses
$(p+1)+q=(p+q)+1$. The signed-degree formulation includes the negative
base degrees, where relative cohomology vanishes. The Leibniz rule
contributes no extra sign because the right factor is closed. Summing
the reindexed components gives an equality between the connecting map
of the overlap sum and the whole-space comparison on the vector of
componentwise connecting classes.

The pair homeomorphism over a chart and the comparison isomorphism
for an empty base are formalized. The remaining algebraic step is to
assemble the cocycle maps on the signed layers into a morphism of the
cutoff short exact sequences. For the relative base chain complex
$P_*=C_*(V,W;\mathbb Z)$, this should show that the map with
components $(x,y)\mapsto a_i(x)u_i(y)$ induces an isomorphism from the
direct sum of shifted cohomology groups of
$\operatorname{Hom}_{\mathbb Z}(P_*,K)$ to the cohomology of
$\operatorname{Hom}_{\mathbb Z}(\operatorname{Tot}(P_*\otimes C_*(F;\mathbb Z)),K)$.
The triangular change of lifts on chart pairs and the assembly of
the restriction and difference squares in the five-term
Mayer–Vietoris diagram also remain. These results would instantiate
the finite-cover induction with the isomorphism predicate.
