# Singular excision and open covers

Construction details and records for [singular_excision](../../../../libs/topology/singular/excision/README.md).
See [building and checking](../../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

From \(\overline Z\subseteq\operatorname{int}_X A\), construct cover \(\operatorname{int}_X A\), \(X\setminus\overline Z\).

Mayer–Vietoris intersections restrict the left subspace again by the right set.
Homology inclusion is \((i_*,-j_*)\); next map sums both inclusions.
Cochains restrict to both opens, then subtract intersection restrictions.
Degreewise `exactAtSum`, `exactAtWhole`, `exactAtIntersection` return `module_theory.ExactPair.Sequence` containing maps/image-kernel equality.

## Good pairs and quotients

`GoodPair.Data` is `algebraic_topology.NeighborhoodRetract.Data`, specifying nonempty closed subsets and strong neighborhood retractions.
Retractions include continuous maps, identity on subsets, and subset-fixing homotopies.
Construct contractible neighborhood images and homeomorphisms of subset/basepoint complements.

Degrees `z` are arbitrary integers; coefficients `M` arbitrary integer modules.
`QuotientSquare` transfers inclusion/quotient commuting diagrams to chains/homology/cohomology.
Augmented short exact chains compare quotient-point-relative and reduced theories.

## Public excision maps and direct sums

`Excision.Over.Homology[z].isomorphism pair` and `Excision.Over.With[M].At[z].isomorphism pair` return actual excision-induced ordinary-relative isomorphisms.
`Excision.Over.Ordinary[pair]` specifies their domain/codomain types.

For disjoint opens, `MayerVietoris.Over.On.Chains.Disjoint.With[M].At[z].isomorphism` uses empty-intersection cochain vanishing to identify total cohomology with piece sums.
Disjointness is a propositional argument of the isomorphism definition.
