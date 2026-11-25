# `puppe_sequences`

CW cofibrations, iterated pointed cofibers/suspension comparisons, quotient comparisons, contravariant Hom exactness.

APIs are under `Puppe`. Cone base time is zero and apex time is one; successor comparisons include suspension time reversal.

| Entry | Purpose |
| --- | --- |
| `Cofibration.fromExtension` | Cylinder-gluing retractions from existing homotopy extension |
| `Disk.Boundary.cofibration` | All-dimensional disk-boundary cofibrations |
| `CW.Subcomplex.cofibration` | Finite-CW subcomplex cofibrations via boundary extension/skeleton induction |
| `Maps` | Pointed homotopies/quotients, pre/postcomposition |
| `ReducedCone`, `Cone`, `Suspension` | Pointed cones/mapping cones/reduced suspensions, continuous induced maps |
| `Cone.Exactness.exact` | Kernel/image equality in \([C_f,Z]\to[B,Z]\to[A,Z]\) |
| `Cone.Connecting`, `Cone.Morphisms.Of` | Connecting maps, pair-square induced maps/naturality |
| `Cone.Iteration.Inverse.equivalence` | \(C_{B\to C_f}\simeq\Sigma A\), actual projections/inverses/both pointed homotopies |
| `Cone.Iteration.Successor.homotopy` | Next connecting maps compared with time-reversed \(\Sigma f\) |
| `Cone.Iteration.Exactness.exact` | Exact \([\Sigma A,Z]\to[C_f,Z]\to[B,Z]\) |
| `Pair.equivalence` | Mapping-cone/quotient comparison equivalences for cofibrations |
| `CW.Subcomplex.Pointed.equivalence` | Quotient comparison for basepoint-containing finite CW subcomplexes |
| `Sequence.Of.At` | Iterated natural cofiber stages/suspension comparisons, `Hom.exact`, `Hom.connectingExact` |
| `Sequence.Natural` | Inductive stagewise commuting diagrams from pair maps |
| `Equivalence.Contravariant` | Inverse contravariant homotopy-class maps from equivalences |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/topology/puppe_sequences.md)
