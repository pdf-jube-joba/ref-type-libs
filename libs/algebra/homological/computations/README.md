# `homological_algebra`

Homology computations for finite integer complexes, natural universal-coefficient/integral-Künneth short exact sequences.

Inputs are bounded finite-free integer complexes; comparison maps retain canonical inclusions/projections and their actions on computed generators.

| Entry | Purpose |
| --- | --- |
| `Finite.Pair.Of` | Isomorphisms from boundary images inside kernels to Smith-coordinate cokernels |
| `Finite.Compute.Run` | Two-stage Smith computations, free ranks/diagonal factors/generator and inverse-coordinate matrices |
| `Finite.Pair.Of.Result` | Cycle-quotient/cyclic-module-product round trips, generator formulas |
| `Finite.Bounded.Of.At` / `Of.Dual` | Integer-graded homology / cohomology by transpose |
| `Of.BasisChange.With` / `Mapping.At.With` | Basis changes, chain maps, agreement of computed coordinate matrices with induced maps |
| `UniversalCoefficient.CohomologyKernel.sequence` | Ext¹/cohomology/Hom short exact sequences |
| `UniversalCoefficient.Tensor.Projection.Exactness.Derived.sequence` | Tensor/coefficient-homology/Tor₁ short exact sequences |
| `Finite.Bounded.Mapping.At.With.UniversalCoefficient.On` / `TensorUniversalCoefficient.On` | Full short-exact naturality for complex/coefficient maps |
| `Kunneth.Integer.Theorem.At.sequence` | Integral Künneth short exact sequences with canonical external products and Tor projections |
| `Theorem.At.selectedSplitting` / `smithSplitting` | Chosen splittings and direct-sum Smith-coordinate presentations |
| `Theorem.Mapping.With.At.diagram` | Short-exact naturality for maps on both factors |
| `Kunneth.Integer.Assertions` | Universally quantified exactness, naturality, and splitting theorems |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../../USAGE.md)
