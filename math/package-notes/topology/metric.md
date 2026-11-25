# Metric spaces and real continuous functions

Construction details and records for [metric_spaces](../../../libs/topology/metric/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Metric topology, metrization, real line/functions, finite partitions of unity.

## Finite partitions of unity

`existsPartition` in `metric_spaces.PartitionOfUnity.Of[source := ..., family := ...].Construction` proves `Partition` exists from compact Hausdorffness/open covers.
`Partition.parts` is finite lists; each `Entry` has cover opens, continuous unit-interval functions, support-containment proofs.
`Partition.total` means pointwise weights sum to \(1\).
Supports close nonzero loci.

Choose finitely many normality bumps \(f_i\); construct weights by

\[
\varphi_i=f_i\prod_{j>i}(1-f_j)
\]

Some bump equals \(1\) at every point, giving unit total weight.
Nonnegativity/continuity/support containment persist through construction.
