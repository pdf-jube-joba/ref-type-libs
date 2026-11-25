# Singular excision and open covers

From \(\overline Z\subseteq\operatorname{int}_X A\), construct cover \(\operatorname{int}_X A\), \(X\setminus\overline Z\).

| Module | Contents |
| --- | --- |
| `Excision.Over.Pair` / `On` | Excision subsets/closure conditions, two-member covers/inclusions. |
| `On.Chains.Degree` | Before/after small-relative chains identified with free simplices outside subspaces. |
| `Degree.Range` / `Complement` | Lifts after excision, complement-generator bijections/free isomorphisms. |
| `Chains.Preservation` / `Mapping` | Subspace-image preservation, excised/original small-relative maps. |
| `Degree.Comparison` / `Chains.Isomorphism` | Small-relative excision chain isomorphisms, homology/arbitrary-cohomology isomorphisms. |
| `Chains.Naturality` / `Homology` / `Cohomology` | Small/ordinary relative naturality, actual excision-induced isomorphisms. |
| `MayerVietoris.Over.On.Chains` | Two-open chain sums, signed inclusions, sum surjections/short exactness. |
| `Chains.With` | Arbitrary-coefficient dual short/long exact sequences. |
| `Chains.Homology` / `Cohomology` | Ordinary Mayer–Vietoris through small-chain/direct-sum comparisons. |

Mayer–Vietoris intersections restrict the left subspace again by the right set.
Homology inclusion is \((i_*,-j_*)\); next map sums both inclusions.
Cochains restrict to both opens, then subtract intersection restrictions.
Degreewise `exactAtSum`, `exactAtWhole`, `exactAtIntersection` return `module_theory.ExactPair.Sequence` containing maps/image-kernel equality.

## Good pairs and quotients

`GoodPair.Data` is `algebraic_topology.NeighborhoodRetract.Data`, specifying nonempty closed subsets and strong neighborhood retractions.
Retractions include continuous maps, identity on subsets, and subset-fixing homotopies.
Construct contractible neighborhood images and homeomorphisms of subset/basepoint complements.

| Module | Isomorphism |
| --- | --- |
| `GoodPair.On.Homology[z].neighborhoodIsomorphism` | \(H_z(X,A;\mathbb Z)\to H_z(X,N;\mathbb Z)\)。 |
| `GoodPair.Excision.Homology[z].isomorphism` | \(H_z(X,N;\mathbb Z)\to H_z(X/A,qN;\mathbb Z)\)。 |
| `GoodPair.On.Homology[z].relativeIsomorphism` | Quotient-induced \(H_z(X,A;\mathbb Z)\to H_z(X/A,*;\mathbb Z)\). |
| `GoodPair.On.Homology[z].isomorphism` | \(H_z(X,A;\mathbb Z)\to\widetilde H_z(X/A;\mathbb Z)\)。 |
| `GoodPair.On.With[M].At[z].relativeIsomorphism` | Quotient pullback \(H^z(X/A,*;M)\to H^z(X,A;M)\). |
| `GoodPair.On.With[M].At[z].isomorphism` | \(\widetilde H^z(X/A;M)\to H^z(X,A;M)\)。 |

Degrees `z` are arbitrary integers; coefficients `M` arbitrary integer modules.
`QuotientSquare` transfers inclusion/quotient commuting diagrams to chains/homology/cohomology.
Augmented short exact chains compare quotient-point-relative and reduced theories.

## Public excision maps and direct sums

`Excision.Over.Homology[z].isomorphism pair` and `Excision.Over.With[M].At[z].isomorphism pair` return actual excision-induced ordinary-relative isomorphisms.
`Excision.Over.Ordinary[pair]` specifies their domain/codomain types.

For disjoint opens, `MayerVietoris.Over.On.Chains.Disjoint.With[M].At[z].isomorphism` uses empty-intersection cochain vanishing to identify total cohomology with piece sums.
Disjointness is a propositional argument of the isomorphism definition.
