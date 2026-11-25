# Covering spaces and classification

Construction details and records for [covering_spaces](../../../libs/topology/coverings/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`Projection[E, B, total, base, projection]` takes totals/bases/topologies/projections.
`Covering` requires continuous surjections and local products with discrete fibers near every basepoint.

Lift existence uses compact intervals/squares and finite subdivisions.
Discrete local fibers and constancy of paths into discrete spaces give uniqueness.

`goodBasis` in `fundamental_groups.Neighborhoods` gives path-connected open bases with fundamental-group-killing inclusions from standard local/semilocal assumptions.
`PathAction.Realization` uses path transport for sheets, proving topology axioms, continuous projections, local products.
Right coset actions give `Subgroups.Realization[H]` with induced fundamental-group image \(H\).

`Projection.Fundamental[e].Monodromy[covering].imageMembership` equates \(p_*\pi_1(E,e)\) with stabilizers.
Classification `SameSubgroup` and `Conjugate` use these stabilizers.
Conjugacy convention: \(g\mapsto aga^{-1}\).

`Projection.Deck[point].Carrier` is a projection-commuting total homeomorphism; `group` multiplies by ordinary function composition.
`Classification.NormalCosets` consists of \(H\backslash\pi_1(B,b)\) cosets whose representatives normalize \(H\).
`normalizerToClass` and `classToNormalizer` prove this representative criterion.
`normalizerQuotient` constructs group structures and inverse deck-group homomorphisms.
`QuotientIsomorphism.product` ensures \([a][b]=[ab]\), so the quotient is \(N(H)/H\).
Regular covers correspond to normal \(H\), equivalently transitive deck actions on basepoint fibers.
