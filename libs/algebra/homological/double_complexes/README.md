# Nonnegative chain complexes and double complexes

| Module | Contents |
| --- | --- |
| `NonnegativeChain.Over` | Nonnegative chains, maps/homotopies, homology, short exact sequences and connecting maps |
| `ZeroExtension` | Integer-degree extension by zero and homology isomorphisms |
| `Homotopy.ZeroExtension` / `Equivalence.ZeroExtension` | Zero extensions of chain homotopies/equivalences, induced homology isomorphisms |
| `SplitInjection.On` | Quotients of inclusions with degreewise linear left inverses, short/relative long exact sequences |
| `SplitInjection.On.Positive` | Comparison of nonnegative quotients and integer-zero-extended inclusion quotients |
| `ShortExact.Morphism.Straighten` | Commutative diagrams correcting comparison maps by homotopies |
| `DoubleComplex.Over.Total` | Finite first-quadrant diagonal sums, differential \(d_h+(-1)^p d_v\) |
| `Coordinates.StepAt` / `Degree` | Differential component formulas and componentwise zero criteria |
| `Concentrated` / `ConcentratedFirst` | Row/column chain isomorphisms when positive-degree terms vanish |
| `Collapse.On.Exact` / `CollapseFirst` | Total comparison isomorphisms from augmentation kernels and positive-degree exactness |
| `TensorMapping.With` / `TensorSwap` | Both-factor maps, signed \((-1)^{pq}\) swap chain isomorphisms |
| `TensorSplitSequence.With.Split` | Tensor totals of degreewise split short exact sequences |

`Collapse` uses finite induction eliminating the largest first degree on each diagonal by boundaries.
Correct signs with `SignedTranspose` to apply to horizontal exactness too.
See [applications to resolutions](../resolutions/README.md) and [integer-graded totalization](../tensor_chains/README.md).
