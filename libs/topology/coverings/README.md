# Covering spaces and classification

`Projection[E, B, total, base, projection]` takes totals/bases/topologies/projections.
`Covering` requires continuous surjections and local products with discrete fibers near every basepoint.

| Module | Contents |
| --- | --- |
| `Projection.Around` / `Sheets` | Trivializations, continuous local sections, open sheets |
| `Projection.Lifting.Existence` / `Uniqueness` | Path-lift existence/uniqueness |
| `Projection.Lifting.Squares` / `Homotopy` | Square lifts, reflection of endpoint-fixed homotopies |
| `Projection.Transport.Groupoid` / `Action` | Groupoid transport and right fundamental-group actions on fibers |
| `Projection.Fundamental` / `Monodromy` | Injective induced groups, image/stabilizer equality, equivariant coset/fiber bijections |
| `PathAction.Realization` | Sheet topology/trivializations from groupoid actions, transport agreement |
| `Subgroups.existsStandardRealization` | Realize arbitrary subgroups as pointed connected covers on path-connected locally path-connected semilocally simply connected bases |
| `Comparison.pointedClassification` / `uniquePointedMap` | Pointed isomorphisms from equal stabilizers, unique maps |
| `Comparison.unpointedClassification` | Unpointed connected covers classified by subgroup conjugacy |
| `Subgroups.existsUniversalCover` / `Comparison.universalLifting` | Simply connected universal covers, maps to other covers through prescribed points |
| `Projection.Deck.normalizerQuotient` / `normalCoverCriterion` | Deck groups/normalizer quotients, regular-cover criteria |

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

[Build and check](../../USAGE.md) from the repository root:

```sh
ref-type/target/debug/cli libs/topology/coverings --module covering_spaces
```
