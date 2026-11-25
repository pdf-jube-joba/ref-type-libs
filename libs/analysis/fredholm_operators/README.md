# `fredholm_operators`

Compact-operator ideals, Atkinson equivalence, kernel/cokernel indices, index laws and local constancy.

`At` abbreviates `Space[V, space, norm].Operators[W, target, targetNorm].At[f]`, and `H` its `Hilbert[inner, targetInner]`. Indices use actual kernels and image-quotient cokernels.

| Entry | Purpose |
| --- | --- |
| `Operators.After` / `Ideal` | Compact left/right ideals, compact-difference equivalence and composition compatibility |
| `At.kernel` / `image` / `CokernelSpace` | Actual kernels/images/quotient cokernels; also `kernelClosed`, `ClosedRange` |
| `At.Parametrix` / `HasParametrix` | Candidate inverses with compact errors on both sides and their existence |
| `H.Fredholm` | Closed images and finite-dimensional kernels/cokernels |
| `H.atkinsonEquivalence` / `fredholmOfParametrix` / `atkinson` | Fredholm property from parametrices |
| `H.parametrixExists` / `FromFredholm` | Bounded parametrices with finite-rank errors from Fredholm operators |
| `At.Index.Decomposition` | Actual kernel/quotient-cokernel bases |
| `At.Index.fromDecomposition` / `independent` | Integer dimension differences from bases and basis independence |
| `H.index` / `indexFromDecomposition` | Canonical Fredholm index and computation from supplied decompositions |
| `At.Composition.Hilbert.fredholm` / `indexComposition` | Fredholm composition, \(\operatorname{ind}(gf)=\operatorname{ind}f+\operatorname{ind}g\) |
| `H.DirectSum.At.fredholm` / `indexDirectSum` | Operators on constructed Hilbert sums and direct-sum index laws |
| `H.Change.fredholm` / `H.CompactPerturbation.indexInvariant` | Fredholm/index invariance under compact perturbations |
| `H.indexLocallyConstant` | Positive operator-norm neighborhoods with constant Fredholm property/index |
| `Operators.Hilbert.Family.At.locallyConstant` | Local constancy for norm-continuous families over arbitrary topological spaces |
| `FiniteSpace` | Finite bases, unique dimension, subspaces, isomorphism transport, maps through finite spaces |
| `Sum` / `Sum.MapsTo` | Hilbert-sum inner products/norms/completeness, coordinate projections/inclusions, bounded sum maps |
| `Space.Hilbert.Trace` | Finite-rank traces, factorization independence, additivity/scaling/cyclicity |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/analysis/fredholm_operators.md)
