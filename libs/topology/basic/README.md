# Point-set topology

Topologies/subspaces, continuous maps, compactness, separation.

| Module | Public contents |
| --- | --- |
| `Structures` | Shared topology data/laws/types parameterized by carriers. |
| `Topology` | Topologies/generated topologies, open covers, compactness/separation. |
| `Topology.Ext` / `IndexedIntersections` | Extensionality by open families, open/closed finite-coordinate conditions. |
| `Topology.Subspace` | Subspace topology, ambient-open representations of subspace opens. |
| `Topology.Subspace.Properties` / `metric_spaces.MetricSpace.Topology.Hausdorff` | Subspace compactness/Hausdorffness, metric Hausdorffness. |
| `Topology.Finite` / `Topology.Closure` | Finite intersections/closed unions, closures/minimality. |
| `Topology.Interior` | Open interiors, inclusion, maximality of contained opens. |
| `Topology.Compactness` | Empty/singleton/union compactness, closed subsets, Hausdorff compact-closedness, compact-Hausdorff normality. |
| `Compactness` | Continuous compact images, compact codomains of continuous surjections. |
| `Continuity.closedPreimage` | Closed preimages under continuous maps. |
| `Continuity.Covers.pullback` | Pullbacks of whole-space open covers. |
| `Topology.OpenCovers` | Carriers retaining open-cover families and coverage. |
| `Homeomorphism` | Homeomorphisms, inverses, composition. |
| `LocallyCompact` | Compact neighborhoods, local compactness, compact implies locally compact. |


`Maps.Separate` separates points with different images in Hausdorff targets.
`Continuity.Covered` derives global continuity from open-cover restrictions.
`Retract.On.With` constructs image-subspace homeomorphisms from continuous inclusions/left inverses.
