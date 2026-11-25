# Metric spaces and real continuous functions

Metric topology, metrization, real line/functions, finite partitions of unity.

| Module | Public contents |
| --- | --- |
| `metric_spaces.MetricSpace.Compactness` / `Uniform` | Compact metric Lebesgue numbers, uniform continuity. |
| `metric_spaces.MetricSpace.Subspace` | Restricted metrics, metric/subspace topology agreement. |
| `metric_spaces.MetricSpace.Lipschitz.Between` | Uniform continuity/continuity from Lipschitz bounds. |
| `metric_spaces.MetricSpace.Sequences` / `Complete` | Cauchy sequences, preserved limits/bounds, completeness, half-contraction fixed points, sequentially closed completeness. |
| `metric_spaces.BoundedFunctions.On` | Supremum metrics/completeness for functions uniformly bounded from centers. |
| `metric_spaces.BoundedFunctions.On.Continuous` | Continuous uniform limits, complete bounded-continuous metrics. |
| `metric_spaces.RealLine.CompactIntervals` | Compact closed real intervals. |
| `metric_spaces.RealFunctions.Product` / `Lattice` / `SquareRoot` / `Reciprocal` | Continuous real products/max/min/modulus/square roots/nonzero reciprocals. |
| `metric_spaces.RealFunctions` | Local continuity, sums/differences, unit-interval products, Urysohn continuity. |
| `metric_spaces.RealFunctions.FiniteSums` | Continuous finite real sums. |
| `metric_spaces.PartitionOfUnity` | Finite compact-Hausdorff subordinate partitions. |

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
