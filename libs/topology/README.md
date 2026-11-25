# Topology

From topology/homotopy foundations to singular theories and concrete space computations.
Direct dependencies: each `ref.toml`; full check targets: [libs/ref.toml](../ref.toml).

| Location | Contents |
| --- | --- |
| [basic](basic/README.md) | Spaces/subspaces, continuity, compactness, separation |
| [metric](metric/README.md) | Metrics, metrization, real line, partitions of unity |
| [constructions](constructions/README.md) | Products, quotients, coproducts, gluing, compact-open topology |
| [algebra](algebra/README.md) | Topological algebra, coordinate/matrix topologies |
| [thom_spaces](thom_spaces/README.md) | Disk/sphere bundles, Thom quotients, metric/suspension/sum comparisons, finite CW pair types, relative singular theory |
| [cohomology_thom](cohomology_thom/README.md) | Relative Thom products/zero sections, fiber restrictions, standard-disk generators |
| [homotopy](homotopy/README.md) | Homotopies, pointed quotients, mapping cones, CW pairs/standard simplices |
| [singular](singular/README.md) | Singular chains/cochains, excision, products, finite-model comparisons |
| [spheres](spheres/README.md) | Sphere orientations, reflection/circle-power degrees |
| [examples](examples/README.md) | Examples on characteristic spaces and finite models |

Package names are specified by `name` in `ref.toml`, independently of paths.
For example, refer to `singular/cohomology` as `singular_cohomology` and `homotopy` as `algebraic_topology`.

Fundamental groups/coverings: [fundamental](fundamental/README.md) and [coverings](coverings/README.md).

CW-subcomplex homotopy extension, iterated pointed cofibers, and contravariant Hom exactness: [puppe_sequences](puppe_sequences/README.md).
