# K10 Compactly supported K-theory and symbol presentations

## Requirements

- Primary implementation: `compact_support_k`.
- For locally compact Hausdorff spaces, compare one-point-compactification K-groups with groups of bundle triples isomorphic outside compact sets.
- Construct disk/sphere-pair presentations, enlargement of supports, extension by zero for open embeddings, and proper pullback.
- Expose finite-complex presentations, equality criteria via homotopy/stabilization/direct sums, external products, and excision.

## Dependencies

- [K09 Bott periodicity and integer degrees](k09-bott-periodicity.md)

## ImplementationStatus

Complete.
Published general-triple `On.Triples.Group` as a generators-and-relations presentation of the free abelian group on coordinate-model triples over the original space.
Constructed `ToK` from geometric relations for global isomorphisms, bundle isomorphisms, direct sums, composition, and homotopy. Checked choice independence, relation preservation, and additivity of `Input` moving arbitrary bundles into coordinate models.
Target checks also passed for `FromCompact` extension-choice independence, preservation of four compactification generator relations, and compatibility of `Group.FromSymbols` with `ToK`.
Checked `Normalize` stabilization/descent/gluing, `Group.FromK.LeftInverse`, `Group.Comparison`, and general-triple `Group.EqualityCriterion`.
`On.Pullback.Group` and `GroupNaturality` also checked proper pullback for general-triple groups and naturality of actual bundle pullbacks.

`On.FiniteComplexes` accepts arbitrary finite bundle sequences and constructs K-classes from parity sums and contractions on compact boundaries.
Target-checked contraction and compact-neighborhood choice independence and a three-term zero-differential-complex example.
Target-checked homotopy invariance from continuous exact boundary-differential families, parity-sum bundle-isomorphism invariance from constant families, support enlargement, and direct sums.
Also target-checked stabilization by globally exact complexes and formal representatives/equality criteria from generator relations via `Of.Supported.Representatives`.
Final standard full check accepted all 10,999 targets.
Newly checked 281, reused 10,718, save failures 0, corrupt cache reads 0, exit code 0.
Checked source commit: `caf1837dd3fbb05f29b90ffb95e53af87f3d8583`.
`compact_support_k` exposes one-point compactification, integer-degree groups, proper pullback, open-subspace extension by zero, closed-pair complement presentations, disk/sphere-bundle comparisons, external products, and excision.
Compactified symbol groups have two-term bundle complexes, homotopy/stabilization/direct-sum relations, and equality criteria.

`On.BundleTriples.Supported.With` accepts arbitrary bundles on the original space and isomorphisms outside compact sets.
It does not require extending individual bundles to the one-point compactification.
Restrict to compact neighborhoods to form relative triples, then extend by zero using `On.Localization`.
`Choices.equation` proves neighborhood independence; `relative_k_theory.Relative.Pair.BundleTriples` proves independence of finite projection presentations and auxiliary complements for negative bundles.
`On.BundleTriples.To.Supported.With` compares support enlargement and changes of presentation by bundle isomorphisms.
`On.Pullback.BundleTriples.Supported.With.naturality` gives proper-pullback naturality.

`With.symbol` and `comparison` connect general triples to existing small symbol groups and one-point-compactification K-groups.
`On.Symbols.Supported.With.Raw.equation` proves restricting existing symbols to the original space and reconstructing them recovers their classes.
`On.Symbols.RawRepresentatives.existence` gives general bundle-triple representatives for every class.
`Examples.Raw` is a minimal example of equality for different compact neighborhoods.

Reduction of finite complexes to parity sums and choice independence, and general-triple group presentations/additivity/equality criteria on the original space, are proved from actual bundle maps and relation presentations respectively.
